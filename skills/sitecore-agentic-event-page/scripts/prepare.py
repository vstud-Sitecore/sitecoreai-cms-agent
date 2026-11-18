"""Validate an Event Page handoff and print its checked destination and field payload.

Uses Python's standard library only. Does not call Sitecore or modify files.
"""
import argparse
import datetime as dt
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import uuid
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

SCHEMA = Path(__file__).resolve().parents[1] / 'references' / 'schema.json'


NATIVE_REQUIRED_FIELDS = (
    'FormType', 'FormTitle', 'FormSubmitText', 'FormDefaultSalesforceCampaignID',
)
NATIVE_REGISTRATION_FIELDS = NATIVE_REQUIRED_FIELDS + (
    'FormIntroText', 'FormConfirmationMessage', 'FormRedirectURL',
    'FormDefaultProgramStatus', 'FormDefaultCampaignProducts',
)
URL_ATTRIBUTES = {'href', 'src', 'action', 'formaction', 'poster', 'xlink:href', 'cite'}


def unsupported_url(value):
    normalized = re.sub(r'[\t\r\n]', '', value).lstrip()
    return re.match(r'(?:javascript|data):', normalized, re.I) is not None


class RichTextURLs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_unsupported_url = False

    def handle_starttag(self, tag, attrs):
        if any(value and unsupported_url(value) for name, value in attrs if name in URL_ATTRIBUTES):
            self.has_unsupported_url = True


def event_instant(raw, zone, key):
    try:
        if not isinstance(raw, str) or not re.match(r'^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}', raw):
            raise ValueError()
        timestamp = raw[:-1] + '+00:00' if raw.endswith('Z') else raw
        local = dt.datetime.fromisoformat(timestamp)
    except (TypeError, ValueError) as exc:
        raise ValueError(f'{key} must be an ISO 8601 local date and time') from exc

    if local.utcoffset() is not None:
        zoned = local.astimezone(zone)
        if (zoned.replace(tzinfo=None) != local.replace(tzinfo=None)
                or zoned.utcoffset() != local.utcoffset()):
            raise ValueError(f'{key} time and offset do not match {zone.key} on that date')
        return zoned

    candidates = set()
    for fold in (0, 1):
        utc = local.replace(tzinfo=zone, fold=fold).astimezone(dt.timezone.utc)
        if utc.astimezone(zone).replace(tzinfo=None) == local:
            candidates.add(utc)
    if not candidates:
        raise ValueError(f'{key} is skipped by a clock change in {zone.key}; choose a valid local time')
    if len(candidates) > 1:
        offsets = ' or '.join(utc.astimezone(zone).isoformat() for utc in sorted(candidates))
        raise ValueError(f'{key} is ambiguous in {zone.key}; choose {offsets}')
    return next(iter(candidates)).astimezone(zone)


def prepare_schedule(data):
    zone_name = data.get('timeZone')
    if not isinstance(zone_name, str) or not zone_name:
        raise ValueError('timeZone must be an IANA timezone name')
    try:
        zone = ZoneInfo(zone_name)
    except (ValueError, ZoneInfoNotFoundError) as exc:
        raise ValueError(f'Unknown timezone {zone_name!r}. Use an IANA name and a runtime with timezone data.') from exc

    start = event_instant(data.get('start'), zone, 'start')
    end = event_instant(data.get('end'), zone, 'end')
    start_utc = start.astimezone(dt.timezone.utc)
    end_utc = end.astimezone(dt.timezone.utc)
    if end_utc <= start_utc:
        raise ValueError('end must be after start')
    return start, {
        'EventStartDateTime': start_utc.strftime('%Y%m%dT%H%M%SZ'),
        'EventEndDateTime': end_utc.strftime('%Y%m%dT%H%M%SZ'),
    }


def prepare(data, schema, *, schedule_only=False):
    if not isinstance(data, dict):
        raise ValueError('handoff must be a JSON object')
    start, date_fields = prepare_schedule(data)
    if schedule_only:
        return {'fields': [{'name': name, 'value': value} for name, value in date_fields.items()]}

    if 'intake' in data:
        intake = data['intake']
        if not isinstance(intake, dict) or not isinstance(intake.get('openQuestions', []), list):
            raise ValueError('Legacy intake must be an object with an array of openQuestions')
        if intake.get('openQuestions'):
            raise ValueError('Resolve the recorded open questions before writing to the CMS')

    fields = data.get('fields', {})
    if not isinstance(fields, dict):
        raise ValueError('fields must be an object')

    errors = []
    name = data.get('pageName')
    if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        errors.append('pageName must be a lowercase URL slug with hyphens')
    language = data.get('language')
    if not isinstance(language, str) or not language.strip():
        errors.append('language is required')
    parent = schema['rootPath'] + start.strftime('/%Y/%m')
    fields = {**fields, **date_fields}
    invalid = [key for key, value in fields.items() if value is not None and not isinstance(value, str)]
    if invalid:
        errors.extend(key + ' must be a string or null' for key in invalid)
        raise ValueError('\n'.join(errors))

    manifest = {name: kind for section in schema['sections'] for name, kind in section['fields'].items()}
    for key, value in fields.items():
        if key not in manifest:
            errors.append('Unknown field: ' + key)
            continue
        if value is None:
            continue
        kind = manifest[key]
        if kind in ('single-line text', 'multi-line text') and re.search(r'<[^>]+>', value):
            errors.append(key + ' cannot contain HTML')
        if kind == 'checkbox' and value not in ('', '0', '1'):
            errors.append(key + ' must be 1 or blank/0')
        if kind in ('droplink', 'treelistex') and value:
            try:
                for part in value.split('|'):
                    uuid.UUID(part.strip('{}'))
                if kind == 'droplink' and '|' in value:
                    raise ValueError()
            except ValueError:
                errors.append(key + ' requires existing item GUIDs, not display labels')
        if kind in ('image', 'general link') and value:
            try:
                root = ET.fromstring(value)
                if root.tag != ('image' if kind == 'image' else 'link'):
                    raise ValueError()
                if kind == 'image':
                    if root.get('mediaid'):
                        uuid.UUID(root.get('mediaid').strip('{}'))
                    elif not re.match(r'^https?://[^/\s]+', root.get('src', '')) or root.get('dam-content-type') != 'Image':
                        errors.append(key + ' requires an actual mediaid or public image src plus dam-content-type=Image; other image metadata is optional')
                if kind == 'general link' and not (root.get('url') or root.get('anchor') or root.get('id')):
                    raise ValueError()
                if any(unsupported_url(root.get(attr, '')) for attr in ('url', 'src', 'thumbnailsrc')):
                    errors.append(key + ' contains an unsupported URL scheme')
            except (ET.ParseError, ValueError):
                errors.append(key + ' requires valid Sitecore image/link XML')
        if (key == 'RetargetingUrl' or re.fullmatch(r'Speaker[1-9]SocialLink', key)) and unsupported_url(value):
            errors.append(key + ' contains an unsupported URL scheme')
        if kind == 'rich text' and value:
            parser = RichTextURLs()
            parser.feed(value)
            parser.close()
            if parser.has_unsupported_url:
                errors.append(key + ' contains an unsupported URL scheme')
    for key in ('EventHeroHeading', 'EventHeroSubheading'):
        if not fields.get(key):
            errors.append(key + ' is required for a build-ready event brief')
    for i in range(1, 7):
        if bool(fields.get('EventKeyPointHeading' + str(i))) != bool(fields.get('EventKeyPoint' + str(i))):
            errors.append('Takeaway ' + str(i) + ' requires a heading and body together')
    for i in range(1, 9):
        if bool(fields.get('EventFAQQuestion' + str(i))) != bool(fields.get('EventFAQAnswer' + str(i))):
            errors.append('FAQ ' + str(i) + ' requires a question and answer together')
    for i in range(1, 10):
        prefix = 'Speaker' + str(i)
        if any(value for key, value in fields.items() if key.startswith(prefix)) and not fields.get(prefix + 'Name'):
            errors.append(prefix + ' requires a name to display')
    if fields.get('EventOverviewImage') and (fields.get('EventOverviewQuote') or fields.get('EventOverviewQuoteTagline')):
        errors.append('Overview must use either image or quote/tagline')
    if fields.get('EventOverviewQuoteTagline') and not fields.get('EventOverviewQuote'):
        errors.append('Overview attribution needs a quote')
    mode = data.get('registrationMode')
    if mode == 'native':
        for key in NATIVE_REQUIRED_FIELDS:
            if not (fields.get(key) or '').strip():
                errors.append(key + ' is required for native registration')
        if not (fields.get('FormConfirmationMessage') or fields.get('FormRedirectURL')):
            errors.append('Native registration needs a confirmation or redirect')
    elif mode == 'external':
        conflicting_fields = [name for name in NATIVE_REGISTRATION_FIELDS if (fields.get(name) or '').strip()]
        if conflicting_fields:
            errors.append('External registration cannot include native form settings: ' + ', '.join(conflicting_fields))
        if not fields.get('EventCTAButton') or not fields.get('EventCTAButtonText'):
            errors.append('External registration needs a CTA link and label')
        else:
            try:
                link = ET.fromstring(fields['EventCTAButton'])
                if link.get('linktype') != 'external' or not re.match(r'^https?://[^/\s]+', link.get('url', '')):
                    errors.append('External registration requires an HTTP(S) external CTA URL')
            except ET.ParseError:
                pass  # The field XML check above reports the malformed link.
    else:
        errors.append('registrationMode must be native or external')
    if fields.get('EventCTAButton') and not fields.get('EventCTAButtonText'):
        errors.append('CTA link requires button text')
    if errors:
        raise ValueError('\n'.join(errors))
    return {'parentPath': parent, 'pagePath': parent + '/' + name,
            'createPage': {'name': name, 'language': data['language'], 'templateId': schema['templateId']},
            'fields': [{'name': k, 'value': v} for k, v in fields.items() if v is not None]}


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('handoff', type=Path)
    parser.add_argument('--schedule-only', action='store_true', help='Output UTC date fields for an existing event')
    args = parser.parse_args()
    try:
        output = prepare(json.loads(args.handoff.read_text(encoding='utf-8-sig')),
                         json.loads(SCHEMA.read_text(encoding='utf-8')),
                         schedule_only=args.schedule_only)
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

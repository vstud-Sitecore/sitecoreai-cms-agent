"""Validate an Event Page handoff and print its checked destination and field payload.

Uses Python's standard library only. Does not call Sitecore or modify files.
"""
import argparse
import datetime as dt
import json
from pathlib import Path
import re
import sys
import uuid
import xml.etree.ElementTree as ET

SCHEMA = Path(__file__).resolve().parents[1] / 'references' / 'schema.json'


def prepare(data, schema):
    errors = []
    fields = data.get('fields', {})
    if not isinstance(fields, dict):
        raise ValueError('fields must be an object')
    name = data.get('pageName', '')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        errors.append('pageName must be a lowercase URL slug with hyphens')
    if not data.get('language'):
        errors.append('language is required')
    if not data.get('timeZone'):
        errors.append('timeZone is required; record the event timezone separately from its offset')
    schedule = []
    for key in ('start', 'end'):
        try:
            value = dt.datetime.fromisoformat(data.get(key, '').replace('Z', '+00:00'))
            if value.utcoffset() is None:
                raise ValueError()
            schedule.append(value)
        except (ValueError, TypeError):
            errors.append(key + ' must be ISO 8601 with an explicit offset')
    parent = None
    if len(schedule) == 2:
        if schedule[1] <= schedule[0]:
            errors.append('end must be after start')
        parent = schema['rootPath'] + schedule[0].strftime('/%Y/%m')
        if data.get('destinationParent') != parent:
            errors.append('destinationParent must match the event-local start year/month: ' + parent)
        for key, value in zip(('EventStartDateTime', 'EventEndDateTime'), schedule):
            expected = value.astimezone(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
            if fields.get(key) != expected:
                errors.append(key + ' must equal the converted UTC value ' + expected)
    manifest = {f['name']: f['type'] for s in schema['sections'] for f in s['fields']}
    for key, value in fields.items():
        if key not in manifest:
            errors.append('Unknown field: ' + key)
            continue
        if value is None:
            continue
        kind = manifest[key]
        if not isinstance(value, str):
            errors.append(key + ' must be a string or null')
            continue
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
                    elif not all(root.get(attr) for attr in
                                 ('src', 'dam-id', 'dam-content-type', 'width', 'height', 'thumbnailsrc')):
                        errors.append(key + ' requires complete verified DAM image XML; src-only is unsupported in WWW')
                    if key == 'OpenGraphImage':
                        image_name = root.get('filename', '') or root.get('src', '').split('?')[0]
                        extension = Path(image_name).suffix.lower()
                        if extension and extension not in ('.png', '.jpg', '.jpeg'):
                            errors.append('OpenGraphImage requires JPEG or PNG')
                if kind == 'general link' and not (root.get('url') or root.get('anchor') or root.get('id')):
                    raise ValueError()
            except (ET.ParseError, ValueError):
                errors.append(key + ' requires valid Sitecore image/link XML')
        if re.search(r'(?:javascript|data):', value, re.I):
            errors.append(key + ' contains an unsupported URL scheme')
    for key in ('EventHeroHeading', 'EventHeroSubheading', 'EventStartDateTime', 'EventEndDateTime'):
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
        for key in ('FormType', 'FormTitle', 'FormSubmitText', 'FormDefaultSalesforceCampaignID'):
            if not fields.get(key):
                errors.append(key + ' is required for native registration')
        if not (fields.get('FormConfirmationMessage') or fields.get('FormRedirectURL')):
            errors.append('Native registration needs a confirmation or redirect')
    elif mode == 'external':
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
    args = parser.parse_args()
    try:
        output = prepare(json.loads(args.handoff.read_text(encoding='utf-8-sig')),
                         json.loads(SCHEMA.read_text(encoding='utf-8')))
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

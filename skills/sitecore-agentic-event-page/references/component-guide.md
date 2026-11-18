# Agentic Event Page component guide

The [field manifest](schema.json) contains verified WWW template and folder IDs, exact field names and types, and registration references. Read the sections relevant to the task. Revalidate the live template if it differs.

## Rendering

- The template inherits Hero, Audience, Overview, Takeaways, Agenda, Speakers, FAQ and CTA. Registration fields are inherited on the page item. Blank fields may leave an empty rendering, so inspect the preview.
- Overview takes an image or a quote with optional attribution. Takeaways require matching headings and bodies (up to six). Speakers need real names (up to nine). For omitted details, use the [People lookup](../../../references/content-fields.md#named-speakers) and map the verified profile to the matching `SpeakerN*` fields. FAQ questions and answers come in pairs (up to eight).
- Use an HTML table in `EventAgendaTimetable`. Paired asterisks mark highlights in `EventHeroHeading`, `EventOverviewHeading`, `EventTakeawaysHeading`, `EventAgendaHeading`, `SpeakersHeading` and `EventFAQHeading`. These headings remain plain text.
- Prefer a linked venue name in `EventLocation` and its address in `EventLocationTagline`. Use public attendance details for virtual events.
- For `OpenGraphImage`, prefer a public JPEG or PNG rendition when selecting an asset for broad social preview compatibility. Preserve supplied images, including WebP. Apply an explicit platform restriction only when it is documented for the intended channel, or offer an alternate rendition if that channel’s preview fails. Follow the [shared image rules](../../../references/content-fields.md#images).
- Use valid JSON-LD in `JsonLdMarkup` without a script tag. Keep metadata consistent with confirmed event facts. `NoIndexNoFollow=1` requests noindex/nofollow. Resolve live taxonomy and ownership references.

## Registration

For native registration use the confirmed form type, exact Salesforce campaign ID confirmed for this event, title, submit label and confirmation message or redirect. Follow the [gap-filling rules](../../../references/content-fields.md#fill-gaps-during-a-page-build) for missing copy. A native event build requires its own confirmed campaign ID. Resolve form type, program status and campaign product IDs from the live field sources in the manifest. Program status and campaign product depend on the event. Preserve inherited privacy, consent, CSRF and captcha settings. For external registration use the confirmed public URL and CTA label. Leave native form settings out of the payload. Before writing, determine how the inherited native form will be suppressed if the layout still renders it. Use supported page settings or presentation with any required confirmation.

General link examples are `<link linktype="external" url="https://example.com/register" text="Register" />` and `<link linktype="anchor" anchor="event-form" text="Register" />`. Check the rendered link and form target.

## Handoff

For a new page supply a JSON object with `pageName` (lowercase hyphenated slug), `language`, `timeZone` (IANA timezone name, for example `Europe/London`), `start` and `end` (event-local ISO date and time, with an optional explicit offset to disambiguate a clock change), `registrationMode` (`native` or `external`), and `fields` (exact CMS field names with string values or null). See [field rules](../../../references/content-fields.md) for formatting. Keep source notes and confirmed decisions in the mapping, outside the field payload.

Run `python3 scripts/prepare.py <handoff.json>` from this skill directory, using a Python 3 runtime with IANA timezone data. The helper derives the offsets, event-local parent path and UTC date fields from the named timezone. It validates the field payload and returns the proposed paths, creation inputs and field array. For a repeated local time, it returns both valid offsets so the intended instant can be confirmed. For a skipped local time, confirm a valid time. Older handoffs may carry a parent path and computed UTC values. The helper derives both from the confirmed schedule. It also rejects explicitly open questions in an older handoff.

For an existing event's schedule change use `python3 scripts/prepare.py --schedule-only <handoff.json>` with `timeZone`, `start` and `end`. The helper outputs the two UTC date fields. Patch only fields the change affects and preserve the existing page path.

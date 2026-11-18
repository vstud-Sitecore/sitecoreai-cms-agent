---
name: sitecore-agentic-event-page
description: Build or update a Draft Sitecore Agentic Event Page from an event brief or mapping, including when the user asks to continue after mapping. Creates new pages under Events Webinars/YYYY/MM.
---

# Build or update an Agentic Event Page

Use the [event component guide](references/component-guide.md) and [field manifest](references/schema.json) for the template. Use the [shared Draft workflow](../../references/draft-workflow.md) and [content field rules](../../references/content-fields.md) for CMS writes. Read the supplied brief or existing mapping and apply the [gap-filling and speaker lookup rules](../../references/content-fields.md#fill-gaps-during-a-page-build) before asking for details or preparing the handoff.

## Prepare a new event

Before writing, resolve the required facts and choices from the brief and conversation. Ask only for missing or conflicting decisions in one concise round.

- **Event and schedule** — title, purpose and audience, confirmed start/end local date and time with named timezone, and online, in-person or hybrid format with public location or attendance details.
- **Page and content** — Use the supplied language and slug, or choose a clear slug when the user has delegated the build and given no preference. Use supplied copy or draft from confirmed facts. Fill supported fields when grounded in the brief or verified content, including missing metadata and speaker details. Leave optional sections empty when there is no grounded content. Use approved quotes and keep private joining links out of public content.
- **Registration** — native or external. For native, use the exact Salesforce campaign ID supplied or explicitly confirmed for this event. If it is missing or conflicting, ask before building. Never infer, generate, borrow or substitute another campaign ID. Resolve the verified form type and submit text. Draft the thank-you message from the page content when both confirmation copy and a redirect are absent. Use the verified Event form type default when accepted or delegated. For external, use the exact public URL and label and resolve any inherited native form before writing, as described in the component guide.
- **Assets and discovery** — Use supplied public DAM links or choose approved assets when authorized. Leave unspecified optional slots empty. Resolve search visibility, ownership and taxonomy from the brief or existing site defaults. Ask about material choices that remain unresolved.

Keep the decisions and campaign ID source in the readable mapping and show a concise build summary. Proceed when the build is authorized and required decisions are settled. Normalize the mapping into the [handoff format](references/component-guide.md#handoff) and run `python3 scripts/prepare.py <handoff.json>` from this skill directory before the first CMS write. Use the host's Python 3 runtime when needed.

## Create under the event-local month

Use WWW and the IDs and paths in [the field manifest](references/schema.json). Verify the event template, root and target environment. Resolve the exact year and two-digit month paths printed by the helper. Reuse existing folders with the verified Folder template. If one is absent, create only the needed folder under its exact parent. Reread the exact path after uncertain writes. A non-folder at that path or an unrelated page collision needs resolution before proceeding.

Use the exact month folder ID for creation and the validator's field payload for population. Use the inherited page design and renderings. Verify with `get_components_on_page` before considering any presentation changes. Keep inherited privacy, consent, security and tracking settings. If an unused section still renders, follow the connector's confirmation requirement before removing its page-specific instance.

## Edit an existing event

Resolve the page, language and affected settings. Preserve its route and scheduled instants unless the user requests the corresponding changes. Ask only for missing facts that affect the edit. Apply the [shared Draft workflow](../../references/draft-workflow.md#writing-and-verifying-a-sitecore-draft) to write the changed fields and verify the affected preview. For assets and other independent field edits use the [general editing workflow](../sitecore-edit-content/SKILL.md). For schedule changes, reconcile the updated schedule with retained times and use the validator's schedule-only mode to derive the UTC values for the changed date fields. For registration or paired fields, check the changed and retained values together against the component guide. A date change by itself does not move the existing page.

## Verify and deliver

Use `get_page_preview_url` or the route returned by `get_components_on_page` with a verified preview host. Check the actual event-local date and clock time, visible sections, images, venue and registration. If stored UTC times render as local clock times, preserve the correct UTC values, set `HideTimeDetails=1` when needed and show the agreed local hours and timezone in `EventDateTagline`. Verify the result.

For native registration, confirm the visible submit control, campaign, confirmation or redirect, and `#event-form` target if used. For external registration, verify the exact public link and label and address any unwanted inherited form. Lead the handoff with clickable **Edit in Sitecore** and **Preview** links using the [shared link instructions](../../references/draft-workflow.md#preview-and-editor-links). Include the CMS path, any saved handoff, and specific verification gaps. Finish with the [Salesforce campaign ID report](../../references/draft-workflow.md#campaign-id-in-the-build-summary).

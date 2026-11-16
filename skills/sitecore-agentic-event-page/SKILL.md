---
name: sitecore-agentic-event-page
description: Build or update a Draft Sitecore Agentic Event Page from an event mapping or brief, using template 93b92c2a-70a7-4c5c-9f55-abc5003201e2 under Events Webinars/YYYY/MM. Use when the user requests the Sitecore event-page build, including continue after its content mapping.
---

# Build an Agentic Event Page in Sitecore

Use the tools bundled with the **SitecoreAI CMS Agent** plugin. Follow live tool schemas; the workflow below uses their short names. Do not configure another MCP server. If a tool reports expired credentials or authentication required, follow the bundled `sitecore-cms-agent` recovery skill and the host's native reconnect flow. Missing tools alone do not establish an authentication failure. This builder leaves pages in Draft and does not publish them. Read [the component guide](references/component-guide.md) and [the supported field schema](references/schema.json). An event build requires its event details, not a target account relationship questionnaire. Accept an existing event mapping or a supplied event brief. If the optional `agentic-event-page-guide` skill is installed, it can prepare the mapping; it is not a required plugin dependency. Otherwise map supplied content to the bundled field reference, preserve the user's copy and collect only missing essentials. Keep generated mapping/handoff files in the user's requested workspace; follow its AGENTS.md output rules.

## Event brief and handoff

Read the complete supplied document, including image guidance, form settings and production notes. Ask together for missing event title, start/end dates and times, named event timezone, language, location/format, registration route and campaign ID when needed. "Your local time" needs an explicit timezone decision; do not assume it means the chat timezone or every visitor's timezone. Use provided dates rather than dates from a previous demo. Do not invent speakers, quotes, sponsorships, availability, campaign IDs or assets. User-requested sample data must be labeled as a demo and remain unpublished.

The component guide specifies the JSON handoff keys. Normalize a Markdown mapping into that handoff before validation. Save exact field values separately from sources and production notes; preserve null as skip and an empty string as an explicit clear. Use the source document's registration type when it maps to a verified CMS option. Resolve a generic label such as "General form" against real options and the relevant existing event configuration, rather than writing the label into a reference field. The verified Event form type is a default only when the intended form remains unspecified. Use the supplied campaign ID and confirmation/redirect; do not borrow an ABM campaign or invent a live campaign.

## Verified template and destination

- Site: WWW.
- Template: /sitecore/templates/Project/Marketing/WWW/Agentic Event Page, ID 93b92c2a-70a7-4c5c-9f55-abc5003201e2.
- Required root: /sitecore/content/Marketing/WWW/Home/Resources/Events Webinars, ID 778f8ead-0351-484f-b664-88d3f9a2610b.
- Standard folder template: a87a00b1-e6db-45ab-8b54-636fec3b5523.
- Expected inherited Page Design: a412962f-3abb-4aae-8b8c-f815ac9956dd (Logo Event Only). Preserve the template's standard values and configured presentation.

Validate the handoff with `python scripts/prepare.py '<handoff.json>'` using Python 3. If Python is not on PATH, use the host's bundled runtime discovery capability when available. This helper needs no third-party packages and performs no network or CMS writes. Resolve any needed field reference IDs and asset IDs through the live connector. Recheck template identity and root path before creation. Revalidate the schema if the live template has changed. The template field endpoint and child lists truncate at 50; use base templates or exact section/field paths for missing fields. A missing field in a truncated result is not proof that the field does not exist.

## Resolve the real year/month parent

1. Use the event's start date in its event timezone, not the current date and not the UTC-converted date. A start of 2027-01-01T00:30:00+14:00 belongs in 2027/01 even though its UTC instant is in December 2026.
2. Read the exact root with get_content_item_by_path. Then resolve root/YYYY and root/YYYY/MM by exact paths with failOnNotFound:false. Always use two-digit months 01 through 12. Existing 2026 folders 01 through 12 were verified on 2026-10-29; refresh the actual IDs, do not hard-code month IDs.
3. Reuse existing year and month folders. Check their full paths and Folder template. If absent, create only the needed year/month folder with create_content_item, using the verified Folder template and actual parent IDs. Before a retry, reread the exact path to avoid duplicates. A path occupied by a non-folder is a blocker, not permission to delete or replace it.
4. The page parentId must be the ID returned for the exact month folder. Never use the Events Webinars root, the year folder, built-for, a test folder or a parallel Events Webinars tree as the page parent. Never copy example pages as a shortcut.
5. Preflight the full month/page-slug path. If an existing item is present, use it only when the user has requested updating/continuing that page. Otherwise clarify the collision before writing. Do not overwrite an unrelated page or make a duplicate with a guessed suffix.

## Images and event-local time

For media-library images use a verified media GUID. For Content Hub DAM images, copy the full verified image XML with src, dam-id, dam-content-type, width, height and thumbnailsrc. A bare src-only image produces an empty image in WWW. A public delivery URL from CSS or a design document is not a complete asset reference. Do not manufacture an asset ID or combine one asset's DAM metadata with another image URL. If the approved asset cannot be resolved, disclose the missing image; use a verified placeholder only when appropriate to the user's draft request. OpenGraphImage requires JPEG or PNG.

Store correct UTC datetime values while keeping the confirmed event-local date/time and timezone in the mapping. Check the actual preview: the WWW event template has previously displayed stored UTC clock times without the desired local conversion. Do not change the real event time or its timezone to fit that rendering. If this recurs, suppress the conflicting generated time with HideTimeDetails=1 and display the agreed local hours with an explicit timezone in EventDateTagline, confirming the result in preview. This workaround does not implement automatic per-visitor timezone conversion.

## Create and populate

Call create_page with the resolved month parentId, the event template ID, approved page slug and language; omit fields on creation. Retain the returned item ID and full path. After any uncertain creation result, read the exact path before retrying. Confirm the returned template and destination before populating. Do not move/delete a mistakenly created item automatically; report and resolve the mismatch.

Use update_fields_on_item with arrays of name/value pairs in manageable batches, grouping hero/details, content sections, images, registration and metadata. The preparer prints a field payload. null means no write; empty string is an explicit clear. If one field fails, inspect its definition and retry only the affected batch after determining whether changes committed. Do not create a second page to work around a field error.

Respect live datatypes: plain text for single/multi-line text; HTML for rich text; Sitecore image XML for images; Sitecore link XML for general links; existing item GUIDs for droplinks; pipe-separated GUIDs for treelistex; 1 or blank for checkbox; UTC yyyyMMddTHHmmssZ for datetimes. Preserve intentional paired asterisks in supported headings. Do not write display labels such as Event into FormType; resolve its dropdown reference. Do not change DisableCSRF, ReCaptcha, privacy/consent links or other security/tracking defaults to make a form work.

The page's inherited renderings consume fields on the page item; no new datasource is normally needed. Check get_components_on_page rather than adding duplicate components. Leave unused numbered fields blank. This alone does not prove an entire section is hidden. If a whole unused section still renders, identify that page's actual component instance and follow the connector's explicit confirmation requirement for removing it, or give the user the exact Presentation > Details step. Do not alter the shared template or its standard values.

## Verify and deliver

Read back the created page's exact path, template, workflow and critical fields. Reads may omit fields because of the 50-field limit; use rendered HTML/preview or targeted inspection rather than calling empty values success or repeatedly writing all fields. Check get_components_on_page for inherited structure. Obtain the preview via get_page_preview_url or the route returned by get_components_on_page plus a verified preview host; never construct an events URL by blindly slugifying the CMS folder name Events Webinars.

Inspect the preview (rendered HTML, screenshot or browser) for event-local dates/times, venue, used/unused entries, overview image-versus-quote, agenda table, images, mobile layout where available, and registration. For native forms verify a visible enabled submit control with the agreed label, correct form/campaign settings, and the confirmation/redirect configuration. Verify #event-form targets an actual form when used. For external registration verify its exact URL and label and resolve any unwanted inherited native form. Do not submit a real registration as a test without user authorization.

Leave the page in Draft, without publication or workflow approval. Read workflow state using get_content_item_by_id: path reads have returned null workflow/version even when the ID read shows Draft. If a new page has no workflow assigned, resolve the intended site's content workflow and its non-final Draft state, then assign those verified __Workflow and __Workflow state values only on the new page and read back by ID. Never assign an approval/final state or edit the shared workflow/template. Report unresolved workflow state instead of claiming Draft without evidence. Return the clickable preview, full CMS path, saved mapping/handoff, and any specific incomplete verification. Only claim the form works end to end if an authorized submission was actually tested. This skill's creation is not a live build test: the caller must perform these checks for each real event.

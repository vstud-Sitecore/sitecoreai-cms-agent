# Writing Sitecore content fields

Look up the exact field and owning page item or datasource, site, and language. Use the live field definition when the template reference is incomplete. Template and child lists may truncate at 50; inspect base templates or exact paths for missing entries.

Use plain text for text fields, HTML for rich text, Sitecore link XML for general links, GUIDs for droplinks, pipe-separated GUIDs for treelists, and `1` or a clear value for checkboxes. Omit skipped fields. An empty string explicitly clears a field. Follow live tool schemas.

## Fill gaps during a page build

Preserve supplied values and intentional omissions. Before asking a question or skipping an unspecified field, use the approved brief, page copy, verified Sitecore content or the documented template defaults to fill gaps that have a clear answer. For an existing page, preserve populated fields outside the requested changes. Ask only for unresolved facts or decisions required for the work.

- **Metadata:** Draft missing SEO and social titles and descriptions from the final page’s headline, subject and audience. Fill supported keywords where appropriate and use confirmed facts for any applicable structured data. Keep the copy concise and in the page language. Resolve ownership, taxonomy, indexing and other settings from verified choices or documented defaults.
- **Form confirmation:** When an included native form supports a thank-you message and the brief supplies neither one nor a redirect, write `FormConfirmationMessage` as short rich text that thanks the reader for the specific action. Mention next steps only if confirmed. Preserve a supplied message or redirect and any configured redirect on an existing page. Leave this field out for external registration.
- **Operational details:** Require a trusted, event-specific source for campaign IDs and other operational details such as registration destinations and event logistics. Apply documented defaults only where the page type permits them.

## Named speakers

For each named speaker with missing details, look under `/sitecore/content/Marketing/WWW/Data/People` before leaving those fields blank. The folder has alphabetical subfolders. Use `get_content_item_by_path` with the speaker’s full name under the matching letter as a starting point. If the exact path misses, inspect relevant folders for naming variants. Child lists can be truncated. Read the matched profile in the page language and verify the full name against the supplied context, such as employer or role. If several profiles remain plausible, leave the unresolved details blank and flag them.

For matching Person items, use `Name`, `JobTitle`, `Company`, `Info` and `Image` as the sources for speaker name, role, company, bio and headshot. For a plain-text social URL field, extract the verified public URL from the relevant profile link, such as `LinkedinLink`, rather than copying link XML. Map only supported fields, preserve details already supplied and leave any unsupported or unverified details blank. Use existing image references in the supported field format.

## Images

For any image field, including images in a full build, use the supplied public delivery URL directly as `<image src="PUBLIC_URL" dam-content-type="Image" />`. XML-escape all attributes and retain the exact URL and query parameters. Add accurate same-asset information already available, such as DAM ID, alt text, dimensions, thumbnail, or filename. Optional metadata needs neither a question nor a lookup. Use accurate alt text when available or when the image clearly supports a concise description. Preserve an explicitly selected native Sitecore Media Library reference as `<image mediaid="{GUID}" />`. Follow the [ABM icon rules](../skills/sitecore-abm-page/references/component-kit.md#media-slot-rules) and the [event social-preview guidance](../skills/sitecore-agentic-event-page/references/component-guide.md#rendering) for those slots.

When a public URL or native GUID is supplied, use it directly. When selecting an authorized image, resolving a named asset, or looking up a template default, filter the bundled `Media Catalog.csv` with a CSV parser when it is available. Filter by category and source first, then match the name, tags or alt text. Read only matching rows. Use `direct_image_url` and `dam_identifier` for DAM rows, or `media_guid` for Media Library rows. The item path supports exact lookup when a listing is truncated. Keep valid references from existing mappings. If a reference is stale, verify the exact asset before replacing it. Use live asset search when the catalog is unavailable or cannot resolve the approved asset. Confirm applicable usage rights through the brief or source and use verified genuine logos and headshots.

Check that the selected image loads in the affected preview slot. If display fails, inspect the field value, owning item, rendered URL and response before changing anything. If preview is unavailable, report the saved write and display status separately.

## Videos

Resolve the actual video-capable field and its provider configuration. Reuse verified same-video settings and ask only for required details that cannot be resolved. Apply the image rule to the poster. Confirm playback when preview is available.

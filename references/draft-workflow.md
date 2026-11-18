# Writing and verifying a Sitecore Draft

Use the SitecoreAI CMS Agent tools and their live schemas. If the connector reports an authentication failure, use the bundled `sitecore-cms-agent` recovery skill.

1. For a new page, resolve the exact target, verify the template and parent, and check the expected item path before creating. Call `create_page` with the name, template, verified parent ID and, when known, language. Omit fields. Retain the returned ID and path. After an uncertain response, reread the exact path before retrying. Resume an existing item only when the user requested that page and its identity is verified.
2. Populate a newly created page in focused field batches with `update_fields_on_item`. Determine what committed before retrying an affected batch. For existing content use workflow-aware `update_content` with the owning item's site and language. Retain the version returned. An approved item can receive a new Draft version. See [field formats](content-fields.md).
3. Confirm the page path, template and workflow using an item ID read where applicable. If a newly created page has no workflow, use the site's verified workflow and non-final Draft state on that new page only, then read back by ID. Report any unresolved state. Empty or truncated field responses are inconclusive. Use targeted inspection and the rendered preview to check critical fields.
4. Keep content unpublished and report any gaps in verification. Inspect forms in preview without submitting a live registration or lead unless separately authorized.

## Preview and editor links

For each completed event or ABM Draft build, lead the handoff with two clickable links:

- **Edit in Sitecore** opens the exact page in Page Builder so users with the appropriate access can edit or publish it when ready. Use a verified direct editor URL from the CMS if available. For WWW, use `https://pages.sitecorecloud.io/editor?tenantName=sitecoreusa9414-hestiabb15-prod6018&organization=org_ASBNUhVI0VPpeltY&sc_itemid={pageId}`. Replace only `{pageId}` with the verified page item's GUID, lowercase and without braces. Use the page ID returned by creation or read-back, never the parent, template or component ID.
- **Preview** opens the exact Draft for review. Use the page-type-specific verified preview URL.

For another environment, use its verified editor URL format. If the editor URL cannot be resolved, return the preview, state what is missing and ask for a working editor URL for that environment. A CMS item path is separate from the editor link. State that the page is saved as Draft.

## Campaign ID in the build summary

For every page build, include a line labeled **Salesforce campaign ID**. Read `FormDefaultSalesforceCampaignID` from the saved form owner in the correct language and report the exact ID string with its source, such as event brief, retained configuration or the documented General ABM default. If the CMS read-back cannot verify the value, distinguish the ID sent in the write from the saved value. For an external form or page without a Salesforce campaign, report that no ID was configured on the Sitecore page and name the registration mode if applicable. If an unresolved ID blocks a native event build, report that the campaign ID is missing and the build is waiting for confirmation.

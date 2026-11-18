# SitecoreAI CMS Agent

Connect SitecoreAI CMS Agent to build and edit Draft content on the Sitecore Marketing WWW site.

- **ABM page** — share an account and campaign goal or supply a content mapping. The agent asks for any material gaps, then prepares the mapping and builds a Draft when requested.
- **Event page** — supply an event brief or mapping with the local schedule, named timezone, and registration details.
- **Existing content** — give the target page, component, and requested change. A public delivery URL is enough to attach an image.

The builders return a preview. The [shared field rules](references/content-fields.md) apply to all edits. The bundled auth recovery skill handles connector authentication failures.

The workspace package includes an internal media catalog. For source checkouts, use approved asset references or search the connected CMS for the approved asset.

The package uses `plugin.json`, `.codex-plugin/plugin.json`, and its registered app mapping. Distribute updates through the existing workspace plugin release process.

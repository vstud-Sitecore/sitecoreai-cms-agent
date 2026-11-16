# SitecoreAI CMS Agent

SitecoreAI CMS Agent plugin package, version 1.0.6, with ABM and Agentic Event Page builders.

## Included skills

- `sitecore-abm-page`: builds a Draft page from an existing ABM content mapping document. Includes the WWW component and asset reference, plus a bundled page namer with cross-platform JavaScript randomness.
- `sitecore-agentic-event-page`: builds an unpublished Draft from an event brief or mapping using the Agentic Event Page template. Includes a 173-field reference and a Python standard-library handoff validator. Resolves the event-local start date to the existing Events Webinars/YYYY/MM path, reuses its folders, and creates only missing year/month folders.
- `sitecore-cms-agent`: recovers an authentication failure through the host's native reconnect flow.

## Usage

Connect SitecoreAI CMS Agent and provide an ABM mapping document, or use the separate `abm-page-guide` skill to create one. Ask to build the page from that mapping. The builder generates a contextual four-to-eight-word item name before creation, leaves the page in Draft and returns a preview link. Explicitly selected names and existing page routes are preserved; new generated names no longer require a hex suffix. The naming helper prefers Codex's built-in Node REPL and requires no Python installation.

The recorded template, parent, designs and media identifiers target the Sitecore Marketing WWW environment. Verify these identifiers before using another environment. Page builds do not publish content.

New builds use the required account-specific footer with the SitecoreAI disclosure. The builder updates older mapping documents to match this footer before populating the page.

## Event pages

Connect SitecoreAI CMS Agent and supply the event brief or field mapping. Include the start/end times, named event timezone, registration route and campaign ID when using a native form. Ask to build an Agentic Event Page. The builder targets template `93b92c2a-70a7-4c5c-9f55-abc5003201e2` under `/sitecore/content/Marketing/WWW/Home/Resources/Events Webinars/YYYY/MM`. The event-local start month determines placement, including events whose UTC date falls in another month or year.

The optional separate `agentic-event-page-guide` can help prepare copy, but is not required to use this builder. ABM account questions and the ABM page-naming flow do not apply to ordinary event pages. Existing explicit names and routes are preserved for updates. Required references, image metadata, registration controls, rendered dates and Draft workflow are checked before reporting completion. Builds never publish the page or submit a real registration as a test.

## Package layout

The Codex compatibility manifest is `.codex-plugin/plugin.json`, the registered app mapping is `.app.json`, and skill resources are under `skills/`.

This repository stores the plugin source. Pushing here does not update an installed or workspace-published plugin; that requires updating it through its distribution workflow.

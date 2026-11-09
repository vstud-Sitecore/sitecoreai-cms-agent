# SitecoreAI CMS Agent

SitecoreAI CMS Agent plugin package, version 1.0.3, with an ABM landing page builder.

## Included skills

- `sitecore-abm-page`: builds a Draft page from an existing ABM content mapping document. Includes the WWW component and asset reference.
- `sitecore-cms-agent`: recovers an authentication failure through the host's native reconnect flow.

## Usage

Connect SitecoreAI CMS Agent and provide an ABM mapping document, or use the separate `abm-page-guide` skill to create one. Ask to build the page from that mapping. The builder leaves the page in Draft and returns a preview link.

The recorded template, parent, designs and media identifiers target the Sitecore Marketing WWW environment. Verify these identifiers before using another environment. Page builds do not publish content.

## Package layout

The Codex compatibility manifest is `.codex-plugin/plugin.json`, the registered app mapping is `.app.json`, and skill resources are under `skills/`.

This repository stores the plugin source. Pushing here does not update an installed or workspace-published plugin; that requires updating it through its distribution workflow.

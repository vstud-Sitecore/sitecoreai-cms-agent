# SitecoreAI CMS Agent

SitecoreAI CMS Agent plugin package, version 1.0.5, with an ABM landing page builder.

## Included skills

- `sitecore-abm-page`: builds a Draft page from an existing ABM content mapping document. Includes the WWW component and asset reference, plus a bundled page namer with cross-platform JavaScript randomness.
- `sitecore-cms-agent`: recovers an authentication failure through the host's native reconnect flow.

## Usage

Connect SitecoreAI CMS Agent and provide an ABM mapping document, or use the separate `abm-page-guide` skill to create one. Ask to build the page from that mapping. The builder generates a contextual four-to-eight-word item name before creation, leaves the page in Draft and returns a preview link. Explicitly selected names and existing page routes are preserved; new generated names no longer require a hex suffix. The naming helper prefers Codex's built-in Node REPL and requires no Python installation.

The recorded template, parent, designs and media identifiers target the Sitecore Marketing WWW environment. Verify these identifiers before using another environment. Page builds do not publish content.

New builds use the required account-specific footer with the SitecoreAI disclosure. The builder updates older mapping documents to match this footer before populating the page.

## Package layout

The Codex compatibility manifest is `.codex-plugin/plugin.json`, the registered app mapping is `.app.json`, and skill resources are under `skills/`.

This repository stores the plugin source. Pushing here does not update an installed or workspace-published plugin; that requires updating it through its distribution workflow.

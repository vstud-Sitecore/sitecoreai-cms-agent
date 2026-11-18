---
name: sitecore-cms-agent
description: Recover a failed SitecoreAI CMS Agent connection only when a tool reports expired credentials, authentication required, or the user explicitly needs help reconnecting. Do not activate for successful routine CMS requests, listing sites, or normal installation.
---

# Recover Sitecore sign-in
The registered app and host handle authentication and token refresh. Installation requires no additional setup chat.

Use this skill only after an authentication failure or an explicit reconnection request. Let the host refresh the session or present its native sign-in/reconnect action. Ask the user to complete Sitecore sign-in and choose their organization/environment. Never configure another MCP server, edit settings, request secrets or construct OAuth URLs. Do not claim a window opened unless the host opened one.

Keep the original request and resolved target. Once sign-in completes, retry a failed read once. Before retrying an uncertain write, check whether it already succeeded. Follow live tool confirmation requirements.

Permission denied is not an expired session; reconnecting does not grant access. Missing tools alone do not prove expired credentials. If no native sign-in action is exposed, guide the user to this plugin's verified account Connect/Reconnect control.

Do not run connection checks after successful installation or before routine actions. Successful direct CMS requests use their MCP tools without loading this recovery workflow.


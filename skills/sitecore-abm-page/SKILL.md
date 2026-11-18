---
name: sitecore-abm-page
description: Guide users through briefing a personalized ABM landing page for a named account, prepare its content mapping, and build an unpublished Sitecore Draft when requested. Use for account campaigns, personalized event invitations, supplied mappings, and continuing after mapping.
---

# Build an Agentic ABM Page

Use this workflow for a new personalized account page from a brief, an existing Field | Content mapping, or a request to continue after mapping. Read the [ABM component kit](references/component-kit.md) for exact fields and defaults, the [shared Draft workflow](../../references/draft-workflow.md) for writes and checks, and the [shared field rules](../../references/content-fields.md) for field formats and asset lookup. For a targeted edit to an existing page, follow [Sitecore content editing](../sitecore-edit-content/SKILL.md).

## Confirm the brief before drafting

For a new ABM page, check the brief, prior user answers and user-provided materials for these five answers:

1. **Account and market.** Which organization, and which market or business unit if the name alone leaves it ambiguous?
2. **Target reader.** Which team or roles at the account should this page speak to?
3. **Account relationship.** Is the account a current customer, new prospect, former customer, partner, or unknown? If they are a current customer, invite the user to share relevant products or initiatives if known.
4. **Reader familiarity.** Are these readers new to Sitecore, aware of the name, or already familiar through evaluation or use? Confirm this separately from the account relationship.
5. **Campaign goal and action.** What priority, opportunity or event is the page for, and what should the visitor do next? Offer a concrete suggestion when useful.

An answer counts when the user supplied it, it is explicit in a user-provided brief, or the user explicitly delegated that choice. A generic product theme such as “a SitecoreAI message” leaves the goal and action open. Public research and agent assumptions cannot answer the intake on the user's behalf.

**If any answer is missing, ask for the missing answers in one short message and end the turn. Wait for the user's reply before researching the account, drafting a mapping, or creating or updating anything in Sitecore.** A request to “create” or “build” the page authorizes the draft after intake. It does not waive the questions. Accept “unknown” or “use your best judgment” as answers, and offer those choices in the prompt. An explicit request to skip questions permits best-judgment defaults for remaining choices, provided the account is identifiable and the conversion path can be resolved. A ready-to-build mapping supplied by the user or prepared in an earlier turn after intake counts as the brief. Targeted edits to an existing page follow the separate edit workflow.

For example, for “Create a new ABM page targeting JAECOO with a SitecoreAI message,” ask which market and readers to target, whether JAECOO is a current customer or prospect, how familiar those readers are with Sitecore, and which priority and next action to build around. Then wait. A brief that already answers or delegates these choices can proceed immediately.

After intake, introduce Sitecore briefly for unfamiliar or unknown audiences and build on confirmed products or initiatives for familiar teams. If the relationship is unknown, write without assuming a deployment or commercial relationship. Keep unapproved sales notes out of visitor copy. Invite optional account notes, approved proof, assets or a specific Salesforce campaign ID in the same message if helpful. Use the documented General ABM campaign where appropriate when a specific ID is unavailable. Follow up only when a remaining gap prevents a sound page or a working conversion path.

## Plan and prepare the content

Use the brief, primary account sources and approved Sitecore messaging to identify specific priorities, outcomes and proof. Keep supporting sources and omission reasons in the mapping or internal notes. Verify event details, claims and direct quotes. Apply the workspace brand and copy guidance when available.

For a new mapping, default to a full page. Aim to fill most of the template's six optional sections when the evidence supports them, in addition to the required metadata, hero, form and footer. Evaluate every section before omitting it. Use one purpose per section and avoid repeating the hero's message.

| Optional section | What to look for |
|---|---|
| Logo strip | Approved peer logos with a defensible connection to the story. Use a truthful label and avoid suggesting endorsements, attendance or relationships that have not been confirmed. |
| Pain Points | Four distinct account-specific challenges, outcomes, reasons to attend or questions the readers bring. |
| Use Cases | Six distinct steps and a result when there is a genuine workflow, adoption path or event journey. Verify step links or use the documented form anchor where appropriate. |
| Solutions & Differentiator | Three relevant solution or topic pillars, each with imagery, plus one supported reason to choose the offer. |
| Mid-Page CTA | A concise nudge tied to the main action and its verified destination. Include by default when the action is supported. |
| Validation | A relevant sourced case study and supported analyst content, with verified links and approved imagery. |

Fill included fixed-size groups as complete units according to the kit. Match assets to the slots using the shared field rules, including approved ABM icons for the cards and flow. After intake, research [hero metrics](references/component-kit.md#hero-metrics) tied to the account and campaign goal. Lead the hero insights with the strongest relevant number and prioritize sourced metrics for the remaining slots. If a section still lacks substantive copy, proof, valid links, or suitable assets after looking for alternatives, record the reason and omit it as a unit. Never invent account facts, figures, quotes, relationships or endorsements to fill space.

Prepare the Field | Content mapping and Build requirements using exact fields and the kit's defaults. Review copy, full groups, sources, asset references and the main CTA before any CMS write. Check each hero figure against its original source and keep its attribution clear in the rendered copy. If the request is for content or review only, deliver the mapping under the user's workspace output rules. If the user requests a draft build, proceed with the prepared or supplied mapping without a separate review round.

## Target and name

WWW parent: `/sitecore/content/Marketing/WWW/Home/Solutions/built-for` (`31dbe568-c0b5-4545-9414-8cd017ff626e`). Template: Agentic ABM Page (`98e0f7d6-d424-40ad-8f19-8cbbc7ad5ff7`). Verify equivalent targets before using a different environment.

For a new page, choose one distinctive, contextual **3–7-word item name** in letters and single spaces. Avoid fixed account-and-campaign formulas and confidential details. Preserve a name the user explicitly chose and preserve existing routes unless the user requests a rename. Old automatically generated names or hex slugs in a mapping are proposals. Record the final item name and resulting slug in Build requirements. Use the item name for creation and reuse it across retries. Pick a different name for a verified collision with unrelated content.

## Populate and verify

- Apply the component kit's required settings and form configuration. Fill missing supported metadata and form confirmation copy before writing. Use the confirmed campaign ID or the documented General ABM default when applicable. For a new draft use the current footer copy from the kit, even if the source mapping has an older footer. Preserve the source mapping’s footer and leave an existing page’s footer alone unless the user requests a footer edit. Ask only about unresolved material decisions.
- Honor explicit asset selections and omissions. When a selection is needed, follow the shared image lookup and the [ABM media slot rules](references/component-kit.md#media-slot-rules).
- On WWW share the friendly preview at `https://preview.sitecore.com/solutions/built-for/<slug>`. Use the verified route. For standard names the slug is lowercase with spaces replaced by single hyphens. Inspect the preview for the chosen navigation, announcement bar, hero branding, and visible submit control. Confirm that included optional sections render with their full set of cards, steps or pillars, and check the form configuration without submitting.
- Save the page ID, item name and slug, preview and any exceptions with the mapping. Lead the build handoff with clickable **Edit in Sitecore** and **Preview** links using the [shared link instructions](../../references/draft-workflow.md#preview-and-editor-links). Summarize material assumptions, omitted components and their reasons, and any unverified behavior. Finish with the [Salesforce campaign ID report](../../references/draft-workflow.md#campaign-id-in-the-build-summary).

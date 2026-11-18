# Agentic ABM Page field reference

Use these WWW template fields with the approved Field | Content mapping. Apply the [shared field rules](../../../references/content-fields.md) for asset lookup and field writes.

Skip intentional omissions (often marked `—`) unless the template requires an explicit clear. Fill other gaps using the shared field rules. Strip editorial notes. Convert Markdown links and `<br><br>` paragraph breaks only in rich text. Types: S is single-line text, R is rich text, I is image, L is link, C is checkbox. Verify live definitions when values or references are ambiguous.

## Media slot rules

- Card-grid and flow-chart icon slots, including the result, use only Media Library entries in the `ABM icons` category. Use the preferred IDs recorded in the workspace media catalog when available. Otherwise, resolve the approved ABM icons in the Media Library. When a flow-chart step has no suitable icon, use the matching `number-1-circle` through `number-6-circle` marker. For an exact lookup, use the recorded item path.
- Use Sitecore message graphics or suitable landscape imagery for `SolutionNImage`. Use suitable landscape photography for `CaseStudyImage` and keep message graphics in pillar slots. The `AnalystNLogo` slots use approved analyst logos or flat ABM icons. For the standard layout use Forrester, Gartner and Forrester in order. Logo-strip selections should be approved peer logos.

## Build requirements

Record navigation, any announcement, logo exceptions and the expected form action label. Use Blank navigation on new pages when the brief is silent. Honor an explicit navigation choice. WWW designs: Blank for no navigation `9DBFD004-7816-4176-AD67-0384A404C513`; Default for standard navigation `B6C665BC-2DC3-43C8-A344-22297B1D371D`. Section links require an existing supported design and destination anchors.

## SEO / Metadata (Base Page)

Required. Set `NoIndexNoFollow` to `1`. WWW defaults: `ContentOwnership` Jacqueline Baxter and `ContentType` Other. Resolve these labels to valid IDs from the fields’ sources. The live ABM Base Page template uses a TreelistEx for ownership and a Droplink for content type. Review the default labels and footer copy by 2027-01-01.

| Field | Type |
|---|---|
| MetadataTitle | S |
| MetadataDescription | S |
| MetadataKeywords | S |
| NoIndexNoFollow | C |
| OpenGraphTitle | S |
| OpenGraphDescription | S |
| ContentOwnership | TreelistEx |
| ContentType | Droplink |

## Header

Write an empty string to clear `HeaderBannerDescription` unless Build requirements explicitly calls for an announcement. It is plain text.

| Field | Type |
|---|---|
| HeaderBannerDescription | S |

## Hero

Required. Keep the template’s paired logo slots and separator. Default primary logo for dark heroes: the approved `Sitecore reverse logo (white)`, alt text `Sitecore`. Use a suitable approved variant for a light background. Use the approved account logo when available and record deliberate omissions. Preserve proportions and clear space. Hero CTA normally targets `#form-section`.

| Field | Type |
|---|---|
| HeroLogoPrimary | I |
| HeroLogoSecondary | I |
| HeroHeadline | S |
| HeroDescription | R |
| HeroCTAText | S |
| HeroCTALink | L |
| HeroInsight1Metric | S |
| HeroInsight1Description | R |
| HeroInsight2Metric | S |
| HeroInsight2Description | R |
| HeroInsight3Metric | S |
| HeroInsight3Description | R |

### Hero metrics

Use the three Hero Insight pairs to show the prospect why the page is worth reading. Lead with the strongest researched number and use distinct insights that connect to the campaign goal. Research account-specific figures first in primary sources such as annual reports, investor updates, newsroom announcements or official datasets. Look for metrics that establish scale, show momentum or make an opportunity tangible. If suitable account figures are scarce, use clearly attributed results from an approved Sitecore customer story or a relevant benchmark from its original publisher. Choose figures for their relevance to the reader's priorities.

Put a short figure and its unit in `HeroInsightNMetric`. In `HeroInsightNDescription`, explain in plain language what the figure measures and why it matters to the reader. Include the owner, period, geography, cohort or baseline where needed to interpret it. Keep source links and claim context in the mapping. Label peer results and market benchmarks so readers can tell whose numbers they are. A peer result cannot serve as a forecast or promised outcome for the prospect. For a slot without a credible, relevant number, use a distinct sourced qualitative insight. Use each insight pair as a unit.

## Logo Strip

Optional. `Logo1` through `Logo8` are image fields for approved peer logos.

## Pain Points

Optional. Use ABM library icons for the card slots.

| Field | Type |
|---|---|
| PainPointsEyebrow | S |
| PainPointsTitle | S |
| PainPointsDescription | R |
| PainPoint1Icon … PainPoint4Icon | I |
| PainPoint1Title … PainPoint4Title | S |
| PainPoint1Description … PainPoint4Description | R |

## Use Cases

Optional. Use all six steps or skip the chain. Every step and the result use ABM library icons. Link each step to its configured destination or `#form-section`. The result has no link.

| Field | Type |
|---|---|
| UseCasesEyebrow | S |
| UseCasesTitle | S |
| UseCase1Icon … UseCase6Icon | I |
| UseCase1Title … UseCase6Title | S |
| UseCase1Link … UseCase6Link | L |
| UseCaseResultsTitle | S |
| UseCaseResultsIcon | I |

## Solutions & Differentiator

Optional. Populate or skip both parts together. Use suitable landscape pillar images. `SolutionsDescription` is a legacy mapping row with no matching field.

| Field | Type |
|---|---|
| SolutionsEyebrow | S |
| SolutionsTitle | S |
| Solution1Image … Solution3Image | I |
| Solution1Title … Solution3Title | S |
| Solution1Description … Solution3Description | R |
| DifferentiatorEyebrow | S |
| DifferentiatorTitle | S |
| DifferentiatorDescription | R |

## Mid-Page CTA

Optional. `Mid-PageCTADescription` is plain text. The CTA normally targets `#form-section`.

| Field | Type |
|---|---|
| Mid-PageCTADescription | S |
| Mid-PageCTAButtonText | S |
| Mid-PageCTALink | L |

## Validation (Case Study + Analysts)

Optional. Preserve the `CaseStudyHightlight*` field spelling. Use a suitable landscape photo for `CaseStudyImage` and approved logos or flat ABM icons for `AnalystNLogo`.

| Field | Type |
|---|---|
| CaseStudyEyebrow | S |
| CaseStudyTitle | S |
| CaseStudyImage | I |
| CaseStudyHighlightTag | S |
| CaseStudyHighlightQuote | S |
| CaseStudyHighlightDescription | S |
| CaseStudyHightlightCTAText | S |
| CaseStudyHightlightCTALink | L |
| Analyst1Logo, Analyst2Logo, Analyst3Logo | I |
| Analyst1Description … Analyst3Description | R |

## Form Defaults and Form Datasource

Required. Preserve the exact `Company Name` field spelling and use a country for Region. Use the confirmed campaign ID or the accepted General ABM default `701Ui00001FUy7FIAT`. Use the inherited submit control and verify the visible label from Build requirements, defaulting to Submit.

| Field | Type |
|---|---|
| Company Name | S |
| Region | S |
| State | S |
| FormTitle | S |
| FormIntroText | R |
| FormConfirmationMessage | R |
| FormDefaultSalesforceCampaignID | S |
| LastInterestingMomentDescription | S |

## Footer

Required single-line copy for new drafts. Replace the placeholders with the year the draft is created and the account name:

> © [year] Sitecore A/S. Built for [Account name]. This page was generated with SitecoreAI.

| Field | Type |
|---|---|
| FooterDisclaimer | S |

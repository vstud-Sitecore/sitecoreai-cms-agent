# Agentic ABM Page — component kit

The template renders, top to bottom: Header banner → Hero → Logo strip → Card grid → Flow chart → Image pillars + Differentiator → Mid-page CTA → Highlight + pillars → Form → Footer. Metadata is invisible. Any component except Hero, Form, Footer, and Metadata may be skipped. Header banner is empty by default and used only for an explicit announcement.

## Contents

1. [Mapping doc conventions](#mapping-doc-conventions)
2. [SEO / Metadata](#1-seo--metadata-always-filled) — always filled
3. [Header banner](#2-header-banner-announcement-only) — announcement only
4. [Hero](#3-hero-required) — required
5. [Logo strip](#4-logo-strip-optional)
6. [Card grid (2×2)](#5-card-grid-22--pain-points-fields-optional)
7. [Flow chart](#6-flow-chart--use-cases-fields-optional)
8. [Image pillars + Differentiator](#7-image-pillars--differentiator--solutions-fields-optional)
9. [Mid-page CTA](#8-mid-page-cta-optional)
10. [Highlight + pillars](#9-highlight--pillars--validation-fields-optional)
11. [Form](#10-form-always-filled)
12. [Footer](#11-footer-always-filled)
13. [Icon library](#icon-library)
14. [Known image IDs](#known-image-ids) — full image catalog

## Mapping doc conventions

The output doc is one markdown file. Use these **exact section headers** (the build skill navigates by them) and a `| Field | Content |` table under each: `## SEO / Metadata (Base Page)`, `## Header`, `## Hero`, `## Logo Strip`, `## Pain Points`, `## Use Cases`, `## Solutions & Differentiator`, `## Mid-Page CTA`, `## Validation (Case Study + Analysts)`, `## Form Defaults`, `## Form Datasource`, `## Footer`.

- Field names must match this file character for character, including `Company Name` (with space) and the `CaseStudyHightlight*` misspelling.
- **Skipped component** → keep the section and every field row, with `—` as the content. The build skill leaves those fields blank in Sitecore.
- **Image fields** → `Use image id {GUID}`, picked from this file's tables. Hero logos may instead use the verified DAM delivery-reference format documented in Hero branding. **Every filled image slot needs a real ID.** The sentence `Populate <FieldName> with the most relevant image you can find in Media Library under Images/ABM` still works, but it is a last resort for a slot the catalog genuinely cannot serve, not a default — it hands an aesthetic call to the build skill, which makes it without any of the story context. Where a slot is documented as safely empty, `—` means "no image" and is fine.
- **Rich text fields** may contain markdown links `[text](url)`; the build skill converts them to `<a href>`. A paragraph break inside a rich text cell is written as `<br><br>` (the build skill turns it into separate `<p>` blocks). No other HTML in the doc.
- **Single-line fields** must be plain text: no links, no markdown, no HTML. The two that get this wrong most: `Mid-PageCTADescription` and `HeaderBannerDescription`.
- Escape literal pipes as `\|`.
- Field types below: **S** = single-line text, **R** = rich text, **I** = image, **L** = link/URL, **C** = checkbox.

## 1. SEO / Metadata (always filled)

Invisible to the visitor; draft silently from the approved content. Section header: `## SEO / Metadata (Base Page)`.

| Field | Type | Guidance |
|---|---|---|
| MetadataTitle | S | Search hook + brand: `[reader benefit] \| SitecoreAI`. Name the account. ~6–9 words, under 60 chars. |
| MetadataDescription | S | Value promise + the page's CTA. Name the account once. ~150–160 chars. |
| MetadataKeywords | S | Comma-separated: account name, SitecoreAI, plus the page's themes. ~8–12 terms. |
| NoIndexNoFollow | C | Always `Checked` — ABM pages stay out of search indexes. |
| OpenGraphTitle | S | Social-share headline, names the account. ~10–14 words. |
| OpenGraphDescription | S | One sentence: what they'll get + the offer. ~18–25 words. |
| ContentOwnership | S | Always `Jacqueline Baxter`. |
| ContentType | S | Always `Other`. |

## 2. Header banner (announcement only)

Leave this text bar empty unless the user explicitly requests an announcement. It is not a positioning tagline or site navigation. Keep the Header section and use `—` by default; the builder writes an empty string to clear inherited content.

| Field | Type | Guidance |
|---|---|---|
| HeaderBannerDescription | S | Default `—`. Only for an explicit announcement: concise visitor-facing announcement copy, ~15–22 words. **Plain text only.** |

## 3. Hero (required)

H1, supporting line, CTA button, and **three highlight stats in a row** (big metric + one-line explanation each). The metric slot is short display text — a number, a ratio, a date range ("Oct 14–16"), a percentage. It does not have to be numeric, but it must be short.

| Field | Type | Guidance |
|---|---|---|
| HeroLogoPrimary | I | Approved Sitecore reverse logo by default. See Hero branding below. |
| HeroLogoSecondary | I | Approved target-account logo, paired in the existing hero slots; `—` if unavailable, with an exception in Build requirements. |
| HeroHeadline | S | The one-line pitch. ~9–13 words. |
| HeroDescription | R | What the visitor will get from this page. ~15–20 words. |
| HeroCTAText | S | Button label naming the action/offer. 2–4 words. |
| HeroCTALink | L | `#form-section` (scrolls to the form) unless the CTA goes elsewhere. |
| HeroInsight1Metric | S | Stat 1 display value. 1–4 tokens. |
| HeroInsight1Description | R | What the stat means for the reader. ~12–20 words. Cite real sources as markdown links. |
| HeroInsight2Metric | S | Stat 2 display value. |
| HeroInsight2Description | R | As above. |
| HeroInsight3Metric | S | Stat 3 display value. |
| HeroInsight3Description | R | As above. |

Stats must be true and sourced; a linked source in the description is the house pattern. If the story has no three defensible stats, use three key facts (dates, venue, "50+ sessions") rather than inventing numbers.

### Hero branding

Use HeroLogoPrimary and HeroLogoSecondary for the Sitecore/account pairing, not the customer social-proof strip. The component supplies a separator when both slots are filled. Preserve original artwork, proportions, clear space and comparable visual weight. Use the white mono Sitecore reverse logo on the dark/gradient hero by default; record exceptions for light backgrounds or deliberate omission. Never imply that a prospect is a customer or partner.

Use catalog image IDs where available. Hero logos also support `Use DAM image URL <https-url>` for a verified existing public delivery reference; carry DAM identity and alt text in Build requirements. The future preferred flow is approved account artwork → Content Hub DAM upload/approval → delivery reference → hero attachment. Automated upload is not part of the present skill.

Verified Sitecore white mono reverse: DAM asset `M2jN1Nb7SUOBL_fs2povFQ`, delivery URL `https://delivery-sitecore.sitecorecontenthub.cloud/api/public/content/1a4cb6c5678d4a66a51589f568e71e08?v=a2056199`. Existing Sitecore footer asset, inspected 9 November 2026; SVG uses white fills. Recheck if the asset changes. Alt text: `Sitecore`. This is a DAM reference, not a Sitecore media-library GUID. Copy the complete verified image value from `/sitecore/content/Marketing/WWW/Data/Footers/Shakespeare Footer`, field `Logo`, when attaching this asset. A bare `src` image value resolves to an empty image in this environment: preserve `dam-id`, `dam-content-type`, `width`, `height` and `thumbnailsrc` as well as `src` and alt text. Verified XML:

```xml
<image src="https://delivery-sitecore.sitecorecontenthub.cloud/api/public/content/1a4cb6c5678d4a66a51589f568e71e08?v=a2056199" dam-id="M2jN1Nb7SUOBL_fs2povFQ" width="463" height="100" dam-content-type="Image" thumbnailsrc="https://sitecore.sitecorecontenthub.cloud/api/gateway/118539/thumbnail" alt="Sitecore" />
```

### Page build settings (outside field tables)

Record the exact `<account>-<campaign>-<random-suffix>` item name/slug, with at least 16 securely random lowercase hex characters. Keep it stable after creation. Record Navigation: no navigation / section links / standard navigation; Announcement: none / requested announcement; and logo exceptions. No navigation maps to Blank Page Design `{9DBFD004-7816-4176-AD67-0384A404C513}`; standard navigation maps to Default `{B6C665BC-2DC3-43C8-A344-22297B1D371D}`. Section links require a verified existing implementation. These are build settings, not invented content fields.

## 4. Logo strip (optional)

A row of 8 customer logos. Canonical use: peer social proof. Also works for: partners, sponsors, brands attending an event. **Default to including it on net-new and sales-oriented pages** — social proof carries weight with a prospect.

**Pick all eight yourself, by ID, from the [customer logos table](#customer-logos--imagesabmcustomer-logos).** Order them: the account's own sector first, then nearest-adjacent sectors, then recognisable enterprise names to fill the row. With 23 logos in the catalog you will rarely get eight sector-perfect matches, and that is fine — a considered near-match beats delegating the choice. Never imply a partnership a logo doesn't support. Skip the whole strip only when peer logos would feel off for the story.

Fields: `Logo1` … `Logo8`, all type I.

## 5. Card grid (2×2) — "Pain Points" fields (optional)

Eyebrow + section title + intro, then **four cards in a 2×2 grid**, each with an icon, a short title, and a couple of sentences. Canonical use: the account's pain points. Also works for: reasons to attend, benefits, themes, "what you'll learn", FAQs. This is usually where the page earns its personalization — make the four cards specific to the account, not statements any company could receive.

| Field | Type | Guidance |
|---|---|---|
| PainPointsEyebrow | S | Section label. 1–3 words (e.g. `Opportunities`, `Why attend`). |
| PainPointsTitle | S | Section headline anchored in an account-specific fact. ~8–12 words. |
| PainPointsDescription | R | Acknowledge what the account does well, then frame the opportunity. Name them once. ~28–35 words. |
| PainPoint1Icon … PainPoint4Icon | I | Pick from the [icon library](#icon-library). |
| PainPoint1Title … PainPoint4Title | S | Action-framed card headline, not a lament. ~4–7 words. |
| PainPoint1Description … PainPoint4Description | R | The specific point and its consequence for the reader, tied to something real about the account. ~20–28 words. |

## 6. Flow chart — "Use Cases" fields (optional)

Eyebrow + title, then a **horizontal chain of six steps flowing into a seventh result slot** (1→2→3→4→5→6 → result). Each step: icon + short title + link. The result: title + icon, no link. Canonical use: platform use cases. Also works for: an event agenda, an onboarding path, a day-in-the-life, "your journey to X" — anything with sequence and a payoff.

| Field | Type | Guidance |
|---|---|---|
| UseCasesEyebrow | S | Section label. ~4–8 words. |
| UseCasesTitle | S | What the journey adds up to. ~8–12 words. |
| UseCase1Icon … UseCase6Icon | I | **Always** from the [icon library](#icon-library) — never a photo or any other media library image. No icon fits a step? Use `number-1-circle`…`number-6-circle` in order. |
| UseCase1Title … UseCase6Title | S | Step label, verb-led. ~4–7 words. |
| UseCase1Link … UseCase6Link | L | Where the step is a Sitecore capability, link the matching sitecore.com use-case page (see county examples: `https://www.sitecore.com/platform/use-cases/...`). Otherwise `#form-section`. |
| UseCaseResultsTitle | S | The payoff. ~4–7 words. |
| UseCaseResultsIcon | I | From the [icon library](#icon-library) only. Usually `increased-sales` `{048F7BB8-CCD6-4BE3-9C26-3EAB5AB1B8C2}` or `success` `{3F415967-F33D-45CF-83BA-235A9F73E7F2}`. |

All six steps or none — a shorter chain leaves empty boxes.

## 7. Image pillars + Differentiator — "Solutions" fields (optional)

Eyebrow + title, then **three pillars, each with a landscape image, a title, and a description**. Canonical use: solution pillars. Also works for: session tracks, featured speakers, product lines, offers. Below it sits a small **Differentiator** text block (eyebrow + title + short rich text) — the "why us / why this" close. The two render as one section: use both or skip both.

| Field | Type | Guidance |
|---|---|---|
| SolutionsEyebrow | S | Short label naming the account, e.g. `What Nestle could unlock`. ~3–5 words. |
| SolutionsTitle | S | Outcome-led headline. ~8–12 words. |
| SolutionsDescription | — | Always `—`; the template has no matching rendering for it. |
| Solution1Image … Solution3Image | I | Landscape images — **match the image to the pillar's theme, don't assign by position**, and give each one a real ID. Pick from the [image catalog](#known-image-ids): the three pillar graphics map to Run, Expand and Drive, the use-case graphics cover capabilities like DAM, MCP, multi-site, localization and campaign management, and the case study backgrounds cover the account's own industry. Re-order freely. `—` is allowed here and means "no image" — an empty slot doesn't break this component — but a deliberate ID is better on nearly every page. |
| Solution1Title … Solution3Title | S | Pillar headline. ~4–7 words. |
| Solution1Description … Solution3Description | R | What the reader gains, in outcome terms. ~20–26 words. |
| DifferentiatorEyebrow | S | Short label. ~2–3 words. |
| DifferentiatorTitle | S | Two short clauses, punchy. ~6–10 words. |
| DifferentiatorDescription | R | Two short paragraphs in one cell, separated by `<br><br>`. **Fit the angle to the page's story, don't default to a stock claim.** On a platform pitch, the house angle (AI is Already Included, no surcharge, no bolt-ons) fits; on an event invite, it's why this event and why now; on a partner page, why the partnership. ~35–45 words total. |

## 8. Mid-page CTA (optional)

A one-line nudge with a button, halfway down the page.

| Field | Type | Guidance |
|---|---|---|
| Mid-PageCTADescription | S | One sentence naming the account and the payoff. ~10–16 words. **Plain text only — this field breaks if given HTML.** |
| Mid-PageCTAButtonText | S | `Discover Sitecore` unless the page's action reads better. 2–3 words. |
| Mid-PageCTALink | L | `#form-section`. |

## 9. Highlight + pillars — "Validation" fields (optional)

Eyebrow + title, then a **large image with an overlaid text highlight** (tag, quote, attribution, CTA link), followed by **three pillars each with an image and a rich description**. Canonical use: customer case study + three analyst endorsements. Also works for: a testimonial + proof points, an event keynote highlight + supporting reasons, a venue shot + logistics.

| Field | Type | Guidance |
|---|---|---|
| CaseStudyEyebrow | S | Section label, often all-caps. ~3–5 words (e.g. `A COUNTY LIKE YOURS`, `HEAR IT FROM A CUSTOMER`). |
| CaseStudyTitle | S | Section headline. ~8–12 words. |
| CaseStudyImage | I | The big image, always by ID. Broward County press image `{52227DD3-3B92-413F-8104-EC93DD4275A2}` for the canonical case study; otherwise pick the account's sector from the [case study backgrounds](#case-study-backgrounds--imagesabmcase-study-backgrounds), or another verified suitable landscape photograph. Never use an asset from `Images/ABM/Sitecore Message Graphics`, including on platform pitches. |
| CaseStudyHighlightTag | S | Small tag over the image (e.g. `Press Release`, `Customer story`). 1–3 words. |
| CaseStudyHighlightQuote | S | The overlaid quote, in quotation marks. ~30–60 words. |
| CaseStudyHighlightDescription | S | Attribution line: `– Name, Title, Organization`. |
| CaseStudyHightlightCTAText | S | (Note spelling.) Link text, e.g. `Read the press release →`. |
| CaseStudyHightlightCTALink | L | (Note spelling.) Destination URL. |
| Analyst1Logo, Analyst2Logo, Analyst3Logo | I | Canonical: Forrester `{E1A8996A-0E7A-4C8D-8EFD-E1D2900C2D0A}`, Gartner `{B620D09D-D477-4FD5-8EE1-BF37CEC8C23F}`, Forrester. Repurposed: a relevant logo or flat ABM library icon only. These small slots cannot carry photos, illustrations or message graphics. |
| Analyst1Description … Analyst3Description | R | One sentence of proof each, with a markdown link to the source. Evergreen defaults: Forrester TEI [371% ROI](https://www.sitecore.com/resources/insights/content-management/forrester-total-economic-impact-of-sitecoreai); Leader, [2026 Gartner® Magic Quadrant for Content Marketing Platforms™](https://www.sitecore.com/solutions/analyst-reports/gartner-magic-quadrant-content-marketing-leader); Leader, [The Forrester Wave™: Digital Experience Platforms, Q4 2025](https://www.sitecore.com/solutions/analyst-reports/the-forrester-wave-digital-experience-platforms). |

## 10. Form (always filled)

Two sections in the doc. `## Form Defaults` pre-fills the visitor's form; `## Form Datasource` is the conversion block copy.

**A visible, working submit button is mandatory.** Add a `Build requirements` note outside the field tables with its action label (default: `Submit`). The build skill must use the template's existing form controls and verify the button in preview. No submit-button field is documented here; inspect the existing form configuration rather than inventing a field name.

| Field | Type | Guidance |
|---|---|---|
| Company Name | S | (Space in name.) The target account's name. |
| Region | S | **A country**, e.g. `United States`, `Denmark`, `Switzerland` — never a sales region like EMEA. If the user didn't give one and you're not sure, `—`. |
| State | S | If applicable, else `—`. |
| FormTitle | S | The offer as a verb phrase: what they get by submitting. ~4–7 words. |
| FormIntroText | R | One or two sentences making the offer concrete for this account. ~20–30 words. |
| FormDefaultSalesforceCampaignID | S | Always filled, never `—`. Ask the user: their own Salesforce campaign ID if they have one, otherwise the General ABM id `701Ui00001FUy7FIAT`. Don't offer "no campaign" as a third option — every page ties to a campaign, named or general. |
| LastInterestingMomentDescription | S | Short lead-source label for sales, e.g. `ABM Lead from <Campaign>`. Derive from the campaign; confirm with the user if a campaign name exists. |

## 11. Footer (always filled)

| Field | Type | Guidance |
|---|---|---|
| FooterDisclaimer | S | `© 2026 Sitecore A/S. Built for <Account>.` Use directly publishable, visitor-facing copy only. Never include review status or production notes such as "ready to be proofed", "awaiting review" or "draft". Add AI disclosure only when appropriate; claim completed human proofing only if confirmed. |

## Icon library

Icons for card grid and flow chart slots. **Every icon slot in both components must come from these two folders** — never substitute a photo, customer logo or illustration from elsewhere in the media library. Match the slot's theme against the name and association terms, then use `Use image id {GUID}`.

> **Asset IDs refreshed September 2026.** The whole ABM media library was re-imported: every name stayed the same, every GUID changed, and `Images/ABM/Icons` was renamed `Images/ABM/Icons1`. The IDs below are the current ones, verified against the live library. Any GUID from an older copy of this file, or from an existing mapping doc, is dead and will fail the build.

**How the two folders relate.** `Icons1` is the complete set — all 83 icons. `Icons2` holds a second copy of 33 of those same names under different IDs. Either copy renders identically; prefer the `Icons2` entry for those 33 so pages already built stay consistent. Anything not in `Icons2` comes from `Icons1`.

**Folder listings cap at 50 children**, so a `get_content_item_by_id` on `Icons1` stops at `increased-sales` and hides the last 33 items. They are all listed below — recovered by path lookup — so read this table rather than listing the folder. Don't conclude an icon is missing because a listing didn't show it.

**`Images/ABM/Icons1`** — 83 items (‡ = past the 50-child listing cap)

| Name | Asset ID | Association terms |
|---|---|---|
| 3-pluses | `18556e6c-a413-4739-af98-e651ec992f19` | growth, added value |
| achievement | `b4ff840f-c487-454e-bcce-f0a5f71b10b9` | award, badge, success, recognition |
| advertising | `91ecafca-f9d1-40c3-b6d0-aa7426a5e7a3` | campaign, promotion, megaphone |
| analytics | `39251d80-b669-4537-8251-f7c57a442f02` | dashboard, performance, reporting, insights |
| artificial-intelligence | `148b001e-8529-4664-ada7-89eebff30bcf` | AI, automation, machine learning |
| automation | `08ef5f86-a24a-40cf-9e18-5def94184906` | workflow, efficiency, process |
| awareness | `21655c68-1a3d-4668-9583-57705323dafe` | brand recognition, audience reach |
| brochure | `c3c2d163-80f8-4a72-abd9-8c580ab95ad1` | collateral, print, sales sheet |
| browser | `6c4e7cfb-a4ee-40e3-958c-37626b87d4ee` | web, window, online |
| calendar | `0cc40252-90fb-4de6-ac47-5ba253ae3bee` | schedule, planning, dates, event |
| chat | `88e684b9-abb8-42c8-94d2-1911edd25933` | conversation, messaging, support |
| checkmark | `420dac5b-3918-4a5c-9b69-3775745151ed` | approval, success, completed, verified |
| cloud | `6012e313-2fb6-4407-ab29-110d43d36bb3` | cloud computing, platform, storage |
| cloud-index | `3911a754-dc3a-4036-b2c5-f2fb9e7df2e7` | search, data catalog |
| cloud-storage | `1c247fce-73e4-4273-89e5-22e91c26ca7e` | backup, repository |
| cloud-web-services | `7839fe75-46d9-4408-9c5a-a676727f9b09` | infrastructure, platform |
| cms | `ef01f7d1-ffa2-4233-b96a-79fbb42f3943` | content management, publishing |
| coding-hierarchy | `ae602c40-4b78-4e48-b594-401883a5263c` | development, structure, architecture |
| connected | `4d2a2cee-e35a-451c-bd94-5d5950e0949f` | systems, network, integration |
| content | `3cc5f813-dbed-4997-9957-03cf96118ccf` | document, page, asset, information |
| content-marketing | `a3578d1c-f8c1-4ee9-8a2d-5e5c95ec9dff` | strategy, editorial, promotion |
| conversation | `17268dd5-b1b1-44ff-a59b-c1cb547b6abe` | dialogue, communication bubbles |
| conversion | `3d4f2820-ad95-4889-9c74-b46c3cf61e76` | funnel, goal, optimization |
| cookies | `03febb27-9d9a-496c-b7b4-e032180c33c0` | consent, privacy, tracking |
| corporation | `5c4e0f7c-f279-4a87-9044-3408a4f7f8f4` | enterprise, office building |
| create-content | `f290844c-73d7-47da-b71c-30451d6d6d51` | writing, editing, publishing |
| crosschannel | `b2dd095e-55ee-4398-b41f-69eb1850e5e9` | omnichannel, orchestration |
| customer-first | `ed215548-185b-4b87-a66b-7e43e7e4b6ba` | experience, empathy, service |
| customer-journey | `78a1d884-284a-45a6-b972-3e986be18fe2` | path, lifecycle, touchpoints |
| customer-service | `c0278269-6334-4fdb-bdfe-e884eedb205d` | support, help desk |
| dam | `b58d0ef7-55f7-4797-816f-3b992608915e` | digital asset management, repository |
| data | `6b1d6df1-2927-4453-b5a5-12ca3572dfaf` | analytics, database, information |
| data-modeling | `59f39666-05e5-48db-b931-a00de2109633` | schema, planning, architecture |
| database | `986631bc-4b84-46b1-95e7-c0a733e61c95` | storage, records, system |
| decrease | `6c06521f-4510-4d06-af6b-a68b46415ebe` | downward trend, decline |
| developer | `937b9c0a-e4a8-4f5c-a0c2-9d8050513809` | coding, software engineer |
| dislikes | `9f8d5886-a1fa-492e-8d0a-2c53d25863d5` | negative feedback, audience response |
| distribution | `d705984a-224a-43f2-bd30-06b839f421a5` | channel, delivery, reach |
| document | `29ea8d38-dd54-4b76-a889-9adced32b73f` | file, paper, download |
| download | `34a3d7e0-34f0-4c62-afb9-7517dcdad86d` | file transfer, export |
| edit | `1ed48538-94c1-442d-bd9a-d5b4ad6719ae` | modify, update, pencil |
| email | `f5c06037-ce19-447d-a390-1dac64428a8d` | message, inbox, campaign |
| empty-cart | `b56583ae-935e-4352-8ffb-05b82e7aff97` | ecommerce, purchase |
| faq | `74bab8d4-4fd7-46ee-968a-c11862a521d4` | help, questions, answers |
| financial-services | `05f7f852-27b0-4150-841b-caa8344a940e` | banking, insurance, industry |
| government | `f7d1bf00-1d52-4d46-8af7-66e0700279f5` | public sector, policy |
| healthcare | `d3a540a7-bf27-4a2a-b099-5f63208f1dd6` | medical, patient care |
| heart | `a3efe231-d33c-431c-9a15-d2bada2e0cd2` | favorite, like, engagement |
| homepage | `a822e4b0-8cec-43c5-9ea1-e97c58a5f8a3` | home page, navigation, website |
| increased-sales | `66e5643b-2f38-4b56-b15a-aef9dce9c4ce` | growth, revenue increase |
| insurance ‡ | `a44c86f6-0893-428d-8b63-c9175ea8c167` | policy, coverage, protection, shield |
| interaction ‡ | `d449d900-f8ab-4c1d-b464-d2a6b90b8435` | engagement, touchpoint |
| inventory ‡ | `b58972da-ac36-46b5-8ef5-d7b082709a7f` | stock, warehouse, supply |
| it ‡ | `2fb765c1-b735-49f9-b9d0-723e49ed55e9` | information technology, infrastructure |
| json ‡ | `26071743-6e6f-410b-9b9f-ffa3de547803` | data file, code, API |
| jss ‡ | `e6dfc04e-0d58-4b4f-9c64-1137e5ecef2d` | headless, development framework |
| laptop ‡ | `1c894961-6928-48bd-a578-8851b5239754` | computer, device, workstation |
| light-bulb-option ‡ | `7d1e5231-9ff8-4171-8d58-b78b8f579752` | idea, insight, innovation, tip |
| number-1-circle ‡ | `d123be06-89ea-4297-b1af-5f394b0a3bde` | step marker 1 |
| number-2-circle ‡ | `44691684-e2dc-42f5-b791-accb197deaca` | step marker 2 |
| number-3-circle ‡ | `abdf9ab1-257f-423b-b437-29d6b0323e2d` | step marker 3 |
| number-4-circle ‡ | `025c5477-26f0-4946-b631-48f737a1d4cd` | step marker 4 |
| number-5-circle ‡ | `7df06893-39cf-439d-a447-1c64a0b1ee4e` | step marker 5 |
| number-6-circle ‡ | `8d025e3f-a3d0-4c52-b188-04d7121a77f5` | step marker 6 |
| number-7-circle ‡ | `86ad5bcd-e433-4f97-9c63-8da1510de6fd` | step marker 7 |
| number-8-circle ‡ | `d69dba19-e18c-4a85-9607-a3730b4dc09f` | step marker 8 |
| number-9-circle ‡ | `c7911784-1409-4705-a806-d7887d76cf6d` | step marker 9 |
| question-mark-option ‡ | `ecba98dd-753c-434e-86a9-a299100b4b3e` | help, FAQ, inquiry |
| realtime ‡ | `f0080dcc-23fc-4d1f-917e-8eb7e89baa84` | live, instant updates |
| report-builder ‡ | `28ce50df-3b1e-4a02-aada-13df0cba7015` | dashboard, reporting tool |
| retail-banking ‡ | `34ae9e5b-9b9d-44aa-bc3e-c7a75bc5cb6c` | finance, branch, consumer |
| right-arrow ‡ | `f1fead3f-df98-4f4b-8f3c-e685272141b2` | next, forward, direction |
| right-diagonal-arrow ‡ | `1823b9d3-f851-4e8d-afb4-e8e2770e34ef` | external link, upward growth |
| savings ‡ | `e8f28935-a303-4a3a-ad8a-0b16119da6c9` | cost reduction, budget, efficiency |
| search ‡ | `8aaa47ac-48e3-42ac-b5ef-55838442c9e2` | search |
| social-media ‡ | `898727f0-1124-4643-8cb7-70a68c9fce4d` | channels, sharing, engagement |
| speed ‡ | `fdb1ca8f-3bda-4323-896f-c5f115f388a1` | performance |
| success ‡ | `50070db2-6104-4684-bbec-9635442db58b` | achievement, goal, win, results |
| takeaway-option ‡ | `0a8b69d6-23a4-400d-8927-17746e9ce84b` | key takeaway, summary, highlight |
| testing ‡ | `025a1dca-96da-4f5e-b75c-2628499819fb` | experimentation, A/B, QA |
| upload ‡ | `e1eb5d01-de26-4f16-8738-daced230bb41` | file import, transfer |
| video ‡ | `8fa843a6-d99c-4578-bdaa-b86793da81cd` | playback, media content |
| worker ‡ | `78216226-e3d8-4a97-8e48-30d7ddc7e1dc` | **artwork is cogs/gears, not a person** — process, integration, workflow |

**`Images/ABM/Icons2`** — 33 items (duplicate copies of the ‡ names above)

| Name | Asset ID | Association terms |
|---|---|---|
| insurance | `219ab60c-1b13-4c0d-b139-85e5e0fccb49` | policy, coverage, protection, shield |
| interaction | `f8ed68a6-657b-4aa4-8c17-530fec9926cc` | engagement, touchpoint |
| inventory | `bba5c267-9f9f-4752-ace8-713fb8644905` | stock, warehouse, supply |
| it | `de6cfc82-6650-43ff-bddb-809bd41406a2` | information technology, infrastructure |
| json | `08c5c842-78fa-4c86-bdd8-4ba08fcf9bdb` | data file, code, API |
| jss | `fb21fe87-2ab2-4c53-9df6-3318839d0c75` | headless, development framework |
| laptop | `b8e7241e-e3f5-425d-ae58-b56a26d3b234` | computer, device, workstation |
| light-bulb-option | `0edd91fb-3401-4eea-92f8-9c17d13286b2` | idea, insight, innovation, tip |
| number-1-circle | `39cc028a-765b-4860-8b16-ebfaf1fbd515` | step marker 1 |
| number-2-circle | `e4d618ce-f201-4929-813f-b8f5dad9cf55` | step marker 2 |
| number-3-circle | `4c2d07ff-8cbf-40c0-a676-d27c6deb3b8d` | step marker 3 |
| number-4-circle | `fb5e25fc-c7e8-4c22-880c-f6ae0972e2f6` | step marker 4 |
| number-5-circle | `704943fd-e830-43e2-8457-5e7b9ab5ef6e` | step marker 5 |
| number-6-circle | `a1bcbf67-a2a1-49b7-93dc-1e05a26e8d3c` | step marker 6 |
| number-7-circle | `1cb5d68a-8f9a-465d-abd2-dfcd22f445ee` | step marker 7 |
| number-8-circle | `b920453c-972c-4015-a304-39cc9ca6083e` | step marker 8 |
| number-9-circle | `2630f279-3db1-447b-80f7-e41afaab47a2` | step marker 9 |
| question-mark-option | `fa1d51b9-e0c3-4041-8c70-9cc394931591` | help, FAQ, inquiry |
| realtime | `c2c88634-9561-4cca-b9c9-1ebbc46bc042` | live, instant updates |
| report-builder | `04bc2356-0b5a-4c4f-be88-e3417be398f0` | dashboard, reporting tool |
| retail-banking | `7cc22d5b-5709-4e46-a758-0374cd59aef5` | finance, branch, consumer |
| right-arrow | `15198ed3-7395-4ecd-be1f-f25a5a0b5f27` | next, forward, direction |
| right-diagonal-arrow | `9a847293-86f2-4e80-89ab-f685109615f1` | external link, upward growth |
| savings | `774dd7da-60a8-4402-9005-1d8b70edf1f7` | cost reduction, budget, efficiency |
| search | `caa5b7e4-6b61-4d87-828c-ada03a632a63` | magnifying glass, discovery |
| social-media | `44a10f6c-759f-4ff9-9540-70aeacd68d27` | channels, sharing, engagement |
| speed | `ee938e07-4852-4430-bc84-8182675192d1` | performance, velocity, gauge |
| success | `2b1380f2-afd0-461c-9b1e-6c01f447452a` | achievement, goal, win, results |
| takeaway-option | `50609347-cbe6-400d-aaa2-e422656582de` | key takeaway, summary, highlight |
| testing | `53cfb755-5aea-4a7e-b6c6-80080936caf3` | experimentation, A/B, QA |
| upload | `a22032e3-a546-447a-bda1-e170626bc3a2` | file import, transfer |
| video | `398800e3-cc48-4921-979c-51f61f32dbfe` | play, media, streaming |
| worker | `dd1aa7eb-52ff-4be4-ac8c-0c694126bfd1` | **artwork is cogs/gears, not a person** — process, integration, workflow |

## Known image IDs

Full-size imagery and logos under `Images/ABM`. Use `Use image id {GUID}` and match the image to the theme of the slot, never to its position. These tables are the catalog: pick from them. If a slot genuinely has nothing here that fits, the `Populate <FieldName> with the most relevant image you can find in Media Library under Images/ABM` sentence is the fallback — flag it when you deliver, because it usually means this file is missing an asset that belongs in it.

### Sitecore message graphics — `Images/ABM/Sitecore Message Graphics`

SVG product and pillar graphics. Built for the three `SolutionNImage` pillar slots. Never use these in `CaseStudyImage` or `AnalystNLogo` slots, even when repurposing the section. The seven use-case graphics carry a `-hero-image-2400x1257-optimized` suffix in the media library — match on the use-case part of the name.

| Name | Asset ID | Use for |
|---|---|---|
| Run your operations A | `e610b332-9d46-4535-b9e5-93d7373abc11` | Run pillar: operations, efficiency, workflows, governance, agents |
| Expand your presence | `355b904f-5255-4d67-adf0-c01cbd1f1f45` | Expand pillar: AI visibility, discoverability, search, LLM answers |
| Drive your outcomes | `41aa07b3-8a6b-42b5-be0a-e82df69a818e` | Drive pillar: personalization, testing, conversion, outcomes |
| use-case-automate-account-based-marketing-hero-image-2400x1257-optimized | `666949e9-8b97-46ed-b0cc-f1d12a01087f` | ABM, account-based campaigns, campaign automation |
| use-case-connect-ai-assistants-with-mcp-hero-image-2400x1257-optimized | `266fb0df-8778-4687-abb3-a9eb9fec1c1a` | MCP, AI assistants, agent integration, Marketer MCP |
| use-case-find-the-right-digital-asset-hero-image-2400x1257-optimized | `f5d37a42-accb-422d-8e8b-123adda0914a` | DAM, asset search, internal discoverability |
| use-case-manage-multiple-websites-hero-image-2400x1257-optimized | `76757ee2-96df-4ac5-818c-e724b02afb00` | multi-site, multi-brand, regional site management |
| use-case-marketing-campaign-management-hero-image-2400x1257-optimized | `09428aae-ebd3-4893-9308-e3b990684058` | campaign planning, orchestration, performance reporting |
| use-case-website-personalization-hero-image-2400x1257-optimized | `30e0978b-afe6-4b48-b6a1-3c3640a752a2` | personalization, segments, audience targeting |
| use-case-website-translation-localization-hero-image-2400x1257-optimized | `cadb45b3-3a97-4c7f-b683-ab712f410b89` | translation, localization, multilingual rollout |

### Case study backgrounds — `Images/ABM/Case Study Backgrounds`

Landscape industry photography. Built for `CaseStudyImage`, and useful for `SolutionNImage` when the pillar is about the account's own industry rather than a Sitecore capability. Pick by the account's sector.

| Name | Asset ID | Size | Use for |
|---|---|---|---|
| broward-country-case-study-background | `52227dd3-3b92-413f-8104-ec93dd4275a2` | 800 x 378 | the canonical Broward County story, US counties, public sector |
| city-government-institution-bank-photography | `82ad9dac-9634-4867-82f6-241b0be9de6a` | 876 x 522 | government, public institutions, civic and institutional banking |
| college-university-school-education-teaching-photography | `97a83978-dc77-476d-961e-6b64ada7e920` | 1100 x 732 | education, universities, training, research |
| energy-sustainable-wind-landscape-photography | `2537595d-4e27-41bc-be3b-31d21e3b9222` | 1100 x 734 | energy, utilities, sustainability, ESG |
| healthcare-hospital-doctor-photography | `555fdb23-80c0-41e9-a71a-ed8f630ed576` | 980 x 580 | healthcare, hospitals, life sciences, patient experience |
| makeup-cosmetics-fashion-lifestyle-happy-photography | `b9f69daa-e967-4520-b75a-6f8a00c8e92a` | 1100 x 734 | beauty, cosmetics, fashion, consumer lifestyle brands |
| manufacturing-production-supply-photography | `837c2492-55a8-48d5-aea5-7d94a46abc0a` | 1100 x 706 | manufacturing, industrials, production, supply chain |
| payment-shopping-online-bank-card-transaction-money-photography | `5510f535-708d-448d-b0a5-864b9cbdaa24` | 1100 x 734 | financial services, payments, retail and ecommerce checkout |
| pets-dogs-funny-food-photography | `62bfe927-1757-4214-9329-b859ea5693d4` | 1100 x 734 | pet care, food and beverage, CPG |
| travel-airline-holiday-beach-hospitality-photography | `cd098708-6448-470d-9671-e8032d873ad8` | 1100 x 618 | travel, airlines, hotels, hospitality, leisure |

### Analyst logos — `Images/ABM/Analyst Logos`

Transparent PNGs for the `AnalystNLogo` slots.

| Name | Asset ID | Use for |
|---|---|---|
| forrester-logo-transparent | `e1a8996a-0e7a-4c8d-8efd-e1d2900c2d0a` | Forrester — TEI/ROI and Wave proof points |
| gartner-logo-transparent | `b620d09d-d477-4fd5-8ee1-bf37cec8c23f` | Gartner — Magic Quadrant proof points |
| idc-logo-transparent | `398645da-9973-477d-b425-3b86ecdce4e9` | IDC — MarketScape and analyst proof points |

### Customer logos — `Images/ABM/Customer Logos`

Sitecore customer logos, for social proof: a logo strip, or a `SolutionNImage` / card slot where a recognisable peer brand does more work than an icon. **Pick peers in the target account's own sector** — a logo from an unrelated industry reads as filler. Never put a customer logo in an icon slot (see the icon library rule above), and never imply a partnership the logo doesn't support.

| Name | Asset ID | Use for |
|---|---|---|
| Bayer-logo-color | `25567b82-9351-45de-8c30-faa391751f21` | pharma, life sciences, agriculture |
| BeyondBlue-Logo-Color | `fae45b6a-5926-4d4b-a7ab-3fc448ab0187` | non-profit, mental health, public health |
| British_Red_Cross_logo | `99337f84-3950-4c59-8f97-fb8b05f4d26d` | non-profit, humanitarian, charity |
| Canon_wordmark | `f431cdf2-2b13-4c44-80cd-697cd3c5c6a9` | electronics, imaging, manufacturing |
| ECG-logo | `913b6f7c-ab3b-439a-bc15-d4e0ce4d714e` | healthcare consulting, professional services |
| Emirates-Logo | `1e9fea31-2bf3-4212-92b4-9c314b9a6d9e` | airline, travel, hospitality |
| enmax-logo-color | `49e0c0d6-3c23-4b18-a9d0-a70d3b9afc76` | energy, utilities |
| Fujitsu-Logo | `137652a2-5daf-4109-9875-fc84c37537fc` | IT services, technology |
| HSBC-logo | `d8fc7098-f05a-4727-ae5d-4f91dcd28088` | banking, financial services |
| komatsu-logo | `cba6b2e8-e13d-4554-84df-d375a5ac4993` | manufacturing, heavy equipment, industrials |
| LogoofBrowardCountyFlorida | `4fb3a7c2-1263-4c64-bc29-63a542bac937` | US counties, public sector, local government |
| Michelin-Logo | `5583f5ab-056b-407c-8950-86d3b5daca2d` | manufacturing, automotive, tyres |
| Procter and Gamble Logo | `f5314b51-e16e-4615-b4a7-9717aae217a1` | CPG, consumer brands, multi-brand |
| Royal-Canin-Logo | `d9810ba9-39db-4832-a72a-5d9fc5a7f3e6` | pet care, CPG |
| Suncoast Credit Union | `4a8fd6e1-784c-4800-bbdb-087ec3bcb896` | credit union, retail banking, financial services |
| the_tile_shop-logo-color | `62951464-df59-4094-be90-f9c5def1315c` | retail, home improvement, ecommerce |
| Thule-Logo | `5088d5c8-9b58-418e-8da0-84cc6d576e02` | retail, outdoor, consumer goods |
| Toyota-logo-color | `94961290-1031-4126-a10c-ead6c748be5b` | automotive, manufacturing |
| united-airlines-logo-color | `ec19a6d8-e115-4cec-a464-e9884a63bf38` | airline, travel, hospitality |
| Upmc-logo | `a269ab75-a264-4358-a0d8-7807970b0889` | healthcare, hospitals, payer-provider |
| velux-logo-color | `b5e30ccf-ff2d-4d0f-a145-9ce7283bebb7` | manufacturing, building products |
| WAGO-logo-color | `85604291-33cc-42b2-8617-9d42adcb06c1` | manufacturing, industrial automation |
| wellspan-logo-color | `d1f0a62f-e7aa-4291-aa0b-6fb0047945c4` | healthcare, hospital networks |

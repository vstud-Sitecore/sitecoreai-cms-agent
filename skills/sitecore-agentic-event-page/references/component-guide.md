# Agentic Event Page component and handoff guide

Field names, types and layout were recorded against the Sitecore Marketing WWW environment on 29 October 2026. Revalidate against the connected environment before writing. This is a template reference, not approved event copy. Supply the actual event brief and its approved assets at build time.

## Layout and limits

The verified template has eight preconfigured renderings in headless-main: Agentic Event Hero, Agentic Event Audience, Agentic Event Overview, Agentic Event Takeaways, Agentic Event Agenda, Agentic Speakers, Agentic Event FAQ, Agentic Event CTA. Registration fields are inherited on the page item. Preserve the event template's presentation and inspect each new page. Do not build from the ABM component kit.

Hero: EventHeroImage, EventHeroEyebrow, EventHeroHeading, EventHeroSubheading.
Details: EventStartDateTime, EventEndDateTime, EventDateTagline, EventTimeTagline, HideTimeDetails, EventLocation, EventLocationTagline, EventLogoHeading, EventLogo1 through EventLogo8.
Audience: EventAudienceTitle, EventAudienceDescription. Job-role bullets render with markers separating the roles.
Overview: EventOverviewEyebrow, EventOverviewHeading, EventOverviewSubheading; either EventOverviewImage OR EventOverviewQuote with EventOverviewQuoteTagline.
Takeaways: EventTakeawaysEyebrow/Heading/Subheading and EventKeyInfo; up to six EventKeyPointHeadingN + EventKeyPointN pairs. Use EventKeyInfo for useful details such as duration/materials, with confirmed facts.
Agenda: EventAgendaEyebrow/Heading/Subheading/Timetable/Footnote. EventAgendaTimetable needs an HTML table, not Markdown table syntax. Keep local session times aligned with the confirmed event schedule.
Speakers: SpeakersEyebrow/Heading/Subheading; up to nine SpeakerNName/Headshot/JobRole/CompanyName/Bio/SocialLink entries. A name is required to display that speaker; optional missing details stay blank.
FAQ: EventFAQEyebrow/Heading/Subheading, up to eight EventFAQQuestionN + EventFAQAnswerN pairs.
CTA: EventCTAEyebrow/Heading/Subheading, EventCTAButton, EventCTAButtonText. For a verified native form, #event-form scrolls to that form.

Unused entries stay blank, with no invented fillers. The request form permits removing an unused whole section under Presentation > Details; the connector requires explicit user confirmation for component removal. Blank field content does not prove a rendering has disappeared.

Paired asterisks mark highlight phrases in EventHeroHeading, EventOverviewHeading, EventTakeawaysHeading, EventAgendaHeading, SpeakersHeading and EventFAQHeading. Do not turn those single-line fields into HTML, and do not apply the ABM rule that bans all Markdown-like characters to these intentional highlights.

Event start/end are entered as event-local times in the brief; record a named timezone and explicit offsets. Sitecore examples use UTC datetime storage. Convert instants deliberately, then confirm what the preview actually displays. HideTimeDetails hides time details when appropriate, for example a multi-day event; it does not remove the need for a confirmed schedule or select a folder date.

Location: prefer a linked venue name in EventLocation and the address in EventLocationTagline. For a virtual event describe the joining arrangement honestly; do not publish private attendee meeting links unless intended for public use.

## Registration and references

FormType default Event: 807b51b0-87b8-45ea-a752-fbbfc25385b0.
Webinar alternative: 271b50d2-9283-4885-bcf3-1aecf78bcbf6.
Resolve against /sitecore/content/Marketing/Shared/Data/Form Types (and site-specific options when supplied). Form type definitions must be valid members of the live field Source.
Program status source: /sitecore/content/Marketing/Shared/Data/Resources/Forms/Program Status.
Campaign products source: /sitecore/content/Marketing/Shared/Data/Resources/Forms/Campaign Products.
No event-specific default program status or Salesforce campaign was established. Ask for the real campaign and use only an applicable existing dropdown option; do not invent an Event - Registered reference or borrow an ABM campaign.

Native form core fields: FormType, FormTitle, FormIntroText, FormSubmitText, FormDefaultSalesforceCampaignID, FormDefaultProgramStatus when supplied, FormDefaultCampaignProducts when relevant, FormConfirmationMessage and/or FormRedirectURL. Other inherited fields are listed in schema.json. Preserve privacy, consent, CSRF and captcha defaults.

General links are Sitecore XML, e.g. an external URL: <link linktype="external" url="https://example.com/register" text="Register" />. A form anchor can use <link linktype="anchor" anchor="event-form" text="Register" />. XML-escape ampersands and quotes. Verify actual rendered anchors and links; the example syntax is not proof of functioning registration.

## Metadata, assets and taxonomy

Use MetadataTitle/Description/Keywords, OpenGraphTitle/Description/Image, InternalSearchImage, JsonLdMarkup, ContentOwnership, ContentType and relevant GlobalTaxonomies. JSON-LD belongs in JsonLdMarkup as valid JSON-LD based on confirmed event facts. Do not emit a script tag in a text field. Keep event names, dates, locations and registration URLs consistent with the visitor-facing content. Actual rendered JSON-LD still needs inspection.

OpenGraphImage must be JPEG or PNG for the event workflow; reject SVG/WebP for this slot. Use approved media for hero/overview and genuine participant headshots/logos. The helper checks XML and required DAM metadata shape; verify each media ID/URL, asset rights and format live.

NoIndexNoFollow is a negative control: 1 means request noindex/nofollow. Explain the actual indexing choice and agree whether the event should be discoverable. Do not force noindex for all events. Select relevant existing taxonomy IDs by their live sources. The event reference groups them as audience, event type, interests, products/capabilities, regions, verticals and year. Existing example years 2026/2027 are not a permanent year limit. Taxonomy regions and inherited form Region are distinct concepts; do not assume identical values.

## Handoff JSON contract

Top-level keys: pageName (lowercase hyphenated slug), language, timeZone (named event timezone), start/end (ISO 8601 local timestamps with explicit UTC offsets), destinationParent (exact Events Webinars/YYYY/MM path), registrationMode (native or external), fields (object keyed by exact CMS field names). Sources, asset/reference evidence and pending questions belong in the readable mapping, outside fields. For portability the handoff can additionally carry sources/evidence notes outside fields.

fields values are strings ready for the live field datatype, or null to skip writing. Blank string means intentional clear. Use UTC yyyyMMddTHHmmssZ strings for EventStartDateTime/EventEndDateTime. Use a verified media-library image XML value or the complete verified Content Hub image XML. The helper requires either a mediaid or all of src, dam-id, dam-content-type, width, height and thumbnailsrc. Live asset identity and rendering must still be verified. Do not substitute a URL string for an image XML value. Use existing GUIDs for droplinks and pipe-separated GUIDs for treelistex. Rich text accepts HTML, including the agenda table. Plain fields accept plain text; preserve only documented asterisk emphasis in headings.

The packaged prepare.py validates the handoff and prints the required parentPath, pagePath, creation inputs without parentId, and an update_fields_on_item-compatible field array. Resolve parentId live after checking/creating the exact folders; it cannot be safely generated offline. It does not create or publish anything.

## Supported field manifest

The following 173 supported inherited content/design fields were verified from each base template and direct missing speaker-field paths. This is a supported authoring surface, not every Sitecore system/legacy field. If another field is needed, inspect its live definition and deliberately extend the manifest rather than guessing. The direct parent template and speaker template responses were capped at 50; this manifest includes verified fields beyond that cap.

### Base Page

| Exact field | Type |
|---|---|
| BaseTaxonomies | treelistex |
| ContentOwnership | treelistex |
| ContentType | droplink |
| CustomMetadata | name value list |
| GlobalTaxonomies | treelistex |
| InternalSearchImage | image |
| JsonLdMarkup | multi-line text |
| MetadataDescription | multi-line text |
| MetadataKeywords | multi-line text |
| MetadataTitle | single-line text |
| NoIndexNoFollow | checkbox |
| OpenGraphDescription | multi-line text |
| OpenGraphImage | image |
| OpenGraphTitle | single-line text |

### _Designable

| Exact field | Type |
|---|---|
| Page Design | droplink |

### Event Hero

| Exact field | Type |
|---|---|
| EventDateTagline | single-line text |
| EventEndDateTime | datetime |
| EventHeroEyebrow | single-line text |
| EventHeroHeading | single-line text |
| EventHeroImage | image |
| EventHeroSubheading | rich text |
| EventLocation | rich text |
| EventLocationTagline | single-line text |
| EventLogo1 | image |
| EventLogo2 | image |
| EventLogo3 | image |
| EventLogo4 | image |
| EventLogo5 | image |
| EventLogo6 | image |
| EventLogo7 | image |
| EventLogo8 | image |
| EventLogoHeading | single-line text |
| EventStartDateTime | datetime |
| EventTimeTagline | single-line text |
| HideTimeDetails | checkbox |

### Event Audience

| Exact field | Type |
|---|---|
| EventAudienceDescription | rich text |
| EventAudienceTitle | single-line text |

### Event Overview

| Exact field | Type |
|---|---|
| EventOverviewEyebrow | single-line text |
| EventOverviewHeading | single-line text |
| EventOverviewImage | image |
| EventOverviewQuote | single-line text |
| EventOverviewQuoteTagline | single-line text |
| EventOverviewSubheading | rich text |

### Event Takeaways

| Exact field | Type |
|---|---|
| EventKeyInfo | single-line text |
| EventKeyPoint1 | rich text |
| EventKeyPoint2 | rich text |
| EventKeyPoint3 | rich text |
| EventKeyPoint4 | rich text |
| EventKeyPoint5 | rich text |
| EventKeyPoint6 | rich text |
| EventKeyPointHeading1 | single-line text |
| EventKeyPointHeading2 | single-line text |
| EventKeyPointHeading3 | single-line text |
| EventKeyPointHeading4 | single-line text |
| EventKeyPointHeading5 | single-line text |
| EventKeyPointHeading6 | single-line text |
| EventTakeawaysEyebrow | single-line text |
| EventTakeawaysHeading | single-line text |
| EventTakeawaysSubheading | rich text |

### Event Agenda

| Exact field | Type |
|---|---|
| EventAgendaEyebrow | single-line text |
| EventAgendaFootnote | rich text |
| EventAgendaHeading | single-line text |
| EventAgendaSubheading | rich text |
| EventAgendaTimetable | rich text |

### Speakers

| Exact field | Type |
|---|---|
| Speaker1Bio | rich text |
| Speaker1CompanyName | single-line text |
| Speaker1Headshot | image |
| Speaker1JobRole | single-line text |
| Speaker1Name | single-line text |
| Speaker1SocialLink | single-line text |
| Speaker2Bio | rich text |
| Speaker2CompanyName | single-line text |
| Speaker2Headshot | image |
| Speaker2JobRole | single-line text |
| Speaker2Name | single-line text |
| Speaker2SocialLink | single-line text |
| Speaker3Bio | rich text |
| Speaker3CompanyName | single-line text |
| Speaker3Headshot | image |
| Speaker3JobRole | single-line text |
| Speaker3Name | single-line text |
| Speaker3SocialLink | single-line text |
| Speaker4Bio | rich text |
| Speaker4CompanyName | single-line text |
| Speaker4Headshot | image |
| Speaker4JobRole | single-line text |
| Speaker4Name | single-line text |
| Speaker4SocialLink | single-line text |
| Speaker5Bio | rich text |
| Speaker5CompanyName | single-line text |
| Speaker5Headshot | image |
| Speaker5JobRole | single-line text |
| Speaker5Name | single-line text |
| Speaker5SocialLink | single-line text |
| Speaker6Bio | rich text |
| Speaker6CompanyName | single-line text |
| Speaker6Headshot | image |
| Speaker6JobRole | single-line text |
| Speaker6Name | single-line text |
| Speaker6SocialLink | single-line text |
| Speaker7Bio | rich text |
| Speaker7CompanyName | single-line text |
| Speaker7Headshot | image |
| Speaker7JobRole | single-line text |
| Speaker7Name | single-line text |
| Speaker7SocialLink | single-line text |
| Speaker8Bio | rich text |
| Speaker8CompanyName | single-line text |
| Speaker8Headshot | image |
| Speaker8JobRole | single-line text |
| Speaker8Name | single-line text |
| Speaker8SocialLink | single-line text |
| Speaker9Bio | rich text |
| Speaker9CompanyName | single-line text |
| Speaker9Headshot | image |
| Speaker9JobRole | single-line text |
| Speaker9Name | single-line text |
| Speaker9SocialLink | single-line text |
| SpeakersEyebrow | single-line text |
| SpeakersHeading | single-line text |
| SpeakersSubheading | rich text |

### Event FAQ

| Exact field | Type |
|---|---|
| EventFAQAnswer1 | rich text |
| EventFAQAnswer2 | rich text |
| EventFAQAnswer3 | rich text |
| EventFAQAnswer4 | rich text |
| EventFAQAnswer5 | rich text |
| EventFAQAnswer6 | rich text |
| EventFAQAnswer7 | rich text |
| EventFAQAnswer8 | rich text |
| EventFAQEyebrow | single-line text |
| EventFAQHeading | single-line text |
| EventFAQQuestion1 | single-line text |
| EventFAQQuestion2 | single-line text |
| EventFAQQuestion3 | single-line text |
| EventFAQQuestion4 | single-line text |
| EventFAQQuestion5 | single-line text |
| EventFAQQuestion6 | single-line text |
| EventFAQQuestion7 | single-line text |
| EventFAQQuestion8 | single-line text |
| EventFAQSubheading | rich text |

### Event CTA

| Exact field | Type |
|---|---|
| EventCTAButton | general link |
| EventCTAButtonText | single-line text |
| EventCTAEyebrow | single-line text |
| EventCTAHeading | single-line text |
| EventCTASubheading | rich text |

### Form Datasource

| Exact field | Type |
|---|---|
| DisableCSRF | checkbox |
| DisableProgressiveFunctionality | checkbox |
| DisableQueryStringOverride | checkbox |
| Email | droplink |
| FormConfirmationMessage | rich text |
| FormDefaultCampaignProducts | droplink |
| FormDefaultProgramStatus | droplink |
| FormDefaultSalesforceCampaignID | single-line text |
| FormGoal | droplink |
| FormHostType | droplink |
| FormIntroText | rich text |
| FormPartnerName | single-line text |
| FormPrivacyPolicyLink | general link |
| FormRedirectURL | general link |
| FormSubmitText | single-line text |
| FormTitle | single-line text |
| FormType | droplink |
| LastInterestingMomentDescription | single-line text |
| LeftAlignFormTitleAndIntroText | checkbox |
| ProgressiveForm | droplink |
| ReCaptcha | checkbox |
| RetargetingUrl | single-line text |
| SetRetargetingUrl | checkbox |

### Form Defaults

| Exact field | Type |
|---|---|
| Company Name | single-line text |
| Province | single-line text |
| Region | single-line text |
| State | single-line text |
| Territory | single-line text |

## Observed rendering and workflow behavior

The fixed layout may automatically hide empty optional sections; confirm in preview before considering a component removal. Date/time display and image handling need separate checks: src-only DAM image XML resolves to an empty object in WWW, and stored UTC times have appeared as UTC clock times. Preserve correct scheduled instants and use the explicit local-time display fallback described in SKILL.md if needed.

CMS reads by path have returned null workflow/version metadata while reads of the same item by ID returned Draft. Use the item-ID read when checking workflow, and only assign a verified site content workflow and non-final Draft state to a new page if absent. A successful update call alone is not a workflow check.

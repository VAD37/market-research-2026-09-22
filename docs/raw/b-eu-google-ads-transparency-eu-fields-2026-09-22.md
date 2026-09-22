# Google Advertising Policies Help — Ads transparency (Germany/EU view)

```yaml
source:          Google Advertising Policies Help
url_or_doc_id:   https://support.google.com/adspolicy/answer/13733850?hl=en&co=GENIE.CountryCode%3DDE
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own docs
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Google — AI Overviews, AI Mode, Gemini; also Google Search generally
metric_kind:     none
supersedes:      none
captured:        full page (article element), get_page_text, country view forced to Germany (DE) via URL parameter
```

## Verbatim

"Your confidence in Google's products and services is essential. Google wants to empower you to make informed decisions about the ads and advertisers you see through Google services by providing greater transparency about who our advertisers are, where they're located, and which ads they show."

"**Ads Transparency Center**

Google provides a searchable repository of advertisers and the ads they've served on Google platforms like Search, Display, Gmail, and YouTube. You can search for advertisers to learn more about them and the ads they've run during a certain time period. You can search for an advertiser via the Ads Transparency Center using the advertiser or website name and filter your search results by details like date and targeted location."

"**Information about the ad campaigns**

In the Ads Transparency Center and in ad disclosures, Google will show advertiser information such as the advertiser name, location, the entity that pays for the ads, and the ads they have served over a certain time period for all advertisers serving ads on Google platforms including Google Search and YouTube."

"**View additional information disclosed by location**

For ads served in certain countries or regions, Google will make the following additional information available in the Ads Transparency Center.

**Germany**
Targeting information
Total number of recipients for each ad
Subject matter label of the ad (at times Google-generated)

Google provides API access to data about ads served in the EEA in the Ads Transparency Center. Access to and usage of the data in the Ads Transparency Center is subject to the Ads Transparency Center terms of service.

Google may provide regulators and self-regulatory organizations with API access to existing data from the Ads Transparency Center about ads served outside of the EEA."

## Pull notes — mechanical only

- The page's list of covered surfaces — "Search, Display, Gmail, and YouTube" — names none of Google's AI-answer surfaces (AI Overviews, AI Mode, Gemini) explicitly. "Google Search" is named as a covered platform; whether an AI Overviews or AI Mode ad unit (as distinct from a classic Search results-page ad) is treated as a "Google Search" ad for this repository's purposes is **not stated anywhere on this page** — recorded as `unknown — checked support.google.com/adspolicy/answer/13733850 2026-09-22`.
- EU/EEA-specific fields confirmed, additive to the base field set: targeting information; total number of recipients per ad; subject-matter label (sometimes Google-generated). Base fields (all locations): advertiser name, location, payer entity, ads served over a time period.
- **Machine-readable: yes** — "Google provides API access to data about ads served in the EEA in the Ads Transparency Center," gated by that API's own terms of service (not captured in this pull).
- An earlier attempt in this pull session to reach `adstransparency.google.com` directly redirected to a Vietnamese-region view (`?region=VN`) reflecting this session's browser locale, not an EU view, and returned essentially no page text beyond a "Political ads" label — the live searchable tool itself was not usefully reached in English/EU mode in this pull. This help-center page is the substitute primary source for the EU field list.

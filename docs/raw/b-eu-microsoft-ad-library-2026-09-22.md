# Microsoft Advertising Help — About the Ad Library (Article 39 EU ad repository)

```yaml
source:          Microsoft Advertising Help
url_or_doc_id:   https://help.ads.microsoft.com/apex/index/3/en/60180 ; repository itself at https://adlibrary.ads.microsoft.com/
published:       undated — no date on page (footer copyright "© 2026 Microsoft")
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own docs
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Bing / Microsoft Copilot, model version n/a
metric_kind:     none
supersedes:      none
captured:        full page (body element), get_page_text
```

## Verbatim

"About the Ad Library

The Microsoft Ad Library is a public-facing repository of ads served by Microsoft Advertising on Bing in the European Union (EU) and European Economic Area (EEA). The Ad Library includes ads which received impressions in the EU and the EEA regardless of advertiser location. ... Individuals may search for ads in the Ad Library by ad content or the advertiser and may filter by dates and/or the country or countries where the ad was served."

"**Information included in the Ad Library**

Select View ad details when searching for ads to learn more about them, including:

Advertiser name and the country, or countries, where the advertiser is located
Who paid for the ad, if different from the advertiser
A representative copy of each ad, including ad content, images, and links
The start and end dates of the ad
Estimated reach (total estimated impressions for ads delivered in the EU/EEA and a percentage breakdown by country)
General targeting criteria the advertiser chose for the ad

Either the advertiser ID or account ID will be visible in the Ad Library URL that's associated with the advertiser. ... Please note that the advertiser ID or account ID are also available in the Ad Library API."

"As an advertiser, can I opt out from my ads being shown in the Ad Library? No. Pursuant to the EU Digital Services Act, all ads served on Bing in the EU must be publicly available in the Ad Library. Additionally, all ad types are eligible to appear in the Ad Library."

"What ad types are eligible to appear in the Ad Library? App Install ads, Audience ads, Dynamic Search ads, Hotel Price ads, Multimedia ads, Product ads, Responsive Search ads, text ads, and Vertical ads are eligible to appear in the Ad Library if they served were served on Bing through the Microsoft Advertising Network and received impressions in the EU/EEA. Ad extensions are excluded."

"What advertisements are included in the Ad Library? The Ad Library includes all ads served on Bing through the Microsoft Advertising Network that have received impressions in the EU/EEA. The advertisers can be located in both the EU/EEA and non-EU/EEA countries."

"Ads appear in the Ad Library within 24-48 hours after receiving their first eligible impression. ... After an ad stops running, it remains in the Ad Library exactly one year after the date of its last eligible impression."

"Who can access the Ad Library? The Ad Library is available for everybody in all countries."

"What is ad targeting? Ad targeting allows advertisers to focus on reaching potential customers who meet their targeting criteria, including age, gender, location, and audiences associated with their audience lists."

## Pull notes — mechanical only

- Supersedes the earlier lower-confidence pull of this same target (search-tool synthesis rather than direct fetch), which is being kept as-is per the raw-pull rule against editing after the fact; this file is the direct, verbatim capture.
- **Named ad-unit types**: "App Install ads, Audience ads, Dynamic Search ads, Hotel Price ads, Multimedia ads, Product ads, Responsive Search ads, text ads, and Vertical ads." No ad type named "Copilot ad," "chat ad," or any conversational-surface-specific unit. The repository is framed entirely around "ads served on Bing" through "the Microsoft Advertising Network" — the page never once names "Copilot."
- **Fields exposed** (structured list, per the page's own "Information included" heading): advertiser name and country/countries; payer, if different from advertiser; ad creative (content, images, links); start/end date; estimated reach (EU/EEA total impressions, with a percentage breakdown by country); general targeting criteria; advertiser ID or account ID.
- **Machine-readable: yes** — an "Ad Library API" is named twice (advertiser ID/account ID "are also available in the Ad Library API"), though this page does not itself document the API's endpoint, schema, or authentication.
- Whether any entry in this repository is an ad shown specifically inside a Copilot conversational answer, as opposed to a classic Bing search-results-page ad, is **not stated anywhere on this page** — recorded as `unknown — checked help.ads.microsoft.com/apex/index/3/en/60180 2026-09-22`. Per P2-c6's already-landed findings (`docs/method/STATE.md`), Copilot ads reuse the existing Microsoft Advertising Network ad types (Multimedia, Product, Search-with-logo, Vertical) — all four of which are named on this Ad Library page as eligible ad types — so a Copilot-served ad of one of those types would structurally qualify for inclusion, but this page gives no confirmation that any such ad has in fact appeared there.

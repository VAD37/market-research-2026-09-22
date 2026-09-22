# FTC — Native Advertising: A Guide for Businesses

```yaml
source:          Federal Trade Commission, Business Guidance
url_or_doc_id:   https://www.ftc.gov/business-guidance/resources/native-advertising-guide-businesses
published:       undated — no date on page (staff-level "Guide for Businesses" supplementing the FTC's December 2015 Enforcement Policy Statement on Deceptively Formatted Advertisements, per the guide's own reference to "the Enforcement Policy Statement"; the guide page itself carries no visible publication or last-reviewed date in the captured text)
pull_date:       2026-09-22
pull_method:     browser extension (also cross-checked via WebFetch, which loaded this URL directly without the 202/redirect behaviour seen on eur-lex.europa.eu and ecfr.gov)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default for platform/regulator-own guidance page — informal FTC staff guidance, not itself a codified rule (the codified rule is 16 CFR Part 255, pulled separately in this cluster)
source_label:    company-stated
lane:            B, D
sub_market:      paid placement
engine:          n/a — cross-engine regulatory guidance
metric_kind:     none
supersedes:      none
captured:        the "watchword is transparency" disclosure-standard paragraph; "Example 7" (content-recommendation-widget / "More Content for You" native-ad labelling scenario)
```

## Verbatim

### Core transparency and disclosure standard

"...resentation that it comes from a party other than the sponsoring advertiser.

What do businesses need to know to ensure that the format of native advertising is not deceptive? The Enforcement Policy Statement explains the law in detail, but it boils down to this:

From the FTC's perspective, the watchword is transparency. An advertisement or promotional message shouldn't suggest or imply to consumers that it's anything other than an ad.

Some native ads may be so clearly commercial in nature that they are unlikely to mislead consumers even without a specific disclosure. In other instances, a disclosure may be necessary to ensure that consumers understand that the content is advertising.

If a disclosure is necessary to prevent deception, the disclosure must be clear and prominent.

II. Examples of when businesses should disclose that content is native advertising

In digital media, native ads often resemble the design, style, and functionality of the media in which they are disseminat[note: truncated at tool output limit]"

### Example 7 — content-recommendation widget

"...ormation relating to vacuum cleaners, and not an ad developed and published on behalf of a sponsoring advertiser. Thus, effective disclosures informing consumers of the ad's commercial nature – both in the site's feed and on the click-into infographic – are necessary to prevent deception.

Example 7

A content recommendation widget included on different publisher sites displays links to external pages. One site on which these third-party links are placed is Newsby. On the Newsby site, these links are formatted to look like news headlines and are grouped together in a box with headings like "More Content for You," or "From Around the Web." One of the headlines appearing in the box is for the Winged Mercury ad described in Example 4, "Running Gear Up: Mistakes to Avoid." The similarity of the Winged Mercury ad's format to the type of headlines Newsby publishes on its site, combined with phrases like "More Content for You," or "From Around the Web," is likely to lead consumers to belie[note: truncated at tool output limit]"

## Pull notes — mechanical only

- Unlike eur-lex.europa.eu and ecfr.gov, `WebFetch` loaded this ftc.gov URL directly (no 202/redirect block); the Chrome extension was additionally used to independently confirm the exact wording (the two matched on every sentence checked).
- Same truncation constraint as the other pulls in this cluster: the JS-execution tool caps returned strings at roughly 1000-1100 characters, so quotes above are cut at `[note: truncated at tool output limit]`. Examples 1 through 6 of this guide, and the end of Example 7's disclosure recommendation, were not captured.
- This page names no AI system, chatbot, or AI assistant anywhere in the text captured. "Example 7" is the closest analogue in this Guide to an algorithmically-curated recommendation surface (a "content recommendation widget"), but the widget described is a syndicated-links box on a publisher's own site, not a conversational AI answer — the applicability of this example's reasoning to an AI-assistant-generated product recommendation is not stated by the source and is not asserted here.
- No explicit "last reviewed" or publication date was found in the captured DOM text of this specific page; the December 2015 date commonly associated with the FTC's Native Advertising materials refers to the separate "Enforcement Policy Statement on Deceptively Formatted Advertisements" that this Guide explicitly supplements, not to a date printed on this guide's own page as pulled today. Recorded as `unknown — checked www.ftc.gov/business-guidance/resources/native-advertising-guide-businesses 2026-09-22` in the summary file.

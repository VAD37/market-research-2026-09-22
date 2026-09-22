# Meta Transparency Center — Meta Ad Library tools

```yaml
source:          Meta, Transparency Center
url_or_doc_id:   https://transparency.meta.com/researchtools/ad-library-tools/
published:       "UPDATED AUG 24, 2023"
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own docs
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Meta AI (via Facebook/Instagram, Meta's only DSA-designated services), model version n/a
metric_kind:     none
supersedes:      none
captured:        full page (main element), get_page_text
```

## Verbatim

"UPDATED AUG 24, 2023

Meta's comprehensive hub for ads transparency

**Ad Library**

Meta Ad Library is a comprehensive, searchable database for ads transparency. People can use the Ad Library to get more information about the ads they see across Meta technologies.

People can search for all active ads running across products from Meta. For ads about social issues, elections or politics, Meta provides additional information, including spend, reach and funding entities. These ads are visible whether they're active or inactive and are stored in the Ad Library for 7 years.

**Meta offers more information for ads that deliver an impression in the EU or associated territories. These ads are displayed in the Ad Library while active and archived for one year upon the delivery of their last impression.** The Ad Library also has a searchable database that displays all active, public branded content running on Facebook and Instagram with a paid partnership label.

Learn more about the types of data available in the Ad Library.

**Ad Library API**

The Ad Library API is an application programming interface that allows for a deeper analysis of ads about social issues, elections or politics, as well as ads that deliver to the EU and associated territories. Authorized users can also analyze active and public branded content running on Facebook and Instagram via the API.

**Ad Library Report**

The Ad Library Report provides an aggregated and comprehensive view of ads about social issues, elections or politics in a selected country for a given time period. ...

**Ad Targeting dataset**

The Ad Targeting dataset allows approved researchers to analyze targeting information selected by advertisers who ran ads about social issues, elections or politics any time after August 2020 in more than 120 countries. ..."

## Pull notes — mechanical only

- This page never names "Meta AI" as a product surface — its scope is "products from Meta," explicitly named elsewhere on the page as "Facebook and Instagram" (the paid-partnership-label branded-content database line). Meta AI is not separately designated as a VLOP/VLOSE on the Commission's list (`b-eu-ec-designated-vlops-vloses-list-2026-09-22.md`) — only Facebook and Instagram are. Whether any ad or sponsored content shown inside a Meta AI conversational answer is included in this Ad Library is **not stated anywhere on this page** — recorded as `unknown — checked transparency.meta.com/researchtools/ad-library-tools/ 2026-09-22`.
- **Machine-readable: yes** — an "Ad Library API" is named and described (scope: social-issue/election/political ads, plus EU-delivered ads, plus branded content).
- EU-specific field detail (targeting parameters, demographic reach breakdown, beneficiary/payer, member-state-level reach) was reported by the web-search tool prior to this direct pull but was not independently re-confirmed by this page's own text — this page states only that Meta "offers more information for ads that deliver an impression in the EU," without itemizing the field names. Recorded as `unknown — checked transparency.meta.com/researchtools/ad-library-tools/ 2026-09-22` for the exact EU field list beyond what is quoted above; a deeper Meta Transparency Center sub-page ("Learn more about the types of data available in the Ad Library," linked but not followed) likely carries the itemized list and was not reached in this pull.
- Page's own "UPDATED AUG 24, 2023" date is more than one quarter stale relative to `query-book.md`'s split date rule for surface-state questions (`after:2026-06-22`) — flagged `stale — published 2023-08-24` per `plan.md`'s staleness rule. The page's content may not reflect any Meta Ad Library changes made since 2023.

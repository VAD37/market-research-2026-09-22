# Buyer-size band attribution — headcount for named high-CPA employers, vendor customers and conference names (S1, S2, S7, S8)

```yaml
source:          LinkedIn company pages (linkedin.com/company/*); Revelio Labs, LeadIQ, Tracxn, ZoomInfo workforce-data profiles; Wikipedia company infoboxes; Primerica, Inc. public statements
url_or_doc_id:   linkedin.com/company/geico ; linkedin.com/company/amica-mutual-insurance-co ; linkedin.com/company/embrace-pet-insurance ; linkedin.com/company/insurify ; linkedin.com/company/the-juice-plus-company ; linkedin.com/company/simply-business_39914 ; linkedin.com/company/jerryinc ; zurich.co.uk/careers/about-zurich ; en.wikipedia.org/wiki/The_Hartford ; linkedin.com/company/aetna ; reveliolabs.com/companies/midfirst-bank ; reveliolabs.com/companies/primerica ; tracxn.com/d/companies/nerdwallet ; reveliolabs.com (Mutual of Omaha) ; reveliolabs.com/companies/franklin-templeton-asset ; reveliolabs.com/companies/john-lewis-partnership
published:       live pages / profiles, undated; underlying headcounts dated per row below
pull_date:       2026-09-23
pull_method:     WebSearch — search-tool-synthesized figures from the pages named per row, not independently fetched page-by-page
pull_purpose:    evidence about a number
tier:            5
tier_reason:     workforce-data aggregators (Revelio Labs, LeadIQ, Tracxn, ZoomInfo) do not publish their headcount-estimation method on the page; LinkedIn's own "People" count is platform-primary (tier 3) but is read here through a search-tool synthesis, not the page itself — held at 5 per trust-rubric.md's "hidden method drops one tier" plus the indirect capture
source_label:    company-stated (LinkedIn self-reported headcount) / analyst-derived (aggregator estimates), per row
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        one headcount figure (or a small range where sources disagree) per company, with its source and as-of date where stated
verbatim:        partial — figures as returned by the search tool from each named page, not the page's full text
```

## Verbatim, per company — figures as returned, side by side where sources disagree, never averaged

| Company | Vertical role | Figures found, verbatim as returned | Band (headcount, `demand-signals.md` bands) |
|---|---|---|---|
| GEICO | S1 employer, insurance | "26,142 employees as of March 2026" (Revelio Labs); "over 40,000 associates" (GEICO's own LinkedIn page text) | **Enterprise** — both figures exceed 1,000 |
| Amica Mutual Insurance | S1 employer, insurance | "Amica Insurance has 3,132 employees listed on their jobs page" (LinkedIn); "3,524 employees as of December 2025" (Revelio Labs) | **Enterprise** |
| Embrace Pet Insurance | S1 employer, insurance | "company size ... 51-200 employees" (LinkedIn band, via search aggregation); "approximately 202 employees" as of August 2026, "201" as of 2026-07-31 (LeadIQ) | **Mid-market** — exact-count sources (201–202) exceed the 100 SMB ceiling; the LinkedIn band label straddles SMB/mid-market. Recorded per the exact count, not the label |
| Insurify | S1 employer, insurance | "51-200 employees" (LinkedIn band, via Inc.com); "approximately 166 people" (GetLatka, 2026); "approximately 242 employees" as of July 2026, "233" as of June 2026 (LeadIQ) | **Mid-market** — every exact count (166–242) exceeds 100 |
| The Juice Plus+ Company | S1 employer, supplements | "3,875 employees according to its LinkedIn profile" | **Enterprise** |
| Simply Business | S1 employer, insurance | "851 employees according to LinkedIn"; "approximately 850 employees as of July 2026" | **Mid-market** |
| Jerry.ai (Jerry Inc.) | S2 vendor customer, insurance | "approximately 392 employees" as of July 2026; "394 employees as of May 26" (Tracxn) | **Mid-market** |
| Zurich Insurance UK | S2 vendor customer, insurance | "employs over 5,000 people" (Zurich's own careers page, via search); "approximately 5,000 people in the UK" | **Enterprise** |
| The Hartford (Hartford Financial Services Group) | S2 vendor customer, insurance | "approximately 27,220 employees in 2026" (Wikipedia); "21,742" as of 2026-06-30 (Tracxn); "18,100" (Owler) | **Enterprise** — every figure exceeds 1,000; not averaged |
| Aetna (a CVS Health company) | S2 vendor customer, insurance | "approximately 41,000 employees" as of June 2026; "just under 40,000 employees" | **Enterprise** |
| MidFirst Bank | S2 vendor customer, cards/banking | "1,948 employees" (LinkedIn jobs page count); "2,648 employees as of December 2025" (Revelio Labs); "more than 3,300 employees" (LinkedIn profile text); "1,640" (SignalHire) | **Enterprise** — every figure exceeds 1,000; four sources disagree, not averaged |
| Primerica, Inc. | S7 filing subject, insurance | "45,392 people worldwide as of December 2025" (total, "up 141 (+0.3%) from the prior year"); "over 2,800 corporate employees who support over 151,000 licensed independent representatives" | **Enterprise** on either the total or the corporate-only figure |
| NerdWallet, Inc. | S7/S8 subject, cards/finance | "the latest employee count at NerdWallet is 735" as of 2026-06-30 (Tracxn) | **Mid-market** |
| Mutual of Omaha | S8 conference name, insurance | "more than 6,000 employees" (company careers page, via search); "approximately 9.5K employees across 6 continents" as of July 2026 (LeadIQ/Revelio-style aggregator) | **Enterprise** — every figure exceeds 1,000 |
| Franklin Templeton | S8 conference name, finance | "9,800 employees as of 2025" (company financial statements, via search); "11,278 employees/professionals" (PitchBook); "approximately 12K employees" as of September 2025 (LeadIQ) | **Enterprise** |
| John Lewis Financial Services (unit); John Lewis Partnership (parent) | S8 conference name, insurance/finance | No standalone figure found for the Financial Services unit. Parent: "around 74,000 employees as of 2024" (Wikipedia); "26,615 employees as of December 2025" (Revelio Labs, entity recorded as "John Lewis Partnership Trust Ltd."); "69,000 ... known as Partners" (Statista) | **Enterprise**, via the parent only — the Financial Services unit's own headcount is `unknown — checked LinkedIn, Wikipedia, Statista, Revelio Labs, ZoomInfo 2026-09-23`; parent used per `demand-signals.md`'s proxy order (no filing or careers page gave the unit a number) |

## Pull notes — mechanical only

- Every row above is a WebSearch synthesis over the named pages, not an independent fetch of each page's full text; multiple aggregators are quoted side by side per company because they disagree, per root `CLAUDE.md` ("conflicting figures sit side by side, attributed, never averaged").
- No company here discloses a company-defined size band of its own (e.g., "we are a 1,000-employee enterprise") — every band above is mapped from a raw headcount figure to the `demand-signals.md` bands (SMB under 100; mid-market 100–999; enterprise 1000 or more).
- John Lewis Financial Services: the source that names it in this repo (`raw/f-signal-hr-S8-conferences-2026-09-22.md`, MozCon London) is a division of John Lewis Partnership, not a separately reported entity in any aggregator found. The parent figure is recorded as the nearest available proxy, with the gap stated, not guessed past.
- No login, no account, no CAPTCHA encountered — all data reached through WebSearch result synthesis.

# Ziff Davis — Form 10-K FY2025 and Form 10-Q Q2 2026: OpenAI copyright suit; no AI content-licensing revenue line

```yaml
source:          Ziff Davis, Inc., CIK 0001084048 — Form 10-K fiscal year ended 2025-12-31 (accession 0001084048-26-000005) and Form 10-Q quarter ended 2026-06-30 (accession 0001084048-26-000046)
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1084048/000108404826000005/zd-20251231.htm ; https://www.sec.gov/Archives/edgar/data/1084048/000108404826000046/zd-20260630.htm
published:       2026-02-24 (10-K); 2026-08-07 (10-Q) — EDGAR file dates
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid", sec.gov Archives HTTP 200; HTML tag-stripped; grep for "OpenAI", "content licens", "licensing revenue", "generative AI")
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed
source_label:    filed
lane:            B
sub_market:      n/a — publisher / sell-side monetisation
engine:          OpenAI (defendant)
metric_kind:     none
supersedes:      none
captured:        legal-proceedings paragraphs naming OpenAI (both filings); revenue-definition sentences for "subscription and licensing revenues"
```

## Verbatim

10-K FY2025 — Item 1 and Item 3 (identical wording in both places):

> On April 24, 2025, the Company and certain of its subsidiaries filed a lawsuit against OpenAI, Inc. in the United States District Court for the District of Delaware, alleging copyright infringement, violations of the Digital Millennium Copyright Act, unjust enrichment and trademark dilution as a result of OpenAI's unlawful and unauthorized copying and use of the Company's content. On May 14, 2025, the Judicial Panel for Multidistrict Litigation consolidated our case with others pending against OpenAI in the Southern District of New York.

10-Q Q2 2026 — legal proceedings:

> On April 24, 2025, the Company and certain of its subsidiaries filed a lawsuit against OpenAI, Inc. in the United States District Court for the District of Delaware, alleging copyright infringement, violations of the Digital Millennium Copyright Act and unjust enrichment as a result of OpenAI's unlawful and unauthorized copying and use of the Company's content. On May 14, 2025, the Judicial Panel for Multidistrict Litigation consolidated our case with others pending against OpenAI in the Southern District of New York.

10-K FY2025 — revenue definitions:

> Our revenues consist of revenues from (i) advertising and performance marketing revenues, which are earned from the delivery of advertising services, marketing, performance marketing, and production services, and (ii) subscription and licensing revenues, which are earned through the granting of access to, or delivery of, certain data products or services to customers, usage-based fees, and by reselling various t[hird-party solutions — truncated at 400 characters in this pull]
> Licensing revenues are earned through the license of certain assets to clients. Licensing revenues also include revenues from transactions involving the sale of perpetual software licenses, related software support, and maintenance.

10-Q Q2 2026 — revenue definitions (same structure):

> Subscription and licensing revenues are earned from (i) subscription services with performance obligations that are satisfied over time; and (ii) licensing arrangements that have standalone functionality with performance obligations satisfied at a point in time [...]

## Pull notes — mechanical only

- Case-insensitive grep for "content licens" and "generative AI" in both filings returns no revenue statement; "licensing" occurs only inside the "subscription and licensing revenues" segment metric (Gaming & Entertainment, Health & Wellness, Connectivity, Cybersecurity & Martech), which is software and data licensing, not AI content licensing.
- The 10-Q's legal paragraph drops "trademark dilution" from the 10-K's list of claims; both quoted verbatim, side by side.
- No settlement, licence agreement or AI-company partner is named in either filing.

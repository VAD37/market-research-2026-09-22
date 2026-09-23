# News Corp — Form 10-K, fiscal year ended 2026-06-30: content-licensing statements (no dollar line)

```yaml
source:          News Corp, CIK 0001564708 — Form 10-K, fiscal year ended June 30, 2026, accession 0001564708-26-000175
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1564708/000156470826000175/nws-20260630.htm
published:       2026-08-07 (EDGAR file date)
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid", sec.gov Archives HTTP 200; HTML tag-stripped; grep for "content licens", "AI compan", "OpenAI", "artificial intelligence")
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed
source_label:    filed
lane:            B
sub_market:      n/a — publisher / sell-side monetisation
engine:          n/a — "OpenAI" does not occur in the filing text
metric_kind:     none
supersedes:      none
captured:        every sentence containing "content licens" or "AI companies" (Item 1 strategy, Item 1 IP, Dow Jones and News Media MD&A, purchase-obligation footnote)
```

## Verbatim

Item 1 — strategy:

> The Company expects to continue to pursue various strategic initiatives, incorporate new technologies and develop new and enhanced products and services to remain competitive. These include additional licensing arrangements with large platform operators, AI companies and other partners for the use of its content, the continued expansion into different business models and adjacencies, streaming audio partnerships for its books, multi-product digital bundles and other innovative digital news products and experiences. The Company is also developing products and services that incorporate AI solutions to enhance insights and value for consumers and customers and using AI to improve efficiency and productivity internally. The Company has incurred, and expects to continue to incur, significant costs in connection with these efforts [...]
> For example, not all of the Company's content license agreements have been renewed, and there is no guarantee that existing agreements will be renewed on terms favorable to the Company or at all.

Item 1 — intellectual property:

> The Company derives value and revenue from its intellectual property assets through, among other things, digital and print newspaper and magazine subscriptions and sales, the sale of subscriptions to its content and information services, content licensing, the operation of websites and other digital properties and the sale, distribution and/or licensing of print and digital books.

Dow Jones segment description:

> Revenue from the Dow Jones segment's news products is derived primarily from circulation, which includes individual consumer and enterprise customer subscriptions and single-copy sales of its digital and print news products, the sale of digital and print advertising, licensing fees for its print and digital content and participation fees for its live journalism events.

MD&A — Dow Jones, fiscal 2026 vs fiscal 2025:

> Circulation and subscription revenues increased $136 million, or 7%, for the fiscal year ended June 30, 2026 as compared to fiscal 2025. Professional information business revenues increased $85 million, or 9%, primarily due to the $55 million and $23 million increases in Dow Jones Risk & Compliance and Dow Jones Energy revenues, respectively, driven by price increases, new customers and product expansion. Circulation and other revenues increased $51 million, or 5%, driven by increased digital circulation revenues due to the conversion of customers from introductory promotions to higher pricing and growth in digital-only subscriptions, driven by enterprise customers, and higher content licensing revenues, partially offset by print circulation declines. Digital revenues represented 76% of circulation revenue for the fiscal year ended June 30, 2026, as compared to 74% for fiscal 2025.

MD&A — News Media, fiscal 2026 vs fiscal 2025:

> For the fiscal year ended June 30, 2026, revenues at the News Media segment increased $57 million, or 3%, as compared to fiscal 2025. Circulation and subscription revenues increased $57 million, or 5%, as compared to fiscal 2025, primarily due to the $43 million, or 4%, positive impact of foreign currency fluctuations, price increases, higher content licensing revenues and digital subscriber growth in the U.K., partially offset by print volume declines. Advertising revenues decreased $16 million, or 2%, as compared to fiscal 2025, primarily due to lower print advertising revenues, partially offset by the $28 million, or 3%, positive impact of foreign currency fluctuations.

Contractual obligations footnote:

> (a) The Company has commitments under purchase obligations related to technology infrastructure services, marketing agreements, content licensing costs and other legally binding commitments.

## Pull notes — mechanical only

- Case-insensitive grep for "OpenAI" returns zero hits in the FY2026 10-K text. The 2024 OpenAI agreement referenced in earlier raws (`raw/e-case-*` Dow Jones rows) is not named in this filing.
- No dollar figure is attached to content licensing at any layer; it appears only as a driver inside "Circulation and other revenues" (Dow Jones) and "Circulation and subscription revenues" (News Media).
- Filing located via data.sec.gov/submissions (EDGAR full-text search walled to this session; see `raw/b-sec-reddit-10q-q2-2026-content-licensing-2026-09-23.md` pull notes).

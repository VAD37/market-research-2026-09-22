# Amazon — quarterly results releases: Rufus / Alexa for Shopping users, incremental sales, advertising

```yaml
source:          Amazon.com, Inc. — quarterly results releases (aboutamazon.com newsroom; ir.aboutamazon.com)
url_or_doc_id:   https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2025-report ; https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report ; https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx
published:       2025-10-30 ; 2026-02-05 ; 2026-07-30 (dates as given by the fetch tool)
pull_date:       2026-09-23
pull_method:     fetch (WebFetch, sentence extraction — partial)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — company's own results release; the same text is furnished as 8-K Ex. 99.1 (sec.gov URLs seen in search results, not opened)
source_label:    company-stated
lane:            C (agentic commerce), also E (Pass 13 user counts)
sub_market:      agentic commerce; paid placement (ad revenue baseline)
engine:          Amazon — Rufus / Alexa for Shopping
metric_kind:     sales (incremental annualized sales); none (user counts)
supersedes:      none
verbatim:        partial — quoted sentences only
captured:        sentence extracts
```

## Verbatim

### Q3 2025 results — 2025-10-30
- "Saw strong usage of Rufus (AI-powered assistant in Amazon's store), with 250 million customers using it this year."
- "Shoppers using Rufus are 60% more likely to complete a purchase."

### Q4 2025 results — 2026-02-05
- "Rufus can shop tens of millions of items in other online stores directly and make purchases on behalf of customers using its agentic Buy For Me feature."
- "Rufus was used by 300 million+ customers and saw an even stronger response than anticipated, helping deliver nearly $12 billion in incremental annualized sales last year."
- "Announced that Alexa+ is available to all customers in the U.S. for $19.99 per month as a standalone subscription, and free for Prime members."

### Q2 2026 results — 2026-07-30
- "Brought together Rufus and Alexa+ into Alexa for Shopping, an agentic AI shopping assistant that offers personalized recommendations, product comparisons, price history, and the ability to automate shopping through features like Price Alerts and Auto-Buy. Worldwide customer adoption and engagement accelerated in Q2, with active users close to doubling and interactions up over 5x year-over-year."
- Advertising services revenue "grew 26% year-over-year to $19.8 billion in Q2 2026" [note: as summarised by the fetch tool, not a verbatim sentence]

## Pull notes — mechanical only
- businesswire.com copies of the three releases returned HTTP 403 to WebFetch.
- Metric definitions: "customers using it this year" (2025-10-30) and "used by 300 million+ customers" (2026-02-05, calendar 2025) are cumulative-in-year counts, not monthly actives; 2026-07-30 gives a ratio only ("active users close to doubling"), no absolute.
- "incremental annualized sales" — Amazon's own term; method not stated in the release.

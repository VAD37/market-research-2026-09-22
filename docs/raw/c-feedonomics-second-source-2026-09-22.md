# StockTitan — Commerce.com Series 1 (CMRC) stock news page — admission-rule second source for Feedonomics

```yaml
source:          StockTitan (stocktitan.net) — third-party financial-news aggregator, independent of Commerce/Feedonomics
url_or_doc_id:   https://www.stocktitan.net/news/CMRC/
published:       page aggregates releases through 2026-09-10; page itself undated as a standalone document
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool, plain HTTP, no browser needed)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     adjusted down from table default 3 — StockTitan's "Rhea-AI Summary" content is AI-generated summarization of the underlying press release/filing, not the filing itself; used here (consistent with this repo's prior practice in P3-c2/P3-c3, e.g. a-changeagents-funding-filing-2026-09-22.md, a-hubspot-filing-2026-09-22.md) as a substitute for a direct sec.gov pull, which returned HTTP 403 to this session's fetch tool (robots.txt-based autonomous-fetch refusal, matching every prior P2/P3 cluster's identical finding per docs/method/STATE.md)
source_label:    analyst-derived
lane:            C
sub_market:      agentic commerce
engine:          n/a — financial reporting on the parent company, not an assistant engine
metric_kind:     sales
supersedes:      none
captured:        page excerpt — company description plus the two most recent news items at pull time
```

## Verbatim

"Commerce.com Series 1 (CMRC) Stock News | StockTitan"

"Welcome to our dedicated page for Commerce.com Series 1 news (Ticker: CMRC), a resource for investors and traders seeking the latest updates and insights on Commerce.com Series 1 stock."

"Commerce.com, Inc. reports developments across its open, AI-driven commerce ecosystem for merchants and brands. **The company operates technology solutions associated with BigCommerce, Feedonomics and Makeswift**, including SaaS ecommerce storefronts, product data optimization, channel connections, B2B commerce, payments and AI-assisted shopping experiences."

"Recurring news for CMRC includes quarterly financial results, annual recurring revenue, subscription solutions revenue, gross merchandise volume, product launches, PayPal-related payments and catalog integrations, **Feedonomics agentic catalog capabilities**, merchant platform migrations, customer wins and regional partner awards. Updates also reflect the company's position as the renamed successor to BigCommerce Holdings, Inc. and its focus on data-centric commerce infrastructure."

"09/10/2026 08:00 AM — News — Commerce Announces Strategic Operating Plan to Accelerate Profitability and Free Cash Flow Generation — Rhea-AI Summary: Commerce (CMRC) announced a strategic operating plan targeting at least 20% full-year non-GAAP operating margins beginning in 2027, plus a new $50 million share repurchase authorization effective through September 10, 2028. The plan is expected to reduce the annualized non-GAAP operating cost base by approximately $60 million to $80 million... For 2026, total revenue guidance is reaffirmed at $336.5 million to $344.5 million, while non-GAAP operating income guidance is raised by $3 million to $31.0 million to $37.0 million."

"08/06/2026 07:00 AM — News — Commerce Announces Second Quarter 2026 Financial Results — Rhea-AI Summary: Commerce (Nasdaq: CMRC) reported Q2 2026 revenue of $84.5 million, up 0.1% year over [year, truncated by tool output limit]"

## Pull notes — mechanical only

- Fetched via plain HTTP fetch tool. Content truncated by the tool's max_length after the Q2 2026 summary's first sentence; not re-fetched at a higher start_index in this pull since the load-bearing fact (Commerce/CMRC is a Nasdaq-listed public company whose reported business lines explicitly include Feedonomics) was already captured.
- Direct sec.gov / efts.sec.gov EDGAR access was attempted first and refused: `mcp__MCP_DOCKER__fetch` reported `"When fetching robots.txt (https://www.sec.gov/robots.txt), received status 403 so assuming that autonomous fetching is not allowed"` for both `www.sec.gov/cgi-bin/browse-edgar` and `efts.sec.gov/LATEST/search-index` — identical to the block already logged by P3-c2 and P3-c3 in `docs/method/STATE.md`. This StockTitan pull is the substitute, per the same precedent those clusters set.
- **Admission-rule role of this file**: this is the second, independent-of-Feedonomics source required by this task's rewritten P3-c6 admission rule, alongside source 1 (`docs/raw/c-paypal-protocol-agentic-commerce-2026-09-22.md`, PayPal's own partner page naming "Commerce (BigCommerce & Feedonomics)"). StockTitan is a third-party financial-news aggregator with no ownership or commercial relationship to Commerce/Feedonomics disclosed on this page, satisfying the roster rule's "two or more independent non-listicle sources" test (limb (a)) for Feedonomics.
- Revenue figures ($336.5M–$344.5M 2026 guidance, $84.5M Q2 2026 revenue) are Commerce-wide (BigCommerce + Feedonomics + Makeswift combined), not broken out per subsidiary on this page — recorded as Commerce-level, not claimed as a Feedonomics-specific revenue figure. `unknown — checked stocktitan.net/news/CMRC 2026-09-22, no Feedonomics-only revenue line item found`.

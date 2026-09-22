# Shopify — Shopify Delivers Again as Merchants Clear $100 Billion in Q1 GMV

```yaml
source:          Shopify (Shopify Newsroom / press release; quotes attributed to Harley Finkelstein, President, and Jeff Hoffmeister, CFO, Shopify)
url_or_doc_id:   https://www.shopify.com/news/shopify-q1-2026-financial-results
published:       2026-05-05
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     adjusted down from the P2-c8 shortlist's table default of 5 — this is a standard quarterly financial press release (filed-adjacent, GAAP/non-GAAP disclosure) with no AI-specific breakout at all; kept only as platform-scale context, not as an AI-referral figure
source_label:    vendor-reported
lane:            C
sub_market:      agentic commerce
engine:          n/a — no engine named; no AI attribution breakout in this release at all
metric_kind:     sales
note:            the "$100 billion" GMV figure is total platform Gross Merchandise Volume across all of Shopify's channels for Q1 2026 (quarter ended March 31, 2026) — it is NOT AI-referral-attributed and carries no AI-specific breakout anywhere in this release. Included only as the population/scale denominator against which the AI-specific figures in c-shopify-analytics-ai-search-insights-q1-2026-09-22.md (same Q1 2026 window) sit. Not an "influenced revenue" figure — it is total reported GMV, GAAP/non-GAAP financial disclosure.
supersedes:      none
captured:        full page (excluding the non-GAAP reconciliation table, not reproduced)
```

## Verbatim

"Shopify Delivers Again as Merchants Clear $100 Billion in Q1 GMV
May 5, 2026
by Shopify

May 5, 2026 - Shopify announced today financial results for the quarter ended March 31, 2026. Shopify achieved 34% revenue growth and 15% free cash flow margins.

'Shopify has entered the AI era with a clear edge: strong, durable growth and two decades of commerce intelligence. That puts us in a category of one, and we're about to see that advantage compound throughout 2026,' said Harley Finkelstein, President of Shopify.

Jeff Hoffmeister, Chief Financial Officer, said, 'Q1 delivered broad-based growth across geographies, merchant sizes, and channels, with over $100 billion of GMV in the first quarter alone. That is the platform compounding. The durability of this model allows us to invest strategically in growth, both in the merchant-facing tools that drive commerce innovation and in the internal capabilities that let us build and ship faster.'

...

2026 Outlook

...For the second quarter of 2026, we expect:
Revenue to grow at a high-twenties percentage rate on a year-over-year basis;
Gross profit dollars to grow at a mid-twenties percentage rate on a year-over-year basis;
Operating expenses as a percentage of revenue to be 35% to 36%;
Stock-based compensation to be $145 million; and
Free cash flow margin to be in the mid-teens.

...

Gross Merchandise Volume, or GMV, represents the total dollar value of orders facilitated through the Shopify platform including certain apps and channels for which a revenue-sharing arrangement is in place in the period, net of refunds, and inclusive of shipping and handling, duty, and value-added taxes."

## Pull notes — mechanical only

- Full page loaded and captured in a single `get_page_text` call, no retry needed.
- No paywall, login wall, or truncation encountered.
- Non-GAAP financial-statement reconciliation tables at the foot of the release were present but not reproduced (out of scope — no AI-specific content).
- Screened for an AI-attributed GMV/order breakout; none found on this page. Cross-reference only: this quarter (Q1 2026) is the same window as the AI-specific session/order figures in `c-shopify-analytics-ai-search-insights-q1-2026-09-22.md`, but the two are not directly combinable — this file's $100B is total GMV, not AI-referral GMV.

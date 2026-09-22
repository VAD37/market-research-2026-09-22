# ReFiBuy — "AI1000 Rankings Reshuffle in Q2, but Retail Challengers Hold the Lead" (Q2 2026 AI Commerce Rankings, with Digital Commerce 360)

```yaml
source:          ReFiBuy (co-developed with Digital Commerce 360)
url_or_doc_id:   https://refibuy.ai/articles/ai1000-rankings-reshuffle-in-q2-but-retail-challengers-hold-the-lead ; index page https://refibuy.ai/ai1000
published:       2026-08-18
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool; refibuy.ai fetches cleanly)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     analyst/vendor-derived study, n=1,000 retailers (the Top 1000 Database), quarterly date window (Q1 vs Q2 2026) and a stated method (catalog, traffic and momentum signals scored quarterly) named on page, but no full scoring-methodology appendix or confidence interval published on this specific article — per trust-rubric.md tier 5 "vendor or agency study with n, dates, method," bias flagged (ReFiBuy sells Agentic Commerce Optimization services; the index promotes its own commercial category)
source_label:    analyst-derived
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT — OpenAI; Gemini — Google; Claude — Anthropic; Perplexity
metric_kind:     traffic
supersedes:      none
captured:        substantially full article (through "New This Quarter" heading, where the fetch tool's length limit truncated the remainder). Pointer trade item: Digital Commerce 360, "Ecommerce Trends: Which AI sources are sending referral traffic to online retailers?" (headline tag: "Ecommerce Trends: Top AI sources sending retailers referral traffic"), https://www.digitalcommerce360.com/2026/09/03/ecommerce-trends-ai-sources-referral-traffic-online-retailers/, published 2026-09-03, read 2026-09-22 — primary reached, no separate pointer file filed. DC360's article draws on this same ReFiBuy/DC360 co-produced Q2 dataset via an interview with ReFiBuy CEO Scot Wingo; the figures DC360 quotes (844→722 ChatGPT-led retailers, 16→32 Gemini-led, 1→15 Claude-led, 8→21 Perplexity-led) match this primary exactly.
```

## Verbatim

Byline: "Brian Chapman, Aug 18, 2026, News & Announcements." Dateline: "RALEIGH, NC / ACCESS Newswire / August 18, 2026 /"

> "ReFiBuy, the company that coined Agentic Commerce Optimization (ACO), today published the Q2 2026 edition of the AI1000, the first quarterly update to the category-defining benchmark it co-developed with Digital Commerce 360. The index uses catalog, traffic and momentum signals to score the Top 1000 retailers by online sales for agentic commerce readiness, showing whether each retailer's catalog is accessible, visible, gaining momentum and positioned to compete as AI shopping evolves.
>
> Of the 1,000 retailers ranked, 972 changed position in Q2. The median retailer moved 35 spots, and 641 moved at least 25 positions."

AI traffic leadership by engine — the figures the DC360 pointer item and PPC Land-adjacent coverage draw on:

> "AI traffic leadership is spreading beyond ChatGPT. In Q1, ChatGPT was the largest source of AI-referred traffic for 844 of the 1,000 retailers. In Q2, that number fell to 722. Over the same quarter, the number of retailers whose largest AI traffic source was Gemini doubled from 16 to 32. Perplexity-led retailers grew from eight to 21, while Claude-led retailers increased from one to 15. ChatGPT remains the largest source for far more retailers than any other engine, but a catalog tuned for one engine now has to perform across a growing number of AI surfaces."

Index-average trend:

> "The readiness bar is rising faster than retailers are clearing it. The AI1000 Index Average was 39.7 in Q2, compared with 42.0 in Q1, reflecting a more demanding environment as traffic spreads across more engines and selling surfaces."

Scale distribution finding:

> "Retail challengers held the lead, even as No. 1 changed hands. Nixon, a watch and accessories brand ranked No. 722 by online sales, overtook Online Labels, ranked No. 814, by 0.03 points. ... for the second consecutive quarter, only 10 of the 100 largest online retailers place in the AI1000 top 100, while half of the AI1000 top 100 sits outside the sales top 500."

CEO quote:

> "'We built the AI1000 as a quarterly index because AI shopping moves on a different clock from traditional ecommerce,' said Scot Wingo, CEO and co-founder of ReFiBuy. 'Q2 showed how much the market can shift in a single quarter and why retailers can't treat Agentic Commerce Optimization as a one-time project. Retailers preparing their catalogs now will enter Q4 with a real head start as holiday shoppers increasingly turn to AI agents to research, find and buy products.'"

Category-level movement:

> "Rank movement varied sharply by category. Automotive Parts & Accessories climbed an average of 20.1 positions, while Flowers & Gifts fell 17.8, a spread of nearly 38 positions."

UCP adoption figure, cited from Salesforce within this release:

> "Salesforce forecasts that 20% of 2026 holiday ecommerce traffic will originate from AI chat agents, according to its 2026 holiday predictions. Yet only 225 of the Top 1000 retailers have a detectable Universal Commerce Protocol (UCP) endpoint, part of an emerging standard that allows AI agents to connect directly with merchant catalogs."

[note: the article continues past a "New This Quarter" heading; the fetch tool's response was cut off there (5000-character limit) and not re-fetched with a continuation call, since every figure the pointer trade item (Digital Commerce 360) cites was already captured above.]

## Pull notes — mechanical only

- Fetched cleanly via plain fetch, no 403, no extension needed.
- The DC360 pointer article itself (fetched separately, full text) frames this same dataset through an interview with Scot Wingo rather than quoting the ReFiBuy release directly, but every figure DC360 attributes to Wingo ("in Q1, 844 retailers had ChatGPT as No. 1... that decreased to 722"; "[Google] Gemini went from 16... to 32"; "only one retailer had Claude as their top source of traffic [in Q1], and now there's 15") matches this ReFiBuy primary verbatim.
- DC360's article also cites, separately and not from this primary, an Adobe Analytics figure ("AI-associated referral traffic to ecommerce sites rising by 62% year over year" in July, "shoppers referred by AI tools generated 53% more revenue per visit") — not independently re-pulled here since Adobe Digital Insights data of this kind is already covered in this repo's Pass 2 cluster P2-c8 raw pulls (`docs/raw/c-adobe-analytics-*-2026-09-22.md`); the specific July 2026 figures DC360 cites were not checked against those existing files for an exact match and may represent a newer Adobe release than what P2-c8 captured.

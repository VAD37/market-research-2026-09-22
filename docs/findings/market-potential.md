# Market potential — user counts, trends, forecasts and floors, three sub-markets

| | |
|---|---|
| File date | 2026-09-23 |
| Oldest pull depended on | 2026-09-22 (Pass 2/3/6 raw). Oldest source date carried: 2024-01-04, `raw/e-perplexity-user-query-counts-2026-09-23.md` |
| Lane · hypotheses touched | E, reading A, B and C · H16, H21, H22 |
| Claims at tier 3 or better | 3 of 7 (C1, C2, C7) |

## Question

> How large and how fast does each sub-market read — organic, paid, agentic — from engine user counts, share and referral trends, published forecasts, and floors built only from disclosed inputs?

## Answer

Observations, not a verdict. Six of nine engines publish two or more dated user counts; Claude, Perplexity and DeepSeek do not. Every engine with two numeric points grew between them (Meta's two read the same), but no two engines use the same metric. Referral share moved from ChatGPT to Gemini on both series that carry both. AI tools stay under 2% of US desktop search events. Forecasts disagree 1.9× (organic, 2034) to 26× (agentic, 2030). Disclosed floors: organic ARR in the tens of millions of USD, paid ≥$1B run rate on one engine, agentic checkout volume undisclosed.

## Evidence

**(i) Engine user counts, as each engine names the metric.** Raw prefix `raw/`, suffix `-2026-09-23.md` unless stated.

| Engine | Metric, engine's words | Dated points | Tier | Raw |
|---|---|---|---|---|
| ChatGPT | "weekly active users" | 700M 2025-09-15 · 900M 2026-02-27 · ">1 billion" 2026-08-31 | 3 | `e-openai-chatgpt-user-counts` |
| Gemini app | "monthly active users" | 400M (2025-05, as restated) · 450M 2025-07-23 · 650M 2025-10-29 · 750M 2026-02-04 · 900M 2026-05-19 · 950M 2026-07-22 | 3 | `e-google-alphabet-user-counts` |
| AI Overviews · AI Mode | monthly (active) users; AI Mode once DAU | AIO 2B 2025-07-23 · 2.5B 2026-05-19. AI Mode 100M US+India 2025-07-23 · 75M DAU 2025-10-29 · 1B 2026-05-19 | 3 | same |
| Microsoft Copilot | "family of Copilot apps" MAU | 100M 2025-07-30 · 150M 2025-10-29; consumer app ratios only | 3 | `e-microsoft-copilot-user-counts` |
| Meta AI | "monthly actives" | "more than a billion" 2025-07-30 · 2025-10-29; ratios only after | 3 | `e-meta-ai-user-counts` |
| Grok | MAU "that used Grok's AI features" | 89M 2025-12-31 · 117M 2026-03-31 | 2 | `e-spacex-s1a-grok-mau` |
| Amazon Rufus | customers using it in-year | 250M 2025-10-30 · "300 million+" 2025 (stated 2026-02-05); "close to doubling" 2026-07-30 | 3 | `c-amazon-rufus-user-sales-statements` |
| Perplexity | MAU; queries | 10M MAU, "over half a billion queries in 2023" (2024-01-04, t3) · 780M queries May 2025 (t5 title) | 3/5 | `e-perplexity-user-query-counts` |
| Claude · DeepSeek | none | Claude: EU "well below the 45 million threshold", 6 mo to 2025-10-31; run rate "$14 billion" 2026-02-12. DeepSeek: `unknown — checked WebSearch 2026-09-23` | 3 · 7 | `e-anthropic-claude-scale-statements`; `e-engine-user-count-checks` |

**(ii) Share and referral trends, one definition per row.**

| Series, definition | Points | Method | Tier | Raw |
|---|---|---|---|---|
| StatCounter AI-chatbot referral share, worldwide | ChatGPT 84.21% → 79.4%; Gemini 2.31% → 10.93%; Perplexity 12.07% → 4.34%; Claude 0.3% → 2.53% (2025-04 → 2026-08) | referral pageviews, tagged sites; FAQ published | 4 | `e-statcounter-share-monthly-series` |
| Similarweb gen-AI web-visit share | ChatGPT ~76% → ~53%; Gemini <9% → ~27–28%; Claude ~2% → ~9% (Jun 2025 → May 2026) | panel named, size undisclosed | 4 | `a-similarweb-share-gen-ai-stats-2026-09-22.md` |
| Similarweb AI referral visits to sites | 770.7M/month avg, Jun 2025–May 2026, "+117.4%" YoY | same panel, six named engines | 4 | `a-similarweb-ai-referral-industry` |
| Datos, AI tools share of desktop search events | US 1.31% (Jan–Mar 2025) → 1.65% (Jan–Mar 2026); EU/UK 0.54% → 1.08% (Jan 2025 → Mar 2026) | clickstream; primary gated (form) | 5 | `a-ppc-land-share-datos-q1-2026-2026-09-22.md` |
| StatCounter search-engine referral share | Google 89.89% → 91.02%; Bing 3.92% → 4.55% (2025-08 → 2026-08) | as row 1 | 4 | `e-statcounter-share-monthly-series` |
| Adobe AI traffic to US retail | "Up 393% YoY" Jan–Mar 2026; "Up 138% YoY" May 2026 | Adobe Analytics customers | 4 | `c-retail-analytics-table-2026-09-22.md` |
| Baseline — Google Search & other revenue | $175,033M (2023) → $198,084M (2024) → $224,532M (2025) | 10-K | 2 | `b-alphabet-10k-2025-search-revenue` |

**(iii) Forecasts per sub-market, per target year.** Every row a forecast, never a size; * new this pass. Raw: `raw/e-market-size-table-2026-09-22.md` rows 1–18; new — `e-market-size-marketsandmarkets-organic`, `-coherent-organic`, `-marketintelo-organic-agentic`, `-mediapost-emarketer-aisearch-paid`, `-wppmedia-midyear-paid`, `-juniper-agentic`, `-mordor-agentic`, `-nextmsc-agentic`, all `-2026-09-23.md`. Single-forecast years: organic 2031 Valuates $7.318B, 2032 MarketsandMarkets* $4.25B; agentic 2028 Gartner B2B $15T, 2029 EMARKETER $144B, 2031 Mordor* $218.37B (AI software, adjacent), 2033 Grand View $65.5B, 2034 Market Intelo* $16.8B, 2035 NextMSC* $54.22B. Sub-scope spreads inside agentic 2030: US-only 5.26× ($190B–$1T); global 3.33× ($1.5T–$5T).

| Sub-market | Target year | Lowest | Highest | High ÷ low | n | Tiers |
|---|---|---|---|---|---|---|
| Organic | 2034 | Dimension $17.15B | Market Decipher $32.92B | 1.92 | 4 (+IntelMarketResearch $22B, Market Intelo* $19.8B) | 6 |
| Organic | 2033 | Coherent* services $13B | Coherent* platform $26.85B | 2.07, two scopes | 2 | 6 |
| Paid | 2030 | EMARKETER US chatbot "just over $5 billion" | WPP* global gen-search "over $100 billion"; OpenAI leak $100B | ~20, scopes differ | 4 (+EMARKETER US all-AI $68.25B) | 5 |
| Paid | 2029 | EMARKETER* US AI search "nearly $26 billion" | OpenAI leak $53B | 2.05 | 2 | 5 |
| Agentic | 2030 | Morgan Stanley US $190B | McKinsey global $5T | 26.3 | 7 (+Bain, Juniper* $1.5T, Edgar Dunn, McKinsey US $1T) | 5–6 |

**(iv) Bottom-up floors, disclosed inputs only.**

| Sub-market | Arithmetic | Inputs | Label, tier | Floor |
|---|---|---|---|---|
| Organic | $38M + $4M–$10M + $0.22M = $42.2M–$48.2M; + €2.2M unconverted | Semrush "AI products surpassed $38 million in ARR" 2025-12, `raw/a-semrush-filing-2026-09-22.md`; Peec AI ARR ">$4 million" 2025-11 vs "10m" 2026-05, `raw/a-peec-funding-techcrunch-2025-11-`, `a-vendor-roster-2026-09-22.md`; Rankscale "~$220K ARR", roster; Searchable €2.2M, `raw/a-searchable-funding-2026-09-22.md` | filed 2; company-stated 5 | **$42.2M–$48.2M + €2.2M ARR**, 4 vendors, dates 2025-11 to 2026-05. Pass 6 price × count build $5.3M–$35.2M sits beside |
| Paid | one engine discloses: $1B annualized | "ChatGPT Ads has reached $1 billion in annualized revenue run rate", 2026-08-31, `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` | company-stated 3 | **≥ $1B run rate**; 1,000 ÷ 224,532 = 0.45% of Google Search & other 2025, bases differ |
| Agentic | none possible | no engine, platform or rail states agent-executed checkout volume; adjacent: Rufus "nearly $12 billion in incremental annualized sales" 2025, `c-amazon-rufus-user-sales-statements` | company-stated 3 | `unknown — checked OpenAI, Shopify, PayPal, Stripe, Google, Amazon 2026-09-23` for agent-executed GMV |

**(v) Done-row cells — `plan.md` Programme done, Pass 13 row: 9 of 9 filled or `unknown — checked`.**

| Sub-market | User-count trend | Forecast | Bottom-up floor |
|---|---|---|---|
| Organic | engine counts (i) + referral 770.7M/month, +117.4% | 2034: $17.15B–$32.92B | $42.2M–$48.2M + €2.2M ARR |
| Paid | ChatGPT WAU 700M → >1B; AI Overviews 2B → 2.5B | 2030: ~$5B–$100B+ | ≥ $1B run rate |
| Agentic | Rufus 250M → 300M+ customers, 2025 | 2030: $190B–$5T | `unknown — checked` (iv) |

## Claims

| # | Claim | Evidence | Tier of weakest row | Load-bearing |
|---|---|---|---|---|
| C1 | Six of nine engines publish ≥2 dated user counts at tier ≤3; Claude, Perplexity, DeepSeek do not | (i) | 3 | yes |
| C2 | No two engines count users the same way: WAU, MAU, DAU, in-year customers, AI-feature MAU | (i) | 3 | yes |
| C3 | Referral and web-visit share moved from ChatGPT to Gemini on both series carrying both, Jun 2025–Aug 2026 | (ii) rows 1–2 | 4 | yes |
| C4 | AI tools held under 2% of US desktop search events while Google's referral share rose | (ii) rows 4–5 | 5 | yes |
| C5 | Forecast spread: organic 1.92× (2034), paid ~20× (2030), agentic 26.3× (2030) | (iii) | 6 | yes |
| C6 | Floors: organic tens of millions ARR; paid ≥$1B, one engine; agentic undisclosed | (iv) | 5 | yes |
| C7 | H21 killed; H22 killed; H16 unresolved — checked | below | 3 | yes |

**Hypothesis marks.** H21 — **killed**: Claude has no dated user-count statement after anthropic.com newsroom and support.claude.com were checked; Anthropic files no IR (private). ChatGPT (3 points) and Google (Gemini app 6 points) meet it. H22 — **killed**: organic 2034 highest ÷ lowest 1.92, at or below 3; paid 2030 (~20) and agentic 2030 (26.3) exceed 3. H16 — **unresolved — checked**, unchanged from `findings/unknowns.md` L40: 10 new forecasts, all forecast-labelled; MarketsandMarkets ("reached"), Market Intelo, NextMSC ("valued at") again present base years as measured without method, tier 6. Nearest tier-3 closed-window figure, Rufus "$12 billion" for 2025, is one engine's influenced sales, not a sub-market size.

## Survivorship

Engines publish counts when they are large or rising. Anthropic, DeepSeek and, since 2024-01, Perplexity publish no user count; Meta stopped at "more than a billion" and Copilot's family MAU stops at 2025-10-29, both switching to ratios. Forecasts reach the web through report-sales pages and press releases; paywalled bodies (EMARKETER, WPP full forecast, Gartner, Statista, Datos Apr–Jun 2026 report) are unread.

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| User counts for Claude, DeepSeek, Perplexity 2026; agent-executed checkout GMV, any engine or rail | anthropic.com, support.claude.com, claude.com, perplexity.ai site searches; openai.com (403), shopify.com 2026-08-05 release, PayPal/Stripe search, aboutamazon.com | 2026-09-23 |
| AI-surface ad revenue beyond ChatGPT; forecast bodies (EMARKETER, MAGNA 2026, Statista, Datos) | Alphabet 10-K FY2025; Microsoft, Amazon, Meta IR; emarketer.com (DNS failure), magnaglobal.com, statista.com (paywall), datos.live (form) | 2026-09-23 |

## Caveats

- Forecasts are tier 5–6: none publishes a model. Coherent's stated 13.6% and 14% CAGRs do not reproduce its own endpoints (2.70 → 26.85 over 7 years ≈ 38.9%; 1.25 → 13 ≈ 39.7%); recorded, not corrected. Scopes differ inside every row of (iii); ratios compare labels, not like quantities. User counts are company-stated, definitions differ, and "active" is defined only by OpenAI (message in prior seven days) and SpaceX (30-day interaction). Never summed across engines.
- Floors mix ARR dates (2025-11 to 2026-05), currencies and one filed "AI products" line broader than AI visibility; Peec AI $4M and $10M sit side by side. Paid floor is a run rate, not booked revenue; its 0.45% ratio compares a run rate with a fiscal year. Share series (ii) use three definitions, never combined; Datos rows are a tier-5 pointer. Nothing here is a verdict or a size.

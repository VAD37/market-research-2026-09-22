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

## Pricing across sub-markets, COMPILE-2, 2026-09-23

Task COMPILE-2 (Pass 16), per `method/biz-review-solution-2026-09-23.md` §2 row 10. Appended only. Every price is copied verbatim from the cited raw as the profile, `markets/` file or `ai-ads-evidence.md` carries it; no conversion between currencies, no averaging. Tier is the cited raw's own tier line (own pricing page = 3). `unknown — checked` where the repo records the channel silent. JPY prices come from geolocated pulls (`markets/organic-recommendation.md:117`).

| Sub-market | Seller | Price verbatim | Unit | Date | Tier | Raw path (compiled line) |
|---|---|---|---|---|---|---|
| Organic tools | Rankscale.ai | "$20/mo" Essentials; /facts "from €20" — unreconciled | per month, credit-metered | 2026-09-22 | 3 | `raw/a-rankscale-pricing-2026-09-22.md` (`competitors/rankscale-ai.md:22`) |
| Organic tools | Otterly.AI | "$29/mo, Lite ($25/mo annual)" | per month | 2026-09-22 | 3 | `raw/a-otterly-pricing-2026-09-22.md` (`competitors/INDEX.md:36`) |
| Organic tools | RankPrompt | "$39 per month, Starter; same page also '$49/mo'" | per month, credits | 2026-09-22 | 3 | `raw/a-rankprompt-pricing-2026-09-22.md` (`INDEX.md:26`) |
| Organic tools | Promptwatch | "$95/monthly, Essential"; top self-serve "$579/month" | per month | 2026-09-22 | 3 | `raw/a-promptwatch-pricing-2026-09-22.md` (`INDEX.md:21`; `organic-recommendation.md:32`) |
| Organic tools | Onclusive | "From $105/month", Starter, annual plan | per month | 2026-09-22 | 3 | `raw/a-onclusive-roster-clear-feature-pricing-2026-09-22.md` (`INDEX.md:41`) |
| Organic tools | Searchable | "$125/month, Pro"; Enterprise "$999/month" | per month | 2026-09-22 | 3 | `raw/a-searchable-pricing-2026-09-22.md` (`INDEX.md:17`; `organic-recommendation.md:26`) |
| Organic tools | Sitefire | "$249/month, Lite" | per month | 2026-09-22 | 3 | `raw/a-sitefire-pricing-2026-09-22.md` (`INDEX.md:27`) |
| Organic tools | Scrunch AI | "$250/mo, Core" | per month | 2026-09-22 | 3 | `raw/a-scrunch-pricing-2026-09-22.md` (`INDEX.md:16`) |
| Organic tools | AthenaHQ | "$295/month Starter"; Free / Essential "$25 free credit" | per month + credits | 2026-09-22 | 3 | `raw/a-athenahq-pricing-2026-09-22.md` (`INDEX.md:23`) |
| Organic tools | Peec AI | "€75/mo ($87); €169/mo ($196); 'from €424 per month ($493)'" — historical tiers; current page renders no figure | per month | 2025-11-17; 2026-09-22 | 5; 3 | `raw/a-peec-funding-techcrunch-2025-11-2026-09-22.md`; `raw/a-peec-pricing-2026-09-22.md` (`competitors/peec-ai.md:21`) |
| Organic tools | geoSurge | "$0/month, Free BYOK"; Enterprise subscription undisclosed | per month, usage | 2026-09-22 | 3 | `raw/a-geosurge-pricing-2026-09-22.md` (`INDEX.md:19`) |
| Organic tools | Profound | not disclosed — free 7-day trial only | — | 2026-09-22 | 3 | `raw/a-profound-pricing-2026-09-22.md` (`INDEX.md:22`) |
| Organic tools | AirOps; Brandlight; Conductor; Yext; Birdeye; Quattr; SOCi; Uberall; Muck Rack; Change Agents; Locafy | not disclosed — `unknown — checked each vendor's pricing URL 2026-09-22` (404, form, credit packages, or no dollar figure) | — | 2026-09-22 | 3 | `raw/a-<vendor>-pricing-2026-09-22.md` each (`INDEX.md:18`, `:24`, `:28`, `:30`–`:35`, `:37`, `:43`–`:44`) |
| Organic tools, range | 13 pure-plays | "$20–$999/month self-serve; Enterprise 'Custom' at nearly all"; disclosed price 14 of 34 rostered | per month | 2026-09 | 3 | `raw/a-vendor-census-c1-`…`-c4-2026-09-22.md` (`organic-recommendation.md:26`, `:66`) |
| Organic, incumbent bundle | Semrush | "$199/mo Starter, first AI Visibility tier; SEO base $139/mo"; delta "+$60/mo monthly, +$47.84/mo annually" | per month | 2026-09-22 | 3 | `raw/a-semrush-pricing-2026-09-22.md`; `raw/a-vendor-census-c3-2026-09-22.md` (`organic-recommendation.md:68`, `:87`) |
| Organic, incumbent bundle | HubSpot | "¥6,000/mo or '$50/mo' standalone — both stated, unreconciled" | per month | 2026-09-22 | 3 | `raw/a-hubspot-pricing-2026-09-22.md` (`INDEX.md:25`) |
| Organic, incumbent bundle | Ahrefs | "¥19,900/mo, Lite — base plan already includes Brand Radar"; standalone "$199 vs ¥30,600" on two pages | per month | 2026-09-22 | 3 | `raw/a-ahrefs-pricing-2026-09-22.md` (`INDEX.md:29`; `competitors/ahrefs.md:71`) |
| Organic, incumbent bundle | SE Ranking | "¥17,455/mo, Core annual; AI Search add-on +¥10,478/mo" | per month | 2026-09-22 | 3 | `raw/a-seranking-pricing-2026-09-22.md` (`INDEX.md:42`) |
| Organic, incumbent bundle | Similarweb | "$99, AEO Intelligence — no billing period labelled"; "$333 Best for marketers & SEO managers" | unlabelled | 2026-09-22 | 3 | `raw/a-similarweb-pricing-2026-09-22.md` (`INDEX.md:40`) |
| Organic, incumbent bundle | BrightEdge | not disclosed; one reviewer states "At over $55,000/year" | per year, reviewer | 2026-09-22 | 3 (page); review tier 5 | `raw/a-brightedge-pricing-2026-09-22.md` (`INDEX.md:32`) |
| Organic, incumbent bundle | Base-plan delta, six c3 incumbents | "0 of 6 c3 incumbents disclose a base-plan dollar price"; no clean isolated delta — `unknown — checked all six c3 and five c4 pricing pages 2026-09-22` | — | 2026-09-22 | 3 | `raw/a-vendor-census-c3-`, `-c4-2026-09-22.md` (`organic-recommendation.md:68`, `:110`) |
| Organic, agency | Pace Generative | "$1,499 / $1,999 / $2,499" per package (Community Platform Mentions Basic $1,499) | one-time package | 2026-09-22 | 3 | `raw/f-pace-generative-pricing-2026-09-22.md`; `raw/f-agency-census-c5-2026-09-22.md` §5 (`INDEX.md:45`; `organic-recommendation.md:67`) |
| Organic, agency | Orange142; Intero Digital; Seer Interactive; Fire&Spark | "4 contact-only" — `unknown — checked orange142, interodigital, seerinteractive, fireandspark pricing pages 2026-09-22` | — | 2026-09-22 | 3 | `raw/f-orange142-`, `f-intero-digital-`, `f-seer-interactive-`, `f-fire-and-spark-pricing-2026-09-22.md` (`organic-recommendation.md:67`) |
| Paid inventory | OpenAI, ChatGPT Ads | "$3–$5 USD per click" recommended max bid | CPC bid guidance, not a rate card | 2026-09-22; 2026-09-23 | 3 | `raw/b-openai-platform-summary-2026-09-22.md`; `raw/b-openai-help-ads-basics-2026-09-23.md` (`paid-placement.md:34`, `:74`; `ai-ads-evidence.md:41`) |
| Paid inventory | OpenAI, ChatGPT Ads | minimum daily spend "25 USD", "15 EUR", "15 GBP", "2,500 JPY", "725 INR"; 23 currencies | floor on spend | 2026-09-23 | 3 | `raw/b-openai-help-create-campaigns-2026-09-23.md` (`paid-placement.md:147`) |
| Paid inventory | OpenAI, ChatGPT Ads | billing "CPM, CPC, oCPC, oCPM"; "relevance-weighted, second-price auction" | pricing basis | 2026-09-23 | 3 | `raw/b-openai-help-ads-basics-`, `b-openai-help-conversion-optimized-2026-09-23.md` (`paid-placement.md:170`) |
| Paid inventory | OpenAI, as trade-reported | launch "$60" CPM, "$200,000–$250,000 minimum"; "$25" CPM mid-April; minimum removed 2026-05-05 | CPM history | 2026-02 to 2026-05 | 5 | `raw/b-digiday-openai-ads-fomo-cpm-`, `b-ppcland-adthena-europe-benchmark-2026-09-23.md` (`paid-placement.md:148`; `ai-ads-evidence.md:42`) |
| Paid inventory | ChatGPT Ads, practitioner-reported | "$4.41 CPC on $9,620 spend, 34 days" — graded Fools gold | realised CPC | 2026-09-22 | 5 | `raw/e-case-common-thread-collective-chatgpt-ads-2026-09-22.md` (`paid-placement.md:69`, `:119`) |
| Paid inventory | ChatGPT Ads, Reddit self-reports | CPC "$3.37"; "CPM of $47"; CPC "$7-8"; CPC "less than $6"; "$50 USD CPM", "$5k USD minimum outlay" (agency offer, hearsay) | realised, archive copy | 2026-05 to 2026-09 | 5 | `raw/b-reddit-advertiser-reports-repull2-2026-09-23.md` (`ai-ads-evidence.md:108`, `:114`, `:115`, `:120`, `:121`) |
| Paid inventory | Google, AI Overviews / AI Mode | "auction, no unit or figure named"; existing Search, Shopping, PMax campaigns auto-eligible, "you can't opt out"; AI Mode format pricing `unknown — checked` | auction | 2026-09-22; 2026-09-23 | 3 | `raw/b-google-platform-summary-2026-09-22.md`; `raw/b-google-ads-help-aio-ads-2026-09-23.md` (`paid-placement.md:76`, `:111`; `ai-ads-evidence.md:48`) |
| Paid inventory | Microsoft Copilot, via Bing auction | "Microsoft Advertising auction, ManualCpc / EnhancedCpc; no Copilot-specific unit"; price delta `unknown — checked about.ads.microsoft.com 2026-09-22` | auction | 2026-09-22 | 3 | `raw/b-microsoft-amazon-platform-summary-2026-09-22.md` (`paid-placement.md:37`, `:79`, `:91`) |
| Paid inventory | Amazon, Rufus / Alexa sponsored prompts | "we will begin to charge for these ads as part of your CPC bidding and billing parameters"; GA US 2026-03-25 | CPC, existing campaigns | 2026-09-22 | 3 | `raw/b-amazon-sponsored-prompts-ga-2026-09-22.md`; `raw/b-microsoft-amazon-platform-summary-2026-09-22.md` (`paid-placement.md:38`, `:80`; `ai-ads-evidence.md:52`) |
| Paid inventory | Perplexity | "subscription pricing disclosed; ad rate not disclosed"; programme "winding down… by the end of 2026"; "fewer than 0.5% of brands who applied" admitted | — | 2026-09-22; 2026-09-23 | 3; 5 | `raw/b-anthropic-perplexity-platform-summary-2026-09-22.md`; `raw/b-campaign-perplexity-ads-end-`, `b-pymnts-perplexity-ads-end-2026-09-23.md` (`paid-placement.md:82`; `ai-ads-evidence.md:53`) |
| Paid inventory | Engines, coverage | "0 of 8 publish a rate card"; "No engine publishes a unit price" | — | 2026-09-22; 2026-09-23 | 3 | `raw/b-*-platform-summary-2026-09-22.md` (`paid-placement.md:39`, `:143`; `whitespace.md:22` E1) |
| Paid inventory, network | Kontext | "Rates starting from just $3 CPM" — third-party apps, not an engine | CPM floor | 2026-09-23 | 3 | `raw/b-kontext-advertisers-page-2026-09-23.md` (`paid-placement.md:150`; `ai-ads-evidence.md:55`) |
| Paid inventory, network | Kontext, via PPC Land | "$2.50 CPM vs Facebook $7.35 (one pilot)"; "revenue share 25–30%" | pilot CPM; take rate | 2026-09-23 | 5 | `raw/b-ppcland-kontext-10m-2026-09-23.md` (`paid-placement.md:151`) |
| Paid inventory, network | Koah; Taboola | Koah "Click-through rates average 7.5%", no price; Taboola no price | — | 2026-09-23 | 3 | `raw/b-koah-launch-release-`, `b-taboola-genai-ad-platform-2026-09-23.md` (`ai-ads-evidence.md:55`) |
| Paid inventory, reseller | Amazon DSP into ChatGPT; OpenAI Reseller Program; Dentsu, Omnicom, Publicis, WPP | "no fee, revenue share or commission stated" — `unknown — checked raw/b-amazon-ads-chatgpt-integration-2026-09-22.md 2026-09-22` | take rate | 2026-09-22 | 3 | `raw/b-amazon-ads-chatgpt-integration-2026-09-22.md`; `raw/b-openai-platform-summary-2026-09-22.md` (`paid-placement.md:67`) |
| Paid inventory, sell-side | Criteo GO; StackAdapt; Pacvue; Kargo | "Criteo GO CPM-based, no rate card; StackAdapt 5 tiers, no figure; Pacvue no pricing page (404); Kargo contact-only" | — | 2026-09-22 | 3 | `raw/c-vendor-census-c6-2026-09-22.md`; `raw/b-stackadapt-pricing-2026-09-22.md` (`paid-placement.md:68`; `INDEX.md:50`–`:53`) |
| Agentic | Microsoft Copilot Checkout | "No. Today, Microsoft does not take a commission or affiliate fee" — 0%; protocols-table pull reads `unknown` for the same FAQ | commission | 2026-09-22 | 3 | `raw/b-microsoft-agentic-commerce-2026-09-22.md`; `raw/c-agentic-commerce-protocols-table-2026-09-22.md` (`agentic-commerce.md:25`, `:89`, `:119`) |
| Agentic | OpenAI Instant Checkout | fee `unknown — checked developers.openai.com, help.openai.com, docs.stripe.com 2026-09-22` | take rate | 2026-09-22 | 3 | `raw/c-openai-commerce-get-started-2026-09-22.md`; `raw/c-openai-shopping-chatgpt-search-2026-09-22.md` (`agentic-commerce.md:86`, `:111`) |
| Agentic | Google AI Mode / Gemini; Perplexity checkout programs | fee undisclosed — "One fee statement across four live programs" | take rate | 2026-09-22 | 3 | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` (`agentic-commerce.md:66`) |
| Agentic | Protocols ACP, UCP, AP2, x402, Visa TAP, Mastercard Agent Pay | "No protocol states a fee clause"; 6 of 6 `unknown — checked` 2026-09-22 | fee clause | 2026-09-22 | 3 | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` (`agentic-commerce.md:67`; `whitespace.md:17`) |
| Agentic, platform | Shopware | "Free, € 0" Community; Rise "From € 600/month"; Evolve "€2,400/mo"; Intelligence+ "€19–29/mo"; G2 shows "$600" beside "€600" | per month | 2026-09-22 | 3 | `raw/c-vendor-census-c6-2026-09-22.md` (`agentic-commerce.md:23`, `:69`; `competitors/shopware.md:77`) |
| Agentic, feed tooling | Feedonomics | custom quote; "we never take a percentage of revenue" | — | 2026-09-22 | 3 | `raw/c-feedonomics-pricing-2026-09-22.md`; `raw/c-vendor-census-c6-2026-09-22.md` (`agentic-commerce.md:70`; `INDEX.md:54`) |
| Agentic, platform | Wix | "unknown — no figure for any AI-surface feature" | — | 2026-09-22 | 5 | `raw/c-wix-second-source-2026-09-22.md` (`INDEX.md:56`) |
| Agentic, engines (organic side) | OpenAI, Anthropic, Google | "none — engines take no fee on this lane"; Google: "no additional requirements... nor other special optimizations necessary" | — | 2026-09-22 | 3 | `raw/a-google-ai-features-guidance-2026-09-22.md` (`organic-recommendation.md:65`) |

Count: 45 rows. Prices disclosed as a unit price by a seller on its own page: organic tools 14 of 34 rostered; paid 0 of 8 engines, 1 network (Kontext floor); agentic 1 fee statement (Copilot, 0%) of 4 programs, 0 of 6 protocols, 1 platform rate card (Shopware); agencies 1 of 5.

**Caveats.** Own-page prices are tier 3 — reliable on existence, biased on framing — and change without notice; every price is as pulled 2026-09-22 or 2026-09-23. Currencies (USD, EUR, JPY) sit side by side, unconverted; JPY figures are geolocated renderings of the same vendors' USD pages. Bid guidance, minimum spend, CPM history and self-reported realised CPC are four different kinds of number and none is a rate card (`paid-placement.md:143`). Willingness to pay is not inferred from any row (`plan.md` line 600). This file was at its 100-line budget before this append; overrun stated here. Evidence, not a verdict.

## Sub-markets side by side, COMPILE-2, 2026-09-23

Per REV-BIZ-B (coordinator addition to COMPILE-2's brief). One row per sub-market; every cell copies a compiled figure and cites its file:line. No ranking of sub-markets, no choice. Demand tallies per sub-market after R-BLOCKED-2 are arithmetic on the cell rows at `demand-map.md:50–52` (2026-09-22), `:107–116` (P8-r E13, E14, E15, E16), `:130–136` (organic 6 / paid 1 / agentic 1 spend) and `:148` §R-BLOCKED-2 (E14–E16 to `none — checked`); the totals reconcile to the stated 8/1/17/1 strict and 8/1/18/0 loose.

| Sub-market | Demand, 9 cells: spend / attention / none / blank — strict | — loose | Best proof grade, count | Supply count, disclosure ratio | Size floor | Forecast spread | Risk ranks touching it (`whitespace.md` risk register) |
|---|---|---|---|---|---|---|---|
| Organic recommendation | 6 / 1 / 1 / 1 (blank: E2 skincare Organic/Mid) — `demand-map.md:136`, `:148` | 6 / 1 / 2 / 0 | 0 Gold; Silver 7 grade_raw / 1 grade_rule1 (X1); ~980 + ~1,640 screened — `proof-scorecard.md:23`, `:59–60`, `:112–113` | 34 rostered (13 pure-play, 16 incumbent bundles, 5 agencies); price 14 of 34; customer count 8 of 34; funding 8 of 34; filed revenue 2 of 34; price + count 4 of 34 — `organic-recommendation.md:25–30`; 34 profiles `INDEX.md:16–49` | $42.2M–$48.2M + €2.2M ARR (4 vendors); $5.3M–$35.2M price × count build beside — `market-potential.md:60`, `:68`; `organic-recommendation.md:36`, `:131` | 2034: $17.15B–$32.92B, 1.92×, 4 forecasts, tier 6 — `market-potential.md:50`, `:68` | 1 (organic 3 of 9 engine cells), 3, 4, 5, 6, 7, 10, 11 — `whitespace.md:96–108` |
| Paid placement | 1 / 0 / 8 / 0 — `demand-map.md:51`, `:110–111`, `:148` | 1 / 0 / 8 / 0 | Fools gold; 15 screened, 0 cleared; 10 observational advertiser reports (RB1–RB10), 0 controlled — `ai-ads-evidence.md:68`, `:83–84`, `:125`; `paid-placement.md:119` | Engines: 5 of 8 live product; 4 of 5 pricing basis; 0 of 8 rate card; 1 of 8 revenue; 0 of 8 precise advertiser count — `paid-placement.md:39`. Sell-side profiles 4, price 0 of 4 — `INDEX.md:50–53`. Networks 4, price floor 1 (Kontext) — `paid-placement.md:150`, `:173` | ≥ $1B annualized run rate, one engine; 0.45% of Google Search & other 2025, bases differ — `market-potential.md:61`, `:69` | 2030: ~$5B–$100B+, ~20×, scopes differ; 2029: 2.05× — `market-potential.md:52–53`, `:69` | 2 (paid 9 cells), 4, 5, 6, 7, 8, 11 — `whitespace.md:97–108` |
| Agentic commerce | 1 / 0 / 8 / 0 (spend: skincare Enterprise) — `demand-map.md:52`, `:110`, `:135`, `:148` | 1 / 0 / 8 / 0 | none graded: Feedonomics 22 screened, all "screened — not opened"; T17 Feedonomics ×2 class (c); Shopware, Wix 0 claims — `INDEX.md:54–56`; `proof-scorecard.md:196` | Sell-side 3 of 7 rostered; price 1 of 3 (Shopware); engine programs 4 live, fee 1 of 4 (Copilot 0%); protocol fee clauses 0 of 6; merchant count 0 engines — `agentic-commerce.md:22–26`, `:67`; 3 profiles `INDEX.md:54–56` | `unknown — checked OpenAI, Shopify, PayPal, Stripe, Google, Amazon 2026-09-23` for agent-executed GMV; adjacent Rufus "nearly $12 billion" 2025 — `market-potential.md:62`, `:70` | 2030: $190B–$5T, 26.3×, 7 forecasts, tier 5–6; "roughly 35×" over 2029–30 beside — `market-potential.md:54`, `:70`; `agentic-commerce.md:54`, `:132` | 4, 5, 6, 9 (agentic 9 cells), 11 — `whitespace.md:99–108` |

**Caveats, this section.** The one agentic spend cell is read two ways by two compilers: `demand-map.md:135` "skincare Agentic/Enterprise spend" against `agentic-commerce.md:105` "Skincare × enterprise — attention" (e.l.f. posting, tier 3, "below the tier-5 spend floor"); both stand, listed in `unknowns.md` "Figures carried twice" row 41. Demand cells count signals, not buyers; willingness to pay is `unknown` in all 27 (`demand-map.md:55`). Proof grades are per vertical in `proof-scorecard.md` and are assigned to a sub-market here by the case's lane, not by a sub-market column that file lacks. Supply ratios use each file's own denominator (34 rostered, 8 engines, 7 sell-side vendors) and are not comparable across rows. Risk ranks follow the register's stated criterion (evidence tier, then breadth), not severity. Floors and forecasts are never sizes. Evidence, not a verdict; no sub-market is preferred here.

## Baseline context, P16-c1, 2026-09-23

The filed baselines the sub-market figures in (iv) sit against. No ratio is computed here; the only ratio in this file remains the 0.45% at (iv), carried as written. Raw prefix `raw/`, suffix `-2026-09-23.md`. Compiled table with periods and verbatim rows: `../markets/paid-placement.md` §"Baselines beyond Google".

| Baseline | Latest full year, verbatim | Latest quarter, verbatim | Label, tier | Raw |
|---|---|---|---|---|
| Google Search & other | FY2025 "$ 224,532" M | — (Q2 2026 transcript in repo) | filed, 2 | `b-alphabet-10k-2025-search-revenue` |
| Microsoft Search advertising | FY2026 (June) "15,176" M | Q4 FY2026 ex-TAC "increased 10%" | filed, 2 | `b-microsoft-10k-fy2026-search-advertising`; `b-microsoft-8k-q4-fy2026-search-advertising` |
| Amazon Advertising services | FY2025 "68,635" M | Q2 2026 "19,809" M | filed, 2 | `b-amazon-10k-2025-advertising-services`; `b-amazon-10q-q2-2026-advertising-services` |
| Meta Advertising | FY2025 "$ 196,175" M | Q2 2026 "$ 59,363" M, "27%" | filed, 2 | `b-meta-10k-2025-advertising-revenue`; `b-meta-10q-q2-2026-advertising-revenue` |
| Reddit Advertising revenue | FY2025 "$ 2,062,480" thousand | Q2 2026 "$ 761,625" thousand | filed, 2 | `b-reddit-10k-2025-advertising-revenue`; `b-reddit-10q-q2-2026-advertising-revenue` |
| Walmart global advertising business | no dollar figure filed | Q2 FY2027 "up 38%"; Walmart Connect "43%" | filed, 2 | `b-walmart-8k-q2-fy2027-advertising` |
| US digital ad revenue, IAB/PwC | 2025 "$294.6 billion"; Search "$114.2B"; Commerce Media "$63.4B" | — | analyst-derived, 4 | `e-iab-pwc-internet-ad-revenue-fy2025` |
| Global keyword search, MAGNA | 2024 "$330 billion"; US "$152 billion" | — | analyst-derived, 5 | `e-magna-search-report-page` |
| Sub-market figures these sit against | organic ARR floor $42.2M–$48.2M + €2.2M; paid "≥ $1B run rate", one engine; agentic `unknown — checked` | — | (iv) above | as cited in (iv) |

**Caveats — this append.** Bases differ in scope, currency unit and fiscal year; no two rows are like quantities. None of the filers states an AI-surface ad line, so the paid floor stays one engine's run rate. Search engines walled this pass (`f-search-engines-wall-log-2026-09-23.md`); MAGNA 2026 and IAB report body unreached. Nothing here is a verdict. File now over its 100-line budget; overrun is this append.

## Primary re-pulls, REPULL-1, 2026-09-23

- Similarweb gen-AI traffic shares · `raw/a-similarweb-share-gen-ai-stats-2026-09-22.md` (4 — WebFetch summary) · `raw/a-similarweb-gen-ai-stats-primary-2026-09-23.md` (4) · "ChatGPT's share of generative AI website visits fell from about 76% in June 2025 to roughly 53% by May 2026"; "Gemini … rising from under 9% to around 27–28%"; "Claude moved from barely 2% to close to 9%"; citations in US ChatGPT prompts "1.6% in June 2025 to roughly 6.8% by May 2026"; "roughly 26% of ChatGPT responses now contain an ad" (2026-07-29; eight charts saved) · agrees
- Perplexity query volume (169M/month) · `raw/e-perplexity-user-query-counts-2026-09-23.md` (3 — figure from a search snippet, page 403) · `raw/e-perplexity-enterprise-pro-launch-primary-2026-09-23.md` (3) · "now serving 169 million queries per month" (Perplexity blog, 2024-04-23); "Prices start at $40/month or $400/year per seat" (Enterprise Pro) · agrees

## Brand-side adoption series, P16-c4, 2026-09-23

Time series of brand-side adoption proxies, each point dated and tiered. Wayback captures are the page's own claim at that date (tier 5); host counts read off an archived directory page are ours over what that page rendered. Raw prefix `raw/`, suffix `-2026-09-23.md` unless stated. No point below is a count of paying brands; every row is a proxy (`method/demand-signals.md`).

| Date | Proxy | Value | Method | Tier | Raw |
|---|---|---|---|---|---|
| 2025-11-14 | G2 "Answer Engine Optimization (AEO)" listings | 160 | Wayback capture, "N Listings … Available" string | 5 | `e-wayback-g2-capterra-category-counts` |
| 2025-12-03 | same | 216 | same | 5 | same |
| 2026-01-13 | same | 159 | same | 5 | same |
| 2026-07-24 | same | 458 | same | 5 | same |
| 2026-08-05 | same | 477 | same | 5 | same |
| 2026-09-14 | same | 618 | same | 5 | same |
| 2026-09-23 | same | 632 | live page, browser | 5 | `f-g2-capterra-S4-repull` |
| 2026-07-22 | G2 "AI Search Visibility Optimization Tools" listings | 246 | Wayback capture | 5 | `e-wayback-g2-capterra-category-counts` |
| 2026-08-01 | same | 288 | same | 5 | same |
| 2026-09-17 | same | 521 | same | 5 | same |
| 2026-09-23 | same | 541 | live page, browser | 5 | `f-g2-capterra-S4-repull` |
| 2026-08-03 | Capterra "AI Search Visibility Software" | pagination to page 5, no count printed | Wayback capture | 5 | `e-wayback-g2-capterra-category-counts` |
| 2026-09-23 | same | "Page 1 of 9"; page 9 holds 36 profiles | live page, browser | 5 | `f-g2-capterra-S4-repull` |
| 2024-11-27 | llmstxt.site — distinct hosts listed | 56 | Wayback capture, hosts before `/llms.txt` counted by us | 5 | `e-wayback-llms-txt-directories` |
| 2025-03-02 | same | 89 | same | 5 | same |
| 2025-06-15 | same | 224 | same | 5 | same |
| 2025-09-09 | same | 683 | same | 5 | same |
| 2025-12-13 | same | 1,491 | same | 5 | same |
| 2026-04-01 | same | 1,491 | same — byte-identical to 2025-12-13 | 5 | same |
| 2026-08-27 | same | 1,491 | same — byte-identical | 5 | same |
| 2026-09-23 | same | 1,497 | live page, curl | 5 | same |
| 2024-11-17 | directory.llmstxt.cloud — distinct hosts rendered | 51 | Wayback capture, counted by us | 5 | same |
| 2025-03-05 | same | 107 | same | 5 | same |
| 2025-06-06 · 2025-09-04 · 2025-12-11 | same | 583 · 583 · 583 | same | 5 | same |
| 2026-09-23 | directory.llmstxt.cloud — "Websites listed" | 3,830 | live page prints the total; rendered list is a featured subset (9 hosts) | 5 | same |
| 2025-01-24 | Profound /customers — case-study links | 1 (9 logo alts) | Wayback capture, `/customers/<slug>` links counted by us | 5 | `e-wayback-profound-customers` |
| 2025-04-28 | same | 2 | same | 5 | same |
| 2025-08-06 | same | 5 | same | 5 | same |
| 2025-11-26 | same | 7 | same | 5 | same |
| 2026-03-06 | same | 10 | same | 5 | same |
| 2026-07-01 | same | 18 | same | 5 | same |
| 2026-09-03 | same | 20 | same | 5 | same |
| 2026-09-23 | same | 21 (21 logo alts) | live page, curl | 5 | same |
| 2026-09-22 · 2026-09-23 | llms.txt on sampled brand domains, cross-section | beauty 3 of 5; B2B SaaS 9 of 10; high-CPA 3 of 9; local/multi-location 2 of 16 answering | measured-by-us HTTP checks, one date each | 1 | `f-signal-sk-S12-llms-txt-beauty-domains-2026-09-22.md`; `f-signal-bs-S12-llms-txt-domains-2026-09-22.md`; `f-signal-hr-S12-llmstxt-sample-2026-09-22.md`; `f-llms-txt-multilocation-domains-S12` |

**Read.** Three series carry more than three dated points: G2 AEO listings (160 → 632, 2025-11-14 → 2026-09-23, with a 216 → 159 dip between 2025-12 and 2026-01 that the archived pages state and this file does not explain); llmstxt.site hosts (56 → 1,497, 2024-11 → 2026-09, flat at 1,491 across the last three captures); Profound customer stories (1 → 21, 2025-01 → 2026-09). No series distinguishes a paying brand from a listed vendor or a self-submitted domain.

**Checked, nothing usable.** Wayback CDX returned no captures for peec.ai/customers, otterly.ai/customers, scrunchai.com/customers, scrunch.com/customers, athenahq.ai/customers, and no JSON for a G2 "generative-engine-optimization-geo" slug (`e-wayback-profound-customers`, `e-wayback-g2-capterra-category-counts`). HTTP Archive and Cloudflare Radar publish no llms.txt statistic on record (`findings/unknowns.md`, 2026-09-22); a Common Crawl path-wildcard query is not a supported shape — `unknown — checked web.archive.org CDX, httparchive.org (2026-09-22), index.commoncrawl.org query shape 2026-09-23`. Single-date vendor claims are not series and sit in their profiles (Scrunch "Trusted by 500+ leading brands and agencies", `raw/a-scrunch-customers-2026-09-22.md`; Birdeye 16,240 scans across "1,500+" / "1,762" brands, `raw/f-birdeye-multilocation-ai-search-S2-S6`).

**Caveats, this append.** G2 listing counts are vendor sign-ups to a review site, not buyers; both G2 categories overlap (Profound sits in both). Directory host counts are self-submissions and, for directory.llmstxt.cloud after 2026-02, a rendered subset against a printed total — the 583 → 3,830 step is a page redesign, not measured growth. Wayback sampling is one capture per month, chosen by CDX collapse; digests differ where byte counts are identical. Profound story counts are the vendor's publishing cadence. The llms.txt cross-sections are four different samples on two dates, not a series. File over its 100-line budget; overrun includes this append.

## EU engine share and users, P16-c3, 2026-09-23

One definition per row; rows with different definitions are never combined. Raw prefix `raw/`, suffix `-2026-09-23.md` unless stated. UK, FR, ES, IT, NL requested; DE and EU-wide rows carried where the same pull returned them.

| Country | Engine / measure | Figure verbatim | Definition | Date | Tier | Raw |
|---|---|---|---|---|---|---|
| UK | ChatGPT · Gemini · Copilot · Claude · Perplexity | 77.44% · 9.28% · 6.47% · 3.99% · 2.81% | referral page-view share to StatCounter-tracked sites | 2026-08 | 4 | `a-statcounter-ai-chatbot-share-eu-countries` |
| FR | same five | 80.68% · 9.92% · 3.17% · 2.9% · 3.29% | same | 2026-08 | 4 | same |
| ES | same five | 78.42% · 12.66% · 3.11% · 2.26% · 3.54% | same | 2026-08 | 4 | same |
| IT | same five | 69.35% · 17.34% · 5.42% · 2.86% · 5.03% | same | 2026-08 | 4 | same |
| NL | same five | 81.67% · 8.73% · 3.19% · 3.18% · 3.23% | same | 2026-08 | 4 | same |
| DE | same five | 77.83% · 9.85% · 3.82% · 3.05% · 5.44% | same | 2026-08 | 4 | same |
| UK | ChatGPT, series | 80.83% (2025-09) → 65.53% (2026-04) → 77.48% (2026-08) | same, monthly CSV | 2025-09 to 2026-08 | 4 | same |
| IT | Gemini, series | 2.41% (2025-09) → 17.52% (2026-08) | same, monthly CSV | 2025-09 to 2026-08 | 4 | same |
| FR | ChatGPT · Gemini · "Autres IA" | 63 % · 13 % · 24 % | share of generative-AI users naming it most used, Crédoc survey n=4,145 | fieldwork 2025-06-05 to 06-21 | 4 | `b-arcep-barometre-numerique-2026` |
| FR | generative AI, population | 48 % (2025) · 33 % (2024) · 20 % (2023); "85 % chez les 18-24 ans" | share of population aged 12+ using generative AI | 2025 | 4 | same |
| EU27 · DE · ES · FR · IT · NL | generative AI tools, last 3 months | 32.66 · 32.25 · 37.88 · 37.46 · 19.86 · 44.7 | percentage of all individuals, Eurostat isoc_ai_iaiu | 2025 | 3 | `a-eurostat-genai-use-individuals-2025` |
| EU27 · DE · ES · FR · IT · NL | generative AI for work purposes | 15.36 · 15.79 · 17.94 · 18.44 · 8.0 · 26.56 | percentage of all individuals | 2025 | 3 | same |
| UK | generative AI, Eurostat | not in dataset — UK absent from the 2025 EU survey | — | 2025 | — | same |
| UK · FR · ES · IT · NL · DE | AI chatbots for news, weekly use | 4% · 5% · 8% · 6% · 7% · 5% | share of online adults using AI chatbots for news weekly, YouGov panel | fieldwork 2026-01 to 02 | 4 | `a-reuters-dnr-2026-ai-chatbots-countries` |
| UK · FR · ES · IT · NL · DE | trust news from AI chatbots | 6% · 15% · 18% · 16% · 11% · 13% | share trusting news from AI chatbots | same | 4 | same |
| EU/UK | AI tools, desktop search events | 0.54% (2025-01) → 1.08% (2026-03) | share of desktop search events, Datos clickstream, relayed | 2026-03 | 5 | `a-ppc-land-share-datos-q1-2026-2026-09-22.md` |
| EU (27) | ChatGPT search, average monthly active recipients | "approximately 159.1 million" | DSA Art. 24(2) six-month average; per-state split not published | period ending 2026-03-31 | 3 | `b-eu-openai-dsa-transparency-2026-09-22.md`; walls in `a-similarweb-openai-dsa-country-cut-walls` |
| EU (27) | Bing, average monthly active users | "approximately 155 million" | DSA six-month average | period ending 2025-12-31 | 3 | `b-eu-microsoft-dsa-bing-2026-09-22.md` |
| UK · FR · ES · IT · NL | Similarweb visit share per country | unknown — checked similarweb.com (202 empty), data.similarweb.com (403) 2026-09-23 | — | — | — | `a-similarweb-openai-dsa-country-cut-walls` |
| UK | Ofcom Online Nation 2025 gen-AI use | unknown — checked ofcom.org.uk (403), web.archive.org 2026-09-23 | — | — | — | `b-regulators-eu-genai-usage-checks` |
| ES · IT | CNMC Panel de Hogares; AGCOM Rapporto IA 2026 | unknown — CNMC pages client-rendered; AGCOM Part I ENG carries no Italian user share | — | 2026 | 3 | same |

**Reads.** Five countries carry a tier-4 per-engine referral share for 2026-08 (StatCounter); ChatGPT holds 69–82 % on that definition, Gemini 9–17 %, Italy the Gemini high. Population-level generative-AI use is tier 3 for FR, ES, IT, NL, DE (Eurostat 2025) and absent for the UK. France is the only country with a survey naming which engine users use most (ChatGPT 63 %, tier 4). No per-country user count exists for any engine; the DSA figures are EU-wide. Google AI Overviews were not rolled out in France as of 2026-03 per Google's own documentation as relayed by Reuters DNR 2026 (footnote, `a-reuters-dnr-2026-ai-chatbots-countries`; primary Google page not pulled for the country list).

**Caveats, this append.** StatCounter measures referral clicks to tracked sites, not users; its HTML table and CSV differ by hundredths for the same month. Eurostat, Crédoc and YouGov measure people; none measures queries. The Datos row is a relayed pointer (tier 5). Country rows sit beside the worldwide rows in Evidence above and are not averaged with them. File over its 100-line budget; overrun includes this append.

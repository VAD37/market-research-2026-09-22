# Retail/e-commerce analytics publishers — AI-assistant referral traffic, conversion, orders — summary table

```yaml
source:          compiled by this agent from the 16 raw pulls below (Adobe Digital Insights, Salesforce, Shopify)
url_or_doc_id:   n/a — summary of docs/raw/c-adobe-*, c-salesforce-*, c-shopify-* (2026-09-22)
published:       n/a
pull_date:       2026-09-22
pull_method:     manual (compiled from this agent's own raw pulls, same session)
pull_purpose:    evidence about a number
tier:            n/a — see each cited row's own tier
tier_reason:     table default
source_label:    vendor-reported
lane:            C
sub_market:      agentic commerce
engine:          see rows — no publisher in this cluster breaks figures out per individual priority-1 engine
metric_kind:     traffic
supersedes:      none
captured:        summary table only — no new source text; every figure below is copied verbatim from the cited raw file
```

Per P2-c8 task instructions: no interpretation. Table rows only; figures verbatim from the cited raw file. Conflicting figures sit side by side, never averaged, per root `CLAUDE.md`.

## Adobe Digital Insights

Population (all Adobe rows): Adobe's own transaction data, "more than 1 trillion visits to U.S. retail sites and more than 100 million SKUs" — Adobe Analytics customer base, not the open web. Survey rows: Adobe Consumer Survey, "more than 5,000 U.S. respondents" (March 2026) or "more than 1,000 U.S. respondents" (holiday 2025 survey, as stated in that specific pull).

| Metric | Figure (verbatim) | Date window | Measured/modelled | Tier | Raw path |
|---|---|---|---|---|---|
| Traffic | "AI-Driven Traffic to Retail Sites Up 393% YoY in Quarter One" | Q1 2026 (Jan-Mar 2026) | measured | 4 | `c-adobe-analytics-q2-2026-traffic-report-2026-09-22.md` |
| Traffic | "In March 2026, it was up 269% YoY" | March 2026 | measured | 4 | `c-adobe-analytics-retail-visibility-2026-09-22.md` |
| Traffic | "AI-Driven Traffic to Retail Sites Up 138% YoY in May 2026" | May 2026 | measured | 4 | `c-adobe-analytics-q3-2026-traffic-report-2026-09-22.md` |
| Traffic (holiday) | "traffic to retail sites from generative AI tools... increased by 693.4% compared to the year prior" (also stated as "693%" elsewhere in the same article) | Nov-Dec 2025 | measured | 4 | `c-adobe-analytics-holiday-industries-2026-09-22.md` |
| Traffic (holiday, monthly) | "In November, AI-driven traffic to retail sites jumped 769%, followed by another strong increase of 673% in December" | Nov 2025 / Dec 2025 | measured | 4 | `c-adobe-analytics-holiday-industries-2026-09-22.md` |
| Traffic (holiday, CONFLICTS with row above) | Q2 2026 PDF text references "a natural pullback from the holiday peak (1,151% in December)" | December 2025 | measured | 4 | `c-adobe-analytics-q2-2026-traffic-report-2026-09-22.md` — **conflicts with the 673% December figure in the holiday-industries blog pull above; both are Adobe's own stated figures, not averaged, both kept** |
| Traffic (2025 baseline) | "generative AI traffic has grown substantially in recent months, rising 4,700% YoY in July 2025" | July 2025 (vs. July 2024 baseline) | measured | 4 | `c-adobe-analytics-shopping-rises-2026-09-22.md` — stale (published 2025-08-21) |
| Sales (conversion) | "AI Conversion Now 42% Higher" | March 2026 | measured | 4 | `c-adobe-analytics-q2-2026-traffic-report-2026-09-22.md` |
| Sales (conversion) | "AI Conversion Is Now 54% Higher" | May 2026 | measured | 4 | `c-adobe-analytics-q3-2026-traffic-report-2026-09-22.md` |
| Sales (conversion, holiday) | "AI referrals moved from lagging to leading, converting 31% more than other traffic sources—nearly doubling YoY" | Holiday 2025 season | measured | 4 | `c-adobe-analytics-holiday-industries-2026-09-22.md` |
| Sales (revenue per visit) | "AI Visits Worth 37% More Than Non-AI Visits" | March 2026 | measured | 4 | `c-adobe-analytics-q2-2026-traffic-report-2026-09-22.md` |
| Sales (revenue per visit) | "AI Visits Worth 53% More Than Non-AI Visits" | May 2026 | measured | 4 | `c-adobe-analytics-q3-2026-traffic-report-2026-09-22.md` |
| Sales (revenue per visit, holiday) | "a significant boost in AI-driven revenue per visit (RPV), which is up 254% this holiday season year-to-date" | Holiday 2025 season | measured | 4 | `c-adobe-analytics-holiday-industries-2026-09-22.md` |
| Sales (revenue per visit, 2025 baseline) | "AI-driven revenue-per-visit has grown in recent months, increasing by 84% from January 2025 to July 2025" | Jan-Jul 2025 | measured | 4 | `c-adobe-analytics-shopping-rises-2026-09-22.md` — stale |

## Salesforce

Population (Shopping Index rows): "the activity of more than 1.5 billion global shoppers across more than 89 countries" / "1.5 trillion page views" (Cyber Week pull) / "37 countries between Q1 2024 and Q1 2026" (agentic-search-growth pull) — Salesforce Commerce Cloud/Agentforce customer base, not the open web. Survey rows carry their own stated n (see each raw file).

| Metric | Figure (verbatim) | Date window | Measured/modelled | Tier | Raw path |
|---|---|---|---|---|---|
| Sales (influenced revenue) | "AI and agents powered a massive portion of the holidays, driving 20% of all retail sales and fueling $262 billion in revenue" | Nov 1 - Dec 31, 2025 | **modelled — attributed, not incremental** ("Several factors are applied to extrapolate macroeconomic figures for the broader retail industry") | 5 | `c-salesforce-analytics-holiday-2025-2026-09-22.md` |
| Sales (conversion, cross-channel) | "shoppers referred to retailer websites from AI-powered search channels converted nine times more often than those coming through social media referrals" | Holiday 2025 season | measured (Salesforce platform data; comparator is social referral, not organic search) | 5 | `c-salesforce-analytics-holiday-2025-2026-09-22.md` |
| Sales (influenced revenue, forecast) | "Salesforce anticipates that $73 billion, or 22% of all global sales, will be influenced by AI and agents during Cyber Week" | Cyber Week 2025 (Nov 27-Dec 1) | **forecast, not measurement** — source's own word "anticipates"; also modelled — attributed, not incremental | 5 | `c-salesforce-analytics-cyber-week-2025-2026-09-22.md` |
| Sales (influenced orders, pre-period) | "Over 19% of orders were influenced by AI and agents in the lead up to Cyber Week" | Oct 1 - Nov 15, 2025 | **modelled — attributed, not incremental** (measured historical period, but "influenced" is an attribution model, not incrementality) | 5 | `c-salesforce-analytics-cyber-week-2025-2026-09-22.md` |
| Traffic | "Traffic from AI- and agent-powered sources like ChatGPT, Perplexity, etc. also increased 3.8x globally YOY over the last seven weeks and 1.8x in the U.S." | 7 weeks to Nov 20, 2025 | measured | 5 | `c-salesforce-analytics-cyber-week-2025-2026-09-22.md` |
| Traffic | "Use of agentic search as the first step in the shopping journey grew 200% year over year" | reported 2026-07-28, State of Commerce report window | measured (survey-derived headline) | 5 | `c-salesforce-analytics-agentic-search-growth-2026-09-22.md` |
| Traffic | "Traffic referred from AI chats grew between 150% and 428% year over year in every quarter measured" | Q1 2024 - Q1 2026 (quarterly, per publisher's platform-behavior dataset) | measured | 5 | `c-salesforce-analytics-agentic-search-growth-2026-09-22.md` |
| Sales (retailer-agent cohort, NOT AI-referral) | "Retailers that deployed AI agents during the holiday shopping season saw a 4x higher sales growth rate" (8% YoY with agents vs. 2% without) | Holiday season (Feb 2025-Apr 2026 analysis window per Index methodology) | measured (before/after cohort comparison) | 5 | `c-salesforce-analytics-agentic-enterprise-index-2026-09-22.md` — **population is retailers running Salesforce's own Agentforce agents on owned properties, not third-party AI-assistant referral traffic; not directly comparable to the other rows in this table** |
| — | (context only, not AI-specific) "39% of shoppers — and 54% of Gen Z — using AI for product discovery" | survey fielded Nov 27-Dec 26, 2024 | measured (self-reported survey) | 5 | `c-salesforce-analytics-retail-trends-2025-2026-09-22.md` — stale; attitudinal, not a traffic/conversion/order figure |

## Shopify

Population (all Shopify rows with figures): Shopify's own multi-merchant platform ("Shopify's Q1 2026 commerce data" / "Shopify's Q2 commerce data") — no merchant count or session count disclosed on either page.

| Metric | Figure (verbatim) | Date window | Measured/modelled | Tier | Raw path |
|---|---|---|---|---|---|
| Traffic (orders) | "AI-referred orders on Shopify grew nearly 13x year-over-year" | Q1 2026 | measured | 5 | `c-shopify-analytics-ai-search-insights-q1-2026-09-22.md` |
| Traffic (sessions) | "Referral sessions from AI chatbots... grew more than 8x year-over-year on Shopify storefronts as of Q1 2026" | Q1 2026 | measured | 5 | `c-shopify-analytics-ai-search-insights-q1-2026-09-22.md` |
| Sales (conversion) | "AI-referred visitors convert at nearly 50% higher rates than organic search" (product detail page sessions) | Q1 2026 | measured | 5 | `c-shopify-analytics-ai-search-insights-q1-2026-09-22.md` |
| Sales (conversion, category) | "AI-referred session conversion rates outperform organic SEO in 23 of 25 merchant categories by an average of 56% within those categories" | Q1 2026 | measured | 5 | `c-shopify-analytics-ai-search-insights-q1-2026-09-22.md` |
| Sales (AOV) | "orders attributed to AI-powered search carry 14% higher average order values compared to organic search" | Q1 2026 | measured | 5 | `c-shopify-analytics-ai-search-insights-q1-2026-09-22.md` |
| Traffic (sessions) | "AI-referred sessions to Shopify storefronts grew 197% year-over-year" (also stated as "roughly 3x") | Q2 2026 | measured | 5 | `c-shopify-analytics-ai-search-category-q2-2026-09-22.md` |
| Traffic (orders) | "orders also grew 3x" | Q2 2026 | measured | 5 | `c-shopify-analytics-ai-search-category-q2-2026-09-22.md` |
| Traffic (comparator) | "organic search sessions grew 12% on a much larger base" | Q2 2026 | measured | 5 | `c-shopify-analytics-ai-search-category-q2-2026-09-22.md` |
| Sales (conversion) | "AI-referred shoppers reached a product page, they converted about 80% better than shoppers referred by organic search" | Q2 2026 | measured | 5 | `c-shopify-analytics-ai-search-category-q2-2026-09-22.md` |
| Sales (conversion, spec-led categories) | "In those categories, AI-referred shoppers converted at roughly twice the rate of organic-referred shoppers" | Q2 2026 | measured | 5 | `c-shopify-analytics-ai-search-category-q2-2026-09-22.md` |
| Sales (not AI-attributed) | "over $100 billion of GMV in the first quarter alone" | Q1 2026 (quarter ended March 31, 2026) | measured, but **not AI-attributed — total platform GMV across all channels** | 3 | `c-shopify-analytics-q1-2026-gmv-2026-09-22.md` |
| — | (no figure) Agentic Storefronts launch, ChatGPT/Copilot/AI Mode/Gemini named as channels | announced 2026-03-24 | n/a — product existence only | 3 | `c-shopify-analytics-agentic-storefronts-launch-2026-09-22.md` |
| — | (no figure) Universal Commerce Protocol (UCP) launch, co-developed with Google | announced 2026-01-11 | n/a — product existence only | 3 | `c-shopify-analytics-ucp-platform-2026-09-22.md` |
| — | (no figure) original Agentic Storefronts feature announcement (Winter '26 Edition) | announced 2025-12-10 | n/a — product existence only, stale | 3 | `c-shopify-analytics-winter26-storefronts-2026-09-22.md` |

## Unknowns per priority-1 engine

Per `plan.md`'s engine matrix, priority-1 engines are ChatGPT/OpenAI, Claude/Anthropic, and Google (AI Overviews/AI Mode/Gemini). None of the three publishers pulled in this cluster break any traffic, conversion, or order figure out per individual priority-1 engine — every figure above is an aggregate "AI" or "generative AI" category.

- `unknown — checked Adobe Digital Insights 2026-09-22` — no per-engine breakout for ChatGPT, Claude, or Google specifically anywhere in the two PDF reports or three blog posts pulled; traffic is reported only as one aggregate "generative AI tools and browsers" category.
- `unknown — checked Salesforce (Shopping Index, State of Commerce report, Agentic Enterprise Index) 2026-09-22` — no per-engine breakout for ChatGPT, Claude, or Google specifically; "third-party AI search channels like ChatGPT and Perplexity" and "AI and agents" are reported collectively, never split by engine.
- `unknown — checked Shopify Enterprise Blog 2026-09-22` — no per-engine breakout in any growth/conversion/AOV figure; ChatGPT, Perplexity, Google Gemini, Microsoft Copilot, Claude, and Grok are named only collectively as "AI chatbots" / "AI platforms." Gemini is named individually only in merchant-side analytics-filtering guidance ("for Gemini, filter 'Referrer Host' for gemini.google.com"), not attached to any growth or conversion figure.

## Screened out — further pages found by the P2-c8 queries, not pulled (no AI-specific figure with n/population/date window, or out of scope)

| Page | Reason screened out |
|---|---|
| `business.adobe.com/blog/adobe-report-ai-traffic-travel-sites-surges-200-percent` | Travel vertical, out of scope for retail/e-commerce |
| `business.adobe.com/assets/pdfs/resources/reports/ai-traffic-report/ai-sourced-traffic-insights-2025.pdf` | Superseded/duplicate of the July 2025 data already captured verbatim in `c-adobe-analytics-shopping-rises-2026-09-22.md` |
| `business.adobe.com/content/dam/dx/us/en/resources/reports/adobe-digital-insights-quarterly-report/adobe-digital-insights-quarterly-report.pdf` | Generic landing asset, no distinct dataset identified from its URL/title alone |
| `business.adobe.com/resources/sdk/q3-ai-traffic-trends-report.html` | Landing page for the Q3 PDF already pulled directly |
| `salesforce.com/news/stories/global-ai-readiness-index-insights-2025/` | Country-level AI-readiness index, not retail/e-commerce AI-referral traffic |
| `salesforce.com/news/stories/online-shopping-discounts-predictions/` | Discount/pricing forecast, not an AI-referral traffic/conversion/order figure |
| `salesforce.com/news/stories/agentforce-commerce-announcement/` | Product-release announcement; not fetched — same publisher family as the announcement-only Shopify pages already pulled, lower priority than data-bearing posts |
| `shopify.com/news/shopify-q4-2025-financial-results` | General quarterly financial results, no AI-specific breakout |
| `shopify.com/news/spring-26-edition-merchant`, `shopify.com/news/spring-26-edition-dev` | Feature-edition announcements; not fetched |
| `shopify.com/news/shopify-open-ai-commerce` | Partnership announcement; not fetched |
| `shopify.com/news/bfcm-data-2025` | Black Friday Cyber Monday sales record; WebSearch summary found no AI-specific percentage/breakdown |
| `shopify.com/news/live-globe-2024` | BFCM infrastructure/ops story, not a traffic/conversion/order figure |

## Caveats

- No figure in this table is broken out per individual priority-1 engine (ChatGPT, Claude, Google) by any of the three publishers — see Unknowns section above.
- Every Salesforce "influenced" or "driving X% of sales" figure is explicitly modelled/attributed per the source's own methodology text ("Several factors are applied to extrapolate macroeconomic figures for the broader retail industry"), never incremental. Flagged `note: modelled — attributed, not incremental` in each source raw file's header, per task instructions.
- Salesforce's Cyber Week 2025 $73B/22% figure is a forecast ("Salesforce anticipates..."), not a measurement, published ahead of the event it describes — kept per trust-rubric.md (not discarded, since the source itself labels it a prediction), but excluded from any measured-figure claim.
- Adobe's two holiday-season December 2025 traffic-growth figures conflict across two of Adobe's own publications (673% in the January 2026 blog post vs. 1,151% referenced in the April 2026 Q2 PDF) — both are the same publisher describing what appears to be the same underlying series; not reconciled, kept side by side per root `CLAUDE.md`.
- Adobe and Salesforce populations are each a single vendor's own customer/platform base (Adobe Analytics customers; Salesforce Commerce Cloud/Agentforce customers), not the open web or a general population — every figure in this table describes that publisher's own customer base, never a market-wide figure.
- Shopify's own guidance in `c-shopify-analytics-ai-search-insights-q1-2026-09-22.md` states that AI-assisted discovery via Google AI Overviews is classified as organic search in standard referral analytics, so "the actual share of AI-mediated commerce is almost certainly higher than what referral attribution alone can show" — stated by the source, not verified independently.
- Three of the six Shopify pulls (Agentic Storefronts launch, UCP platform, Winter '26 storefronts) and none of Salesforce's/Adobe's carry zero AI-specific traffic/conversion/order figures at all — confirms channels.md's C32 bias note ("Vendor-reported, no base disclosed") as the norm rather than the exception for Shopify's newsroom product announcements; the two data-bearing figures Shopify does publish sit on its Enterprise Blog, not its Newsroom.
- This table cites 16 raw pulls (5 Adobe, 5 Salesforce, 6 Shopify). Oldest pull depended on: 2025-03-24 (Salesforce Connected Shoppers Report, `c-salesforce-analytics-retail-trends-2025-2026-09-22.md`), flagged stale in its own raw file.

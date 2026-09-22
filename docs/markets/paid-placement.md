# Paid placement

| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every raw file cited. Oldest source-dated content carried: 2024-11-12, `raw/b-perplexity-ads-launch-2026-09-22.md` |
| Lane | B |
| Engines covered | P1: ChatGPT, Claude, Google (AI Overviews, AI Mode, Gemini app). P2: Microsoft Copilot, Amazon (Rufus / Alexa for Shopping), Grok. Perplexity carried (P3 after `plan.md` reweight 1) |
| Geography | Global; US and EU where a source bounds it |

## Definition and boundary
| | |
|---|---|
| Definition | Ad inventory sold inside AI assistant or AI search surfaces (`method/glossary.md`) |
| Aliases in sources | "ChatGPT Ads", "Sponsored Agents", "Conversational Discovery ads", "Offer Highlights", "Sponsored prompts", "Generative Search", "AI chatbot advertising" |
| In | Ad units and sponsored placements rendered inside AI answers or AI search surfaces; sponsored agents; sponsored prompts |
| Out | Classical search ads, except as the proxy below; agentic checkout fees (lane C); unpaid appearance (lane A) |
| Metric the market is denominated in | Spend. Ad-presence percentages count answers, never spend |

## Sizing
Disclosed figures, side by side. No total is computed: the scopes below do not nest.

| Figure, verbatim | Author | Base period | Population | Author's label | Tier | Raw |
|---|---|---|---|---|---|---|
| "$1 billion in annualized revenue run rate" | OpenAI | point-in-time, "less than 200 days after launch", published 2026-08-31 | ChatGPT Ads, "tens of thousands of advertisers", 40+ countries | "reached" | 3 | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` |
| "26% of ChatGPT responses already carry a sponsored ad"; "nearly 30% of ad-eligible Google AI Mode queries already show ads" | Similarweb | "to-date" — no window, no country stated | ChatGPT Free and Go tiers; AI Mode ad-eligible queries; "real user panel conversations", no n | "to-date" | 5 | `raw/b-similarweb-ai-ads-2026-09-22.md` |
| "ChatGPT served ads on 4.47% of US queries", "1.06 ad items" per ad-bearing answer | Adthena | Mar–May 2026 | ~850,000 AI search queries, US | measured, "captured before the European launch" | 5 | `raw/b-adthena-chatgpt-ads-europe-2026-09-22.md` |
| "0.00 percent ad frequency", "zero of the 29,237 total ad items"; US "AIO ad penetration rate of just 0.16 percent" | Adthena via PPC Land | June 2026 | 169,560 UK ChatGPT scrapes; US AI Overviews | measured | 5 (pointer, primary unreachable) | `raw/b-pointer-ppcland-uk-chatgpt-ad-share-2026-09-22.md` |

**Bottom-up inputs that exist** — engines with a live product × disclosed pricing basis × disclosed advertiser count.

| Engine | Live product | Disclosed pricing basis | Rate card | Advertiser count disclosed | Raw |
|---|---|---|---|---|---|
| ChatGPT — OpenAI | yes | CPC, CPM, outcome-optimised bidding; "$3–$5 USD per click" recommended max bid | no | "tens of thousands of advertisers" (no n) | `raw/b-openai-platform-summary-2026-09-22.md`, `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` |
| Google — AI Overviews | yes | auction — "existing auction ranking system and signals"; no unit named | no | none stated | `raw/b-google-platform-summary-2026-09-22.md` |
| Google — AI Mode | yes, stated as testing | `unknown — checked raw/b-google-platform-summary-2026-09-22.md 2026-09-22` | no | none stated | same file |
| Microsoft Copilot | yes | Microsoft Advertising auction, ManualCpc / EnhancedCpc; no Copilot-specific unit | no | none stated | `raw/b-microsoft-amazon-platform-summary-2026-09-22.md` |
| Amazon — Rufus / Alexa for Shopping | yes, GA 2026-03-25 US | CPC — "as part of your CPC bidding and billing parameters" | no | none stated | same file |
| Coverage | 5 of 8 engines carry a live product; 4 of 5 disclose a pricing basis; 0 of 8 publish a rate card; 1 of 8 discloses any revenue figure; 0 of 8 a precise advertiser count | | | | |

**Build.** Not computable. The multiplication has no price term (no engine publishes a rate card) and no count term (the one advertiser figure is "tens of thousands", not a number). Price is disclosed at two points in the whole chain below — OpenAI's recommended $3–$5 CPC bid, and Shopware's tooling list price; every take rate is unknown. No engine states a revenue growth rate with a base period.

| Result | Figure | Method | Coverage | Confidence limit |
|---|---|---|---|---|
| Bottom-up size | `unknown — checked raw/b-*-platform-summary-*, raw/e-market-size-table-2026-09-22.md 2026-09-22` | bottom-up, disclosed inputs | 0 of 8 engines supply both inputs | Sees no price and no advertiser count on any engine |

**Proxy.** `plan.md` Pass 6 names one proxy: share of search or SEO budget, analyst-derived. The search-ad-spend primary is gated — EMARKETER "US Search Advertising Forecast 2026" reached no figure, `unknown — checked emarketer.com 2026-09-22`, `raw/e-market-size-emarketer-searchad-paid-2026-09-22.md`. The only proxy figure found measures attention, not dollars: IAB, "optimizing content for AI-generated answers is now the No. 1 area of increased focus among buyers at 76%", n = "more than 200 brand and agency ad investment decision-makers", fielded ahead of a 2026-09-10 release, tier 4, `raw/e-market-size-iab-paid-2026-09-22.md`. Labelled proxy, kept out of the build.

## Forecasts — side by side, never as the size
| Author | Forecast figure | Target year | Base and method | Label | Raw |
|---|---|---|---|---|---|
| EMARKETER (Nate Elliott), via PPC Land | "$32.03 billion this year to $68.25 billion by 2030", US, all three AI ad types | 2030 | base 2026; three named categories; model paywalled | analyst-derived | `raw/e-market-size-emarketer-aiads-paid-2026-09-22.md` |
| EMARKETER, same report | standalone chatbot category "less than $1 billion" US 2026, "just over $5 billion" 2030 | 2030 | base 2026 | analyst-derived | same file |
| WPP Media (This Year Next Year, Midyear) | "Generative Search... projected to jump from $5.1 billion in 2026 to over $100 billion by 2030", global | 2030 | base 2026; channel undefined against EMARKETER's categories | analyst-derived | `raw/e-market-size-wppmedia-paid-2026-09-22.md` |
| OpenAI internal, relayed by Axios via EMARKETER | "$2.5 billion in ad revenues this year... $11 billion in 2027, $25 billion in 2028, and $53 billion in 2029... $100 billion by 2030", global | 2030 | base 2026; "a source familiar with recent presentations to investors"; assumes 2.75bn weekly users by 2030 | analyst-derived (leak, no published method) | `raw/e-market-size-emarketer-openai-paid-2026-09-22.md` |

## Growth
| Measure | From | To | Base period | Label | Raw |
|---|---|---|---|---|---|
| ChatGPT Ads consumer markets | US pilot | "over 40 countries" | 2026-02 to 2026-08-31 | company-stated | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` |
| ChatGPT Ads European markets | 0 | 31 markets, self-serve in all 31 | 2026-06-06 (UK) to 2026-08-31 | company-stated | `raw/b-openai-de-chatgpt-ads-europe-2026-09-22.md` |

## Value chain — and where margin sits
| Stage | Who does it | What is charged | Margin evidence | Label | Raw |
|---|---|---|---|---|---|
| Engine / owned auction | OpenAI, Google, Microsoft, Amazon | CPC / CPM / auction; no rate card published | Only revenue figure at any stage: OpenAI $1B run rate | company-stated | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` |
| Ad platforms and resellers | Amazon DSP into ChatGPT; OpenAI Reseller Program; agencies Dentsu, Omnicom, Publicis, WPP | `unknown — checked raw/b-amazon-ads-chatgpt-integration-2026-09-22.md 2026-09-22` — no fee, revenue share or commission stated | none | company-stated | `raw/b-amazon-ads-chatgpt-integration-2026-09-22.md`, `raw/b-openai-platform-summary-2026-09-22.md` |
| Sell-side and feed tooling | Criteo, StackAdapt, Pacvue, Kargo, Feedonomics, Shopware | Criteo GO CPM-based, no rate card; StackAdapt 5 tiers, no figure; Pacvue no pricing page (404); Kargo contact-only; Feedonomics custom-quoted, "we never take a percentage of revenue"; Shopware €600/mo Rise, €2,400/mo Evolve | Shopware is the only public rate card in the sell-side census | vendor-reported | `raw/c-vendor-census-c6-2026-09-22.md` |
| Advertiser | brands and agencies | practitioner-reported $4.41 CPC on $9,620 spend, 34 days | graded Fools gold — no control metric | company-stated | `raw/e-case-common-thread-collective-chatgpt-ads-2026-09-22.md` |

## Per-engine inventory and cells — priority-1 and priority-2 engines × paid placement
| Engine | Surface | Product live | Formats and label wording, verbatim | Pricing basis | Countries | Self-serve | Raw |
|---|---|---|---|---|---|---|---|
| ChatGPT — OpenAI | consumer chat | yes, from 2026-02-09 | below-response unit; "Ads are clearly labeled as sponsored and visually separated from ChatGPT's response"; "Sponsored Agents"; "clearly labeled conversation with a business-sponsored agent" | CPC/CPM/outcome bidding; "$3–$5 USD per click" recommended max bid | 9 named consumer countries 2026-08-11; "over 40 countries" 2026-08-31; 31 EU markets; advertiser sign-up 55 countries | yes — Ads Manager beta, plus intermediary/reseller path | `raw/b-openai-platform-summary-2026-09-22.md`, `raw/b-openai-sponsored-agents-hubspot-shopify-2026-09-22.md`, `raw/b-openai-de-chatgpt-ads-europe-2026-09-22.md` |
| Claude — Anthropic | consumer chat | no — "Claude will remain ad-free... nor will Claude's responses... include third-party product placements", 2026-02-04 | n/a | n/a | n/a | n/a | `raw/b-anthropic-perplexity-platform-summary-2026-09-22.md` |
| Google — AI Overviews | search-integrated | yes — "Ads are eligible to be shown above, below or within AI Overviews on Search" | "text, shopping, local, or app ads"; reported as "Top Ads"; no "Sponsored" wording on the pulled page | auction, no unit or figure named | 12 named countries (within-AIO); "200+ markets" (above/below) | no separate buy; existing campaigns auto-eligible, "you can't opt out" | `raw/b-google-platform-summary-2026-09-22.md` |
| Google — AI Mode | search-integrated | yes, stated as testing | "Conversational Discovery ads", "Highlighted Answers" — "will also continue to be clearly labeled as 'Sponsored.'"; "Direct Offers" labelled "Sponsored deal" | `unknown — checked raw/b-google-platform-summary-2026-09-22.md 2026-09-22` | "US" only, per a 2025-12-08 page, stale, not updated | no separate buy; PMax/Shopping/Search eligibility | same file |
| Google — Gemini app | consumer chat | `unknown — checked raw/b-google-platform-summary-2026-09-22.md 2026-09-22` | `unknown — checked` same | `unknown — checked` same | `unknown — checked` same | `unknown — checked` same | same file |
| Microsoft Copilot | consumer chat | yes — "Microsoft Advertising serves ads in varying formats which are displayed in Copilot's responses" | Multimedia, Product, Search-with-logo, Vertical ad types; "Offer Highlights", 2026-04-21. Label wording `unknown — checked raw/b-microsoft-amazon-platform-summary-2026-09-22.md 2026-09-22` | Microsoft Advertising auction, ManualCpc/EnhancedCpc; no Copilot-specific metric | Product ads ~139 countries; Offer Highlights "English-speaking markets" | yes — existing Microsoft Advertising account | `raw/b-microsoft-amazon-platform-summary-2026-09-22.md` |
| Amazon — Rufus / Alexa for Shopping | shopping assistant | yes — GA US 2026-03-25 | "Sponsored Products prompts", "Sponsored Brands prompts", "Alexa+ Conversational Ads", "Prime Video Sponsored Tiles". Label wording `unknown — checked raw/b-microsoft-amazon-platform-summary-2026-09-22.md 2026-09-22` | CPC — "we will begin to charge for these ads as part of your CPC bidding and billing parameters" | United States only | yes — existing Sponsored Products/Brands campaigns | same file |
| Grok — xAI | consumer chat | `unknown — checked raw/b-eu-dsa-ad-repositories-table-2026-09-22.md 2026-09-22` — "Grok" is never named on X's ads-transparency page | `unknown — checked` same | `unknown — checked` same | `unknown — checked` same | `unknown — checked` same | `raw/b-eu-dsa-ad-repositories-table-2026-09-22.md` |
| Perplexity (P3, carried) | consumer chat | announced 2024-11-12 ("sponsored follow-up questions"); no live ad product or advertiser page found 2026-09-22 — status read by absence | announced format wording only | subscription pricing disclosed; ad rate not disclosed | none stated | no "Advertise" path found | `raw/b-anthropic-perplexity-platform-summary-2026-09-22.md` |

**Measured-by-us.** 0 sponsored or ad units observed across 90 runs on Google AI Mode (76) and AI Overviews (14), day 0, 2026-09-22, tier 1, `raw/e-google-aimode-panel-2026-09-22-retry.md`. One date, one network path, logged-out, IP-localised to Vietnam (Vietnamese UI, VND prices, some answers generated in Vietnamese); 14 of 14 AI Overviews checks rendered no block at all. The absence is text-extraction-scoped: `get_page_text` would miss an icon-only or CSS-only "Sponsored" label. It bounds nothing about the market.

## Structural checks
| Check | Answer | As of | Label | Raw |
|---|---|---|---|---|
| Substitute — what the brand does instead; is "do nothing" the real competitor | Keep buying search and retail media: it auto-serves into AI surfaces. Google — existing Search/Shopping/PMax campaigns eligible, "you can't opt out"; Microsoft reuses Microsoft Advertising Network ad types; Amazon reuses Sponsored Products/Brands CPC bids. EMARKETER: "over 80% flows next to AI content, not inside chatbots" | 2026-06 to 2026-09 | company-stated; analyst-derived | `raw/b-google-platform-summary-2026-09-22.md`, `raw/b-microsoft-amazon-platform-summary-2026-09-22.md`, `raw/e-market-size-emarketer-aiads-paid-2026-09-22.md` |
| Platform risk — which engine ships native tooling making third-party vendors redundant | Every engine with a live product owns its auction. OpenAI ships self-serve Ads Manager, Pixel, Conversions API, "more than 50 technology and measurement partners", plus HubSpot and Shopify apps. Third parties resell (Amazon DSP, StackAdapt, Criteo, Kargo, Pacvue) or measure what no engine discloses (Similarweb AI Ads) | 2026-09 | company-stated; vendor-reported | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md`, `raw/b-openai-sponsored-agents-hubspot-shopify-2026-09-22.md`, `raw/c-vendor-census-c6-2026-09-22.md`, `raw/b-similarweb-ai-ads-2026-09-22.md` |
| Incumbent bundling — which incumbent added this as a feature, at what price delta | Microsoft Advertising and Amazon Ads both bundle: same ad types, same auction, same CPC bid, new surface, no separate SKU. Price delta `unknown — checked raw/b-microsoft-amazon-platform-summary-2026-09-22.md 2026-09-22` — neither publishes a rate card. Acquisitions (addition 1): none recorded in the paid sell-side census; Feedonomics sits inside Commerce (Nasdaq: CMRC, formerly BigCommerce) | 2026-03 to 2026-09 | company-stated; vendor-reported | `raw/b-microsoft-amazon-platform-summary-2026-09-22.md`, `raw/c-vendor-census-c6-2026-09-22.md` |
| Regulatory — ad-disclosure rules in force at the pull date | EU AI Act Art. 50(1)–(4) in force 2026-08-02: AI-interaction notice and synthetic-content marking; names no assistant. DSA Art. 26 (ad identification) and Art. 27 (recommender parameters) bind "online platforms" — whether an AI chat surface is one is `unknown — checked eur-lex CELEX:32022R2065 2026-09-22`. Art. 39 repositories: ChatGPT designated VLOSE 2026-08-31, 159.1M EU users, no repository yet, ~January 2027 window; Google Search, Bing, Amazon Store and X have repositories but none distinguishes an ad inside an AI answer; Claude and Perplexity not designated, self-stated below the 45M threshold. FTC 16 CFR 255 §255.5(a) material connection and §255.0(f) clear-and-conspicuous, plus the Native Advertising Guide — none names AI. UK CMA fair-ranking conduct requirement, 2026-06-17, covers organic ranking in "search generative AI features", not paid. No enforcement action found against any engine on AI-answer ad disclosure | 2026-09-22 | filed | `raw/b-regulators-ad-disclosure-table-2026-09-22.md`, `raw/b-eu-dsa-ad-repositories-table-2026-09-22.md` |

## Litigation naming ad or referral harm
| Caption | Court, case no. | Engine | Figure, verbatim | Tier | Raw |
|---|---|---|---|---|---|
| In Re: OpenAI Copyright Infringement Litigation, News Plaintiffs' SJ brief, ECF 1977-1 | S.D.N.Y. 1:25-md-03143 | Microsoft Copilot; ChatGPT | "Microsoft recording 83-93% drops in click-through rates for The Times and DNP's domains, and 51% to 94% for ZD's domains" (p.10); restated as "87% to 93% for The Times's websites, 83% to 91% for DNP's websites, and 51% to 94% for ZD" (p.76) — both verbatim, unreconciled in the brief itself. Also "87.78% of ChatGPT users visit no external websites during their search, compared to only 26.91% of Google users" (SF1539, third-party study as cited, not opened) | 2 | `raw/a-court-mdl-microsoft-ctr-data-2026-09-22.md` |
| Chegg, Inc. v. Google LLC | D.D.C. 1:25-cv-00543 | Google AI Overviews | "71% of Chegg Study traffic" and "60% of Chegg Study acquisitions" from search referrals (2024); Google "$200 billion" annual search revenue | 2 | `raw/b-court-dockets-table-2026-09-22.md` |
| Penske Media Corp. v. Google LLC | D.D.C. 1:25-cv-03192 | Google AI Overviews, AI Mode | Count V: "nearly 60%" of Google searches zero-click, "over 80%" among AI-Overview searches; organic affiliate revenue "declined by more than a third" by end-2024; new count pleads unlawful tying of AI Overviews to general search | 2 | same file |
| Dow Jones and NYP Holdings v. Perplexity | S.D.N.Y. 1:24-cv-07984 | Perplexity | ¶73 Publishers' Program ad-revenue share an "unspecified portion"; ¶70 "virtually no click-through traffic" | 2 | same file |

No docket found alleges harm from an ad unit inside an AI answer. Every row above pleads referral or substitution harm.

## Unknowns
| Question | Channels checked | Date |
|---|---|---|
| Any engine rate card (CPC/CPM), and a precise advertiser count for any engine ("tens of thousands" is the only figure) | openai.com, openai.com/de-DE, support.google.com/google-ads, about.ads.microsoft.com, advertising.amazon.com | 2026-09-22 |
| Take rate or revenue share at any reseller or sell-side stage | advertising.amazon.com ChatGPT integration page, criteo.com, stackadapt.com, pacvue.com (404), kargo.com | 2026-09-22 |
| Ad format inside the Gemini app | support.google.com/google-ads, blog.google/products/ads-commerce, developers.google.com/search | 2026-09-22 |
| On-surface label wording for Copilot and for Amazon prompts | Microsoft and Amazon own pages pulled in P2-c6 | 2026-09-22 |
| Pricing model for Google AI Mode's five named ad formats | `raw/b-google-gml2026-search-ads-2026-09-22.md`, `raw/b-google-ads-highlights-2025-2026-09-22.md` | 2026-09-22 |

## Caveats
- Nothing here is a size. The bottom-up build is not computable: no engine publishes a price, none publishes an advertiser count, and the one revenue figure in the sub-market is a company's statement about itself.
- Every dollar total with a horizon above (EMARKETER, WPP Media, the Axios-relayed OpenAI figures) is its author's own forecast; their category boundaries are undefined against each other, and EMARKETER's US $68.25B and WPP's global $100B+ are not reconciled or averaged.
- Product existence, formats, countries and pricing basis are all company-stated from each engine's own pages — reliable on existence, biased on framing (`method/trust-rubric.md` tier 3). Google's AI Mode country scope and Copilot's engagement blog rest on pages dated 2025-12-08 and 2025-08-06, both past the staleness cutoff and flagged stale in their own raw files.
- Ad-presence percentages conflict irreconcilably and sit side by side: Similarweb 26% of ChatGPT responses (no n, no window) against Adthena 4.47% of US queries (Mar–May 2026, ~850k queries) and 0.00% of 169,560 UK scrapes (June 2026).
- The measured-by-us row is one date, 90 runs, one localised network path, and text-extraction-scoped. It is not evidence that AI Mode carries no ads.
- The only practitioner-level price and return figures ($4.41 CPC, ROAS 3.3x–6.8x) are graded Fools gold — agency-authored, brand unnamed, no control metric — and are cited as category noise, not performance evidence.
- The category is roughly two years old as of 2026-09; every figure is a point reading, and the staleness rule in `../method/plan.md` applies to each pull cited.

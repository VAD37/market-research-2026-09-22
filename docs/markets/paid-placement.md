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

### Pass 12 addition, 2026-09-23

Task P12-ads. Appended only; lines above unchanged. Where a figure here differs from one above, both stand. Raw: 91 files `raw/b-*-2026-09-23.md`. Finding: `findings/ai-ads-evidence.md`.

**Size inputs — revenue and advertiser counts.** No total is computed; scopes do not nest.

| Figure, verbatim | Author | Date or window | Scope | Label | Tier | Raw |
|---|---|---|---|---|---|---|
| "$100 million annualized revenue mark"; "over 600 advertisers" | OpenAI spokesperson via Reuters | 2026-03-26 | ChatGPT US pilot | company-stated | 5 | `raw/b-reuters-openai-ads-100m-2026-09-23.md` |
| "roughly $83 million a month" behind the $1B run rate | Digiday | 2026-08-31 | ChatGPT | analyst-derived | 5 | `raw/b-digiday-openai-ads-1bn-2026-09-23.md` |
| "3x return on ad spend across its campaigns over 28 days" | OpenAI | 2026-08-31 | one unnamed advertiser | company-stated | 3 | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` |
| ~300 (April) → "more than 820" (July) advertisers | Sensor Tower via Business Insider | 2026-04 to 2026-07 | US ChatGPT mobile app, panel | vendor-reported | 5 | `raw/b-biggo-sensortower-advertisers-820-2026-09-23.md` |
| "approximately 1,200 unique advertisers"; ad density +163% | Sensor Tower via PPC Land | August 2026 vs April | US, mobile and desktop | vendor-reported | 5 | `raw/b-ppcland-sensortower-chatgpt-mix-2026-09-23.md` |
| 7,378 distinct advertisers; US 4,982 | Adthena index via PPC Land | 2026-07-13 to 07-20 | US, UK, AU, rest of world | vendor-reported | 5 | `raw/b-ppcland-adthena-7378-advertisers-2026-09-23.md` |
| 5,171 unique advertisers; 3,770 active in 7 days | Similarweb | 2026-03-30 to 2026-06-08 | global panel, n not stated | vendor-reported | 5 | `raw/b-similarweb-chatgpt-ad-stats-2026-09-23.md` |
| 1,159 unique advertisers | SE Ranking | publ. 2026-08-10 | 50,006 US commercial prompts | vendor-reported | 5 | `raw/b-seranking-chatgpt-ads-study-2026-09-23.md` |
| "over 2,000 brands… through Criteo" (June); "More than one thousand" (May) | Criteo | 2026-05 to 2026-06 | Criteo API clients only | vendor-reported | 3 | `raw/b-criteo-openai-update-june-`, `b-criteo-openai-update-may-2026-09-23.md` |
| Search & Other "over $63 billion"; no AI-surface line | Alphabet | Q2 2026 | Google Search | company-stated | 3 | `raw/b-alphabet-q2-2026-earnings-transcript-2026-09-23.md` |
| search ad revenue ex-TAC +10%; no Copilot line | Microsoft | FY26 Q4 | Search and news | company-stated | 3 | `raw/b-microsoft-fy26-q4-release-2026-09-23.md` |
| ads "$17.2 billion… up 22%" vs "24%"; no Rufus line | Amazon (Jassy) vs PPC Land | Q1 2026 | all Amazon ads | company-stated | 3 vs 5 | `raw/b-amazon-jassy-q1-2026-ads-`, `b-ppcland-amazon-q1-2026-ads-2026-09-23.md` |

**Prices published.** No engine publishes a unit price. Every figure found:

| Price | Seller | Kind | Tier | Raw |
|---|---|---|---|---|
| minimum daily spend 25 USD, 15 EUR, 15 GBP, 2,500 JPY, 725 INR; 23 currencies | OpenAI | floor on spend, not unit price | 3 | `raw/b-openai-help-create-campaigns-2026-09-23.md` |
| launch "$60" CPM, $200,000–$250,000 minimum; "$25" CPM mid-April; $50,000; minimum removed 2026-05-05 | OpenAI, as reported | trade-reported history | 5 | `raw/b-digiday-openai-ads-fomo-cpm-`, `b-ppcland-adthena-europe-benchmark-2026-09-23.md` |
| CPC ~$7, CTR ~0.6%, "no conversions" | agency executives via MediaPost | practitioner hearsay, no n | 5 | `raw/b-trendingtopics-openai-ads-1bn-2026-09-23.md` |
| "Rates starting from just $3 CPM" | Kontext | published floor, third-party apps | 3 | `raw/b-kontext-advertisers-page-2026-09-23.md` |
| $2.50 CPM vs Facebook $7.35 (one pilot); revenue share 25–30% | Kontext documents via PPC Land | pilot and take rate | 5 | `raw/b-ppcland-kontext-10m-2026-09-23.md` |

**Measured presence and CTR — side by side, not reconciled.**

| Figure | Measurer | Window | n | Tier | Raw |
|---|---|---|---|---|---|
| ChatGPT ads in ~0.8% of responses | Adthena | launch weeks, undated | 500+ prompts | 5 | `raw/b-adthena-ads-in-ai-search-2026-09-23.md` |
| ChatGPT 24.7% US; AI Mode 5.8% | Adthena email | July 2026 | not stated | 5 | `raw/b-ppcland-adthena-7378-advertisers-2026-09-23.md` |
| ChatGPT 26% US desktop (14% May); CTR 0.50% | Similarweb | June 2026 | not stated | 5 | `raw/b-ppcland-similarweb-ai-ads-2026-09-23.md` |
| ChatGPT 25.94%; 14.35% off-topic; 96.37% advertiser uncited | SE Ranking | publ. 2026-08-10 | 50,006 prompts | 5 | `raw/b-seranking-chatgpt-ads-study-2026-09-23.md` |
| SE Ranking own campaigns: 97,000+ impressions, 1,263 clicks, CTR 1.30%, "very few sign-ups" | SE Ranking | "roughly two weeks" | 48 ads | 5 | same file |
| AI Mode text ads 29.45%; 71.1% show two ads | SE Ranking | 2026-06-30 | 50,032 keywords | 5 | `raw/b-seranking-aimode-ads-study-2026-09-23.md` |
| AIO ads 0.052% → 0.12% of US queries | Adthena | 2025-11-24; April 2026 | 25,000 SERPs; not stated | 5 | `raw/b-ppcland-adthena-29m-report-2026-09-23.md` |
| CTR 0.91%, one client; "just 3%" of $250K spent after weeks | Adthena via Campaign | 2026-03 | 1 client each | 5 | `raw/b-campaign-chatgpt-ads-underwhelming-2026-09-23.md` |

**Value chain — additions.** Take rate at every intermediary: `unknown — checked criteo.com, wppmedia.com, dentsu.com, kontext.so, koahlabs.com 2026-09-23`, except Kontext's reported 25–30%.

| Stage | Who | Evidence | Tier | Raw |
|---|---|---|---|---|
| Engine auction | OpenAI "relevance-weighted, second-price auction"; CPM, CPC, oCPC, oCPM billing | help centre | 3 | `raw/b-openai-help-ads-basics-`, `b-openai-help-conversion-optimized-2026-09-23.md` |
| Agencies | WPP (Adobe, Ford, Mazda named), Omnicom ("more than 30 of its clients"), dentsu | launch-day statements, 2026-02-09 | 3 / 5 | `raw/b-wppmedia-openai-ads-pilot-`, `b-mediapost-openai-pilot-agencies-`, `b-dentsu-openai-ads-pilot-2026-09-23.md` |
| Engine into another chatbot | Microsoft Advertising sells "Sponsored Links in Snapchat's My AI" | 2023 page, 2026 status unknown | 3 | `raw/b-microsoft-ads-snap-my-ai-partnership-2026-09-23.md` |
| Networks into third-party AI apps | Kontext ($10M seed), Koah ($5M seed; "more than $26 million" total), Gravity ($30.5M Series A), ZeroClick ($55M, "over 10,000 advertisers"), Taboola (opened 2026-06-16, no price) | funding and launch reports | 3 / 5 | `raw/b-ppcland-kontext-10m-`, `b-adweek-koah-series-a-`, `b-contentgrip-gravity-series-a-`, `b-mi3-zeroclick-55m-`, `b-taboola-genai-ad-platform-2026-09-23.md` |

**Per-engine updates.**

| Engine | Update, verbatim where quoted | Tier | Raw |
|---|---|---|---|
| ChatGPT | carousel ≈23% of US desktop ads 2026-08-15 to 08-30; Sponsored Agents "limited alpha test"; EEA: "Personalized ads are not initially available" | 3 / 5 | `raw/b-ppcland-sensortower-chatgpt-mix-`, `b-openai-help-sponsored-agents-`, `b-openai-help-ads-in-chatgpt-2026-09-23.md` |
| Google AI Mode | Direct Offers pilots Gap, L'Oréal, Chewy (Q1), IHG (Q2); Highlighted Answers "clearly marked sponsored links"; AI Mode "one billion monthly active users" | 3 | `raw/b-alphabet-q1-2026-earnings-transcript-`, `b-alphabet-q2-2026-earnings-transcript-2026-09-23.md` |
| Gemini app | "our focus right now is on AI Mode… we're not rushing anything here" (Q1); 950 million MAU (Q2); no ads | 3 | same two files |
| Perplexity | "winding down its advertising programme by the end of 2026"; "fewer than 0.5% of brands who applied" admitted | 5 | `raw/b-campaign-perplexity-ads-end-2026-09-23.md` |
| Copilot | "fully ramped in all English, French, and German speaking markets", 2025 page, stale | 3 | `raw/b-microsoft-ads-copilot-formats-blog-2026-09-23.md` |
| Amazon Alexa for Shopping | active users "close to doubling", interactions "up over 5x" (Q2); no assistant ad figure | 3 | `raw/b-amazon-q2-2026-release-2026-09-23.md` |
| Meta AI, Grok, Duck.ai, Brave Leo | no ad unit named; Meta uses AI-chat data for Facebook/Instagram targeting (2025-10); Grok plan 2025-08 only | 3 / 5 | `raw/b-meta-q2-2026-release-`, `b-techcrunch-meta-ai-chat-ad-targeting-`, `b-techcrunch-grok-ads-plan-`, `b-duckduckgo-duckai-help-`, `b-brave-leo-page-2026-09-23.md` |

**Structural checks — additions.** Regulatory: ChatGPT VLOSE obligations "start applying in January 2027" (`raw/b-techpolicy-chatgpt-dsa-designation-2026-09-23.md`, 5); FTC 2026-07-01 proposed statement on AI "accuracy" names ideological distortion, not ads (`raw/b-ftc-ai-accuracy-policy-statement-2026-09-23.md`, 2); Google's July 2026 AI-label policy covers AI-made creatives, not ads inside answers (`raw/b-google-adspolicy-ai-labeling-2026-09-23.md`, 3); no enforcement against an ad inside an AI answer found, `unknown — checked ftc.gov, asa.org.uk, techpolicy.press 2026-09-23`. Supply: "fewer than 20% are shown ads daily" of ~85% eligible, 2026-03 (`raw/b-reuters-openai-ads-100m-2026-09-23.md`, 5).

**Caveats — this addition.** Every panel figure is from a vendor selling the data; none publishes panel n. Advertiser counts differ by scope (global all-time, US month, three-market week, prompt sample) and are never summed. Snap, Copilot-format and Grok sources predate one quarter. Tier 6 noise filed, not used: `raw/b-seroundtable-similarweb-ctr-`, `b-novadata-rufus-ads-free-`, `b-trendsvc-ai-ad-networks-`, `b-q1media-chatgpt-ads-results-2026-09-23.md`.

### Pass 13 addition, 2026-09-23

Per `../method/plan.md` Pass 13. Compiled read: `../findings/market-potential.md`. Nothing above is edited.

| Read | Figure | As of | Label, tier | Raw |
|---|---|---|---|---|
| Ad-supported reach, ChatGPT | 700M → 900M → "more than 1 billion weekly active users" | 2025-09-15 → 2026-02-27 → 2026-08-31 | company-stated, 3 | `raw/e-openai-chatgpt-user-counts-2026-09-23.md` |
| Floor — one engine discloses | **≥ $1B annualized run rate**, ChatGPT Ads; 1,000 ÷ 224,532 = 0.45% of Google Search & other 2025 | 2026-08-31; FY2025 | company-stated 3; filed 2 | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md`; `raw/b-alphabet-10k-2025-search-revenue-2026-09-23.md` |
| Baseline — Google Search & other | $175,033M (2023) → $198,084M (2024) → $224,532M (2025) | FY | filed, 2 | `raw/b-alphabet-10k-2025-search-revenue-2026-09-23.md` |
| Baseline — other engines' search ads | Microsoft search ad revenue ex-TAC +21% (FY25 Q4) → +10% (FY26 Q4), growth only; Amazon advertising services $19.8B, +26% (quarter to 2026-06-30) | 2025-07-30 → 2026-07-30 | company-stated, 3 | `raw/e-microsoft-copilot-user-counts-2026-09-23.md`; `raw/c-amazon-rufus-user-sales-statements-2026-09-23.md` |
| New forecasts, never sizes | EMARKETER US AI search "slightly more than $1 billion" 2025 → "nearly $26 billion" 2029, 0.7% → 13.6% of search ad spend; WPP generative search $5.1B (2026) → "over $100 billion" (2030), search incl. generative "21.8%" of $1.3T (2026); MAGNA search + retail media $357B (2025) | pub. 2025-06-04; 2026-06-16; 2025-06-17 | analyst-derived, 5 | `raw/e-market-size-mediapost-emarketer-aisearch-paid-`, `-wppmedia-midyear-paid-`, `-magna-2025-paid-2026-09-23.md` |
| Forecast spread | 2030: ~20× (EMARKETER US chatbot "just over $5 billion" to WPP/OpenAI $100B+, scopes differ); 2029: 2.05× | 2029, 2030 | analyst-derived, 5 | same, plus `raw/e-market-size-emarketer-*-2026-09-22.md` |

**Caveats — Pass 13 addition.** This append takes the file past its 120-line budget; overrun recorded here. The 0.45% ratio compares a run rate with a fiscal year. Pass 12 (`findings/ai-ads-evidence.md`) was live in parallel and is not read here. MAGNA's 2025 figure is stale; its 2026 editions were not located.

## Tier revisions, P9-r, 2026-09-23
sec.gov Archives re-fetched 2026-09-23 (HTTP 200; 403 on 2026-09-22). Rows above are not edited; each row below sits beside its original.

| line | row | tier revised 2026-09-23 | raw |
|---|---|---|---|
| 140 | Microsoft FY26 Q4, search ad revenue ex-TAC +10%, no Copilot line | 3 → 2 (filed 8-K Exhibit 99.1; the 10-K renames the line "Search advertising (formerly Search and news advertising)", FY +12%) | `raw/b-sec-microsoft-8k-ex991-2026-07-29-2026-09-23.md`; `raw/b-sec-microsoft-10k-2026-07-29-2026-09-23.md` |

## Baselines beyond Google, P16-c1, 2026-09-23
Filed ad-revenue lines the AI-surface figures above sit against. Scopes do not nest; nothing is summed or divided. Raw prefix `raw/`, suffix `-2026-09-23.md`.

| Company | Line item | Period | Figure verbatim | Source kind | Tier | Raw |
|---|---|---|---|---|---|---|
| Alphabet | "Google Search & other" (USD M) | FY2023 → FY2025 | "$ 175,033 $ 198,084 $ 224,532" | filed | 2 | `b-alphabet-10k-2025-search-revenue` — cite confirmed: Archives URL HTTP 200, 2026-09-23 |
| Microsoft | "Search advertising (formerly Search and news advertising)" (USD M) | FY2026, FY2025, FY2024 (June) | "15,176 13,878 12,306" | filed | 2 | `b-microsoft-10k-fy2026-search-advertising` |
| Microsoft | same, ex-TAC growth | FY2026; Q4 FY2026 | "increased 12%"; "increased 10% (up 9% in constant currency)" | filed | 2 | same; `b-microsoft-8k-q4-fy2026-search-advertising` |
| Amazon | "Advertising services" (USD M) | FY2023 → FY2025 | "46,906 56,214 68,635" | filed | 2 | `b-amazon-10k-2025-advertising-services` |
| Amazon | "Advertising services" (USD M) | Q2 2025 → Q2 2026; H1 | "15,694 19,809"; "29,615 37,052" | filed | 2 | `b-amazon-10q-q2-2026-advertising-services` |
| Meta | "Advertising" (USD M) | FY2025, FY2024, FY2023 | "$ 196,175 $ 160,633 $ 131,948 22% 22%" | filed | 2 | `b-meta-10k-2025-advertising-revenue` |
| Meta | "Advertising" (USD M) | Q2 2026 vs Q2 2025; H1 | "$ 59,363 $ 46,563 27%"; "$ 114,387 $ 87,955 30%" | filed | 2 | `b-meta-10q-q2-2026-advertising-revenue` |
| Reddit | "Advertising revenue" (USD thousands) | FY2025, FY2024, FY2023 | "$ 2,062,480 $ 1,185,456 $ 788,782" | filed | 2 | `b-reddit-10k-2025-advertising-revenue` |
| Reddit | "Advertising revenue" (USD thousands) | Q2 2026 vs Q2 2025 | "$ 761,625 $ 464,785" | filed | 2 | `b-reddit-10q-q2-2026-advertising-revenue` |
| Walmart | "Global advertising business" | Q2 FY2027, to 2026-07-31 | "up 38%"; "43% increase in Walmart Connect (ex-VIZIO)"; no dollar figure | filed | 2 | `b-walmart-8k-q2-fy2027-advertising` |
| Walmart | 10-K FY2026 | FY to 2026-01-31 | no advertising-business revenue figure; "emerging agentic shopping tools and platforms" named as competitors | filed | 2 | `b-walmart-10k-fy2026-advertising` |

AI-surface ad line inside any of these filers: none stated. Microsoft names Copilot only inside the Search advertising family; Meta attributes no ad revenue to Meta AI; Amazon's 10-K and 10-Q do not contain "Rufus"; Reddit names Reddit Answers as a search feature, not an ad line.

**Industry totals.** Forecasts labelled forecast; never a size.

| Author | Figure verbatim | Scope, period | Author's label | Tier | Raw |
|---|---|---|---|---|---|
| IAB / PwC | "$294.6 billion in 2025, reflecting a 13.9% year-over-year increase"; Search "$114.2B", "11%", "38.8%"; Commerce Media "$63.4B", "18%", "21.5%" | US, FY2025 | measured benchmark; "Search revenues (including AI search)" | 4 | `e-iab-pwc-internet-ad-revenue-fy2025` |
| MAGNA, Search Report | "$330 billion globally in 2024, capturing 35% of total ad spend and 50% of digital ad spend"; US "$152 billion" | global, US; 2024 | estimate | 5 | `e-magna-search-report-page` |
| dentsu | "increase by 5.1 percent in 2026, surpassing 1 trillion US dollars"; Americas "460.5 billion US dollars"; retail media "14.1 percent growth"; digital "68.7 percent of total investment" | global, 2026 | forecast | 5 | `e-dentsu-global-ad-spend-forecast-2026` |
| Gartner | "more than 70% of global ad spend and 80% of U.S. ad spend will flow through self-serve advertising platforms in which AI materially influences media buying" | global, US; by 2028 | prediction (forecast) | 5 | `e-gartner-ad-platforms-prediction-2028` |
| MAGNA 2026 editions | `unknown — checked magnaglobal.com ×4 pages 2026-09-23`; pointer only: "U.S. advertising spending will grow 11% in 2026" | US, 2026 | forecast, relayed by a blog | 6 | `e-magna-dec-2025-pointer-mediaconfidential` |
| WPP Media, midyear 2026 | already compiled at Pass 13 row above ("21.8% of total advertising revenue in 2026") | global, 2026 | forecast | 5 | `e-market-size-wppmedia-midyear-paid` |

**Caveats — this append.** Fiscal years differ (Microsoft June, Walmart January, others December). Amazon's line spans sponsored, display and video on every Amazon surface; Microsoft's includes Microsoft News, Edge and third-party affiliates; Meta and Reddit are social. IAB's categories overlap (shares sum past 100%). IAB report body, Gartner CMO Spend and MAGNA 2026 forecasts unreached — `f-search-engines-wall-log-2026-09-23.md`. Alphabet cite re-checked, not re-pulled. File further over its 120-line budget; overrun is this append.

## Primary re-pulls, REPULL-1, 2026-09-23
- 820 ChatGPT advertisers (Sensor Tower) · `raw/b-biggo-sensortower-advertisers-820-2026-09-23.md` (5) · `raw/b-businessinsider-sensortower-chatgpt-advertisers-primary-2026-09-23.md` (4) · "from around 300 in April to more than 820 this July, with at least 160 of that tally joining this month" (Sensor Tower estimate; Business Insider 2026-07-31); financial services "rising from 2% to 12% since April" · agrees
- US AI ad spend $32.03bn 2026 to $68.25bn 2030 · `raw/e-market-size-emarketer-aiads-paid-2026-09-22.md` (5) · `raw/e-market-size-emarketer-aiads-primary-2026-09-23.md` (4) · "AI ad spending will more than double in the next five years to $68.25 billion in 2030"; chart labels "$32.03" (2026), "$68.25" (2030), "2.1x"; "More than 80% of AI advertising in 2026 will appear next to AI content" (EMARKETER, 2026-06-04) · agrees; chatbot sub-figures (<$1bn 2026, ~$5bn 2030) and the $60 → ~$15 CPM line not in primary (public page; body behind PRO+)
- US search ad spend forecast (no figure reached) · `raw/e-market-size-emarketer-searchad-paid-2026-09-22.md` (n/a) · `raw/e-market-size-emarketer-searchad-primary-2026-09-23.md` (4) · "Google will earn 48.5% of search ad spending in 2026, the first time in more than 20 years that number has fallen below half" (EMARKETER, 2026-05-14) · not in primary (AI share of search ad spend / SEO budget shift — still `unknown — checked emarketer.com 2026-09-23`)
- Perplexity sponsored follow-up format · `raw/b-perplexity-ads-launch-2026-09-22.md` (3) · `raw/b-perplexity-ads-launch-primary-2026-09-23.md` (3) · post text identical (14 paragraphs); FIG. 01 example ad rendering saved at `raw/img/b-perplexity-ads-launch-primary-2026-09-23/01-perplexity-fig01-sponsored-follow-up-example.png` (unread until IMG-1) · agrees
- Google AI Mode ad formats (GML 2026 example media) · `raw/b-google-gml2026-search-ads-2026-09-22.md` (3 — text only, format examples not captured) · `raw/b-google-gml2026-search-ads-primary-2026-09-23.md` (3) · the six format examples (Conversational Discovery, Highlighted Answers, AI-powered Shopping ads, Business Agent for Leads, Promotional bundling + native checkout, Travel deals) are mp4 videos on storage.googleapis.com, 4.2–22.4 MB each; no chart or table image on the page · not in primary as images (videos; URLs recorded in `raw/img/INDEX.csv`, not downloaded); text unchanged
- OpenAI projects $2.5bn ad revenue 2026, $100bn by 2030 · `raw/e-market-size-emarketer-openai-paid-2026-09-22.md` (5 — EMARKETER relay) · `raw/e-market-size-axios-openai-ad-revenue-projection-primary-2026-09-23.md` (5) · "OpenAI expects to generate $2.5 billion in ad revenue this year and $100 billion by 2030, according to a source familiar with recent presentations to investors"; "$11 billion in 2027, $25 billion in 2028 and $53 billion by 2029"; "assume OpenAI's products reach 2.75 billion weekly users by 2030"; "ad pilot generated $100 million in annual recurring revenue in under two months" (Axios, 2026-04-09) · agrees
- ChatGPT 800M/900M WAU; $122B raise · `raw/e-openai-chatgpt-user-counts-2026-09-23.md` (3 — this URL 403; WAU from another OpenAI page) · `raw/e-openai-122bn-raise-user-counts-primary-2026-09-23.md` (3) · "$122 billion in committed capital at a post money valuation of $852 billion"; "more than 900 million weekly active users, and over 50 million subscribers"; "We are now generating $2B in revenue per month"; "our ads pilot reached more than $100 million in ARR in under six weeks"; enterprise "more than 40% of our revenue" (2026-03-31) · agrees (900M WAU, 50M subscribers); adds the ads-pilot ARR figure at an OpenAI URL

## EU depth, P16-c3, 2026-09-23
Regional facts outside DE for paid placement. Raw prefix `raw/`, suffix as stated.

| Fact | Countries | Statement verbatim | Source kind | Date | Tier | Raw |
|---|---|---|---|---|---|---|
| ChatGPT Ads availability, named EU countries | DE, FR, ES, IT, SE, NO, DK, NL, AT named; UK not named on this page | "Nächste Woche wird ChatGPT Ads auf 31 europäische Länder ausgeweitet, darunter Deutschland, Frankreich, Spanien, Italien, Schweden, Norwegen, Dänemark, die Niederlande und Österreich." | company-stated | 2026-08-18, update 2026-08-31 | 3 | `b-openai-de-chatgpt-ads-europe-2026-09-22.md` (already compiled as "31 EU markets"; per-country naming added here) |
| ChatGPT Ads, UK | UK | `unknown — not in the named list; whether the UK is among "over 40 countries" not stated on pages pulled; checked 2026-09-23` | — | — | — | same; `b-openai-1bn-run-rate-milestone-2026-09-22.md` |
| In-product ad reporting, ChatGPT | all markets | "To report an ad in ChatGPT: On the ad, click ⋯ (top right). Select Report this ad. In the pop-up, choose why you're reporting it." and "If you are a UK user and wish to opt out of future communications once you have submitted your report, please use the content reporting form" | company-stated | help article "Updated: 6 days ago" at archive capture (latest CDX 2026-03-18) | 3 | `b-openai-help-reporting-content-personal-data-removal-2026-09-23.md` |
| Google AI Overviews, France | FR | not rolled out in France as of 2026-03 (relay of Google documentation) — within-AIO ad eligibility in France follows from surface absence, not from an ad-policy statement | analyst-derived relay | 2026-03 | 5 | `a-reuters-dnr-2026-ai-chatbots-countries-2026-09-23.md` |
| EU ad repository, Bing | EU | Microsoft Ad Library named as the DSA Art. 39 repository; Copilot not named (already compiled) | company-stated | 2026-09-22 | 3 | `b-eu-microsoft-dsa-bing-2026-09-22.md` |
| Per-country assistant reach, paid inventory context | UK, FR, ES, IT, NL | StatCounter referral shares 2026-08 and Eurostat 2025 use rates — see `findings/market-potential.md` "EU engine share and users, P16-c3" | analyst-derived | 2026-08; 2025 | 4; 3 | `a-statcounter-ai-chatbot-share-eu-countries-2026-09-23.md`; `a-eurostat-genai-use-individuals-2025-2026-09-23.md` |
| Regulator statements on AI ads, per country | UK (Ofcom), ES (CNMC), IT (AGCOM) | none found: Ofcom site 403; CNMC press listing carries no AI line; AGCOM Rapporto IA 2026 Part I ENG carries no ad-disclosure statement in the lines read | — | 2026-09-23 | — | `b-regulators-eu-genai-usage-checks-2026-09-23.md` |
| Public tenders naming paid AI surfaces | EU | TED `FT~"ChatGPT Ads"` 0, `"sponsored answers"` 0 (already recorded, R-BLOCKED-2); `FT~"Perplexity"` 6 notices, DEU 6 of 6 | filed | 2025-06-06 to 2026-05-28 | 2 | `f-ted-ukcf-S10-eu-country-brand-accuracy-2026-09-23.md` |

**Caveats, this append.** Country availability rests on one OpenAI locale page and its named examples; the full 31-country list was not published on it. ASA/CAP and DSA rows from 2026-09-22 stand unchanged. File over its 120-line budget; overrun includes this append.

## Image reads, IMG-1b, 2026-09-23
| Figure / text as shown | Chart or image | Date | Tier | Img raw |
|---|---|---|---|---|
| On-surface label wording, Copilot ad unit: card header "Microsoft Advertising"; label line "Sponsored ···" inside the unit; advertiser placeholders Contoso / Fabrikam — fills the `unknown — checked` label-wording cell in the engine table above (row "Microsoft Copilot") from the vendor's own mock-ups, not a live capture | "Example feed-based ad in Copilot", "Example Multimedia ad in Copilot", "Example Search ad in Copilot" (three help-page images) | page ms.date 2026-06-18, updated 2026-09-02 | 3 | `raw/b-microsoft-ads-in-copilot-primary-2026-09-23-img-2026-09-23.md` |
| Feed-based unit: five product cards with price and advertiser (e.g. "119.97" struck "$154", Contoso.com); Multimedia unit: image + headline + "Book Now" button + URL; Search unit: headline + sitelink-style title + Contoso.com | same three images | same | 3 | same |
| Merchant Center "Ad example": Product ads grid ("Ads" heading, 8 tiles, prices $29.99–$69.99) on a search results page layout, not a Copilot response | "Ad example." (help-page image) | page ms.date 2026-06-18, updated 2026-07-27 | 3 | `raw/c-microsoft-merchant-center-overview-primary-2026-09-23-img-2026-09-23.md` |

Caveat: mock-ups drawn by the vendor; prices and advertisers are illustrative and carry no market figure.

## Image reads, IMG-1a, 2026-09-23
| Figure / text as shown | Chart or image | Date | Tier | Img raw |
|---|---|---|---|---|
| Segment tops, $bn, measured-by-us (read off axis): 2026 search-adjacent ~26, conversational ~30.5, total 32.03; 2030 ~40, ~63, 68.25 | "AI Ad Spending Will More Than Double by 2030" (EMARKETER 366969) | chart "May 2026" | 4 | `raw/e-market-size-emarketer-aiads-primary-2026-09-23-img-2026-09-23.md` |
| 2027–2029 totals redacted "$--.--"; intermediate tops ~43, ~51.5, ~59.5 (read off axis) | same | same | 4 | same |
| Amazon 24.2% of US search ad revenues 2026 (not in page text); Google 48.5% | "Google's Share of Search Advertising Will Fall Below 50%…" (365186) | chart "March 2026" | 4 | `raw/e-market-size-emarketer-searchad-primary-2026-09-23-img-2026-09-23.md` |
| Sponsored follow-up unit: "How can I use Indeed to enhance my job search?" labelled "SPONSORED", first of six "Related" rows | second page image (no caption) | page undated (2024-11 per substitute) | 3 | `raw/b-perplexity-ads-launch-primary-2026-09-23-img-2026-09-23.md` |
| "FIG. 01" is an illustration: no ad unit, no text | FIG. 01 | same | 3 | same |
| Ad-impression-by-session-position chart absent: image under that alt is a product demo table | alt "Where ChatGPT ad impressions land in a session" | page 2026-07-29 | 4 | `raw/a-similarweb-gen-ai-stats-primary-2026-09-23-img-2026-09-23.md` |

Caveat: ~ values are axis readings of a redacted chart, not published figures; the Perplexity unit is the vendor's own example.

## Image reads, IMG-1c, 2026-09-23
| Figure / text as shown | Chart or image | Date | Tier | Img raw |
|---|---|---|---|---|
| US 4,982 unique advertisers, 60.1% share of total; top: Booking.com 8.7%, Almedia USA, Inc. 8.1%, BestMoney 6.1% | "Distinct advertisers and competitive saturation by market" (dashboard cards) | week of 2026-07-13 to 07-20 (alt and page text; none inside image) | 5 | `raw/f-adthena-S2-eu-paid-agentic-2026-09-23-img-2026-09-23.md` |
| UK 1,342 unique advertisers, 16.2%; top: giffgaff 14.0%, Vodafone 11.3%, Booking.com 9.0% | same | same | 5 | same |
| AU 912 unique advertisers, 11%; top: Booking.com 13.4%, Almedia USA, Inc. 12.4%, Finder AU 10.9% | same | same | 5 | same |
| All-markets leaderboard ranks 1–5: Booking.com 13.81% (AU, Other, UK, US); Almedia USA, Inc. 12.76% (same four); efaq.com 4.55% (same four); Expert Market 4.38% (AU, UK, US); giffgaff 4.28% (UK) — image cut after rank 5 | "Top ChatGPT advertisers by Visibility %, week of July 13" (dashboard table) | same | 5 | same |
| Booking.com visibility by market: Other 32.38%, AU 13.41%, UK 9.00%, US 8.72% — "Other" figure appears nowhere else | "Brand look-up tool" (dashboard card) | same | 5 | same |
| Rest-of-world 1,055 (12.7%) and the 7,378 headline are absent from all three images; they rest on the relay row above (`b-ppcland-adthena-7378-advertisers`) | — | — | 5 | same |

Caveat: dashboard screenshots of a vendor index promoting the vendor's paid product; "Visibility %" denominator (monitored prompts) and panel unpublished; every figure in the images matches the PPC Land relay where both carry it, with two-decimal vs one-decimal rounding on Booking.com (8.72% / 8.7%, 13.41% / 13.4%).

## ChatGPT Ads buying mechanics, GAP-B — added 2026-09-24
Orphan-audit lane B. Raw prefix `raw/`, suffix `-2026-09-23.md`. OpenAI help pages undated, pulled 2026-09-23; label company-stated, tier 3 unless shown.

| Fact | Figure | Raw |
|---|---|---|
| Stage | beta; "focused pilot from February through April" | `b-openai-help-ads-faq` |
| Benchmarks | "does not yet have performance benchmarks across advertisers" | same |
| Billing | postpay; card charged at assigned threshold, e.g. "$25" | `b-openai-help-billing-payment` |
| Conversion objective | oCPC or oCPM; "Ads are not billed per conversion" | same |
| Daily budget | 7-day average; max 2× per day, 7× per week | `b-openai-help-daily-budgets` |
| Total-budget pacing | to end date, max 365 days; default 60 days | `b-openai-help-budget-pacing` |
| Default bid | "Maximize results"; no CPA, CPC or ROAS guarantee | `b-openai-help-maximize-results` |
| Who may open accounts | businesses only; agencies cannot create client accounts, invited after | `b-openai-help-account-setup` |
| Account caps | 10 ad accounts per login; verification via Persona, "rolling queue" | same |
| Object caps | 5,000 campaigns, 5,000 ad groups, 5,000 ads per account | `b-openai-help-launch-campaigns` |
| Ad unit spec | title ≤50 chars, copy ≤100; square image ≤1200×1200 | same |
| Targeting inputs | objective, country, ad-group "context hints"; no keywords named | same; `b-openai-help-quickstart` |
| Reporting latency | clicks, CTR ~15 min; spend delayed 7–8 hours | `b-openai-help-quickstart` |
| Product feeds | "among the strongest-performing ads", no figure | `b-openai-help-product-feed-campaigns` |
| Feed vs organic | feed products "will not appear in organic ChatGPT conversations" | same |

## ChatGPT Ads and Gemini timeline, GAP-B — added 2026-09-24
| Date | Event | Label, tier | Raw |
|---|---|---|---|
| 2025-12-08 | Adweek: Google told ≥2 clients Gemini ads target 2026 | analyst-derived, 5 | `b-ppcland-gemini-ads-denial`, `b-mediaincanada-gemini-ads-denial` |
| 2025-12-08 | Google VP: "no ads in the Gemini app… no current plans" | company-stated, 5 | same |
| 2026-03-02 | Criteo first ad-tech partner in US pilot | company-stated, 3 | `b-criteo-openai-pilot-march` |
| 2026-03-27 | pilot extended past April; IO commitments requested; Canada, NZ, Australia next | analyst-derived, 5 | `b-emarketer-openai-ads-100m` |
| 2026-04-21; 04-23 | OAI-AdsBot documented; ads shown to logged-out users | analyst-derived, 5 | `b-ppcland-criteo-1000-brands` |
| 2026-04-17/18 | Criteo buyers report CPM "$35-$25" | analyst-derived, 5 | same |
| 2026-06-06 | UK live, first European market | analyst-derived, 5 | `b-trendingtopics-chatgpt-ads-eu-privacy` |
| 2026-08-05 | email: feed carousel test; oCPC beta for feeds; Brazil, Mexico "coming week" | analyst-derived, 5 | `b-seroundtable-chatgpt-ads-updates` |
| 2026-08-06 | carousel: one retailer per unit; platform picks single vs carousel | analyst-derived, 5 | `b-digiday-openai-carousels` |
| 2026-08-11 | OpenAI update: live in Mexico, Brazil, Japan, South Korea | analyst-derived, 5 | `b-trendingtopics-chatgpt-ads-eu-privacy` |
| 2026-08-24 | 31 EEA+CH countries; Plus, Pro, Enterprise, Business, Education ad-free | analyst-derived, 5 | `b-euperspectives-chatgpt-ads-eu` |
| end 2026-08 | WPP Media NL tests; NL "approximately 4 million weekly active users" | company-stated, 3 | `b-wppmedia-netherlands-chatgpt-ads` |
| 2026-08-31 | self-serve rollout India, Europe, Middle East, North Africa | company-stated, 5 | `b-cnbc-openai-ads-1bn` |

UK row answers the `unknown` UK cell in "EU depth, P16-c3" at tier 5; `b-euperspectives-chatgpt-ads-eu` also lists the UK among eight pre-EU markets.

## EU and UK rules on ChatGPT Ads, GAP-B — added 2026-09-24
| Fact | Figure | Date | Label, tier | Raw |
|---|---|---|---|---|
| EEA launch targeting | topic, approximate location, device, time, language; no past chats | 2026-08-17 | analyst-derived, 5 | `b-trendingtopics-chatgpt-ads-eu-privacy` |
| Legal basis | contextual: legitimate interest; personalised: opt-in consent | same | same | same |
| Exclusions | health, mental health, politics; temporary chats, Atlas, minors | same | same | same |
| Ad-free free tier | offered with lower limits; EDPB 08/2024 "consent or pay" open | same | same | same |
| Supervisors | OpenAI Ireland controller, Irish DPC; Coimisiún na Meán is DSC | undated page | filed, 2; 5 | `b-eu-cnam-dsa-2026-09-22.md`; same |
| UK ASA/CAP | existing Codes apply to AI ads; "closely monitoring"; no assistant rule | 2025-02-07 | company-stated, 3 | `b-asa-cap-ai-monitoring` |

## Vendor and company performance claims, GAP-B — added 2026-09-24
| Claim | Figure | Window, n | Label, tier | Raw |
|---|---|---|---|---|
| Criteo, LLM-referred conversion vs other referral | "approximately one and half times" | Feb 2026, 500 US retailers | vendor-reported, 3 | `b-criteo-openai-pilot-march` |
| Criteo, AI-referred conversion vs traditional search | "close to two times"; CTR ~3× | 2026-05-05; three categories, n unstated | vendor-reported, 5 | `b-ppcland-criteo-1000-brands` |
| Criteo, CTR vs comparable formats; new customers | "two to three times"; ">80%" | June 2026; n unstated | vendor-reported, 3 | `b-criteo-openai-update-june` |
| OpenAI, ad quality | "Fewer than 7%" rated "low relevance"; "no impact" on trust | to 2026-03-30; n unstated | company-stated, 5 | `b-campaign-openai-ads-100m` |
| Chatbot CTR vs Google search benchmark | "as low as 0.91%" vs "6.4%" | Adweek relay, 2026-03-27 | analyst-derived, 5 | `b-emarketer-openai-ads-100m` |
| OpenAI research, relayed by WPP | "20% of conversations… direct commercial intent" | undated | company-stated relay, 3 | `b-wppmedia-netherlands-chatgpt-ads` |
| SE Ranking ad tracker | one sponsored card per answer; bundled, "no separate contract" | 2026-08-27 | vendor-reported, 5 | `b-seranking-chatgpt-ads-tracker` |

**Caveats, GAP-B.** Help pages are undated and describe a beta; limits may change. Criteo figures are the vendor's own clients, no control; May and June n `unknown — checked criteo.com, ppc.land 2026-09-24`. Criteo 1.5× compares referral channels, May 2× compares with search: different baselines, not a trend. EEA targeting rests on a trade relay of an OpenAI email, not the policy text. WPP's 20% relays OpenAI research not pulled. Gemini denial is 2025-12; Alphabet Q2 2026 "no ads" row in Pass 12 stands beside it. Sensor Tower 2026-09-01 and Adthena June Data Pulse primaries still unlocated (`b-sensortower-chatgpt-ads-rising-density-repull2`, `b-adthena-data-pulse-repull2`). File further over budget; overrun is this append.

# AI-assistant ads — who sells, at what price, to whom, with what result

| | |
|---|---|
| File date | 2026-09-23 |
| Oldest pull depended on | 2026-09-22 — `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md`, via `markets/paid-placement.md`; oldest source content 2023-09, `raw/b-microsoft-ads-snap-my-ai-partnership-2026-09-23.md` |
| Lane | B (paid placement); E for H20 |
| Hypotheses touched | H17, H18, H19, H20 (`method/hypotheses.md`, additions 2026-09-23) |
| Compiled file behind every E-row | `markets/paid-placement.md`, "Pass 12 addition, 2026-09-23" |
| Claims at tier 3 or better | 3 of 5 |

## Question

> Which AI engines sell ads today, in what formats, at what disclosed price, to how many advertisers, for how much revenue, with what measured result, sold through whom, under which rules?

## Answer

Four engines sell ads inside AI answers per their own tier-3 pages as of 2026-09-23: ChatGPT, Google (AI Overviews, AI Mode), Microsoft Copilot, Amazon Rufus / Alexa for Shopping; no ad product was found for the Gemini app, Claude, Meta AI, Duck.ai or Brave Leo, and Perplexity is winding its programme down. Only OpenAI discloses revenue and an advertiser count ("tens of thousands"); third-party ChatGPT advertiser counts run 820 to 7,378 on different panels, and no engine publishes a unit price. No advertiser result with a control exists; the metrics are visibility (ad presence) and traffic (CTR), never sales.

## Answer table — engine rows

| Engine | Inventory live | Format, label | Disclosed price | Advertisers | Revenue | Sold through |
|---|---|---|---|---|---|---|
| ChatGPT | yes, 40+ countries (E1) | below-answer unit "labeled as sponsored"; carousel; Sponsored Agents alpha (E5) | CPC bid "$3–$5"; min spend 25 USD/day; launch $60 CPM (E3, E4) | "tens of thousands" (E1) vs 820–7,378 panels (E6, E7) | $1B run rate; ~$83M/month (E1, E2) | self-serve, agencies, Criteo, Amazon DSP (E9) |
| Google AI Overviews | yes; within-AIO 12 countries (E10) | text, Shopping ads; label `u —` Google Ads Help | auction, no unit price (E10) | `u —` Alphabet Q1, Q2 transcripts | not broken out (E11) | existing Search, Shopping, PMax campaigns (E10) |
| Google AI Mode | yes, testing (E11) | Direct Offers; Highlighted Answers, "clearly marked sponsored links" (E11) | `u —` Alphabet Q1, Q2 transcripts | named pilots Gap, L'Oréal, Chewy, IHG (E11) | not broken out (E11) | existing campaigns (E11) |
| Gemini app | no — "focus right now is on AI Mode" (E11) | n/a | n/a | n/a | n/a | n/a |
| Microsoft Copilot | yes, EN/FR/DE markets, 2025 (E13) | Showroom ads, Dynamic filters; label `u —` about.ads.microsoft.com | auction, no unit price (E13) | `u —` FY26 Q4 release | not broken out (E13) | Microsoft Advertising accounts (E13) |
| Amazon Rufus / Alexa | yes, US, GA 2026-03-25 (E14) | Sponsored Products / Brands prompts; label `u —` advertising.amazon.com | "as part of your CPC bidding" (E14) | `u —` Q1 remarks, Q2 release | not broken out (E14) | existing Sponsored Products / Brands campaigns (E14) |
| Perplexity | winding down by end-2026 (E15) | sponsored follow-up questions (prior pull) | `u —` FT relays | "fewer than 0.5%" of applicants admitted (E15) | `u —` FT relays | direct only (E15) |
| Others | Snap My AI yes, stale (E16); Claude, Meta AI, Duck.ai, Leo none (E16) | Snap "Sponsored Links" | `u —` own pages | `u —` own pages | `u —` own pages | Microsoft Advertising into Snap (E16) |

Cells cite E-rows; `u —` = `unknown — checked <channel> 2026-09-23`. Measured result with n and window: one, ChatGPT — 1.30% CTR on 97,000+ impressions over ~2 weeks, "very few sign-ups" (E7). Rules: ChatGPT is a VLOSE with DSA ad-repository duty from January 2027; AIO excludes finance and healthcare ads (E10, E18).

## Evidence

| # | Evidence | Metric | Raw behind it | Label | Tier |
|---|---|---|---|---|---|
| E1 | "$1 billion in annualized revenue run rate"; "tens of thousands of advertisers"; "3x return on ad spend… over 28 days", one advertiser | sales | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` | company-stated | 3 |
| E2 | "$100 million annualized" in six weeks, "over 600 advertisers" (2026-03-26); "roughly $83 million a month" | sales | `raw/b-reuters-openai-ads-100m-`, `b-digiday-openai-ads-1bn-2026-09-23.md` | company-stated; analyst-derived | 5 |
| E3 | CPM, CPC, oCPC, oCPM; second-price auction; "$3–$5 USD per click"; min "25 USD", "15 EUR", "15 GBP" | none | `raw/b-openai-help-ads-basics-`, `b-openai-help-create-campaigns-2026-09-23.md` | company-stated | 3 |
| E4 | launch $60 CPM, $200K–$250K minimum; "$25" CPM by mid-April; minimum removed 2026-05-05 | none | `raw/b-digiday-openai-ads-fomo-cpm-`, `b-ppcland-adthena-europe-benchmark-2026-09-23.md` | analyst-derived | 5 |
| E5 | "clearly labeled as sponsored"; carousel ≈23% of US desktop ads, 2026-08-15 to 08-30 | visibility | `raw/b-openai-help-ads-in-chatgpt-`, `b-ppcland-sensortower-chatgpt-mix-2026-09-23.md` | vendor-reported | 5 |
| E6 | Sensor Tower ~300 (April) → 820+ (July) US mobile, ~1,200 US (August); Adthena 7,378, week 2026-07-13 to 07-20; Similarweb 5,171 since 2026-03-30 | visibility | `raw/b-biggo-sensortower-advertisers-820-`, `b-ppcland-sensortower-chatgpt-mix-`, `b-ppcland-adthena-7378-advertisers-`, `b-similarweb-chatgpt-ad-stats-2026-09-23.md` | vendor-reported | 5 |
| E7 | 1,159 advertisers, ads on 25.94% of 50,006 US prompts; own test 1,263 clicks | traffic | `raw/b-seranking-chatgpt-ads-study-2026-09-23.md` | vendor-reported | 5 |
| E8 | presence 0.8% of 500+ prompts (launch weeks); 4.47% of ~850K US (Mar–May); 24.7% (Jul); 26% US desktop (Jun); CTR 0.50% (Similarweb), 0.91% (one Adthena client) | visibility; traffic | `raw/b-adthena-ads-in-ai-search-`, `b-ppcland-adthena-europe-benchmark-`, `b-ppcland-similarweb-ai-ads-`, `b-campaign-chatgpt-ads-underwhelming-2026-09-23.md` | vendor-reported | 5 |
| E9 | "over 2,000 brands… through Criteo"; Omnicom "more than 30 of its clients"; Amazon DSP pilot | none | `raw/b-criteo-openai-update-june-`, `b-mediapost-openai-pilot-agencies-2026-09-23.md`, `b-amazon-ads-chatgpt-integration-2026-09-22.md` | vendor-reported | 5 |
| E10 | within-AIO "Australia… and US"; "200+ markets" above/below; finance, healthcare excluded | none | `raw/b-google-ads-help-aio-ads-2026-09-23.md` | company-stated | 3 |
| E11 | Direct Offers pilots; Highlighted Answers; Gemini app "not rushing"; Search & Other "over $63 billion" Q2, no AI line | sales | `raw/b-alphabet-q1-2026-earnings-transcript-`, `b-alphabet-q2-2026-earnings-transcript-2026-09-23.md` | company-stated | 3 |
| E12 | AI Mode ads 29.45% of 50,032 keywords vs 5.8%; AIO 0.052% (2025-11) → 0.12% (April 2026) | visibility | `raw/b-seranking-aimode-ads-study-`, `b-ppcland-adthena-7378-advertisers-`, `b-ppcland-adthena-29m-report-2026-09-23.md` | vendor-reported | 5 |
| E13 | Copilot ads "fully ramped" EN/FR/DE, "25% better" relevance, no n; search ad revenue ex-TAC +10% | sales | `raw/b-microsoft-ads-copilot-formats-blog-`, `b-microsoft-fy26-q4-release-2026-09-23.md` | company-stated | 3 |
| E14 | prompts GA US, CPC-billed; "nearly 20% of shoppers… continue the conversation", no n | visibility | `raw/b-amazon-sponsored-prompts-ga-2026-09-22.md`, `b-amazon-jassy-q1-2026-ads-2026-09-23.md` | company-stated | 3 |
| E15 | "winding down… by the end of 2026"; "fewer than 0.5% of brands who applied" admitted | none | `raw/b-campaign-perplexity-ads-end-`, `b-pymnts-perplexity-ads-end-2026-09-23.md` | company-stated | 5 |
| E16 | Microsoft sells "Sponsored Links in Snapchat's My AI"; Claude "will remain ad-free"; Meta Q2, Duck.ai, Leo pages name no AI ad unit | none | `raw/b-microsoft-ads-snap-my-ai-partnership-`, `b-snap-my-ai-sponsored-links-`, `b-meta-q2-2026-release-`, `b-duckduckgo-duckai-help-`, `b-brave-leo-page-2026-09-23.md`, `b-anthropic-ad-free-2026-09-22.md` | company-stated | 3 |
| E17 | Kontext "Rates starting from just $3 CPM"; Koah "Click-through rates average 7.5%"; Taboola no price | traffic | `raw/b-kontext-advertisers-page-`, `b-koah-launch-release-`, `b-taboola-genai-ad-platform-2026-09-23.md` | vendor-reported | 3 |
| E18 | VLOSE 2026-08-31, obligations "start applying in January 2027"; EEA ads not personalised at launch | none | `raw/b-techpolicy-chatgpt-dsa-designation-`, `b-openai-help-ads-in-chatgpt-2026-09-23.md` | analyst-derived | 5 |

Not reconciled: E1 vs E6, E7 (scopes: global, US month, 3-market week, prompt sample); E8's presence and CTR figures; E12 29.45% vs 5.8%; E8 vs E7 CTR; Amazon Q1 ad growth "22%" vs "24%" (`raw/b-amazon-jassy-q1-2026-ads-`, `b-ppcland-amazon-q1-2026-ads-2026-09-23.md`).

## Claims

| # | Claim | Evidence | Tier of weakest row | Grade | Load-bearing |
|---|---|---|---|---|---|
| C1 | Four engines sell ads inside AI answers; Gemini app and Claude do not | E1, E10, E11, E13, E14, E16 | 3 | n/a | yes |
| C2 | OpenAI is the only engine disclosing AI-ad revenue or an advertiser count | E1, E11, E13, E14 | 3 | n/a | yes |
| C3 | Panel counts of ChatGPT advertisers span 820–7,378 | E6, E7 | 5 | n/a | yes |
| C4 | No engine publishes a unit price; one network publishes a $3 CPM floor | E3, E10, E13, E14, E17 | 3 | n/a | yes |
| C5 | No advertiser result with a control exists; the best has n and window only | E1, E7, E8 | 5 | Fools gold | yes |

## Hypotheses scored — Pass 9 rule

| ID | Mark | Evidence |
|---|---|---|
| H17 | **killed** — no numeric count or AI-surface revenue from Google, Microsoft, Amazon; checked Alphabet Q1/Q2 transcripts, Google Ads Help, Microsoft FY26 Q4 release, Amazon Q1 remarks, Q2 release 2026-09-23 | E11, E13, E14 |
| H18 | **confirmed** — Kontext "$3 CPM" floor, own page, tier 3; network in third-party apps, not an engine | E17 |
| H19 | **confirmed** — Microsoft Advertising sells into Snap My AI, seller's own page, tier 3; 2026 status `u —` | E16 |
| H20 | **killed** — 15 screened, 0 with holdout, geo-split, switchback or control | Survivorship |

## Survivorship

| | |
|---|---|
| Candidates screened | 15: OpenAI ROAS; OpenAI partner new-customer share; SE Ranking; Adthena ×2; Criteo ×4; Kontext ×2; Koah; Microsoft; Amazon; Common Thread Collective (`raw/e-case-common-thread-collective-chatgpt-ads-2026-09-22.md`) |
| Cleared the evidence bar | 0 |
| Window; channels | 2026-02-09 to 2026-09-23; WebSearch, engine help centres, IR pages, vendor newsrooms, trade press |

## Unknowns

| Question | Channels checked | Date | Why not answerable |
|---|---|---|---|
| On-surface label wording, AIO, Copilot, Rufus | support.google.com, about.ads.microsoft.com, advertising.amazon.com | 2026-09-23 | pages name formats, not label text |
| AI-surface ad revenue, Google, Microsoft, Amazon | Alphabet, Microsoft, Amazon IR; sec.gov 10-Q (403) | 2026-09-23 | no segment below Search or search ads |
| Grok status after the 2025-08 plan (`raw/b-techcrunch-grok-ads-plan-2026-09-23.md`); Sensor Tower 2026-09-01 primary; Markey letter replies | x.ai/news, sensortower.com, markey.senate.gov (403), WebSearch | 2026-09-23 | not found or not retrievable |

## Caveats

- C1, C2, C4 rest on tier-3 engine pages: reliable on existence, biased on framing; C3, C5 on tier-5 vendors selling ad intelligence, none publishing panel n.
- H18 confirms on a "starting from" floor, not a schedule; H19 on a 2023 page with no 2026 status. Both sit outside P1 engines.
- The run rate (E1) is one month × 12, not booked revenue; EMARKETER forecasts under $1B for all chatbot ads in 2026 (`raw/b-emarketer-chatgpt-inventory-2026-09-23.md`). No metric crossing is relied on. Oldest pull cited 2026-09-22.
- Absences (Gemini app, Meta AI, Duck.ai, Leo) hold only for the channels named; Snap and Copilot-format sources predate one quarter, flagged stale. Tier 6 noise filed, not used: `raw/b-seroundtable-similarweb-ctr-`, `b-novadata-rufus-ads-free-`, `b-trendsvc-ai-ad-networks-`, `b-q1media-chatgpt-ads-results-2026-09-23.md`. This file carries evidence, not a verdict.

### R-BLOCKED-2, 2026-09-23

Advertiser-reported results from Reddit, pulled through the Arctic Shift archive (curl, no browser). All rows: engine ChatGPT (OpenAI Ads), label company-stated (self-report), tier 5 held — archive copy, coverage unverified, no permalink verified elsewhere. Raw: `raw/b-reddit-advertiser-reports-repull2-2026-09-23.md`. No Perplexity or Google AI Mode / AI Overviews advertiser metric found; AI Mode posts relay third-party figures only.

| # | Advertiser, as posted | Window | Figures verbatim | Class | Design |
|---|---|---|---|---|---|
| RB1 | US visa/passport expediting service, AOV ~$650 | Aug 28 – Sep 4 | $707 spend; CTR 0.75%; CPC $3.37; Orders: 0 | metric-moved | observational |
| RB1b | same, vs own Google campaign, identical page | six days | click→session 9.1% vs 29.8%; ~$555 vs ~$92 | metric-moved | observational, concurrent channel comparison |
| RB2 | premium DTC supplement brand, Spain | 4 September | 5,590 impressions; 160 clicks; €37.61; 0 conversions | metric-moved | observational |
| RB3 | marketing software (Launch10), three ad groups | 3 days; then 2 weeks | 228 impressions; then CTR 1.31%/2.16%/0.43%, conversions 4/6/0 | metric-moved | observational; own Google Search "8-10%+ CTR" |
| RB4 | unnamed, $25/day | about a week | CTR "around 0.5%" to "around 5%" after image swap | metric-moved | pre/post, no control |
| RB5 | SaaS with free tier, worldwide | 4 days | "73 signups, 0 of them became paying customers" | metric-moved | observational |
| RB6 | unnamed, broad topic | month to 2026-07-27 | "CPM of $47"; "likely shutting it down" | metric-moved | observational |
| RB7 | PPC audit offer, US targeting | couple of days | CPC "less than $6"; one conversion | metric-moved | observational |
| RB8 | SaaS signups | Sept 11 | Ads Manager 4 conversions vs API 18 | metric-moved | measurement discrepancy |
| RB9 | home services, Sydney | about 4 days | CTR "Around 0.8%" | metric-moved | observational |
| RB10 | unnamed | a few days | CTR "around 0.8%" | metric-moved | observational |
| RB11 | ZapDigits, agency-reporting software | unstated | ~$4,800; CTR ~2.9%; 87 paid; CAC ~$55 | metric, window unstated | observational |
| RB12 | six further advertisers | unstated | CPC $7-8; CTR 0.65%; 70.2% recorded; 50 vs 5-10 clicks; 2x budget | metric, window unstated | observational |
| RB13 | AU in-house, agency trial offer | 2026-05-19 | "$5k USD minimum outlay"; "$50 USD CPM" | price terms, question | n/a |
| RB14 | eight posters | 2026-06 to 2026-09 | 3 positive, 5 negative; one "~34,000 usd" spend, no outcome | claim-without-metric | action named, outcome unknown |
| RB15 | Nile employee, public Penn/Haverford dataset | Mar 8 – Apr 12 2026 | 3,602 placements; 91 pairs; "-0.3 percentage points" | third-party measurement | paired, ad vs no ad |

**Quality of evidence.** Metric moved, experimental: 0. Metric moved, observational: 10 advertiser reports (RB1–RB10). Metric stated, window unstated: 7 advertisers (RB11, RB12 ×6; RB13 is price terms, not a result). Action named, outcome unknown: 8 (RB14). Screened: 852 archive records, 499 naming an engine and an ad term, 38 read in full.

**Survivorship.** Most reports with a sales outcome are negative or zero (RB1, RB2, RB5; RB14 five of eight); RB11 is the one positive paid-conversion figure and names its own product. Posters self-select; nothing is audited.

**Hypotheses.** H20: no holdout, geo-split, switchback or pre/post-with-control case; RB1b is the nearest — concurrent same-page channel comparison, all seven bar items present on its own page, not a registered design. Mark stands **killed**, near-miss recorded. H17, H18, H19: not moved — Reddit carries no engine disclosure; price relays (RB13; "$1 million upfront", "$250K minimum" in comments) are hearsay, not rate cards.

**Caveats.** Archive copy; posts could be deleted or edited live. Several posters promote products or communities (RB3 Launch10, RB11 ZapDigits, RB15 Nile). Figures are platform-reported unless stated; RB2's figures were confirmed by OpenAI support per the poster's quote. Buyer size is unstated for every row; no row moves a segment cell. Channels not reached: comments outside r/PPC and r/marketing; nine title searches timed out (raw lists them).

## Tier revisions, P9-r, 2026-09-23

sec.gov Archives re-fetched 2026-09-23 (HTTP 200; 403 on 2026-09-22). Rows above are not edited; each row below sits beside its original.

| line | row | tier revised 2026-09-23 | raw |
|---|---|---|---|
| 51 | E13, "search ad revenue ex-TAC +10%" element | 3 → 2 (8-K Exhibit 99.1: "Search advertising revenue excluding traffic acquisition costs increased 10% (up 9% in constant currency)"; no Copilot advertising line) | `raw/b-sec-microsoft-8k-ex991-2026-07-29-2026-09-23.md`; annual +12% in `raw/b-sec-microsoft-10k-2026-07-29-2026-09-23.md` |
| 51 | E13, Copilot "fully ramped" / "25% better" element | unchanged 3 (blog) | — |

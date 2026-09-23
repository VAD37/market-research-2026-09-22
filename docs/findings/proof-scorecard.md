# Proof scorecard — what the published cases prove

| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every `raw/` file cited. Oldest source publication carried: 2026-02-25, `raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md`, via `markets/organic-recommendation.md` |
| Lane | E, with A and F feeding it |
| Hypotheses touched | H3, H6, H11, H14 (scored in `unknowns.md`) |
| Claims at tier 3 or better | 1 of 7 |

## Question

> Which published cases clear the seven-item evidence bar, at what grade, and what did the screen behind them cost?

## Answer

Visibility and traffic, with two sales crossings named below. **No Gold case exists as of 2026-09-22**: across approximately 980 candidates screened in Passes 3 and 4, zero disclose a holdout, geo-split or switchback. Seven cases carry a raw-file Silver grade, and under grading rule 1 six of them miss a bar item, leaving only E7 at Silver — both counts stand; every one is an observational pre/post with a within-site or within-company control, and two of the seven run negative or null.

## Evidence

**The bar, restated once.** A case qualifies only when it names all seven of: brand; engine(s); absolute date window; baseline; intervention; sample size or traffic volume; who measured and whether paid by the outcome (`method/plan.md` evidence bar + grading rule 1).

### Every Gold and Silver case — 0 Gold, 7 Silver as graded in raw; 1 under grading rule 1

| # | Case | Metric, direction | Engines named | Date window | Control | Who measured | Paid by outcome | Brand-side | Tier | Raw |
|---|---|---|---|---|---|---|---|---|---|---|
| E1 | Quattr / Men's Wearhouse | visibility, traffic — up: "75% more AI Mode visibility, 50% more top-3 ChatGPT citations… 46% more clicks on treated product pages" | Google AI Mode, ChatGPT | none absolute — "days 0-30/31-60" | yes — untreated pages 10,940 → 11,356, +3.8% | Quattr, on customer's GSC data | unknown | silent — checked menswearhouse.com | 5 | `raw/e-case-quattr-menswearhouse-2026-09-22.md` |
| E2 | Sitefire / Pointhound | traffic, visibility — up: "+300% more site visits from AI Search… Visibility Score 0 → 1.0%" | ChatGPT, Perplexity, Claude (crawler UAs) | yes, absolute — "February 23 to June 29, 2026" | yes — "new content vs. rest of site" | Pointhound GA4/CDN logs; Sitefire prompt set | unknown | not among the 59 checked | 5 | `raw/e-case-sitefire-pointhound-2026-09-22.md` |
| E3 | Sitefire / Jerry — **contested grade: Bronze (c10) / Silver (c13), both stand** | traffic, visibility — up: "+78% AI referral traffic… 112% vs. 72% treated-vs-untouched" | "GPT-5.4" named as a confound; "AI models" otherwise generic | yes — waves "between April and June 2026"; 3 months after vs 3 weeks before | yes — untouched comparable page set | Sitefire, vendor | unknown | silent — checked jerry.ai | 5 | `raw/e-case-c13-sitefire-jerry-2026-09-22.md`; `raw/e-case-c10-sitefire-jerry-2026-09-22.md` |
| E4 | Seer Interactive / anonymised "SaaS HR" client | traffic — up: "300% increase in AI traffic"; second client "54% increase in GPT-User bot hits" | "AI traffic" generic; GPT-User named | none absolute | yes — site-wide AI sessions "remained stagnant" | Seer, agency, own client work | unknown — checked seerinteractive.com | client anonymised — n/a | 5 | `raw/e-case-seer-interactive-content-recency-2026-09-22.md` |
| E5 | Gaurav Tiwari, GSC audit | traffic — **mixed/negative**: "22% CTR drop"; 14 of 18 AI-Overview queries down; opinion queries "up 8%" | Google AI Overviews | none absolute — "last month", "last quarter" | yes — 32 non-triggering queries against 18 triggering | the author alone, self-interested | not paid, not disinterested | self-authored — n/a | 5 | `raw/e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-2026-09-22.md` |
| E6 | NerdWallet 8-K | sales — **negative**: "Credit cards revenue of $26.5 million decreased 24% year-over-year", cause stated as organic-search headwinds from "AI overviews and LLMs" | "AI overviews", "LLMs" — generic | yes — Q4 2025 vs Q4 2024 | contrast lines in the same release: Insurance +13%, Loans +141% | the company, in a filing | n/a | self-filed | 2 | `raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md` |
| E7 | TW3 Partners / Citead, arXiv 2609.07559 | visibility (citation) — **null**: the 2023 GEO levers move citation on **none** of ten engine families | ten families, incl. three gpt-5.x arms | yes — July 2026 replication arm; paper 2026-09-07 | negative-control gates, 95% CIs, p-values | TW3 Partners (Citead), code and data published | n/a — academic | n/a | 4 | `raw/e-case-c11-arxiv-tw3-partners-geo-score-2026-09-22.md` |

E3's two grades conflict — **not reconciled**. E6 and E7 run against the category's own direction and are the two highest-tier rows in the table.

### Screened and cleared, per vertical

| Vertical | Screened | Cleared Bronze or better | Silver | Gold | Compiled file |
|---|---|---|---|---|---|
| Skincare and beauty | ~133 (c8); 0 screened as such in c1, c2, c3, c5, c11 | 2 Bronze — eMarketer index via BeautyMatter; 5W ranking via Glossy | **0** | 0 | `customers/skincare-beauty.md` |
| B2B SaaS | ~100 (c9) | 4 Bronze (c9) + 4 (c4, c13) + 2 (c2: Foundation/Bitly Bronze, Seer Silver; one aggregate not graded) | **1** — E4 | 0 | `customers/b2b-saas.md` |
| High-CPA regulated | 34 (cards 16, insurance 12, supplements 6) | cards 1, insurance 2, supplements **0** | **1, negative** — E6; E3 contested | 0 | `customers/high-cpa-regulated.md` |
| None named — the rest | ~150 Pass 3 titles re-graded + c1 64 + c2 8 pulled + 7 screened + c3 6 talks + c5 34 + c6 30 + c11 ~180 + c12 151 | 45 Bronze, 24 Fools gold (c13 tally) | 4 — E1, E2, E5, E7 | 0 | `markets/organic-recommendation.md` |

### Done-condition row — "Success stories"

| Bar | Vertical | Arm met | Status |
|---|---|---|---|
| One Silver per vertical, **or** documented absence with screened count | Skincare and beauty | documented-absence arm — 0 Silver at ~133 screened | met |
| | B2B SaaS | Silver arm — E4 | met |
| | High-CPA regulated | Silver arm — E6 (negative direction); E3 contested | met |
| | **Row status** | all three meet one arm; under grading rule 1, B2B SaaS and high-CPA via absence arm (~100, 34 screened) | **satisfied** |

## Claims

| # | Claim | Evidence | Tier of weakest row | Grade | Load-bearing |
|---|---|---|---|---|---|
| C1 | No Gold case exists as of 2026-09-22; zero of ~980 candidates screened in Passes 3 and 4 discloses a holdout, geo-split or switchback | E1–E7, survivorship below | 5 | Gold 0 | yes |
| C2 | Seven cases clear Silver; every one is observational treated-vs-untreated, not randomized | E1–E7 | 5 | Silver | yes |
| C3 | Two of the seven Silvers report a negative or null direction | E6, E7 | 4 | Silver | yes |
| C4 | Paid-by-outcome is disclosed on no graded vendor case — 0 yes / 0 no / 12 unknown at full-page re-grade | E1–E4, `raw/e-case-census-c4-2026-09-22.md` | 6 | n/a | yes |
| C5 | Brand-side corroboration is absent: of 59 brands checked on their own domains, 0 corroborate, 0 contradict, 59 silent | `raw/e-case-census-c7-2026-09-22.md` via `markets/organic-recommendation.md` | 3 | n/a | yes |
| C6 | The anchor vertical produced no Silver at all; the two Silvers inside a tracked vertical are one agency-authored and one negative filing | E4, E6, per-vertical table | 5 | Silver | yes |
| C7 | One case carries two grades from two clusters, Bronze and Silver, not reconciled | E3 | 5 | Bronze / Silver | no |

C2 and C6 cross visibility → sales only at E6, which is a filing's own revenue line attributed by management, not incremental (`method/glossary.md` crossing rule): graded Silver, never cited as lift.

## Survivorship

Published cases are winners. Stated once for this programme.

| | |
|---|---|
| Candidates screened, Passes 3 and 4 | **~980** — Pass 3 ~150 case titles (re-graded by c4 and c13, not re-screened) + Pass 4 c1 64, c2 8 pulled + 7 screened, c3 6 talks, c5 34, c6 30, c7 59 of ~166 (brand checks, not case candidates), c8 ~133, c9 ~100, c10 34, c11 ~180, c12 151 |
| Cleared Silver or better | **7** |
| Cleared Gold | **0** |
| Screen window | 2026-09-22 to 2026-09-22 (all pulls same day; source publications 2026-02-25 to 2026-09-17) |
| Channels searched | EDGAR full-text and filer pages, vendor customer and case pages, agency blogs, 11 conference agendas, practitioner blogs and HN, trade press (PPC Land, Glossy, BeautyMatter, OMR, t3n, horizont, onlinemarketing.de), arXiv, G2 / Capterra / OMR reviews, brand-owned domains |

The counts do not sum cleanly and are not forced to. `plan-review-1-2026-09-22.md` §3 records three incompatible operationalisations of one bar across c1, c2, c3, c4 and c6 — c1 graded metric-less testimonials Fools gold on intake, c2 excluded the same items as no-claim, c3 counted 26 unopened titles as screened, c6 scored binary cleared / not-cleared with no grade at all. `raw/e-case-census-c13-2026-09-22.md`'s master table is the one internally consistent tally: 47 opened this pull + 31 already opened, 25 screened — not opened, 2 not reachable, 34 screened — no claim, 45 Bronze, 24 Fools gold, 3 Silver, 0 Gold. Full-page re-grading moved 12 cases up and 0 down — the teaser reads undercounted, and the no-Gold result survives that correction.

## Unknowns

| Question | Channels checked | Date | Why not answerable here |
|---|---|---|---|
| Whether any of the ~107 unchecked named brands corroborates a vendor claim on its own domain | brand newsrooms, IR and case pages — 59 of ~166 checked, cap reached | 2026-09-22 | cluster cap, not exhaustion |
| Whether the 25 unopened and 2 unreachable Pass 3 titles hold a Silver | airops.com, otterly.ai, feedonomics.com, criteo.com, pacvue.com, kargo.com, searchable.com, searchengineland.com | 2026-09-22 | pages not reached inside the pull's budget; a gated stub in one case |
| Whether any negative case exists in the three tracked verticals | reddit.com (403), html.duckduckgo.com (rate-limited), g2.com (DataDome CAPTCHA), arxiv.org/abs/2609.06811 | 2026-09-22 | the three richest negative channels were blocked this session |
| Paid-by-outcome for any case | every graded case page | 2026-09-22 | no vendor or agency states its fee structure on any case page |

## Caveats

- C1, C2 and C6 are load-bearing and sit at tier 5, C4 at tier 6: every case above Bronze except E6 and E7 is vendor- or agency-reported about its own work, with no independent replication. `trust-rubric.md`'s "vendor measuring the thing it sells" flag applies to all three Silver vendor cases.
- Claims below tier 3: C4 (tier 6), C1, C2, C6, C7 (tier 5) and C3 (tier 4). Only C5 reaches tier 3.
- Metric crossings: E6 crosses a traffic-headwind statement to a revenue line inside one filing — Silver, correlational. E1, E2, E3 stop at traffic; E4, E5 at traffic; E7 at citation. None is cited as sales proof.
- Conflicts left unreconciled: E3's Bronze/Silver split; E5's three CTR figures (15–30%, 20–40%, 22%) for what reads as one phenomenon, kept side by side.
- Absence is only as strong as the channels listed. Reddit, G2/Capterra and sec.gov were blocked this session, not exhausted.
- The oldest pull cited is 2026-09-22; pulls older than one quarter at citation are re-checked and the re-check dated (`method/plan.md` staleness rule). No cited pull is stale. This file carries evidence, not a verdict.
- Amended 2026-09-23 per `findings/review-1-2026-09-23.md` §9; both readings stand where the review and the original disagree.

### Pass 4 re-run, 2026-09-23

Task P4-r. Census `raw/e-case-census-r1-2026-09-23.md`; 29 new raw files `raw/e-case-*-2026-09-23.md`. Grades per grading rule 1 (2026-09-23 reading) and the evidence-quality append; both grades stated.

**Answer, this pass.** Still no Gold: 0 holdout, geo-split or switchback in ~1,640 new items screened. Four new Silver (raw), one under grading rule 1 — all four experimental, all outside the three verticals. First brand-side corroboration: Chime's own page states AirOps' result.

#### Claims restated — 2026-09-22 beside 2026-09-23

| # | 2026-09-22 | 2026-09-23, beside it |
|---|---|---|
| C1 | No Gold; ~980 screened | No Gold; ~1,640 more screened, detail below |
| C2 | 7 Silver raw, 1 rule1; all observational | +4 Silver raw (X1, X2, X5, X6); +1 rule1 (X1) |
| C3 | 2 of 7 Silvers negative or null | +4 negative or null graded; +1 ungraded replication |
| C4 | Paid-by-outcome 0 yes / 0 no / 12 unknown | Unchanged; 0 new cases state fees |
| C5 | 0 of 59 brands corroborate | 1 of 109 corroborates (Chime); cumulative 1 of 168 |
| C6 | Anchor vertical: 0 Silver | Unchanged: 0 new Silver in any vertical |

Screened this pass: EDGAR 1,098 documents (30 queries) plus 34 tickers per-CIK; brand pages 109; Pass 3 titles 19 line items plus 16 client pages; vendor sitemap-new 44 URLs; agency and talks ~110 search entries; experiments ~25; Reddit 221 comments (Arctic Shift archive).

#### Every new case at Silver or better — 0 Gold, 4 Silver raw, 1 Silver rule1

| # | Case | Vertical | Metric moved | Window | Design | Raw / rule1 | Brand side | Raw |
|---|---|---|---|---|---|---|---|---|
| X1 | OtterlyAI Reddit test | none — vendor's test communities | AI citations 48 control vs 426 treated | 2026-04-11 to 2026-06-10 | experimental: two arms, one unit each, unmatched | Silver / Silver | n/a — own | `raw/e-case-otterly-reddit-experiment-2026-09-23.md` |
| X2 | OtterlyAI HTML vs Markdown | none | .md citations 0; bot visits 0% vs 2.8–4.6% | 14 days, dates not printed | experimental: paired pages | Silver / Bronze — item 3 | n/a — own | `raw/e-case-otterly-html-vs-markdown-experiment-2026-09-23.md` |
| X5 | Jonathan Mall, "Brand A" | none — expert services | ChatGPT citations +171 / −32; mentions flat | July 2 to 9, year absent | experimental: pre/post, untreated pages, noise floor | Silver / Bronze — items 1, 3 | n/a — anonymised | `raw/e-case-jonathanmall-geo-experiment-2026-09-23.md` |
| X6 | Boily, two dental clinics | none — healthcare | mention rate 11→27% vs 11→10% | two weeks, slug 2026-06 | experimental: pre/post, one untreated clinic | Silver / Bronze — item 3 | n/a — anonymised | `raw/e-case-boily-dental-geo-comparison-2026-09-23.md` |

X2 and X5's mention result run null. X1's vendor labels its own design "observational study"; X6's vendor writes "not a controlled A/B".

#### Quality of evidence, this pass

| Category | Cases | Inside the three verticals |
|---|---|---|
| Metric moved, experimental | 4 (X1, X2, X5, X6) | 0 |
| Metric moved, observational | 28 | 16 |
| Action named, outcome unknown | 13 | 6 |

#### Per vertical, this pass — grade_rule1

| Vertical | Screened | Bronze+ | Fools gold | Silver | Gold | Negative / null |
|---|---|---|---|---|---|---|
| Skincare and beauty | 22 | 3 — Nuvadermis, OptimizeGEO haircare, "Lumara" | 1 — Fresha | 0 | 0 | 0 |
| B2B SaaS | 41 | 6 — incl. Lago, PagePilot, HubSpot blog loss | 3 — incl. HubSpot cohort | 0 | 0 | 1 — HubSpot −5M visits |
| High-CPA regulated | 21 | 3 — Venn, Chime (both borderline), supplement brand | 0 | 0 | 0 | 0 |

Supplements had 0 cleared on 2026-09-22; the Fire&Spark supplement case (V8) is the first Bronze. Chime (B1) is the only case with a brand-side page stating the vendor's result: "tripled our AI citations" (`raw/e-case-chime-careers-airops-2026-09-23.md`).

#### Done row "Success stories" — restated

| Vertical | 2026-09-22 | 2026-09-23, rule1 reading |
|---|---|---|
| Skincare and beauty | absence arm, ~133 screened | absence arm, ~155 screened |
| B2B SaaS | Silver E4 (raw); absence under rule1 | absence arm under rule1, ~141 screened |
| High-CPA regulated | Silver E6 (raw); absence under rule1 | absence arm under rule1, ~55 screened |
| Row | satisfied | satisfied — absence arm in all three |

#### Hypotheses — marks beside 2026-09-22

| ID | 2026-09-22 | 2026-09-23 | Deciding evidence |
|---|---|---|---|
| H3 | killed | killed — unchanged | 0 Gold in ~1,640 more; best design X1, one unit per arm |
| H6 | unresolved — checked | confirmed narrowly (rule1) / unresolved in verticals, both stand | X1: vendor-owned property, dated action, P1 engines, Silver rule1 |
| H11 | not produced | confirmed — tier 2–3, action named | Coty 10-K; LendingTree 8-K; HubSpot op-ed; Chime page |

H11 rows: skincare — Coty 10-K 2026-08-20 "deploying improvements… to drive generative engine optimization" (tier 2); high-CPA — LendingTree 8-K 2026-07-29 ChatGPT app (tier 2), Chime careers page (tier 3, borderline); B2B SaaS — HubSpot CMO op-ed, Fortune 2026-09-22 (tier 3). Outcome unknown for Coty and LendingTree. Sources: `raw/e-case-edgar-fulltext-results-2026-09-23.md`, `raw/e-case-fortune-hubspot-blog-traffic-loss-2026-09-23.md`.

#### Caveats, this append

- This file was at 100 lines, its budget; this append adds 78 lines. Overrun recorded here, not trimmed from the original.
- All four new Silvers are vendor- or practitioner-run on their own properties; trust-rubric "vendor measuring the thing it sells" applies to X1, X2, X6. None is replicated.
- The evidence-quality table counts pre/post with control as experimental. By that reading E1–E4 above also qualify; C2's "observational" label stands beside it.
- Vertical tags "borderline": Venn (business cards), Chime (neobank), Fresha (beauty booking). Readings without them: high-CPA 1 Bronze, skincare 0 Fools gold.
- Chime's page is a 2026-02-23 Wayback copy of a 2025-11-24 post; the live page blocks fetch.
- WebSearch session cap (200 calls) was reached; later searches used DuckDuckGo html. Reddit came from an archive, comments only; G2, Capterra and live Reddit deferred to the extension holder.
- Sitemap lastmod is not a publication date; "new since 2026-09-01" means new to this programme.
- Paywalled or blocked primaries (grro.io, aicited.org, one SEL article) are listed in the census for REPULL-1; none is graded.

## Evidence-quality three-count, 2026-09-23

Task COMPILE-1 (Pass 16), per `method/plan.md` "Evidence bar — evidence-quality reporting, 2026-09-23". Appended only. Classes: (a) metric moved, experimental design — holdout, geo-split, switchback, pre/post with control; (b) metric moved, observational; (c) action named, outcome unknown. Itemised over every graded case above: E1–E7 (2026-09-22) and the P4-r register `raw/e-case-census-r1-2026-09-23.md` (raw abbreviated to `raw/e-case-<name>-2026-09-23.md`). Two readings of pre/post-with-control stand side by side: R1 reads it as (a) per plan.md L146; R2 reads vendor pre/post as (b) per C2 above.

| Case | Vertical | Class | grade_raw | grade_rule1 | Raw path |
|---|---|---|---|---|---|
| E1 Quattr / Men's Wearhouse | none | a (R1) / b (R2) | Silver | Bronze | `raw/e-case-quattr-menswearhouse-2026-09-22.md` |
| E2 Sitefire / Pointhound | none | a / b | Silver | Bronze | `raw/e-case-sitefire-pointhound-2026-09-22.md` |
| E3 Sitefire / Jerry | high-CPA (c10); none (c13) | a / b | Bronze / Silver | Bronze | `raw/e-case-c13-sitefire-jerry-2026-09-22.md`; `-c10-` |
| E4 Seer / "SaaS HR" client | B2B SaaS | a / b | Silver | Bronze | `raw/e-case-seer-interactive-content-recency-2026-09-22.md` |
| E5 Tiwari, GSC audit — negative | none | a / b | Silver | Bronze | `raw/e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-2026-09-22.md` |
| E6 NerdWallet 8-K — negative | high-CPA | b | Silver | Bronze | `raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md` |
| E7 TW3 Partners / Citead — null | none | a (replication, not a brand case) | Silver | Silver | `raw/e-case-c11-arxiv-tw3-partners-geo-score-2026-09-22.md` |
| T7 AirOps / Venn | high-CPA, borderline | b | Bronze | Bronze | `airops-venn` |
| T10 Otterly / Chatarmin | B2B SaaS | b | Fools gold | Fools gold | `otterly-chatarmin` |
| T11 Otterly / NOLA Marketing | none | b | Bronze | Bronze | `otterly-nola-spoc` |
| T12 Otterly / SORN.AI | B2B SaaS | b | Bronze | Bronze | `otterly-sornai-pagepilot` |
| T13 Otterly / What IF Web | none | b | Bronze | Bronze | `otterly-whatifweb` |
| T15 Searchable / Blackbird | none | b | Bronze | Bronze | `titles-opened-multi` |
| T16 Orange142 / Pigeon Forge | none | b | Bronze | Bronze | `titles-opened-multi` |
| T17 Feedonomics / Euro Car Parts; Fruugo — 2 | none | c ×2 | — | — | `titles-opened-multi` |
| B1 Chime — AirOps, brand-side | high-CPA, borderline | b | Bronze | Bronze | `chime-careers-airops` |
| B2 Fresha, own post | skincare, borderline | b | Fools gold | Fools gold | `fresha-ai-bookings` |
| B3 Proper Propaganda — Scrunch | none | b | Bronze | Bronze | `brandside-found-multi` |
| V1 AthenaHQ / Nuvadermis | skincare | b | Bronze | Bronze | `athenahq-new-multi` |
| V2 AthenaHQ / AutoRFP.ai | B2B SaaS | b | Fools gold | Fools gold | `athenahq-new-multi` |
| V3 AthenaHQ / Lago | B2B SaaS | b | Bronze | Bronze | `athenahq-new-multi` |
| V4 AthenaHQ / Buried | none | b | Fools gold | Fools gold | `athenahq-new-multi` |
| V5 Profound / Kiteworks | B2B SaaS | b | Bronze | Bronze | `profound-new-multi` |
| V6 Profound / WHOOP | none | b | Bronze | Bronze | `profound-new-multi` |
| V7 Profound / Apartment List | none | b | Bronze | Bronze | `profound-new-multi` |
| V8 Fire&Spark / supplement brand | high-CPA | b | Bronze | Bronze | `fireandspark-supplement-citations` |
| V9 Birdeye / Arrow Senior Living | none | b | Bronze | Bronze | `birdeye-arrow-senior-living` |
| A1 OptimizeGEO / haircare brand | skincare | b | Bronze | Bronze | `ddg-vendor-multi` |
| A2 BrandCited / "Lumara" | skincare | b | Bronze | Bronze | `ddg-vendor-multi` |
| A3 Over The Top SEO / "ProjectFlow" | B2B SaaS | b | Bronze | Bronze | `ddg-vendor-multi` |
| A4 Go Fish Digital / unnamed | unknown | b | Bronze / Fools gold | Bronze / Fools gold | `ddg-vendor-multi` |
| A8 HubSpot AEO cohort | B2B SaaS | b | Fools gold | Fools gold | `hubspot-aeo-data-cohort` |
| A9 HubSpot CMO op-ed — negative | B2B SaaS | b | Bronze | Bronze | `fortune-hubspot-blog-traffic-loss` |
| X1 Otterly Reddit test | none | a | Silver | Silver | `otterly-reddit-experiment` |
| X2 Otterly HTML vs Markdown — null | none | a | Silver | Bronze | `otterly-html-vs-markdown-experiment` |
| X3 Otterly llms.txt — null | none | b | Bronze | Bronze | `otterly-llms-txt-experiment` |
| X4 Otterly FAQ on homepage | none | b | Bronze | Bronze | `otterly-geo-guide-experiment-claims` |
| X5 Jonathan Mall / "Brand A" | none | a | Silver | Bronze | `jonathanmall-geo-experiment` |
| X6 Boily / two dental clinics | none | a | Silver | Bronze | `boily-dental-geo-comparison` |
| E1 Yext 8-K, own brand | B2B SaaS | b | Bronze | Bronze | `edgar-fulltext-results` |
| E3 TechTarget 8-K; E7 Freshworks 10-K; E8 HubSpot DEF 14A — 3 | B2B SaaS | c ×3 | — | — | `edgar-fulltext-results` |
| E4 Coty 10-K | skincare | c | — | — | `edgar-fulltext-results` |
| E5 LendingTree 8-K; E6 Chime DRS/A — 2 | high-CPA | c ×2 | — | — | `edgar-fulltext-results` |
| E9 JOINT Corp 8-K; E10 Klarna, Etsy, Rent the Runway, ZipRecruiter — 5 | none | c ×5 | — | — | `edgar-fulltext-results` |

| Count | (a) experimental | (b) observational | (c) action named, outcome unknown | Total |
|---|---|---|---|---|
| P4-r own tally, append above L136–138 | 4 | 28 | 13 | 45 |
| COMPILE-1 recount, P4-r register only | 4 | 28 | 13 | 45 — agrees |
| COMPILE-1 cumulative, E1–E7 added, R1 | 10 | 29 | 13 | 52 |
| COMPILE-1 cumulative, E1–E7 added, R2 | 5 | 34 | 13 | 52 |
| Skincare and beauty (R1 / R2) | 0 / 0 | 4 / 4 | 1 / 1 | 5 |
| B2B SaaS (R1 / R2) | 1 / 0 | 9 / 10 | 3 / 3 | 13 |
| High-CPA regulated (R1 / R2) | 1 / 0 | 4 / 5 | 2 / 2 | 7 |
| None named or borderline-excluded (R1 / R2) | 8 / 5 | 12 / 15 | 7 / 7 | 27 |

Divergence: P4-r and this recount agree on the register; the cumulative rows differ only by the R1/R2 reading of E1–E5 (pre/post with control) and E7 (controlled replication). E3 sits in high-CPA per c10's tag. The 45 Bronze and 24 Fools gold of `raw/e-case-census-c13-2026-09-22.md` carry no design field and are not classed here.

Caveats, this append: (a) counts vendor- or practitioner-run designs with one unit per arm (X1, X6) and unmatched arms; no (a) case is randomised or replicated; classes describe design, never grade; two rows (T17, E10) group cases as the census does; file overrun of the 100-line budget recorded, not trimmed.

## Negative tail — filings and exhibits, 2026-09-23

Task COMPILE-1 (Pass 16). Every tier-1/2/3 document in `docs/raw/` carrying a decline, null or negative direction, then the listed lower-tier nulls; the positive Silver cases follow in the same columns. No averaging, no net read.

| Company | Document, date | Figure verbatim | Direction | Tier | Raw path | Compiled file:line |
|---|---|---|---|---|---|---|
| Microsoft, in News plaintiffs' brief | ECF 1977-1, 1:25-md-03143, 2026-09-17 | "83-93% drops in click-through rates for The Times and DNP's domains, and 51% to 94% for ZD's domains" | negative | 2 | `raw/a-court-mdl-microsoft-ctr-data-2026-09-22.md` | `markets/paid-placement.md:97` |
| NerdWallet | 8-K Ex-99.1, 2026-02-25 | "Credit cards revenue of $26.5 million decreased 24% year-over-year, primarily due to continued headwinds in organic search traffic" | negative | 2 | `raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md`; `raw/e-nerdwallet-8k-repull-2026-09-23.md` | L32 above |
| IAC / People Inc | 8-K Ex-99.2 deck, 2026-02-03 | "50% decline in Google Search referrals since 2023"; AIO on "nearly 70% of top People Inc. queries" | negative | 2 | `raw/e-case-iac-investor-deck-2026-02-03-2026-09-22.md` | `findings/transition-evidence.md:35` |
| IAC / People Inc | 8-K Ex-99.2 deck, 2026-05-04 | "63% decline in Google Search referrals over two years" | negative | 2 | `raw/e-case-iac-investor-deck-2026-05-04-2026-09-22.md` | `findings/transition-evidence.md:35` |
| People Inc | 10-Q, 2026-08-03 | "22% decline in Core Sessions, due primarily to the impact of the increasing prominence of Google AI Overviews" | negative | 2 | `raw/e-case-edgar-fulltext-results-2026-09-23.md` | not carried |
| Chegg | 8-K, 2025-08-05 | "2.6 million subscribers... year-over-year decline of 40%... lower traffic, largely due to Google AI Overviews" | negative | 2 | `raw/e-case-edgar-fulltext-results-2026-09-23.md` | not carried |
| Chegg | 10-Q, 2026-05-11 | AIO, ChatGPT "materially adversely affected our business... by reducing traffic to our platform" | negative, no figure | 2 | `raw/e-case-chegg-10q-2026-05-11-2026-09-22.md` | not carried |
| Chegg v. Google | complaint, D.D.C. 1:25-cv-00543, 2025-02-24 | "71% of Chegg Study traffic" and "60% of Chegg Study acquisitions" from search referrals (2024) | negative, dependence pleaded | 2 | `raw/b-court-dockets-table-2026-09-22.md` | `markets/paid-placement.md:98` |
| Penske Media v. Google | amended complaint, 1:25-cv-03192, 2025-12-04 | affiliate revenue "declined by more than a third" by end-2024; "over 80%" zero-click among AIO searches | negative | 2 | `raw/b-court-dockets-table-2026-09-22.md` | `markets/paid-placement.md:99` |
| Dow Jones, NYP v. Perplexity | complaint, 1:24-cv-07984, 2024-10 | "virtually no click-through traffic"; ad-revenue share "unspecified portion" | negative | 2 | `raw/b-court-dockets-table-2026-09-22.md` | `markets/paid-placement.md:100` |
| LendingTree | 10-K, 2026-03-09 | "organic searches and artificial intelligence ('AI') overviews, that depend upon the searchable content on our sites" | negative, risk factor, no figure | 2 | `raw/e-case-lendingtree-10k-2026-03-09-2026-09-22.md` | not carried |
| Reddit | 10-Q, 2026-07-31 | suit "alleging... false or misleading statements... concerning the impact of Google Search and its AI Overviews feature" | negative, allegation | 2 | `raw/e-case-reddit-10q-2026-07-31-2026-09-22.md` | not carried |
| EDGAR full-text, R-BLOCKED re-pull | 4 phrases, 57 hits, filed 2025-03-24 to 2026-09-22 | no hit states a moved metric; TechTarget risk factor "would reduce the number of visitors" only | null — no result-stating filing | 2 | `raw/e-edgar-fulltext-repull-2026-09-23.md` | not carried |
| Yelp | 8-K Ex-99.2, 2026-08-06 | "3.4x as many AI citations than the next closest platform", commissioned study | positive, cross-sectional | 2 | `raw/e-case-yelp-shareholder-letter-2026-08-06-2026-09-22.md` | `findings/transition-evidence.md:35` |
| TechTarget | 10-K, 2026-03-11 | "2x to 3x higher membership conversion rate from answer engine and LLM citations" | positive, ratio, no baseline | 2 | `raw/e-case-techtarget-10k-2026-03-11-2026-09-22.md` | not carried |
| Criteo | 8-K Ex-99.1, 2026-08-05 | "over 2,000 brands advertising on ChatGPT across seven countries" | positive, count only | 2 | `raw/e-case-criteo-earnings-release-2026-08-05-2026-09-22.md` | `findings/ai-ads-evidence.md:47` |
| EverQuote | 8-K Ex-99.2 deck, 2026-08-03 | "Consumer adoption of AI adds new sources of high-intent traffic" | positive, no figure | 2 | `raw/e-case-everquote-investor-deck-2026-08-03-2026-09-22.md` | not carried |
| Yext | 8-K Ex-99.3, 2026-09-01 | "grow its AI visibility by 147%... in only two weeks", vendor on itself | positive | 2 | `raw/e-case-edgar-fulltext-results-2026-09-23.md` | `markets/organic-recommendation.md:87` |
| HubSpot | Fortune op-ed, 2026-09-22 | blog "5 million" fewer visits in a thirty-day period; AI search "+37%", traditional search "−11%" | negative | 3 | `raw/e-case-fortune-hubspot-blog-traffic-loss-2026-09-23.md` | L145 above |
| TW3 Partners / Citead | arXiv 2609.07559, 2026-09-07 | 2023 GEO levers move citation on "none" of ten engine families | null | 4 | `raw/e-case-c11-arxiv-tw3-partners-geo-score-2026-09-22.md` | L33 above |
| OtterlyAI | HTML vs Markdown experiment, 2026-04-01 | .md citations 0; bot visits 0% vs HTML 2.8–4.6% | null, tactic | 5 | `raw/e-case-otterly-html-vs-markdown-experiment-2026-09-23.md` | L126 above |
| OtterlyAI | llms.txt experiment, 2026-02-05 | /llms.txt 84 of 62,100+ AI bot visits (0.1%) | null | 5 | `raw/e-case-otterly-llms-txt-experiment-2026-09-23.md` | not carried |
| Jonathan Mall | GEO experiment, undated | mentions +32 / −27, flat; citations 171 gained vs 32 lost | null (mentions); up (citations) | 5 | `raw/e-case-jonathanmall-geo-experiment-2026-09-23.md` | L127 above |
| Gaurav Tiwari | GSC audit, 2026-08-31 | "22% CTR drop"; 14 of 18 AI-Overview queries down | negative | 5 | `raw/e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-2026-09-22.md` | L31 above |
| SE Ranking | own ChatGPT campaigns, publ. 2026-08-10 | CTR 1.30% on 97,000+ impressions, "very few sign-ups" | null, paid | 5 | `raw/b-seranking-chatgpt-ads-study-2026-09-23.md` | `findings/ai-ads-evidence.md:45` |
| Adthena client, via Campaign | 2026-03 | "just 3%" of $250K spent after weeks; CTR 0.91% | negative, paid | 5 | `raw/b-campaign-chatgpt-ads-underwhelming-2026-09-23.md` | `findings/ai-ads-evidence.md:46` |
| r/SEO commenter | Arctic Shift, 2026-09-03 | impressions 5K → 15K daily, "no traffic increase at all" | null | 7 | `raw/e-case-reddit-arcticshift-comments-2026-09-23.md` | not carried |

**Positive Silver cases, same columns** — grade_raw / grade_rule1 in the company cell.

| Company | Document, date | Figure verbatim | Direction | Tier | Raw path | Compiled file:line |
|---|---|---|---|---|---|---|
| Quattr / Men's Wearhouse — Silver / Bronze | vendor case, undated | "75% more AI Mode visibility... 46% more clicks"; untreated 10,940 → 11,356 | positive | 5 | `raw/e-case-quattr-menswearhouse-2026-09-22.md` | L27 above |
| Sitefire / Pointhound — Silver / Bronze | vendor case, window 2026-02-23 to 06-29 | "+300% more site visits from AI Search"; "Visibility Score 0 → 1.0%" | positive | 5 | `raw/e-case-sitefire-pointhound-2026-09-22.md` | L28 above |
| Sitefire / Jerry — Bronze (c10), Silver (c13) / Bronze | vendor case, Apr–Jun 2026 | "+78% AI referral traffic... 112% vs. 72% treated-vs-untouched" | positive | 5 | `raw/e-case-c13-sitefire-jerry-2026-09-22.md`; `-c10-` | L29 above |
| Seer Interactive / "SaaS HR" — Silver / Bronze | agency study, July 2026 | "300% increase in AI traffic"; site-wide AI sessions "remained stagnant" | positive | 5 | `raw/e-case-seer-interactive-content-recency-2026-09-22.md` | L30 above |
| OtterlyAI Reddit test — Silver / Silver | vendor experiment, 2026-04-11 to 06-10 | AI citations 48 (dormant arm) vs 426 (active arm) | positive | 5 | `raw/e-case-otterly-reddit-experiment-2026-09-23.md` | L125 above |
| Jonathan Mall / "Brand A" — Silver / Bronze | practitioner experiment, July 2–9, year absent | treated page 23 → 72 citing queries; 171 gained vs 32 lost | positive, citations | 5 | `raw/e-case-jonathanmall-geo-experiment-2026-09-23.md` | L127 above |
| Boily / two dental clinics — Silver / Bronze | vendor comparison, 2026-06 | mention rate 11% → 27% treated; 11% → 10% untreated | positive | 5 | `raw/e-case-boily-dental-geo-comparison-2026-09-23.md` | L128 above |
| Chime / AirOps — Bronze / Bronze, brand-side | careers page, 2025-11-24 | "tripled our AI citations and increased content velocity by 70 percent" | positive | 3 | `raw/e-case-chime-careers-airops-2026-09-23.md` | L148 above |

Caveats, this append: the two Silvers that run negative or null (E6 NerdWallet, E7 TW3) and X2 sit in the first table, not the second; Yelp, TechTarget, Criteo, EverQuote and Yext run positive and are kept in the first table because the brief names them, direction column stating it; every positive Silver is tier 5 and vendor- or practitioner-measured, the one tier-3 positive is Bronze; the tier-2 negatives are the filer's own attribution to AI surfaces, not a measured incremental effect; Chegg 8-K and People Inc 10-Q sentences come from a regex-selected raw and no compiled file carries them; overrun of the 100-line budget recorded, not trimmed.

## Primary re-pulls, REPULL-1, 2026-09-23
- AI Overviews CTR self-measured audit (E5) · `raw/e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-2026-09-22.md` (5) · `raw/e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-primary-2026-09-23.md` (5) · remainder of the article (from "Here's the ironic twist…" to FAQs): "Sites with 70%+ Google dependency are the most vulnerable"; "40-50% of traffic … barely feeling the impact"; "5-10% per quarter" (projection); "15-30% of informational queries" (unnamed studies); five in-article images saved · agrees ("22% CTR drop", 14 of 18 sit in the substitute's captured part; nothing in the remainder contradicts); images unread until IMG-1
- +54% GPT-User bot hits (E4, Silver) · `raw/e-case-seer-interactive-content-recency-2026-09-22.md` (5) · `raw/e-case-seer-interactive-content-recency-primary-2026-09-23.md` (5) · text figures "300%", "219%", "54%", "80%", "3.6%" unchanged; two results charts saved at `raw/img/e-case-seer-interactive-content-recency-primary-2026-09-23/02-…png`, `03-…png` (unread until IMG-1) · agrees
- Blackbird case (Searchable customer story, census c13 "screened — not opened") · `raw/e-case-census-c13-2026-09-22.md` (n/a — href not resolved) · `raw/e-case-searchable-blackbird-primary-2026-09-23.md` (6) · "170 hours saved in 30 days"; "+30% average improvement in AI search visibility across client base"; "$25k MRR built through Searchable partnership"; "$1.1M in 2026 pipeline from AI search service line"; agency customer, no n, no window, no baseline, engines named without version · not in substitute (page now reached); no brand-level outcome — agency operating metrics and an unbased "+30%"
- HubSpot blog "5 million" fewer visits (A9, L270 / H11 row) · `raw/e-case-fortune-hubspot-blog-traffic-loss-2026-09-23.md` (3) · `raw/e-case-fortune-hubspot-blog-traffic-loss-primary-2026-09-23.md` (3) · "Our blog lost 5 million visits in a thirty-day period. We saw AI search usage climbing 37% while traditional search declined 11 percent." · agrees — bypass-extension re-read found the same 37 paragraphs, no figure added or missing; tier unchanged (P16-c4b, 2026-09-23)

### Primary re-pull RP2-A, 2026-09-23
- IAC / People Inc, 2026-02-03 deck slide 7 — claim: "50% decline in Google Search referrals since 2023" (row L254). Substitute (prior text-extraction pull) flagged the callout as unreconciled against the chart's printed bar totals (2,255/2,327/2,021). Primary (chart image, `raw/img/e-case-iac-investor-deck-repull2-2026-09-23/01-slide7-q4-audience-trends-core-sessions.jpg`): those totals are **Core Sessions** (Google Search + All Other combined); the Google Search segment alone reads 1,223 (Q4'23) → 612 (Q4'25) = **49.96% decline**, reconciling the "50%" callout exactly. The 2026-05-04 deck's "63% decline... over two years" (row L255) is a different deck, different window — carried side by side, not averaged; this re-pull does not touch it. Raw: `raw/e-case-iac-investor-deck-repull2-2026-09-23.md`; `raw/e-case-iac-investor-deck-repull2-2026-09-23-img-2026-09-23.md`. Tier 2 (filed), unchanged.

### Primary re-pull RP2-A, 2026-09-23 (Otterly image pulls)
- OtterlyAI llms.txt experiment (L273, X3 L221) — claim: "/llms.txt 84 of 62,100+ AI bot visits (0.1%)". Image pull confirms both headline figures via a per-URL bot-breakdown screenshot: /llms.txt's 84 hits break down as 81 ChatGPT-User On-Demand Fetcher + 3 OAI-SearchBot, zero from Claude/Perplexity/Gemini/Mistral. New, not in the article's own text: a dashboard tile reads "Total Agents Page Visits: 62.1K" against "418.2K human page visits" = agent share **12.9%** of combined traffic; and /robots.txt (the article's own comparator) received **1,140** total bot hits across five named bots, ~13.6x llms.txt's 84. Figures agree; grade unchanged (Bronze/Bronze, tier 5). Raw: `raw/e-case-otterly-llms-txt-experiment-repull2-2026-09-23.md`; `raw/e-case-otterly-llms-txt-experiment-repull2-2026-09-23-img-2026-09-23.md`.
- OtterlyAI Reddit test (L125, X1 "Silver / Silver" — the one rule-1 Silver Otterly case) — chart images (social-citation-share bar, methodology infographic, organic-search version-A-vs-B bar) reconfirm the article's own text figures (7 vs 20 Google keywords ranked; 46.4%/31.8%/13.0% social-citation shares); grade unchanged (Silver/Silver, tier 5). One new, uncorroborated figure: a Reddit-native mod-insights screenshot shows "2.8k views, 1.5k members, 52 posts, 221 comments" over an unlabeled 30-day window, not attributable to either arm by the image alone — not carried into a grade. Raw: `raw/e-case-otterly-reddit-experiment-repull2-2026-09-23.md`; `raw/e-case-otterly-reddit-experiment-repull2-2026-09-23-img-2026-09-23.md`.
- OtterlyAI HTML vs Markdown experiment (L272, X2 L220) — claim: ".md citations 0; bot visits 0% vs HTML 2.8-4.6%". Image pull (Citations dashboard screenshot) adds a figure not in the article's own text: the two HTML test pages were cited **52 and 17 times** respectively (69 total, 14-day window) in OtterlyAI's own Brand Report citations view, while both `.md` mirrors show 0 — corroborating "zero .md citations". This citation-count metric is a different OtterlyAI product surface than the article's own "AI bot visits" crawler-analytics figure (7.4%/0%, 137 visits) — carried side by side, not summed. Grade unchanged (Silver/Bronze — item 3, tier 5). Raw: `raw/e-case-otterly-html-vs-markdown-experiment-repull2-2026-09-23.md`; `raw/e-case-otterly-html-vs-markdown-experiment-repull2-2026-09-23-img-2026-09-23.md`.

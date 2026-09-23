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

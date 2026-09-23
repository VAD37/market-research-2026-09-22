# Director brief — demand for brand visibility inside AI assistants

| | |
|---|---|
| File date | 2026-09-23 |
| Oldest pull depended on | 2026-09-22 — every compiled file cited; oldest source publication carried 2024-11-12 (`findings/whitespace.md` L6) |
| Lanes | all six, A–F, via `findings/`, `markets/`, `customers/`, `competitors/INDEX.md` |
| Hypotheses touched | all 23 — H1–H16, HE1–HE3, HP1–HP4 |
| Claims at tier 3 or better | none new; restates compiled figures. Programme count: 68.0% (17 of 25, Pass 9) and 44.4% (12 of 27, review-1), both stand |
| Form | long form of `findings/executive-brief-2026-09-23.md`; 10–20 minutes |

Reading key. Paths are relative to `docs/`; `L` is the line as read 2026-09-23. Tier per `method/trust-rubric.md` L9–17: 1 strongest, 7 weakest; tier 6 is "Marketing. Not a source" (L16). Labels: vendor-reported, analyst-derived, filed, company-stated, measured-by-us. Every pull is dated 2026-09-22 unless stated. Research only: evidence, no verdict (`MegaPlan.md` §Non-goals).

## 1. The question, and the short answer

> Which segments show real-world demand for visibility and recommendation inside AI assistants, what evidence shows it works, and what did brands that moved actually change? (`method/plan.md` L11)

Demand is visible, thin, and enterprise-heavy: 7 of 27 segment cells read spend, 5 of them enterprise, and 6 of the 7 rest on job postings, the weakest spend signal. Proof of a sales effect does not exist in the published record: 0 Gold of ~980 cases screened, and no case uses a holdout, geo-split or switchback. Paid inventory is live on ChatGPT and Google and refused by Claude; no engine publishes a rate card. No sub-market has a measured size; every dollar size found is a forecast. Brands that moved changed content operations and tooling far more often than paid media: 63 and 58 cases against 2. Our own engine sampling stopped at a partial day 0, by owner decision 2026-09-22 22:40.

## 2. What was done

| Pass | What it pulled | Count | Deliverable | Source |
|---|---|---|---|---|
| 0 | rules, glossary, hypotheses, panel protocol | 5 deliverables | `method/` | `method/STATE.md` L33 |
| 1 | source channels and query book | 22 of 22 red-team amendments; 42 clusters after AMEND-1 | `sources/` | `method/STATE.md` L37, L71 |
| 2 | platform primaries, share, crawlers, regulators, dockets | 11 clusters, ~150 raw pulls | `raw/` a-, b-, c- | `method/STATE.md` L54 |
| 3 | vendor census | 121 screened, 26 rostered; ~190 raw pulls | `raw/` vendor censuses c1–c6 | `method/STATE.md` L51, L64 |
| 4 | published success stories | 13 clusters; ~980 candidates screened | `raw/e-case-census-c1`…`c13` | `method/STATE.md` L83; `findings/proof-scorecard.md` L75 |
| 5 | manipulation techniques and countermeasures | 7 clusters, ~70 raw pulls | `raw/d-technique-census-c1`…`c7` | `method/STATE.md` L99 |
| 6 | market sizes | 16 size pulls, 18 figures; 3 market files | `markets/` | `method/STATE.md` L84, L101 |
| 7 | competitor profiles | 41 profiles + INDEX | `competitors/` | `method/STATE.md` L111 |
| 8 | demand signals per segment | 15 + 10 + 12 signal pulls; 27 cells | `customers/` | `method/STATE.md` L85–87, L97 |
| 9 | findings, then an independent review | 4 files; review recounted 27 claims | `findings/` | `method/STATE.md` L113, L116 |
| 11 | what brands that moved changed | 108 cases, 99 name a change | `findings/transition-evidence.md` | `method/STATE.md` L117 |

**Pass 10 held.** Day 0, 2026-09-22: Claude 83 of 160 runs, logged-in, Memory localising to Vietnam; Gemini 24 of 160, "Flash-Lite", throttled; Google AI Mode 76 of a possible 176, AI Overviews 0 of 14 rendered; ChatGPT and Perplexity 0 runs, blocked. Copilot and Rufus never sampled. Hold from 2026-09-22 22:40; gap never back-filled (`method/STATE.md` L127–137; `method/plan-review-2-2026-09-23.md` L52–59).

## 3. The market

**Key detail: no sub-market has a measured size.** Every dollar size is a forecast, and forecasts disagree by up to ~35× on the same horizon.

### 3a. Size — measured against forecast, side by side

| Metric | Figure | Label, tier | Path |
|---|---|---|---|
| Measured size, any sub-market | none; 15 of 18 published figures are forecasts | analyst-derived, 6 | `findings/whitespace.md` L24 |
| Organic, bottom-up floor | $5.3M–$35.2M annualised; 4 of 34 vendors (~12%) | vendor-reported inputs, 5 | `markets/organic-recommendation.md` L36 |
| Paid, bottom-up | not computable: 0 of 8 engines give price and count | — | `markets/paid-placement.md` L45 |
| Agentic, bottom-up | not computable from disclosed inputs | — | `markets/agentic-commerce.md` L32 |
| Forecast, organic | Valuates US$7,318M by 2031 · Market Decipher USD 32.92B by 2034 | forecast, 6 | `markets/organic-recommendation.md` L44, L46 |
| Forecast, organic | Dimension USD 17,148.6M 2034 · IntelMarketResearch USD 22B 2034 | forecast, 6 | `markets/organic-recommendation.md` L45, L48 |
| Forecast, paid | EMARKETER US $68.25B 2030 · WPP Media global "over $100 billion" 2030 | forecast, analyst-derived | `markets/paid-placement.md` L52, L54 |
| Forecast, agentic | EMARKETER US $144B 2029 · McKinsey global $3T–$5T 2030 | forecast, 6 · 5 | `markets/agentic-commerce.md` L46, L49 |
| Forecast, agentic | Morgan Stanley $190B–$385B · Bain $300B–$500B, US 2030 | forecast, 5 · 6 | `markets/agentic-commerce.md` L47–48 |
| Forecast, agentic, outliers | Gartner "$15 trillion" B2B 2028 · Grand View USD 65.5B 2033 | forecast, 6 | `markets/agentic-commerce.md` L51–52 |
| Attention proxy, not dollars | IAB: 76% of >200 buyers name AI answers No. 1 focus | analyst-derived, 4 | `markets/organic-recommendation.md` L38 |

Two organic forecasts share a 40.6% CAGR off ~$1.09B in 2026 and land at $17.1B and $32.9B (`markets/organic-recommendation.md` L50). Agentic 2029–2030 figures span USD 144B to USD 5T, "roughly 35×", scopes not comparable (`markets/agentic-commerce.md` L54).

### 3b. Paid inventory — per engine

| Engine | Status | Label, tier | Path |
|---|---|---|---|
| Assistant share leader | ChatGPT first on web-visit, referral, desktop share: ~53% · 79.4% · 34.80% | vendor-reported, 4 · 4 · 5; never averaged | `method/plan.md` L146, L168 |
| ChatGPT | live from 2026-02-09; self-serve Ads Manager beta | company-stated, 3 | `markets/paid-placement.md` L74 |
| ChatGPT ads revenue | "$1 billion in annualized revenue run rate", published 2026-08-31 | company-stated, 3 | `markets/paid-placement.md` L25 |
| ChatGPT reach | "tens of thousands of advertisers"; "over 40 countries"; 31 EU markets | company-stated, 3 | `markets/paid-placement.md` L25, L60–61 |
| Google AI Overviews | live; existing campaigns auto-eligible, "you can't opt out" | company-stated, 3 | `markets/paid-placement.md` L76 |
| Google AI Mode · Gemini app | "testing" · unknown — checked 2026-09-22 | company-stated, 3 | `markets/paid-placement.md` L77–78 |
| Claude | no — "Claude will remain ad-free", 2026-02-04 | company-stated, 3 | `markets/paid-placement.md` L75 |
| Copilot · Amazon | live via Microsoft auction · GA US 2026-03-25, CPC | company-stated, 3 | `markets/paid-placement.md` L79–80 |
| Coverage | 5 of 8 engines live; 0 of 8 rate cards; 1 of 8 revenue figure | company-stated, 3 | `markets/paid-placement.md` L39 |
| Only price stated | OpenAI max-bid guidance "$3–$5 USD per click" | company-stated, 3 | `findings/whitespace.md` L23 |
| ChatGPT ad presence | 26% (Similarweb) · 4.47% US (Adthena) · 0.00% of 169,560 UK scrapes | vendor-reported, 5; not reconciled | `markets/paid-placement.md` L26–28 |
| Measured by us | 0 ad units in 76 AI Mode runs; 0 of 14 AI Overviews rendered | measured-by-us, 1; one date, VN IP | `markets/paid-placement.md` L84 |
| Where AI ad money sits | EMARKETER: "over 80% flows next to AI content, not inside chatbots" | analyst-derived | `markets/paid-placement.md` L89 |

### 3c. Agentic checkout, regulation, litigation

| Metric | Figure | Label, tier | Path |
|---|---|---|---|
| Live checkout programs | 4 — ChatGPT, Google, Copilot, Perplexity; Claude, Amazon, Grok none | company-stated, 3 | `markets/agentic-commerce.md` L24 |
| Fee disclosed | 1 of 4 — Copilot, "does not take a commission" | company-stated, 3 | `markets/agentic-commerce.md` L25 |
| Protocol fee clauses | 6 of 6 `unknown — checked` 2026-09-22 | company-stated, 3 | `findings/whitespace.md` L32 |
| Open protocols | ACP, UCP, x402 Apache-2.0, no gate to read (H8) | company-stated, 3 | `findings/unknowns.md` L32 |
| AI conversion vs non-AI visits | Adobe "AI Conversion Now 42% Higher" | vendor-reported, 4 | `markets/agentic-commerce.md` L37 |
| AI conversion vs organic search | Shopify "nearly 50% higher rates than organic search" | vendor-reported, 5 | `markets/agentic-commerce.md` L39 |
| EU AI Act Art. 50 | in force 2026-08-02; names no assistant | filed, 2 | `markets/paid-placement.md` L92 |
| ChatGPT DSA status | VLOSE 2026-08-31; 159.1M EU recipients; no Art. 39 repository yet | filed, 2 | `findings/whitespace.md` L33 |
| UK CMA | fair-ranking requirement 2026-06-17 covers "search generative AI features" | filed | `markets/organic-recommendation.md` L88 |
| US | FTC 16 CFR 255 names no AI; 16 CFR 465.2 bans procured fake reviews | filed | `markets/organic-recommendation.md` L88 |
| Enforcement on AI-answer ad disclosure | none found, any jurisdiction | filed | `markets/paid-placement.md` L92 |
| Referral harm, court record | Microsoft "83-93% drops in click-through rates" (ECF 1977-1) | filed, 2 | `markets/paid-placement.md` L97 |

## 4. Supply side

**Key detail: funding is large, disclosure is small.** A $1.8B valuation sits beside 2 of 34 vendors filing any revenue, and neither breaks out this product.

| Metric | Figure | Label, tier | Path |
|---|---|---|---|
| Vendors rostered | 26 of 121 screened; 34 after Pass 3 | analyst-derived | `markets/organic-recommendation.md` L25 |
| Profiles | 41; stale from 2026-12-22 | — | `competitors/INDEX.md` L8, L58 |
| Largest round | Profound $180M Series D at $1.8B, 2026-09-15 | company-stated, 3 | `markets/organic-recommendation.md` L28 |
| Funding disclosed | 8 of 34; others tier 5 via press | company-stated, 5 | `markets/organic-recommendation.md` L28 |
| Other rounds | AirOps $40M B · Brandlight $30M A · Peec AI $21M A | company-stated, 5 | `markets/organic-recommendation.md` L28 |
| Round conflict | geoSurge "$12M seed" vs EU-Startups €10M, unreconciled | company-stated, 5 | `markets/organic-recommendation.md` L28 |
| Price disclosed | 14 of 34; self-serve $20/mo to $999/month | vendor-reported | `markets/organic-recommendation.md` L26 |
| Price, agencies · sell-side | 1 of 5 (Pace $1,499–$2,499) · 1 of 7 (Shopware) | vendor-reported | `method/STATE.md` L105, L107 |
| Customer count disclosed | 8 of 34; units not comparable, never summed | vendor-reported | `markets/organic-recommendation.md` L27 |
| Filed revenue | 2 of 34; neither broken out to this product | filed, 5 relayed | `markets/organic-recommendation.md` L29 |
| Product revenue, incumbent | Semrush $38M AI-products ARR, 2025-12 | filed | `competitors/INDEX.md` L39 |
| Pure-play revenue | Peec AI ARR $4M vs $10M · Searchable €2.2M · Rankscale ~$220K | vendor-reported; analyst-derived | `competitors/INDEX.md` L17, L20, L38 |
| Prompt set behind composite score | 0 of 34 vendors; 0 of 41 profiles | vendor-reported, 3 | `findings/whitespace.md` L26 |
| Incumbent deltas | Semrush "+$60/mo"; HubSpot "$50/mo"; Similarweb "$99" | vendor-reported | `markets/organic-recommendation.md` L68 |
| Acquisitions | Semrush → Adobe 2026-04-28, $12.00/share; Scrunch → Sitecore 2026-06-03 | filed; company-stated | `markets/organic-recommendation.md` L87 |
| Scrunch deal value | undisclosed (Sitecore) vs $225M (Bloomberg, unconfirmed) | company-stated; relayed | `markets/organic-recommendation.md` L87 |
| Engines' native tooling | Google Search Console, no AI segment; OpenAI a UTM tag; Anthropic none | company-stated, 3 | `markets/organic-recommendation.md` L86 |
| "Do nothing" substitute | Google: "no additional requirements... nor other special optimizations necessary" | company-stated, 3 | `markets/organic-recommendation.md` L85 |

## 5. Demand side

**Key detail: willingness to pay is unknown in 27 of 27 cells.** No buyer anywhere discloses a price paid.

| Metric | Figure | Label, tier | Path |
|---|---|---|---|
| 27-cell read | 7 spend · 1 attention · 11 none — checked · 8 blank | analyst-derived, 5 | `findings/demand-map.md` L17, L76 |
| Signal carrying spend | 6 of 7 spend cells rest on S1 job postings | company-stated, 3 | `findings/demand-map.md` L77 |
| Where spend sits | 5 of 7 spend cells enterprise; 1 of 9 SMB cells | analyst-derived, 3 | `findings/demand-map.md` L80 |
| By sub-market | organic 5 spend · paid 1 · agentic 1 | analyst-derived, 3 | `findings/demand-map.md` L51–53 |
| Willingness to pay | unknown, 27 of 27 cells | — | `findings/demand-map.md` L58 |
| Rule split | strict `none` rule: 8 of 27 cells meet bar; loose: 27 of 27 | analyst-derived | `method/plan-review-2-2026-09-23.md` L71 |

- **Skincare and beauty** — 3 spend, all enterprise (e.l.f. AEO/GEO team; e.l.f. Direct Offers pilot "Sponsored deal"; e.l.f. agentic role), 1 attention (SMB, one OMR reviewer), 5 none (`customers/skincare-beauty.md` L6, L21–29). Agentic × enterprise reads spend there and attention in `markets/agentic-commerce.md` L105; both stand (`findings/demand-map.md` L82).
- **B2B SaaS** — 3 spend, all organic (Actindo 52–70 employees, AutoLeap 199–225, Pennylane and Mercury), 6 paid and agentic cells none — checked on 9 of 12 signals (`customers/b2b-saas.md` L8, L22–30).
- **High-CPA regulated** — 1 spend (Cigna, "Lead Analyst, Technical Search (SEO/AEO/GEO)"), 8 blank; no source states an SMB or mid-market band (`customers/high-cpa-regulated.md` L6, L19–27); cards 0 of 9 posting queries (L32).

Both readings stand on the floor. The `customers/` files read tier-3 postings as spend; the source censuses marked the same postings attention, reading the tier-5 floor as a ceiling (`findings/demand-map.md` L68). Two compilers applied the `none` rule two ways; 19 of 27 reads turn on it (`findings/demand-map.md` L45).

## 6. Proof — what the published cases show

**Key detail: no causal lift anywhere, and the two highest-tier Silvers run against the category.**

| Metric | Figure | Label, tier | Path |
|---|---|---|---|
| Candidates screened | ~980, Passes 3 and 4 | measured-by-us | `findings/proof-scorecard.md` L75 |
| Gold | 0; zero holdout, geo-split or switchback | vendor-reported cases, 5 | `findings/proof-scorecard.md` L59 |
| Silver | 7 as graded in raw · 1 under grading rule 1 | vendor-reported cases, 5 | `findings/proof-scorecard.md` L17, L23 |
| Direction of the Silvers | 2 of 7 negative or null (NerdWallet, TW3/Citead) | filed 2; preprint 4 | `findings/proof-scorecard.md` L61 |
| Brand-side corroboration | 0 of 59 corroborate; 59 silent; ~107 unchecked | measured-by-us, 3 | `findings/proof-scorecard.md` L63 |
| Paid-by-outcome disclosed | 0 yes / 0 no / 12 unknown | vendor-reported, 6 | `findings/proof-scorecard.md` L62 |
| Anchor vertical | skincare 0 Silver at ~133 screened; supplements 0 cleared of 6 | vendor-reported, 5 | `findings/whitespace.md` L30 |
| Causal lift, any vendor | none; H3 killed | vendor-reported cases, 5 | `findings/unknowns.md` L27 |

The seven Silvers, each graded two ways. Grading rule 1: "a case missing any of items 1–7 is Bronze at best" (`method/plan.md` L117). Items: brand, engine, absolute date window, baseline, intervention, sample size, who measured (`findings/proof-scorecard.md` L21).

| # | Case | Direction, as stated | Grade as graded | Grade, rule 1 (item missing) | Tier | Path |
|---|---|---|---|---|---|---|
| E1 | Quattr / Men's Wearhouse | up: "46% more clicks on treated product pages" | Silver | Bronze (3) | 5 | `findings/proof-scorecard.md` L27 |
| E2 | Sitefire / Pointhound | up: "+300% more site visits from AI Search" | Silver | Bronze (6) | 5 | `findings/proof-scorecard.md` L28 |
| E3 | Sitefire / Jerry | up: "+78% AI referral traffic" | Bronze (c10) / Silver (c13) | Bronze (6) | 5 | `findings/proof-scorecard.md` L29 |
| E4 | Seer / "SaaS HR" client | up: "300% increase in AI traffic" | Silver | Bronze (3, 7) | 5 | `findings/proof-scorecard.md` L30 |
| E5 | Tiwari GSC audit | mixed: "22% CTR drop" | Silver | Bronze (3, 5) | 5 | `findings/proof-scorecard.md` L31 |
| E6 | NerdWallet 8-K | negative: credit cards revenue "decreased 24%" | Silver | Bronze (6) | 2 | `findings/proof-scorecard.md` L32 |
| E7 | TW3 / Citead, arXiv 2609.07559 | null: GEO levers move citation on none of ten families | Silver | Silver | 4 | `findings/proof-scorecard.md` L33 |

Missing items per `findings/review-1-2026-09-23.md` L102. Every Silver is an observational pre/post with a within-site or within-company control; none is randomised (`findings/proof-scorecard.md` L60). Only E6 crosses to sales, and it is a revenue line attributed by management, not lift (L67).

## 7. What brands that moved changed

**Key detail: paid-media change is named twice in 108 cases, both one Google pilot.**

| Kind of change | Cases naming it | Of which tier ≤3 | Path |
|---|---|---|---|
| Content ops | 63 | 16 (15 are llms.txt) | `findings/transition-evidence.md` L56 |
| Stack (vendor tool) | 58 | 2 | `findings/transition-evidence.md` L57 |
| Other (agency, PR, KPI, checkout) | 19 | 1 | `findings/transition-evidence.md` L59 |
| Org (hire, team, role) | 12 | 12 | `findings/transition-evidence.md` L55 |
| Paid media | 2 | 2 | `findings/transition-evidence.md` L58 |
| None named | 9 | 5 | `findings/transition-evidence.md` L60 |
| Cases in set | 108; 99 name a change | 38 | `findings/transition-evidence.md` L15, L61 |

Counts are measured-by-us over self-reports; stack rests on vendor pages at tier 5–6, org on postings and filings at tier 2–3 (L15). 57 of 58 stack cases rest on vendor pages (L72). Both paid cases are Google's Direct Offers pilot, e.l.f. and L'Oréal (L23, L69).

| H | Pass 11 mark | Earlier marks, standing beside | Path |
|---|---|---|---|
| H10 — org/content named more than paid | confirmed: 28 vs 2 at tier ≤3; 13 vs 2 excl. llms.txt | not produced (Pass 9, review-1) | `findings/transition-evidence.md` L66, L74 |
| H11 — tier-3 change in each vertical | confirmed: e.l.f., Pennylane, Cigna | killed (Pass 9); not produced (review-1) | `findings/transition-evidence.md` L67, L74 |

## 8. Manipulation and countermeasures (Lane D) — described, not operational

**Key detail: engines police prompt injection and fake reviews; none names corpus seeding, comparison-page farming or citation-preference content.**

| Metric | Figure | Label, tier | Path |
|---|---|---|---|
| Technique clusters | 6 techniques + 1 countermeasure cluster; ~70 raw pulls | measured-by-us | `method/STATE.md` L99 |
| Engine × technique cells named | 6 of 36 | company-stated, 3 | `findings/whitespace.md` L27 |
| Named, by engine | OpenAI 1, Anthropic 2, Google 2, Microsoft 1, Perplexity 0, Amazon 0 | company-stated, 3 | `method/STATE.md` L89 |
| Published single-action before-and-after on a production surface | 0 techniques | preprint, 4 | `findings/whitespace.md` L29 |
| llms.txt fetched by engines | 0: 15 tools × 3 trials, zero fetch events | preprint, 4 | `findings/whitespace.md` L28 |
| Citation-preference benchmarks | 9 measured rows, all benchmark, 0 live-site | preprint, 3–5 | `method/STATE.md` L94 |
| GEO levers, replication; 45-study survey | move citation on none of 10 families (n=605–1,531); no stable causal effect | preprint, 4 | `markets/organic-recommendation.md` L85 |
| In-the-wild brand-steering injection campaign | none documented | preprint, 3–5 | `method/STATE.md` L92 |

H13 confirmed (6 of 36 named; `findings/unknowns.md` L37). H14 killed: regulated 0 specimens, anchor 0 at the tier-4 floor (L38). H5 killed at Pass 9, unresolved — checked per review-1: FeatGEO Table 4 is a published pre/post (L29; `findings/review-1-2026-09-23.md` L43).

## 9. Hypotheses — all 23

Marks, three readings, none averaged. Pass 9: 6 confirmed · 6 killed · 4 unresolved · 7 not produced (`method/STATE.md` L112). Current register, review-1: 4 · 3 · 8 · 8 (`findings/unknowns.md` L49). Pass 11 adds H10, H11 confirmed; scored 17 of 23, 6 not produced (`method/STATE.md` L198). Pass 9 column per `findings/review-1-2026-09-23.md` L20–39.

| ID | Hypothesis | Pass 9 | Register now | Tier | Path |
|---|---|---|---|---|---|
| H1 | AI referral converts above organic search | unresolved | unresolved — checked | 4 | `findings/unknowns.md` L25 |
| H2 | paid inventory exists at scale | confirmed | confirmed | 3 | `findings/unknowns.md` L26 |
| H3 | a vendor demonstrates causal lift | killed | killed | 5 | `findings/unknowns.md` L27 |
| H4 | demand attention-only in every SMB cell | killed | killed; census read opposite | 3 | `findings/unknowns.md` L28 |
| H5 | corpus seeding measurably moves an answer | killed | unresolved — checked | 4 | `findings/unknowns.md` L29 |
| H6 | brand action precedes measured visibility change | confirmed | unresolved — checked | 5 | `findings/unknowns.md` L30 |
| H7 | organic spends in more cells than paid, agentic | unresolved | unresolved — checked | 3 | `findings/unknowns.md` L31 |
| H8 | protocol implementable without contract | confirmed | confirmed | 3 | `findings/unknowns.md` L32 |
| H9 | agentic spend enterprise, absent SMB | unresolved | unresolved — checked | 3 | `findings/unknowns.md` L33 |
| H10 | org/content changes outnumber paid | not produced | not produced; Pass 11 confirmed | 3 | `findings/unknowns.md` L34; `findings/transition-evidence.md` L66 |
| H11 | tier-3 transition evidence per vertical | killed | not produced; Pass 11 confirmed | 3 | `findings/unknowns.md` L35; `findings/transition-evidence.md` L67 |
| H12 | paid price disclosed publicly | unresolved | unresolved — checked | 3 | `findings/unknowns.md` L36 |
| H13 | P1 engine names a Pass-5 technique | confirmed | confirmed | 3 | `findings/unknowns.md` L37 |
| H14 | manipulation denser in regulated than anchor | killed | killed | 4 | `findings/unknowns.md` L38 |
| H15 | composite-score vendors disclose prompt set | killed | unresolved — checked | 3 | `findings/unknowns.md` L39 |
| H16 | every published size is a forecast | confirmed | unresolved — checked | 3 | `findings/unknowns.md` L40 |
| HE1 | ChatGPT paid product live, documented | confirmed | confirmed | 3 | `findings/unknowns.md` L41 |
| HE2 | Claude returns brand recommendations | not produced | not produced | 1 | `findings/unknowns.md` L42 |
| HE3 | ad formats render in Google AI surfaces | not produced | not produced | 1 | `findings/unknowns.md` L43 |
| HP1 | between-engine gap exceeds within-engine spread | not produced | not produced | 1 | `findings/unknowns.md` L44 |
| HP2 | recommended brand set unstable between dates | not produced | not produced | — | `findings/unknowns.md` L45 |
| HP3 | citation-to-mention ratio below 0.50 | not produced | not produced | 1 | `findings/unknowns.md` L46 |
| HP4 | citation rate higher with search on | not produced | not produced | 1 | `findings/unknowns.md` L47 |

## 10. Programme done — 6 rows

| Condition | Bar | Status | Path |
|---|---|---|---|
| Tier-3 share of load-bearing claims | ≥80% | not met — 17 of 25 = 68.0% (Pass 9); 12 of 27 = 44.4% (review-1) | `findings/unknowns.md` L55 |
| P1 engine × sub-market cells | number or `unknown — checked` | met — 9 of 9 | `findings/whitespace.md` L48 |
| Segment matrix | every cell spend, attention or none | not met — 19 of 27; strict 8, loose 27 | `method/plan-review-2-2026-09-23.md` L13 |
| Success stories | one Silver per vertical, or absence with count | met under both grade readings | `method/STATE.md` L197 |
| Hypotheses | every H scored | not met — 15 of 23 (register); 17 of 23 (after Pass 11) | `findings/unknowns.md` L59; `method/STATE.md` L198 |
| Pass 10 | 3 predictions checked on panel | not met — 0 of 3; held | `findings/unknowns.md` L60 |

Tier-3 share, split (review-2): excluding the 8 case-corpus claims 12 of 19 = 63.2%; excluding meta-claims too 12 of 16 = 75.0%; dropping only the 3 meta-claims 12 of 24 = 50.0% (`method/plan-review-2-2026-09-23.md` L32; `findings/review-1-2026-09-23.md` L79). While Pass 10 is held, 4 of 6 rows can move; Hypotheses caps at 17 of 23 and Pass 10 at 0 of 3 (`method/plan-review-2-2026-09-23.md` L18).

## 11. What the evidence does not show

- Causal sales lift from any intervention: no holdout, geo-split or switchback in ~980 screened (`findings/proof-scorecard.md` L59).
- Whether AI referral converts above organic search: Adobe compares AI to non-AI visits; the organic comparator exists only at tier 5 (`findings/unknowns.md` L25).
- The size of any sub-market, a price any buyer paid, or any engine's rate card (`findings/whitespace.md` L23–24; `findings/demand-map.md` L58).
- A per-engine breakout of AI referral or conversion from any retail-analytics publisher (`findings/whitespace.md` L34).
- Whether any named brand confirms a vendor case on its own domain: 0 of 59 checked; ~107 unchecked (`findings/proof-scorecard.md` L63).
- What engines return to buying-shaped prompts under neutral conditions: six panel hypotheses not produced (`findings/unknowns.md` L42–47).
- Whether any posting was filled or any named change shipped (`findings/transition-evidence.md` L82).
- Anything from blocked channels (section 12).

## 12. Blocked vs exhausted channels

| Channel | State 2026-09-22 | What it holds back | Path |
|---|---|---|---|
| sec.gov, EDGAR | blocked — 403, then 503 | filings at tier 2; entered via IR copies or relays | `findings/unknowns.md` L85 |
| reddit.com, g2.com, capterra.com | blocked — 403, CAPTCHA | negative cases; review velocity, reviewer industry | `findings/unknowns.md` L91–92 |
| indeed.com, upwork.com | blocked — 403, Cloudflare | SMB and mid-market postings | `findings/unknowns.md` L92 |
| trends.google.com | blocked — relative index only | absolute search interest | `findings/unknowns.md` L92 |
| chatgpt.com, perplexity.ai consumer surfaces | blocked, then held by owner | measured-by-us panel | `findings/unknowns.md` L93 |
| emarketer.com, Gartner | blocked — subscription, 403 | analyst sizes | `findings/unknowns.md` L90 |
| Engine ad and checkout pages | exhausted — pages exist, name no price or fee | rate cards, take rates | `findings/unknowns.md` L86, L88 |
| Brand newsrooms | cap, not exhaustion — 59 of ~166 | brand-side corroboration | `findings/unknowns.md` L91 |

## 13. Questions only the owner can answer

No lean is attached to any of these.

1. Do the seven paste-ready appends in `method/plan-review-2-2026-09-23.md` §8 (a–g, L104–112) go into `method/plan.md`?
2. Does Pass 10 sampling reopen, and under which vantage — logged-in or logged-out, which region or egress? No raw file records a US egress path (`method/plan-review-2-2026-09-23.md` L59).
3. Which Silver count governs reading: 7 as the censuses graded, or 1 under grading rule 1 read literally?
4. Which sub-market does the hypothetical product target — organic, paid, agentic, or more than one?
5. Does the builder-constraint question — "which of the gaps above, if any, is reachable by a team whose cost advantage is engineering rather than distribution?" — return to scope (`findings/whitespace.md` L52)?

## 14. Confidence and caveats

- Research only. This file names no verdict, no prescription and no sequencing; the call is the owner's (`MegaPlan.md` §Non-goals).
- The tier-3 shortfall is structural: every load-bearing claim below tier 3 is a Lane E case claim or a tier-6 forecast (`findings/unknowns.md` L62; `method/plan-review-2-2026-09-23.md` L32).
- Survivorship: published cases are winners; full-page re-grading moved 12 up and 0 down (`findings/proof-scorecard.md` L71, L81).
- Self-reports throughout: prices, customer counts, funding and cases are vendor or company statements, none independently audited.
- Measured by us: only the partial day-0 panel and our own screen counts; the panel is one date, one localised network path.
- Conflicts kept side by side, never averaged: 68.0% / 44.4%; Silver 7 / 1; Jerry Bronze / Silver; H5, H6, H11, H15, H16 marks; ChatGPT ad presence 26% / 4.47% / 0.00%; Peec AI ARR $4M / $10M; geoSurge $12M / €10M; Scrunch deal undisclosed / $225M; `none` / `blank` compiler rules; skincare agentic spend / attention.
- Absence is only as strong as the channels listed in section 12; `findings/whitespace.md` L85 names five blocked, `findings/unknowns.md` L84–93 lists more rows — both stand.
- Every pull dated 2026-09-22; the category turns over fast, and a pull older than one quarter is re-checked before citation (`method/plan.md` §Staleness rule). Profiles go stale 2026-12-22 (`competitors/INDEX.md` L58).
- Forecasts appear only as forecasts, with tiers; none is used as a size.

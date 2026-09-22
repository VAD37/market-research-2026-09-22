# Demand-signal census — skincare and beauty (P8-c1-sk)

```yaml
source:          this cluster's own compilation of the ten f-signal-sk-* raw pulls below, plus cross-reference to four already-landed vendor-census files and six already-landed conference-agenda files
url_or_doc_id:   n/a — census document
published:       n/a
pull_date:       2026-09-22
pull_method:     manual compilation
pull_purpose:    evidence about a number
tier:            n/a — this file assigns no new tier; each cited cell carries the tier of its own raw file
source_label:    n/a — mixed, per cited raw file
lane:            F, E
sub_market:      organic recommendation, paid placement, agentic commerce — all three, per row
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        nine-cell × twelve-signal matrix; signal-by-signal query/result log; spend/attention tally; unknowns
```

Vertical: skincare and beauty. Hypotheses moved: H4, H7, H9. Cell-read rule, tiers, and signal catalogue are `docs/method/demand-signals.md`'s. This file provides the checked/blank/none marks only — **no spend/attention/none cell-read verdict is assigned here**; that is Pass 8's compile job.

## Raw pulls this cluster produced

| Signal | File | Tier | One-line result |
|---|---|---|---|
| S1 | `docs/raw/f-signal-sk-S1-jobs-linkedin-indeed-upwork-freelancer-2026-09-22.md` | 3 | E.L.F. BEAUTY: named AEO/GEO team + "AI Product Owner, Agentic Commerce" role, $110-140K base pay, Enterprise. Indeed and Upwork blocked |
| S4 | `docs/raw/f-signal-sk-S4-omr-reviews-2026-09-22.md` | 5 | OMR/Rankscale.ai reviewer, Industry: Cosmetics, 1-50 employees (SMB). G2, Capterra blocked both ways |
| S5 | `docs/raw/f-signal-sk-S5-hn-algolia-reddit-2026-09-22.md` | 4 | No beauty-specific practitioner thread found. reddit.com blocked (403) |
| S6 | `docs/raw/f-signal-sk-S6-gr0-agency-case-studies-2026-09-22.md` | 6 | GR0 agency: dedicated "GEO" service line, named luxury-skincare-brand case study (client unnamed, size unassigned) |
| S7 | `docs/raw/f-signal-sk-S7-coty-10k-2026-09-22.md` | 2 | Coty Inc. 10-K names "generative engine optimization" directly; 11,335 employees (Enterprise). Estee Lauder, elf Beauty, Ulta Beauty, Inter Parfums: zero hits |
| S8 | `docs/raw/f-signal-sk-S8-conference-agendas-2026-09-22.md` | 3 | Zero beauty-tagged sessions across 6 already-landed P4-c3 conference files |
| S9 | `docs/raw/f-signal-sk-S9-google-trends-2026-09-22.md` | 4 | "AI visibility beauty" average index 1 of 100 (US, 12mo) — negligible |
| S10 | `docs/raw/f-signal-sk-S10-procurement-2026-09-22.md` | 5 | sam.gov and Contracts Finder both non-phrase-matching, no genuine record; TED 405 (confirmed) |
| S11 | `docs/raw/f-signal-sk-S11-price-paid-2026-09-22.md` | 2 | 35 EDGAR entityName×vendor sweeps, no confirmed price-paid figure |
| S12 | `docs/raw/f-signal-sk-S12-llms-txt-beauty-domains-2026-09-22.md` | 1 | 3 of 5 beauty domains (elfbeauty.com, sephora.com, lorealparisusa.com) serve genuine llms.txt |

S2 and S3 are **not** freshly pulled by this cluster (per task scope); read-only against already-landed files: `docs/raw/a-vendor-census-c1-2026-09-22.md`, `a-vendor-census-c2-2026-09-22.md`, `a-vendor-census-c3-2026-09-22.md`, `a-vendor-census-c4-2026-09-22.md` — grepped for beauty/skincare/cosmetics brand names and vendor customer/logo rosters; **zero matches** in all four files (checked 2026-09-22).

## Nine-cell matrix

`checked — <finding> (tier)` / `blank — unattributed` (a signal exists but the source names no buyer-size band, or the signal kind does not apply to that sub-market) / `none — checked <channels> 2026-09-22` (checked, nothing found).

### Organic recommendation / SMB

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | checked — Rankscale.ai reviewer, GEO Consultant at Marcvs Group, Industry: Cosmetics, 1-50 employees, "In the last 6 months" (5) | none | blank — unattributed (GR0 case names no client/size) | none | none | none | none | none | blank — unattributed (no SMB beauty domain in the 5 checked) |

### Organic recommendation / Mid-market

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | none | none | blank — unattributed | none | none | none | none | none | blank — unattributed (no mid-market beauty domain in the 5 checked) |

### Organic recommendation / Enterprise

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| checked — E.L.F. BEAUTY posting names an in-house "AEO (Answer Engine Optimization) and GEO (Generative Engine Optimization) team"; company states net sales $1.6B FY26 (3) | none | none | none | none | blank — unattributed | checked — Coty Inc. 10-K: "deploying improvements across touchpoints to drive generative engine optimization"; 11,335 employees per same filing (2) | none | none | none | none | checked — elfbeauty.com, sephora.com, lorealparisusa.com serve genuine llms.txt; all three enterprise-scale (1) |

### Paid placement / SMB

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | blank — unattributed (no paid-placement tool review category checked this pull) | none | blank — unattributed (no paid-placement agency page checked for beauty this pull) | none | none | none | none | none | blank — unattributed (S12 measures organic on-property artifacts by definition) |

### Paid placement / Mid-market

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | blank — unattributed | none | blank — unattributed | none | none | none | none | none | blank — unattributed |

### Paid placement / Enterprise

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | blank — unattributed | none | blank — unattributed | none | none | none | none | none | blank — unattributed |

### Agentic commerce / SMB

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | blank — unattributed | none | blank — unattributed | none | none | none | none | none | blank — unattributed |

### Agentic commerce / Mid-market

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | blank — unattributed | none | blank — unattributed | none | none | none | none | none | blank — unattributed |

### Agentic commerce / Enterprise

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| checked — E.L.F. BEAUTY "AI Product Owner, Agentic Commerce" posting, base pay $110,000–$140,000/yr disclosed, 116 applicants, 2 weeks old (3) | none | none | blank — unattributed | none | blank — unattributed | none | none | none | none | none | blank — unattributed |

## Signal-by-signal query and result log

**S1 — job postings.** LinkedIn (`linkedin.com/jobs/search/?keywords=...`), four queries: `generative engine optimization beauty`; `"generative engine optimization" beauty`; `"AEO" OR "GEO" skincare OR beauty OR cosmetics`; `GEO specialist skincare small business` — all returned LinkedIn's saturation count ("4,000+" to "10,000+"), confirmed token-OR matching, not exact phrase. One genuinely on-topic full posting opened: E.L.F. BEAUTY "AI Product Owner, Agentic Commerce". Indeed (`indeed.com/jobs?q="generative engine optimization" beauty&l=`): "Blocked - Indeed.com" under the browser extension. Upwork (`upwork.com/nx/search/jobs/?q=generative engine optimization beauty`): Cloudflare challenge, not cleared. Freelancer.com GEO category page: 1 job total, Web3/crypto, not beauty. Freelancer.com keyword search `AI visibility beauty`: 352 jobs, top result unrelated (gaming app).

**S4 — review velocity.** G2 (`g2.com/categories/ai-search-visibility`): 403 to plain fetch; blocked (empty body) under browser extension too. Capterra (`capterra.com/p/ai-search-visibility/`): 403 to plain fetch, not retried via extension. OMR category page (`omr.com/en/reviews/category/generative-engine-optimization-geo`): extension-free 200, 20 products with review counts. Three products' review sections opened via browser (JS-hydrated): Rankscale.ai (26 reviews, 15 rendered, 1 Cosmetics-industry hit), Otterly.AI (56 reviews, 15 rendered, 0 beauty hits), Peec AI (18 reviews, 15 rendered, 0 beauty hits, 2 "Consumer Goods" unmapped).

**S5 — community threads.** HN Algolia (`hn.algolia.com/api/v1/search`), eight queries run (`generative engine optimization beauty` nbHits 1; `AI visibility beauty` nbHits 16, one vendor Show-HN, not beauty-specific; `GEO skincare` nbHits 1934, confirmed noise; `skincare AEO` nbHits 113; `cosmetics LLM visibility` nbHits 0; `beauty brand ChatGPT recommendation` nbHits 0; `"GEO manager" beauty` nbHits 0; `"answer engine optimization" skincare` nbHits 0). reddit.com: `r/SkincareAddiction/search.json` and `r/beauty/.json`, both HTTP 403.

**S6 — agency pages.** `gr0.com/case-studies/` (extension-free 200): 6 beauty/skincare case-study titles found by grep; one opened in full (`gr0.com/case-study/luxury-skincare-brand`) naming Profound as the tracking tool, no client name, no price. `gr0.com/pricing`: JS-rendered, no price text extracted by static fetch.

**S7 — earnings/filings.** EDGAR full-text search (`efts.sec.gov/LATEST/search-index`), `entityName`-scoped to Estee Lauder, elf Beauty, Ulta Beauty, Coty Inc, Inter Parfums, each queried across the O alias set (10 terms) — only "Coty Inc" × "generative engine optimization" hit (1 of 1). Cross-referenced against already-landed `docs/raw/e-case-census-c1-2026-09-22.md` (P4-c1), whose own targeted query `q="AI Overviews" (skincare OR beauty OR cosmetics)` over 8-K/10-Q/10-K, 2025-01-01 to 2026-09-22, returned 6 hits, all IAC/Yelp, zero beauty filers — corroborates the near-total absence found independently by this cluster.

**S8 — conference agendas.** Re-check (grep) of six already-landed P4-c3 files: ANA, brightonSEO, Content Marketing World 2026, GEO Conference, MozCon, SMX. Zero beauty/skincare/cosmetics session titles. MozCon and SMX carry unmapped "E-Commerce"/"Retail" tracks.

**S9 — search interest.** Google Trends (`trends.google.com/trends/explore`), browser-only, US region, past 12 months: `AI visibility beauty` vs `generative engine optimization`. Average index 1 vs 49; beauty-specific term's "Related queries" panel returned "not enough data."

**S10 — procurement.** sam.gov internal search API: 5 queries, all returning implausible five/six-figure `totalElements` (non-phrase-matching, unusable). Contracts Finder (`contractsfinder.service.gov.uk/Search/Results?Keywords=...`): "AI visibility" beauty → 675 notices, top 10 titles all irrelevant (energy, defense, bedding plants). TED (`ted.europa.eu`): 405 to plain GET, confirmed per task brief.

**S11 — price paid.** 35 EDGAR `entityName`×vendor-name queries (5 beauty filers × 7 named AI-visibility vendors: Profound, Scrunch, Otterly, Ahrefs, Semrush, Peec, Rankscale). Two non-zero, both "Profound" (likely the common English word, not the vendor; not resolved — Estee Lauder ×3, Ulta Beauty ×1, one hit dated 2025-01-06 opened and not further pursued). Cross-referenced against S6 (GR0/Profound case study, no price), S4 (Rankscale.ai's own list price, not a price paid), S7 (Coty 10-K, no price).

**S12 — on-property artifacts.** Five domains checked twice (no-UA/no-redirect, then browser-UA/redirects-followed): elfbeauty.com (200/200, genuine), esteelauder.com (200-soft-404 body / 403 Akamai), sephora.com (404/200, genuine), ulta.com (403/200-but-generic-error-page, not genuine), lorealparisusa.com (404/200, genuine). Six bonus domains spot-checked, not in the five-domain sample: glossier.com, rarebeauty.com, maccosmetics.com (all genuine), drunkelephant.com (410), charlottetilbury.com (200, not genuine), theordinary.com (404).

## Spend-class vs attention-class tally per cell

Per `demand-signals.md`: S1, S2, S3(ARR only), S4(purchase-verified only), S7(named figure only), S10, S11 are spend-class; S3(round), S4(unverified), S5, S6, S7(no figure), S8, S9, S12 are attention-class. This cluster assigns no cell-read verdict — the tally below is descriptive only, for Pass 8 compile's use.

| Cell | Spend-class signals found | Attention-class signals found | Tier of strongest |
|---|---|---|---|
| Organic / SMB | 0 | 1 (S4, tier 5 — Validated Reviewer, not confirmed purchase) | 5 |
| Organic / Mid-market | 0 | 0 | — |
| Organic / Enterprise | 2 (S1 tier 3, S7 tier 2 — both below the tier-5 spend floor, so each counts as attention for any cell-read per the cell-read rule) | 1 (S12, tier 1) | 1 |
| Paid placement / SMB, Mid-market, Enterprise | 0 | 0 | — |
| Agentic commerce / SMB, Mid-market | 0 | 0 | — |
| Agentic commerce / Enterprise | 1 (S1 tier 3, below the tier-5 spend floor, counts as attention for the read) | 0 | 3 |

Note: S1 and S7's Enterprise findings are catalogue-class "spend" but their pulled tier (3 and 2 respectively) sits below the tier-5 floor the cell-read rule sets for a spend verdict — per `demand-signals.md`, "A spend-class signal below tier 5 counts as attention for the read, and is still recorded at its own tier and class." Both are recorded above at their own class (spend) and tier, with this caveat carried forward for Pass 8.

## Unknowns per channel

| Channel | Status | Date |
|---|---|---|
| indeed.com | Blocked under both plain fetch (403) and browser extension ("Blocked - Indeed.com" interstitial) | 2026-09-22 |
| upwork.com | Blocked under both plain fetch (403) and browser extension (Cloudflare challenge, not cleared after 4s wait) | 2026-09-22 |
| g2.com | Blocked under both plain fetch (403) and browser extension (empty DOM body) | 2026-09-22 |
| capterra.com | Blocked under plain fetch (403); browser-extension retry not attempted this pull | 2026-09-22 |
| reddit.com | Blocked (403) on subreddit JSON endpoints; task brief marks this unreachable for the session | 2026-09-22 |
| sam.gov | Documented public UI not independently confirmed searchable; internal JSON API found but does not honor phrase queries, unusable for a precision result | 2026-09-22 |
| ted.europa.eu | 405 to plain GET on the documented search path; one alternate path resolved to a "Page not found" page; no working REST endpoint found | 2026-09-22 |
| EDGAR "Profound" hits (Estee Lauder ×3, Ulta Beauty ×1) | Not opened/resolved — ambiguous between the AI-visibility vendor and the common English word | 2026-09-22 |
| Beauty-industry-specific trade conferences (Cosmoprof, IBS/PBA, etc.) | Not searched by this cluster or by P4-c3 — recorded as unchecked, not as none, for S8 | 2026-09-22 |

## Caveats

- No cell-read verdict (spend / attention / none) is assigned in this file — that is Pass 8's compile job per the task brief. This file provides checked-or-blank-or-none marks with tiers and classes only.
- LinkedIn's displayed job-search result counts ("4,000+" etc.) are confirmed saturation displays, not literal counts, across every query run this pull — see `f-signal-sk-S1-*`.
- Two genuinely strong findings this pull (E.L.F. BEAUTY's named AEO/GEO team and agentic-commerce product role; Coty Inc.'s 10-K "generative engine optimization" passage) are both Enterprise-banded and both sit below the tier-5 floor the cell-read rule requires for a spend verdict, despite both being catalogue-class "spend" signals (S1, S7) — this is the single most load-bearing nuance for Pass 8 to carry forward on H7 and H9.
- SMB and Mid-market cells across all three sub-markets are thin: the one SMB signal found (S4, Rankscale.ai/Cosmetics reviewer) is attention-class by its verification status, and no Mid-market cell carries any signal in any sub-market from this pull.
- Publication bias runs one way (per `demand-signals.md`): a `none` mark here is weaker evidence than a `checked` mark — quiet SMB/mid-market beauty spend on AI-visibility tooling would leave little public trace under any of these channels.
- G2 and Capterra — the two highest-tier-expectation review channels for S4 (tier 5) — were both fully blocked; the S4 finding rests entirely on OMR, a DACH-weighted corpus (`channels.md` C65's own stated bias), and the one qualifying reviewer's employer (Marcvs Group) was not independently verified as a beauty-industry company beyond OMR's own "Industry: Cosmetics" field.

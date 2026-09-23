# Demand map — the 27-cell segment matrix

| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every `raw/` file cited. Oldest source publication carried: 2025-06-03 (HN thread title), via `customers/b2b-saas.md`; oldest load-bearing 2026-01-11, `raw/c-google-ucp-merchant-agentic-2026-09-22.md`, via `customers/skincare-beauty.md` |
| Lane | F, with A, B and C feeding it |
| Hypotheses touched | H4, H7, H9 — scored below; full register in `unknowns.md` |
| Claims at tier 3 or better | 5 of 7 |

## Question

> Which of the 27 sub-market × vertical × buyer-size cells show a spend signal, which show only attention, and which were checked and found empty?

## Answer

None of the three metrics: this file reads demand signals, not visibility, traffic or sales. Seven of 27 cells read **spend**, one **attention**, eleven **none — checked**, eight **blank** (not checked). Willingness to pay is `unknown` in all 27.

## Evidence

Reads carried verbatim from the three `customers/` files. Floor per `method/demand-signals.md`: spend needs a spend-class signal at tier 5 or better **for that exact cell** (tiers 1–5; lower is better).

| # | Vertical | Sub-market | Size | Read | Deciding signal, figure verbatim | Tier | Compiled file |
|---|---|---|---|---|---|---|---|
| E1 | Skincare | Organic | SMB | attention | S4 — one OMR reviewer, "GEO Consultant at Marcvs Group", "1-50 employees", "Industry: Cosmetics"; identity-checked, not purchase-verified | 5 | `customers/skincare-beauty.md` |
| E2 | Skincare | Organic | Mid | none — checked | 10 of 12 signals checked, nothing attributable to this cell | — | same |
| E3 | Skincare | Organic | Enterprise | **spend** | S1 — e.l.f. Beauty posting names an in-house "AEO … and GEO … team" | 3 | same |
| E4 | Skincare | Paid + Agentic | SMB, Mid | none — checked ×4 | 9 of 12 signals each; S4, S6, S12 never run against paid or agentic | — | same |
| E5 | Skincare | Paid | Enterprise | **spend** | S2 — Google names e.l.f. Cosmetics a Direct Offers pilot collaborator, unit labeled "Sponsored deal" | 3 | same |
| E6 | Skincare | Agentic | Enterprise | **spend** | S1 — e.l.f. "AI Product Owner, Agentic Commerce", "$110,000.00/yr - $140,000.00/yr", 116 applicants | 3 | same |
| E7 | B2B SaaS | Organic | SMB | **spend** | S1 — Actindo, 52–70 employees, "Du unterstützt SEO- und GEO-Maßnahmen" | 3 | `customers/b2b-saas.md` |
| E8 | B2B SaaS | Organic | Mid | **spend** | S1 — AutoLeap "SEO Lead", 199–225 employees | 3 | same |
| E9 | B2B SaaS | Organic | Enterprise | **spend** | S1 — Pennylane "More than 1,100 Pennylaners"; Mercury 1,001–5,000 | 3 | same |
| E10 | B2B SaaS | Paid + Agentic | all three | none — checked ×6 | 9 of 12 signals each; S5 and S6 run with organic-alias terms only | — | same |
| E11 | High-CPA | Organic | Enterprise | **spend** | S1 — The Cigna Group, "Lead Analyst, Technical Search (SEO/AEO/GEO)"; band is the word "Enterprise", no figure | 3 | `customers/high-cpa-regulated.md` |
| E12 | High-CPA | Organic SMB/Mid; Paid + Agentic all three | — | blank ×8 | S2, S3, S9 unchecked, S10 part-unresolved; no source states an SMB or mid-market band, and the one agentic signal (S8, John Lewis Financial Services) states none either | — | same |

### The two compilers' treatments of a partial check — side by side, not reconciled

| Compiler | Rule applied | Result |
|---|---|---|
| `customers/skincare-beauty.md`, `customers/b2b-saas.md` | `none — checked` where 9 or 10 of 12 signals ran and returned nothing, shortfall itemised | 11 cells read `none` |
| `customers/high-cpa-regulated.md` | `blank` wherever any catalogue signal went unchecked — "a blank is never written as `none`" | 8 cells read `blank` |

`demand-signals.md`'s `none` condition reads strictly ("Every catalogue signal checked, nothing found"). Two compilers applied one rule two ways on the same day. Both stand, neither adjusted (`STATE.md` §Decisions). Under the strict rule the 11 `none` reads become `blank`; under the loose one the 8 `blank` reads become `none — checked`. 19 of 27 cells turn on this.

### Tallies — sub-market rows, then buyer-size rows

| Axis | spend | attention | none | blank |
|---|---|---|---|---|
| Organic recommendation | 5 | 1 | 1 | 2 |
| Paid placement | 1 | 0 | 5 | 3 |
| Agentic commerce | 1 | 0 | 5 | 3 |
| SMB | 1 | 1 | 4 | 3 |
| Mid-market | 1 | 0 | 5 | 3 |
| Enterprise | 5 | 0 | 2 | 2 |

**Willingness to pay:** `unknown` in all 27. Channels: EDGAR ×35 entity×vendor sweeps, OMR, gr0.com, lite.duckduckgo.com, vendor pricing pages, the Pass-4 case files — `raw/f-signal-sk-S11-price-paid-`, `-bs-S11-`, `-hr-S11-2026-09-22.md`. No buyer in any vertical discloses a price paid. Excluded by rule: list prices (Semrush +$60/mo, Pace $1,499–$2,499, Rankscale €20/mo) are asking prices, and salary bands (e.l.f. $110–140K, Simply Business $114,700–$189,200) are internal headcount cost.

### Hypotheses scored from this matrix

| H | Condition | Reading | Mark |
|---|---|---|---|
| H4 — attention-only in every SMB cell | kill: any SMB cell with a spend signal | B2B SaaS organic × SMB reads spend on E7 — S1, spend class, tier 3, above the tier-5 floor. Confirm also fails: 3 SMB cells read blank | **killed** |
| H7 — organic carries spend in more cells than paid or agentic | both conditions require **all 27 cells checked** | Organic 5 against paid 1 and agentic 1; 8 cells read blank, so neither condition is reachable | **unresolved — checked** |
| H9 — agentic spend in enterprise, absent from SMB | confirm requires all 6 agentic SMB + enterprise cells checked | Skincare agentic × enterprise spend (E6); no agentic SMB cell spends; 2 of the 6 read blank | **unresolved — checked** |

Channels behind both `unresolved` marks, 2026-09-22: LinkedIn guest API, Indeed, Upwork, Freelancer, vendor censuses c1–c4 and c6, G2, Capterra, OMR, EDGAR full-text, HN Algolia, reddit.com, 6–9 conference agendas, Google Trends, sam.gov, Contracts Finder, TED, DuckDuckGo HTML. H4's kill rests on a rule application the source censuses read the other way: `raw/f-signal-census-bs-2026-09-22.md` and `-sk-` marked the same tier-3 postings **attention**, reading the tier-5 floor as an upper bound. Both readings sit here; the `customers/` files apply `demand-signals.md` literally. Not averaged.

**Done-condition row — "Segment matrix" (bar: every cell reads spend, attention, or none, with signals behind it): not satisfied.** 19 of 27 cells do; 8 high-CPA cells read `blank`, which `demand-signals.md` defines as not-yet-checked and forbids writing as `none`. The shortfall is S2, S3, S9 and two thirds of S10 in that vertical.

## Claims

| # | Claim | Evidence | Tier of weakest row | Grade | Load-bearing |
|---|---|---|---|---|---|
| C1 | 7 of 27 cells read spend, 1 attention, 11 none — checked, 8 blank | E1–E12 | 5 | n/a | yes |
| C2 | Six of the seven spend reads rest on S1 job postings, the catalogue's own weakest spend class | E3, E6, E7, E8, E9, E11 | 3 | n/a | yes |
| C3 | Willingness to pay is unknown in all 27 cells; no buyer anywhere discloses a price paid | willingness-to-pay block | 3 | n/a | yes |
| C4 | Organic carries 5 spend cells against 1 each for paid and agentic | tallies | 3 | n/a | yes |
| C5 | 5 of the 7 spend cells are enterprise; exactly 1 of 9 SMB cells reads spend | tallies | 3 | n/a | yes |
| C6 | Two compilers applied the `none` rule differently on the same day; the difference moves 19 of 27 reads | side-by-side table | n/a — compiled files only, no raw/ | n/a | yes |
| C7 | Skincare agentic × enterprise reads spend in `customers/` and attention in `markets/agentic-commerce.md`; both stand | E6 | 3 | n/a | no |

## Survivorship

Not case-based — survivorship does not apply; the proof counts inside `customers/` are carried in `proof-scorecard.md`, stated once there.

## Unknowns

| Question | Channels checked | Date | Why not answerable here |
|---|---|---|---|
| Any SMB or mid-market posting naming GEO/AEO that LinkedIn's non-phrase-strict guest API missed; review velocity and reviewer industry for any AI-visibility tool | indeed.com (403 / "Blocked"), upwork.com (Cloudflare), freelancer.com (JS shell), g2.com (403, empty DOM, DataDome), capterra.com (403), omr.com (reached — DACH-weighted, industry undisclosed) | 2026-09-22 | the two boards carrying SMB hiring were blocked both ways, and S4 rests on one corpus that does not expose buyer size |
| Practitioner thread volume, absolute search volume per vertical, and any procurement award naming the category | reddit.com (403), hn.algolia.com (15 queries), trends.google.com (relative index only, token-gated), sam.gov (phrase queries not honoured), contractsfinder (filter non-functional), ted.europa.eu (405) | 2026-09-22 | one channel blocked, one publishes no absolute count, three returned untrusted results rather than zero |
| S2, S3, S9 per cell in high-CPA; S5, S6 with paid- and agentic-framed terms in B2B SaaS | vendor roster only; Trends not reached; those sweeps never run | 2026-09-22 | unrun, so the cells stay blank |

## Caveats

- Every read is an internet-only proxy; no signal observes a budget (`scope.md` R2). A `spend` cell evidences that money moved somewhere in it, never how much. C1, C2, C4 and C5 are load-bearing and rest on one signal class, S1, whose catalogue bias reads "lags spend; large firms over-represented… headcount budget, not category spend — weakest spend class". Three of four B2B SaaS headcounts come from third-party data-vendor snippets read via search result, not opened; AutoLeap's sources conflict at 199 and 225 against a "51-200" band straddling the SMB / mid-market boundary — recorded, not averaged.
- C1 is tier 5 through E1; C6 carries no raw tier; no metric crossing is relied on. Publication bias runs one way: quiet spending leaves no public trace, so `none` and `blank` are weaker evidence than `spend`; SMB and mid-market is where that bites hardest, and every channel that could have caught them was blocked this session. The buyer-size bands are a method choice fixed 2026-09-22, not a fact about how this market segments itself; a market that cuts differently is mis-cut here invisibly. One raw file was edited after creation — `raw/f-signal-sk-S7-coty-10k-2026-09-22.md`, headcount added post-landing to band a cell. The oldest pull cited is 2026-09-22; no cited pull is stale under `method/plan.md`. This file carries evidence, not a verdict.
- Amended 2026-09-23 per `findings/review-1-2026-09-23.md` §9; both readings stand where the review and the original disagree.

### Pass 8 re-run, 2026-09-23

Task P8-r. Closes the eight high-CPA blanks (S2, S3, S9, S10) and the eleven partial-`none` cells (skincare Paid/Agentic × SMB/Mid, S4/S6/S12; B2B SaaS Paid/Agentic × all three sizes, S5/S6 paid- and agentic-framed). Source: `customers/high-cpa-regulated.md`, `customers/skincare-beauty.md`, `customers/b2b-saas.md`, all §"Pass 8 re-run, 2026-09-23".

**Cells restated, old → new:**

| # | Cell | Old (2026-09-22) | New (2026-09-23) | Deciding change |
|---|---|---|---|---|
| E2 | Skincare, Organic, Mid | none — checked (10 of 12) | none — checked (unchanged; **out of this pass's scope** — S6, S12 still blank there) | not touched |
| E4 | Skincare, Paid+Agentic, SMB/Mid (×4) | none — checked (9 of 12 each) | none — checked (**12 of 12**, S4 and S12 now `n/a` by construction, S6 checked-unattributed) | `raw/f-signal-sk-S6-*-2026-09-23.md` |
| E10 | B2B SaaS, Paid+Agentic, all three (×6) | none — checked (9 of 12 each) | none — checked (**12 of 12**, S5 zero via HN Algolia API, S6 checked-unattributed or none) | `raw/f-signal-bs-S5-S6-paid-agentic-2026-09-23.md` |
| E11 | High-CPA, Organic, Enterprise | spend (S1, Cigna only) | **spend, reinforced** — GEICO, Amica, Juice Plus+ (S1); Zurich UK, Hartford, Aetna, MidFirst Bank (S2); Primerica, Mutual of Omaha, Franklin Templeton (S7/S8) all now band Enterprise | `raw/f-signal-hr-band-attribution-2026-09-23.md` |
| E13 | High-CPA, Organic, Mid-market | blank | **spend** — Embrace Pet Insurance (201 emp.), Insurify (166–242 emp.), Simply Business (850 emp.), all S1, tier 3, Mid-market by headcount | same |
| E14 | High-CPA, Organic, SMB | blank | none — checked (loose) / **blank** (strict, S10/TED) | `raw/f-signal-hr-S2-paid-agentic-check-2026-09-23.md`, `-S9-repull-`, `-S10-repull-2026-09-23.md` |
| E15 | High-CPA, Paid, all three sizes (×3) | blank | none — checked (loose) / **blank** (strict, S10/TED) | same three raw files |
| E16 | High-CPA, Agentic, all three sizes (×3) | blank | none — checked (loose) / **blank** (strict, S10/TED); John Lewis Financial Services (S8) stays `unassigned` — a division, no independent band found, parent John Lewis Partnership (~74,000) not applied | same |

### Tallies — restated, both readings, 27 cells

| Reading | spend | attention | none | blank |
|---|---|---|---|---|
| **Strict** (every catalogue signal, incl. a still-blocked one, must be checked) | 8 | 1 | 10 | 8 |
| **Loose** (a channel blocked-and-logged today counts as checked, per this file's and `customers/`'s existing convention) | 8 | 1 | 18 | 0 |

Strict-closed cells (spend+attention+none) rise from 8 of 27 to **19 of 27**; strict blanks fall from 19 to **8**. Of the original 8 high-CPA blanks: 1 closes to spend under the strict reading (E13); all 8 close under the loose reading (7 to none, 1 to spend). Loose reading was already reachable by relabeling before this pass (review-1 §5); it is now reachable by evidence — every cell it counts as `none` rests on a signal actually run or a channel actually retried and logged in `blocked-channels.md`, not a reinterpretation of an unrun signal.

**Done-condition row — "Segment matrix" restated:** bar is every cell spend/attention/none with signals behind it. **Loose: satisfied, 27 of 27. Strict: not satisfied, 19 of 27** — 8 cells remain blank, all resting on one channel each: TED's human-verification wall (6 high-CPA cells) and skincare Organic/Mid's unrun S6/S12 (1 cell, out of this pass's scope) plus a corollary count — see caveats.

### Hypotheses re-scored

| H | Condition | New reading | Mark |
|---|---|---|---|
| H4 | kill: any SMB cell with spend | Unchanged — B2B SaaS Organic/SMB is still the only SMB spend cell. Today's high-CPA band pass found six named SMB-candidate employers and banded zero of them SMB (three Mid-market, three Enterprise) — reinforces, does not overturn | **killed** (unchanged, reinforced) |
| H7 | organic > paid, > agentic in spend-cell count; confirm/kill need all 27 checked | Organic 6 (skincare 1, B2B SaaS 3, high-CPA 2) against paid 1 and agentic 1. **Loose: confirmed** — all 27 cells checked, organic strictly ahead of both. **Strict: unresolved — checked** — 8 cells still blank, condition unreachable | **confirmed (loose) / unresolved — checked (strict)** — both stand, not merged |
| H9 | confirm: agentic spend only at enterprise, never at SMB; needs all 6 agentic SMB+enterprise cells checked | The 6 cells: skincare Agentic/SMB none, /Enterprise spend; B2B SaaS both none; high-CPA both none (loose) / both blank (strict). Agentic spend exists at exactly one cell, and it is enterprise. **Loose: confirmed.** **Strict: unresolved — checked** — high-CPA's two agentic cells still blank | **confirmed (loose) / unresolved — checked (strict)** — both stand |

Full register, both marks beside the 2026-09-22 originals: `findings/unknowns.md` §"Pass 8 re-run, 2026-09-23".

### Caveats, this append

- The strict/loose duality is unchanged in kind from `review-1-2026-09-23.md` §5 — only the count of cells it applies to shrank, from 19 partial/blank cells to 8. The 8 remaining strict blanks are not evenly weak: 6 rest on one still-blocked channel (TED, `blocked-channels.md`), and the 7th component in those same 6 (UK Contracts Finder) returned a result but with a non-functional keyword filter — an untrusted zero, not a clean one. The 8th, skincare Organic/Mid-market, was never in this pass's scope.
- H7's and H9's `confirmed` marks hold only under the loose reading's convention that a retried-and-logged-blocked channel counts as checked; a reader who rejects that convention should read both as `unresolved — checked`, unchanged from 2026-09-22.
- No band in this append rests on a guess: every Mid-market or Enterprise assignment traces to a headcount figure in `raw/f-signal-hr-band-attribution-2026-09-23.md`, and one candidate promotion (John Lewis Financial Services via its parent's headcount) was deliberately not applied, recorded instead as a named possibility.
- Willingness to pay is unchanged: `unknown` in all 27 cells; this pass found no price paid in any new pull.
- File now 145 lines against the 100-line `finding.md` budget; overrun is this append.

### R-BLOCKED-2, 2026-09-23

Re-probe of TED, Indeed and Reddit. Compiled source: `customers/high-cpa-regulated.md` §R-BLOCKED-2; `findings/ai-ads-evidence.md` §R-BLOCKED-2. Raw: `raw/f-ted-S10-repull2-`, `f-indeed-S1-repull2-`, `f-reddit-S5-counts-repull2-`, `b-reddit-advertiser-reports-repull2-2026-09-23.md`.

**Cells whose read changes:**

| # | Cell | Before (strict / loose) | Now (strict / loose) | Deciding change |
|---|---|---|---|---|
| E14 | High-CPA, Organic, SMB | blank / none | none — checked / none | TED reached; no SMB buyer in vertical |
| E15 | High-CPA, Paid, all three (×3) | blank / none | none — checked / none | TED 0 on paid terms |
| E16 | High-CPA, Agentic, all three (×3) | blank / none | none — checked / none | TED 0 in vertical; John Lewis FS still unassigned |
| E11 | High-CPA, Organic, Enterprise | spend / spend | spend / spend, reinforced | S10 KKH, 11,000,000.00 EUR framework, tier 2 |

**Tallies, 27 cells:**

| Reading | spend | attention | none | blank |
|---|---|---|---|---|
| Strict | 8 | 1 | 17 | 1 |
| Loose | 8 | 1 | 18 | 0 |

Segment-matrix done row: loose met, 27 of 27; strict 26 of 27. Strict blank left: E2, skincare Organic/Mid-market — S6, S12 unrun there; not in this task's channels.

**Hypotheses.** H9 strict: unresolved — checked → **confirmed**; both readings now confirmed. H7 strict: unresolved — checked, unchanged, resting on E2 alone. H4: killed, unchanged — no SMB spend signal found.

**Signals found, no cell moved (size unstated):**

| Signal | Observation | Vertical, sub-market | Tier |
|---|---|---|---|
| S11 buyer-stated spend | DTC supplement brand, Spain: "€37.61", "0 conversions" | High-CPA, Paid | 5 |
| S11 buyer-stated spend | marketing SaaS, ZapDigits, SaaS free tier, developer software | B2B SaaS, Paid | 5 |
| S10 filed | JLU Gießen, visitBerlin, BIÖG, An Post, NRW.BANK, KfW | public sector / lending, outside verticals | 2 |
| S1 postings | 35 Indeed cards, none banded | mixed, unassigned | 3 |
| S5 threads | 9 subreddits, Mar–Sep 2026, no vertical term | vertical-level only | 5 |

The B2B SaaS Paid rows sit beside that vertical's `none — checked` Paid reads (E10), attributed, not merged: sub-market and vertical are source-stated, buyer size is not.

**S5 counts, nine subreddits summed (r/SaaS timed out), threads per month Mar → Sep-to-23:**

| Query sent | Mar | Apr | May | Jun | Jul | Aug | Sep | Total |
|---|---|---|---|---|---|---|---|---|
| `"generative engine optimization"` | 12 | 9 | 22 | 15 | 9 | 8 | 3 | 78 |
| `GEO` | 155 | 177 | 151 | 141 | 102 | 72 | 66 | 864 |
| `"AI visibility"` | 58 | 61 | 53 | 44 | 45 | 36 | 23 | 320 |
| `AEO` | 57 | 76 | 75 | 63 | 55 | 39 | 34 | 399 |

r/SEO carries most: `GEO` 525 threads, 418 unique authors; `AEO` 259 / 210; `"AI visibility"` 168 / 140. Unique posters are per window only. `GEO` includes geo-targeting noise. Attention class; moves no cell.

**Caveats, this append.** Strict `none` reads on seven high-CPA cells rest on TED (EU public buyers only) plus earlier channels; private demand stays invisible there. Reddit counts are an archive's, held at tier 5, coverage unverified; September is partial. Indeed gave card fields for 2 of 36 queries before its wall; no S1 band assigned. Willingness to pay: `unknown` in all 27 cells — spends above are ad spend or a framework ceiling, not a price paid for a visibility product.

## Primary re-pulls, REPULL-1, 2026-09-23

- Agency ChatGPT-ads service claim (E2M, S6 B2B SaaS paid) · `raw/f-signal-bs-S5-S6-paid-agentic-2026-09-23.md` (3 on existence — search synthesis, `verbatim: partial`) · `raw/f-e2m-white-label-chatgpt-ads-services-primary-2026-09-23.md` (3) · "We build ChatGPT Ads as part of a broader white label PPC service, so it complements, rather than competes with, your clients' existing Google, Meta, and LinkedIn Ads campaigns"; "Sponsored Answers for SaaS/B2B, Shopping Carousels for Retail/DTC"; plans "Up to $5K budget $499/mo · Up to $10K budget $999/mo · Up to $20K budget $1,999/mo · Above $20K Custom"; "one-time setup fee starts at $499 per website" · agrees in substance (synthesis wording is not the page's); primary adds list prices — an asking price, not a price paid

## Local / multi-location cells and engine × segment, P16-c4, 2026-09-23

Task P16-c4. A fourth vertical read on the P8 pattern into `customers/local-multi-location.md`; the 27-cell tally above is not recomputed — the nine new cells are stated separately and do not enter it. Floor unchanged: spend needs a spend-class signal at tier 5 or better for that exact cell.

**Nine local / multi-location cells:**

| # | Vertical | Sub-market | Size | Read | Deciding signal, figure verbatim | Tier | Compiled file |
|---|---|---|---|---|---|---|---|
| L1 | Local / multi-location | Organic | SMB | attention | S5 — r/localseo threads matching `"AI visibility"` 73, `AEO` 47, Mar–Sep 2026; S6 — Local Falcon "$24.99 to $199.99 when billed monthly", "Cancel anytime" | 5; 3 | `customers/local-multi-location.md` |
| L2 | Local / multi-location | Organic | Mid | attention | S7 — The Joint Corp 8-K decks: "Ongoing SEO and AI visibility optimization" (Q1), "SEO and AI visibility optimization driving organic traffic and lead quality" (Q2); ~202 full-time employees, 960+ clinics; no figure | 2 | same |
| L3 | Local / multi-location | Organic | Enterprise | **spend** | S1 — Walgreens "Senior Manager, Performance Search & AI Marketing", Indeed card matched on `"generative engine optimization"`, "$125,000 - $218,750 a year"; ~312,000 employees | 3 | same |
| L4 | Local / multi-location | Paid | SMB, Mid, Enterprise | none — checked ×3 | 11 of 12 signals run or n/a; no local buyer named on any paid roster, page or filing | — | same |
| L5 | Local / multi-location | Agentic | SMB, Mid | none — checked ×2 | as L4 | — | same |
| L6 | Local / multi-location | Agentic | Enterprise | attention | S7 — IHG 6-K: "our ChatGPT plug-in recommends IHG hotels … onward to IHG's direct booking channels"; "participating in Google's Agentic AI booking pilot … within Google's AI Mode"; no figure | 2 | same |

Tally, 9 cells: spend 1, attention 3, none — checked 5, blank 0. Willingness to pay: `unknown` in all 9. Strict and loose readings agree — every channel that would decide a cell either ran or is `n/a` by construction; r/smallbusiness returned HTTP 422 on five of seven windows and 0 on the two that answered, recorded as checked.

**Reserve-vertical trigger (`method/plan.md` L233: open consumer electronics and travel "only if the anchor set produces no Gold or Silver cases").** Two readings, both from `findings/proof-scorecard.md`, neither merged: under `grade_raw`, B2B SaaS holds one Silver (E4) and high-CPA one negative Silver (E6, E3 contested) — trigger **not met**; under `grade_rule1`, all three verticals sit on the documented-absence arm (0 Silver) — trigger **met**. Gold: 0 either way. Neither vertical is opened here. Evidence already in raw that touches them without a pass: travel — visitBerlin TED notice with a "Konzeptpapier GEO" requirement, EUR 3,647,000 (`raw/f-ted-S10-repull2-2026-09-23.md`, tier 2); Hyatt 10-K naming "ChatGPT, Claude, Gemini, Grok" as "alternative distribution channels" and IHG's ChatGPT plug-in (`raw/f-edgar-fts-local-multilocation-S7-2026-09-23.md`, tier 2); MakeMyTrip 20-F in the "AI search" hit list, not opened; six hotel entries at the head of llmstxt.site (`raw/e-wayback-llms-txt-directories-2026-09-23.md`). Consumer electronics — nothing surfaced in any P16-c4 channel; Samsung appears only as a Yext story link, not opened.

**Engine × vertical, mentions in raw already pulled plus this pass (files-with-mention in brackets), `raw/f-engine-mentions-raw-count-2026-09-23.md`, measured-by-us word count, tier of each mention inherited:**

| Vertical (files) | ChatGPT | Gemini / AI Mode / AI Overviews | Perplexity | Claude | Copilot | Rufus | Grok | Top |
|---|---|---|---|---|---|---|---|---|
| Skincare (26) | 91 (18) | 51 (13) | 8 (4) | 16 (6) | 2 (1) | 17 (3) | 0 | ChatGPT |
| B2B SaaS (38) | 104 (22) | 63 (16) | 30 (10) | 29 (10) | 17 (5) | 0 | 0 | ChatGPT |
| High-CPA (22) | 49 (10) | 35 (7) | 15 (6) | 7 (3) | 0 | 0 | 2 (2) | ChatGPT |
| Local / multi-location (30) | 97 (17) | 102 (15) | 52 (16) | 25 (9) | 6 (4) | 0 | 8 (4) | Gemini / AI Mode / AIO by mentions; ChatGPT by files |
| Indeed cards, mixed (1) | 1 | 1 | 1 | 0 | 1 | 0 | 0 | — |

Cell-attributable engine naming exists in five cells only: skincare Organic and Agentic / Enterprise (e.l.f. posting: ChatGPT, Perplexity, AI Overviews, Copilot, Claude), skincare Paid / Enterprise (AI Mode, Direct Offers), high-CPA Organic / Enterprise (Juice Plus+: AI Overviews, ChatGPT, Gemini, Perplexity), local Agentic / Enterprise (IHG: ChatGPT, AI Mode). B2B SaaS postings name no engine. Per-vertical detail: the four `customers/` files, §"Engine × segment and buying process, P16-c4".

**Caveats, this append.** L3 rests on an Indeed card whose posting body was not read — the match on "generative engine optimization" is Indeed's, the title names "AI Marketing"; P16-c4b is queued to open the body. L2 and L6 are S7 statements without a budget figure, attention by rule. Engine counts are word matches over raw files of unequal size and provenance (headers, query strings and case text all count); they order engines, they do not measure share. The local vertical overlaps travel (hotels) and healthcare (dental, chiropractic); its boundary is stated in the customer file. The 27-cell done row is unchanged by this append. File over its 100-line budget; overrun includes this append.

## S1 body check, P16-c4b, 2026-09-23

Indeed viewjob channel: walled at page 1 (Cloudflare "Additional Verification Required", Ray ID a3f87a4098e73f67, 2026-09-23 16:21); 0 of 35 bodies and 0 of 34 remaining queries read on Indeed. Bodies then read from employer career sites and ATS endpoints (`raw/f-indeed-S1-repull3-2026-09-23.md`, tier 3, company-stated).

| Count | n | Detail |
|---|---|---|
| Cards checked (body read) | 6 of 35 | Walgreens #22, Choice Hotels #21, A Place for Mom #4, MAHEC #6, The Cigna Group #20, AT&T #2 |
| Confirmed — phrase in body as a duty | 6 | GEO in all six; AEO in Choice, Cigna, AT&T; "LLM visibility" in Choice |
| Weakened — phrase only in card | 0 | — |
| Unread — wall | 29 | 6 of these also absent from the employer's own board (Ziggi's, RestauNax, Vasion, GESA, Intuit, Solventum) |
| Spend cells resting on a read card | 2 confirmed / 0 weakened | local Organic / Enterprise (Walgreens, Choice); high-CPA Organic / Enterprise (Cigna — via the LinkedIn pull of the same posting) |
| Engines named by brand in bodies | 0 of 6 | generic "AI assistants" (Walgreens, AT&T), "answer engines" (Cigna, AT&T); "Claude Code" in Cigna is a development tool |
| Vendors named in bodies | 1 of 6 | Cigna: "Profound, Scrunch, Bluefish, Evertune" (AEO tools, "e.g.") — buyer-side naming, no purchase stated |
| Salary lines in bodies | 5 of 6 | Walgreens $125,000–$218,750; Choice $123,663–$145,486; APFM $165,000–$195,000 + 10%; Cigna $79,100–$131,800; AT&T $128,400–$215,800; MAHEC none |

Caveats: S1 stays the weakest spend class ("headcount budget, not category spend"); the six bodies are the employer's own text, tier 3, and none states a category budget. The 29 unread cards keep their card-only status; skincare and B2B SaaS cells rest on no Indeed card, so this check moves no read in those files.

## EU paid and agentic cells, P16-c3b, 2026-09-23

Per-country EU cells (UK, FR, ES, IT, NL × 3 verticals), sub-markets paid placement and agentic commerce, read 2026-09-23 from `customers/*.md` appends of the same name. Cell = country × vertical × sub-market; size band inside the cell as the evidence states. The 27-cell core tally above is not recomputed.

| Cut | Cells | spend | attention | none — checked | unassigned beside |
|---|---|---|---|---|---|
| EU organic, P16-c3 | 15 | 1 (FR × B2B SaaS × enterprise, Pennylane) | 0 | 12 | 2 (Make ES; Compare the Market UK) |
| EU paid, P16-c3b | 15 | 0 | 0 | 15 | 2 (Jotform UK B2B SaaS; BestMoney UK high-CPA) |
| EU agentic, P16-c3b | 15 | 1 (FR × high-CPA × mid-market, Alan) | 0 | 14 | 0 |
| EU total | 45 | 2 | 0 | 41 | 4 |

Channels behind the 30: S1 LinkedIn guest API 38 pages, Hellowork FR, Tecnoempleo ES (tier 3); S2 OpenAI locale posts es/it/nl, Shopify Agentic Storefronts ×5 locales, Adyen, Adform, Adthena UK index (3–5); S5 Arctic Shift 17 queries, 6 unresolved after 422 ×2 (5); S10 TED 20 terms, UK Contracts Finder 12 terms (2). Raw: `f-*-eu-paid-agentic-2026-09-23.md`, six files; images 3 (Adthena leaderboard, saturation, look-up; IMG-1 pending).

Outside the verticals, EU paid, recorded and moving no cell: Volkswagen, Vodafone testing ChatGPT Ads via Adform (release 2026-09-10, tier 3); giffgaff, Vodafone, Booking.com top UK ChatGPT advertisers, 1,342 distinct UK advertisers week 2026-07-13 to 07-20 (tier 5).

**Caveats, this append.** Nine of the 30 `none` reads (UK agentic, ES paid, NL agentic, across three verticals) carry S5 unresolved; they rest on S1, S2, S10. The single agentic spend read is one product posting, S1 alone, tier 3. TED phrase hits on "commerce agentique" and "publicité IA" are pre-category text matches, not demand. Publication bias: private ChatGPT Ads buyers in the five countries leave no trace in any channel here except Adthena's images, which are unread.

## GAP-SK — cell E2 closed, 2026-09-23

Closes E2 (Skincare, Organic, Mid-market), the strict matrix's last blank cell (R-BLOCKED-2 note above, "Strict blank left: E2, skincare Organic/Mid-market — S6, S12 unrun there"). Compiled source: `customers/skincare-beauty.md` §"Gap fill GAP-SK, 2026-09-23". Raw: `raw/f-edgar-sk-headcount-midmarket-olaplex-beautyhealth-2026-09-23.md`, `raw/f-signal-sk-S1-hydrafacial-workday-geo-aeo-2026-09-23.md`, `raw/f-signal-sk-S1-olaplex-greenhouse-check-2026-09-23.md`, `raw/f-signal-sk-S12-llms-txt-midmarket-2026-09-23.md`, `raw/f-signal-sk-S6-organic-midmarket-2026-09-23.md`.

| # | Cell | Before (strict / loose) | After | Deciding signal, figure verbatim | Tier |
|---|---|---|---|---|---|
| E2 | Skincare, Organic, Mid-market | blank / none — checked | **spend** | S1 — The Beauty Health Company (Hydrafacial), "Develop and execute SEO, AEO, and GEO strategies…", posting JR101647, "$121,000- 143,000/annually" | 3 |

New mid-market beauty employers, filed headcount: OLAPLEX Inc. 278 employees, The Beauty Health Company (Hydrafacial) 613 employees, both as of 2025-12-31 (10-K, tier 2). S12: genuine llms.txt present on both companies' consumer domains (olaplex.com, hydrafacial.com), tier 1, attention — corroborating, not deciding. S6: checked, blank — unattributed (Passionfruit "Mid-market" GEO/SEO retainer band, $12,000–$30,000/month; no named mid-market beauty buyer). S7: checked, nothing in either 10-K.

**Tallies, 27 cells, revised (all signals now run or n/a by construction for every cell):**

| Reading | spend | attention | none | blank |
|---|---|---|---|---|
| Strict | 9 | 1 | 17 | 0 |
| Loose | 9 | 1 | 17 | 0 |

Segment-matrix done row: **both readings now satisfied, 27 of 27, zero blanks.** Strict and loose converge for the first time since Pass 8 — every remaining cell's `none — checked` rests on a signal actually run, not a channel-blocked reinterpretation.

**Hypotheses, re-touched.** H4 (kill: any SMB cell with spend) — unaffected, E2 is Mid-market not SMB; still killed via B2B SaaS Organic/SMB. H7 (organic > paid, agentic in spend-cell count) — organic rises to 7 (skincare 2, B2B SaaS 3, high-CPA 2) against paid 1 and agentic 1; **strict now also confirmed**, both readings converge. H9 (agentic spend only at enterprise) — unaffected by an organic cell; both readings remain confirmed per R-BLOCKED-2.

**Caveats, this append.** S1 is this vertical's fourth spend cell resting on a single job posting at a single employer — the catalogue's own weakest spend class, per C2 above ("Six of the seven spend reads rest on S1…"; now seven of nine). The mid-market band for both new employers rests on one filed headcount snapshot, 2025-12-31. Only two mid-market-banded beauty companies were checked; not an exhaustive sweep of small/mid-cap beauty issuers. Willingness to pay is unchanged: `unknown` in all 27 cells — the Hydrafacial posting's salary band is internal headcount cost, not a price paid to a vendor. File over its 100-line budget; overrun is this append, consistent with every prior append.

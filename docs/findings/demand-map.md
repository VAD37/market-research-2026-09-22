# Demand map — the 27-cell segment matrix

| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every `raw/` file cited. Oldest source publication carried: 2025-06-03 (HN thread title), via `customers/b2b-saas.md`; oldest load-bearing 2026-01-11, `raw/c-google-ucp-merchant-agentic-2026-09-22.md`, via `customers/skincare-beauty.md` |
| Lane | F, with A, B and C feeding it |
| Hypotheses touched | H4, H7, H9 — scored below; full register in `unknowns.md` |
| Claims at tier 3 or better | 7 of 7 |

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
| C1 | 7 of 27 cells read spend, 1 attention, 11 none — checked, 8 blank | E1–E12 | 3 | n/a | yes |
| C2 | Six of the seven spend reads rest on S1 job postings, the catalogue's own weakest spend class | E3, E6, E7, E8, E9, E11 | 3 | n/a | yes |
| C3 | Willingness to pay is unknown in all 27 cells; no buyer anywhere discloses a price paid | willingness-to-pay block | 3 | n/a | yes |
| C4 | Organic carries 5 spend cells against 1 each for paid and agentic | tallies | 3 | n/a | yes |
| C5 | 5 of the 7 spend cells are enterprise; exactly 1 of 9 SMB cells reads spend | tallies | 3 | n/a | yes |
| C6 | Two compilers applied the `none` rule differently on the same day; the difference moves 19 of 27 reads | side-by-side table | 3 | n/a | yes |
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
- No claim here is below tier 3; no metric crossing is relied on. Publication bias runs one way: quiet spending leaves no public trace, so `none` and `blank` are weaker evidence than `spend`; SMB and mid-market is where that bites hardest, and every channel that could have caught them was blocked this session. The buyer-size bands are a method choice fixed 2026-09-22, not a fact about how this market segments itself; a market that cuts differently is mis-cut here invisibly. One raw file was edited after creation — `raw/f-signal-sk-S7-coty-10k-2026-09-22.md`, headcount added post-landing to band a cell.
- The oldest pull cited is 2026-09-22; no cited pull is stale under `method/plan.md`. This file carries evidence, not a verdict.

# Business-review solution 1 — what closes each gap, 2026-09-23

Written by the main thread from `biz-review-1-2026-09-23.md` (REV-BIZ-A). Section 5 is reserved for `biz-review-2-bakeoff-2026-09-23.md` (REV-BIZ-B, queued). Every task below is a research or compilation task; none plans execution. Effort words are shapes (append / one pass), never dates.

## 1. Read of the review

Accepted in full. The repo is deep on demand cells, engine × sub-market cells, vendor profiles and case screening; it is thin on the two BA sections that open and close a brief (why now; ranked risks) and both reader briefs are stale. Two of 22 gaps block a brief; 12 close by desk compilation from raw already pulled; 8 need one more research pass with web; 1 is not closable without owner credentials.

Principle for closing: **compile before pulling.** Gaps 1, 2, 4, 5, 6, 9, 10, 20, 21 need no new evidence. They go first, in one agent with no browser, so BRIEF-4 and the bake-off have inputs regardless of how the wider pass lands.

## 2. Gap → task map

| # | Gap (review §7) | Task | Lands in | Order |
|---|---|---|---|---|
| 1 | Dated external-trigger timeline | COMPILE-1 | `findings/trigger-timeline.md` (new, 100 lines, Lane E/B) — one row per dated event with tier, raw path; no interpretation column | 2 |
| 2 | Ranked risk table; platform capture | COMPILE-1 | `findings/whitespace.md` append "Risk register": criterion stated (tier of the evidence that the risk is real × breadth of cells it touches), likelihood only where a source states it, early signal = the raw that would show it; platform capture first-class row | 2 |
| 4 | Evidence-quality three-count | COMPILE-1 | `findings/proof-scorecard.md` + `transition-evidence.md` appends per `plan.md` L146–155: metric moved experimental / metric moved observational / action named, outcome unknown; per case, itemised | 2 |
| 5 | Tier-2 negative tail in one table | COMPILE-1 | `findings/proof-scorecard.md` append: every filing, exhibit or docket carrying a decline, side by side with the positive Silvers | 2 |
| 6 | 32-row hypothesis register | COMPILE-2 | `findings/unknowns.md` append: H1–H16, HE1–HE3, HP1–HP4, H17–H25; every prior mark side by side (Pass 9, review-1, P12–P14), `not produced` where so | 4 |
| 9 | Funding, M&A, valuation table | COMPILE-2 | `competitors/INDEX.md` append; 8-K rows tier 2, relays tier 5, PitchBook `unknown — paid` | 4 |
| 10 | Cross-sub-market pricing table | COMPILE-2 | `findings/market-potential.md` append; vendor list price, rate card, CPC guidance, commission; tier per cell | 4 |
| 20 | Glossary rows (Datos definitions, MAU vs query share) | COMPILE-2 | `method/glossary.md` dated addition | 4 |
| 21 | `unknowns.md` by-file roll-up stale vs headers | COMPILE-2 | `findings/unknowns.md` append restating the roll-up from current headers | 4 |
| 22 | Line-budget overruns (markets, customers) | AMEND-3 | `plan.md` Line budgets dated note: files over budget listed; compression pass named as method debt, no rewrite of evidence | 4 |
| 8 | Search-ad baseline beyond Google | P16-c1 | `markets/paid-placement.md` append: MSFT, AMZN 10-K search/ads lines (EDGAR FTS, tier 2); IAB/PwC 2025 report (tier 4); MAGNA 2026 if public | 5 |
| 7 | Budget line stolen from | P16-c1 | `customers/*.md` appends: IAB outlook, agency surveys; expected `unknown — checked` at tier ≤3 | 5 |
| 15 | Publisher / sell-side monetisation | P16-c2 | `markets/organic-recommendation.md` append or `findings/whitespace.md` E-row: Cloudflare pay-per-crawl docs, TollBit, ProRata pages (tier 3); publisher 10-Ks (tier 2) | 5 |
| 16 | Ad-measurement vendors; OpenAI partner list | P16-c2 | `competitors/` new profiles where a vendor sells AI-ads measurement; archive of OpenAI partner page | 5 |
| 17 | Brand-accuracy demand signal | P16-c3 | `method/demand-signals.md` dated addition S13 (brand-misinformation complaints, correction requests); `customers/*.md` appends | 5 |
| 18 | EU depth outside DE; EU engine share | P16-c3 | `markets/*.md` appends: Similarweb country cuts (tier 4), C64 press, DSA repositories; UK/FR/ES/IT demand cells | 5 |
| 12 | Local-business vertical; reserve trigger | P16-c4 | `customers/local-multi-location.md` (new, P8 pattern); Indeed via `ext` when free | 5 |
| 11 | Engine × segment read | P16-c4 | `customers/*.md` appends: engines named in S1 posting text and S2 listings; partial by design | 5 |
| 13 | Brand-side adoption series | P16-c4 | `findings/market-potential.md` append: Wayback captures of G2 categories, LinkedIn counts, HTTP Archive llms.txt | 5 |
| 19 | Switching cost, buying process ×27 | P16-c4 | `customers/*.md` appends from vendor T&Cs (contract length), OMR; expected mostly `unknown — checked` | 5 |
| 14 | Agentic GMV, fees, merchant counts | — | `blocked-channels.md` already lists Shopify Partner, Mastercard registration; owner decision | — |
| 3 | Both briefs stale | BRIEF-4 | `findings/executive-brief-<date>.md`, `director-brief-<date>.md`, deck regenerated; runs after COMPILE-1/2 and P16 so it inherits the new tables | 6 |

Contradictions (review §4 rows 1–13): COMPILE-2 appends one "Figures carried twice" table to `findings/unknowns.md` listing each pair with both paths, so the brief writer sees them; nothing is reconciled or averaged. Rows 6 and 7 get an annotation append in `markets/paid-placement.md` pointing at the newer `ai-ads-evidence.md` row.

Missing business interests (review §6): rows 1, 2, 6, 7 are P16 clusters above; rows 3 (compliance tooling), 4 (agency holding-co revenue) and 8 (SMB via Indeed) fold into P16-c2, P16-c1 and R-BLOCKED-2 / P16-c4 respectively; row 5 (protocol fees) stays credential-blocked; row 9 (adjacent categories) is P16-c4's local vertical only — consumer electronics and travel stay reserve unless P16-c4 finds the trigger met.

## 3. Queue order after this review

Cap 3. The user's same-day instructions rank above this review: paywall re-pulls (REPULL-1) and image pulls come first.

| order | task | why here |
|---|---|---|
| 1 | REPULL-1 (`ext`) | User priority 2026-09-23; primaries replace secondaries before any compile reads them |
| 2 | COMPILE-1 | No browser; unblocks BA §2, §5, §6 and the judge's `why_now`, `negative_tail`, `risks_ranked`, `platform_capture` columns |
| 3 | P9-r (after P4-r) | Tier-3 recount, already queued |
| 4 | COMPILE-2, AMEND-3 | Desk; registers and tables |
| 5 | P16-c1 … c4 | One agent per cluster, web; `ext` only for c4 Indeed |
| 5 | IMG-1 (after REPULL-1) | Image transcriptions feed the same compiled files |
| 6 | REV-BIZ-B, then BRIEF-4 | Brief inherits everything above |
| 7 | P15 bake-off | Last pass, gate unchanged |

## 4. What this does not do

- No market number is written here. Every task above compiles from `docs/raw/` or pulls into it.
- No verdict, no dates for action, no budget. "Risk register" ranks evidence about threats to the guiding hypothetical; it sets no kill criterion.
- Pass 10 stays skipped; the tier-1 AI Mode row in `whitespace.md` keeps its skipped-pass caveat.
- Review §7 row 14 is not worked around; the owner supplies credentials or the cell stays `unknown — checked`.

## 5. Bake-off output needs — pending REV-BIZ-B

Reserved. When `biz-review-2-bakeoff-2026-09-23.md` lands, this section maps each input the ten methods and the judge columns demand to the file that supplies it, and adds tasks only where §2 above leaves a hole.

## Caveats

- Written from one reviewer's read; the reviewer did not open the 41 profiles or ~780 raw bodies, so §2 may miss compiled rows that already exist. COMPILE agents check before appending.
- P4-r and R-BLOCKED-2 are in flight; their landings may change gaps 4, 5 and 12 before COMPILE-1 runs. COMPILE-1 reads the tree as landed at its spawn.

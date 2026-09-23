# Snapshot index

Generated 2026-09-24; evidence as of commit 5603409 (last commit touching raw or compiled) by `python docs/method/gen-snapshot-index.py` -- never hand-edit; re-run after any landing. Per-file rows: `snapshot-index.csv` (same folder). Tokens are `ceil(chars/3.5)`, a heuristic. Split budget: 120,000 tokens per agent (`--budget N`).

Staleness: if `git log -1 --format=%h -- docs/raw docs/markets docs/competitors docs/customers docs/findings` differs from that commit, or `git status` shows changes there, re-run.

## Layers

| layer | files | words | tokens_est | agents at budget |
|---|---|---|---|---|
| raw | 1044 | 1,274,751 | 2,545,601 | 22 |
| markets | 3 | 19,248 | 38,440 | 1 |
| competitors | 44 | 60,673 | 116,891 | 1 |
| customers | 4 | 21,117 | 39,429 | 1 |
| findings | 15 | 72,504 | 132,332 | 2 |

## Raw by lane

| lane | files | words | tokens_est | agents at budget | orphan | repull | img | flagged |
|---|---|---|---|---|---|---|---|---|
| A organic (GEO/AEO/LLMO) | 220 | 221,708 | 440,000 | 4 | 0 | 2 | 4 | 12 |
| B paid placement | 244 | 276,879 | 536,913 | 5 | 14 | 10 | 4 | 1 |
| C agentic commerce | 68 | 71,796 | 149,450 | 2 | 0 | 1 | 2 | 3 |
| D manipulation | 117 | 108,858 | 230,931 | 2 | 0 | 3 | 0 | 8 |
| E measurement / proof | 233 | 424,743 | 843,642 | 8 | 3 | 13 | 15 | 25 |
| F transition evidence | 162 | 170,767 | 344,665 | 3 | 2 | 12 | 2 | 18 |

## Raw by lane x key

Key = second name segment (`<lane>-<key>-...`); e-case, e-market, f-signal, f-roles, f-jobboards take the third. Select files with `ls docs/raw/<lane>-<key>-*`.

| lane-key | files | tokens_est | dates | orphan |
|---|---|---|---|---|
| a-vendor | 6 | 50,364 | 2026-09-22 .. 2026-09-23 | 0 |
| a-cloudflare | 7 | 21,613 | 2026-09-22 .. 2026-09-23 | 0 |
| a-similarweb | 11 | 19,300 | 2026-09-22 .. 2026-09-23 | 0 |
| a-scrunch | 8 | 16,726 | 2026-09-22 .. 2026-09-23 | 0 |
| a-peec | 8 | 16,225 | 2026-09-22 .. 2026-09-23 | 0 |
| a-searchable | 8 | 15,503 | 2026-09-22 .. 2026-09-23 | 0 |
| a-profound | 6 | 14,453 | 2026-09-22 .. 2026-09-23 | 0 |
| a-semrush | 6 | 12,355 | 2026-09-22 | 0 |
| a-airops | 5 | 11,668 | 2026-09-22 | 0 |
| a-promptwatch | 6 | 11,552 | 2026-09-22 | 0 |
| a-practitioner | 4 | 11,115 | 2026-09-22 | 0 |
| a-google | 5 | 11,057 | 2026-09-22 | 0 |
| a-otterly | 7 | 10,838 | 2026-09-22 .. 2026-09-23 | 0 |
| a-yext | 7 | 10,477 | 2026-09-22 .. 2026-09-23 | 0 |
| a-rankprompt | 5 | 10,322 | 2026-09-22 | 0 |
| a-quattr | 5 | 10,301 | 2026-09-22 | 0 |
| a-brightedge | 5 | 9,731 | 2026-09-22 | 0 |
| a-conductor | 5 | 9,034 | 2026-09-22 | 0 |
| a-locafy | 7 | 8,975 | 2026-09-22 | 0 |
| a-hubspot | 4 | 8,760 | 2026-09-22 | 0 |
| a-rankscale | 4 | 8,582 | 2026-09-22 | 0 |
| a-muckrack | 7 | 8,528 | 2026-09-22 .. 2026-09-23 | 0 |
| a-geosurge | 5 | 8,126 | 2026-09-22 | 0 |
| a-athenahq | 5 | 7,875 | 2026-09-22 | 0 |
| a-sitefire | 5 | 7,612 | 2026-09-22 | 0 |
| a-amazon | 4 | 7,577 | 2026-09-22 | 0 |
| a-brandlight | 7 | 7,265 | 2026-09-22 | 0 |
| a-ahrefs | 5 | 6,976 | 2026-09-22 | 0 |
| a-changeagents | 6 | 6,195 | 2026-09-22 | 0 |
| a-birdeye | 4 | 6,088 | 2026-09-22 | 0 |
| a-statcounter | 4 | 4,800 | 2026-09-22 .. 2026-09-23 | 0 |
| a-other (27 small keys) | 39 | 70,007 | 2026-09-22 .. 2026-09-23 | 0 |
| b-openai | 34 | 82,469 | 2026-09-22 .. 2026-09-23 | 2 |
| b-ppcland | 10 | 54,270 | 2026-09-23 | 0 |
| b-court | 17 | 41,635 | 2026-09-22 .. 2026-09-24 | 0 |
| b-microsoft | 15 | 39,371 | 2026-09-22 .. 2026-09-23 | 0 |
| b-eu | 23 | 36,330 | 2026-09-22 .. 2026-09-23 | 1 |
| b-alphabet | 3 | 32,354 | 2026-09-23 | 0 |
| b-sec | 20 | 29,811 | 2026-09-23 | 0 |
| b-reddit | 3 | 18,881 | 2026-09-23 | 0 |
| b-google | 9 | 17,852 | 2026-09-22 .. 2026-09-23 | 1 |
| b-amazon | 8 | 17,565 | 2026-09-22 .. 2026-09-23 | 0 |
| b-perplexity | 9 | 10,628 | 2026-09-22 .. 2026-09-23 | 0 |
| b-criteo | 5 | 9,500 | 2026-09-22 .. 2026-09-23 | 0 |
| b-anthropic | 4 | 9,399 | 2026-09-22 .. 2026-09-23 | 0 |
| b-adthena | 5 | 8,364 | 2026-09-22 .. 2026-09-23 | 0 |
| b-other (50 small keys) | 79 | 128,484 | 2026-09-22 .. 2026-09-23 | 10 |
| c-openai | 7 | 15,182 | 2026-09-22 | 0 |
| c-adobe | 6 | 13,438 | 2026-09-22 .. 2026-09-23 | 0 |
| c-microsoft | 7 | 12,332 | 2026-09-22 .. 2026-09-23 | 0 |
| c-shopify | 8 | 10,179 | 2026-09-22 .. 2026-09-23 | 0 |
| c-google | 5 | 10,031 | 2026-09-22 | 0 |
| c-salesforce | 5 | 8,363 | 2026-09-22 | 0 |
| c-feedonomics | 5 | 7,257 | 2026-09-22 | 0 |
| c-other (19 small keys) | 25 | 72,668 | 2026-09-22 .. 2026-09-23 | 0 |
| d-technique | 7 | 54,559 | 2026-09-22 | 0 |
| d-paper | 39 | 51,724 | 2026-09-23 | 0 |
| d-citationpref | 9 | 21,250 | 2026-09-22 | 0 |
| d-structured | 9 | 20,614 | 2026-09-22 | 0 |
| d-review | 8 | 19,284 | 2026-09-22 | 0 |
| d-injection | 13 | 17,285 | 2026-09-22 | 0 |
| d-seeding | 12 | 17,084 | 2026-09-22 | 0 |
| d-countermeasure | 9 | 12,221 | 2026-09-22 | 0 |
| d-comparison | 7 | 9,445 | 2026-09-22 | 0 |
| d-other (4 small keys) | 4 | 7,465 | 2026-09-23 | 0 |
| e-case-census | 14 | 104,690 | 2026-09-22 .. 2026-09-23 | 0 |
| e-case-edgar | 1 | 79,948 | 2026-09-23 | 0 |
| e-case-reddit | 2 | 73,133 | 2026-09-22 .. 2026-09-23 | 0 |
| e-google | 3 | 55,061 | 2026-09-22 .. 2026-09-23 | 0 |
| e-claude | 1 | 52,793 | 2026-09-22 | 0 |
| e-market-size | 38 | 50,155 | 2026-09-22 .. 2026-09-23 | 1 |
| e-case-otterly | 14 | 40,163 | 2026-09-23 | 0 |
| e-gemini | 1 | 29,126 | 2026-09-22 | 0 |
| e-case-c13 | 13 | 26,634 | 2026-09-22 | 0 |
| e-case-c9 | 9 | 22,861 | 2026-09-22 | 0 |
| e-case-c12 | 12 | 22,574 | 2026-09-22 | 0 |
| e-case-practitioner | 8 | 19,066 | 2026-09-22 .. 2026-09-23 | 0 |
| e-case-quattr | 6 | 17,984 | 2026-09-22 .. 2026-09-23 | 0 |
| e-case-airops | 5 | 17,653 | 2026-09-23 | 0 |
| e-case-profound | 3 | 17,473 | 2026-09-22 .. 2026-09-23 | 0 |
| e-case-c8 | 9 | 14,226 | 2026-09-22 | 0 |
| e-case-c11 | 6 | 12,085 | 2026-09-22 | 0 |
| e-case-seer | 4 | 8,120 | 2026-09-22 .. 2026-09-23 | 0 |
| e-case-iac | 4 | 4,381 | 2026-09-22 .. 2026-09-23 | 0 |
| e-other (59 small keys) | 80 | 175,516 | 2026-09-22 .. 2026-09-23 | 2 |
| f-indeed | 3 | 34,125 | 2026-09-23 | 0 |
| f-signal-hr | 18 | 28,009 | 2026-09-22 .. 2026-09-23 | 1 |
| f-signal-bs | 19 | 24,286 | 2026-09-22 .. 2026-09-23 | 0 |
| f-signal-sk | 18 | 23,830 | 2026-09-22 .. 2026-09-23 | 1 |
| f-roles-jd | 3 | 21,323 | 2026-09-23 | 0 |
| f-conference | 6 | 15,888 | 2026-09-22 | 0 |
| f-signal-census | 3 | 15,710 | 2026-09-22 | 0 |
| f-roles-forum | 3 | 15,284 | 2026-09-23 | 0 |
| f-roles-av | 9 | 15,124 | 2026-09-23 | 0 |
| f-roles-blogs | 5 | 14,999 | 2026-09-23 | 0 |
| f-reddit | 5 | 13,603 | 2026-09-23 | 0 |
| f-linkedin | 4 | 11,786 | 2026-09-23 | 0 |
| f-roles-salary | 6 | 9,619 | 2026-09-23 | 0 |
| f-intero | 5 | 5,773 | 2026-09-22 | 0 |
| f-seer | 4 | 4,542 | 2026-09-22 | 0 |
| f-fire | 4 | 2,807 | 2026-09-22 | 0 |
| f-other (30 small keys) | 47 | 87,957 | 2026-09-22 .. 2026-09-23 | 0 |

## Compiled files

Dated sections stack on older text without supersede notes; read the latest dated section as the current reading and check earlier sections for the figure it replaces.

| file | words | tokens_est | sections | latest dated section |
|---|---|---|---|---|
| `competitors/*.md` (43 profiles, per-file in CSV) | 54,766 | 105,906 | 10-11 each (18 with a dated section) | |
| `competitors/INDEX.md` | 5,907 | 10,985 | 2 (2 dated) | Funding, M&A and valuation, COMPILE-2, 2026-09-23 |
| `customers/b2b-saas.md` | 5,134 | 9,365 | 19 (9 dated) | Pass 8 re-run, 2026-09-23 |
| `customers/high-cpa-regulated.md` | 5,748 | 10,780 | 18 (8 dated) | Pass 8 re-run, 2026-09-23 |
| `customers/local-multi-location.md` | 2,824 | 5,252 | 13 (2 dated) | Birdeye study cover — added 2026-09-24 |
| `customers/skincare-beauty.md` | 7,411 | 14,032 | 22 (12 dated) | Pass 8 re-run, 2026-09-23 |
| `findings/ai-ads-evidence.md` | 3,050 | 5,789 | 14 (5 dated) | Orphan compile, GAP-B — added 2026-09-24 |
| `findings/demand-map.md` | 6,179 | 10,555 | 23 (9 dated) | EU national job boards, all terms — added 2026-09-24 |
| `findings/director-brief-2026-09-23-r2.md` | 8,868 | 16,028 | 17 (0 dated) |  |
| `findings/director-brief-2026-09-23.md` | 4,633 | 8,251 | 17 (0 dated) |  |
| `findings/executive-brief-2026-09-23-r2.md` | 2,239 | 4,093 | 5 (0 dated) |  |
| `findings/executive-brief-2026-09-23.md` | 1,091 | 1,990 | 6 (0 dated) |  |
| `findings/frontier-scan.md` | 3,700 | 7,601 | 12 (1 dated) | Manipulation evidence ledger — added 2026-09-24 |
| `findings/geo-aeo-roles.md` | 3,988 | 7,080 | 12 (0 dated) |  |
| `findings/market-potential.md` | 7,390 | 13,781 | 17 (9 dated) | US / EU cuts and unused forecast detail — added 2026-09-24 |
| `findings/proof-scorecard.md` | 6,721 | 12,139 | 18 (7 dated) | Orphan case files, GAP-ACEF — added 2026-09-24 |
| `findings/review-1-2026-09-23.md` | 3,418 | 5,302 | 17 (0 dated) |  |
| `findings/transition-evidence.md` | 3,679 | 6,345 | 12 (4 dated) | Evidence-quality three-count, 2026-09-23 |
| `findings/trigger-timeline.md` | 2,025 | 4,318 | 10 (3 dated) | Primary re-pulls, REPULL-1, 2026-09-23 |
| `findings/unknowns.md` | 11,306 | 19,934 | 28 (7 dated) | Pass 8 re-run, 2026-09-23 |
| `findings/whitespace.md` | 4,217 | 9,126 | 14 (5 dated) | Litigation risk register — added 2026-09-24 |
| `markets/agentic-commerce.md` | 4,458 | 9,088 | 18 (7 dated) | Merchant readiness and orphan lane-C items — added 2026-09-24 |
| `markets/organic-recommendation.md` | 6,792 | 13,534 | 20 (8 dated) | Publisher litigation — added 2026-09-24 |
| `markets/paid-placement.md` | 7,998 | 15,818 | 23 (13 dated) | ChatGPT Ads buying mechanics, GAP-B — added 2026-09-24 |

## Coverage and flags

Raw reach: direct compiled cite 765, via another cited raw 232, named only in method/ or sources/ 28, orphan 19 (of 1044). Orphan = none of those; audit verdicts in `orphan-audit-*.md`.
Audit verdicts: compiled 103, covered 44, not-briefable 11, superseded 1.

Header flags on 67 files (per-file in CSV `flags`): tier-n/a 43, label-n/a 33, no-header 9, label-mixed 9, tier-mixed 7, label-user-reported 4, tier-missing 1, label-missing 1, label-per 1. Labels outside the five kinds (vendor-reported, analyst-derived, filed, company-stated, measured-by-us) are flagged; `n/a` and `mixed` mark tables and censuses that aggregate several sources.

No header at all: `a-assistant-share-table-2026-09-22.md`, `d-technique-census-c1-2026-09-22.md`, `d-technique-census-c4-2026-09-22.md`, `d-technique-census-c5-2026-09-22.md`, `d-technique-census-c6-2026-09-22.md`, `e-case-census-c12-2026-09-22.md`, `e-case-census-c3-2026-09-22.md`, `e-case-census-c6-2026-09-22.md`, `e-market-size-table-2026-09-22.md`.

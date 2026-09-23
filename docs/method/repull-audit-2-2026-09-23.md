# Repull audit 2 — what still needs a pull before the brief

Date 2026-09-23. Task REPULL-AUDIT-2. Read-only over `docs/`, plus 33 curl probes (no browser, no git). Input: `repull-queue-2026-09-23.csv` (169 rows), STATE landings REPULL-1 9c2aece, REPULL-1b 3a290b8, P9-r c2fef4a, P16-c2 602f55b, R-BLOCKED-2 631dedd, P4-r 2df8a8d, IMG-1a/b/c; `blocked-channels.md` re-probe 3; `img/INDEX.csv`; `findings/unknowns.md` §Unknowns. The queue CSV now has a `status` column (last).

## Status, 169 rows

| status | rows | how assigned |
|---|---|---|
| done-9c2aece (REPULL-1) | 22 | `supersedes:` header in a `*-primary-*` raw, file time 13:18–13:48 |
| done-3a290b8 (REPULL-1b) | 24 | same, file time 15:38–16:09 |
| done-c2fef4a (P9-r) | 9 | `b-sec-*` filings superseding sec.gov relays |
| done-631dedd / 2df8a8d / 602f55b | 4 / 1 / 1 | Arctic Shift, TED; P4-r Reddit; Adthena index |
| unknown-checked | 21 | wall re-tested 2026-09-23 and stands, or page gone (404) |
| credential | 13 | paid seat, login, or registration form (repo rule: no forms) |
| open | 74 | not attempted since the audit, or new channel found |

`credential` here includes free registration forms (Datos, Pace PDF, Adthena 29M report, Foundation report, generativepulse) and LinkedIn login, not only paid seats. Indeed rows 162/164/167 are `unknown-checked` (Cloudflare verification stands); card bodies belong to live GAP-IND.

## Open rows — value filter

52 of 74 open rows are cited by no compiled file (filename or claim grep over `findings/`, `markets/`, `customers/`, `competitors/`): dropped. Includes comScore 82–84, Radyant 129–131, regulator truncations 105–108, conference logos 156–158, Otterly 139/140/143/145/146, Reddit subs 161/169.

22 cited open rows, ranked:

| row | claim | cited in | lift / load | probe 2026-09-23 | verdict |
|---|---|---|---|---|---|
| 137 | IAC Google referrals "50%" vs "63%" chart | proof-scorecard, trigger-timeline; r2 director brief | tier 2; reconciles r2 figure | slide 7 JPG in accession folder, 200 (contact UA) | pull — A |
| 144 | Otterly Reddit test (only Silver rule-1) | proof-scorecard, whitespace, unknowns | chart values of r2 case | blog 200 with browser UA; wp-content images 200 | pull — A |
| 142 | Otterly llms.txt test, "84 of 62,100+" | proof-scorecard; r2 director brief | chart values | blog 200 browser UA | pull — A |
| 141 | Otterly HTML vs Markdown test | proof-scorecard | chart values | same pattern | pull — A |
| 109 | Adobe Q2 2026 AI-traffic PDF | via retail-analytics table; H1, E12 in r2 | may hold per-engine or organic comparator | business.adobe.com times out; Wayback id_ PDF 200, 2.28 MB | pull — A |
| 110 | Adobe Q3 2026 PDF, pp. 13–53 uncaptured | same | same | no Wayback capture; domain times out to curl | try — B (`ext`) |
| 47 | Ulta × Google agentic (Cloud Next '26) | transition-evidence, skincare-beauty | tier 5 → 3 | ulta.com IR press list 200 | pull — A |
| 49 | Sephora/Ulta AI figures (Ulta IR, LVMH, NielsenIQ, Circana) | skincare-beauty:16 | tier 5 → 2–3 where filed | Ulta IR 200 | pull — A, IR/filings only |
| 48 | 5W: ingredient-led brands lead AI citations | skincare-beauty:73 | tier 5 → 4–5 | 5wpr.com/new 200; report URL unknown | try — A, one pass |
| 39 | Sensor Tower ChatGPT ads mix report | ai-ads-evidence:43, paid-placement:134, adthena | tier 5 → 4 | sensortower.com/blog 200; guessed slug 404 | try — A, one pass |
| 31 | dockets: Amazon/Meta/xAI searches; Chegg/Penske MTD outcome | agentic-commerce, paid-placement, proof-scorecard, trigger-timeline | tier 2 completeness | courtlistener HTML search 200; API timed out; 66834516 404 | pull — A |
| 159 | Zendesk llms.txt present? | market-potential | measured-by-us cell | 200 text/plain, 741,350 bytes | pull — A (was blocked) |
| 74, 77 | llms.txt: GEICO, GNC, Estée Lauder, Ulta | high-cpa, skincare, transition-evidence | measured-by-us cells | geico 403, esteelauder 403, gnc 307 | try — B (`ext`) |
| 37 | Adthena Data Pulse June 2026, UK share zero | paid-placement:28 | tier 5, no lift; IMG-1c UK board newer | adthena.com/resources 200; doc not found | try — B, low |
| 43, 50, 70, 75, 95, 100, 134 | Reddit 2020 thread; OMR audio; SEL topic list; rosters; OCR scan; ad image; Chime | various | no lift or no tool | not probed | skip — little value |

## Non-CSV items

| item | state 2026-09-23 | verdict |
|---|---|---|
| REPULL-1b leftover rows 139–146 (Otterly charts) | 3 cited → A; 5 uncited | A for 141, 142, 144; drop rest |
| leftover 100 (OpenAI ad-unit image) | text re-fetched (`b-openai-help-ads-basics-2026-09-23.md`); image only | skip |
| leftovers 109–110 (Adobe PDFs) | Q2 via Wayback; Q3 needs browser | A / B |
| leftover 126 (W&V SEOWERK) | wuv.de wall server-side, identical on 2 articles | skip; status unknown-checked |
| leftover 137 (IAC chart) | JPG reachable at sec.gov Archives | A |
| INDEX: 6 GML mp4 | storage.googleapis.com 200, 8.3 MB video | skip — ad-format demos, no figures |
| INDEX: 2 Adobe PDFs | as rows 109–110 | A / B |
| INDEX: 2 OpenAI images | src hidden; openai.com 403 to curl | skip — ad-format screenshots |
| INDEX: 1 Business Wire image | mms.businesswire.com 403 (browser UA too) | skip — product image |
| unknowns Lane E per-engine referral breakout | Adobe PDFs are the one free lead | A / B |
| unknowns Lane C Perplexity merchant terms | only Wayback capture 2025-07-16 renders blank | skip |
| unknowns Lane B/F dockets for Amazon, Meta, xAI | courtlistener reachable | A (row 31) |
| unknowns Lane E brand corroboration, Pass 3 titles | P4-r read 109 brand pages, 1 corroborated | skip — little value |
| unknowns Lane F G2 velocity | DataDome CAPTCHA; no free channel | skip |
| GAP-SK, GAP-IND | assigned to live agents | excluded |

## Batches

| batch | channel | rows / items | compiled files touched | tool rounds |
|---|---|---|---|---|
| RP2-A | curl/fetch only; sec.gov contact UA; Wayback `id_`; browser UA for otterly | 137, 144, 142, 141, 109, 47, 49, 48, 39, 31, 159 | proof-scorecard, trigger-timeline, whitespace, skincare-beauty, transition-evidence, ai-ads-evidence, paid-placement, market-potential, agentic-commerce | 35–45 |
| RP2-B | `ext` (one holder) | 110 (Adobe Q3 PDF), 74, 77 llms.txt, 37 | market-potential, high-cpa, skincare-beauty, paid-placement | 12–18 |
| RP2-C | none (image reads) | images A and B save: IAC slide 7, Otterly charts, Adobe pages | as A | 10–15 |

RP2-C exists because the image rule makes reads a separate pass; A can do them inline if the main thread waives that. RP2-B: Adobe Q3 is its only item of weight; the llms.txt and Adthena items are little value.

## Verdict

Worth one short run, not a sweep: RP2-A touches three r2-brief figures (IAC, Otterly Silver, Otterly llms.txt) and one open unknown (Adobe per-engine/organic comparator). Everything else: little value left. Paywall retries: none (0 of 5 opened 2026-09-23).

## Caveats

- Row-to-commit mapping for primaries uses file modification time (13:xx vs 15:xx–16:xx), not git; REPULL-1 and 1b wrote no row log.
- Compiled-cite grep matched filenames plus 40 claim keywords; a claim carried without either is missed.
- REPULL-1b's "primary not located 4" rows are not named in STATE; rows 39, 48 may be among them.
- Probes are one request each from one IP on 2026-09-23; otterly.ai, zendesk.com and courtlistener.com turned from wall to 200 since 2026-09-22 — per-request, may revert.
- Row 91 (StatCounter) and 100 have later pulls that do not cover the queued gap (device splits, image); left `open`.
- No figure was read from any probed page; the value column is a judgment, not a result.

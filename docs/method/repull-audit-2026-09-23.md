# Repull audit — which raw pulls carry a substitute instead of the primary

Date 2026-09-23. Task REPULL-AUDIT. Read-only scan of `docs/raw/` (808 files at last count; 806 at spawn, 2 in-flight files landed during the scan) for pulls that never reached the primary page and recorded a secondary (press coverage, syndication, IR-site copy, aggregator, pointer, snippet, paraphrase, partial capture) instead. Queue: `repull-queue-2026-09-23.csv` (169 rows, 167 distinct raw files; header fixed by the brief). Occasion: the user installed a paywall-bypass extension in the `ext` Chrome profile; question is which of these substitutes it could replace.

Method: (1) machine index of every raw file's header fields (`url_or_doc_id`, `pull_method`, `tier`, `tier_reason`, `supersedes`, `captured`) plus every line matching wall, secondary, and image vocabulary; (2) hand read of the resulting digest for 670 candidate files (header + matched lines, not the full body); (3) hand classification into the queue; (4) grep of each queued filename across `docs/findings`, `docs/markets`, `docs/customers`, `docs/competitors` for the compiled cite. Three files were opened in full (Fortune HubSpot, HubSpot AEO cohort, Fresha bookings), the rest were read through the digest. No web, no browser, no git, no raw file touched.

## Tally

| measure | count | note |
|---|---|---|
| raw files scanned | 808 | all of `docs/raw/` |
| files with any `[note:` marker | 234 | template marker; many are tool-truncation, not walls |
| files matching wall / secondary vocabulary (machine, over-inclusive) | 525 | includes successful `403→ext` pulls that mention the 403 |
| queued after hand read | 167 files / 169 rows | two files carry two distinct walls |
| **secondary carried instead of primary** | **69 files / 70 rows** | relay, pointer, mirror, IR copy, snippet, archive, summary; 42 rows cited by a compiled file |
| partial primary (paywall stub, tool truncation, JS shell, chart-only) | 98 rows | primary reached but incomplete |
| by wall type: bot wall (403 / WAF / Cloudflare / CAPTCHA / 429) | 46 | 31 cited |
| hard paywall (subscription, client seat, Crunchbase Pro, 402) | 21 | 13 cited |
| metered paywall (free paragraphs then wall) | 4 | 1 cited |
| registration / login / download form | 10 | 8 cited |
| JS-rendered shell (no static body) | 12 | 5 cited |
| legal-copyright paraphrase / model-mediated extract | 8 | 1 cited; MozCon paraphrase, WebFetch summaries |
| primary never tried or never located (relay filed instead) | 25 | 13 cited |
| tool truncation of a reached primary (results section cut) | 16 | 6 cited; 104 files show tool truncation overall, only these cut a load-bearing section |
| chart / image / figure not captured | 25 | 3 cited |
| by lane: a / b / c / d / e / f | 31 / 31 / 5 / 11 / 63 / 28 | Lane E carries the most substitutes (trade-press pointers, market forecasts) |
| by tier of the substitute: 1 / 2 / 3 / 4 / 5 / 6 / 7 / n-a | 4 / 10 / 31 / 11 / 63 / 20 / 2 / 28 | tier 5 dominates: trade-press relays of tier 2–4 primaries |
| priority: P1 / P2 / P3 / P4 | 12 / 66 / 80 / 11 | P4 = channel already re-pulled by R-BLOCKED-2 (Reddit via Arctic Shift, Indeed, TED) |
| in-flight files in the queue | 13 | untracked `e-case-*-2026-09-23.md`, `*-repull2-2026-09-23.md` |
| **Images noted** | **83 files** | 38 are `d-paper-*` (generic "figures and tables are images"), 7 `e-case-otterly-*`, rest individual; top 10 below |

Images noted, top 10 by evidentiary weight (queued with `wall_type` starting `chart`): `c-adobe-analytics-q2-2026-traffic-report-2026-09-22.md` (unlabeled y-axis, ambiguous 12% callout); `c-adobe-analytics-q3-2026-traffic-report-2026-09-22.md` (15% callout, pages 13–53 uncaptured); `e-case-seer-interactive-content-recency-2026-09-22.md` (two results charts, Silver-graded case); `e-case-iac-investor-deck-2026-02-03-2026-09-22.md` (50% referral-decline callout not reconcilable with plotted bars); `a-cloudflare-crawl-refer-ratio-blog-2026-09-22.md`; `a-cloudflare-crawler-purpose-industry-blog-2026-09-22.md`; `e-case-jonathanmall-geo-experiment-2026-09-23.md`; `e-case-boily-dental-geo-comparison-2026-09-23.md`; `e-case-otterly-reddit-experiment-2026-09-23.md`; `b-microsoft-ads-in-copilot-2026-09-22.md` (three ad-format images). `a-statcounter-share-ai-chatbot-market-share-2026-09-22.md` is a JS dashboard whose device splits were never rendered.

## Which walls a paywall-bypass extension plausibly helps — reviewer judgment

| wall type | bypass helps? | reason |
|---|---|---|
| metered paywall (Adweek, Bloomberg, Fortune, Business Insider) | yes | these are the extension's target case; 4 metered + most of the 21 hard-paywall rows are publisher paywalls |
| hard paywall on trade press (FT, Sifted, W&V, WWD/Tollbit 402, Trends.vc Pro) | plausible | server-side gating varies; W&V and Sifted return the stub server-side, so success is not assured |
| analyst client seats (Gartner, Forrester $1,495, Statista chart values, EMARKETER, WPP clients-only, Crunchbase Pro, PitchBook) | no | credential-gated, not a cookie or CSS wall; EMARKETER also failed at DNS on this network 2026-09-23 |
| registration / download forms (Datos, Muck Rack report, Pace Generative PDF, Adthena report) | no | form submission is out of scope by repo rule |
| login walls (LinkedIn company pages, Google OAuth on `ai.google.dev/llms.txt`) | no | credential-gated; LinkedIn company headcounts stay snippet-sourced |
| bot walls (Cloudflare, AWS WAF, DataDome, PerimeterX, Akamai, 403/429/405) | no | not a paywall; the plain `ext` browser already clears many (SEL, TED, G2, Upwork reached 2026-09-23); CAPTCHAs never solved per repo rule |
| sec.gov 403 (2026-09-22 only) | no, and unnecessary | Archives returned 200 to fetch on 2026-09-23; the 10 sec.gov rows need a plain re-fetch, not a bypass |
| JS-rendered shells (Peec pricing, Adthena index, Ashby, Framer archives) | no | browser rendering, not paywall; `ext` `get_page_text` is the fix |
| tool truncation, model-mediated WebFetch extracts, chart images | no | agent tooling limits; re-pull with the browser and save data-bearing images to `docs/raw/img/` |
| audio / video primaries (OMR podcast, two YouTube talks) | no | needs a transcript tool |

Net: 20 rows `bypass_helps = yes`, 3 `partial`, 71 `no`, 75 `n/a`. Every P1 row is a `yes`.

## Load-bearing check — priority 1 (compiled cite present and bypass plausibly helps)

| raw file | primary | compiled cite (file:line) | claim carried |
|---|---|---|---|
| `a-bloomberg-scrunch-sitecore-repull-2026-09-23.md` | bloomberg.com 2026-06-03 | `competitors/scrunch-ai.md:32`, `:81` (via the older Scrunch pull) | $225M deal value; 2 paragraphs read |
| `a-promptwatch-funding-2026-09-22.md` | sifted.eu | `competitors/promptwatch.md:6`, `:29`, `:35` | EUR 6M seed; Sifted body obfuscated |
| `b-biggo-sensortower-advertisers-820-2026-09-23.md` | businessinsider.com (URL unrecorded) | `markets/paid-placement.md:133` | 820 ChatGPT advertisers |
| `b-campaign-perplexity-ads-end-2026-09-23.md` | ft.com 2026-02-17 (URL unrecorded) | `markets/paid-placement.md:182` | Perplexity ended ads |
| `b-pymnts-perplexity-ads-end-2026-09-23.md` | same FT article | `findings/ai-ads-evidence.md:53` | same |
| `b-techcrunch-grok-ads-plan-2026-09-23.md` | ft.com 2025-08 (URL unrecorded) | `findings/ai-ads-evidence.md:93` | Grok ads plan |
| `e-case-c8-beautymatter-emarketer-ai-visibility-index-2026-09-22.md` | emarketer.com (slug guessed, 404) | `customers/skincare-beauty.md:73` | beauty AI Visibility Index |
| `e-case-census-c12-2026-09-22.md` | wuv.de third article (URL unrecorded) | `customers/skincare-beauty.md:74` | EU case candidate |
| `e-case-census-c8-2026-09-22.md` | wwd.com (Tollbit 402) | `customers/skincare-beauty.md:72` | beauty coverage never read |
| `e-market-size-emarketer-aiads-paid-2026-09-22.md` | emarketer.com US AI Advertising Forecast 2026 | `markets/paid-placement.md:52`, `:89` | $32.03bn to $68.25bn |
| `e-market-size-emarketer-searchad-paid-2026-09-22.md` | emarketer.com US Search Advertising Forecast 2026 | `markets/organic-recommendation.md:38`; `markets/paid-placement.md:47` | no figure reached |
| `e-market-size-stellagent-agentic-2026-09-22.md` | EMARKETER AI Commerce 2026; Edgar Dunn (URLs unrecorded) | `markets/agentic-commerce.md:41`, `:46`, `:50` | agentic forecasts via a vendor blog |

Also user-named: `e-case-fortune-hubspot-blog-traffic-loss-2026-09-23.md` (fortune.com, in-flight, P3): the fetch captured the op-ed body with `verbatim: partial` and no wall marker; one bypass pass would confirm nothing was cut. Not cited by a compiled file yet.

Priority 2 highlights (cited, bypass unlikely, agent tries once): the 10 sec.gov substitutes (`a-changeagents-funding-filing`, `a-locafy-funding-filing`, `a-hubspot-filing`, `a-yext-filing`, `b-microsoft-fy26-q4-release`, `b-criteo-second-source`, `c-feedonomics-second-source`, `c-wix-second-source` and two mirrors) now fetchable direct; `a-peec-pricing` (JS, cited 12 times in `competitors/peec-ai.md`); `a-muckrack-pricing` / `-customers` / `-method` (Cloudflare, `competitors/muck-rack.md`); `e-case-census-c13` (cited 40 times; Blackbird page never located); `a-funding-crunchbase-pitchbook-repull` (Crunchbase Pro, `customers/high-cpa-regulated.md:104`); `b-court-dockets-table` (4 dockets behind WAF, `markets/agentic-commerce.md:100`); `d-technique-census-c7` / `-c6` (OpenAI Atlas 403 backlog, `findings/whitespace.md:27`).

## Publishers by count

Queue rows by primary domain: sec.gov 10; otterly.ai 9 (chart-only, in-flight); perplexity.ai 7; reddit.com 6; openai.com 6 (+ help.openai.com 4); emarketer.com 4; ft.com 3; wuv.de 3; muckrack.com 3; datos.live 3; comscore.com 3; radyant.io 3; indeed.com 3; ted.europa.eu 3; businesswire.com 2; stocktitan.net 2 (as substitute); crunchbase.com 2; adweek.com 2; gartner.com 2; linkedin.com 2; foundationinc.co 2; youtube.com 2; eur-lex.europa.eu 2; ecfr.gov 2; ftc.gov 2; business.adobe.com 2; blog.cloudflare.com 2; hackerone.com 2; koahlabs.com 2; learn.microsoft.com 2; bloomberg.com 1; sifted.eu 1; businessinsider.com 1; wwd.com 1; pitchbook.com 1; axios.com 1; mckinsey.com 1; fortune.com 1.

Named in the brief but absent from the queue: wsj.com, theinformation.com, nytimes.com, economist.com (no raw file attempted them); digiday.com and adexchanger.com (pulled clean, no wall); searchengineland.com (blocked 2026-09-22, reached by `ext` 2026-09-23 — `e-searchengineland-home-depot-guide-repull-2026-09-23.md`); courtlistener.com (9 dockets reached; only the 4 unopened candidates queued); statista.com and forrester.com (inside the `e-analyst-paywalls-repull` row).

Machine count of raw files that mention a publisher on a wall-marked line (over-inclusive, includes solved 403s): openai.com 35, sec.gov 21, reddit.com 16, courtlistener.com 15, g2.com 15, perplexity.ai 13, capterra.com 11, indeed.com 9, upwork.com 8, emarketer.com 8, searchengineland.com 8, linkedin.com 8, businesswire.com 7, ft.com 6, crunchbase.com 6, ted.europa.eu 6, muckrack.com 5, gartner.com 3, wuv.de 3, forbes.com 3.

## Already re-pulled, not queued

Resolved on 2026-09-23 by R-BLOCKED / R-BLOCKED-2 and excluded: G2 and Capterra category pages (`f-g2-capterra-S4-repull`, CAPTCHA ceiling remains), Google Trends (`f-google-trends-S9-repull`), Upwork logged-out (`f-jobs-upwork-indeed-freelancer-S1-repull`), Search Engine Land Home Depot guide (`e-searchengineland-home-depot-guide-repull`), NerdWallet 8-K (`e-nerdwallet-8k-repull`), EDGAR full-text (`e-edgar-fulltext-repull`, `e-case-edgar-fulltext-results`), Bing webmaster guidelines, Amazon community guidelines, arXiv 2609.06811. Indeed, TED and Reddit rows stay in the queue at P4 because the re-pulls are in flight and partial (Indeed rate-limited after 5 pages; TED XML endpoint WAF outside the tab; Reddit via Arctic Shift).

## Caveats

- Heuristics miss walls the puller never marked: a page that silently served a stub without a `[note:]`, a `pull_method` that omits the failed first attempt, and relays whose `tier_reason` does not say "pointer" or "relay". The 25 "primary never tried" rows are the ones that said so; unstated ones are not counted.
- Heuristics over-count the other way: `403` and `subscriber` appear on lines about successful `403→ext` pulls and about NYT subscriber counts. The 525 machine hits are therefore an upper bound; the 169 queue rows are the hand-read count.
- 670 candidate files were read through the digest (header block plus matched lines), not in full; a wall recorded only in an unmatched body line was not seen. Three files were opened whole.
- `primary_url` is `unknown` in 27 rows because the raw file recorded only the relay; an agent must locate the primary before pulling it.
- Compiled cites were matched on the raw filename. A compiled file that carries the substitute's number through a census or table without naming the raw file (as `competitors/scrunch-ai.md` does for the Bloomberg value) is missed unless spotted by hand; one such case was added by hand, others may exist.
- `bypass_helps` is reviewer judgment, untested: no bypass was tried in this task. Server-side stubs (W&V, Sifted, EMARKETER) may not yield.
- Tool-truncation rows (16 queued of 104 seen) were kept only where the note says a results, methodology, or terms section was cut; the other 88 are marketing-page tails.
- The 38 `d-paper-*` image notes are generic (arXiv figures) and are counted in "Images noted" but not queued row by row; they are reachable as PDFs at any time.
- Priority 4 rows are tied to live agents R-BLOCKED-2 (Reddit, Indeed, TED); if those land differently, re-cut.
- No verdict on which substitute is wrong; a relay may be accurate. The queue lists provenance gaps, not errors.

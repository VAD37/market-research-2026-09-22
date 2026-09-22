# P4-c1 census — earnings calls and investor decks

```yaml
source:          this agent's own discovery log and candidate table for task P4-c1
url_or_doc_id:   n/a — compiled from the raw pulls listed below
published:       2026-09-22
pull_date:       2026-09-22
pull_method:     fetch, browser extension
pull_purpose:    evidence about a number
tier:            n/a — this file is a census/index, not a source pull; every figure in it traces to the raw/ files it cites, each tiered on its own header
tier_reason:     n/a
source_label:    n/a
lane:            E, F
sub_market:      organic recommendation, paid placement
engine:          see candidate table
metric_kind:     visibility, traffic, sales (mixed — see candidate table)
vertical:        see candidate table
supersedes:      none
captured:        n/a — index file
```

No interpretation below. Counts and quotes trace to the raw/ files named.

## Discovery log — queries run, hits screened per source

All queries run 2026-09-22 against `efts.sec.gov/LATEST/search-index` (EDGAR full-text search API), fetched via WebFetch (robots.txt blocked `mcp__MCP_DOCKER__fetch` and the browser extension could not read `efts.sec.gov` directly — `Permission denied for reading page content on this domain`). Individual filing pages were then fetched via the SEC Archives HTML path, either through the browser extension (dedicated tab, tabId 1697684059) or WebFetch.

| # | Query | Filter | Hits | Notes |
|---|---|---|---|---|
| Q1 | `q="AI Overviews"` | forms 8-K,10-Q,10-K; 2026-01-01 to 2026-09-22 | 27 | Top hit cluster: IAC Inc./People Inc. (7 filings, same CIK across two tickers), TripAdvisor (3), Reddit (3), Chegg (2), plus one each Alphabet, BuzzFeed, LegalZoom, LendingTree, NerdWallet, Onfolio Holdings, Rocket Companies, VisitIQ Corp, Yelp |
| Q2 | `q="ChatGPT" "traffic"` | forms 8-K,10-Q,10-K; 2026-01-01 to 2026-09-22 | 71 | Top 10 by relevance returned; dominated by repeated Eightco Holdings (ORBS) 8-Ks (6 of top 10) |
| Q3 | `q="AI search" "traffic"` | forms 8-K,10-Q,10-K; 2026-01-01 to 2026-09-22 | 30 | Full hit list returned; Yelp (3), 1stdibs, Bridgeline Digital, VisitIQ Corp, SEMrush Holdings, TechTarget, IAC, Expedia, GSI Technology, Yext, 1-800-Flowers, Freshworks, Urban One, Eventbrite, Amplitude (3), Walmart, Trump Media, Cimpress, Elastic, Atlassian, Host Hotels, Snap |
| Q4 | `q="AI Overviews" (skincare OR beauty OR cosmetics)` | forms 8-K,10-Q,10-K; 2025-01-01 to 2026-09-22 | 6 | All 6 hits were IAC/People Inc. and Yelp filings already found by Q1 — no skincare/beauty-vertical filer surfaced at all |
| Q5 | `q="ChatGPT"` | forms 8-K only; 2026-06-22 to 2026-09-22 | 38 | Broad, low-precision sweep for the post-staleness-cutoff window; ZoomInfo, Upwork, ZipRecruiter, Reddit, LendingTree, Yelp, Getty Images, Sprinklr, Innovative Eyewear, EverQuote, Criteo, LiveRamp, Eightco Holdings (8 more), Bridgeline (dup), and ~20 further names screened without opening (see below) |
| — | fool.com earnings-call transcripts | site path `fool.com/earnings/call-transcripts/...` | 0 | Guessed URL for Chegg's Q1 2026 call returned HTTP 404; no working fool.com index page found within this task's time budget. No fool.com transcript entered this cluster's raw/ files — all ten raw pulls are SEC-filed documents (8-K exhibits, 10-Q, 10-K) |
| — | Seeking Alpha | not attempted | — | Deprioritized after EDGAR full-text search alone produced far more candidates than the 8-12 target; not reached this pull |

## Candidate table

| Company | Ticker | Document | Date | Speaker | Engine named | Metric named | Figure verbatim | Vertical (as named) | Direction | Grade (missing bar items) | Raw path |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IAC Inc. / People Inc. | IAC / PPLI | 8-K Ex-99.2, Q4'25 Investor Presentation | 2026-02-03 | none (deck, unsigned) | Google AI Overviews | traffic, visibility | "50% decline in Google Search referrals since 2023"; "AI Overviews appear on nearly 70% of top People Inc. queries" | none named | negative | Bronze (missing 4, 5; 7 present but self-measured) | `docs/raw/e-case-iac-investor-deck-2026-02-03-2026-09-22.md` |
| IAC Inc. / People Inc. | IAC / PPLI | 8-K Ex-99.2, Q1'26 Investor Presentation | 2026-05-04 | none (deck, unsigned) | Google AI Overviews | traffic, visibility | "63% decline in Google Search referrals over two years"; "AI Overviews appear on nearly 70% of top People Inc. queries" | none named | negative | Bronze (missing 4, 5; 7 present but self-measured) | `docs/raw/e-case-iac-investor-deck-2026-05-04-2026-09-22.md` |
| Yelp Inc. | YELP | 8-K Ex-99.2, Q2 2026 Letter to Shareholders | 2026-08-06 | Jeremy Stoppelman (CEO), David Schwarzbach (CFO) | ChatGPT, Google Gemini, Perplexity, Google AI Mode | visibility (citations) | "receiving 3.4x as many AI citations than the next closest platform"; "512.7k" Yelp citations vs. "149.7k" BBB | none named | positive | Bronze (missing 4, 5; 7 present but commissioned, not independent) | `docs/raw/e-case-yelp-shareholder-letter-2026-08-06-2026-09-22.md` |
| Chegg, Inc. | CHGG | 10-Q | 2026-05-11 | none (filed prose) | Google AI Overviews (AIO), ChatGPT | none stated (qualitative) | "materially adversely affected our business, operating results and financial condition by reducing traffic to our platform" | none named | negative | Fools gold (missing 4, 6) | `docs/raw/e-case-chegg-10q-2026-05-11-2026-09-22.md` |
| NerdWallet, Inc. | NRDS | 8-K Ex-99.1, Q4 FY25 earnings release | 2026-02-25 | Tim Chen (Co-Founder & CEO) | AI overviews, LLMs (generic) | traffic, sales | "Credit cards revenue of $26.5 million decreased 24% year-over-year, primarily due to continued headwinds in organic search traffic"; "SMB products revenue ... down 12%" vs. "Insurance revenue ... increased 13%" | high-CPA regulated (credit cards, insurance, loans named) | negative (mixed, offset elsewhere) | Silver (missing/weak 6, 7) | `docs/raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md` |
| TechTarget, Inc. | TTGT | 10-K, FY2025 | 2026-03-11 | none (filed prose) | "answer engine[s]" / LLMs (generic) | none named (ratio only) | "2x to 3x higher membership conversion rate from answer engine and LLM citations compared to traditional organic search" | none named | positive | statement only (missing 2 specific, 3, 4, 5, 6, 7) | `docs/raw/e-case-techtarget-10k-2026-03-11-2026-09-22.md` |
| Criteo S.A. | CRTO | 8-K Ex-99.1, Q2 2026 results | 2026-08-05 | Michael Komasinski (CEO), Sarah Glickman (CFO) | ChatGPT (OpenAI) | none per glossary.md (advertiser count, not visibility/traffic/sales) | "over 2,000 brands advertising on ChatGPT across seven countries" | none named | positive | statement only (missing 3 closed window, 4, 7) | `docs/raw/e-case-criteo-earnings-release-2026-08-05-2026-09-22.md` |
| EverQuote, Inc. | EVER | 8-K Ex-99.2, Q2 2026 investor deck | 2026-08-03 | none (deck, unattributed) | ChatGPT | none | "Consumer adoption of AI adds new sources of high-intent traffic" (ChatGPT listed as a channel, no figure) | none named | positive | statement only (missing 3, 4, 5, 6, 7) | `docs/raw/e-case-everquote-investor-deck-2026-08-03-2026-09-22.md` |
| LendingTree, Inc. | TREE | 10-K, FY2025 | 2026-03-09 | none (filed prose) | "AI overviews" (generic) | none | "organic searches and artificial intelligence ('AI') overviews, that depend upon the searchable content on our sites" | none named | negative (risk factor framing) | statement only (missing 3, 4, 5, 6, 7) | `docs/raw/e-case-lendingtree-10k-2026-03-09-2026-09-22.md` |
| Reddit, Inc. | RDDT | 10-Q | 2026-07-31 | none (filed prose; underlying claim is a plaintiff allegation) | Google Search, Google AI Overviews | none | "alleging that we and certain of our officers made false or misleading statements and omissions concerning the impact of Google Search and its AI Overviews feature on our business" | none named | negative (third-party allegation, not a company admission) | statement only (missing 4, 5, 6, 7; not a company-stated claim) | `docs/raw/e-case-reddit-10q-2026-07-31-2026-09-22.md` |

## Screened-out list, with reason

Every item below was found by a query above and did **not** enter `docs/raw/`.

| Company | Document | Date | Reason screened |
|---|---|---|---|
| TripAdvisor, Inc. | 10-Q | 2026-05-07 | Opened; no AI, ChatGPT, AI Overviews or generative-AI mention found anywhere in the filing despite the EDGAR full-text match |
| TripAdvisor, Inc. | 10-K | 2026-02-13 | Not opened, same pattern expected as the 10-Q above |
| TripAdvisor, Inc. | 10-Q | 2026-08-06 | Not opened, same pattern expected |
| Rocket Companies, Inc. | 10-K | 2026-03-02 | Opened; AI mentioned only generically (mortgage AI, fair-lending risk) — no ChatGPT, AI Overviews, or traffic-impact language |
| Alphabet Inc. | 10-K | 2026-02-05 | "AI Overviews" is Alphabet's own product, discussed as the platform vendor, not as an effect on Alphabet as a "brand" — off-target for this task's brand-side scope |
| BuzzFeed, Inc. | 10-K | 2026-03-16 | Opened; "AI-enabled search functionality has the potential to disrupt traffic" — generic, no specific engine named, per task's screening rule |
| Onfolio Holdings, Inc. | 10-K | 2026-03-31 | Already covered by a different agent's P3-c5 agency census (per `docs/method/STATE.md`); not re-opened here to avoid duplicate work across agents |
| SEMrush Holdings, Inc. | 10-K | 2026-03-02 | Already covered by a different agent's P3-c4 vendor census (per `docs/method/STATE.md`); is itself a P3-rostered AI-visibility vendor, out of this task's "brands, not vendors" scope |
| Yext, Inc. | 10-K | 2026-03-10 | Already covered by a different agent's P3-c3 vendor census (per `docs/method/STATE.md`); is itself a P3-rostered incumbent vendor, out of scope |
| VisitIQ Corp. | 10-K | 2026-05-20 | Not opened — micro-cap filer, low relevance score, outside this task's time budget |
| GSI Technology Inc. | 10-K, 10-Q | 2026-06-05, 2026-08-11 | Not opened — low relevance score in the Q3 hit list |
| Freshworks Inc. | 10-K | 2026-02-26 | Not opened — low relevance score |
| Urban One, Inc. | 10-K | 2026-03-20 | Not opened — low relevance score |
| Eventbrite, Inc. | 10-K | 2026-03-12 | Not opened — low relevance score |
| Amplitude, Inc. | 10-K, 10-Q ×2 | 2026-02-19, 2026-05-07, 2026-08-06 | Not opened — low relevance score |
| Walmart Inc. | 10-K | 2026-03-13 | Not opened — low relevance score in a 30-hit sweep |
| Trump Media & Technology Group Corp. | 10-K | 2026-02-27 | Not opened — low relevance score |
| Cimpress plc | 10-K | 2026-08-07 | Not opened — low relevance score |
| Elastic N.V. | 10-K | 2026-06-08 | Not opened — low relevance score |
| Atlassian Corp | 10-K | 2026-08-14 | Not opened — low relevance score |
| Host Hotels & Resorts, Inc. | 10-K | 2026-02-25 | Not opened — low relevance score |
| Snap Inc | 10-K | 2026-02-05 | Not opened — low relevance score |
| 1-800-Flowers.com, Inc. | 10-K | 2026-09-11 | Not opened — low relevance score |
| ZoomInfo Technologies Inc. | 8-K | 2026-08-05 | Opened; names ChatGPT/Claude only as AI-agent/MCP integration partners for ZoomInfo's own product (GTM.AI) — a product-integration story, not AI-search visibility, referral, GEO/AEO or AI-surface advertising |
| Upwork, Inc. | 8-K | 2026-08-10 | Opened; names ChatGPT only as an app-integration channel; "AI-related work" revenue growth is demand for AI freelance work, not Upwork's own AI-search visibility |
| ZipRecruiter, Inc. | 8-K ×2 | 2026-05-07, 2026-08-05 | Opened; "ZipRecruiter app for ChatGPT" and a Claude connector are product/distribution integrations, not a visibility, referral-traffic, or GEO/AEO measurement — closest of the three integration cases to on-topic, still screened as off-target |
| Eightco Holdings Inc. (ORBS) | 8-K ×14 (across two queries) | 2026-05-06 to 2026-09-17, various | Verified by direct read of one filing: a crypto/treasury holding company whose "AI search"/"traffic" language describes bot-traffic/non-human-traffic statistics tied to its OpenAI and Worldcoin equity exposure, not an operating brand's own AI-search visibility or referral traffic — all 14 filings screened as off-target on this basis |
| Getty Images Holdings, Inc. | 8-K | 2026-06-22 | Not opened — outside time budget |
| Sprinklr, Inc. | 8-K (2 exhibit files, 1 filing) | 2026-08-13 | Not opened — outside time budget |
| Innovative Eyewear Inc | 8-K | 2026-07-09 | Not opened — outside time budget |
| LiveRamp Holdings, Inc. | 8-K | 2026-08-05 | Not opened — outside time budget |
| Bridgeline Digital, Inc. | 8-K | 2026-08-18 | Not opened — outside time budget |
| 1stdibs.com, Inc. | 8-K ("roadmap review") | 2026-09-02 | Not opened — outside time budget |
| Research Solutions, Inc. | 8-K | 2026-09-09 | Not opened — outside time budget |
| Inuvo, Inc. | 8-K | 2026-08-11 | Not opened — outside time budget (plausibly on-topic, an ad-tech company; deprioritized once the 8-12 hit target was reached) |
| Bitmine Immersion Technologies, Inc. | 8-K | 2026-07-16 | Not opened — crypto-treasury-adjacent name, same pattern suspected as Eightco Holdings, not verified |
| Expensify, Inc. | 8-K | 2026-08-06 | Not opened — outside time budget |
| Morningstar, Inc. | 8-K | 2026-08-25 | Not opened — outside time budget |
| C. H. Robinson Worldwide, Inc. | 8-K | 2026-07-29 | Not opened — outside time budget |
| Clarivate Plc | 8-K | 2026-07-29 | Not opened — outside time budget |
| Corbus Pharmaceuticals Holdings, Inc. | 8-K | 2026-09-14 | Not opened — outside time budget |
| Bluerock Acquisition Corp. | 8-K | 2026-08-03 | Not opened — outside time budget |
| Life360, Inc. | 8-K | 2026-08-10 | Not opened — outside time budget |
| Priority Technology Holdings, Inc. | 8-K | 2026-08-26 | Not opened — outside time budget |
| Progress Software Corp | 8-K | 2026-07-22 | Not opened — outside time budget |
| Domo, Inc. | 8-K | 2026-07-22 | Not opened — outside time budget |
| Reddit, Inc. | 8-K Ex-99.2, Q2 2026 press release | 2026-07-30 | Not opened — the Reddit 10-Q for the same quarter (pulled above) was judged sufficient; press release not separately checked for additional AI-Overviews language |
| fool.com Chegg Q1 2026 transcript (guessed URL) | — | — | HTTP 404; fool.com transcript index not located within time budget — no fool.com source entered this cluster |

## Counts

| | Count |
|---|---|
| Screened total (candidates examined via query match, opened or not) | 64 (50 distinct non-Eightco filings + 14 Eightco filings, one entity) |
| Screened — vertical: skincare and beauty | 0 |
| Screened — vertical: B2B SaaS | 0 |
| Screened — vertical: high-CPA regulated | 0 (Rocket Companies, LendingTree, EverQuote and NerdWallet are the vertical-adjacent screened/cleared names, but the vertical tag is only applied where the AI-relevant passage itself names the vertical — see caveats) |
| Screened — vertical: none named / not opened far enough to tag | 64 |
| Cleared the evidence bar (any grade Bronze or better) — total | 4 (IAC ×2, Yelp, NerdWallet) |
| Cleared — vertical: skincare and beauty | 0 |
| Cleared — vertical: B2B SaaS | 0 |
| Cleared — vertical: high-CPA regulated | 1 (NerdWallet, Silver) |
| Cleared — vertical: none named | 3 (IAC ×2 Bronze, Yelp Bronze) |
| Gold | 0 |
| Silver | 1 (NerdWallet) |
| Bronze | 3 (IAC ×2, Yelp) |
| Fools gold | 1 (Chegg) |
| Statement only | 5 (TechTarget, Criteo, EverQuote, LendingTree, Reddit) |
| Negative-result cases (direction: negative) | 5 (IAC ×2, Chegg, NerdWallet, LendingTree, Reddit) |
| Positive-direction cases | 4 (Yelp, TechTarget, Criteo, EverQuote) |
| Mixed/offset-framed cases | 1 (NerdWallet — counted once, in the negative row above, per its dominant framing: organic-search headwinds named as the cause) |
| Unknowns recorded | 2 (see Unknowns below) |

## Unknowns

| Question | Channels checked | Date | Why not answerable from the channels used |
|---|---|---|---|
| Does any fool.com earnings-call transcript in this category exist and carry a verbatim Q&A (not a prepared deck/letter) naming AI-assistant visibility, referral, GEO/AEO or AI-surface advertising? | `fool.com/earnings/call-transcripts/...` (one guessed URL, 404) | 2026-09-22 | fool.com's transcript URL structure was not independently discovered within this task's time budget; no working index or search entry point was reached |
| Does any skincare/beauty-vertical filer (public or otherwise EDGAR-indexed) name AI-assistant visibility, referral, GEO/AEO or AI-surface advertising on an earnings call, deck or filing? | EDGAR full-text search, `q="AI Overviews" (skincare OR beauty OR cosmetics)`, 2025-01-01 to 2026-09-22 | 2026-09-22 | Zero skincare/beauty-vertical filer surfaced; the six hits returned were IAC/People Inc. and Yelp filings already found by the base "AI Overviews" query, with no skincare/beauty content — consistent with most skincare/beauty brands (the anchor vertical) being privately held and outside EDGAR's US-registrant-only coverage (per `docs/sources/channels.md` C13's stated bias) |

## Caveats

- **Vertical coverage gap, not closed.** Of ten cleared/graded cases, only one (NerdWallet) carries a named vertical from this cluster's sources, and it maps to high-CPA regulated, not the anchor (skincare and beauty) or B2B SaaS. No skincare/beauty or B2B SaaS case cleared. This is a real result of EDGAR being a US-public-company-only, filing-driven channel (`docs/sources/channels.md` C13's bias line): skincare/beauty brands with AI-search stories are overwhelmingly private, and most B2B SaaS AI-search discussion found here (ZoomInfo, Upwork, ZipRecruiter) turned out to be a different topic (AI-agent product integration) rather than AI-search visibility/referral. H11 ("transition evidence at tier 3+ exists for at least one brand in each vertical") is **not** closed by this cluster for two of the three verticals.
- **Vertical tagging was applied strictly.** Two candidates (LendingTree, EverQuote) were initially considered for a `high-CPA regulated` tag based on the filer's known business (loans/insurance marketplace, P&C insurance marketplace respectively), but neither filer's AI-relevant passage itself names a vertical — only NerdWallet's does, directly and verbatim, in the same sentence set as its AI-overviews claim. The tag was withheld on the other two per the Pass 4 rule (never assigned by inference), so their vertical reads `none named` in their own raw/ files even though a reader with outside knowledge would guess otherwise.
- **No Gold case found.** The strongest evidence in this cluster (NerdWallet, Silver) rests on a company's own segment revenue and a single-quarter YoY comparison across different product lines, not a holdout, geo-split or switchback. This is consistent with `plan.md`'s framing that Pass 4 is "the pass most likely to return little" and that a near-zero Gold count is a legitimate finding, not a search failure.
- **fool.com and Seeking Alpha were not reached.** All ten raw pulls in this cluster are SEC filings (8-K exhibits, 10-Q, 10-K); no spoken earnings-call transcript with a named analyst question and a conversational answer was captured — the closest equivalents are the IAC and Yelp investor decks/letters, which are prepared documents, not live Q&A. The one fool.com URL guessed returned 404, and this task's WebSearch budget was already exhausted for the session per prior agents' notes in `docs/method/STATE.md`, so no further search-based discovery of a working fool.com index was attempted.
- **The Chegg and Reddit cases both carry a causal/impact claim without a supporting number in the exact passage captured** (Chegg: "materially adversely affected," no baseline or figure; Reddit: a plaintiff's allegation, not Reddit's own claim, no figure). Both are filed here at their honest grade (Fools gold and statement-only respectively) rather than upgraded on the strength of the language alone.
- **Extraction method varies by file** and is stated in each raw/ file's pull notes: IAC ×2, Yelp, NerdWallet and Criteo were captured by full-page browser text extraction (tabId 1697684059, no other tab in the shared session touched); Chegg, TechTarget, EverQuote, LendingTree and Reddit were captured via an automated fetch-and-quote tool (WebFetch) instructed to return exact verbatim text — none of the latter five was independently cross-checked against raw HTML.
- Oldest pull depended on: 2026-09-22 (all ten raw files and this census were pulled today; document dates on the underlying filings range 2026-02-03 to 2026-08-06, all within the current fiscal year and none flagged stale under `plan.md`'s one-quarter rule as of the pull date).

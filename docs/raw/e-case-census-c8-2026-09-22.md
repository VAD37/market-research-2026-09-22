# P4-c8 census — skincare and beauty vertical sweep, second sweep

```yaml
source:          this agent's own discovery log and candidate table for task P4-c8
url_or_doc_id:   n/a — compiled from the raw pulls listed below
published:       2026-09-22
pull_date:       2026-09-22
pull_method:     fetch (WebFetch only — fetch-only agent per task brief, no browser extension, no Playwright)
pull_purpose:    evidence about a number
tier:            n/a — this file is a census/index, not a source pull; every figure traces to the raw/ files it cites, each tiered on its own header
tier_reason:     n/a
source_label:    n/a
lane:            E, F
sub_market:      organic recommendation, agentic commerce
engine:          see candidate table
metric_kind:     visibility, traffic, sales (mixed — see candidate table)
vertical:        skincare and beauty (anchor) — see candidate table for sub-category as each source names it
supersedes:      none
captured:        n/a — index file
```

No interpretation below. Counts and quotes trace to the raw/ files named. Task scope: brands, retailers, agencies or vendors that have published a result about AI-assistant visibility, AI referral traffic, or AI-attributed sales for a skincare/beauty brand, priority order per brief: brand IR/newsroom > beauty trade press (pointer, tier 5) > DTC founder write-ups > vendor/agency cases tagged beauty > negative results.

## Discovery log — sources and paths checked, hits screened per source

| # | Source / channel | Query or path | Result | Hits screened |
|---|---|---|---|---|
| 1 | Profound newsroom (`tryprofound.com/newsroom`) | direct fetch, requested link list | Found "Estée Lauder Companies Announces Partnership with Profound" (15 Sep 2026) and its `cosmeticsbusiness.com` trade-press pickup | 2 (both pulled) |
| 2 | Estée Lauder Companies own site | `elcompanies.com/en/news`, `elcompanies.com/en/news/press-releases` | Both HTTP 404 — correct newsroom URL structure not located this session | 0 opened; not recovered |
| 3 | e.l.f. Beauty investor site | `elfbeauty.com/investors/news-events/press-releases` | HTTP 200, but no press-release content resolved in the fetched nav/header shell — no AI-related headline confirmed present or absent | 1 opened, inconclusive |
| 4 | Coty | `coty.com/newsroom` (404); `ir.coty.com` (DNS not found) | Both unreachable | 0 |
| 5 | Olaplex | `investors.olaplex.com/news-events/news` (DNS not found) | Unreachable | 0 |
| 6 | Beiersdorf | `beiersdorf.com/media/media-releases` (404) | Unreachable | 0 |
| 7 | Ulta Beauty, Sephora/LVMH, Shiseido, L'Oréal own IR/newsroom | not attempted this session | — | 0 — see Unknowns |
| 8 | SEC EDGAR full-text search | `efts.sec.gov/LATEST/search-index?q="ChatGPT"&forms=8-K&startdt=2026-01-01&enddt=2026-09-22` | 98 hits; top companies Eightco Holdings, Morningstar, C. H. Robinson, Life360, Getty Images, ZipRecruiter, Applied Digital — none a skincare/beauty-vertical filer | 98 screened (by company-name scan of returned list), 0 opened individually, 0 beauty |
| 9 | SEC EDGAR (reused finding) | `docs/raw/e-case-census-c1-2026-09-22.md` Q4: `q="AI Overviews" (skincare OR beauty OR cosmetics)`, 2025-01-01 to 2026-09-22 | 6 hits, all IAC/People Inc. and Yelp (already known, off-vertical) — zero skincare/beauty filer, per prior task; not re-run | 6 (reused, not re-screened) |
| 10 | Cosmetics Business | `cosmeticsbusiness.com/search?q=AI+search+visibility` | "(0 records)" on-site search | 0 |
| 11 | BeautyMatter | direct search-page fetch, `q=AI+search+visibility` | 6 headlines returned | 6 screened, 3 opened and pulled (eMarketer index, Ulta/Google agentic, Stella Rising webinar), 3 screened-not-opened (stale/duplicate, see screened-out list) |
| 12 | Glossy | `glossy.co/tag/artificial-intelligence/` (404); `glossy.co/beauty/` archive (no AI content in recent listing); `glossy.co/?s=ChatGPT` (8 headlines); `glossy.co/?s=AI+Overviews+traffic+decline` (0 relevant); `glossy.co/?s=AI+visibility+no+lift+beauty` (1 paywalled, stale, off-target) | 8 headlines from the ChatGPT query | 8 screened, 4 opened and pulled (Sephora/Google, Beauty Briefing, 5W citations, E.l.f. Chopra), 4 screened-not-opened (off-vertical or duplicate, see screened-out list) |
| 13 | Beauty Independent | `beautyindependent.com/?s=AI+search` | 1 relevant title surfaced ("907 pages" of results, only title-level reviewed) | 1 screened, 0 opened as a case (off-target on read) |
| 14 | WWD | `wwd.com/?s=...` → 307 redirect to `tollbit.wwd.com/?s=...` → HTTP 402 Payment Required | Paywalled, blocked | 0 |
| 15 | 5W AI Communications (primary for the Glossy citation-share article) | `5wpr.com/new/news/` | HTTP 404 | 0 — primary unreached, Glossy filed as pointer |
| 16 | eMarketer (primary for the BeautyMatter index article) | `emarketer.com/content/ai-visibility-index-beauty-personal-care-q1-2026` (guessed slug) | HTTP 404 | 0 — primary unreached, BeautyMatter filed as pointer |
| 17 | Stella Rising (agency named in the webinar recap) | `stellarising.com/case-studies` | HTTP 404 | 0 |
| 18 | Hacker News via Algolia | `hn.algolia.com/api/v1/search?query=skincare beauty AI search visibility` | 0 hits | 0 |
| 19 | DuckDuckGo HTML | 2 queries (`"eMarketer" "AI Visibility Index" beauty`; skincare-brand-founder Medium/Substack query) | Both HTTP 403 | 0 — channel blocked this session |
| 20 | Reddit (r/SkincareAddiction, for negative results) | `reddit.com/r/SkincareAddiction/search.json?q=ChatGPT recommend` | Fetch tool refused (`Claude Code is unable to fetch from www.reddit.com`) | 0 — channel blocked this session |
| 21 | Existing `docs/raw/` files (reused, not re-pulled) | grep for beauty-brand names across all prior `docs/raw/` pulls | Found beauty-relevant passages in `a-profound-funding-2026-09-22.md`, `a-athenahq-customers-2026-09-22.md`, `a-brandlight-customers-2026-09-22.md`, `a-brandlight-funding-2026-09-22.md` — none carries a graded case (logo mentions or a no-metric partnership announcement only) | 4 files reused as leads, 0 re-pulled as new c8 cases |

## Candidate table

| # | Brand | Sub-category (as named) | Source type | Date | Engines named | Metric | Figure, verbatim | Direction | Grade (missing items) | Paid by outcome | Raw path |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | E.l.f. Beauty | colour cosmetics | brand-own quote via trade press (Glossy) | 2026-04-01 | ChatGPT, Google | visibility (discovery share, no base) | "almost 60% of discovery is happening on LLMs, specifically ChatGPT and Google" — Ekta Chopra, CDO | positive | statement only (missing 3, 4, 6, 7) | n/a | `docs/raw/e-case-c8-elf-beauty-chopra-llm-discovery-2026-09-22.md` |
| 2 | The Estée Lauder Companies | multi-category (skincare, colour cosmetics, fragrance, haircare — 25 brands named) | brand-own press release (Business Wire, hosted on vendor newsroom) | 2026-09-15 | ChatGPT, Gemini | none | partnership announcement only, no metric | n/a | screened — no claim | unknown | `docs/raw/e-case-c8-estee-lauder-profound-partnership-2026-09-22.md` |
| 3 | The Estée Lauder Companies | beauty, "MAC Cosmetics and Jo Malone London" named | trade press pointer (Cosmetics Business) | 2026-09-15 | ChatGPT, Gemini, Claude | none | same announcement, no metric | n/a | screened — no claim | unknown | `docs/raw/e-case-c8-cosmeticsbusiness-estee-lauder-profound-2026-09-22.md` |
| 4 | La Roche-Posay, CeraVe, Neutrogena, Vanicream, Dior + 15 more | facial skincare, bodycare, fragrance, haircare, colour cosmetics | trade press pointer (BeautyMatter) citing eMarketer AI Visibility Index | 2026-04-23 (Q1 2026 data) | unnamed ("AI-generated product recommendations") | visibility (appearance rate) | "La Roche-Posay leads... 22%... CeraVe at 20%"; "facial skincare, La Roche-Posay appears in 81% of queries" | positive (leaders), neutral (ranking) | Bronze (missing 2, 4-full, 5, 6, 7-full) | unknown | `docs/raw/e-case-c8-beautymatter-emarketer-ai-visibility-index-2026-09-22.md` |
| 5 | The Ordinary, CeraVe, La Roche-Posay, Charlotte Tilbury, Rare Beauty, Drunk Elephant, Estée Lauder | skincare, colour cosmetics | trade press pointer (Glossy) citing 5W AI Communications | 2026-07-15 | ChatGPT, Claude, Perplexity, Google AI Overviews | visibility (citation rate) | "The Ordinary... appeared in 7% of responses... Charlotte Tilbury... appearing in 4.5% of AI citations" | positive (leaders), negative-framed (legacy brands, Estée Lauder rank 18) | Bronze (missing 3, 4, 5, 6; 7 partial) | unknown | `docs/raw/e-case-c8-glossy-5w-ai-beauty-citations-2026-09-22.md` |
| 6 | Sephora | skin-care diagnostics, beauty broadly | brand-own quote via trade press (Glossy), conference talk | 2026-06-03 | Sephora's own "AI Beauty Chat"/"Smart Skin Scan" (proprietary, not third-party) | sales (same-day purchase rate), traffic-adjacent (completion rate) | "more than 80%... complete it"; "More than 20%... make a purchase the same day" | positive | Fools gold (missing 3, 4, 6; 2 partial) | n/a | `docs/raw/e-case-c8-glossy-sephora-google-ai-2026-09-22.md` |
| 7 | Amazon (Rufus), Ulta Beauty, LVMH/Sephora — mixed, no single beauty-brand-own AI metric | retail/omni-category | trade press pointer (Glossy) citing NielsenIQ, Tinuiti, Amazon, Ulta, LVMH, Circana | 2026-05-12 | ChatGPT (Sephora), Google Gemini (Ulta), Amazon Rufus | traffic (search volume), sales (mostly not AI-attributed) | "over 1 billion beauty-related searches per week on ChatGPT"; Rufus users "spent 80% more" (Nov-Dec 2025); Ulta net sales "+11.8% to $3.9B" | mixed — Rufus positive (self-reported), rest screened — no claim | Fools gold (Rufus row only; missing 3-full, 4, 6); screened — no claim (all other rows) | unknown | `docs/raw/e-case-c8-glossy-beauty-briefing-sephora-ulta-ai-2026-09-22.md` |
| 8 | Ulta Beauty | beauty broadly | brand-own quotes via trade press (BeautyMatter), launch event | 2026-04-24 | Google Gemini, AI Mode in Search, UCP, Gemini Enterprise | none | agentic-commerce launch announcement only, no metric | n/a | screened — no claim | n/a | `docs/raw/e-case-c8-beautymatter-ulta-google-agentic-2026-09-22.md` |
| 9 | none — category-level, no single beauty brand named | beauty, category-wide | trade press pointer (BeautyMatter) citing Stella Rising (agency), Adobe Analytics, BCG/WWD | 2026-08-02 | ChatGPT, Google AI Overviews (user-count context only) | traffic (AI referral traffic growth, category-wide) | "AI referral traffic has increased 393% year over year" (Adobe Analytics, not beauty-specific) | n/a (category-level) | screened — no claim (item 1 fails — no brand) | n/a | `docs/raw/e-case-c8-beautymatter-stella-rising-geo-webinar-2026-09-22.md` |

## Screened-out list, with reason

| Item | Source | Reason screened |
|---|---|---|
| "The Knot joins OpenAI's ChatGPT ad test as brands rethink AI visibility" | Glossy | off-vertical — wedding/events, not skincare or beauty |
| "How Thorne is leveraging an AI-powered wellness advisor in the ChatGPT era" | Glossy | off-vertical — supplements/wellness, not skincare or beauty per the vertical overlay tokens |
| "How Aviator Nation is preparing for AI-led shopping" | Glossy | off-vertical — apparel |
| "Beauty & Wellness Briefing: How brands are preparing for AI-driven GEO search as consumers embrace ChatGPT" | Glossy | not opened — duplicate ground already covered by the two Beauty Briefing/Sephora-Ulta pieces pulled; deprioritized once the 8-12 target was in reach |
| "Glossy+ Research: The marketer's guide to AI applications, agentic AI, AI search and GEO/AEO in 2026" | Glossy+ (paywalled) | not opened — paywalled tier, dated Nov 2025 (stale, before 2026-06-22), and a general marketer's guide, not beauty-specific or a graded case |
| "10 Takeaways from Webinar Cracking the Code on Search: SEO vs. GEO" | BeautyMatter | not opened — dated Nov 4, 2025, stale (before 2026-06-22), and not the primary source for any figure pulled |
| "From SEO to GEO: How ChatGPT Is Rewriting Beauty's Search Playbook" | BeautyMatter | not opened — dated Sep 28, 2025, stale (before 2026-06-22), member-exclusive |
| "Intent over Influence: How Agentic AI Is Reshaping Beauty Discovery" | BeautyMatter | not opened — deprioritized once the 8-12 target was in reach; not the primary source for any figure pulled |
| "The Phia Controversy And The Flaws In Affiliate Attribution" | Beauty Independent | opened at snippet level; off-target — covers an AI shopping assistant's affiliate-commission dispute, not a beauty brand's own AI-visibility, referral-traffic, or AI-sales result |
| Glossy `?s=AI+Overviews+traffic+decline` search | Glossy | 0 relevant results — only an off-topic H&M merchandising article returned |
| e.l.f. Beauty investor press-releases page | elfbeauty.com | opened but inconclusive — page shell resolved without press-release list content in the fetched markdown; not confirmed present or absent |

## Counts

| | Count |
|---|---|
| Screened total (candidate items examined via search/page, opened or not, per Discovery log) | approx. 133 (98 EDGAR ChatGPT-8-K hits scanned by company name + 6 EDGAR beauty-tagged hits reused from c1 + 6 BeautyMatter search hits + 8 Glossy ChatGPT-search hits + 1 Beauty Independent hit + 4 reused existing-raw-file leads + 10 named-but-unopened trade-press headlines above) |
| Opened (pages actually fetched and read this session) | 9 pulled as raw files + 6 additional pages opened but not pulled (elfbeauty.com press-releases page, Beauty Independent snippet page, cosmeticsbusiness.com search page, Glossy beauty archive page, Glossy 2 negative-search pages, BeautyMatter search-results page) = 15 |
| Cases pulled into `docs/raw/e-case-c8-*` | 9 |
| Graded (per grading rule 1 — carries a metric, ticked against the seven items) | 4 (E.l.f. Beauty statement-only; eMarketer/BeautyMatter Bronze; 5W/Glossy Bronze; Sephora Fools gold; Beauty Briefing Fools-gold-row) — 5 rows across 4 files, see table |
| Screened — no claim (no metric; not graded per rule 1) | 5 files fully (ELC/Profound ×2, Ulta/Google agentic, Stella Rising webinar) plus multiple embedded sub-claims inside the Beauty Briefing file |
| Screened — not opened | 10 (screened-out list above) |
| Cleared the evidence bar (Bronze or better) | 2 — both Bronze: eMarketer/BeautyMatter (row 4), 5W/Glossy (row 5). Zero Silver, zero Gold |
| Gold | 0 |
| Silver | 0 |
| Bronze | 2 |
| Fools gold | 2 (Sephora AI Beauty Chat/Smart Skin Scan; Amazon Rufus row inside the Beauty Briefing file) |
| Statement only | 1 (E.l.f. Beauty) |
| Negative-result cases (direction: negative) | 0 dedicated cases; 1 negative-framed sub-finding (legacy brands, incl. Estée Lauder at rank 18, inside the Bronze-graded 5W/Glossy citation-share case) — no skincare/beauty brand was found publishing its own negative AI-visibility, AI-traffic, or AI-sales result this sweep |
| Unknowns recorded | 6 (see Unknowns below) |

## Unknowns

| Question | Channels checked | Date | Why not answerable from the channels used |
|---|---|---|---|
| Does L'Oréal, Ulta Beauty, Sephora/LVMH, Shiseido, or Beiersdorf carry a brand-own newsroom or IR statement naming AI-assistant visibility, referral traffic, or AI-attributed sales? | Not attempted this session (time budget exhausted after the Estée Lauder Companies, Coty, e.l.f. Beauty, Olaplex, Beiersdorf attempts above) | 2026-09-22 | These five named channels in the task brief were not reached at all this session; absence here is a gap in coverage, not a checked absence |
| Does Coty (COTY) or Olaplex (OLPX) name AI-assistant visibility, GEO, or AI referral/sales anywhere on their own investor or newsroom sites? | `coty.com/newsroom` (404), `ir.coty.com` (DNS not found), `investors.olaplex.com/news-events/news` (DNS not found) | 2026-09-22 | Correct IR/newsroom hostnames for these two filers were not located this session |
| Does any skincare/beauty-vertical SEC filer (8-K/10-Q/10-K) name ChatGPT, AI Overviews, or generative AI search in a filed document, Jan 2026-Sep 2026? | `efts.sec.gov` q="ChatGPT" forms=8-K (98 hits, company names scanned, none beauty); reused `e-case-census-c1-2026-09-22.md` Q4 (q="AI Overviews" + skincare/beauty/cosmetics, 6 hits, zero beauty) | 2026-09-22 | Consistent zero across two independent EDGAR full-text queries — recorded as an absence with channels named, not a guess |
| Does a DTC beauty-brand founder have a public write-up (blog, Substack, Medium, LinkedIn) naming an AI-assistant traffic or sales result? | Hacker News Algolia (0 hits); DuckDuckGo HTML (2 queries, both HTTP 403, channel blocked) | 2026-09-22 | WebSearch budget exhausted per task brief; DuckDuckGo HTML — this session's only remaining general-search substitute — returned 403 on both attempts |
| Does Reddit (r/SkincareAddiction, r/MakeupAddiction, r/30PlusSkinCare — the three subreddits 5W AI Communications names as AI-citation sources) carry a beauty-specific negative result about AI visibility or referral traffic? | `reddit.com/r/SkincareAddiction/search.json` — fetch tool refused this domain entirely | 2026-09-22 | Reddit is not fetchable by this agent's tools this session; no substitute route (browser extension explicitly disallowed for this task) |
| Does WWD Beauty carry primary-linked AI-visibility coverage for a named beauty brand? | `wwd.com/?s=...` → 307 to `tollbit.wwd.com` → HTTP 402 Payment Required | 2026-09-22 | WWD's search is paywalled behind a Tollbit paywall for this session; no content reached |

## Browser backlog

None encountered requiring a browser this session — every source reached (or blocked) via plain fetch. `wwd.com`/`tollbit.wwd.com` is paid-walled, not browser-gated, so it is not added here; a future agent with WWD access (subscription or extension) could recheck it.

## Caveats

- **Most-common shape found: a partnership or launch announcement with no metric, or a visibility-only ranking with no engine/date/n specificity.** Zero Gold, zero Silver this sweep — consistent with `plan.md`'s framing that Pass 4 is "the pass most likely to return little," and with `e-case-census-c1-2026-09-22.md` and `e-case-census-c4-2026-09-22.md`'s prior findings that the anchor vertical (skincare and beauty) produced zero cleared cases in both the earnings/filings sweep (c1) and the vendor-case-study re-grade (c4). This sweep is the first to clear the evidence bar for the anchor vertical at all, and only at Bronze.
- **No sales-attributed case clears the bar.** The two sales/conversion-shaped figures found (Sephora's AI Beauty Chat same-day-purchase rate; Amazon Rufus's "80% more" spend) both carry a percentage with no disclosed base — discard-on-sight caution per `trust-rubric.md` — and are graded Fools gold, not cited as sales proof.
- **eMarketer AI Visibility Index and 5W AI Communications are the two best-sourced visibility rankings found, and neither discloses a prompt set, sample size, or model version.** Consistent with the P3 vendor census finding (`a-vendor-census-c1-2026-09-22.md`, `a-vendor-census-c2-2026-09-22.md`) that no vendor in the roster discloses a composite score's prompt set.
- **The Estée Lauder Companies / Profound partnership (15 Sep 2026) is the strongest brand-own signal found** — a named, dated, on-the-record commitment from a major ticker-bearing beauty group (EL) to a named AI-visibility vendor — but it carries no metric as of the pull date and is filed `screened — no claim`, not as evidence of a result.
- **Trade-press pointer chain, not independently verified:** every Bronze/Fools-gold/statement-only figure in this file traces to a trade-press relay (Glossy or BeautyMatter) of a third-party measurer (eMarketer, 5W AI Communications, Adobe Analytics, NielsenIQ, Tinuiti, Amazon, Stella Rising) whose own primary page was not independently reached this session (each attempt logged in the Discovery log above, all HTTP 404 or not located). This is a structural limitation of this pull, not evidence the primaries don't exist.
- **Five of the nine named priority brand-IR channels (L'Oréal, Ulta Beauty, Sephora/LVMH, Shiseido) were not attempted this session** due to time budget after the other five (Estée Lauder Companies, Coty, e.l.f. Beauty, Olaplex, Beiersdorf) were checked — recorded in Unknowns, not folded into the "no beauty brand found" reading.
- Oldest pull depended on: 2026-09-22 (all nine raw files and this census pulled today; underlying source publication dates range 2026-04-01 to 2026-09-15, all within one quarter of the pull date except none — every cited article is dated on/after 2026-04-01, none flagged stale under `plan.md`'s one-quarter rule as of the pull date; the screened-out Nov 2025/Sep 2025 items are the only stale material encountered and were not pulled).

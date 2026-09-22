# P4-c11 census — negative-result sweep

```yaml
source:          this agent's own discovery log and candidate table for task P4-c11
url_or_doc_id:   n/a — compiled from the raw pulls listed below
published:       2026-09-22
pull_date:       2026-09-22
pull_method:     fetch, browser extension
pull_purpose:    evidence about a number
tier:            n/a — this file is a census/index, not a source pull; every figure traces to the raw/ files it cites, each tiered on its own header
tier_reason:     n/a
source_label:    n/a
lane:            E, F
sub_market:      organic recommendation
engine:          see candidate table
metric_kind:     visibility, none (mixed — see candidate table)
vertical:        see candidate table — none named in any item this cluster cleared
supersedes:      none
captured:        n/a — index file
```

No interpretation below. Counts and quotes trace to the raw/ files named.

## 1. Discovery log — queries and sites checked, screened per source

Per task instructions: the WebSearch tool's budget was already exhausted for this session; `reddit.com` is blocked this session (recorded as `unknown — checked reddit.com, blocked this session, 2026-09-22` per source row below, not queried); the Chrome extension slot was held by this task alone, `tabs_context_mcp` called first, a dedicated new tab created and never touching the two other tabs already open in the shared session (a Google skincare search, and — appearing mid-pull — an agency case-study page).

| # | Channel / query | Method | Date | Result |
|---|---|---|---|---|
| 1 | `hn.algolia.com/api/v1/search?query=generative+engine+optimization+no+lift` | fetch | 2026-09-22 | General GEO discussion, no negative-result specifics; screened |
| 2 | `hn.algolia.com/api/v1/search?query=%22AI+visibility%22+waste` | fetch | 2026-09-22 | One dissent comment ("wasted spend, inconsistent presence, and unmeasurable leakage" — treating each LLM as one channel) and one Show-HN self-promo (an AI-visibility-audit tool); both screened — no specific measured negative result, no named brand/case |
| 3 | `hn.algolia.com/api/v1/search_by_date?query=%22generative+engine+optimization%22&tags=comment` (date-sorted, all time) | fetch | 2026-09-22 | 20 comments read; overwhelmingly definitional/skeptical-of-the-name dissent ("a phrase as dumb as the idea", "equally unsavory in how trust is being eroded"), no comment names a specific brand's GEO/AEO effort and its measured (non-)result; all screened |
| 4 | `hn.algolia.com/api/v1/search?query=%22AI+visibility%22+scam+OR+snake+oil` | fetch | 2026-09-22 | 0 on-point hits (returned nothing) |
| 5 | `hn.algolia.com/api/v1/search?query=GEO+doesn%27t+work` / `%22no+ROI%22+GEO` / `AEO+snake+oil` / `%22AI+visibility%22+%22no+measurable%22` / `%22generative+engine+optimization%22+skeptic` | fetch | 2026-09-22 | All off-topic (GEO = geography/geosynchronous orbit in most hits) or zero hits; screened |
| 6 | `hn.algolia.com/api/v1/search?query=%22AI+visibility%22+churned` / `GEO+client+%22no+results%22` / `%22tried+GEO%22` / `cancelled+%22AI+visibility%22+subscription` / `%22did+not+move+the+needle%22+AI+search` | fetch | 2026-09-22 | 0 on-point hits |
| 7 | `hn.algolia.com/api/v1/search?query=ChatGPT+ads+underperform` / `agentic+checkout+abandoned` / `Perplexity+ads+withdrawn` / `%22AI+ads%22+%22didn%27t+work%22` | fetch | 2026-09-22 | 0 on-point hits — no brand-side or practitioner account of a failed AI-surface ad buy or agentic-checkout integration surfaced via HN Algolia this pull |
| 8 | `hn.algolia.com/api/v1/search_by_date?query=generative+engine+optimization&tags=comment&numericFilters=created_at_i%3E1750550400` (post-2026-06-22 window) | fetch | 2026-09-22 | 74 hits, 15 read; same pattern as row 3 — definitional dissent and manipulation-adjacent commentary (a Reddit-seeding technique described on the "True Rate of Unemployment" thread), no measured negative-result case |
| 9 | `export.arxiv.org/api/query?search_query=all:"generative engine optimization"` (30 most recent, sorted by date) | fetch | 2026-09-22 | 30 titles/abstracts screened at listing level; 4 opened in full detail (rows 10-13 below); remainder are manipulation/defence/benchmark papers (Lane D territory) or positive-effect measurement papers, not null-result papers on point for this cluster |
| 10 | `arxiv.org/abs/2609.07559` — "Scoring Without the Engine" (TW3 Partners/Citead) | fetch, full-text render | 2026-09-22 | **Cleared — Silver.** Pulled as `docs/raw/e-case-c11-arxiv-tw3-partners-geo-score-2026-09-22.md` |
| 11 | `arxiv.org/abs/2607.14035` — "Optimizing Visibility in Generative Engines: A Critical Survey" (Olivier Martinez) | fetch | 2026-09-22 | **Cleared — not graded (survey shape), central finding on point for H5.** Pulled as `docs/raw/e-case-c11-arxiv-martinez-geo-critical-survey-2026-09-22.md` |
| 12 | `arxiv.org/abs/2606.16344` — "Whose hotel does the AI recommend?" (LLM hotel-recommendation audit) | fetch | 2026-09-22 | Read in full; reports which signals move recommendations (rating, price, list position) and that management response is "ignored" — a null finding for one specific signal, but the paper is not framed around a failed GEO/AI-visibility effort and is outside this repo's three verticals; screened, not pulled |
| 13 | `arxiv.org/abs/2605.25517` — "What Gets Cited: Competitive GEO" | fetch | 2026-09-22 | Read in full; reports several levers (topical relevance, list position, price, timestamp) that **do** move citation, i.e. a positive-effect paper, not a null result; ends with a vendor pilot (Sprinklr) reporting positive qualitative feedback — screened, not pulled |
| 14 | `arxiv.org/abs/2609.06811` — "Measuring GEO Visibility: Prompt Corpora Define the Answer Market" | attempted | 2026-09-22 | Not reached — this agent's local scratch file (used to stage the fetch for parsing) was deleted mid-pull by an unrelated process in this shared, multi-agent worktree before the abstract could be extracted; not retried within this task's time budget. Recorded as `unknown — checked arxiv.org/abs/2609.06811, technical failure, 2026-09-22`, not as screened |
| 15 | `g2.com/categories/generative-engine-optimization` | browser (fetch first, 403; extension) | 2026-09-22 | 404 — wrong slug |
| 16 | `g2.com/categories/ai-search-visibility` | browser | 2026-09-22 | 404 — wrong slug |
| 17 | `g2.com/products/profound/reviews` (base page), then `?filters[nps_score][]=1#reviews` and `?filters[nps_score][]=2#reviews` | browser | 2026-09-22 | Category resolved via this product's own breadcrumb to "AI Search Visibility Optimization Tools" (539 listings). 1-star filter: 1 review found — **cleared, pulled** as `docs/raw/e-case-c11-g2-profound-review-2026-09-22.md`. 2-star filter: 1 review found — screened (positive about the AI-visibility function; complaint is an unrelated hiring/candidate-experience grievance) |
| 18 | `g2.com/categories/ai-search-visibility-optimization-tools` | browser | 2026-09-22 | Correct category, 539 listings, all 15 products shown on page 1 rated 4.4-4.9; no sub-4.0 vendor visible on page 1 |
| 19 | `g2.com/products/scrunch-ai/reviews` (1-star filter) | browser | 2026-09-22 | "Scrunch AI hasn't been reviewed yet" — this G2 listing (seller shown as "Sitecore", post-acquisition) carries 0 reviews, distinct from the "Scrunch AI 4.6/5 (73)" listing referenced elsewhere on G2's own comparison widgets; not pursued further |
| 20 | `g2.com/products/brandlight-ai/reviews` (1-star filter) | browser | 2026-09-22 | **Blocked.** Returned a DataDome "Verification Required" slider CAPTCHA. Per this session's standing rules, CAPTCHAs are not solved. G2 was not used again this pull. Recorded as `browser backlog: 1` (further G2 vendor low-star review checks — Otterly.AI, Peec AI, AthenaHQ, Brandlight AI — not completed) |
| 21 | `capterra.com/search/?query=AI%20visibility` | browser | 2026-09-22 | Resolved a dedicated "AI Search Visibility" category, 20 small pure-play products (mostly 1-review 5.0 listings, too thin to yield a low-star review) |
| 22 | `capterra.com/ai-search-visibility-software/` (broader 394/539-product category, page 1 of 9) | browser | 2026-09-22 | BrightEdge lowest on page 1 at 4.1/5 (45 reviews) |
| 23 | `capterra.com/p/124928/BrightEdge/reviews/` | browser | 2026-09-22 | 45 reviews read (page 1, "Sort by Rating" control clicked but did not visibly reorder results). **2 cleared, pulled**: 1-star "Scam -- don't do it" (`docs/raw/e-case-c11-capterra-brightedge-scam-review-2026-09-22.md`) and 2-star "Almost as clunky and poorly built as it is expensive" (`docs/raw/e-case-c11-capterra-brightedge-autopilot-review-2026-09-22.md`). 5 more sub-4-star reviews read and screened (table inside that second file) |
| 24 | `capterra.com/p/148472/SimilarWeb-Pro/reviews/` | browser | 2026-09-22 | 25 reviews read (page 1 of 261 total); all 4.0-5.0, none naming an AI-visibility failure; screened, none cleared |
| 25 | `capterra.com/p/219972/Writesonic/reviews/` | browser | 2026-09-22 | 25 reviews read (page 1 of 2,102 total); lowest found 3.0 ("It need editing" — output-quality complaint, not AI-visibility/citation-specific); tool is a content-generation product, not primarily an AI-visibility tracker; screened, none cleared |
| 26 | `omr.com/en/reviews/category/generative-engine-optimization-geo` | fetch | 2026-09-22 | 24 vendors listed, aggregate ratings 4.50-5.00 (full table in `docs/raw/e-case-c11-omr-rankscale-review-2026-09-22.md`); no vendor below 4.50 |
| 27 | `omr.com/en/reviews/product/rankscale-ai`, `/otterly-ai`, `/blinq` (the three most-reviewed products, 26+56+22=104 individual reviews) | fetch | 2026-09-22 | Individual star values recovered via each page's embedded JSON-LD: cluster at 3.0-5.0 only, no 1-star or 2-star found among 104 reviews. **1 cleared, pulled**: the single 3.0-star review found (lowest of the 104), `docs/raw/e-case-c11-omr-rankscale-review-2026-09-22.md` |
| 28 | `reddit.com/r/SEO`, `/r/bigseo`, `/r/PPC` negative-result queries (query-book.md amendment 7) | not run | 2026-09-22 | `unknown — checked reddit.com, blocked this session, 2026-09-22` per task instructions — recorded as blocked, not attempted |
| 29 | `html.duckduckgo.com/html/?q=%22AI+visibility%22+agency+%22no+lift%22+client` | fetch | 2026-09-22 | Rate-limited (236-byte error response: "If this persists, please email us"), consistent with the rate-limiting another Pass 4 agent already recorded for this endpoint (`docs/raw/e-case-census-c2-2026-09-22.md` row 34); not retried per "sparingly" instruction. Recorded as `unknown — checked html.duckduckgo.com, rate-limited, 2026-09-22` |

## 2. Candidate table — cleared items (6, this cluster's own pulls)

| Source | Type | Date | Vendor named | Engines | Metric | Claim (verbatim, abbreviated) | Direction | Grade (missing items) | Vertical | Raw path |
|---|---|---|---|---|---|---|---|---|---|---|
| arXiv (TW3 Partners/Citead) | paper (vendor admission / null-result) | 2026-09-07, tested July 2026 | TW3 Partners / Citead (paper authors' own company) | 10 modern engine families (6 open-weight + gemini-3.1-flash-lite + 3 gpt-5.x) | visibility (citation) | "re-measuring the only published causal anchors (2023 effect sizes) on ten modern engine families shows their levers move citation on none" | negative | Silver — item 1 (brand) not applicable, all others present | none named | `e-case-c11-arxiv-tw3-partners-geo-score-2026-09-22.md` |
| arXiv (Olivier Martinez) | paper (null-result survey) | 2026-07-15 | none | many, across 45 reviewed studies | visibility | "no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior" | negative/null | not graded — meta-analysis, not a single-brand case | none named | `e-case-c11-arxiv-martinez-geo-critical-survey-2026-09-22.md` |
| G2.com | review (1-star) | 2026-05-21 | Profound | none named | none | "It is trying to solve AI Visibility but again is that really benefiting I doubt it" | negative | screened — no claim | none named | `e-case-c11-g2-profound-review-2026-09-22.md` |
| OMR Reviews | review (3-star, lowest found in category) | 2026-05-18 | Rankscale.ai | none named | none | UX/keyword-list-management complaint; no lift claim | neutral/mixed | screened — no claim | none named | `e-case-c11-omr-rankscale-review-2026-09-22.md` |
| Capterra | review (1-star) | 2021-08-10 | BrightEdge | none named | none | "Did not provide what was promised... They are not ethical people" (contract/ethics complaint, no AI content, stale) | negative (off-target) | screened — no claim | none named | `e-case-c11-capterra-brightedge-scam-review-2026-09-22.md` |
| Capterra | review (2-star) | 2023-10-26 | BrightEdge | none named | none | "Autopilot integration was pretty bad... Opportunity forecasting... was unusable" (feature-bug complaint, stale) | negative | screened — no claim | none named | `e-case-c11-capterra-brightedge-autopilot-review-2026-09-22.md` |

## 3. Cross-referenced — already pulled by other Pass 4 clusters, cited per task instructions, not re-filed or double-counted in the counts below

| Source | Type | Date | Vendor/cause named | Grade | Vertical | Raw path |
|---|---|---|---|---|---|---|
| NerdWallet, Inc. (8-K Ex-99.1, Q4 FY25 earnings release) | brand admission | 2026-02-25 | AI overviews, LLMs (generic, no single vendor) | Silver (per `docs/raw/e-case-census-c1-2026-09-22.md` candidate table) | high-CPA regulated (credit cards, insurance, loans named in the filing) | `docs/raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md` |
| Seer Interactive — "The Problem & The Fix on GEO case studies promising results in 1 week" | practitioner / agency category-noise post | 2026-05-20 | none named (critiques unnamed other agencies) | not graded — category-noise, per `docs/raw/e-case-census-c2-2026-09-22.md` candidate #6 | none named | `docs/raw/e-case-seer-interactive-fake-fast-results-2026-09-22.md` |

## 4. Screened-out list, with reason (beyond the discovery-log rows above)

| Item | Reason screened |
|---|---|
| G2 Profound 2-star review (Evangelia S., 5/22/2026, "Effective Visibility Tool, Needs Better Candidate Experience") | Affirmatively positive about AI-visibility efficacy ("Profound ensures my company name and products come up first when searched, which was very valuable for my makeup brand"); low score driven entirely by an unrelated candidate-ghosting complaint. Off-target, not filed |
| 5 further sub-4-star BrightEdge Capterra reviews (Chiara G. 2.0, Gaurav G. 3.0, Cole R. 3.0, Verified Reviewer 3.0, Adam C. 3.0) | General usability/pricing complaints, no AI/GEO/AEO content, several pre-date the AI-visibility category entirely (2018, 2019, 2020, 2023); full table in `docs/raw/e-case-c11-capterra-brightedge-autopilot-review-2026-09-22.md` |
| ~35 distinct HN comments/threads across 8 query batches (discovery-log rows 1-8) | Definitional dissent about the GEO/AEO name and the category's trust/manipulation risk; none names a specific brand's effort and its measured (non-)result |
| 2 arXiv papers read in full (2606.16344 hotel audit, 2605.25517 competitive-GEO) | Positive-effect or off-scope findings, not null/negative results on point for this cluster |
| Similarweb, Writesonic Capterra reviews (page 1 each, 50 reviews read) | No sub-4-star review named an AI-visibility-specific failure |
| G2 category slug guesses (`generative-engine-optimization`, `ai-search-visibility`) | 404, wrong slugs; superseded by the correct category found via a product breadcrumb |
| G2 Scrunch AI listing | 0 reviews on this specific (post-acquisition, Sitecore-branded) G2 listing |

## 5. Counts

| | Count |
|---|---|
| Screened total (candidates examined across all channels: HN comments read in detail, arXiv abstracts read in full, review pages/individual reviews read) | ≈180 — 35 HN comments (rows 1-8) + 4 arXiv papers read in full beyond the 2 cleared (row 9-13) + 30 arXiv titles/abstracts scanned at listing level (row 9) + 2 G2 reviews (1 cleared, 1 screened) + 104 OMR individual reviews' ratings scanned (1 cleared) + 7 BrightEdge reviews (2 cleared, 5 screened) + 50 Similarweb/Writesonic reviews (0 cleared) |
| Negative or null found — cleared into `raw/` this cluster | 6 (candidate table §2) |
| Negative or null found — cross-referenced, already on file from other clusters | 2 (§3: NerdWallet, Seer) |
| Vendor-named — this cluster's own pulls | 3 distinct AI-visibility-category vendors named as the subject of a negative account (Profound, Rankscale.ai, BrightEdge), plus 1 vendor-author company whose paper is the evidence itself, not the subject under test (TW3 Partners / Citead) |
| Cleared by grade — this cluster's own pulls | Silver: 1 (TW3 Partners/Citead). Not graded (shape mismatch — survey): 1 (Martinez). Screened — no claim: 4 (G2 Profound, OMR Rankscale, Capterra BrightEdge ×2). Gold: 0. Bronze: 0. Fools gold: 0 |
| Per-vertical — this cluster's own pulls | Skincare and beauty: 0 screened as such, 0 cleared. B2B SaaS: 0 screened as such, 0 cleared. High-CPA regulated: 0 screened as such, 0 cleared. None named: 6 cleared, all 6 (every cleared item names no vertical; no source this pull named a vertical, so none is assigned by inference, per `demand-signals.md`'s cell-attribution rule) |
| Browser backlog | 1 (further G2 low-star review checks — Otterly.AI, Peec AI, AthenaHQ, Brandlight AI — blocked by a DataDome CAPTCHA this session did not solve) |
| Unknowns recorded | 3 formal `unknown — checked <channel> 2026-09-22` lines: reddit.com (blocked this session), html.duckduckgo.com (rate-limited), arxiv.org/abs/2609.06811 (technical failure — local scratch file lost mid-pull in the shared multi-agent worktree) |

## 6. Survivorship statement

This cluster is the counterweight to the published-winners bias structural to every other Pass 4 channel: `docs/raw/e-case-census-c1-2026-09-22.md` through `c10` all pull from channels that only a brand, vendor, or agency choosing to publish would ever populate — earnings decks, vendor case studies, agency blog posts, conference talks — and a party that ran a GEO/AEO effort and saw nothing worth telling generally tells no one. This pull confirms that structural asymmetry from the negative-result side directly: the two strongest items found (`e-case-c11-arxiv-tw3-partners-geo-score-2026-09-22.md`, Silver, and the Martinez survey) are both **academic**, not brand- or vendor-sourced, because the academic literature is the one channel with an incentive (publication, replication) to report a null result at all. Every review-site channel checked (G2, OMR, Capterra — 6 vendors, well over 150 individual reviews read or rating-scanned across them) returned an overwhelmingly positive rating distribution (mostly 4.4-5.0), consistent with the review-farming bias `docs/sources/channels.md` flags for these exact channels (C36, C65: "Vendors farm reviews; check velocity not count"); genuinely negative (1-2 star) reviews exist but are rare, and the ones found either carry no AI-visibility-specific claim at all (BrightEdge, both stale and pre-dating the category) or carry a claim with no metric behind it (Profound, Rankscale.ai). No brand-side account of a failed AI-surface ad buy or agentic-checkout integration was found via any channel this pull touched (HN, arXiv, review sites) — recorded as an absence, not a demotion, per root `CLAUDE.md`.

## 7. Unknowns per source

| Source | Status |
|---|---|
| reddit.com (r/SEO, r/bigseo, r/PPC negative-result queries) | `unknown — checked reddit.com, blocked this session, 2026-09-22` |
| html.duckduckgo.com | `unknown — checked html.duckduckgo.com, rate-limited, 2026-09-22` |
| arxiv.org/abs/2609.06811 ("Measuring GEO Visibility: Prompt Corpora Define the Answer Market") | `unknown — checked arxiv.org/abs/2609.06811, technical failure (local scratch file lost mid-pull), 2026-09-22` |
| G2.com — Otterly.AI, Peec AI, AthenaHQ, Brandlight AI low-star reviews | `unknown — checked g2.com, CAPTCHA-blocked after the Profound and Scrunch AI listings, not solved, 2026-09-22` |

## Caveats

- No interpretation, no ranking beyond what grading rule 1 mechanically assigns. This file states what was found and where.
- All 6 items this cluster pulled name no vertical from this repo's three-vertical framework. This is a real, recorded absence (§5), not a tagging failure — no source this pull touched named skincare/beauty, B2B SaaS, or high-CPA regulated in connection with a negative or null AI-visibility outcome.
- Every review-site item filed graded "screened — no claim" rather than Bronze or better, because none carries any visibility/traffic/sales number at all — this is the honest, expected shape of user-review evidence against the seven-item bar, not a grading error.
- The two cross-referenced items in §3 (NerdWallet, Seer) are cited per this task's brief ("already pulled; cite") and are **not** counted in the "cleared" or "screened" totals in §5, to avoid double-counting against the other clusters' own censuses.
- The academic literature's two null-result items (§2 rows 1-2) both concern the organic-recommendation sub-market (Lane A/E) specifically; no null or negative result was found this pull for paid placement (Lane B, AI-surface ad buys) or agentic commerce (Lane C, agentic-checkout integrations) — recorded as an absence with the channels checked (discovery-log row 7), not as evidence those efforts succeed.
- The TW3 Partners/Citead paper (`e-case-c11-arxiv-tw3-partners-geo-score-2026-09-22.md`) is vendor-affiliated; the tier-4 assignment and its reasoning are stated in that file's own header and are not repeated as a qualifier here beyond this pointer.
- Oldest pull depended on: 2026-09-22 for every file's own pull date; oldest **source-published** date cited is 2021-08-10 (the stale BrightEdge "Scam" review), flagged stale in its own raw file per `plan.md`'s staleness rule; it is filed because it is the single most negative review found for that vendor, not because it is current evidence about AI-visibility efficacy.

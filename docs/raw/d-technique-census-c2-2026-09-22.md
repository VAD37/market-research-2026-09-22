# Technique census — P5-c2: review and listicle manufacture

```yaml
source:          compiled from the 8 raw pulls listed below, all pulled 2026-09-22
url_or_doc_id:   n/a — census of docs/raw/d-review-*-2026-09-22.md (8 files) plus one already-landed cross-cluster pull (P2-c9)
published:       n/a — compiled 2026-09-22
pull_date:       2026-09-22
pull_method:     manual (compiled from this session's own raw pulls; no new fetch beyond what each cited file records)
pull_purpose:    evidence about a number
tier:            n/a — inherits the tier of each cited row, stated per row below
source_label:    n/a — mixed, per row
lane:            D
sub_market:      organic recommendation
engine:          n/a — cross-engine
metric_kind:     none
supersedes:      none
captured:        four question tables (mechanism, actors, measured-effect, engine/platform statements), the H14 per-vertical density table, screened-out list, counts, unknowns. No text beyond what the cited raw files already carry.
technique:       review and listicle manufacture
task:            P5-c2
hypotheses:      H5, H13, H14
```

## Q1 — Mechanism: how it works, per source

| Source | What the source says the mechanism is | Raw path |
|---|---|---|
| arXiv 2506.13313 (Hidden Persuaders) | LLMs (tested: ChatGPT o1 as generator) can write fake product reviews that both humans (50.8% detection accuracy — chance level) and seven LLM detector models cannot reliably distinguish from genuine ones, at the individual-review level | `docs/raw/d-review-arxiv-hidden-persuaders-2026-09-22.md` |
| arXiv 2606.20065 (GEO at Scale, Ranqo) | The ranked "best-of" listicle is the single most-cited content format in AI-engine answers (~21% of all citations, out of 100K+ sampled responses) — i.e. the mechanism's leverage point is that engines already weight listicle-format pages heavily in what they cite, ahead of most other formats | `docs/raw/d-review-arxiv-geo-at-scale-2026-09-22.md` |
| arXiv 2601.00912 (Discovery Gap) | Counter-mechanism claim: a composite "GEO score" (on-page optimization, of which review/listicle-style content is one hypothesized input) showed no measured correlation with whether a product surfaces in discovery-style AI queries — what did correlate were referring-domain count, Product Hunt ranking, and community mentions, i.e. classical link/community signals, not GEO content tactics | `docs/raw/d-review-arxiv-discovery-gap-2026-09-22.md` |
| FTC 16 CFR 465.2 | Frames the mechanism from the regulator's side as three distinct acts: a business (1) writing/creating a review that misrepresents the reviewer's existence, product experience, or opinion; (2) purchasing such a misrepresenting review; or (3) procuring one through a third party — each an "unfair or deceptive act or practice" | `docs/raw/d-review-ftc-fake-reviews-rule-2026-09-22.md` |
| G2 Community Guidelines | Names the mechanism as "Fraudulent or Manipulative Review Activity: creating, soliciting, or submitting fake or otherwise inauthentic reviews... in a deliberate attempt to manipulate consumer perception or behavior," plus a separate "Biased Review Collection" mechanism (segmenting out negative reviews, undisclosed incentives) | `docs/raw/d-review-g2-community-guidelines-2026-09-22.md` |
| Capterra review-verification page | Frames the mechanism as producing "spam profiles, fake identities, and fraudulent reviews" that its own QA process (30+ moderators, 20+ checks/review, AI-content and plagiarism detection) is built to catch | `docs/raw/d-review-capterra-review-verification-2026-09-22.md` |
| Trustpilot Guidelines for Reviewers (Jun 2026) | "A fake review is a review which doesn't reflect your genuine experience... often written in an attempt to mislead and manipulate what other consumers think about that business (positively or negatively)" — separately flags "AI-generated content" under its misinformation/promotional-content flagging category | `docs/raw/d-review-trustpilot-guidelines-2026-09-22.md` |
| Google spam policies | Defines the adjacent, broader mechanism "scaled content abuse": "many pages... generated for the primary purpose of manipulating search rankings and not helping users," including AI-generated pages, scraped/stitched/synonymized pages, and keyword-stuffed low-value pages — not specific to reviews or listicles by name | `docs/raw/d-review-google-spam-policies-2026-09-22.md` |

## Q2 — Actors: who is documented doing it, per source

| Actor (as named by the source) | Actor type | Source's own characterization | Raw path |
|---|---|---|---|
| No specific company, vendor, or individual actor is named as doing review-and-listicle manufacture in any of this cluster's 8 raw pulls | n/a | The FTC rule (465.2) and three platform policies (G2, Capterra, Trustpilot) all describe the *category* of prohibited actor behavior — "a business," "vendors," "reviewers" — in general/hypothetical terms, naming no specific violator | all 8 files above |

Closest partial evidence found, **not** captured as a full raw pull this cluster (see Unknowns and Pull-blockers below): an HN Algolia index record (title, URL, score, date only — no body text) of a 2020-08-18 Reddit r/Supplements thread titled "Here's a brand that's building its reviews steadily," 181 points / 131 comments, alleging a specific (unnamed in the index metadata) supplements brand manufacturing Amazon reviews. `docs/raw` does not carry this as a filed pull because `reddit.com` was blocked to both `WebFetch` and the browser extension this session (see Pull-blockers) and the HN Algolia index alone does not carry a verbatim reviewable body, which the raw-pull template and trust-rubric's "discard on sight" rule (no verifiable method/body) both weigh against filing.

## Q3 — Measured effect: does published evidence show manufactured review/listicle corpora moving an AI answer? (H5)

| Source | Models | Date window | Prompt set published? | n | Effect on an AI answer, verbatim | Replicated by | Tier |
|---|---|---|---|---|---|---|---|
| arXiv 2606.20065 (Ranqo) | ChatGPT, Claude, Perplexity, Gemini | March–May 2026 (general corpus); CRM sub-study Jan 2026 | Not confirmed in this pull | 100K+ prompt responses, 100+ brands (general); 2,500 responses / 9,600+ brand mentions (CRM sub-study, n=10 CRM brands × 50 prompts × 5 engines × 10 runs) | "the highest-leverage page is the ranked 'best-of' listicle, the most-cited content format at about 21% of all citations" — a snapshot citation-share measurement, **not** a before/after test of manufacturing a listicle and observing a citation-rate change | none found this pull | 5, vendor-authored (Ranqo), bias-flagged |
| arXiv 2601.00912 (Discovery Gap) | ChatGPT gpt-4o-mini, Perplexity sonar (web search on) | Sample: 2025 Product Hunt top-500 leaderboard; query-run date not separately stated | Not confirmed in this pull | 2,240 queries across 112 startups | "Generative Engine Optimization (GEO)... showed no correlation with actual discovery rates" — a **negative** correlational result for GEO broadly (not review/listicle manufacture in isolation) | none found this pull | 5 |
| arXiv 2506.13313 (Hidden Persuaders) | Generator: ChatGPT o1. Detectors: ChatGPT-o1, DeepSeek-R1, Grok-3, Gemini-2.0-Flash-Thinking, ChatGPT-4o, Gemma-3-27B-it, Qwen2.5-Max | Not stated beyond 2025-06-16 submission date | Not confirmed in this pull | 50 reviews (25 real + 25 fake), 288 human participants, 7 detector models | Measures review-corpus-level detectability, not any AI assistant's downstream answer or recommendation — **out of scope for H5** on its own, filed as upstream mechanism evidence only | none found this pull | 5 |

**H5 read from this cluster alone:** no item in this cluster's 8 pulls meets the H5 confirm bar ("Before-and-after with prompt set and n published, tier 4"). One item (Ranqo) shows a correlational snapshot consistent with listicles mattering; one item (Discovery Gap) shows a correlational snapshot cutting the other way for GEO broadly. Neither is a before/after manipulation test, and neither publishes a fixed prompt set in what this pull captured. Per `hypotheses.md`, this is recorded as `unresolved — checked arXiv, ACL Anthology (not separately queried this cluster), Semantic Scholar (rate-limited, see Pull-blockers) 2026-09-22`, not as a kill — Pass 9 makes the final call across all of Pass 5's clusters, not this one alone.

## Q4 — What engines and review platforms say or do about it

| Engine / platform | Stated policy or absence | Page and date | Raw path |
|---|---|---|---|
| G2 | "Fraudulent or Manipulative Review Activity" and "Biased Review Collection" named as prohibited vendor behaviors; enforcement actions listed (review removal, listing revocation, banner warning buyers, platform ban); AI-assisted reviews restricted to identity-verified reviewers only | `legal.g2.com/community-guidelines`, undated page, checked 2026-09-22 | `docs/raw/d-review-g2-community-guidelines-2026-09-22.md` |
| Capterra | Reviews run through 20+ automated and human checks per submission, including detection for "generative AI and plagiarized content"; suspicious reviews trigger a re-verification request, permanent flag/removal on failure | `capterra.com/resources/how-we-verify-reviews/`, undated page, checked 2026-09-22 | `docs/raw/d-review-capterra-review-verification-2026-09-22.md` |
| Trustpilot | Fake reviews defined and banned ("undermine trust and are illegal... we do not tolerate them"); automated detection plus human plus community reporting; separately flags "AI-generated content" under its misinformation-flagging category | `corporate.trustpilot.com/legal/for-reviewers/guidelines-for-reviewers/jun-2026`, version 2.2, dated June 2026, checked 2026-09-22 | `docs/raw/d-review-trustpilot-guidelines-2026-09-22.md` |
| Google Search | "Scaled content abuse" named and defined as a spam policy, explicitly including AI-generated mass page creation; does not name "reviews" or "listicles" specifically in what this pull captured | `developers.google.com/search/docs/essentials/spam-policies`, last-updated 2026-08-28 (per page), checked 2026-09-22 | `docs/raw/d-review-google-spam-policies-2026-09-22.md` |
| FTC (US regulator, not a platform) | Binding rule (16 CFR 465.2) prohibiting a business from writing/creating, purchasing, or procuring a fake or false consumer review or testimonial; separately, 16 CFR Part 255 (already pulled at P2-c9, cited here rather than re-pulled) requires disclosure of material connections behind an endorsement | `ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465/section-465.2`, source "89 FR 68077, Aug. 22, 2024," checked 2026-09-22; endorsement-guides companion at `docs/raw/b-us-regulator-endorsement-guides-2026-09-22.md` (P2-c9, pulled 2026-09-22, cited not re-pulled) | `docs/raw/d-review-ftc-fake-reviews-rule-2026-09-22.md` |
| ChatGPT / Claude / Gemini / Perplexity / Copilot / Amazon (AI-assistant engines specifically) | `unknown — checked developers.google.com/search/docs (Google Search's general spam policy only, not an AI-Overviews/AI-Mode-specific page) 2026-09-22`. No engine-specific policy page naming review or listicle manipulation as an AI-answer-manipulation vector was pulled in this cluster; this question is also explicitly the scope of the separate P5-c7 "Engine countermeasures" cluster (queued, not yet landed, per `docs/method/STATE.md`), so a fuller answer sits there rather than being duplicated here | n/a | — |

## H14 — Per-vertical density comparison

Screened counts by search route, this cluster only. A source is tagged to a vertical only where the source itself names it — never by inference (`demand-signals.md` cell-attribution rule).

| Vertical | Route | Screened | Cleared (named in a citable source this cluster) |
|---|---|---|---|
| High-CPA regulated — supplements | arXiv `abs:"supplement" AND abs:"review" AND abs:"large language model"` | 10 (all off-topic — code review, literature review, healthcare eval, math, etc., see screened-out list) | 0 |
| High-CPA regulated — insurance / cards | arXiv `abs:"insurance" AND abs:"review" AND abs:"manipulation"` | 3 (cyber insurance framework, data-poisoning benchmark using an insurance-claims dataset, image-tamper-detection survey — none on review/listicle manufacture) | 0 |
| High-CPA regulated — supplements | HN Algolia `fake reviews supplements` | 19 hits, 1 relevant (2020 Reddit r/Supplements thread on a supplements brand building fake Amazon reviews) | 1 — but **not filed as a raw pull** (see Q2 and Pull-blockers); recorded as screened-cleared-but-unpullable |
| High-CPA regulated — insurance / cards | HN Algolia `fake reviews insurance OR credit card` | 3 hits, 0 relevant (BBC Amazon-fraud story, an unrelated tech-bubble essay, an unrelated Ask HN thread) | 0 |
| Skincare and beauty | arXiv `abs:"skincare" OR abs:"cosmetics" AND abs:"review" AND abs:"generative"` | 10 (dermatology datasets, pore-simulation, makeup-residue UX, biosurfactant chemistry review, LLM cosmetic-chemistry benchmark, sentiment-analysis corpus, ingredient-based recommender, wrinkle imaging, skin-attribute detection — none on review/listicle manufacture) | 0 |
| Skincare and beauty | HN Algolia `fake reviews skincare OR beauty OR cosmetics` | 0 (zero hits returned) | 0 |
| B2B SaaS | HN Algolia `G2 fake reviews SaaS` | 1 (2016 "Ask HN: How to disrupt the SaaS review sites marketplace?" — 1 point, 0 comments, no engagement, no verifiable claim) | 0 — discarded per trust-rubric's "no n, no method" rule; too thin to file |
| B2B SaaS | arXiv 2606.20065 (Ranqo), self-reported sample-skew caveat only, not a targeted vertical search | n/a — incidental finding inside an already-pulled item, not a dedicated screen | 0 cleared as review/listicle-specific evidence — the paper's own words are: "brands skew toward SaaS, retail-execution, fintech, and Indian DTC" (general GEO-visibility skew, not a review/listicle-manufacture finding) |
| Cross-vertical | FTC enforcement-action search (`ftc.gov/news-events/news/press-releases` with `query=fake+reviews`, `query=reviews`, `query=supplement+reviews`) | 3 query attempts | 0 — the query parameter appears not to be honored by a plain fetch of that URL (same generic recent-release list returned each time); recorded as an unresolved access method, not a true zero |

**Read (evidence only, no scoring — Pass 9's job):** across every route this cluster ran, zero items were filed as citable raw pulls naming any of the three verticals in connection with review-and-listicle manufacture specifically. One thin, unpullable practitioner claim (supplements) and one incidental vendor-paper skew note (SaaS) are the only vertical-adjacent signals found; skincare/beauty and insurance/cards returned nothing at any route tried. This is too thin, and too unevenly screened across routes, to read as confirming or killing H14 from this cluster alone.

## Screened-out list (not pulled, with reason)

- 10 arXiv hits for the supplements query — off-topic (code review automation, literature-review tooling, healthcare LLM evaluation framework, systematic-review search-strategy automation, math-word-problem survey, crash-narrative coding benchmark, adversarial-reasoning RL, RAG mental-health study, medication-evidence characterization, RAG privacy SoK).
- 3 arXiv hits for the insurance query — off-topic (cyber-insurance risk-design framework; data-poisoning detection benchmark that merely uses an "Insurance Claims" dataset; a 2013 digital-image-tamper-detection survey that mentions insurance claims as one application domain).
- 10 arXiv hits for the skincare/cosmetics query — off-topic (dermatology imaging datasets, facial-pore simulation, opera-makeup-residue UX tool, biosurfactant chemistry review, a cosmetic-chemistry LLM-accuracy benchmark, a Korean cosmetics-review sentiment corpus, an ingredient-based beauty recommender, tactile wrinkle-depth imaging, skin-attribute transfer learning).
- arXiv 2608.11390 ("Mechanism Design for Generative Engines... citation wars") — screened, not filed in this cluster: discusses GEO content-rewrite attacks and a platform-creator reward mechanism generally, but its abstract does not name reviews, listicles, "best-of" pages, or affiliate/comparison content as the gaming tactic studied; judged closer to this programme's P5-c1/P5-c4 clusters' scope than P5-c2's.
- HN Algolia `listicle GEO AI search` — 0 hits.
- HN Algolia `fake reviews AI recommendation` — 8 hits, all off-topic Show-HN/Ask-HN posts unrelated to review manufacture as a technique.
- HN Algolia `fake reviews skincare OR beauty OR cosmetics` — 0 hits.
- HN Algolia `fake reviews insurance OR credit card` — 3 hits, 0 relevant (listed under H14 table above).
- HN Algolia `G2 fake reviews SaaS` — 1 hit, too thin to file (listed under H14 table above).
- HN Algolia `fake reviews supplements` — 19 hits; 1 relevant but unpullable (2020 Reddit thread, see Q2/Pull-blockers); the remaining 18 are off-topic (Amazon-review-fraud press coverage generally, unrelated Ask-HN threads, unrelated science/retraction items).
- Semantic Scholar API — 2 queries attempted (`review manipulation LLM product recommendation`; `fake review detection generative AI search engine citation`), both returned HTTP 429 (rate-limited) before any results were retrieved; not counted toward screened/cleared totals since no results were ever returned to screen.
- `developers.google.com/search/docs/appearance/writing-high-quality-reviews` and `.../appearance/product-reviews` — both guessed URLs, both 404. Not filed.
- `duckduckgo.com/html/?q=...` (two attempts) — both returned "Permission denied for reading page content on this domain" from the browser extension mid-session (see Pull-blockers); zero usable results.

## Counts

- Raw files landed this cluster: 8 (`docs/raw/d-review-*-2026-09-22.md`), plus this census (9th file).
- Cross-cluster pull cited, not re-pulled: 1 (`docs/raw/b-us-regulator-endorsement-guides-2026-09-22.md`, P2-c9).
- Highest tier reached: 2 (FTC 16 CFR 465, filed federal regulation).
- Measured-effect rows in the Q3 table: 3, none meeting H5's confirm bar; 0 with a published prompt set confirmed in this pull.
- Engines/platforms with a stated policy captured: 4 — G2, Capterra, Trustpilot, Google Search (spam policies). FTC counted separately as a regulator, not a platform.
- Per-vertical screened items: supplements 29 (10 arXiv + 19 HN), insurance/cards 6 (3 arXiv + 3 HN), skincare/beauty 10 (10 arXiv + 0 HN), B2B SaaS 1 (HN) + 1 incidental (Ranqo paper's skew sentence, not a dedicated screen. Total unique dedicated-search items screened across all three verticals: 46.
- Cleared (citable, vertical-named): 0 filed. 1 screened-cleared-but-unpullable (supplements, Reddit thread).
- Unknowns recorded (this file): 9 explicit `unknown — checked...` lines across the raw pulls and this census (2 in the FTC file re: remaining Part 465 sections and enforcement-action search; 1 each in the G2, Capterra, Trustpilot files re: companion pages not pulled; 2 in the Google file re: dedicated review-guidance URL and AI-surface-specific policy; 1 each in the Hidden Persuaders, GEO-at-Scale, and Discovery Gap files re: code/prompt-set publication and study dates).

## Pull-blockers encountered this cluster

- `reddit.com` (all subdomains, including `old.reddit.com/*.json`) is blocked outright to both `WebFetch` ("Claude Code is unable to fetch from...") and the browser extension's `navigate` tool ("This site is not allowed due to safety restrictions") this session. This prevented filing the one screened-cleared supplements practitioner item as a full raw pull; only its HN Algolia index metadata (title, URL, score, comment count, date) could be captured.
- `support.trustpilot.com` returned "Permission denied for reading page content on this domain" from the browser extension on first navigation; the working Trustpilot policy was found at `corporate.trustpilot.com` instead.
- `duckduckgo.com/html/?q=...` returned the same permission-denied error inconsistently — one query returned a readable "no results" page via the `find` tool, a second, otherwise-identical-shaped query was denied. Not relied on further after two attempts, per the task's "use sparingly" instruction.
- Semantic Scholar API (`api.semanticscholar.org`) returned HTTP 429 on both attempts across the session (roughly 40 minutes apart) — not usable this cluster.
- `ftc.gov/news-events/news/press-releases?query=...` does not appear to honor its own `query` URL parameter when fetched via `WebFetch` (identical generic recent-release list returned for three different query strings) — FTC enforcement-action search for named fake-review violators could not be completed by this method; a browser-driven, JS-rendered search was not attempted this cluster (time budget).

## Caveats

- This census compiles 8 pulls made in one session under one time budget. Several `unknown — checked` lines reflect time-budget stops, not confirmed absences — each is named at its row/source above, not silently treated as a negative finding.
- The H14 density table's screened counts are **not equal-effort across verticals** in a strict sense: the supplements route benefited from one extra, higher-yield HN query (19 hits, 1 relevant) that the other two verticals' routes did not independently replicate at the same query count. `hypotheses.md`'s own caveat on H14 ("equal screen effort... is not measurable to a fine grain") applies directly here.
- No `docs/raw/` file in this cluster shows a published, peer-reviewed (tier 2 or 3) measurement of review-or-listicle manufacture moving an AI assistant's answer. The two closest items (Ranqo's listicle-citation-share snapshot; the Discovery Gap's negative GEO-correlation snapshot) are both tier 5, both correlational/snapshot rather than causal/before-after, and — per `trust-rubric.md`'s rule that conflicting figures are "never averaged" — are recorded side by side in the Q3 table rather than reconciled.
- Oldest pull depended on: 2026-09-22 (all 8 raw files in this cluster, plus the cited P2-c9 file, were pulled or landed on this date).

# Quattr — Quattr Method, Metrics dictionary, and AI Visibility Proof Index

```yaml
source:          Quattr, Inc.
url_or_doc_id:   https://www.quattr.com/ai-visibility/method; https://www.quattr.com/ai-visibility/method/ai-visibility-proof; https://www.quattr.com/ai-visibility/metrics; https://www.quattr.com/ai-visibility/prompts
published:       undated on method/metrics pages; the metrics page states its formulas were "confirmed against the product by the analytics owner (Saket Mittal, September 2026)"
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary methodology/docs pages
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Google AI Overviews (named as a distinct surface from AI Mode), Google AI Mode, Gemini, Claude — all named across these four pages
metric_kind:     visibility
supersedes:      none
captured:        full pages (method page's lever grid condensed — table structure preserved in substance, not cell-by-cell HTML markup)
feature:         AI Visibility — Quattr Method (5-rung "ladder": Reachable/Retrieved/Referenced/Represented/Rewarded), Metrics dictionary (141 metrics, 20 tagged "AI visibility"), Prompt gallery (analyst-facing example prompts, distinct from the brand-tracking prompt set)
```

## Verbatim

### Quattr Method — the five rungs ("Know")

"Five diagnostic questions in a fixed order. Each is a gate: failing it makes every rung above it unreachable, not merely weaker."

- R1 Reachable — "Can crawlers and AI bots fetch you at all?" Measured by: "Server logs for what was actually fetched and with which status, site crawl for what is reachable and indexable, and the two crossed to separate 'could not' from 'did not'."
- R2 Retrieved — "Do you enter the consideration set?" Measured by: "Impressions and ranked-keyword coverage on the search side; prompt-level presence in answer-engine results on the AI side. Absence here reads very differently from a bad position."
- R3 Referenced — "Are you the source answers are built from?" Measured by: "Citation rate and cited URLs per answer engine, share of voice against tracked rivals, and prompt coverage gaps, kept strictly separate from Google's on-SERP AI Overviews, which is a different surface."
- R4 Represented — "Does AI describe you the way you would?" Measured by: "Sentiment and framing in answer text where you are mentioned, read as a distribution over prompts rather than as a single score with an absolute threshold." Flagged on-page as "Partially instrumented — Instrumented for mentions and sentiment; the positioning-fidelity half is not fully measured yet."
- R5 Rewarded — "Does any of it turn into traffic, conversions, revenue?" — "the one that cannot be inferred from the four below it."

"Act — The eight levers, what to do about it." Eight named levers (L1 Technical & crawl health, L2 Demand modeling, L3 Refresh & content quality, L4 Internal linking & architecture, L5 Net-new content, L6 Authority & off-site, L7 AI-answer visibility, L8 Paid/organic interplay), each mapped to which rung(s) it primarily (P) or secondarily (s) moves, in a grid. L7 "AI-answer visibility" is stated to primarily move R3 (Referenced) and secondarily R4 (Represented).

### AI Visibility Proof Index — full results table

"A customer appears only if its case study reports a measured result on a named AI surface. Nine of the twelve studies report search outcomes only, or mention AI surfaces as context without a figure, so they are not listed." "Where a study presents a number only inside a chart or a table without stating its scope in the text, that number is left out. A figure whose study states no window carries 'Not stated' rather than a window borrowed from the result beside it."

AI-surface results table (customer / AI surface / metric / result / measurement window):
- Men's Wearhouse — Google AI Mode — AI Mode prompt and query footprint — Grew 75% — "The observed launch window"
- Men's Wearhouse — ChatGPT — Top-3 citation coverage — Grew 50% — "The observed launch window"
- CloudEagle — "AI answers, captured from consumer-facing responses" — AI Citation Share — Increased 3x after optimizations (scope note 2) — 12 weeks
- Kiteworks — Google AI Overviews — AI Overview presence — 79% expansion (scope note 3) — "Not stated"
- Kiteworks — Google AI Overviews — Content citation rate against baseline — 20% higher (scope note 3) — "Within one week"

Companion search-outcome table (same customers/engagements, explicitly separated so the two kinds of result do not read as one number) — includes: Men's Wearhouse "10x stronger day-30 clicks on GIGA-launched pages" (first 30 days after launch); Men's Wearhouse "46% more clicks during the rollout" (scope note 1, post-rollout window); CloudEagle clicks "2.47K to 5.25K, a 113% sustained lift" (12 complete weeks following intervention); CloudEagle "77% of post-intervention clicks" and "328 queries" (post-intervention); Kiteworks "30% increase [in indexed pages], reversing a decline" (within eight weeks of deployment); Kiteworks "22% increase [keywords positions 1-3], alongside 18% more unique keywords" (within six weeks).

Scope notes (reproduced in full, verbatim):
1. "The product-page figure is the rollout outcome, not an isolated linking effect. The study reports the product-page result in two layers and says so explicitly. 46.4% is the total treated lineage-level rollout outcome, measured over 1,136 treated product page lineages carried forward through successor self-canonical URLs. After controlling for starting traffic and variant-opening footprint, the most heavily linked product pages still showed a roughly 7% to 8% click advantage over the least linked group, and that is the figure the study calls the isolated linking signal."
2. "The AI citation figure was read from live answers. The study states the scope of its own capture: the insights came from real consumer-facing AI responses, not simulated prompts or API outputs. It does not attribute the 3x increase to a single named engine, so no engine is named here. AI Citation Share is the metric name the study uses."
3. "This result is on Google AI Overviews, an on-SERP surface. The study's own headline calls these answer engine citations, and its body measures AI Overview presence. AI Overviews and answer-engine citations are different surfaces collected in different ways, so the surface named here is the one the body measured. The study states no measurement window for the 79% figure; the one-week window belongs to the citation-rate figure beside it."

### Metrics dictionary — AI visibility category (20 of 141 total metrics)

Header stats: "93 report families · 22 categories · 10 inferred · 38 in review · 141 metrics." Status legend, verbatim: "Verified: the formula and sources were confirmed against the product by the analytics owner (Saket Mittal, September 2026). Inferred: the definition follows the product's documentation and has not yet been confirmed against the implementation. In review: drafted, awaiting the analytics owner's sign-off, shown so the gap is visible rather than hidden."

Sampled metric definitions, verbatim:
- "AI answer presence score — A weighted points total for how present your brand is in answer-engine responses: each citation counts 1.25 and each brand mention counts 1, summed over the tracked prompt basket for one answer engine." Type: score. Unit: weighted points. Rung: R3.
- "AI citation count — The number of times answer engines cited your site across the tracked prompt basket in a period." Type: raw measure. Unit: citations. Rung: R3.
- "AI citation rate — Your share of all the citations answer engines awarded across the tracked competitor set for a prompt basket, your citations as a percentage of every tracked domain's citations, not the proportion of answers that cited you." Type: share. Unit: percent of all tracked domains' answer-engine citations. Rung: R3.
- "AI mention count — The number of answer-engine responses in the period that named your brand." Type: raw measure. Unit: mentions. Rungs: R4, R3.
- "AI mention share — The share of answer-engine responses naming your brand, relative to the brands named across the tracked set." Type: share.

Data-source breakdown for the "AI visibility" metric category specifically: 20 metrics draw on a data source itself labelled "AI visibility" (distinct from Rank tracking 51, Google Search Console 32, GA4/Adobe Analytics 27, Google Ads 24, Lighthouse/CWV 15, Server logs 6, Site crawl 5). Separately, 5 metrics are tagged "AI referral traffic" as their own category.

### Prompt gallery — distinct from the brand-tracking prompt set

`quattr.com/ai-visibility/prompts` lists 106 total example prompts across 12 categories (AI visibility 14, Content 5, Market share 5, Organic 14, Paid 5, Replaces a ritual 31, Reporting 6, Revenue 4, Stats 9, Technical 7, Utilities 6). These are analyst-facing example questions a user types into an AI client connected to Quattr (e.g. "How visible are we across AI answer engines?"; "What is our citation rate on ChatGPT vs Perplexity?"; "Are our AI citations trending up or down?"), each tagged with a target role (SEO lead / Content lead / Exec / Engineering) and a linked workflow. **This page is not the "tracked prompt basket" used to compute AI citation/mention metrics for a brand** — no page reached this cluster discloses the size (n) or literal content of that underlying brand-tracking prompt basket.

## Pull notes — mechanical only

- All four pages fetched via `curl` with a browser User-Agent string; each returned HTTP 200, full static HTML.
- The method page's lever-by-rung grid is reproduced in substance (which lever moves which rung, primary vs. secondary) rather than as a literal HTML table transcription, since the source markup interleaves grid cells with repeated header text in a way that does not linearize cleanly to plain text; the mapping stated here is complete and unaltered from the source's own cell-by-cell claims.
- **Prompt-set/n/method disclosure answer for Quattr: partial.** Method (the five-rung ladder, the eight levers, and every metric's exact formula) is disclosed in more structural detail than any other vendor pulled in this cluster, and the AI Visibility Proof Index explicitly states measurement windows or their absence per case. But the size (n) and literal content of the "tracked prompt basket" or "tracked prompt set" that AI citation/mention metrics are computed over is not disclosed on any page reached — the "prompt gallery" page names a different, unrelated set of analyst example-questions, not the brand-visibility tracking prompt set.

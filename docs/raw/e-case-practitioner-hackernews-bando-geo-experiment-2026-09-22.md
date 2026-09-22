# Hacker News (marcosviladomiu) — Bang & Olufsen EMEA Marketing Director's brand-recommendation tracking experiment

```yaml
source:          marcosviladomiu, self-described EMEA Marketing Director at Bang & Olufsen, Hacker News post
url_or_doc_id:   https://news.ycombinator.com/item?id=47349948 (HN Algolia API: https://hn.algolia.com/api/v1/items/47349948)
published:       2026-03-12
pull_date:       2026-09-22
pull_method:     fetch (HN Algolia API, raw JSON, via curl)
pull_purpose:    evidence about category noise
tier:            6
tier_reason:     No n, no absolute date window ("over the past year" only), no quantified figures for any claim ("results were uncomfortable" is qualitative). Self-reported role (Bang & Olufsen EMEA Marketing Director) not independently verified against a company or LinkedIn profile in this pull. Discard-on-sight per trust-rubric.md ("No n, no date window, or no method") — kept at tier 6 and filed only as category-noise evidence, per pull_purpose, not as a number.
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Claude — no model versions stated
metric_kind:     visibility
supersedes:      none
captured:        full page (post text); 0 comments returned by the API
vertical:        none named — "premium audio" is the author's own category description, not one of the three tracked verticals (skincare and beauty, B2B SaaS, high-CPA regulated); recorded as `none named` per demand-signals.md cell-attribution rule, category quoted verbatim above
evidence_grade:  Fools gold, and thin even for that grade. Bar items present: brand named (Bang & Olufsen, via a self-described EMEA Marketing Director — a credibly specified profile, not anonymised); engines named (ChatGPT, Perplexity, Claude); a described method (manual prompting with "prompt templates and spreadsheets", tracked over time). Bar items missing: no absolute date window ("past year" only); no baseline figure or post figure — "results were uncomfortable" and "some brands... others... at times" carry no number; no sample size (prompt count, run count) stated; three named metrics (Share of Echo Voice, Brand Accuracy Score, Conversational Depth Index) are defined but no value is given for any of them; who measured is the author only, self-reported, unverified, and the author discloses monetizing the framework ("I wrote a short book on this").
artefacts_published: none in the post itself — a "short book" is mentioned as available on request but not linked or published in this thread
direction:       negative (as characterized by the author — "the results were uncomfortable" and Bang & Olufsen itself is named as sometimes among the brands with weak or absent AI recommendations) — unquantified
```

## Verbatim

**Post title:** (none — HN Algolia returned no `title` field; this was a self-text submission)
**Author:** marcosviladomiu
**Points:** not returned by API (field absent)
**Created:** 2026-03-12T12:58:39.000Z

I'm the EMEA Marketing Director at Bang & Olufsen. Over the past year
I've been running a simple experiment: asking ChatGPT, Perplexity, and
Claude for brand recommendations in our category — premium audio — and
tracking which brands appear, how often, and with what level of
specificity.

The results were uncomfortable. Some brands consistently surface
with rich, accurate descriptions. Others — including ours at times —
either don't appear or appear with vague, outdated framing. This has
nothing to do with SEO. It's about how well a brand's identity is
structured in the data that LLMs train and retrieve from.

I've been calling this GEO — Generative Echo Optimisation. The core idea: AI doesn't find your brand, it reflects it. If your brand's presence online is fragmented, inconsistent, or lacks depth, the AI produces a faint echo or none at all.

A few things I've been trying to measure:

- Share of Echo Voice (SEV): % of times your brand appears vs.
  competitors in relevant AI recommendation queries
- Brand Accuracy Score (BAS): how closely AI descriptions match
  your intended positioning
- Conversational Depth Index (CDI): how much detail AI generates
  about your brand vs. surface-level mentions

The problem is there's no standard tooling for this yet. I'm doing
it manually with prompt templates and spreadsheets.

Has anyone else been tracking this? Are there tools I'm missing?
And do you think GEO is a real discipline or just repackaged content strategy with an AI label?

(I wrote a short book on this if anyone wants the framework — but genuinely more interested in what others have found.)

## Pull notes — mechanical only

- Retrieved via `https://hn.algolia.com/api/v1/items/47349948` (Hacker News Algolia API). The item's JSON returned `title: null` and `points: null` — this appears to be a submission where HN Algolia's story metadata is sparse (title/points fields absent from the API response); the post is a self-text submission (no external `url`), confirmed by the `text` field being present and populated.
- `children` array was empty at pull time (0 comments) — matches the story-search result's `num_comments: null`/absent reported earlier in this cluster's discovery pass.
- The author's claimed identity (Bang & Olufsen EMEA Marketing Director) was not independently cross-checked against a company page, LinkedIn, or press mention in this pull — recorded as self-reported, per `source_label: company-stated`.
- No book title, ISBN, or link was given for the "short book" mentioned — cannot be located or pulled from this post alone.

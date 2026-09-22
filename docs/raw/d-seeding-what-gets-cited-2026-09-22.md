# Vishwakarma, Kumar & Jamidar (arXiv, Sprinklr) — What Gets Cited: Competitive GEO in AI Answer Engines

```yaml
source:          Rahul Vishwakarma, Shushant Kumar, Ratnesh Jamidar (all affiliated with Sprinklr)
url_or_doc_id:   arxiv.org/abs/2605.25517
published:       2026-05-25
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-authored — all three authors affiliated with Sprinklr, paper reports "an early internal pilot at Sprinklr"; abstract claims a public protocol release but no code/data/checklist URL was found anywhere on the page or html full text (checked 2026-09-22) — academic table row "vendor-authored," bias flagged
source_label:    vendor-reported
lane:            D
sub_market:      organic recommendation
engine:          Gemini-2.5-Flash, GPT-5-Nano, GPT-5-Mini, GPT-5.2, Claude-3.5-Sonnet, Kimi-K2-Thinking
metric_kind:     visibility
supersedes:      none
captured:        abstract, limitations section, author-affiliation and code-release check (via arxiv.org/html/2605.25517 full-text extraction)
technique:       corpus seeding adjacent — factor-level study of what makes one of two competing sources get cited first (topical relevance, list position, price disclosure, recency, completeness/trust cues, formatting)
models_tested:   Gemini-2.5-Flash, GPT-5-Nano, GPT-5-Mini, GPT-5.2, Claude-3.5-Sonnet, Kimi-K2-Thinking
date_window:     not given as an execution date range; paper dated "25 May 2026," references a July 2026 conference
measured_effect: yes — 252,000 trials, 18 content factors, mixed-effects models; "topical relevance and list position are the biggest drivers of being cited first," price info and recent timestamp "help consistently," completeness/trust cues "add smaller gains," "formatting-only edits have little impact"
vertical:        none named
```

## Verbatim

### Abstract

"AI answer engines generate answers from retrieved pages but cite only a few sources. This makes visibility depend not just on ranking, but on being cited. We study competitive Generative Engine Optimization (GEO): when two retrieved candidates compete, what makes one more likely to be cited first? We build a controlled two-document retrieval-augmented generation (RAG) testbed that injects exactly two candidate sources into the model context and measures which source is referenced by the first citation marker in the output. Across six LLMs we execute 252,000 trials, repeated paired comparisons under one factorial program over 18 content factors. In each trial the two sources differ in exactly one factor; we use brand anonymization and counterbalanced source order to separate content effects from position bias. Mixed-effects models show that topical relevance and list position are the biggest drivers of being cited first. Including explicit price information and a recent timestamp also helps consistently. Completeness and trust cues add smaller gains, while formatting-only edits have little impact. We release a reproducible evaluation protocol and a prioritized GEO checklist for practitioners, and we exercised it in an early internal pilot at Sprinklr, where teams reported positive qualitative feedback on workflow usability."

### Author affiliations (verbatim, from html full text)

Rahul Vishwakarma: Sprinklr, Gurugram, India. Shushant Kumar: Sprinklr, Dubai, UAE. Ratnesh Jamidar: Sprinklr, Gurugram, India.

### Limitations (verbatim)

"Production RAG often retrieves five to ten or more pages, so real citation pools are larger than our testbed. We nevertheless injected exactly two candidates because the study targets factor-level attribution: we ask which single content attributes move first-citation preference when everything else is held fixed."

"We anonymized brands and publishers so citation choices reflect the text, not a famous name or a well-known site the model may have seen often. Production systems may still favor trusted domains or strong brands when they pick sources."

"GPT-4o was used to generate seeds, perform anonymization, and create paired rewrites. The process of building the corpus is distinct from how citation preferences are evaluated."

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2605.25517 for metadata, arxiv.org/html/2605.25517 for full text), both 200.
- Discrepancy noted mechanically: the abstract states "we release a reproducible evaluation protocol and a prioritized GEO checklist," but no repository, dataset, or checklist URL was located anywhere in the fetched abs page or html full text as of this pull.

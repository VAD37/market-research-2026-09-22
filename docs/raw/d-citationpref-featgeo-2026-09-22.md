# Liu and Xu — Think Before Writing: Feature-Level Multi-Objective Optimization for Generative Citation Visibility (FeatGEO)

```yaml
source:          Zikang Liu, Peilan Xu
url_or_doc_id:   arxiv.org/abs/2604.19113; accepted ACL 2026 (aclanthology.org/2026.acl-long.929 per the P5-c1 critical-survey pull's bibliography)
published:       2026-04-21
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed venue (ACL 2026, per the critical survey's bibliography entry: "Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics") with code released ("Code is availab[le]") — academic table "peer-reviewed, data or code published"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          GEO-Bench evaluated across three generative engines: GPT-4o-mini, Gemini-2.5-flash, Qwen-plus; quality judged by GPT-4o-mini plus two alternate judges Gemini-2.5-flash and Claude-3.5-Sonnet
metric_kind:     visibility
supersedes:      none
captured:        abstract, mechanism (feature-space taxonomy: structural/content/linguistic properties), the interpretable feature list including fluency, authority, statistics, entity-adjacent dimensions, before-and-after results tables comparing token-level heuristic rewrites against FeatGEO's feature-level method, and a genuine pre/post test on human-written competitor pages
technique:       content written to satisfy known citation preferences — directly operationalizes the technique's exact named features (statistics, authoritative tone, fluency, keyword focus, readability) as a structured, scored "feature space" and tests each in isolation and combination
models_tested:   GPT-4o-mini, Gemini-2.5-flash, Qwen-plus (generative engines); GPT-4o-mini (primary quality judge), Gemini-2.5-flash and Claude-3.5-Sonnet (alternate judges); Qwen3-4B mentioned as a further tested scale
date_window:     not stated beyond arXiv submission date 2026-04-21
measured_effect: yes — token-level heuristic rewrites (Authoritative, Statistics, Citations, Fluency, Unique Words, Easy-to-Understand, Technical Terms) DECREASE visibility vs. an unmodified baseline on GEO-Bench; FeatGEO's own feature-level method increases visibility +37% to +96% relative, depending on engine; separately, a genuine before/after test on human-written pages shows heuristic methods average +0.99 points (18.72% to 19.71%)
vertical:        none named in the passages captured here; one worked example in "the education domain" (Table 5) is domain-specific but not one of this programme's three anchor verticals
```

## Verbatim

### Abstract

"Generative answer engines expose content through selective citation rather than ranked retrieval, fundamentally altering how visibility is determined. This shift calls for new optimization methods beyond traditional search engine optimization. Existing generative engine optimization (GEO) approaches primarily rely on token-level text rewriting, offering limited interpretability and weak control over the trade-off between citation visibility and content quality. We propose FeatGEO, a feature-level, multi-objective optimization framework that abstracts webpages into interpretable structural, content, and linguistic properties. Instead of directly editing text, FeatGEO optimizes over this feature space and uses a language model to realize feature configurations into natural language, decoupling high-level optimization from surface-level generation. Experiments on GEO-Bench across three generative engines demonstrate that FeatGEO consistently improves citation visibility while maintaining or improving content quality, substantially outperforming token-level baselines. Further analyses show that citation behavior is more strongly influenced by document-level content properties than by isolated lexical edits, and that the learned feature configurations generalize across language models of different scales."

### Mechanism — the named feature dimensions, verbatim

"easy_to_understand_level [1.0, 3.0] Content readability and language simplicity; fluency_level [1.0, 3.0] Writing fluency and logical coherence between sentences; keyword_focus_level [1.0, 3.0] Focus and rep[etition strength of core keywords]."

"[Baseline heuristic methods compared against include] Easy-to-Understand (simpler language), Fluency Optimization (improved fluency), Unique Words & Technical Terms (lexical enrichment)... AutoGEO-global (Wu et al., 2025): a token-level rewriting framework."

"[Feature configurations] mapped to descriptive cues (e.g., emphasizing statistics or improving structural clarity), which are incorporated into the system prompt."

### Results — Table 2, GEO-Bench visibility (Vis%) by engine and method

Method | GPT-4o-mini Vis | Gemini-2.5-flash Vis | Qwen-plus Vis
---|---|---|---
Baseline (unmodified) | 13.34 | 8.89 | 5.20
Fluency Optimization | 11.74 | 5.04 | 3.67
Unique Words | 10.92 | 4.62 | (not captured)
Cite Sources | 11.78 | 5.62 | 3.46
Easy-to-Understand | 11.06 | 4.96 | 3.03
Technical Terms | 11.81 | 5.55 | 3.59
FeatGEO (ours) | 18.31 | 15.35 | 10.17

"On GPT-4o-mini, visibility drops range from 10.92% to 12.21% compared to the baseline of 13.34%; on Gemini, baselines achieve only 4.62%–5.62% versus 8.89%; on Qwen-plus, visibility drops from 5.20% to 2.75%–3.72%. In addition, several baselines negatively impact content quality... FeatGEO achieves the highest visibility across all three engines: 18.31% on GPT-4o-mini (+37% relative improvement), 15.35% on Gemini (+73%), and 10.17% on Qwen-plus (+96%), while maintaining quality scores compara[ble to baseline]."

"[Cross-judge robustness check:] under two alternative LLM judges, Gemini-2.5-flash and Claude-3.5-Sonnet... although the absolute scores are lower than those of the original GPT-4o-mini evaluator, FeatGEO remains the top-ranked method under both Gemini (75.28) and Claude (72.63), outperforming the strong[est baselines, e.g.] Statistics Addition 69.45/69.07, Keyword Stuffing 69.13/69.81."

### Results — Table 4, a genuine pre/post test on human-written competitor pages, verbatim

"[Heuristic GEO methods applied to] human-written competitor pages... these methods yield an average visibility gain of +0.99 (18.72% to 19.71%), with AutoGEO-global achieving the largest improvement (+4.13, from 18.72% to 22.86%). By contrast, the same heuristics deg[rade visibility when applied to already-LLM-generated content]."

"Table 4: Effects of heuristic GEO methods on human-written competitor pages. Pre and Post denote advertiser visibility before and after applying each method."

### Ablation — token-level heuristics "fail to help all engines," verbatim

"[Across] all engines, token-level GEO heuristics fail to consistently improve citation visibility over the unmodified baseline... isolated text-level modifications are insufficient t[o reliably raise visibility, and some] disrupt the natural writing patterns that LLMs prefer to cite."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2604.19113`, converted to plain text by stripping HTML/MathML tags. Table cell alignment across the three-engine × nine-method grid in Table 2 is imperfect in plain-text extraction; the rows reproduced above (Baseline, Fluency Optimization, Unique Words, Cite Sources, Easy-to-Understand, Technical Terms, FeatGEO) are confirmed against the source text; a small number of additional method rows visible in the source (Statistics Addition, Keyword Stuffing, Authoritative, full Table 4 method list) were only partially captured and are not reproduced as a table row above to avoid mis-attributing a number to the wrong method.
- Table 4 is the clearest true before-and-after design found anywhere in this cluster's pulls: "Pre and Post denote advertiser visibility before and after applying each method" on human-written pages — a genuinely paired measurement, though still a benchmark (GEO-Bench-adjacent corpus), not a real-site case.
- ACL 2026 venue and DOI/page numbers (aclanthology.org/2026.acl-long.929, pages 20290-20303) are taken from the bibliography entry already captured in the P5-c1 critical-survey pull (`d-seeding-critical-survey-2026-09-22.md`), not independently re-verified against ACL Anthology by this pull; `unknown — checked aclanthology.org 2026-09-22` for direct confirmation of the camera-ready page range.
- This paper is the P5-c1 census's own screened-out item "2604.19113 (FeatGEO)" — listed there under "GEO papers about a brand's own owned-content optimization, detection, or platform mechanism design (not third-party seeding)" and explicitly judged off-cluster for P5-c1's corpus-seeding scope. It is squarely in-scope for P5-c4 (own-content rewriting to match citation preferences) and was not previously pulled in full; this is a first full pull, not a re-pull.

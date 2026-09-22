# Bagga et al. — E-GEO: A Testbed for Generative Engine Optimization in E-Commerce

```yaml
source:          Puneet S. Bagga, Vivek F. Farias, Tamar Korkotashvili, Tianyi Peng, Yuhang Wu
url_or_doc_id:   arxiv.org/abs/2511.20867
published:       2025-11-25 (v1); last revised 2026-07-14 (v2)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; no venue/review status or code-release statement isolated in this extraction — academic table "preprint without code"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Five representative generative engines (not individually named in the passages captured beyond the rewriter models below); seven LLM rewriters tested with a simple prompt; fifteen hand-crafted heuristic prompts tested with GPT-4.1 as the fixed rewriter, evaluated against five re-rankers
metric_kind:     visibility
supersedes:      none
captured:        abstract, the fifteen named heuristic rewriting styles (directly matching this task's named content features: authoritative tone, FAQ, fluency, technical terminology), quantitative per-heuristic results table, red-team/defense finding
technique:       content written to satisfy known citation preferences — e-commerce-specific test of hand-crafted rewrite heuristics including an explicit "FAQ" heuristic and an "authoritative" heuristic, with a per-heuristic quantitative comparison against a no-heuristic simple-prompt baseline
models_tested:   GPT-4o, GPT-4o-mini, GPT-5, GPT-5.1, GPT-5-mini, Claude Sonnet, Gemini, DeepSeek, Llama 4 (named collectively as tested rewriters/engines across the paper; GPT-4.1 specifically fixed as the rewriter for the fifteen-heuristic sweep)
date_window:     v1 submitted 2025-11-25, v2 revised 2026-07-14; no narrower data-collection window stated
measured_effect: yes — of fifteen heuristic prompts, only four ("trick" +0.14, "FAQ" +0.05, "competitive" +0.03, "format" +0.02) modestly beat or matched the simple-prompt baseline (-0.03 row-mean rank improvement); eleven were worse, several substantially so (advertisement -1.82, language -1.66, minimalist -1.49, storytelling negative-control -4.36)
vertical:        e-commerce, general — "13,747 realistic, multi-sentence consumer product queries, each paired with 10 retrieved Amazon listings"; not one of this programme's three named anchor verticals (skincare, B2B SaaS, high-CPA regulated) but adjacent (general e-commerce/retail)
```

## Verbatim

### Abstract

"With the rise of large language models (LLMs), generative engines have become powerful alternatives to traditional search, reshaping retrieval tasks. In e-commerce, for instance, conversational shopping agents now guide consumers to relevant products. This shift has created the need for generative engine optimization (GEO) -- improving content visibility and relevance for generative engines. Despite its growing importance, current GEO practices are largely ad hoc, and their impacts remain poorly understood, especially in the e-commerce setting. We address this gap by introducing E-GEO, the first dataset built specifically for e-commerce GEO. E-GEO contains 13,747 realistic, multi-sentence consumer product queries, each paired with 10 retrieved Amazon listings, capturing rich intent, constraints, preferences, and shopping contexts that existing datasets miss. Using this dataset, we conduct the first large-scale empirical study of e-commerce GEO across five representative generative engines, seven popular LLM rewriters, and fifteen hand-crafted rewriting heuristics. We further formulate GEO as an optimization problem and develop a lightweight prompt meta-optimization algorithm that significantly improves over heuristic baselines. Notably, the optimized prompts reveal a stable, domain-agnostic pattern, suggesting the existence of a 'universally effective' GEO strategy. Finally, we red-team the GEO system through both heuristic and optimization-based attacks and show that, under a simple in-prompt defense, gains from GEO reflect genuine content improvement rather than manipulation, anchoring GEO as a substantive and well-defined optimization problem."

### Method — the fifteen named heuristics, verbatim

"Prompt | Description — authoritative: Confident, assertive tone. format: Use headings & bullets. technical: Use technical terminology. FAQ: Add an FAQ. unique: Use rare vocabulary. advertisement: Advertisement-like style. fluent: Improve linguistic flow. language: Use foreign expressions. clickable: Persuasive & compelling. minimalist: Reduce to a single sentence. diverse: Reflect inclusivity. storytelling: Write a creative short story. quality: Emphasize product quality. trick: Format like LLM output. competitive: Highlight unique advantages."

"[The] storytelling [heuristic] asks for a creative short story, which is expected to perform badly and is included as a deliberate negative control. For cost purposes, we fix the rewriter to GPT-4.1 and evaluate all fifteen prompts on the five re-rankers."

### Results — per-heuristic rank improvement, verbatim

"Table 5 reports per-prompt mean rank improvement on the test set across the five re-rankers. Overall, heuristic prompts do not reliably outperform the simple prompt. With GPT-4.1 as the rewriter, the simple prompt has a row-mean rank improvement of -0.03 (Table 3), and only four heuristic prompts — trick (row mean +0.14), FAQ (+0.05), competitive (+0.03), and format (+0.02) — modestly beat or match that baseline. The other eleven are worse, several substantially so: advertisement (-1.82), language (-1.66), and minimalist (-1.49) (and of course the storytelling negative control (-4.36)) all drag the rewriter into deeply negative territory. Therefore, manually instilling 'GEO knowledge' through prompt design can backfire, and a more principled, data-driven approach to optimization is needed for reliable improvements."

### Foundational-paper context, verbatim

"[The technique category was] introduced by Aggarwal et al. (2024), who evaluated several hand-crafted rewriting heuristics for increasing a web source's visibility within generative-engine outputs, using an impression score that combines word count, citation position, and GPT-3.5–based quality assess[ment]."

"[Regarding a length/formatting confound found across methods:] length and bullets explain R² = 0.01 of the variance, versus R² = 0.14 for prompt and re-ranker identity."

### Universal-strategy and red-team findings, verbatim

"[The optimizer's solutions reveal] a 'universally effective' rewriting strategy that generalizes across queries, products, and generative engines, suggesting that systematic optimization obviates the need for ad hoc heuristics."

"[We] red-team the GEO system through both heuristic and optimization-based attacks and show that, under a simple in-prompt defense, gains from GEO reflect genuine content improvement rather than manipulation."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2511.20867`, converted to plain text by stripping HTML/MathML tags. This paper had by far the largest extracted text of this cluster's nine pulls (168,301 characters after tag-stripping); only the passages most directly relevant to Pass 5's four questions are captured here, not the full paper.
- This is the only item in this cluster with an explicit "FAQ" heuristic tested in isolation and quantified against a baseline (+0.05, one of only four of fifteen heuristics that did not underperform) — directly on-point for the task's named feature "FAQ blocks."
- "Authoritative" is also tested as one of the fifteen heuristics but its specific row-mean result was not isolated in the passages captured in this extraction pass (only trick, FAQ, competitive, format, advertisement, language, minimalist and storytelling numbers were captured verbatim); `unknown — checked arxiv.org/html/2511.20867 2026-09-22` for the "authoritative" heuristic's specific numeric result in this pull, though the paper states it is one of the fifteen tested and implicitly falls among the eleven that did not beat baseline (only four named ones did, and authoritative was not among the four named).
- Vertical: e-commerce/retail generally (Amazon listings), which is adjacent to but not identical to any of this programme's three named anchor verticals; recorded as "none named" against the three fixed verticals per the task's tagging rule, with e-commerce noted as the closest adjacent category, consistent with how `d-seeding-igaming-notability-2026-09-22.md` (P5-c1) was tagged "adjacent, not identical" for its regulated-vertical analogue.
- No code/data release URL was isolated in this extraction; `unknown — checked arxiv.org/html/2511.20867 2026-09-22` for a repository link.

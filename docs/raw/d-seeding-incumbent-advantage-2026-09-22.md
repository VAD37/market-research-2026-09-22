# Chu & Hou (arXiv) — Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems

```yaml
source:          Xi Chu, Yupeng Hou
url_or_doc_id:   arxiv.org/abs/2606.17443
published:       2026-06-16 (v1 submitted); last revised 2026-08-21
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint, no code/data/prompt release found on abs or html page (checked 2026-09-22) — academic table row "preprint without code"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          GPT-4o-mini, Claude Sonnet, Gemini 3 Flash (exact model snapshot dates not stated)
metric_kind:     visibility
supersedes:      none
captured:        abstract, methodology summary, results passages, limitations section (via arxiv.org/html/2606.17443 full-text extraction)
technique:       corpus seeding — seed paper assigned to this cluster (docs/sources/shortlist.md P5-c1); note in Pull notes on fit
models_tested:   GPT-4o-mini, Claude Sonnet, Gemini 3 Flash
date_window:     not specified in the paper's methodology (no calendar date range given for API-call collection); paper itself dated 2026-06-16 to 2026-08-21
measured_effect: yes — Conditional Monopoly IAI = 10.0 (100% recommendation rate for the real brand when specs are identical); Bias Surplus Value = +0.17 rating points for authority-style marketing language; payoff collapse from +0.802 to +0.007 under universal strategy adoption
vertical:        skincare and beauty (named; robustness check on USB cables and AA batteries as "search goods")
```

## Verbatim

### Abstract

"Large language models (LLMs) are becoming a major way for consumers to find products, but we do not yet understand how brands compete in this new channel. We study brand dynamics in LLM recommendations using skincare products—a category where consumers cannot easily judge quality before buying and must rely on brand reputation—across three commercial LLMs (GPT-4o-mini, Claude Sonnet, Gemini 3 Flash), with a robustness check on search goods. In three experiments, we find: (1) a Conditional Monopoly where well-known brands get recommended 100% of the time (IAI = 10.0) when all products have the same specifications, but this dominance disappears with less than a +0.1-star rating advantage for a competitor; (2) authority-style marketing language, including fabricated clinical-evidence claims, breaks this monopoly at a Bias Surplus Value equal to +0.17 rating points, with each model responding differently; and (3) a social dilemma in multi-brand GEO competition: when all brands adopt the same optimization strategy, individual payoff falls from +0.802 to +0.007 in our payoff proxy, and non-participating brands receive zero recommendations in our tests."

### Methodology (extracted, html full text)

"Protocol α (top-K ranking) and Protocol β (single recommendation) described in Appendix G. Products presented as numbered lists with identical specifications (rating, price, review count, ingredients) except brand name. Temperature = 0.7 with 20–30 repetitions per cell."

Trial counts by experiment: Experiment 1a — 670 valid of 720 designed; Experiment 1b — 2,769 valid of 2,880; Experiment 1c — 9,220 valid of 9,600; Experiment 1d — 14,395 trials across three models (4,800 designed calls per model); Experiment 2 — 4,080 API calls total; Experiment 3 — 4,800 calls, 4,745 valid (98.8%); RAG probe — 1,080 total, 1,074 valid (99.5%).

### Results

Conditional Monopoly: "When all 10 products have identical specifications—same rating, same price, same review count, same ingredient description—the real brand is recommended every single time—IAI = 10.0, the theoretical maximum. This holds across all three models, both languages, and all four product subcategories; not a single fictional brand was ever recommended."

Bias Surplus Value: "Authority language is worth roughly +0.17 rating points—a meaningful gain that costs nothing to write" (Experiment 2 finding).

Payoff collapse: individual payoff drops to +0.007 "nearly zero" from an initial +0.802 advantage for first movers under universal adoption (Experiment 3, Scenario 4).

### Limitations (verbatim)

"Our main experiments use a single product domain (skincare), chosen as a theoretically motivated starting point where brand reputation is a particularly salient differentiator (§1). A robustness check on two search goods (USB cables and AA batteries; Appendix H) shows that Conditional Monopoly and the step-function transition replicate, but we have not tested Experiments 2–3 on search goods. Whether authority-style language has the same BSV in search-good categories is an open question; specification-rich domains may dilute its effect because objective quality signals are easier to verify. All experiments use a fixed user persona and temperature = 0.7 with 20–30 repetitions per cell. This design controls sampling variance through averaging but does not give exact reproducibility per call. Repeated calls to the same model with the same prompt type are not fully independent samples. To handle this, our main robustness check is a cluster bootstrap that resamples model × subcategory × language blocks (24 clusters, N_boot=2,000 iterations; see Appendix D). All main effects remain significant under this analysis; the Authority 95% CI lower bound (58.9%) remains above the Anchoring upper bound (21.1%), confirming the two-tier pattern. We also report GEE with exchangeable correlation structure as a supplementary analysis; however, with only 3 model-level clusters, we treat those results as supportive rather than primary. We test three closed-source models; open-source models may behave differently. Exp 1d's three-way ANOVA uses N=14,395 valid trials across all three models (4,800 designed calls per model). Our RAG probe (§5.2) uses a single embedding model with no re-ranking or query rewriting; we do not claim generalization to commercial RAG systems, which typically include hybrid retrieval, re-ranking, and query rewriting."

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2606.17443 for metadata, arxiv.org/html/2606.17443 for full-text extraction), both returned 200.
- Fit note: this paper studies competitive brand-description dynamics inside a controlled LLM-recommendation testbed (product listings varying by brand name / marketing language), not literal placement of content into third-party high-citation sources (Wikipedia, Reddit, press wires). It is filed here because `docs/sources/shortlist.md` P5-c1 names it as the cluster's seed paper. Its relevance to "corpus seeding in high-citation sources" is as adjacent evidence on content-shaping dynamics and vertical density (skincare, the anchor vertical), not as a direct seeding-technique study.
- Comments field on arXiv abs page: "16 pages, 4 figures, 11 tables" — no code/data/venue statement.
- Semantic Scholar citation-graph check (api.semanticscholar.org/graph/v1/paper/arXiv:2606.17443/citations): 1 citing paper as of 2026-09-22 — "Who Gets Named: Citation Type Predicts Individual Naming by Grounded Language Models..." (arXiv:2607.23893, Žatuchin, 2026) — topic (individual professional naming) not on point for corpus seeding; not pulled separately.

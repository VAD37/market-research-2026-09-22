# Ho et al. — Rewrite-to-Rank: Optimizing Ad Visibility via Retrieval-Aware Text Rewriting

```yaml
source:          Chloe Ho, Ishneet Sukhvinder Singh, Diya Sharma, Tanvi Reddy Anumandla, Michael Lu, Vasu Sharma, Kevin Zhu
url_or_doc_id:   arxiv.org/abs/2507.21099
published:       2025-07-03; ICML 2025 workshop (per the P5-c1 critical-survey pull's bibliography: "ICML 2025 workshop")
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint, workshop-reviewed (ICML 2025 workshop — lighter review than a full-conference track) with a stated code/data availability appendix section ("A.3 Code and Data Availability") — academic table "preprint with code," held at tier 4 rather than 3 given workshop (not full-conference) review status
source_label:    analyst-derived
lane:            D
sub_market:      paid placement — this item sits at the lane B/D boundary: the technique (retrieval-aware text rewriting) is the same class this cluster investigates, but the object rewritten is explicitly an advertisement, and the outcome metric is ad inclusion/ranking, not organic citation. Recorded here as lane D per the shortlist's P5-c4 assignment, with this crossing flagged
engine:          Not a commercial engine; a RAG pipeline built by the authors, using LLaMA-3.1-8B as the fine-tuned rewriter model and Gemini 1.5 Pro for auxiliary ad domain/subdomain labeling
metric_kind:     visibility
supersedes:      none
captured:        abstract, method (supervised fine-tuning plus PPO reinforcement learning on a custom reward), dataset composition, headline quantitative results (DeltaMRR@K, DeltaDIR@K)
technique:       content written to satisfy known citation preferences — rewrites the item's own text (an ad, structurally identical to rewriting a brand's own page) to match what a retrieval/generation pipeline is measured to favor, using a trained rather than hand-crafted rewriting policy
models_tested:   LLaMA-3.1-8B (base rewriter, supervised-fine-tuned then PPO-trained); Gemini 1.5 Pro (used only for ad domain/subdomain labeling, verified by human annotators, not as the generative engine under test)
date_window:     submitted 2025-07-03; no narrower data-collection window stated
measured_effect: yes — "PPO trained models outperform both prompt engineering and supervised fine-tuning in most cases, achieving up to a 2.79 DeltaDIR@5 and 0.0073 DeltaMRR@5 in instruction-based prompting"
vertical:        none named — general digital-advertising dataset, "1,000 ads as our test data," domain/subdomain-labeled by an LLM but not tagged to this programme's three anchor verticals
```

## Verbatim

### Abstract

"Search algorithms and user query relevance have given LLMs the ability to return relevant information, but the effect of content phrasing on ad visibility remains underexplored. We investigate how LLM-based rewriting of advertisements can improve their ranking in retrieval systems and inclusion in generated LLM responses, without modifying the retrieval model itself. We introduce a supervised fine-tuning framework with a custom loss balancing semantic relevance and content fidelity. To evaluate effectiveness, we propose two metrics: DeltaMRR@K (ranking improvement) and DeltaDIR@K (inclusion frequency improvement). Our approach presents a scalable method to optimize ad phrasing, enhancing visibility in retrieval-based LLM workflows. Experiments across both instruction-based and few-shot prompting demonstrate that PPO trained models outperform both prompt engineering and supervised fine-tuning in most cases, achieving up to a 2.79 DeltaDIR@5 and 0.0073 DeltaMRR@5 in instruction-based prompting. These results highlight the importance of how the ad is written before retrieval and prompt format and reinforcement learning in effective ad rewriting for LLM integrated retrieval systems."

### Method, verbatim

"[This is a form of Retrieval-Augmented Generation (RAG), where] a retriever selects documents passed to a generator... [prior work largely improves retrievers or combines retriever-generator components; this work instead focuses on] rewriting the documents themselves to enhance retrievability—without modifying the retriever."

"To further enhance the retrievability of rewritten ads, we apply Proximal Policy Optimization (PPO) on top of our supervised fine-tuned LLaMA-3.1-8B model. PPO enables the model to optimize directly for our [composite reward]."

"We introduce a novel application of Proximal Policy Optimization (PPO) to optimize ad visibility based on a composite reward that balances ranking relevance and content fidelity."

"[Dataset construction:] ads for the train data and 1,000 ads as our test data to construct our initial advertisement dataset. Each ad is associated with a domain and subdomain label using a large language model (Gemini 1.5 Pro), which were verified through human annotators."

"For each query, we retrieve the top k relevant ads from the main advertisement dataset and generate LLM responses conditioned on those ads. The retrieval rankings produced for each query are then retained for later evaluation in rewriti[ng experiments]."

### Results, verbatim

"Prompt Eng. DeltaMRR@5 0.0051, DeltaDIR@5 0.9061. SFT DeltaMRR@5 0.0022, DeltaDIR@5 1.6382. PPO DeltaMRR@5 0.0073, DeltaDIR@5 2.7944." [Table 2: instruction-based prompting, k=5]

"[F]or the few-shot prompting..., PPO continues to increase DeltaDIR (+1.9[X over baseline, exact multiplier not fully captured])."

"[SFT's low MRR relative to DIR] indicat[es] that content-fidelity supervision alone cannot fully overcome retriever bias but that lower MRR does not correlate with higher inclusion."

"[Explaining why PPO-rewritten text ranks and includes better:] This surfaces high-IDF keywords valued by the retriever while preserving semantics, hence the joint lift in DeltaMRR and DeltaDIR."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2507.21099`, converted to plain text by stripping HTML/MathML tags; the paper's math notation for "Δ" (delta) renders inconsistently in the plain-text extraction (sometimes as "Δ", sometimes duplicated as "Δ \Delta") — normalized to "Delta" throughout this pull for readability; underlying numeric values are unaffected.
- Lane/sub-market crossing flagged explicitly per header: this paper's object of optimization is an advertisement (lane B, paid placement) rather than organic brand content, but the shortlist assigns this exact arXiv ID's citation trail to P5-c4 (lane D, A) because the REWRITING TECHNIQUE — learning what a retrieval/generation pipeline rewards and rewriting text to match it — is the same technique class as the rest of this cluster, applied to a different content type. Included per the task's citation-trail-following instruction, with the crossing named rather than silently normalized.
- This paper's dataset (RewriteToRank) is the same one GEO-Bench (already pulled at P5-c1, `d-seeding-geo-bench-2026-09-22.md`) incorporates as one of its five benchmark datasets ("RewriteToRank 10,000 2,202 Products," per that pull's Table 1) — this pull supplies the RewriteToRank dataset's own originating paper and method, not previously captured in P5-c1.
- Exact train-set ad count was not fully captured in this extraction ("[N] ads for the train data and 1,000 ads as our test data") — the train-set number is recorded as `unknown — checked arxiv.org/html/2507.21099 2026-09-22` in this pull; only the 1,000-ad test set count is confirmed verbatim.
- No independent replication found; single-author-group preprint at workshop-review level.

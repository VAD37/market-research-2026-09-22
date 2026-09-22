# Kim et al. — SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization

```yaml
source:          Sunghwan Kim, Wooseok Jeong, Serin Kim, Sangam Lee, Dongha Lee
url_or_doc_id:   arxiv.org/abs/2602.12187; accepted KDD 2026
published:       2026-02-12 (v1); last revised 2026-08-07 (v2)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint accepted at a peer-reviewed venue ("Accepted at KDD 2026"), large corpus with published construction method (170k documents, 9 domains); no prompt-set URL isolated in this extraction, so held at preprint-with-method rather than upgraded to full "peer-reviewed, data or code published" tier 3 pending confirmation of a public release
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          GPT-5.4, GPT-5-mini, Claude-Sonnet-4.6, Qwen3-80B (generation stage); Qwen3-Reranker-4B (reranking stage)
metric_kind:     visibility
supersedes:      none
captured:        abstract, mechanism (full-pipeline evaluation including retrieval/reranking, not just generation), corpus construction, headline finding that content-only rewrites degrade retrieval even while improving citation
technique:       content written to satisfy known citation preferences — specifically isolates the risk this whole cluster's other papers also surface: a rewrite optimized for the generation/citation stage alone can backfire at the earlier retrieval/reranking stage, which existing benchmarks (that skip retrieval) cannot detect
models_tested:   GPT-5.4, GPT-5-mini, Claude-Sonnet-4.6, Qwen3-80B, Qwen3-Reranker-4B
date_window:     v1 submitted 2026-02-12, v2 revised 2026-08-07 for KDD 2026 acceptance; no separate data-collection window stated
measured_effect: yes — content-only (body-text) rewriting "provides only marginal gains in generation-stage visibility and, more importantly, degrades retrieval performance, causing optimized documents to drop out of the retrieval results"; adding structural information (schema markup) mitigates this degradation
vertical:        none named — 170k web documents spanning 9 unnamed domains
```

## Verbatim

### Abstract

"Search-Augmented Generative Engines (SAGE) have emerged as a new paradigm for information access, bridging web-scale retrieval with generative capabilities to deliver synthesized answers. This shift has fundamentally reshaped how web content gains exposure online, giving rise to Search-Augmented Generative Engine Optimization (SAGEO), the practice of optimizing web documents to improve their visibility in AI-generated responses. Despite growing interest, no evaluation environment currently supports comprehensive investigation of SAGEO. Specifically, existing benchmarks lack end-to-end visibility evaluation of optimization strategies, operating on pre-determined candidate documents that abstract away retrieval and reranking preceding generation. Moreover, existing benchmarks discard structural information (e.g., schema markup) present in real web documents, overlooking the rich signals that search systems actively leverage in practice. Motivated by these gaps, we introduce SAGEO Arena, a realistic and reproducible environment for stage-level SAGEO analysis. Our objective is to jointly target search-oriented optimization (SEO) and generation-centric optimization (GEO). To achieve this, we integrate a full generative search pipeline over a large-scale corpus of web documents with rich structural information. Our findings reveal that existing approaches remain largely impractical under realistic conditions and often degrade performance in retrieval and reranking. We also find that structural information helps mitigate these limitations, and that effective SAGEO requires tailoring optimization to each pipeline stage. Overall, our benchmark paves the way for realistic SAGEO evaluation and optimization beyond simplified settings."

### Mechanism, verbatim

"[Prior work] predominantly operate[s] on pre-determined candidate documents, abstracting away the retrieval and reranking stages that precede generation. It remains unclear whether current optimization strategies trade off or benefit performance at earlier search stag[es]."

"Existing benchmarks operate solely on plain body text, discarding structural information present in real web documents (e.g., schema markup). In practice, real search systems do not determine visibility from body text alone. Structural in[formation continues to play an important role]."

"[We construct SAGEO Arena using guidelines] published by commercial search engines, we extract both body text and rich structural information that SAGEO must navigate in practice (e.g., meta descriptions, headings, and schema markup)."

"SAGEO jointly optimizes structural information and body text across the full pipeline to succeed at both stages."

### Corpus, verbatim

"Extensive corpus with rich structural annotations. We curate a corpus of 170k web documents spanning 9 domains. Following guidelines published by commercial search en[gines for structured content]."

### Results, verbatim

"[Content-only, body-text rewriting] provides only marginal gains in generation-stage visibility and, more importantly, degrades retrieval performance, causing optimized documents to drop out of the retrieval results. By contrast, structural information helps mitigate this deg[radation]."

"[T]he two scopes [structural information and body text] play fundamentally complementary roles, with structural information driving retrieval and informative body text remaining a key factor for reranking and generation."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2602.12187`, converted to plain text by stripping HTML/MathML tags.
- This paper is cited in the P5-c1 critical-survey pull (`d-seeding-critical-survey-2026-09-22.md`) as "Kim et al. 2026 PREPR. full pipeline — Downstream rewrites degrade retrieval and reranking; non-commercial pipeline," listed there as a forward-looking citation ("How can we measure the full pipeline") without full detail — this pull supplies that detail directly from the primary source.
- Directly relevant to the task's named content features: schema markup and structured data are explicitly one of the two "scopes" this paper tests, and it finds body-text-only rewriting (the more literal reading of "content written to satisfy citation preferences") can actively hurt visibility by failing at the retrieval stage even as it may help at the generation/citation stage — a stage-decomposition finding not present in this cluster's other papers, most of which test generation-stage visibility only.
- "Non-commercial pipeline" (per the critical survey's own characterization) — SAGEO Arena's retrieval, reranking and generation components are the paper's own constructed pipeline over a static corpus, not a live commercial search engine; this is benchmark evidence, not a real-site or production-engine test, consistent with every other item in this cluster.
- Exact domain names for the "9 domains" in the 170k-document corpus were not isolated in this extraction pass; `unknown — checked arxiv.org/html/2602.12187 2026-09-22` for the domain list, so this pull cannot tag the corpus to any of this programme's three anchor verticals with confidence.

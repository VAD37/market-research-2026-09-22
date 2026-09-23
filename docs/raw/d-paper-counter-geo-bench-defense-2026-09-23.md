# Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization

```yaml
source:          Bing Zheng, Zongyao Zhao, Wenming Yang
url_or_doc_id:   arXiv:2609.02316 ; https://arxiv.org/abs/2609.02316
published:       2026-09-02 (arXiv v1; latest listed 2026-09-02)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (EMNLP 2026 Main) with public benchmark and detector (HuggingFace)
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          victim LLMs Gemma-4-31B-IT, Qwen-3.5-35B-A3B, Claude/others; GPT-5.5 rewriter
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     6
venue_status:    EMNLP 2026 Main
code_availability: https://huggingface.co/datasets/counter-geo/counter-geo-bench ; https://huggingface.co/counter-geo/c-geo-guard
capability_class: defense benchmark showing off-the-shelf guardrails miss information-distorting GEO; a contrastive detector cuts it
```

## Verbatim — abstract

"Generative engine optimization (GEO) enables content producers to increase the visibility of their web pages in generative search engines, but the same techniques can deliver targeted misinformation when adversaries publish ordinary-looking GEO-optimized documents that victim large language models (LLMs) retrieve and synthesize into distorted answers. No existing benchmark evaluates defenses against this threat under controlled conditions. Therefore, we present Counter-GEO-Bench, a defense benchmark that pairs 247 human-verified, quality-gated queries with information-preserving and information-distorting GEO rewrites, and evaluates defenses on attack success rate (ASR), false positive rate, and answer quality across three victim LLMs. Under Counter-GEO-Bench, three off-the-shelf defenses (Granite Guardian, Llama Guard 3, and NeMo Self-Check Fact-Checking) reduce ASR by at most 5.7% relative, while Granite Guardian's reduction is not statistically significant. Safety-taxonomy guardrails target policy violations, while GEO misinformation passes through them as fluent informational content. To this end, a lightweight benchmark baseline, C-GEO Guard, is proposed, reducing ASR by 47.6% relative with near-zero utility loss, which proves threat tractable."

## Verbatim — result sentences (from arXiv HTML full text)

- "Under Counter-GEO-Bench , three off-the-shelf defenses (Granite Guardian, Llama Guard 3, and NeMo Self-Check Fact-Checking) reduce ASR by at most 5.7% relative, while Granite Guardian’s reduction is not statistically significant."
- "To this end, a lightweight benchmark baseline, C-GEO Guard 2 2 2 https://huggingface.co/counter-geo/c-geo-guard , is proposed, reducing ASR by 47.6% relative with near-zero utility loss, which proves threat tractable. 1 Introduction As large language models (LLMs) increasingly serve as primary information sources, organized misinformation campaigns have adapted their tactics."
- "We propose C-GEO Guard, a chunk-level contrastive detector that reduces ASR by 47.6% relative (26.5 pp absolute) with near-zero utility loss."
- "On the full 247 queries rewritten by GPT 5.5, the same guard achieves a 60.4% relative reduction, exceeding the 48% on the Sonnet evaluation set."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2609.02316`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

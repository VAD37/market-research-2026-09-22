# Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers

```yaml
source:          Yixuan Du, Chenxiao Yu, Haoyan Xu, Ziyi Wang, Yue Zhao, Xiyang Hu
url_or_doc_id:   arXiv:2601.12263 ; https://arxiv.org/abs/2601.12263
published:       2026-01-18 (arXiv v1; latest listed 2026-06-07)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed workshop proceedings (KnowFM at ACL 2026, per arXiv comment) with code published
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Qwen2.5-VL-7B (target ranker); GPT-4o, GPT-4o-mini (baselines)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    KnowFM Workshop at ACL 2026
code_availability: https://github.com/glad-lab/MGEO
capability_class: joint image perturbation and text suffix manipulate a vision-language model's product ranking
```

## Verbatim — abstract

"Vision-Language Models (VLMs) integrate visual and textual knowledge into unified representations that increasingly underpin modern retrieval and recommendation systems. However, it remains unclear how reliably these models utilize their cross-modal knowledge when ranking multimodal items, and whether their knowledge grounding can be subverted. In this paper, we expose a fundamental vulnerability in how VLMs apply multimodal knowledge for product ranking: through Multimodal Generative Engine Optimization (MGEO), we show that an adversary can manipulate a VLM's ranking decisions by jointly crafting imperceptible image perturbations and fluent textual suffixes that exploit the model's internal cross-modal knowledge coupling. Using an alternating optimization strategy, MGEO targets the deep interactions between visual and linguistic representations within the VLM, achieving rank manipulations that substantially exceed those of unimodal attacks and heuristic baselines powered by strong commercial models. Our findings reveal that surface-level content quality is insufficient for rank promotion; instead, direct alignment with the model's internal knowledge utilization mechanism is required. These results raise important questions on the faithfulness and robustness of knowledge grounding in multimodal foundation models, and motivate future work on defense mechanisms for multimodal retrieval systems. Code is available at: https://github.com/glad-lab/MGEO"

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2601.12263`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

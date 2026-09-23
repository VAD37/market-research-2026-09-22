# MaxShapley: Towards Incentive-compatible Generative Search with Fair Context Attribution

```yaml
source:          Sara Patel, Mingxun Zhou, Giulia Fanti
url_or_doc_id:   arXiv:2512.05958 ; https://arxiv.org/abs/2512.05958
published:       2025-12-05 (arXiv v1; latest listed 2026-05-19)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     preprint with open-source code and re-calibrated datasets; venue unconfirmed but code+data+demo public; academic table 'preprint with code' = 4, kept conservative at 4
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          GPT-4.1 nano, Claude Haiku 3.5/4.5, Claude Sonnet 4, Llama 3.3-70B
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     4
venue_status:    arXiv preprint
code_availability: https://github.com/spaddle-boat/MaxShapley
capability_class: polynomial-time Shapley-value attribution of content-provider contribution to a generated answer (compensation mechanism)
```

## Verbatim — abstract

"Generative search engines based on large language models (LLMs) are replacing traditional search, fundamentally changing how information providers are compensated. To sustain this ecosystem, we need fair mechanisms to attribute and compensate content providers based on their contributions to generated answers. We introduce MaxShapley, an efficient algorithm for fair credit attribution in generative search pipelines that retrieve external sources before generation. MaxShapley is a special case of the celebrated Shapley value; it leverages a de-composable max-sum utility function to compute attributions with polynomial-time computation in the number of documents, as opposed to the exponential cost of Shapley values. We evaluate MaxShapley on three multi-hop QA datasets (HotPotQA, MuSiQUE, MS MARCO); MaxShapley achieves comparable attribution quality to exact Shapley computation, while consuming a fraction of its tokens--for instance, it gives up to a 9x reduction in resource consumption over prior state-of-the-art methods at the same attribution accuracy. We release open-source code and re-calibrated datasets. An educational demo is available at https://fair-search.com."

## Verbatim — result sentences (from arXiv HTML full text)

- "It achieves strong correlation with brute-force Shapley values computed from an aggregate LLM-as-a-judge utility function (Kendall- τ > 0.5 tau>0.5 ) and strong alignment with human annotations (Jaccard index > 0.85 >0.85 ), using less than 6 % 6% of the token cost (Figure 3 )."
- "Compared to KernelSHAP, our strongest Shapley approximation baseline, MaxShapley reaches the same alignment with human annotations (Jaccard) at less than 7 % 7% the cost (Figure 1 , Figure 3 )."
- "MS-MARCO shows 25% are in perfect agreement."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2512.05958`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

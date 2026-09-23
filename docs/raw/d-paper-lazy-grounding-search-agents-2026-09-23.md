# Lazy Grounding: Attacking Search Agents with Factual Evidence

```yaml
source:          Yulin Zhang, Yukun Huang, Sanxing Chen, Tianyi Lin, Ziang Yang, Xunjian Yin et al.
url_or_doc_id:   arXiv:2608.30303 ; https://arxiv.org/abs/2608.30303
published:       2026-08-31 (arXiv v1; latest listed 2026-09-01)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (EMNLP 2026 Main, per arXiv comment) with code published
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          GPT-5, GPT-5 Mini, GPT-5.4, Gemini 3 Flash, Tongyi Deep Research
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    EMNLP 2026 Main
code_availability: https://github.com/frankyzha/lazy-grounding
capability_class: factual-but-off-target evidence in a search corpus shifts a search-agent's answer
```

## Verbatim — abstract

"Search agents mitigate hallucination by grounding their answers in retrieved web results. However, retrieval-based approaches also introduce an attack surface: agents may cite misinformation from poisoned search corpora containing false or malicious documents. We demonstrate that, in some cases, search agents' reasoning and responses may be steered by completely factual but distracting information. We refer to this failure as lazy grounding. We expose lazy grounding by injecting nearby evidence from answer-changing rewrites of benchmark questions into the search corpora. Each document contains factual evidence that supports a neighboring rewritten question but is retrieved for the original question. Across 12 model-benchmark pairs, the attack causes the accuracy of search agents' responses to drop by 5.9 points on average and by up to 17.3 points, while inducing nearby-answer adoption in every setting. The effect is even stronger when nearby evidence appears later or is more answer-shaped. Our results show that robust search agents must defend against not only misinformation but also the misapplication of factual evidence. The code is publicly available at https://github.com/frankyzha/lazy-grounding."

## Verbatim — result sentences (from arXiv HTML full text)

- "We find that this simple nearby-evidence stress test can cause agents to adopt the neighboring answer at high rates, e.g., 27.0% for Tongyi Deep Research and 23.0% for GPT-5 Mini on XBench , while reducing accuracy from 69.3 to 52.0 and from 65.0 to 52.7, respectively."
- "The largest drop is 17.3 points for Tongyi Deep Research on XBench , from 69.3 to 52.0 (95% CI [10.7, 24.0])."
- "The remaining 14.3% RAA shows that prompting alone does not eliminate lazy grounding."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2608.30303`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

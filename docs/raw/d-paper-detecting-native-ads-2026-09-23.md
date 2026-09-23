# Detecting Generated Native Ads in Conversational Search

```yaml
source:          Sebastian Schmidt, Ines Zelch, Janek Bevendorff, Benno Stein, Matthias Hagen, Martin Potthast
url_or_doc_id:   arXiv:2402.04889 ; https://arxiv.org/abs/2402.04889
published:       2024-02-07 (arXiv v1; latest listed 2024-04-30)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (WWW 2024 Short Papers) with public dataset (Zenodo) and code (github.com/webis-de/WWW-24)
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          GPT-4, Mistral-7B-Instruct; sentence transformers
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     6
venue_status:    WWW 2024 (Short Papers)
code_availability: https://github.com/webis-de/WWW-24 ; Zenodo 10.5281/zenodo.10802427
capability_class: detector for LLM-generated native ads inserted in conversational answers (fine-tuned transformer >0.9 precision/recall)
```

## Verbatim — abstract

"Conversational search engines such as YouChat and Microsoft Copilot use large language models (LLMs) to generate responses to queries. It is only a small step to also let the same technology insert ads within the generated responses - instead of separately placing ads next to a response. Inserted ads would be reminiscent of native advertising and product placement, both of which are very effective forms of subtle and manipulative advertising. Considering the high computational costs associated with LLMs, for which providers need to develop sustainable business models, users of conversational search engines may very well be confronted with generated native ads in the near future. In this paper, we thus take a first step to investigate whether LLMs can also be used as a countermeasure, i.e., to block generated native ads. We compile the Webis Generated Native Ads 2024 dataset of queries and generated responses with automatically inserted ads, and evaluate whether LLMs or fine-tuned sentence transformers can detect the ads. In our experiments, the investigated LLMs struggle with the task but sentence transformers achieve precision and recall values above 0.9."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2402.04889`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

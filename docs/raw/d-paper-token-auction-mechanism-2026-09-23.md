# Mechanism Design for Large Language Models

```yaml
source:          Paul Duetting, Vahab Mirrokni, Renato Paes Leme, Haifeng Xu, Song Zuo
url_or_doc_id:   arXiv:2310.10826 ; https://arxiv.org/abs/2310.10826
published:       2023-10-16 (arXiv v1; latest listed 2024-07-02)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     peer-reviewed (WWW 2024 Best Paper per arXiv comment); no code link found, placed at 4 as for 2406.09459. Pre-window: first posted 2023-10-16
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          'a publicly available LLM' (not named in captured text)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    WWW 2024 (Best Paper)
code_availability: none found
capability_class: token-by-token second-price auction letting advertiser LLMs bid on generated content
```

## Verbatim — abstract

"We investigate auction mechanisms for AI-generated content, focusing on applications like ad creative generation. In our model, agents' preferences over stochastically generated content are encoded as large language models (LLMs). We propose an auction format that operates on a token-by-token basis, and allows LLM agents to influence content creation through single dimensional bids. We formulate two desirable incentive properties and prove their equivalence to a monotonicity condition on output aggregation. This equivalence enables a second-price rule design, even absent explicit agent valuation functions. Our design is supported by demonstrations on a publicly available LLM."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2310.10826`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

# Truthful Aggregation of LLMs with an Application to Online Advertising

```yaml
source:          Ermis Soumalias, Michael J. Curry, Sven Seuken
url_or_doc_id:   arXiv:2405.05905 ; https://arxiv.org/abs/2405.05905
published:       2024-05-09 (arXiv v1; latest listed 2025-02-12)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; code stated as 'will be made available', no link found; academic table 'preprint without code'
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          Llama-2-7b-chat-hf
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    arXiv preprint
code_availability: none found
capability_class: truthful auction aggregating advertiser preferences into LLM answers without fine-tuning
```

## Verbatim — abstract

"The next frontier of online advertising is revenue generation from LLM-generated content. We consider a setting where advertisers aim to influence the responses of an LLM to align with their interests, while platforms seek to maximize advertiser value and ensure user satisfaction. The challenge is that advertisers' preferences generally conflict with those of the user, and advertisers may misreport their preferences. To address this, we introduce MOSAIC, an auction mechanism that ensures that truthful reporting is a dominant strategy for advertisers and that aligns the utility of each advertiser with their contribution to social welfare. Importantly, the mechanism operates without LLM fine-tuning or access to model weights and provably converges to the output of the optimally fine-tuned LLM as computational resources increase. Additionally, it can incorporate contextual information about advertisers, which significantly improves social welfare. Through experiments with a publicly available LLM, we show that MOSAIC leads to high advertiser value and platform revenue with low computational overhead. While our motivating application is online advertising, our mechanism can be applied in any setting with monetary transfers, making it a general-purpose solution for truthfully aggregating the preferences of self-interested agents over LLM-generated replies."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2405.05905`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

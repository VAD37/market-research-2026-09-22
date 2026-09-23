# Sponsored Questions and How to Auction Them

```yaml
source:          Kshipra Bhawalkar, Alexandros Psomas, Di Wang
url_or_doc_id:   arXiv:2512.03975 ; https://arxiv.org/abs/2512.03975
published:       2025-12-03 (arXiv v1; latest listed 2025-12-03)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint, theoretical, no code; academic table 'preprint without code'
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          none (theoretical model)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    arXiv preprint
code_availability: none (theory paper)
capability_class: auction for sponsored clarifying follow-up prompts, and its interaction with a subsequent ad auction
```

## Verbatim — abstract

"Online platforms connect users with relevant products and services using ads. A key challenge is that a user's search query often leaves their true intent ambiguous. Typically, platforms passively predict relevance based on available signals and in some cases offer query refinements. The shift from traditional search to conversational AI provides a new approach. When a user's query is ambiguous, a Large Language Model (LLM) can proactively offer several clarifying follow-up prompts. In this paper we consider the following: what if some of these follow-up prompts can be ``sponsored,'' i.e., selected for their advertising potential. How should these ``suggestion slots'' be allocated? And, how does this new mechanism interact with the traditional ad auction that might follow? This paper introduces a formal model for designing and analyzing these interactive platforms. We use this model to investigate a critical engineering choice: whether it is better to build an end-to-end pipeline that jointly optimizes the user interaction and the final ad auction, or to decouple them into separate mechanisms for the suggestion slots and another for the subsequent ad slot. We show that the VCG mechanism can be adopted to jointly optimize the sponsored suggestion and the ads that follow; while this mechanism is more complex, it achieves outcomes that are efficient and truthful. On the other hand, we prove that the simple-to-implement modular approach suffers from strategic inefficiency: its Price of Anarchy is unbounded."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2512.03975`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

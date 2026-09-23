# LLM-OSDA: An Optimal-Stopping Dynamic Auction for Native Advertising in Multi-Turn LLM Conversations

```yaml
source:          Yan Fang, Jialin Chen, Chun Gan, Hang Yu, Mingjun Nie, Yeyu Zhang et al.
url_or_doc_id:   arXiv:2608.00123 ; https://arxiv.org/abs/2608.00123
published:       2026-07-31 (arXiv v1; latest listed 2026-08-04)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint (submitted AAAI 2027) with code published
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          Qwen3-4B, Qwen3-Embedding
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    arXiv preprint; submitted AAAI 2027
code_availability: https://github.com/2025Fang2025/llm-osda
capability_class: optimal-stopping auction choosing WHEN in a multi-turn conversation to place one native ad
```

## Verbatim — abstract

"LLM-native advertising embeds sponsored content directly into model-generated responses, shifting the unit of sale from a fixed slot to a moment within an evolving conversation. Existing LLM ad-auction mechanisms primarily operate within a single response, settling the winner but not the timing. The extension is nontrivial: with one native insertion opportunity per session, the stopping time depends on bids, coupling timing with allocation, so static truthfulness arguments no longer apply. We propose the LLM-based Optimal Stopping Dynamic Auction (LLM-OSDA), a dynamic cost-per-click auction that integrates Bellman optimal stopping, winner allocation, and envelope pricing. A bid-independent LLM layer estimates contextual click quality and seamlessly renders the winning ad, while bids enter only the committed auction mechanism. Under an exact Bellman oracle, the expected discounted-click allocation is monotone in each advertiser's bid, and the corresponding envelope payment makes truthful bidding weakly dominant in expectation. For practical deployment, a learned StopNet approximates the Bellman action values. We show that its decisions differ from the optimal policy only near the stopping boundary and bound the resulting incentive loss in terms of its approximation error. Experiments on a simulated conversational advertising corpus show that LLM-OSDA improves net revenue by 11 percent over the strongest fixed-timing baseline while maintaining comparable user retention. Code is at https://github.com/2025Fang2025/llm-osda."

## Verbatim — result sentences (from arXiv HTML full text)

- "Experiments on a simulated conversational advertising corpus show that LLM-OSDA improves net revenue by 11% over the strongest fixed-timing baseline while maintaining comparable user retention."
- "Iterative refinement lifts revenue by 14 to 19% across every timing policy (Figure 3 )."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2608.00123`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

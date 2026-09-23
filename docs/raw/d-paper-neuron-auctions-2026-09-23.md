# LLM Advertisement based on Neuron Auctions

```yaml
source:          Peiran Yun, Wenxin Xu, Jiayuan Liu, Yihang Zhang, Liang Zeng, Lingkai Kong et al.
url_or_doc_id:   arXiv:2605.08326 ; https://arxiv.org/abs/2605.08326
published:       2026-05-08 (arXiv v1; latest listed 2026-05-08)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint, no code link found; academic table 'preprint without code'
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          Llama-3-8B, Qwen3-4B, DeepSeek-R1-8B
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    arXiv preprint
code_availability: none found
capability_class: auction over brand-specific neuron amplification inside the model's representations
```

## Verbatim — abstract

"As Large Language Models (LLMs) transition into conversational agents, generative advertising emerges as a crucial monetization strategy. However, embedding advertisements within unstructured LLM outputs introduces a critical trilemma: balancing advertiser payoffs, platform revenue, and user experience. Existing methods, such as prompt injection or rigid position slots, disrupt semantic coherence and lack a parametric framework for independent control, rendering rigorous mechanism design intractable. To bridge this gap, we introduce Neuron Auctions, a novel paradigm that shifts the auction object from the surface text space to the LLM's internal representations. Leveraging mechanistic interpretability, we identify brand-specific feed-forward network (FFN) neurons and demonstrate that competing brands activate within approximately orthogonal subspaces. This near-perfect independence allows us to define continuous, disentangled intervention budgets (specifically, neuron counts and amplification factors) as auctionable commodities. Building on this computational carrier, we design a continuous menu-based auction mechanism that naturally guarantees strategy-proofness and optimizes revenue for the platform. By explicitly incorporating a user utility penalty into the platform's optimization objective, our framework dynamically prices out overly aggressive interventions. Extensive experiments demonstrate that Neuron Auctions effectively preserve natural discourse quality while achieving an optimal alignment between commercial incentives and user satisfaction."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2605.08326`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

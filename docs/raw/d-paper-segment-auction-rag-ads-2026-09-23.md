# Ad Auctions for LLMs via Retrieval Augmented Generation

```yaml
source:          MohammadTaghi Hajiaghayi, Sébastien Lahaie, Keivan Rezaei, Suho Shin
url_or_doc_id:   arXiv:2406.09459 ; https://arxiv.org/abs/2406.09459
published:       2024-06-12 (arXiv v1; latest listed 2025-06-12)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     peer-reviewed (NeurIPS 2024) but no code link found in full text; rubric academic table has no peer-reviewed-without-code row, placed at 4 between rows 3 and 5
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          gpt-4-turbo; multi-qa-MiniLM-L6 embeddings
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    NeurIPS 2024
code_availability: none found (checklist states code will be released)
capability_class: per-segment ad auction inside RAG-generated LLM output; incentive-compatible pricing
```

## Verbatim — abstract

"In the field of computational advertising, the integration of ads into the outputs of large language models (LLMs) presents an opportunity to support these services without compromising content integrity. This paper introduces novel auction mechanisms for ad allocation and pricing within the textual outputs of LLMs, leveraging retrieval-augmented generation (RAG). We propose a segment auction where an ad is probabilistically retrieved for each discourse segment (paragraph, section, or entire output) according to its bid and relevance, following the RAG framework, and priced according to competing bids. We show that our auction maximizes logarithmic social welfare, a new notion of welfare that balances allocation efficiency and fairness, and we characterize the associated incentive-compatible pricing rule. These results are extended to multi-ad allocation per segment. An empirical evaluation validates the feasibility and effectiveness of our approach over several ad auction scenarios, and exhibits inherent tradeoffs in metrics as we allow the LLM more flexibility to allocate ads."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2406.09459`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

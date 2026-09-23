# Ad Insertion in LLM-Generated Responses

```yaml
source:          Shengwei Xu, Zhaohua Chen, Xiaotie Deng, Zhiyi Huang, Grant Schoenebeck
url_or_doc_id:   arXiv:2601.19435 ; https://arxiv.org/abs/2601.19435
published:       2026-01-27 (arXiv v1; latest listed 2026-08-25)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with code and survey materials (anonymous.4open.science repository)
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          GPT-5 (judge), GPT-4o, GPT-4o-mini, DeepSeek-V3, Qwen3-8B, Claude 4.5
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    arXiv preprint
code_availability: https://anonymous.4open.science/r/Ad-Insertion-in-LLM-Generated-Responses-523F/
capability_class: disclosed ad insertion decoupled from generation; genre-level VCG bidding; user acceptability survey
```

## Verbatim — abstract

"Sustainable monetization of large language models (LLMs) remains a critical open challenge. Traditional search advertising, which relies on static keywords, fails to capture the fleeting, context-dependent user intent---the specific information, goods, or services a user seeks---embedded in conversational flows. Beyond the standard goal of social welfare maximization effective LLM advertising requires contextual coherence (aligning ads semantically with transient user intent), computational efficiency (avoiding user-facing latency), and adherence to ethical and regulatory standards, including privacy preservation and explicit ad disclosure. Although recent solutions have explored bidding at the token and query levels, neither category holistically satisfies these constraints. We propose a framework that resolves these tensions through two decoupling strategies. First, we decouple ad insertion from response generation to facilitate pre-screening and explicit disclosure. Second, we decouple bidding from specific user queries by using ``genres'' (high-level semantic clusters) as a proxy. This allows advertisers to bid on stable categories rather than sensitive real-time responses, reducing computational burden and privacy risks. Applying the VCG auction mechanism to this genre-based framework provides approximate guarantees for dominant-strategy incentive compatibility (DSIC), individual rationality (IR), and social welfare. In synthetic experiments with $10^5$ advertisers and 100 candidate slots, VCG clears in approximately 1.25 seconds on a consumer-grade laptop. Finally, we introduce an ``LLM-as-a-Judge'' metric for estimating contextual coherence. Its predictions correlate with mean human ratings at Spearman's $ρ\approx 0.66$ and have a higher correlation with the leave-one-out group mean than 29 of 36 individual raters (80.6\%)."

## Verbatim — result sentences (from arXiv HTML full text)

- "A majority (56.3%) expected ads to appear in LLM responses within a year, whereas only 12.5% thought this would not happen."
- "Despite this expectation, the acceptability of such ads remained low: only 4.2% rated them as acceptable, whereas 64.6% rated them as unacceptable."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2601.19435`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

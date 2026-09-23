# The Injection Paradox: Brand-Level Suppression in Safety-Trained LLM Recommendations via RAG Context Injection

```yaml
source:          Hyunseok Paeng
url_or_doc_id:   arXiv:2606.09204 ; https://arxiv.org/abs/2606.09204
published:       2026-06-08 (arXiv v1; latest listed 2026-07-11)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     non-archival workshop (ICML 2026 FAGEN) treated as preprint; code, prompts and per-trial records released per abstract; academic table 'preprint with code'
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Claude Opus 4.6, Claude Sonnet, Claude Haiku; GPT-4o-mini and other GPT models
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    ICML 2026 Workshop FAGEN (non-archival)
code_availability: released per abstract (code, prompts, per-trial records); URL not captured this pull
capability_class: an injected retrieved document suppresses a brand in safety-trained models yet promotes it in others (model-family split)
```

## Verbatim — abstract

"We present a reproducible failure mode of safety training in RAG-based LLM recommendation, the Injection Paradox, in which prompt injections embedded in retrieved documents backfire against the attacker, suppressing the target brand below the injection-free baseline. In safety-trained Claude models, documents containing prompt injections suffer a sharp drop in recommendation rate, and this suppression propagates beyond the injected document to unmodified documents of the same brand. In Claude Opus 4.6, the target brand drops from a 54% baseline to zero top-2 recommendations across all 50 trials, even though only 1 of 4 brand documents in the corpus contains an injection. The directional pattern is reproduced in counterfactual experiments and across three brands. A contrasting result across the GPT models tested, where the same injection instead increases recommendations, suggests model-family differences in how injection-like context affects recommendation behavior. These findings raise the technical possibility of a reverse-attack scenario in which an adversary embeds injections in a competitor's documents to suppress the competitor's brand via safety-sensitive model behavior. Code, prompts, privacy-preserving per-trial outcome records, and aggregate results are released."

## Verbatim — result sentences (from arXiv HTML full text)

- "In Claude Opus 4.6, the target brand drops from a 54% baseline to zero top-2 recommendations across all 50 trials, even though only 1 of 4 brand documents in the corpus contains an injection."
- "Counterfactual experiments confirm that the presence of injection (0%) yields worse outcomes than the absence of the injected document (28%). 3."
- "In GPT-4o-mini, injection exhibits a promotion effect (17% → to 40%, + 23 +23 pp, p < .001 p{<}.001 )."
- "In contrast, the same injection drives the hit rate sharply below baseline in Claude Sonnet and Opus (Sonnet: 26% → to 8%, − 18 -18 pp, p = .031 p{=}.031 ; Opus: 54% → to 8%, − 46 -46 pp, p < .001 p{<}.001 )."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2606.09204`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

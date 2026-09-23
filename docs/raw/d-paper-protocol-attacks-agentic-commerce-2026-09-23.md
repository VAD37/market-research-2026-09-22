# Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense

```yaml
source:          Yedidel Louck
url_or_doc_id:   arXiv:2607.21824 ; https://arxiv.org/abs/2607.21824
published:       2026-07-23 (arXiv v1; latest listed 2026-07-23)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; benchmark AIP-Bench public (github.com/yedidel/aip-bench-public) but SoK-style; single author, no venue; kept at 5
source_label:    analyst-derived
lane:            D
sub_market:      agentic commerce
engine:          model-independent structural findings; semantic tests across GPT-4o, Gemini, Claude, Llama, Mistral
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     3
venue_status:    arXiv preprint
code_availability: https://github.com/yedidel/aip-bench-public
capability_class: protocol-layer (not model-layer) vulnerabilities in agentic-commerce platforms; deterministic, model-independent
```

## Verbatim — abstract

"Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users' behalf, and they already handle real money. Their security has so far been studied almost entirely at the level of the AI model, through prompt injection and misalignment. We show that the more consequential risks lie one layer down, in the protocol between agents and commerce services. There, vulnerabilities are structural : exploitation is deterministic and ndependent of which model an agent runs, so no model improvement removes them. Across three leading platforms we identify 33 such vulnerabilities, each succeeding deterministically regardless of the deployed model, at a 100% attack-success rate (ASR) wherever live-measured. The same failure modes recur across independently built codebases, a systemic pattern rather than isolated bugs. Three of them chain into an end-to-end payment hijack. We contribute a taxonomy separating these structural attacks from model-dependent semantic ones. We also build two artifacts: AIP-Bench (Agent Interaction Protocol Benchmark), to our knowledge the first deterministic benchmark for agentic commerce security, and PCAT (Protocol-level Commerce Agent Trust), a platform-agnostic defense that drives the structural attack-success rate to zero for four of the five structural classes (RC-1, RC-2, RC-4, RC-5), with RC-3 (observable credential channels) reduced to warn-only, without modifying any platform. Agentic commerce must be secured at the protocol layer, not only the model."

## Verbatim — result sentences (from arXiv HTML full text)

- "Across three leading platforms we identify 33 such vulnerabilities, each succeeding deterministically regardless of the deployed model, at a 100% attack-success rate (ASR) wherever live-measured."
- "Agentic commerce platforms introduce a distinct and previously unstudied attack class: structural attacks , which are protocol-level vulnerabilities that succeed with a 100% ASR regardless of which AI model is deployed."
- "The one semantically-mediated attack class (V5 marketplace IPI) has a structural delivery component (100% ASR , model-independent) and a semantic behavioral impact component (model-dependent)."
- "The cheap commercial models (GPT-4o-mini, Gemini Flash, Mistral) achieve 99–100% impact ASR , GPT-4o achieves 68%, and alignment-trained models (Claude 3-Haiku, Sonnet, Gemini Pro) achieve 0%, with the non-aligned Llama-3.3-70B at 10%."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2607.21824`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

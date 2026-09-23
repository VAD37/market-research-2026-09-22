# Defeating Prompt Injections by Design

```yaml
source:          Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes, Nicholas Carlini, Daniel Fabian et al.
url_or_doc_id:   arXiv:2503.18813 ; https://arxiv.org/abs/2503.18813
published:       2025-03-24 (arXiv v1; latest listed 2025-06-24)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with released code (github.com/google-research/camel-prompt-injection); Google-authored defense
source_label:    analyst-derived
lane:            D
sub_market:      cross
engine:          GPT-4o, GPT-4o-mini, o1/o3, Claude 3.5/4, Gemini 2.5 (as P-LLM/Q-LLM)
metric_kind:     none
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     6
venue_status:    arXiv preprint
code_availability: https://github.com/google-research/camel-prompt-injection
capability_class: system-layer control/data-flow separation defending prompt injection independent of the underlying model
bias_flag:       Google Research / DeepMind authors
```

## Verbatim — abstract

"Large Language Models (LLMs) are increasingly deployed in agentic systems that interact with an untrusted environment. However, LLM agents are vulnerable to prompt injection attacks when handling untrusted data. In this paper we propose CaMeL, a robust defense that creates a protective system layer around the LLM, securing it even when underlying models are susceptible to attacks. To operate, CaMeL explicitly extracts the control and data flows from the (trusted) query; therefore, the untrusted data retrieved by the LLM can never impact the program flow. To further improve security, CaMeL uses a notion of a capability to prevent the exfiltration of private data over unauthorized data flows by enforcing security policies when tools are called. We demonstrate effectiveness of CaMeL by solving $77\%$ of tasks with provable security (compared to $84\%$ with an undefended system) in AgentDojo. We release CaMeL at https://github.com/google-research/camel-prompt-injection."

## Verbatim — result sentences (from arXiv HTML full text)

- "We demonstrate effectiveness of CaMeL by solving 77 % 77% of tasks with provable security (compared to 84 % 84% with an undefended system) in AgentDojo."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2503.18813`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

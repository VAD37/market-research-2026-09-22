# Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via Prompt Injection

```yaml
source:          Tanusree Debi, Wentian Zhu, Pranjol Sen Gupta
url_or_doc_id:   arXiv:2601.22569 ; https://arxiv.org/abs/2601.22569
published:       2026-01-30 (arXiv v1; latest listed 2026-05-18)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     peer-reviewed venue named (IMNS 2026) but pull captured no code link; conservatively placed at 5 (preprint without confirmed code)
source_label:    analyst-derived
lane:            D
sub_market:      agentic commerce
engine:          Gemini-2.5-Flash (via Google ADK)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     3
venue_status:    IMNS 2026 (per journal_ref)
code_availability: none captured (builds on public github.com/google-agentic-commerce/AP2)
capability_class: indirect prompt injection against an AP2 shopping agent manipulates product ranking; runs on the public AP2 reference stack
```

## Verbatim — abstract

"Large language model (LLM) based agents are increasingly used to automate financial transactions, yet their reliance on contextual reasoning exposes payment systems to prompt-driven manipulation. The Agent Payments Protocol (AP2) aims to secure agent-led purchases through cryptographically verifiable mandates, but its practical robustness remains underexplored. In this work, we perform an AI red-teaming evaluation of AP2 and identify vulnerabilities arising from indirect and direct prompt injection. We introduce two attack techniques, the Branded Whisper Attack and the Vault Whisper Attack which manipulate product ranking and extract sensitive user data. Using a functional AP2 based shopping agent built with Gemini-2.5-Flash and the Google ADK framework, we experimentally validate that simple adversarial prompts can reliably subvert agent behavior. Our findings reveal critical weaknesses in current agentic payment architectures and highlight the need for stronger isolation and defensive safeguards in LLM-mediated financial systems."

## Verbatim — result sentences (from arXiv HTML full text)

- "Using a functional AP2-based shopping agent implemented with Gemini-2.5-Flash and the Google Agent Development Kit (ADK), we show that indirect prompt injection achieves a 100% success rate in manipulating product ranking, while direct prompt injection leads to cross-account data exposure in 20% of cases."
- "We measure attack effectiveness using Attack Success Rate (ASR), defined as the fraction of trials in which the injected product is ranked first."
- "Under attack conditions (Figure 6 ), the injected product is ranked first in all 10 trials, yielding an ASR of 100%."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2601.22569`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

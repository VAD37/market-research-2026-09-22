# Meta SecAlign: A Secure Foundation LLM Against Prompt Injection Attacks

```yaml
source:          Sizhe Chen, Arman Zharmagambetov, David Wagner, Chuan Guo
url_or_doc_id:   arXiv:2507.02735 ; https://arxiv.org/abs/2507.02735
published:       2025-07-03 (arXiv v1; latest listed 2026-02-06)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with fully open-source model and training recipe (github.com/facebookresearch/Meta_SecAlign; HF weights); academic table 'preprint with code'
source_label:    analyst-derived
lane:            D
sub_market:      cross
engine:          Meta-SecAlign-70B / -8B (Llama-3 based)
metric_kind:     none
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     6
venue_status:    arXiv preprint
code_availability: https://github.com/facebookresearch/Meta_SecAlign ; https://huggingface.co/facebook/Meta-SecAlign-70B
capability_class: open-source model-level prompt-injection defense at commercial-grade utility
```

## Verbatim — abstract

"Prompt injection attacks, where untrusted data contains an injected prompt to manipulate the system, have been listed as the top security threat to LLM-integrated applications. Model-level prompt injection defenses have shown strong effectiveness, but the strongest defenses are proprietary. Open-source secure models are needed by the AI security community so that co-development of attacks and defenses through open research can drive scientific progress in mitigating prompt injection attacks. To this end, we develop Meta SecAlign, the first fully open-source LLM with built-in model-level defense that achieves commercial-grade performance and is powerful enough for complex agentic tasks. We provide complete details of our training recipe. We perform the most comprehensive evaluation to date on 9 utility benchmarks (measuring general knowledge, instruction following, and agentic workflows) and 7 security benchmarks. Results show that Meta SecAlign, despite being trained only on generic instruction-tuning samples, surprisingly confers security in unseen downstream tasks, including tool-calling and web-navigation, in addition to general instruction-following. Our best model -- Meta-SecAlign-70B -- establishes a new frontier of utility-security trade-off for open-source LLMs, and is more secure than several flagship proprietary models with prompt injection defense. Below are links for the code (https://github.com/facebookresearch/Meta_SecAlign), Meta-SecAlign-70B (https://huggingface.co/facebook/Meta-SecAlign-70B), and Meta-SecAlign-8B (https://huggingface.co/facebook/Meta-SecAlign-8B) models."

## Verbatim — result sentences (from arXiv HTML full text)

- "Specifically, Meta-SecAlign - 70B has a 6.4% attack success rate (ASR) on SEP [ 73 ] instruction following PIs, 1.9% ASR on AgentDojo [ 15 ] tool-calling PIs, and lower ASRs on other 5 PI benchmarks, e.g., 0% ASR on WASP [ 19 ] PIs in web navigation."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2507.02735`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

# The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against Llm Jailbreaks and Prompt Injections

```yaml
source:          Milad Nasr, Nicholas Carlini, Chawin Sitawarin, Sander V. Schulhoff, Jamie Hayes, Michael Ilie et al.
url_or_doc_id:   arXiv:2510.09023 ; https://arxiv.org/abs/2510.09023
published:       2025-10-10 (arXiv v1; latest listed 2025-10-10)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with released attack code (github.com/haizelabs/dspy-redteam); Anthropic/Google DeepMind/academic authors; academic table 'preprint with code'
source_label:    analyst-derived
lane:            D
sub_market:      cross
engine:          defenses evaluated on GPT-5, Gemini-2.5 Pro/Flash, Llama-3.3, Grok 4 and others
metric_kind:     none
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     6
venue_status:    arXiv preprint
code_availability: https://github.com/haizelabs/dspy-redteam
capability_class: adaptive attackers bypass 12 recent prompt-injection/jailbreak defenses that had reported near-zero rates
bias_flag:       co-authored across Anthropic and Google DeepMind
```

## Verbatim — abstract

"How should we evaluate the robustness of language model defenses? Current defenses against jailbreaks and prompt injections (which aim to prevent an attacker from eliciting harmful knowledge or remotely triggering malicious actions, respectively) are typically evaluated either against a static set of harmful attack strings, or against computationally weak optimization methods that were not designed with the defense in mind. We argue that this evaluation process is flawed. Instead, we should evaluate defenses against adaptive attackers who explicitly modify their attack strategy to counter a defense's design while spending considerable resources to optimize their objective. By systematically tuning and scaling general optimization techniques-gradient descent, reinforcement learning, random search, and human-guided exploration-we bypass 12 recent defenses (based on a diverse set of techniques) with attack success rate above 90% for most; importantly, the majority of defenses originally reported near-zero attack success rates. We believe that future defense work must consider stronger attacks, such as the ones we describe, in order to make reliable and convincing claims of robustness."

## Verbatim — result sentences (from arXiv HTML full text)

- "By systematically tuning and scaling general optimization techniques—gradient descent, reinforcement learning, random search, and human-guided exploration—we bypass 12 recent defenses (based on a diverse set of techniques) with attack success rate above 90% for most; importantly, the majority of defenses originally reported near-zero attack success rates."
- "Across most defenses, we achieve an attack success rate above 90% in most cases, compared to the near-zero success rates reported in the original papers. 2 A Brief History of Adversarial ML Evaluations In computer security and cryptography, a defense is deemed to be robust if the strongest human attackers (with large compute budgets) are unable to reliably construct attacks that evade the protection measures."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2510.09023`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

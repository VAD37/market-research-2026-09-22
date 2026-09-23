# A Finger on the Scale: Covert Policy Steering through Agentic Skills

```yaml
source:          Jiarui Li, Jiahao Chen, Chunyi Zhou, Yuwen Pu, Oubo Ma, Zhou Feng et al.
url_or_doc_id:   arXiv:2609.02564 ; https://arxiv.org/abs/2609.02564
published:       2026-09-02 (arXiv v1; latest listed 2026-09-02)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; no author code repository found in full text (only third-party scanner links); academic table 'preprint without code'
source_label:    analyst-derived
lane:            D
sub_market:      agentic commerce
engine:          GPT-5.4, GPT-5.5, Gemini 3-Flash, Claude Haiku 4.5, Qwen3.5-Flash, GLM-4.7, DeepSeek
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     3
venue_status:    arXiv preprint
code_availability: none found
capability_class: a reusable third-party agent skill covertly biases an agent's product selection while preserving valid output
```

## Verbatim — abstract

"Reusable agent skills extend large language model (LLM) agents with task procedures, tool-use guidance, and output constraints. Yet these skills also act as externalized behavioral policies, which create a supply-chain risk: a third-party skill may preserve the declared task and valid output interface while covertly redirecting agent decisions toward an undisclosed objective. We formalize Skill Policy Integrity, which requires a Skill-induced policy to remain aligned with its declared functionality and the user-authorized objective. We further present SkillShift, a constrained black-box framework for covert policy steering without explicit target command injection or task hijacking. It combines semantically plausible policy edits with hierarchical validation, failure-guided optimization, and strategy compression to preserve effectiveness, output validity, transferability, and inconspicuousness. We instantiate this threat in agentic commerce and software dependency use, with SkillShift achieving attacker-favored selection rates of 81.33% and 63.33% while maintaining a 100% utility-preserving rate. The frozen policies also transfer without further optimization across heterogeneous LLM backends and agent environments. Moreover, the evaluated scanners fail to detect the constructed skills, motivating behavioral auditing of reusable skills as agent policy artifacts."

## Verbatim — result sentences (from arXiv HTML full text)

- "Across agentic commerce and coding dependency selection, SkillShift achieves policy steering rates (PSR) of 81% and 63%, improving over clean Skills by +44% and +63% while maintaining a 100% valid-output rate."
- "In Shopping, SkillShift increases PSR from 37.33% to 81.33% while maintaining 100.00% VR."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2609.02564`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

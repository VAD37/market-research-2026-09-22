# From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning

```yaml
source:          Beining Wu, Fuyou Mao, Jiong Lin, Cheng Yang, Jiaxuan Lu, Yifu Guo et al.
url_or_doc_id:   arXiv:2604.19516 ; https://arxiv.org/abs/2604.19516
published:       2026-04-21 (arXiv v1; latest listed 2026-04-21)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (ACL 2026 Findings, per arXiv comment) with code published
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          GPT-5.2, Gemini-3 Pro, Qwen-3 (three engines)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    ACL 2026 Findings
code_availability: https://github.com/Wu-beining/MAGEO
capability_class: learned reusable engine-specific content-edit skills raise generative-engine visibility and citation fidelity
```

## Verbatim — abstract

"Generative engines (GEs) are reshaping information access by replacing ranked links with citation-grounded answers, yet current Generative Engine Optimization (GEO) methods optimize each instance in isolation, unable to accumulate or transfer effective strategies across tasks and engines. We reframe GEO as a strategy learning problem and propose MAGEO, a multi-agent framework in which coordinated planning, editing, and fidelity-aware evaluation serve as the execution layer, while validated editing patterns are progressively distilled into reusable, engine-specific optimization skills. To enable controlled assessment, we introduce a Twin Branch Evaluation Protocol for causal attribution of content edits and DSV-CF, a dual-axis metric that unifies semantic visibility with attribution accuracy. We further release MSME-GEO-Bench, a multi-scenario, multi-engine benchmark grounded in real-world queries. Experiments on three mainstream engines show that MAGEO substantially outperforms heuristic baselines in both visibility and citation fidelity, with ablations confirming that engine-specific preference modeling and strategy reuse are central to these gains, suggesting a scalable learning-driven paradigm for trustworthy GEO. Code is available at https://github.com/Wu-beining/MAGEO"

## Verbatim — result sentences (from arXiv HTML full text)

- "Impact of Engine-Specific Preference Modeling: Removing the engine preference module causes a sharp performance drop ( ∼ sim 19% on GPT 5.2)."
- "Impact of the Skill Bank: Removing the Skill Bank results in a ∼ sim 13% drop."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2604.19516`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

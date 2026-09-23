# DECEPTICON: How Dark Patterns Manipulate Web Agents

```yaml
source:          Phil Cuvin, Hao Zhu, Diyi Yang
url_or_doc_id:   arXiv:2512.22894 ; https://arxiv.org/abs/2512.22894
published:       2025-12-28 (arXiv v1; latest listed 2026-02-06)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint; open-sourcing of tasks and evaluation code stated in text; academic table 'preprint with code'
source_label:    analyst-derived
lane:            D
sub_market:      agentic commerce
engine:          state-of-the-art open- and closed-source web agents (names not captured this pull)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     3
venue_status:    arXiv preprint
code_availability: release stated ('We open-source Decepticon'); URL not captured
capability_class: deceptive UI (dark patterns) steer web-agent trajectories toward unintended outcomes; larger models more susceptible
```

## Verbatim — abstract

"Deceptive UI designs, widely instantiated across the web and commonly known as dark patterns, manipulate users into performing actions misaligned with their goals. In this paper, we show that dark patterns are highly effective in steering agent trajectories, posing a significant risk to agent robustness. To quantify this risk, we introduce DECEPTICON, an environment for testing individual dark patterns in isolation. DECEPTICON includes 700 web navigation tasks with dark patterns -- 600 generated tasks and 100 real-world tasks, designed to measure instruction-following success and dark pattern effectiveness. Across state-of-the-art agents, we find dark patterns successfully steer agent trajectories towards malicious outcomes in over 70% of tested generated and real-world tasks -- compared to a human average of 31%. Moreover, we find that dark pattern effectiveness correlates positively with model size and test-time reasoning, making larger, more capable models more susceptible. Leading countermeasures against adversarial attacks, including in-context prompting and guardrail models, fail to consistently reduce the success rate of dark pattern interventions. Our findings reveal dark patterns as a latent and unmitigated risk to web agents, highlighting the urgent need for robust defenses against manipulative designs."

## Verbatim — result sentences (from arXiv HTML full text)

- "Across state-of-the-art agents, we find dark patterns successfully steer agent trajectories towards malicious outcomes in over 70% of tested generated and real-world tasks -- compared to a human average of 31%."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2512.22894`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

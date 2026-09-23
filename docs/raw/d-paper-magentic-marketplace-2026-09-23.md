# Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets

```yaml
source:          Gagan Bansal, Wenyue Hua, Zezhou Huang, Adam Fourney, Amanda Swearngin, Will Epperson et al.
url_or_doc_id:   arXiv:2510.25779 ; https://arxiv.org/abs/2510.25779
published:       2025-10-27 (arXiv v1; latest listed 2025-10-27)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with open-source environment (github.com/microsoft/multi-agent-marketplace); Microsoft-authored but not measuring a Microsoft commercial product
source_label:    analyst-derived
lane:            D
sub_market:      agentic commerce
engine:          GPT-4o, GPT-4.1, GPT-5, Claude Sonnet 4/4.5, Gemini 2.5 Flash, Qwen3-4B/14B
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     3
venue_status:    arXiv preprint
code_availability: https://github.com/microsoft/multi-agent-marketplace
capability_class: two-sided agent marketplace; first-proposal and position biases and manipulation vulnerability measured
bias_flag:       Microsoft Research authors; environment is open, not a Microsoft product measurement
```

## Verbatim — abstract

"As LLM agents advance, they are increasingly mediating economic decisions, ranging from product discovery to transactions, on behalf of users. Such applications promise benefits but also raise many questions about agent accountability and value for users. Addressing these questions requires understanding how agents behave in realistic market conditions. However, previous research has largely evaluated agents in constrained settings, such as single-task marketplaces (e.g., negotiation) or structured two-agent interactions. Real-world markets are fundamentally different: they require agents to handle diverse economic activities and coordinate within large, dynamic ecosystems where multiple agents with opaque behaviors may engage in open-ended dialogues. To bridge this gap, we investigate two-sided agentic marketplaces where Assistant agents represent consumers and Service agents represent competing businesses. To study these interactions safely, we develop Magentic-Marketplace -- a simulated environment where Assistants and Services can operate. This environment enables us to study key market dynamics: the utility agents achieve, behavioral biases, vulnerability to manipulation, and how search mechanisms shape market outcomes. Our experiments show that frontier models can approach optimal welfare -- but only under ideal search conditions. Performance degrades sharply with scale, and all models exhibit severe first-proposal bias, creating 10-30x advantages for response speed over quality. These findings reveal how behaviors emerge across market conditions, informing the design of fair and efficient agentic marketplaces."

## Verbatim — result sentences (from arXiv HTML full text)

- "For GPT-4o, which shows the least decline across search results, consumer welfare declines by 4.3% when providing one hundred search results versus three search results in the initial consideration set (Mexican 100-300)."
- "However, Qwen3-4B exhibited severe position bias, selecting the third-listed business 57.1% of the time in Mexican restaurant searches and 66.7% in contractor searches—more than double the expected rate under random selection."
- "The experiment results reveal extreme first-mover advantages across all models, with first proposals achieving selection rates between 60-100% compared to near-zero selection for third proposals."
- "GPT-4o and Sonnet-4.5 showed the most extreme behavior in certain conditions, achieving 100% first-proposal selection rates—meaning these agents never waited to compare alternatives once receiving an initial offer."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2510.25779`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

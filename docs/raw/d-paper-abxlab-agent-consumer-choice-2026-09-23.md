# A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments

```yaml
source:          Manuel Cherep, Chengtian Ma, Abigail Xu, Maya Shaked, Pattie Maes, Nikhil Singh
url_or_doc_id:   arXiv:2509.25609 ; https://arxiv.org/abs/2509.25609
published:       2025-09-30 (arXiv v1; latest listed 2026-02-24)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (ICLR 2026, per arXiv comment); framework release stated in text; repository URL not captured this pull
source_label:    analyst-derived
lane:            D
sub_market:      agentic commerce
engine:          17 models incl. GPT-4.1, GPT-5, Claude Sonnet 4, Claude 3.5 Haiku, Gemini 2.5 Pro/Flash, Llama 4, DeepSeek-R1
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     3
venue_status:    ICLR 2026
code_availability: release stated ('We release ABxLab'); URL not captured
capability_class: controlled price/rating/nudge manipulations shift shopping-agent choice predictably
```

## Verbatim — abstract

"Environments built for people are increasingly operated by a new class of economic actors: LLM-powered software agents making decisions on our behalf. These decisions range from our purchases to travel plans to medical treatment selection. Current evaluations of these agents largely focus on task competence, but we argue for a deeper assessment: how these agents choose when faced with realistic decisions. We introduce ABxLab, a framework for systematically probing agentic choice through controlled manipulations of option attributes and persuasive cues. We apply this to a realistic web-based shopping environment, where we vary prices, ratings, and psychological nudges, all of which are factors long known to shape human choice. We find that agent decisions shift predictably and substantially in response, revealing that agents are strongly biased choosers even without being subject to the cognitive constraints that shape human biases. This susceptibility reveals both risk and opportunity: risk, because agentic consumers may inherit and amplify human biases; opportunity, because consumer choice provides a powerful testbed for a behavioral science of AI agents, just as it has for the study of human behavior. We release our framework as an open benchmark for rigorous, scalable evaluation of agent decision-making."

## Verbatim — result sentences (from arXiv HTML full text)

- "The (unweighted) average attribute sensitivity for humans is ∼ sim 7%, lower than all models ."
- "For context, the lowest model is Claude 3.5 Haiku at ∼ sim 13%, and the highest is Claude Sonnet 4 at ∼ sim 31%."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2509.25609`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

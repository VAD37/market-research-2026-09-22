# AgentFloor: How Far Up the tool use Ladder Can Small Open-Weight Models Go?

```yaml
source:          Ranit Karmakar, Jayita Chatterjee
url_or_doc_id:   arXiv:2605.00334 ; https://arxiv.org/abs/2605.00334
published:       2026-05-01 (arXiv v1; latest listed 2026-05-01)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint; pre-registered comparison with released benchmark, harness and full run corpus; academic table 'preprint with code'
source_label:    analyst-derived
lane:            D
sub_market:      cross
engine:          16 open-weight models 0.27B-32B (incl. gemma4:26b, granite4:3b) vs GPT-5
metric_kind:     none
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     5
venue_status:    arXiv preprint
code_availability: released benchmark, harness, sweep configs and run corpus (link stated, not captured)
capability_class: open-weight models match GPT-5 on routine tool-use; frontier gap remains only on long-horizon planning
```

## Verbatim — abstract

"Production agentic systems make many model calls per user request, and most of those calls are short, structured, and routine. This raises a practical routing question that existing evaluations do not directly answer: which parts of an agent workflow truly require large frontier intelligence, and which can be handled by smaller models? We introduce AgentFloor, a deterministic 30-task benchmark organized as a six-tier capability ladder, spanning instruction following, tool use, multi-step coordination, and long-horizon planning under persistent constraints. We evaluate 16 open-weight models, from 0.27B to 32B parameters, alongside GPT-5 across 16,542 scored runs. Our results reveal a clear boundary of model necessity. Small and mid-sized open-weight models are already sufficient for much of the short-horizon, structured tool use work that dominates real agent pipelines, and in aggregate, the strongest open-weight model matches GPT-5 on our benchmark while being substantially cheaper and faster to run. The gap appears most clearly on long-horizon planning tasks that require sustained coordination and reliable constraint tracking over many steps, where frontier models still hold an advantage, though neither side reaches strong reliability. We also find that this boundary is not explained by scale alone: some failures respond to targeted interventions, but the effects are model-specific rather than universal. These findings suggest a practical design principle for agentic systems: use smaller open-weight models for the broad base of routine actions, and reserve large frontier models for the narrower class of tasks that truly demand deeper planning and control. We release the benchmark, harness, sweep configurations, and full run corpus."

## Verbatim — result sentences (from arXiv HTML full text)

- "At matched aggregate accuracy ( ∼ 60 % sim 60% overall TCR for both models), gemma4:26b on a Mac Studio amortised at 0.50/hr reaches 0.0022 per passed task, against GPT-5 at 0.0327 at posted prices — about 15 × times cheaper."
- "Smaller open-weight models reach lower aggregate accuracy at proportionally lower cost: granite4:3b at 40% aggregate TCR sits at 0.00046 per passed task on Mac, 71 × times cheaper than GPT-5."
- "On single-tool use (A), gemma4:26b is formally equivalent to GPT-5 at the ± 10 pm 10 pp margin: Δ = + 2.2 Delta=+2.2 pp, 95% CI [ 0 , + 6.7 ] [0,+6.7] (the 95% interval is wholly within ± 10 pm 10 pp, so the narrower 90% interval used for TOST is also within)."
- "On long-horizon planning under persistent constraints (E), GPT-5 is strictly superior to gemma4:26b : Δ = − 10.2 Delta=-10.2 pp, 95% CI [ − 18.4 , − 2.0 ] [-18.4,-2.0] ."
- "Absolute pass rates are 10% for GPT-5 and 0% for gemma4:26b — neither side reaches practitioner-relevant reliability on E."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2605.00334`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

# What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce

```yaml
source:          Amine Allouah, Omar Besbes, Josué D Figueroa, Yash Kanoria, Akshit Kumar
url_or_doc_id:   arXiv:2508.02630 ; https://arxiv.org/abs/2508.02630
published:       2025-08-04 (arXiv v1; latest listed 2025-12-17)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with code and datasets (github.com/mycustomai/ACES; HF datasets); bias flag: two of five authors affiliated with MyCustomAI
source_label:    analyst-derived
lane:            D
sub_market:      agentic commerce
engine:          Claude Sonnet 4, Claude Opus 4.5, GPT-4.1, GPT-5.1, GPT-4o, Gemini 2.0/2.5 Flash
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     3
venue_status:    arXiv preprint
code_availability: https://github.com/mycustomai/ACES
capability_class: audit of AI buying agents; simple query-conditional seller description tweaks move a product's market share
bias_flag:       Two of five authors affiliated with MyCustomAI (commercial); tool measures agent behaviour generally, not a proprietary product
```

## Verbatim — abstract

"Online marketplaces will be transformed by autonomous AI agents acting on behalf of consumers. Rather than humans browsing and clicking, AI agents can parse webpages or leverage APIs to view, evaluate and choose products. We investigate the behavior of AI agents using ACES, a provider-agnostic framework for auditing agent decision-making. We reveal that agents can exhibit choice homogeneity, often concentrating demand on a few ``modal'' products while ignoring others entirely. Yet, these preferences are unstable: model updates can drastically reshuffle market shares. Furthermore, randomized trials show that while agents have improved over time on simple tasks with a clearly identified best choice, they exhibit strong position biases -- varying across providers and model versions, and persisting even in text-only "headless" interfaces -- undermining any universal notion of a ``top'' rank. Agents also consistently penalize sponsored tags while rewarding platform endorsements, and sensitivities to price, ratings, and reviews vary sharply across models. Finally, we demonstrate that sellers can respond: a seller-side agent making simple, query-conditional description tweaks can drive significant gains in market share. These findings reveal that agentic markets are volatile and fundamentally different from human-centric commerce, highlighting the need for continuous auditing and raising questions for platform design, seller strategy and regulation."

## Verbatim — result sentences (from arXiv HTML full text)

- "While the impact was heterogeneous, a single iteration produced a statistically significant increase in market share for the focal product in 33% of our experiments."
- "In five out of the six AI buying models that we tested, we found statistically significant increase (averaged across product categories) in market share for a randomly chosen focal product: +3.66 (1.33) percentage points (p.p.) for Claude Sonnet 4, +8.37 (1.31) p.p. for GPT-4.1, +14.79 (1.36) p.p. for Gemini 2.5 Flash, +7.38 (1.0) p.p. for Claude Opus 4.5, +14.89 (1.05) p.p. for GPT-5.1, and +0.32 (1.22) p.p. for Gemini 3 Pro Preview."
- "For example, for Claude Sonnet 4, moving a product which is selected 4.5% of the time at the bottom right corner to the top row in the second or third column leads to a 5-fold increase in selection rate."
- "A sponsored tag reduces the likelihood of selection (a product with a baseline selection probability of 10% falls to 8.9% under Claude Sonnet 4, 8.0% under GPT-4.1, and 7.9% under Gemini 2.5 Flash), the scarcity tag effect is weakly negative or statistically indistinguishable from zero, whereas an overall pick endorsement delivers a large positive lift (raising the same baseline to 24.3%, 19.9%, and 42.6%, respectively)."
- "The Overall Pick tag produces very large lifts–e.g., +92% for Claude Sonnet 4, +65% for GPT-4.1 and +138% price headroom for Gemini 2.5 Flash."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2508.02630`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

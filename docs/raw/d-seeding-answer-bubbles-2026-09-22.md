# Huang, Goyal, Saha & Chandrasekharan (arXiv/EMNLP 2026) — Answer Bubbles: Information Exposure in AI-Mediated Search

```yaml
source:          Michelle Huang, Agam Goyal, Koustuv Saha, Eshwar Chandrasekharan
url_or_doc_id:   arxiv.org/abs/2603.16138
published:       2026-03-17 (v1); last revised 2026-08-28 (v2)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (EMNLP 2026, per Comments field) and code released at github.com/scuba-illinois/answer-bubbles-audit — academic table row "peer-reviewed, data or code published"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Vanilla GPT (GPT-4o-mini, no web search), Search GPT (GPT-4o-mini with web search), Google AI Overviews, Perplexity Search (with Grok-4-1), traditional Google Search
metric_kind:     visibility
supersedes:      none
captured:        abstract (abs page), methodology/results/limitations passages (via arxiv.org/html/2603.16138v2 full-text extraction)
technique:       corpus seeding — mechanism evidence for why Wikipedia functions as a high-citation source engines preferentially draw from
models_tested:   GPT-4o-mini (two configurations), Grok-4-1 (via Perplexity); Google AI Overviews and Google Search model/version not disclosed
date_window:     not stated in the extracted passages (checked arxiv.org/html/2603.16138v2 full text, 2026-09-22)
measured_effect: yes (source-representation level) — Wikipedia overrepresented +2.6pp (Search GPT) and +5.4pp (Google AI Overview); Reddit underrepresented, diff=-0.221, p<.001, n=149
vertical:        none named
```

## Verbatim

### Abstract

"Generative search systems are increasingly replacing link-based retrieval with AI-generated summaries, yet little is known about how these systems differ in sources, language, and fidelity to cited material. We examine responses to 11,000 real search queries across five systems---vanilla GPT, Search GPT, Perplexity Search with Grok, Google AI Overviews, and traditional Google Search---at three levels: source diversity, linguistic characterization of the generated summary, and source-summary fidelity. We find that generative search systems exhibit significant source-selection biases in their citations, favoring certain sources over others. Incorporating search also selectively attenuates epistemic markers, reducing hedging by up to 60% while preserving confidence language in the AI-generated summaries. At the same time, AI summaries further compound the citation biases: Wikipedia and longer sources are disproportionately overrepresented, whereas cited social media content and negatively framed sources are substantially underrepresented. Our findings highlight the potential for answer bubbles, in which identical queries yield structurally different information realities across systems, with implications for user trust, source visibility, and the transparency of AI-mediated information access."

### Methodology and results (extracted, html full text)

Query corpus: drawn from Google's Natural Questions (NQ) corpus, 11,000 queries across five systems.

Source-representation methodology: "Sources were identified through citation analysis of generated summaries, with coverage measured using entailment probabilities between source chunks and atomic content units extracted from responses."

Wikipedia: "the most-cited and most over-represented source" — +2.6 percentage points in Search GPT, +5.4pp in Google AI Overview.

Underrepresentation: "social media and forum sources are substantially under-represented. Reddit (n=149, diff=−0.221, p<.001) and Khan Academy (n=21, diff=−0.311, p<.001) are the most under-covered."

Code release: "Code for replicating our experiments can be found in https://github.com/scuba-illinois/answer-bubbles-audit"

### Limitations (verbatim)

"Our study has limitations that outline interesting directions for future work. [Temporal and geographic scope]: Our audit captures behavior of generative search systems at a single point in time from a single location... [Query representativeness]: Our queries are drawn from Google's Natural Questions (NQ) corpus... [Methodological proxies]: Our RQ3 pipeline relies on GPT-4o-mini for atomic content unit decomposition and RoBERTa-large for entailment scoring... [No user-study, ideology, or causal claims]: While we provide detailed characterization of outputs, we do not measure user perception or behavior... [System coverage and confounds]: We audit five systems, but the generative search landscape includes many other systems..."

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2603.16138 for metadata, arxiv.org/html/2603.16138v2 for full text), both 200.
- This paper does not itself describe a seeding technique; it documents the citation-source bias (Wikipedia overrepresentation) that would make Wikipedia a rational seeding target. Filed as mechanism evidence for question (1) "how it works."
- Note a within-source tension worth flagging for the census: the abstract's phrase "cited social media content... substantially underrepresented" and the body's specific Reddit figure (underrepresented, diff=-0.221) do not support a claim that Reddit is a high-citation-and-therefore-seeding-worthy source in this paper's own five-system sample — contrast this against the practitioner sources pulled separately (`d-seeding-justinmckelvey-playbook-2026-09-22.md`, `d-seeding-solcrys-citations-2026-09-22.md`) which report Reddit among the most-cited domains for ChatGPT/Perplexity specifically. Different systems, different windows — conflicting figures kept side by side, not averaged, per root CLAUDE.md.

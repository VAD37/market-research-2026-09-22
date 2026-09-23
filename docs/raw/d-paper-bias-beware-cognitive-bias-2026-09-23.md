# Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations

```yaml
source:          Giorgos Filandrianos, Angeliki Dimitriou, Maria Lymperaiou, Konstantinos Thomas, Giorgos Stamou
url_or_doc_id:   arXiv:2502.01349 ; https://arxiv.org/abs/2502.01349
published:       2025-02-03 (arXiv v1; latest listed 2025-10-22)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (EMNLP 2025, per arXiv comment and Semantic Scholar venue) with code published; academic table 'peer-reviewed, code published'
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Claude 3.5 Sonnet, Claude 3.7, LLaMA 8B/70B/405B, Mistral-large-2407
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    EMNLP 2025
code_availability: https://github.com/geofila/Bias-Beware
capability_class: psychological-principle wording in product descriptions shifts LLM recommendation rate and position
```

## Verbatim — abstract

"The advent of Large Language Models (LLMs) has revolutionized product recommenders, yet their susceptibility to adversarial manipulation poses critical challenges, particularly in real-world commercial applications. Our approach is the first one to tap into human psychological principles, seamlessly modifying product descriptions, making such manipulations hard to detect. In this work, we investigate cognitive biases as black-box adversarial strategies, drawing parallels between their effects on LLMs and human purchasing behavior. Through extensive evaluation across models of varying scale, we find that certain biases, such as social proof, consistently boost product recommendation rate and ranking, while others, like scarcity and exclusivity, surprisingly reduce visibility. Our results demonstrate that cognitive biases are deeply embedded in state-of-the-art LLMs, leading to highly unpredictable behavior in product recommendations and posing significant challenges for effective mitigation."

## Verbatim — result sentences (from arXiv HTML full text)

- "For example, we report that applying social proof to Claude 3.5 Sonnet results in an astounding δ ​ R ​ a ​ t ​ e = + 334 % delta Rate=+334% and a δ ​ P ​ o ​ s = + 50 % delta Pos=+50% ."
- "This results in a δ ​ R ​ a ​ t ​ e = − 30 % delta Rate=-30% when a product is supposed to sell out, while its position deteriorates by δ ​ P ​ o ​ s = − 54.15 % delta Pos=-54.15% ."
- "The impact is even more pronounced for products aimed at an exclusive group of consumers, with a δ ​ R ​ a ​ t ​ e = − 45.23 % delta Rate=-45.23% , and a δ ​ P ​ o ​ s = − 116.23 % delta Pos=-116.23% ."
- "To outline some of our results, in the laptop categories, for example, the social proof attack on Claude 3.5 leads to a δ ​ R ​ a ​ t ​ e = + 288.88 % delta Rate=+288.88% for 3 products (Rates before the attack were 12%, 2%, and 12%, and after the attack they became 30%, 13%, and 32% respectively) while the δ ​ P ​ o ​ s delta Pos did not vary."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2502.01349`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

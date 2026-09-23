# From Prompt to Purchase: How AI Brand Recommendations Move Consumers on the Open Web

```yaml
source:          Michael Iannelli, Alan Ai
url_or_doc_id:   arXiv:2606.10907 ; https://arxiv.org/abs/2606.10907
published:       2026-06-09 (arXiv v1; latest listed 2026-08-31)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; vendor-authored (Scrunch AI) measuring AI-referral effect on a clickstream panel; academic table 'vendor-authored measuring own product' = 5, bias flagged. No public code
source_label:    measured-by-us
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT, Claude, Gemini (assistant conversations joined to opt-in clickstream)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     4
venue_status:    arXiv preprint
code_availability: none (clickstream panel; aggregate results only)
capability_class: causal-style measurement that an AI brand recommendation raises off-platform brand search/site visits
bias_flag:       Authors affiliated with Scrunch AI, an AI-visibility vendor; observational panel, no transactions observed
```

## Verbatim — abstract

"When a conversational assistant recommends a brand to a user with no recent observed engagement, that user's same-name Google search rises $+4.3$ percentage points (pp) [$3.1$, $5.5$], visits to the brand's own site $+2.4$ pp [$1.4$, $3.5$], and brand-specific retailer-page visits $+1.0$ pp [$0.3$, $1.7$] over matched backward placebos. Recovering that estimate is the work. The mention creates a brand exposure no web log attributes to the assistant, and the naive all-mention funnel that seems to measure it is confounded: many mentions are incidental references to brands the user already uses ("your Netflix download"), whose downstream visits are that existing customer's own behavior and surface as a brand-specific pre-trend. We measure off-platform response on a panel that joins opt-in clickstream to the same users' ChatGPT, Claude, and Gemini conversations, and isolate the effect with a pre-trend event study, a stance classifier, non-customer conditioning, and a within-response same-category control: incidental name-drops then move behavior far less ($+1.8/+1.1/+0.3$), and the named brand moves far more than unnamed same-category brands in the same response. The downstream path is mostly search-mediated and reaches both own sites and retailer pages, with a destination mix that tracks baseline brand-directed behavior rather than redirecting toward either. The design is observational and we do not observe transactions, so retail is purchase-adjacent. Standard referrer-based and last-click measurement miss this upstream exposure: assistants move observably-unengaged users into open-web brand navigation along a path attributed elsewhere -- an acquisition touchpoint at the head of the customer journey that journey models and last-click attribution do not see."

## Verbatim — result sentences (from arXiv HTML full text)

- "When a conversational assistant recommends a brand to a user with no recent observed engagement, that user’s same-name Google search rises + 4.3 +4.3 percentage points (pp) [ 3.1 3.1 , 5.5 5.5 ], visits to the brand’s own site + 2.4 +2.4 pp [ 1.4 1.4 , 3.5 3.5 ], and brand-specific retailer-page visits + 1.0 +1.0 pp [ 0.3 0.3 , 1.7 1.7 ] over matched backward placebos."
- "A recommendation moves all three stages two to three times more than an incidental name-drop. 95% user-clustered bootstrap CIs."
- "Stage Lift (pp) Treated rate Recall (24h) + 1.57 +1.57 [ 1.26 1.26 , 1.87 1.87 ] 2.22 % 2.22% Recall (7d) + 2.08 +2.08 [ 1.55 1.55 , 2.54 2.54 ] 5.32 % 5.32% Discovery (7d) + 2.37 +2.37 [ 1.74 1.74 , 2.89 2.89 ] 7.20 % 7.20% Retail (7d, path-aware) + 0.52 +0.52 [ 0.30 0.30 , 0.77 0.77 ] 1.18 % 1.18% Own-site visit rate by day relative to the response."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2606.10907`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

# Disentangling Answer Engine Optimization from Platform Growth: A Log-Based Natural Experiment on ChatGPT Referral Traffic

```yaml
source:          Keisuke Watanabe, Kazuki Nakayashiki
url_or_doc_id:   arXiv:2606.04362 ; https://arxiv.org/abs/2606.04362
published:       2026-06-03 (arXiv v1; latest listed 2026-06-03)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; vendor-authored (Glasp Inc.) measuring AEO effect on its own domain; academic table 'vendor-authored measuring own product' = 5, bias flagged. Public aggregates + analysis code, no raw counts
source_label:    measured-by-us
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT referral traffic (server logs, GA4)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     4
venue_status:    arXiv preprint
code_availability: public release of indexed aggregates and analysis code (raw counts withheld)
capability_class: log-based natural experiment separating AEO intervention lift (1.82x) from platform-growth tailwind
bias_flag:       Authors are Glasp Inc. measuring their own domain; single domain, placebo test p=0.16 (suggestive not conclusive)
```

## Verbatim — abstract

"Large language model (LLM) "answer engines" such as ChatGPT now send measurable referral traffic to the open web, and a practice analogous to search engine optimization, here called Answer Engine Optimization (AEO), has emerged. Public AEO success stories typically quote large raw growth multiples, but raw referral growth is confounded by the rapid platform-level growth of the answer engines themselves. We report a longitudinal field study on a single high-traffic domain (glasp.co) whose corpus of hundreds of thousands of YouTube question-and-answer pages received a defined bundle of AEO interventions in January 2026 (detailed in Section 4). Because the interventions were concentrated on one subset of the site, the untreated remainder of the same domain acts as a contemporaneous control that absorbs the platform tailwind. Using first-party analytics and server logs rather than probabilistic third-party estimators, we find: (1) raw growth is dominated by the platform tailwind: on monthly aggregates total ChatGPT referrals grew 5.7x while untreated pages on the same domain grew 3.5x over the same window; (2) an interrupted time-series model on the weekly treated/control ratio estimates a discrete, intervention-aligned level increase of 1.82x (95% CI 1.31-2.54, HAC p=0.001), robust across engagement-filtered traffic (2.27x) and alternative specifications; (3) however, a conservative placebo-in-time permutation test yields p=0.16, so the effect is suggestive, not conclusive, given a short and noisy pre-period; and (4) Google organic clicks to treated pages did not fall beyond the ambient site-wide trend and indexation was preserved, consistent with the SEO-protection rule. The methodological message, separating treatment from platform tailwind with an on-domain control, matters more than any single multiple, and implies that headline AEO multiples substantially overstate causal effect."

## Verbatim — result sentences (from arXiv HTML full text)

- "The treated corpus was already gaining ChatGPT-referral share before the intervention. • Level break exp ⁡ ( β 2 ) = 1.82 exp(beta_{2})=mathbf{1.82} (95% CI 1.31 1.31 – 2.54 2.54 ), p = 0.001 p{=}0.001 : a significant discrete jump aligned with the intervention. • Slope change β 3 beta_{3} : p = 0.53 p{=}0.53 (not significant)."
- "All estimates sit in the 1.8 1.8 – 2.3 × 2.3times range. 6.6 SEO safety Google organic clicks to treated /youtube/ pages fell only ≈ 25 % approx 25% from their H2 2025 level to 2026, while impressions stayed within their normal range and ended the window near baseline (no deindexation; Figure 3 )."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2606.04362`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.

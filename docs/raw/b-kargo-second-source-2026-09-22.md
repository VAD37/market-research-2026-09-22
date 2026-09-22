# G2 — Kargo reviews page — admission-rule second source

```yaml
source:          G2 (g2.com) — third-party software review site, independent of Kargo
url_or_doc_id:   https://www.g2.com/products/kargo/reviews
published:       page title states "Kargo Reviews 2026"; captured individual review dated 2/26/2024
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text) — plain fetch to g2.com returns HTTP 403 (channels.md C37/C38's documented 403→ext pattern)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     downgraded from table default 3 — the captured review carries no n, no date-window claim beyond its own single post date, and reads as low-informational-content ("Nothing to dislike... best and quality things"); usable only as confirmation that a G2 product listing for Kargo exists and is reviewed, not as evidence about any number
source_label:    analyst-derived
lane:            B
sub_market:      paid placement
engine:          n/a — review-site page, not an assistant engine
metric_kind:     none
supersedes:      none
captured:        one review excerpt (the page's top-loaded review at pull time; page-level aggregate company/pricing summary block not returned by this pull)
```

## Verbatim

"Kargo Reviews 2026: Details, Pricing, & Features | G2"

Review, verified/incentivized: "rachit m. — Small-Business (50 or fewer emp.) — 2/26/2024 — 'Best Advertisement Maker Platform' — 4.5/5"

"What do you like best about Kargo? Kargo creates memorable advertising experiences that go beyond the first impression to captivate consumer attention and eye catcher as well as they make more attractive"

"What do you dislike about Kargo? Nothing to dislike about Kargo as they offer best and quality things"

"What problems is Kargo solving and how is that benefiting you? As it makes me to get order delivered by time"

"Validated Reviewer — Incentivized — Source: G2 invite"

## Pull notes — mechanical only

- Loaded via the Chrome extension (`claude-in-chrome`), `get_page_text`, in a dedicated new tab; the tab was closed immediately after this pull. Plain fetch to g2.com returns `403`, consistent with this cluster's other G2 pulls.
- `get_page_text` returned a single `<article>` review element rather than the page's top-level company/pricing summary block, the same pattern seen on the Pacvue G2 pull in this cluster — not re-queried further given this task's tool budget.
- The captured review is low-informational-content (generic superlatives, one line answers) and is flagged here rather than cited as evidence about Kargo's product or performance; its evidentiary value in this file is narrow — confirming a G2-verified listing for Kargo exists, independent of Kargo's own site — nothing more.
- **Admission-rule role**: this is the second, independent-of-Kargo source required by this task's admission rule, alongside source 1 (`docs/raw/b-openai-new-ways-buy-ads-2026-09-22.md`, OpenAI's own ads-partner page naming Kargo as a "technology partner"). G2 is a third-party review aggregator with no disclosed ownership stake in Kargo, satisfying limb (a)'s "two or more independent non-listicle sources" test — weakly, given the thinness of the specific review captured, but the page's existence itself (a distinct G2 product listing under Kargo's own name) is the operative fact for admission, not the review's content quality.
- No pricing figure captured in this excerpt, consistent with `b-kargo-emerging-platforms-2026-09-22.md`'s finding that Kargo publishes no self-serve pricing.

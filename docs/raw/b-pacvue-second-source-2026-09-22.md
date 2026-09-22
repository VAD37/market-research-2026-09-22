# G2 — Pacvue reviews page — admission-rule second source

```yaml
source:          G2 (g2.com) — third-party software review site, independent of Pacvue
url_or_doc_id:   https://www.g2.com/products/pacvue/reviews
published:       page title states "Pacvue Reviews 2026"; individual review dated 6/29/2026
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text) — plain fetch to g2.com returns HTTP 403 (channels.md C37/C38's documented 403→ext pattern)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor/agency study handling — a single named-role reviewer's account, no independent audit; usable as evidence a G2-verified user exists and names specific product features, not as a hard number
source_label:    analyst-derived
lane:            B
sub_market:      paid placement
engine:          n/a — review-site page, not an assistant engine
metric_kind:     none
supersedes:      none
captured:        one review excerpt (the page's top-ranked/first-loaded review at pull time; page-level aggregate rating/review-count summary not captured in this excerpt)
```

## Verbatim

"Pacvue Reviews 2026: Details, Pricing, & Features | G2"

Review, verified: "Verified User in Consulting, Mid-Market (51-1000 emp.), 6/29/2026 — 'Drive Efficiency with Automation & AI' — 5/5"

"What do you like best about Pacvue? We mainly use it for Amazon, but the biggest benefit is that it is a multi-platform tool. Managing multiple retail media usually requires logging into each dashboard, which is time-consuming. With Pacvue, we only need to log in once to navigate between them."

"What problems is Pacvue solving and how is that benefiting you? Pacvue helps us in two major ways: drastically reducing the time and effort spent on routine operations, and creating new value by enabling advanced analysis that was previously impossible. From an operational efficiency perspective, it allows us to automate ad management on Amazon... Additionally, **with the Pacvue Agent released in 2025**, we can now generate performance reports using natural language. This has transformed our data analysis process, reducing what used to take several hours down to just a few minutes... Furthermore, Pacvue Agent's ability to generate **Amazon Marketing Cloud (AMC) SQL queries** has been a game-changer."

## Pull notes — mechanical only

- Loaded via the Chrome extension (`claude-in-chrome`), `get_page_text`, in a dedicated new tab; the tab was closed immediately after this pull. Plain fetch to g2.com is documented `403→ext` per `channels.md` C37/C38, matching this cluster's identical StackAdapt-page finding.
- `get_page_text` returned an individual review's `<article>` element rather than the page's top-level company/pricing summary block (contrast `b-stackadapt-second-source-2026-09-22.md`, where the `<main>` element returned the full company overview) — a rendering/selector difference between the two G2 product pages, not a content gap on G2's side; this file captures what the tool returned rather than re-querying for the summary block, given this task's tool budget.
- **Admission-rule role**: this is the second, independent-of-Pacvue source required by this task's admission rule, alongside source 1 (`docs/raw/b-openai-new-ways-buy-ads-2026-09-22.md`, OpenAI's own ads-partner page naming Pacvue as a "technology partner"). G2 is a third-party review aggregator with no disclosed ownership stake in Pacvue, satisfying limb (a).
- Confirms independently, via a named G2-verified reviewer (not Pacvue's own marketing copy), that "Pacvue Agent" (an AI feature) exists and was "released in 2025" — corroborates the AI/automation framing on Pacvue's own `request-an-agentic-commerce-readiness-assessment/` page.
- No pricing figure captured in this excerpt (the page's title promises "Pricing" but that section was not returned by this pull); consistent with `b-pacvue-agentic-readiness-2026-09-22.md`'s finding that pacvue.com/pricing 404s. Not re-checked further in this pull.

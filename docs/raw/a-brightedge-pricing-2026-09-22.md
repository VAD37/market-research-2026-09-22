# BrightEdge — pricing (feature vs. base plan)

```yaml
source:          BrightEdge
url_or_doc_id:   https://www.brightedge.com/pricing (404); https://www.brightedge.com/ai-hyper-cube; https://www.brightedge.com/ (homepage/nav, checked for a pricing link)
published:       n/a — no pricing page exists
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — existence check against the vendor's own site structure
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page (404 response) plus homepage/product nav scan for any pricing link
feature:         AI Hyper Cube price delta against BrightEdge's base SEO plan
```

## Verbatim

Request to `https://www.brightedge.com/pricing` returned HTTP 404.

Homepage and AI Hyper Cube product page navigation menus (captured in full in `a-brightedge-ai-hypercube-2026-09-22.md`) list every product and resource link on the site; no "Pricing" or "Plans" link appears anywhere in the primary navigation, footer, or the AI Hyper Cube page's own calls to action, which are all "Request a Demo" / "Request demo" / "Login". Every call to action found across the BrightEdge pages pulled this cluster (AI Hyper Cube, AI Agent Insights, Win in AI Search, case-study index) routes to a demo request or login, never a self-serve checkout or a priced plan.

## Pull notes — mechanical only

- `unknown — checked brightedge.com/pricing (404), brightedge.com homepage nav, brightedge.com/ai-hyper-cube, brightedge.com/win-in-ai-search 2026-09-22` — no public price, and no public base-plan price to compare it against, was found on any BrightEdge page reached this session. BrightEdge is a sales-led enterprise platform; price and price delta are recorded as `not disclosed — checked brightedge.com 2026-09-22`, not estimated.
- No further pricing-guess URL patterns (`/plans`, `/plans-pricing`) were attempted beyond the one 404'd guess and the nav-menu scan, consistent with the task's discard-on-sight rule against guessed figures.

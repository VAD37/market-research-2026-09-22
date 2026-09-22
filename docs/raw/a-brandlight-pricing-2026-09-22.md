# Brandlight AI — pricing

```yaml
source:          Brandlight AI (brandlight.ai)
url_or_doc_id:   https://brandlight.ai/pricing (404); https://brandlight.ai/sitemap.xml (no pricing URL listed); https://brandlight.ai/ (homepage, sales-led CTAs only)
published:       undated
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary; this pull establishes an absence, not a claim
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full sitemap.xml (all listed URLs, none named "pricing"); homepage CTAs
```

## Verbatim

`brandlight.ai/pricing` returns HTTP 404. The site's own `sitemap.xml` (fetched in full, 2026-09-22) lists no `/pricing` URL among its ~50 entries — every call to action on the homepage, "Visibility & Insights" product page, and "AI Visibility For Iconic Brands" page is "Get a demo," "Contact Sales," or "Request your personal AI-Visibility walkthrough," never a self-serve checkout or a listed price.

Homepage CTA text, verbatim: "Get real attribution data, visibility intelligence, and a roadmap that ties AI search directly to outcomes. Contact Sales" (Marketing Leaders panel); "Give your clients the most advanced AI visibility, attribution, and partnership intelligence on the market. Partner With Us" (Agencies panel).

## Pull notes — mechanical only

- `brandlight.ai/pricing` fetched directly: HTTP 404.
- `brandlight.ai/sitemap.xml` fetched in full (raw XML, ~50 URLs) via two calls (max_length 4000 then 6000) — no pricing, plans, or cost page found among them.
- Homepage and two product pages fetched (see sibling files) — none names a dollar figure, a plan tier, or a self-serve signup path.
- Recorded: **not disclosed — checked brandlight.ai/pricing (404), sitemap.xml (no pricing URL), homepage and product pages (sales-led CTAs only), 2026-09-22.** Sales motion is enterprise/sales-led throughout (SOC 2 Type II, white-glove support, "Contact Sales" language).

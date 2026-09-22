# Semrush — pricing (feature vs. base plan, price delta disclosed)

```yaml
source:          Semrush
url_or_doc_id:   https://www.semrush.com/pricing/
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary pricing page
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a on this page itself (plan feature lists name "AI search" and "AI sentiment" generically, no specific engine)
metric_kind:     none
supersedes:      none
captured:        full page (static HTML) — the plan comparison table and add-on list, condensed from repeated nav/footer chrome
feature:         AI Visibility plan tier and its price delta against the base SEO-only plan
```

## Verbatim

"Plans & Pricing — Semrush helps you build and measure brand visibility, everywhere search happens. Start with what you need. Add more as you grow." Toggle: Monthly / Annually ("save up to 17%").

**SEO** — "For freelancers and small businesses looking to grow their online visibility with SEO." $117.33/mo billed annually (instead of $139 monthly). What's inside: 5 websites to monitor; 500 keywords to track daily; Basic keyword research and competitor analysis; Position Tracking; Site Audit; **Track performance in AI search; Monitor AI sentiment; AI visibility reports for any domain; Monitor custom prompts.**

**Starter** — "SEO + AI Search — For small teams and agencies growing across organic search and AI." $165.17/mo billed annually (instead of $199 monthly). SEO: 5 websites to monitor; 500 keywords to track daily; Keyword research and optimization tools; Competitors insights tools; MCP access. **AI Visibility: 50 prompts to track daily; 1 domain for AI brand performance; 300 AI visibility reports per day; AI-ready Site Audit.**

**Pro+** — "SEO + AI Search — For growing teams and agencies scaling SEO and AI visibility across multiple markets, locations, or websites." $248.17/mo billed annually (instead of $299 monthly). All Starter features plus: 15 websites to monitor; 1,500 keywords to track daily; Historical SEO data; Content optimization; Keyword cannibalization analysis; Multi-location/device tracking. **More in AI Visibility: 100 prompts to track daily.**

**Advanced** — "SEO + AI Search — For organizations and agencies scaling SEO and AI visibility with deeper insights, API access, and automation." $455.67/mo billed annually (instead of $549 monthly). All Pro+ features plus: 40 websites to monitor; 5,000 keywords to track daily; SEO share of voice; API data integration. **More in AI Visibility: 200 prompts to track daily.**

Compare-plans table confirms: "Share of Voice" reads "No" for the SEO plan and "Yes" for Starter/Pro+/Advanced.

**Semrush for Enterprise** — "For complex organizations managing multiple brands, regions, and teams — with the scale, controls, and integrations to operationalize visibility and prove its impact." Custom pricing, "Let's talk." Named enterprise-only features include: "Custom large-scale AI prompt tracking," "Multi-brand, multi-product AI visibility," "Forecasting & ROI attribution."

Add-ons (all plans): Additional Users, starting at $45/mo. Lead Generation, $90/mo (branded profile on Semrush Agency Partners platform, Semrush verified badge). Base Report, $10/mo. Pro Report, $20/mo (includes "AI-generated summaries").

## Pull notes — mechanical only

- Fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML, no JS-rendering gate for the pricing table itself.
- **Price delta, disclosed verbatim on the platform's own pricing page:** the base "SEO" plan (no dedicated "AI Visibility" section — though it does include four AI-search monitoring line items) costs **$139/mo month-to-month ($117.33/mo billed annually)**; the first plan naming a distinct, quantified "AI Visibility" section ("Starter") costs **$199/mo month-to-month ($165.17/mo billed annually)**. **Delta: +$60/mo month-to-month, or +$47.84/mo on the annual-billed rate**, for 50 prompts/day tracking, 1 domain for AI brand performance, 300 AI visibility reports/day, and AI-ready Site Audit, plus the SEO-side features Starter adds over the SEO plan (MCP access, keyword-research/optimization tools, competitor-insights tools) — the delta is not isolable to the AI Visibility line items alone, since Starter is a bundled step up on both SEO and AI axes at once. Recorded as the disclosed delta with this caveat, not decomposed further (no per-feature à la carte price is shown).
- The base "SEO" plan is not a clean "no AI-visibility-at-all" baseline: it already includes "Track performance in AI search," "Monitor AI sentiment," "AI visibility reports for any domain," and "Monitor custom prompts" — meaning some AI-visibility capability ships even at the entry tier, and the named "AI Visibility" toolkit section with prompt-count limits is what differentiates Starter and above.
- Enterprise-tier "AI Visibility" (custom large-scale prompt tracking, multi-brand) is priced "Custom" — `not disclosed — checked semrush.com/pricing 2026-09-22`.

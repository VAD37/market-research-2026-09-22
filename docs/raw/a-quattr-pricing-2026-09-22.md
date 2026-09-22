# Quattr — pricing (feature vs. base plan)

```yaml
source:          Quattr, Inc.
url_or_doc_id:   https://www.quattr.com/pricing
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary page, reliable on existence (no price exists), biased on framing
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page — the URL resolves (HTTP 200) but renders as a demo-booking landing page, not a priced plan table
feature:         AI Visibility price delta against Quattr's base plan
```

## Verbatim

`quattr.com/pricing` returns HTTP 200 but the rendered page carries no plan table, no tier names, and no dollar figures. Every call to action on the page is a demo-request form ("Ready to see Quattr in action? Book a Demo →") or a testimonial/proof panel (G2 rating 4.9/5, 65 reviews; case-study stat callouts for CloudEagle and Men's Wearhouse). The page's own footer states: "Every customer works with a Quattr Strategist," and the demo-request form itself asks for "Company Size" (banded 1-50 / 51-250 / 251-1000 / 1001+ employees) — consistent with a sales-qualification flow, not a self-serve checkout. No "AI Visibility" line-item, add-on price, or tier differentiation appears anywhere on this URL.

## Pull notes — mechanical only

- Fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML.
- `not disclosed — checked quattr.com/pricing 2026-09-22` — no public price for Quattr's base plan or for AI Visibility specifically exists on this page; Quattr is sales-led ("every customer works with a Quattr Strategist"). Price and price delta recorded as not disclosed, not estimated.
- No separate "AI Visibility add-on" pricing page or URL pattern was found; AI Visibility appears to be bundled into the core platform rather than sold as a separately priced SKU (see `a-quattr-ai-visibility-2026-09-22.md` — AI Visibility is one of four named pillars of the single Quattr platform, not a distinct purchasable line item), which is itself the answer to the "price delta" question for this vendor: there is no disclosed base-plan-without-the-feature to compare against.

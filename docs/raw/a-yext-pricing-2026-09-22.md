# Yext — pricing (access attempt; no public page found)

```yaml
source:          Yext (yext.com)
url_or_doc_id:   attempted https://www.yext.com/pricing (404), https://www.yext.com/platform/pricing (404), https://www.yext.com/platform/packages.html (404, despite being listed in yext.com/sitemap1.xml with lastmod 2026-09-09)
published:       n/a
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary; this pull establishes an absence, not a claim
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        three 404 responses; every CTA found across yext.com/, yext.com/platform/scout, and yext.com/customers (see sibling files) reads "Get a demo", "Contact sales", "Get started", or "Get a demo of the new Scout capabilities" — none is a self-serve checkout or a listed price
```

## Verbatim

`/pricing`: HTTP 404. `/platform/pricing`: HTTP 404. `/platform/packages.html`: HTTP 404, despite this exact URL being listed in `yext.com/sitemap1.xml` with `<lastmod>2026-09-09</lastmod>` — the sitemap entry appears stale (the page it points to no longer resolves, or resolves only under different conditions, e.g. a region/locale gate, not reached this pull).

No page fetched anywhere on yext.com this session (homepage, `/platform/scout`, `/customers`) shows a dollar figure, a plan-tier name with a price, or a self-serve signup path for Scout or for any Yext product. Every call to action is sales-led: "Contact sales", "Get started" (routes to a login/signup flow, not a priced checkout), "Get a demo", "See Yext in action", "Talk to an expert".

## Pull notes — mechanical only

- **Recorded: price — not disclosed. `not disclosed — checked yext.com/pricing (404), yext.com/platform/pricing (404), yext.com/platform/packages.html (404, stale sitemap entry), yext.com homepage, yext.com/platform/scout, yext.com/customers (all sales-led CTAs only), 2026-09-22.`**
- **Price delta: cannot be computed — `unknown — checked yext.com 2026-09-22`.** No base-plan price and no Scout-inclusive-plan price exist publicly to compare. Yext's sales motion for both the core platform and Scout specifically is fully enterprise/sales-led ("Contact sales" / "Get a demo"), unlike AirOps, Conductor, and HubSpot in this same cluster, none of which disclosed a dollar figure either but at least showed named self-serve tier structures (Solo/Pro/Enterprise, Essentials/Growth/Enterprise, Free/Starter/Professional/Enterprise). Yext shows no tier structure of any kind on any page pulled.

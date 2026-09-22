# Ahrefs — platform pricing (base plans vs. Brand Radar inclusion)

```yaml
source:          Ahrefs (ahrefs.com)
url_or_doc_id:   https://ahrefs.com/pricing
published:       undated, live pricing page as rendered 2026-09-22
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary pricing page
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        first ~5000 characters (main plan table); truncated before the full add-on section
```

## Verbatim

**Currency note:** displayed in Japanese Yen (¥) on this pull, consistent with the geolocation effect noted elsewhere in this cluster (this session's exit IP resolves to Japan). `ahrefs.com/brand-radar`, fetched the same session, displays USD for the same underlying products — both kept verbatim, unreconciled (see `a-ahrefs-brand-radar-product-2026-09-22.md`).

"# Plans & pricing — From first projects to enterprise scale, Ahrefs' plans help your business stay discoverable in search, AI, and beyond—powered by the world's second-most active crawler and 10+ years of web-scale data."

"### Lite — Essential data for small businesses and personal projects. — ¥19,900/mo — 5 projects, 6 months of historical data, 750 tracked keywords, **5 tracked AI prompts**, 100,000 crawl credits, API and MCP access, 1,000 credits per user, 1 user included, Add 2 more users at ¥6,160/mo each.

### Standard — Perfect for freelance SEOs and marketing consultants. — ¥38,400/mo — 20 projects, 2 years of historical data, 2,000 tracked keywords, **10 tracked AI prompts**, 500,000 crawl credits, API and MCP access, Unlimited credits per user, 1 user included, Add 5 more users at ¥9,240/mo each.

### Advanced — More tools and data for lean in-house marketing teams. — ¥68,900/mo — 50 projects, 5 years of historical data, 5,000 tracked keywords, **20 tracked AI prompts**, 1,500,000 crawl credits, API and MCP access, Unlimited credits per user, 1 user included, Add 10 more users at ¥12,320/mo each."

"What's included — Dashboard, Site Explorer, Keywords Explorer, **Brand Radar**, **Tracked AI prompts**, Site Audit, Always-on audit, Rank Tracker, Competitive Analysis, SERP history, Page Inspect, Web Analytics, API access, MCP Server, Report Builder, Social Media Manager (Beta), GBP Monitor (Beta) [— this feature list is explicitly the Lite tier's inclusions, confirmed by the page structure: 'All Lite features, plus:' precedes the Standard-tier additions]."

"### Enterprise — Scale with advanced customization, automation, and controls – backed by the data and infrastructure trusted by Fortune 500 teams. Talk to us for tailored solutions that ensure visibility where it matters most. — ¥230,900/mo — Annual commitment required — Talk to sales — All Advanced features, plus: Uncapped API access, Custom API Endpoints, SSO & enterprise-grade security, Access management & audit log, Unlimited historical data, Personalized higher limits & data exports, Forecasting & trends."

"### Starter — See what people search and spy on competitors. — ¥4,460/mo — Get started [a separate, smaller/older Ahrefs product tier, likely 'Ahrefs Starter' — not part of the four-tier Lite/Standard/Advanced/Enterprise ladder above]

### Ahrefs Free — Get Ahrefs data on your site and fix what matters. — Free — Get started

### Brand Radar AI — Research any brand across 475M+ organic prompts from Ahrefs database and track your own AI prompts. — Get started from ¥30,600/mo [note: this figure, ¥30,600/mo, and the prompt-count figure '475M+' both differ slightly from the USD '$199/mo' / '454M+' figures on `ahrefs.com/brand-radar` — recorded as found, not reconciled; may reflect a different currency/promo snapshot or a stale figure on one of the two pages]

### Custom prompt packages — Need to track your own prompts only? Subscribe to a package. Tracking one prompt on one platform in one location uses 1 check. Overage is billed at the end of the billing month.
- Basic — E.g. 80 prompts daily on 1 platform — ¥7,700/mo — +2,500 checks/mo — Overage ¥3.0800/check billed monthly
- Growth — E.g. 100 prompts daily on 2 platforms — ¥15,420/mo — +7,000 checks/mo — Overage ¥2.3100/check billed monthly
- Scale — High volume, lowest per-check rate — ¥38,500/mo — +25,000 checks/mo — Overage ¥1.5400/check billed monthly"

"## Optional add-ons — Content Kit... From ¥15,000/mo. Report Builder... ¥15,000/mo. Project Boost Pro [truncated]"

## Pull notes — mechanical only

- Single fetch call, max_length 5000; truncated mid-section ("Project Boost Pro"), remainder of the add-ons section not captured.
- **Base plan with the feature: Lite, ¥19,900/mo, includes Brand Radar (listed in the "What's included" feature table) and "5 tracked AI prompts."** Unlike AirOps, Conductor, and HubSpot's base tiers in this cluster, **Ahrefs's base tier is not feature-gated away from AI visibility — it includes a reduced quota (5 prompts) rather than zero.**
- **Price delta by AI-prompt quota across the four-tier ladder: Lite ¥19,900/mo → 5 prompts; Standard ¥38,400/mo (+¥18,500) → 10 prompts (+5); Advanced ¥68,900/mo (+¥30,500 from Standard, +¥49,000 from Lite) → 20 prompts (+10 from Standard); Enterprise ¥230,900/mo (+¥162,000 from Advanced) → "From 83" prompts. This is the clearest quantified, tiered price-to-AI-prompt-quota delta found across any incumbent in this cluster — all figures verbatim from the pricing table, not computed from estimates.**
- A **separate, standalone path** exists that isolates AI-visibility tracking specifically: "Brand Radar AI... Get started from ¥30,600/mo" (this page) / "AI Visibility Index... $199/mo" (`/brand-radar`, USD) — the two figures for the apparently same standalone product are not reconciled between the two pages pulled this session.

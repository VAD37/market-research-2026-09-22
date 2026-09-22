# HubSpot — Marketing Hub pricing (base plan vs. AEO-inclusive plan vs. standalone AEO)

```yaml
source:          HubSpot (hubspot.com)
url_or_doc_id:   https://www.hubspot.com/pricing/marketing
published:       undated, live pricing page as rendered 2026-09-22
pull_date:       2026-09-22
pull_method:     browser extension (MCP_DOCKER Playwright fallback — claude-in-chrome checked via tabs_context_mcp and reported "not connected" this session, per task's stated fallback order; page requires JS rendering, plain fetch returned an empty body)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary pricing page
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        accessibility-tree snapshot of the rendered page (Marketing Hub Free / Starter / Professional / Enterprise cards, plus the standalone "HubSpot AEO" add-on card)
```

## Verbatim

**Currency note:** the page auto-geolocated this session to Japan (the page's own embedded IP-lookup script reported `{"ip":"159.26.119.97","country":"jp"}`) and rendered all prices in Japanese Yen (¥), not USD. Kept verbatim per `../../method/demand-signals.md`'s currency rule (non-USD figures kept verbatim, never converted). The launch post and product page (see sibling files) separately state the standalone AEO price as "$50/mo" in USD — both figures describe the same SKU and are recorded side by side, unreconciled.

### Marketing Hub — Free / Starter / Professional / Enterprise (JPY, as rendered)

"Free — ¥0/mo — Free for up to 2 users. No credit card required."

"Starter — Essential marketing, sales, service, content, and data management software — Starts at ¥840/mo/seat [discounted/promotional price, 'Save up to 65% on Starter' banner active this pull] — regular price ¥2,400/mo/seat — Includes: 500 HubSpot Credits, 1,000 marketing contacts, Free tools with increased limits, plus remove HubSpot branding from Email marketing and Live chat, and: Agent Hub, Agent Builder, Simple marketing automation, CRM segments, Ad management, Data Agent."

"Professional — For marketing teams who want to effectively run omni-channel campaigns, automation, and reporting to build a scalable demand engine — Starts at ¥96,000/mo — regular price ¥106,800/mo — Includes 3 Core Seats, Additional Core Seats start at ¥5,400/mo — 3,000 HubSpot Credits, 2,000 marketing contacts — **'Marketing Hub Starter, plus:' Marketing studio (BETA), AEO (BETA), Content Agent (BETA), Nurture Agent (BETA), Social media, Video creation & editing** — *Cost shown does not include the required, one-time Professional Onboarding for a fee of ¥360,000."

"Enterprise — For marketing organizations seeking power, flexibility, and governance to orchestrate data-driven customer journeys at scale and accelerate revenue growth — Starts at ¥432,000/mo — Includes 5 Core Seats, Additional Core Seats start at ¥9,000/mo — 5,000 HubSpot Credits, 10,000 marketing contacts — 'Marketing Hub Professional, plus:' Multi-touch revenue attribution, Lookalike Segments (BETA), Customer journey analytics, Email approvals, Limit access to content and data, Behavioral event triggers and reporting — *Cost shown does not include the required, one-time Enterprise Onboarding for a fee of ¥840,000."

### Standalone add-on card, same page

"HubSpot AEO — New — See how your business shows up in answer engines — HubSpot AEO shows you how you appear in ChatGPT, Gemini, and Perplexity, where competitors are winning, and what to do about it. — ¥6,000/mo — ¥5,400/mo if you pay annually — **Track 25 prompts across 3 answer engines daily. Purchase additional prompts anytime.** — [Buy now] [Start 28-day trial] — No additional subscription required. — Learn about AEO: hubspot.com/products/aeo"

## Pull notes — mechanical only

- Browser extension (claude-in-chrome) checked via `tabs_context_mcp` at the start of this task and reported not connected; per the task's instructed fallback order, the MCP_DOCKER Playwright browser was used for this page specifically because the plain `mcp__MCP_DOCKER__fetch` tool returned only an empty `<p>` tag (page is a JS-rendered single-page app).
- Captured via `browser_navigate` + `browser_snapshot` (accessibility tree); the snapshot exceeded the tool's inline output limit and was read from its saved file with `Grep` and `Read` (offset/limit) rather than rendered whole.
- **Base plan without the AI-visibility feature: Marketing Hub Starter, ¥840/mo/seat (promotional) / ¥2,400/mo/seat (regular). AEO is not listed anywhere in the Starter feature list.**
- **Plan the feature sits in: Marketing Hub Professional, ¥96,000/mo (promotional) / ¥106,800/mo (regular), which explicitly lists "AEO (BETA)" under "Marketing Hub Starter, plus:". Enterprise (¥432,000/mo) inherits Professional's feature set including AEO.**
- **Price delta, Starter → Professional (promotional monthly, seat-adjusted where stated): ¥96,000 − ¥840 = ¥95,160/mo at the entry seat count (note: Starter is priced per seat, Professional includes 3 Core Seats bundled at its quoted price, so this is not a strict apples-to-apples per-seat delta — recorded as the vendor's own displayed starting prices, not normalized).** A standalone path exists that isolates the AI-visibility feature alone: the "HubSpot AEO" add-on at ¥6,000/mo (¥5,400/mo annual) / $50/mo (per the launch post and product page, USD), with "no additional subscription required" — this is the cleanest single-feature price point disclosed.
- Currency/geolocation and Starter-vs-Professional seat-count structure are both recorded as caveats in the census file rather than resolved by this pull.

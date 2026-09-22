# SE Ranking — pricing (AI Search add-on price delta, disclosed)

```yaml
source:          SE Ranking
url_or_doc_id:   https://seranking.com/pricing.html
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary pricing page
source_label:    vendor-reported
lane:            A
sub_market:      incumbent bundling
engine:          n/a on the pricing table itself (engines named on the feature page, `a-seranking-roster-clear-feature-2026-09-22.md`)
metric_kind:     none
supersedes:      none
captured:        full pricing page (plan tiers, add-ons, FAQ)
feature:         "AI Search" add-on — explicit price delta over the base platform plans
```

## Verbatim

Currency shown on this pull: **¥ (yen symbol rendered by the page, likely geo-IP-detected currency display — not confirmed as SE Ranking's primary/USD list price; see pull notes)**.

Billing toggle: "Monthly / Annually — Save 20%. Free migration with an annual subscription."

**Core** — "SEO + GEO for marketing teams with repeatable delivery." ¥17,455/mo (annual) / ¥21,819/mo (monthly). Includes: 10 projects & 1 manager seat; 2k keywords & **100 prompts to track daily**; **5 domains in GEO research**; 250k pages/month audit; 25K API credits & MCP access. "What's inside: Rank tracking across major search engines; Unlimited keyword, competitor, backlink research; Website & on-page audit; Data Studio/Matomo/GA/GSC integrations."

**Growth** — "Automation and collaboration for multi-client SEO + GEO." ¥37,752/mo (annual) / ¥47,190/mo (monthly). Includes: 30 projects & 3 manager seats; 5k keywords & **250 prompts to track daily**; **15 domains in GEO research**; 2M pages/month audit; 100K API credits & MCP access. "All Core features, plus: Historical data across project lifetime; Guest links for easy collaboration; Page changes monitoring; Dedicated customer support."

**Enterprise** — "Custom SEO & GEO platform for large teams and complex tasks." "Flexible terms. Custom limits and pricing. Full API & advanced integrations." "Talk to sales."

**Add-on: AI Search** — "Track, analyze, and optimize brand visibility across leading AI platforms." **+¥10,478/mo (annual billing) / +¥13,098/mo (monthly billing).** Tiers within the add-on: 200 / 450 / 1000 prompts. "AI Results Tracker: AI Overviews, AI Mode, Perplexity, ChatGPT. Unlimited competitor research across AI Overviews, AI Mode, Perplexity, and ChatGPT. Access to (200 prompts): A strategic dashboard for tracking brand mentions, citations, and sentiment trends. Automate data collection & reporting."

Other add-ons on the same page, for context: Agency Pack (+¥10,609/mo annual, white-label reporting); API (+¥7,033/mo annual, 3M/12M/60M credits); SMM platform "Planable" (from $33/mo — the one line item on this page shown in **USD**, not yen, an internal inconsistency not reconciled by this pull); standalone "SE Ranking API" (from ¥28,565/mo annual).

FAQ: "What's included in the free 14-day trial? ...up to 10 projects, 750 tracked keywords per day, 20 AI prompts per day, and AI competitive research for up to 3 domains (with unlimited reports)."

## Pull notes — mechanical only

- Fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML, no JS-rendering gate for the numbers captured (a client-side currency/region switcher may exist but was not exercised — this pull reflects whatever currency the server returned by default to a US-based fetch with no explicit region cookie set).
- **Price delta, disclosed verbatim: the "AI Search" add-on costs +¥10,478/mo on top of either the Core or Growth base plan (annual billing), or +¥13,098/mo month-to-month.** Both the Core (¥17,455/mo annual) and Growth (¥37,752/mo annual) base plans already include some GEO/prompt-tracking capacity (100 and 250 daily prompts respectively) — the AI Search add-on is a capacity upgrade (200/450/1000 prompts) and unlocks the described "AI Results Tracker" dashboard, not a strict feature on/off gate. This is the same "base plan already includes some AI capability, paid tier/add-on increases capacity" pattern seen in Semrush's pricing (`a-semrush-pricing-2026-09-22.md`), not a clean feature-absent-vs-feature-present comparison.
- **Currency caveat, load-bearing:** the ¥ symbol appearing throughout this pull is unexplained — SE Ranking is a Wilmington, Delaware-incorporated company (per `a-seranking-roster-clear-feature-2026-09-22.md`'s getlatka.com source) and every other vendor pulled in this cluster displays USD by default to this session's fetches. One line item on this same page (the Planable SMM add-on, "From $33/mo") renders in USD, inconsistent with the yen figures elsewhere on the identical page — flagged as an internal pricing-display inconsistency, not resolved by a second pull with an explicit region parameter this session. `unknown — checked seranking.com/pricing.html only, no region override attempted 2026-09-22` for the confirmed USD list price.

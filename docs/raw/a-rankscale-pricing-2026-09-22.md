# Rankscale.ai — pricing

```yaml
source:          Rankscale GmbH (rankscale.ai)
url_or_doc_id:   https://rankscale.ai/pricing
published:       undated on the pricing page itself; the /facts page (see `a-rankscale-method-engines-2026-09-22.md`) dates its own pricing reference "As of January 2026"
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary pricing page
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Gemini, Perplexity, Claude, DeepSeek, Mistral, Grok, Copilot, and more (per the plan comparison table's own engine-list note)
metric_kind:     none
supersedes:      none
captured:        full pricing page across two fetches (0-5000, then 5000-8500 characters)
```

## Verbatim

"Plans that scale with your ambition — Save 15% [annual toggle]

**Essentials** — Starting at $20/mo [full feature list not captured in the top-card summary; visible only in the comparison table's "Starting at" row]

**Pro** — $99 — 1,200 credits included each month — Used to query AI engines — No charge until day 7 · Cancel anytime — Gain deep insights & share results via dashboards & Looker Studio. — Track up to 4,800 answers from AI engines (depends on which engines you select) — Brand dashboards: 10 (add extra slots anytime in the app) — Page audits included: 50 (AI visibility checks for any URL) — Search terms: unlimited (creation unlimited · execution uses credits) — Regions: all

**Growth** (Most Popular ⭐) — $385 — 5,500 credits included each month — Additional benefits, white-label options, and REST API for seamless integration. — Track up to 22,000 answers from AI engines — Brand dashboards: 50 — Page audits included: 200 — Search terms: unlimited — Regions: all

**Enterprise** — $780 — 12,000 credits included each month — Scale your search strategy with REST API access and a dedicated partner by your side. — Track up to 48,000 answers from AI engines — Brand dashboards: 100 — Page audits included: 200 — Regions: all

'Rankscale GmbH contributes 1% of purchases to remove CO2 from the atmosphere.' — 'Trusted by 1000+ active users' — Brands / Agencies / Publishers

**Credit mechanic** (comparison-table tooltip, verbatim): 'Credits power all monitoring. Each time Rankscale queries an AI engine, it uses a fraction of a credit (typically 0.25). Your allocation renews each billing cycle — top up anytime.'

**Credit rollover** (tooltip): 'Unused credits roll over to the next billing cycle instead of expiring. The multiplier shows the maximum credits you can accumulate - e.g. 2× means up to twice your monthly allocation, 3× means up to three times.' Rollover multiplier: Essentials 'Up to 2×'; Pro/Growth/Enterprise 'Up to 3×'.

**AI engines** (tooltip, repeated verbatim across the comparison table): 'Includes ChatGPT, Gemini, Perplexity, Claude, DeepSeek, Mistral, Grok, Copilot, and more.'

Comparison-table 'Starting at' row, all four tiers: **Essentials $20/mo | Pro $99/mo | Growth $385/mo | Enterprise $780/mo** — all four SKUs carry an explicit dollar figure; none is 'custom' or 'Talk to us,' including the tier named 'Enterprise.'"

## Pull notes — mechanical only

- Fetched via mcp__MCP_DOCKER__fetch, simplified/markdown rendering, two calls (max_length 5000 at start_index 0, then max_length 3500 at start_index 5000) to reach the comparison table's full feature list and the "Starting at" pricing row.
- **All four tiers disclose a dollar figure** — the only vendor of the six in this cluster where even the top-named tier ("Enterprise") carries a public, undiscounted starting price rather than "custom" or "Talk to us." The comparison table's "Essentials" column renders several feature-count cells as "0" (monthly credits, brand dashboard slots, answers from AI engines, AI engines count) in this pull's static capture — likely a JS-populated cell value not captured by simplified fetch, since the top-card summary for Essentials was not separately shown (only referenced via the comparison table's "Starting at $20/mo" row and "Get Essentials" button). [note: Essentials tier's specific credit/dashboard/engine-count allotments not captured — cells rendered "0"]
- The /facts page (separate pull) states pricing 'starts from €20' — a different currency symbol (Euro vs. the pricing page's Dollar sign) for what is presumably the same Essentials tier; recorded side by side, not reconciled, per root CLAUDE.md.
- A promotional banner ("ChatGPT will now include ad placement in 31 new countries. Track your ads") appears twice at the top of every rankscale.ai page pulled this task — recorded once here as a site-wide element, not repeated per file.

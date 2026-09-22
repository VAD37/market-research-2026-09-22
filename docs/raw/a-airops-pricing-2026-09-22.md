# AirOps — pricing

```yaml
source:          AirOps (airops.com)
url_or_doc_id:   https://www.airops.com/pricing ; secondary: https://www.airops.com/aeo (pricing section, differing tier names/limits)
published:       undated — page states no publish date; sitemap.xml lastmod for /pricing is 2026-09-16
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary pricing page; no dollar figure is disclosed on either page pulled, which is itself the finding
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page text, /pricing; pricing section only, /aeo
```

## Verbatim

### /pricing — "The system built for every stage of growth"

"Straightforward pricing that grows with you."

"## Solo — For individuals building content for one brand or project.
- ChatGPT Insights Only
- 35,000 Tasks for Content Production
- 1 Brand Kit, 3 Knowledge Bases
- Basic CMS & SEO Integrations
- Community & Live Chat Support
- Single-User Access
[button: 'Start for free']

## Pro — For small teams building content for one brand or project.
- Insights Across 7+ Answer Engines
- 100,000 Tasks for Content Production
- 1 Brand Kit, 5 Knowledge Bases
- CMS, SEO, AEO, Social & Project Integrations
- Community & Live Chat Support
- Unlimited Seats for Your Team
[button: 'Start for free']

## Enterprise — For organizations building enterprise-grade content and tailored solutions.
- Custom Prompts & Pages Limits
- Multiple Regions, Personas & Languages Tracked
- Custom Agent Builds
- Custom Task Limits
- Unlimited Knowledge Bases & Brand Kits
- Dedicated Account Manager & Training
- 1:1 Expert Onboarding
- Unlimited Seats & Collaboration Functionality
[button: 'Work with us']"

Comparison-table row labels (feature matrix beneath the three cards), verbatim as rendered (table markup collapsed by the fetch tool, cell values follow each row label in Solo/Pro/Enterprise order where stated): "Intelligence — Answer Engines, Agent Analytics, Custom AEO Dashboards, ChatGPT Ads Insights (Beta), Sentiment & Theme Analysis, Competitor Analysis, Citation & Source Analysis — Opportunities — Owned, External (×3, one per tier) — Actions — Tasks — Brand Kits — Knowledge Bases — Collaboration — Quill — Playbooks & Workflows — Campaigns — Content Review & Quality Scores — Human Review & Approvals — Inbox — Collaborative Artifacts & Version History — 35,000 / 100,000 / Custom (Tasks) — 1 / 1 / Unlimited (Brand Kits) — 3 / 5 / Unlimited (Knowledge Bases) — Integrations — CMS — SEO Research — AEO Research — Project Management — Company Context — Social — AirOps MCP — MCP Connectors — Organization — Users — SSO — Bring your own Model API Keys — Support Tier — Forward Deployed Engineer (Enterprise, marked '1') — Community & Live Chat Support (Solo, Pro — marked 'Unlimited') — Dedicated Account Manager (Enterprise — marked 'Add-On')"

No dollar figure, currency symbol, or numeric price appears anywhere on the page for any of the three tiers. Every CTA reads "Start for free" (Solo, Pro) or "Work with us" (Enterprise).

### /aeo — pricing section (same page family, different copy)

"## Pricing Plans

### Solo — For individuals building content for one brand or project
- 100 Tracked Prompts & Pages
- ChatGPT Insights Only
- Monthly Opportunity Reports
- 20,000 Tasks for Content Production
- 1 Brand Kit, 3 Knowledge Bases
- Basic CMS & SEO Integrations
- Community & Live Chat Support
- Single-User Access
[button: 'Start for Free']

### Pro — Recommended — For small teams building content for one brand or project
- 250 Tracked Prompts & Pages
- Multi-Engine Insights
- Weekly Opportunity Reports
- 75,000 Tasks for Content Production
- 1 Brand Kit, 5 Knowledge Bases
- CMS, SEO, AEO, Soci[al...]" [note: page truncated by fetch tool's per-call length limit at this point; Enterprise tier and any further detail on this page not captured this pull]

## Pull notes — mechanical only

- `/pricing` fetched in full (single call, max_length 6000, no truncation marker).
- `/aeo` fetched with max_length 6000; the pricing section is truncated mid-sentence ("CMS, SEO, AEO, Soci...") — the Enterprise tier on this page and any dollar figure beyond this point was not captured this pull.
- Task limits, tracked-prompt limits and engine-count language differ between the two pages pulled on the same day (`/pricing`: "35,000 Tasks", "Insights Across 7+ Answer Engines" for Pro; `/aeo`: "20,000 Tasks", "100 Tracked Prompts & Pages", "Multi-Engine Insights" for Solo/Pro respectively) — not reconciled, recorded as found.
- **Recorded: price — not disclosed on any page pulled. `not disclosed — checked airops.com/pricing, airops.com/aeo, 2026-09-22`.** No self-serve dollar figure exists; both "Solo" and "Pro" tiers route to a free-start CTA with no listed price, and "Enterprise" is sales-led ("Work with us").
- Because no dollar price exists for either the base tier (Solo, "ChatGPT Insights Only") or the tier the AI-visibility/AEO feature sits in (Pro, "Insights Across 7+ Answer Engines" / "Multi-Engine Insights"), a **price delta cannot be computed** and is recorded as `unknown — checked airops.com/pricing, airops.com/aeo, 2026-09-22`. The qualitative delta (Solo = ChatGPT-only insights; Pro = 7+ engines / multi-engine insights, AEO integrations) is stated above verbatim.

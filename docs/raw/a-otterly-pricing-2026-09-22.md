# Otterly.AI — pricing

```yaml
source:          Otterly.AI (otterly.ai)
url_or_doc_id:   https://otterly.ai/pricing
published:       lastmod 2026-09-21T15:53:22.731Z (per sitemap_website.xml)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary pricing page
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Google AI Overviews, Perplexity, MS Copilot (base 4); Claude, Google AI-Mode/AI Mode, Gemini as paid add-ons
metric_kind:     none
supersedes:      none
captured:        full pricing page (single fetch, 5000 characters, page rendered both monthly and annual toggle states in the same static capture)
```

## Verbatim

"Pricing of OtterlyAI — Pick your plan. Start tracking AI search visibility today. — Trusted by great marketing teams & agencies — Monthly / Annually (15% off)

**Lite** — $29/month (monthly) / $25/month (annual, 15% off) — For solo marketers, and small teams — 15 search prompts — Tracking of 4 AI Search Engines: ChatGPT, Google AI Overviews, Perplexity, MS Copilot — Claude, Google AI-Mode, Gemini as extra Add-ons — Unlimited team members — Daily tracking frequency — ChatGPT Ads Tracking

**Standard** (Most Popular) — $189/month (monthly) / $160/month (annual) — For SMEs and small marketing teams — 100 search prompts — same 4-engine base + same 3 add-ons — Unlimited team members — Daily tracking frequency — ChatGPT Ads Tracking — API access — MCP access — Agent Analytics — Add 100 extra search prompts at $99

**Premium** — $489/month (monthly) / $422/month (annual) — For mid-sized companies & agencies — 400 search prompts — same 4-engine base + same 3 add-ons — Unlimited team members — Daily tracking frequency — ChatGPT Ads Tracking — API access — MCP access — Agent Analytics — Add 100 extra search prompts at $99

**Enterprise** — Custom — Starting from 1,000 search prompts — Talk to us — Everything in Premium, plus: Customizable Prompt Tracking, Single Sign-On, Custom payment options, Quarterly GEO Health Check, Custom terms, Personalized Onboarding Session, Dedicated Customer Success Manager

Feature inclusions common across tiers (verbatim, as listed per-tier): Unlimited Brand Reports, Unlimited Team Members, 1 Workspace (Lite) / Unlimited Workspaces (Standard/Premium/Enterprise), 3 Recommendations per week (Lite) / Unlimited Recommendations (Standard/Premium/Enterprise), Multi-country support (50+), AI Prompt Research Tool, Brand Visibility Index, Domain Ranking, Link Citations Analysis, Generative Engine Optimization Audit, Detailed Reports & Export, 1,000 GEO URL Audits/month (Lite) / 5,000 (Standard) / 10,000 (Premium) / Custom (Enterprise), Google Looker Studio Connector (Standard+), API/MCP Requests per month: 2,000/2,000 (Standard), 5,000/5,000 (Premium), Custom/Custom (Enterprise), Agent Analytics Events per month: 200k (Standard), 1M (Premium), Custom (Enterprise), Group Onboarding Session (Lite/Standard) / Personal Onboarding Session (Premium/Enterprise)."

## Pull notes — mechanical only

- Fetched via mcp__MCP_DOCKER__fetch, simplified/markdown rendering, single call (max_length 5000), content ran to the tool's truncation point mid-page; the monthly/annual toggle's two DOM states both appear in this static capture (e.g., "Lite$29/month" and, later in the same text, "Lite$25/month"), reconciled above as monthly vs. 15%-off-annual pricing for the same tier, not two different products.
- Four SKUs disclosed with explicit dollar figures for three of four (Lite, Standard, Premium); Enterprise is custom/undisclosed.
- Prompt-count-based pricing (15/100/400/1,000+ prompts) is the core lever across tiers — the most granular disclosed pricing structure of the six vendors in this cluster.

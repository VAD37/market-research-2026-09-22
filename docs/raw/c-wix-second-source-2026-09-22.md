# StockTitan — Wix.com (WIX) stock news page — admission-rule second source and ChatGPT/Gemini integration evidence

```yaml
source:          StockTitan (stocktitan.net) — third-party financial-news aggregator, independent of Wix
url_or_doc_id:   https://www.stocktitan.net/news/WIX/
published:       page aggregates releases through 2026-08-25; individual items dated 2026-08-25, 2026-08-24, 2026-08-11 (this last truncated)
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool, plain HTTP, no browser needed)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     adjusted down from table default 3 — StockTitan's "Rhea-AI Summary" content is AI-generated summarization of the underlying press release/filing, not the filing itself; used per this cluster's established precedent (see Feedonomics/Criteo second-source files) rather than a direct sec.gov pull
source_label:    analyst-derived
lane:            C
sub_market:      agentic commerce
engine:          ChatGPT — OpenAI (named directly, "Wix app in ChatGPT"); Google Gemini (named directly, dated integration announcement 2026-08-24)
metric_kind:     none
supersedes:      none
captured:        page excerpt — company description plus the three most recent news items at pull time (third item truncated)
```

## Verbatim

"WIX.com (WIX) Stock News & Updates | StockTitan"

"Wix.com Ltd. develops a software-as-a-service platform for creating, managing and growing a digital presence through websites, business tools and online services. News about WIX commonly covers product development in Wix Harmony, Wix Studio and Base44, AI-enabled creation workflows, **integrations such as the Wix app in ChatGPT**, and platform capabilities for commerce, scheduling, payments, SEO, accessibility, performance and security."

"08/25/2026 04:00 PM — News — Wix to Participate in Fireside Chat at Citi's 2026 Global Technology Conference — Rhea-AI Summary: Wix (NASDAQ: WIX) announced that its management will participate in a fireside chat at Citi's 2026 Global Technology Conference on Tuesday, September 8, 2026..."

"08/24/2026 09:00 AM — News — **Wix and Gemini Join Forces to Integrate Website Building Into Everyday Workflows** — Rhea-AI Summary: Wix (Nasdaq: WIX) announced a collaboration with Google to embed Wix Harmony website creation directly inside **Gemini** as a **connected app**. Users can now initiate, build, access, and manage Wix Harmony sites without leaving the Gemini interface. Within Gemini, users describe their site via voice or text, and a fully functional Wix Harmony website is generated on Wix's infrastructure, including support for **commerce, scheduling, payments, SEO and GEO**, accessibility, performance, and security. From the same conversation, users can expand business capabilities, track performance metrics, and make updates through natural language. The Wix app for Gemini is available in **eligible markets**, with sites manageable both in Gemini and via Wix Business Manager."

"08/11/2026 09:00 AM — News — Wix Launches Symphony by Wix, a New Standalone Multi-Agent [truncated by tool output limit]"

## Pull notes — mechanical only

- Fetched via plain HTTP fetch tool, no browser needed. Content truncated mid-headline on the third (oldest) news item; not re-fetched at a higher start_index since the two load-bearing items (ChatGPT app confirmation in the summary paragraph; the full Gemini integration article) were already captured.
- **Admission-rule role**: this is the second, independent-of-Wix source required by this task's admission rule, alongside source 1 (`docs/raw/c-paypal-protocol-agentic-commerce-2026-09-22.md`, PayPal's own partner page naming Wix). This source is unusually strong for the purpose: it independently confirms Wix ships AI-surface integrations with **two different P1 engines** (a "Wix app in ChatGPT," per StockTitan's own recurring-coverage description, and a dated, detailed Gemini connected-app partnership, 2026-08-24) — stronger evidence than Wix's own homepage in `c-wix-product-2026-09-22.md` provided directly.
- No dollar figure, fee, or take-rate stated for either the ChatGPT app or the Gemini integration on this page.
- "GEO" appears explicitly in the Gemini-integration item's feature list ("commerce, scheduling, payments, **SEO and GEO**") — a lane A/C crossover artifact, noted but not re-classified; this file stays lane C per the agentic-commerce framing of the overall Wix/PayPal admission path.

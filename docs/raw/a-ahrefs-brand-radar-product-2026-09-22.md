# Ahrefs — Brand Radar product page

```yaml
source:          Ahrefs (ahrefs.com)
url_or_doc_id:   https://ahrefs.com/brand-radar
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary; the one customer quote on this page is graded separately in `a-ahrefs-customers-2026-09-22.md`
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     visibility
supersedes:      none
captured:        first ~6000 characters (product/pricing sections); FAQ methodology section (chars 6000-9000) captured separately, see `a-ahrefs-method-2026-09-22.md`
```

## Verbatim

Title: "Ahrefs Brand Radar: See ANY brand's AI visibility"

Site-wide banner (unrelated to Brand Radar, marketing a separate new Ahrefs product): "Marketing reports, apps, and automations, handled. Meet Letaido." / "The only AI marketing platform built on Ahrefs' proprietary web index." / "'The AI marketing platform we needed didn't exist. So we built it.' — Tim Soulo, CMO at Ahrefs"

"# Brand Radar — Make AI recommend your brand — Track and grow your brand's visibility across AI answers, YouTube, and Reddit. Turn SEO into AEO and reach new audiences."

"## Track visibility two ways

**Custom Prompts** — Starts for free* — Track the exact questions your buyers ask. Works even if no one searches your brand name yet. Free in every Ahrefs paid plan. *With Ahrefs' Lite+ paid plans

**AI Visibility Index** — Starts at $199/mo — See any brand's AI visibility instantly across 454M prompts. No setup. Best once your brand already appears in AI search."

"454M+ Total monthly prompts — Index / Monthly prompts: AI Overviews 312.8M, Gemini 31.3M, Perplexity 31.2M, ChatGPT 31.2M, Copilot 30.8M, AI Mode 16.9M. 454M+ Total monthly prompts"

"### Preview your AI visibility for free — Check AI Visibility"

"1 AI Visibility — ## Find out what AI says about your brand — Track your brand mentions across AI answers and see how often you show up in the conversations that matter. Benchmark your brand against competitors in AI search and spot the big players. Find valuable AI citations and secure new mentions to boost your visibility in LLM answers.

2 Custom Prompts — ## Track the prompts your buyers actually use — Add the exact questions your buyers ask before they choose a brand. Use AI to generate relevant prompts from competitor comparisons, pricing data, and other signals Ahrefs collects. Discover the fanout queries AI generates when processing a prompt to find content gaps.

3 AI Analytics — ## See which pages AI sends traffic and bots to — AI traffic: Find the pages AI search already sends traffic to, then create more of what's working. Free · Install Web Analytics. Bot visits: Watch AI crawlers in real time: when they read your pages and which ones they visit most. Free while in beta · Install Bot Analytics.

4 AI Sources — ## Track the offsite sources that influence AI visibility — Scour YouTube for thumbnails, video titles, descriptions, and transcripts. See what's trending on TikTok. Search across Reddit results in Google including titles, descriptions, and subreddit snippets."

"## Used by 3,000+ companies" [customer count]

Customer quote (graded in `a-ahrefs-customers-2026-09-22.md`): "Before Brand Radar, I was testing scripts and manually extracting AI responses from ChatGPT, AI Overviews, all the main AI-search platforms. With Brand Radar, it's now just a few clicks to identify what I need, and export everything directly." — Laura Lancu, SEO Growth Specialist, Octopus Energy

"## Customer of Ahrefs? — Free AI prompts are already included in your paid plan.

| | Lite | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| Checks /mo | 150 | 300 | 600 | From 2,500 |
| Platforms | [not stated as a number in this table] | | | |
| Update frequency | | | | |
| AI prompts | 5 | 10 | 20 | From 83 |

Each prompt is checked daily on every selected platform. 5 prompts on 1 platform = 150 checks/mo. Claude consumes 8 checks per update."

"## Pricing

**Custom prompts** — Track how AI answers the prompts you define, refreshed daily. Great if your niche is too specific to show up in any database. — Starts at $50/mo, $699/MO FOR ALL MODELS

**AI Visibility Index** — Map your AI visibility across 454M real prompts people ask AI platforms. See who gets mentioned in your market. — $199/mo
- 83 prompts/day
- +2,500 checks/month
- Overage $0.020/check billed monthly
- All platforms (Claude available)
- Custom refresh cadence

Bonus: YouTube, TikTok & Reddit (free while in beta); Search demand; Web visibility"

**Named metrics (per the FAQ, captured in full in `a-ahrefs-method-2026-09-22.md`):** Mentions, Citations, AI Share of Voice, Estimated Impressions — each explicitly defined.

## Pull notes — mechanical only

- Two fetch calls (0–6000, then a separate call at start_index 6000 for the FAQ, filed as `a-ahrefs-method-2026-09-22.md`); a third region of the page (start_index 9000+) covers further FAQ content, partially captured there too.
- **Currency inconsistency, recorded as found:** this page (`/brand-radar`) displays USD ("$199/mo", "$50/mo", "$699/MO", "$0.020/check"), while `ahrefs.com/pricing` (see `a-ahrefs-pricing-2026-09-22.md`, fetched the same session, same apparent IP) displays Japanese Yen for the base Lite/Standard/Advanced/Enterprise plans. Not reconciled — both recorded verbatim.
- The "Platforms" and "Update frequency" table rows rendered with no values in the fetch tool's markdown simplification (table structure partially lost) — `unknown — checked ahrefs.com/brand-radar 2026-09-22` for the exact per-tier platform count and update-frequency figures beyond what the surrounding prose states.

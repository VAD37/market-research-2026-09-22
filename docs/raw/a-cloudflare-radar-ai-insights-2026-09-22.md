# Cloudflare Radar — AI Insights (live product, default view + News & Publications industry filter)

```yaml
source:          Cloudflare Radar
url_or_doc_id:   https://radar.cloudflare.com/ai-insights (default query); https://radar.cloudflare.com/ai-insights?industrySet=News+%26+Publications (industry-filtered query)
published:       live/continuous product — no single publish date; figures below are the state rendered at pull time
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default per channels.md C26 — telemetry, method published in the companion blog posts (a-cloudflare-crawl-refer-ratio-blog-2026-09-22.md, a-cloudflare-crawler-purpose-industry-blog-2026-09-22.md); page itself states "Change reflects comparison with the previous period" but the page's own on-screen period label is "Last 7 days" with no explicit start/end date printed next to the ratio card (dates inferred from the adjacent client-type chart's x-axis, see pull notes)
source_label:    analyst-derived
lane:            A
sub_market:      n/a
engine:          multiple — Anthropic (Claude), OpenAI, Perplexity, Microsoft, Google, Yandex, ByteDance, Baidu, DuckDuckGo, Mistral
metric_kind:     traffic
supersedes:      none
captured:        section "AI bot & crawler traffic" — HTTP traffic by bot, Crawl purpose, HTML page requests by client type, Crawl-to-refer ratio; default view and the News & Publications industry-set view. Robots.txt-compliance table and "Generative AI services popularity" section seen but not captured (out of this cluster's scope / assistant-share lane owned by another agent — see pull notes)
note:            source crosses metrics — recorded as traffic. Same crossing as the two blog-post pulls: the crawl-to-refer ratio's numerator is crawl volume (not traffic per glossary.md), its denominator is referral traffic (traffic per glossary.md). Population per channels.md C26: "Cloudflare-customer sites only; sells bot control" — this is not a web-wide census.
```

## Verbatim (transcribed from on-screen figures; page title and section headers quoted, table values read off the rendered cards)

Page title: "AI Insights | Cloudflare Radar." Section intro text: "AI bot & crawler traffic — AI bots scan public websites to collect data used in search engines, AI model training, and other data processing tasks." Time-range control at top right of page: "Last 7 days."

### Default view (no industry filter), "Last 7 days" as of 2026-09-22

**HTTP traffic by bot** ("HTTP request trends for top five most active AI bots"), dated x-axis Sep 15 – Sep 21:

| Bot | Share |
|---|---|
| Googlebot | 23.7% |
| ClaudeBot | 13.2% |
| Meta-ExternalAgent | 11.2% |
| Applebot | 9.3% |
| Bingbot | 7.2% |

**Crawl purpose** ("Traffic volume by crawl purpose"):

| Purpose | Share |
|---|---|
| Training | 44.6% |
| Training & Search | 40.1% |
| Search | 10.5% |
| User action | 2.7% |
| Undeclared | 2% |

**HTML page requests by client type** ("Share of HTML page requests by client type"), dated x-axis Sep 15 – Sep 21:

| Client type | Share |
|---|---|
| Non-AI bot | 53.2% |
| Human | 37.6% |
| AI bot | 5.5% |
| Mixed Purpose | 3.7% |

**Crawl-to-refer ratio** ("Ratio of HTML page crawl requests to HTML page referrals by platform. Change reflects comparison with the previous period"):

| Platform | Ratio | Change vs. prior period | User-agent breakdown |
|---|---|---|---|
| Perplexity | 2.5K : 1 | ▲ +17.7% | PerplexityBot 100%, Perplexity-User <0.1% |
| OpenAI | 592.2 : 1 | ▲ +28% | GPTBot 79.1%, OAI-SearchBot 12.9%, ChatGPT-User 8% |
| Anthropic | 581.7 : 1 | ▼ -0.3% | ClaudeBot 81.5%, Claude-SearchBot 18.4%, Claude-User 0.2% |
| Baidu | 43.7 : 1 | ▲ +8.9% | Baiduspider 100% |
| Microsoft | 40.9 : 1 | ▲ +4.2% | Bingbot 100% |
| Yandex | 33.2 : 1 | ▲ +10.6% | YandexBot 99.7%, YandexMobileBot 0.2%, Other 0.2% |
| ByteDance | 8.5 : 1 | ▼ -18.4% | Bytespider 100% |
| Google | 4.4 : 1 | ▼ -4.5% | Googlebot 88%, GoogleOther 11.1%, Other 0.8% |
| DuckDuckGo | 3.7 : 1 | ▲ +13.6% | DuckAssistBot 69.5%, DuckDuckBot 30.5% |
| Mistral | "No referrals" | — | MistralAI-User 100% |

### News & Publications industry-set view, "Last 7 days" as of 2026-09-22 (URL parameter `industrySet=News+%26+Publications`; on-screen badge "Industry set: News & Publications" confirmed present on each updated card)

**HTML page requests by client type** (News & Publications):

| Client type | Share |
|---|---|
| Non-AI bot | 51.6% |
| Human | 38.5% |
| Mixed Purpose | 5.3% |
| AI bot | 4.6% |

**Response status** (News & Publications): 200 — 67.9%; 403 — 10.1%; 301 — 8.4%; 404 — 3.7%; 304 — 2.6%; 302 — 2.3%; 206 — 1.4%; 204 — 0.8%; 308 — 0.6%; Other — 2.3%.

**Crawl-to-refer ratio** (News & Publications):

| Platform | Ratio | Change vs. prior period | User-agent breakdown |
|---|---|---|---|
| Anthropic | 11.7K : 1 | ▲ +1.9K% | ClaudeBot 81.5%, Claude-SearchBot 18.4%, Claude-User 0.2% |
| ByteDance | 909.3 : 1 | ▲ +8.7K% | Bytespider 100% |
| Perplexity | 223.5 : 1 | ▼ -89.4% | PerplexityBot 100%, Perplexity-User <0.1% |
| OpenAI | 109.9 : 1 | ▼ -76.2% | GPTBot 79.1%, OAI-SearchBot 12.9%, ChatGPT-User 8% |
| Microsoft | 50.6 : 1 | ▲ +29.1% | Bingbot 100% |
| Yandex | 32.3 : 1 | ▲ +7.7% | YandexBot 99.7%, YandexMobileBot 0.2%, Other 0.2% |
| Baidu | 17.7 : 1 | ▼ -55.9% | Baiduspider 100% |
| Google | 3 : 1 | ▼ -35.5% | Googlebot 88%, GoogleOther 11.1%, Other 0.8% |
| DuckDuckGo | 2.5 : 1 | ▼ -23.9% | DuckAssistBot 69.5%, DuckDuckBot 30.5% |
| Mistral | "No referrals" | — | MistralAI-User 100% |

## Pull notes — mechanical only

- `radar.cloudflare.com/ai-insights` returned `403` to a plain-fetch attempt in this session's own toolset (consistent with channels.md C26's recorded `403→ext`); reached via the Chrome extension per `tabs_context_mcp` → `navigate` → screenshot/zoom, exactly as the task brief specifies for this row.
- The page's charts and tables render as client-side widgets (canvas/SVG), not as extractable DOM text — `get_page_text` returned only section labels and helper strings ("Learn more...", "Share this...", etc.), no numeric content. All numeric figures above were read off zoomed screenshots of the rendered cards, not off `get_page_text` output. [note: figures transcribed from a rendered UI, not machine-extracted text — cross-checked twice via `zoom` on the same screenshot region before recording]
- **No explicit date-range string is printed directly on the "Crawl-to-refer ratio" card itself** — the page-level control reads "Last 7 days," and the adjacent "HTML page requests by client type" chart's x-axis shows daily ticks "Sep 15" through "Sep 21," which is taken as the implied window for every card on the page at pull time. This is an inference from the page layout, not a printed label on the ratio card — recorded as such rather than asserted as a stated fact.
- Comparing this live pull's default-view figures against the two stale blog posts (June 2025 and "first week of August" 2025 respectively) shows the ratios have moved by roughly two orders of magnitude down for Anthropic (70,900:1 → ~50,000:1 → 581.7:1) and up then down for OpenAI (1.6K:1 → 887:1 → 592.2:1), and Perplexity has moved from a mid-hundreds ratio in both 2025 posts to the **highest** ratio of any platform in this pull's default view (2.5K:1). All three time points are kept side by side in their respective raw files, per root `CLAUDE.md`'s "never averaged" rule — no trend line is asserted here, only the three dated readings.
- **Applebot** appeared in the default-view "HTTP traffic by bot" top five (9.3% share) but not in the "Crawl-to-refer ratio" card in either view captured — Apple carries no referral-ratio entry in this product at pull time. Recorded as `unknown — checked radar.cloudflare.com/ai-insights 2026-09-22` for an Apple crawl-to-refer figure specifically (a platform-identity pull for Apple was still made, since it surfaced here — see `a-apple-crawler-identity-2026-09-22.md`).
- Two further sections on this page — a "robots.txt compliance" table (rows seen: Bing Yes/No/Yes, Amazon Yes/Yes/Yes, ByteDance No/No/No, columns unlabeled in the viewport captured) and "Generative AI services popularity" (assistant-share chart) — were seen while scrolling but are **out of this pull's scope**: robots.txt compliance is closer to Lane D countermeasures than to this cluster's crawler-identity/volume question, and assistant-share data is explicitly reserved for the other live agent per this task's brief ("leave assistant usage-share figures to that agent even when they appear on a Cloudflare page"). Neither section's figures are recorded here.
- Industry-set dropdown offers additional sets beyond "News & Publications" (seen while scrolling the list: Art, Business & Industry, Computer & Electronics, Education, Finance, Gaming & Gambling, Health, Internet & Telecom, Law & Government, Media & Entertainment, Real Estate, Shopping & General Merchandise, Travel) — only "News & Publications" was selected and captured, chosen because it is the one industry example the companion blog post (`a-cloudflare-crawler-purpose-industry-blog-2026-09-22.md`) also names, allowing a same-industry, different-date comparison.

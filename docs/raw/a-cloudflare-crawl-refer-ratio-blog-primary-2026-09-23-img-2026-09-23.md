# Cloudflare — "AI search crawl-to-refer ratio on Radar" (2025-07-01) — image read (IMG-1b)

```yaml
source:          Cloudflare (blog.cloudflare.com; authors David Belson, Sam Rhea) — the twelve in-body images
url_or_doc_id:   https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar/
published:       2025-07-01 (page dateline, per source raw file)
pull_date:       2026-09-23
pull_method:     image read (IMG-1b) — Read tool on the PNGs saved by curl in the source pull
pull_purpose:    evidence about a number
tier:            4
tier_reason:     inherits a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23.md
source_label:    analyst-derived (Cloudflare Radar charts, as the charts state "Cloudflare Radar"); measured-by-us only where a value is read off an axis and marked "~"
lane:            A
sub_market:      n/a
engine:          multiple — Anthropic, OpenAI, Perplexity, Microsoft, Yandex, Google, ByteDance, Baidu, DuckDuckGo, Mistral (as printed on image 03)
metric_kind:     traffic (referral share) and crawl volume share; the ratio table is Cloudflare's own "crawl-to-refer ratio"
supersedes:      none — reads the images referenced in a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23.md; page text is in a-cloudflare-crawl-refer-ratio-blog-2026-09-22.md
captured:        twelve images, each transcribed below
```

Text cross-check note for the whole file: the page body text is in `a-cloudflare-crawl-refer-ratio-blog-2026-09-22.md` (the substitute); the primary file holds only the image list. "Text" below means that substitute's verbatim section.

## 01-blog-2836-image-1

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/01-blog-2836-image-1.png (1673 × 1350 px)

Chart type: two request-flow diagrams stacked, no axes, no numbers.

Top diagram: box "AI application ai.example.com" → arrow labelled "GET information.html / User-Agent: AIBot/1.0" → orange box "Cloudflare" containing "Content provider"; return arrow labelled "200 OK / Content-type: text/html".

Bottom diagram: laptop icon "User" → (1) "Create a travel itinerary for me" → box "AI application ai.example.com"; (2) "GET flights.html / User-Agent: AIBot-User/1.0" down to orange box "Cloudflare" containing "Content provider"; (3) "200 OK / Content-type: text/html" back up; (4) "Here's a suggested itinerary" back to User.

Legend / source line: none. Figures: none.

Text cross-check: the text describes both scenarios ("AIBot" for training, "AIBot-User" for a user request — "looking for flight information, for example"). No figure to compare.

## 02-blog-2836-image-2

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/02-blog-2836-image-2.png (1761 × 882 px)

Chart type: request-flow diagram, no axes, no numbers.

Laptop icon "User" ↔ box "AI application ai.example.com": (1) "Request", (2) "Response". User ↔ orange box "Cloudflare" containing "Content provider": (3) "GET information.html / Referer: https://ai.example.com", (4) "200 OK / Content-type: text/html".

Legend / source line: none. Figures: none.

Text cross-check: matches the text's "the client will often send a Referer: header as part of the request to the target site". No figure.

## 03-blog-2836-image-3

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/03-blog-2836-image-3.png (1137 × 506 px)

Chart type: Radar widget rendered as a static image — a 2 × 5 grid of platform cards, each with a ratio, a change figure, and a horizontal bar per user agent.

Title printed: "Crawl-to-refer ratio". Subtitle: "Ratio of HTML page crawl requests to HTML page referrals by platform. Change reflects comparison with the previous period".

No date range printed on the image.

| Platform | Ratio | Change vs previous period | User agents (share) |
|---|---|---|---|
| Anthropic | 70.9K : 1 | ↓ -5.7% | ClaudeBot 100% · Claude-SearchBot < 0.1% · Claude-User < 0.1% |
| OpenAI | 1.6K : 1 | ↓ -13.1% | GPTBot 94.2% · ChatGPT-User 3.7% · OAI-SearchBot 2.1% |
| Perplexity | 202.4 : 1 | ↓ -3.6% | PerplexityBot 85.1% · Perplexity-User 14.9% |
| Microsoft | 40 : 1 | ↓ -4.4% | Bingbot 100% |
| Yandex | 18 : 1 | ↑ +6.4% | YandexBot 99.4% · YandexMobileBot 0.3% · YandexImages 0.3% · Other < 0.1% |
| Google | 9.4 : 1 | ↓ -19.4% | Googlebot 92.7% · GoogleOther 6.5% · Googlebot-Mobile 0.4% · Other 0.4% |
| ByteDance | 1.4 : 1 | ↓ -7.8% | Bytespider 100% |
| Baidu | 1 : 1 | ↓ -17.2% | Baiduspider 100% |
| DuckDuckGo | 0.3 : 1 | ↑ +6.8% | DuckDuckBot 66.7% · DuckAssistBot 33.3% |
| Mistral | 0.1 : 1 | = 0% | MistralAI-User 100% |

Legend: none beyond the per-card bars. Source line on image: none.

Text cross-check: the text states "for the period June 19-26, 2025 … the ratios range from Anthropic's 70,900:1 down to Mistral's 0.1:1", "increases of over 6% for DuckDuckGo and Yandex to Google's 19.4% decrease" — image: Anthropic 70.9K : 1, Mistral 0.1 : 1, DuckDuckGo +6.8%, Yandex +6.4%, Google -19.4%. The substitute also carries a ten-row table headed "embedded widget, captured live at pull time 2026-09-22" whose every figure is identical to this image; this image is a static PNG served from `blog.cloudflare.com/_emdash/api/media/file/` (per the source raw's pull notes), and its rendering carries no date.

## 04-blog-2836-image-4

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/04-blog-2836-image-4.png (1600 × 774 px)

Chart type: line chart, two series, Cloudflare Radar export.

Title: "HTTP traffic worldwide". Subtitle: "HTTP requests from the specified bot over the selected time period".

Series (legend): "GoogleBot" (solid line) · "Previous 7 days" (dashed line).

Y axis: labelled "Max" at top and "0" at bottom; no intermediate values, no unit. X axis ticks: "Sat, Jun 21, 00:00" · "Sun, Jun 22" · "Tue, Jun 24, 00:00" · "Wed, Jun 25" · "Fri, Jun 27, 00:00".

Footer printed: "Cloudflare Radar" · "Last 7 days | Jun 27, 2025, 15:00 UTC".

Shape (no values readable — axis is Max/0 only): the solid GoogleBot line sits at or near "Max" on Jun 21–22, then runs below the dashed previous-7-days line from about Jun 24 onward — measured-by-us (read off axis, shape only).

Text cross-check: the text states "an observed drop in crawling traffic from GoogleBot starting on June 24". No numeric figure on the chart.

## 05-blog-2836-image-5

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/05-blog-2836-image-5.png (1600 × 774 px)

Chart type: line chart, two series, Cloudflare Radar export.

Title: "HTTP traffic worldwide". Subtitle: "HTTP requests from the specified bot over the selected time period".

Series (legend): "YandexBot" (solid) · "Previous 7 days" (dashed).

Y axis: "Max" / "0", no intermediate values, no unit. X axis ticks: "Sat, Jun 21, 00:00" · "Sun, Jun 22" · "Tue, Jun 24, 00:00" · "Wed, Jun 25" · "Fri, Jun 27, 00:00".

Footer printed: "Cloudflare Radar" · "Last 7 days | Jun 27, 2025, 15:00 UTC".

Shape: the solid YandexBot line rises from the dashed line's level on Jun 21 to a band above it for the rest of the window, reaching "Max" near Jun 27 — measured-by-us (read off axis, shape only).

Text cross-check: the text states "an observed increase in YandexBot crawling activity that started on June 21". No numeric figure on the chart.

## 06-blog-2836-image-7

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/06-blog-2836-image-7.png (1051 × 627 px)

Chart type: stacked-area chart (100 % share) with a share bar beneath. (The page numbers its images 1–13 with no "Image 6".)

Title: "Referred HTML requests time series". Subtitle: "Share of referred HTML requests by AI & search platform over time".

Legend (all series, in printed order): google.* · tiktok.com · bing.com · yandex.* · m.baidu.com · duckduckgo.com · cn.bing.com · chatgpt.com · baidu.com · scholar.google.* · claude.ai · chat.mistral.ai · perplexity.ai · safe.duckduckgo.com · gemini.google.com · html.duckduckgo.com · i.duckduckgo.com · start.duckduckgo.com · lite.duckduckgo.com · www2.bing.com · bing.com.br · beta.duckduckgo.com · next.duckduckgo.com.

Y axis: "Requests", 0% to 100% in 10% steps. X axis ticks: "Sun, Jun 1" · "Thu, Jun 5" · "Mon, Jun 9" · "Fri, Jun 13" · "Tue, Jun 17" · "Sat, Jun 21" · "Wed, Jun 25".

Share bar beneath the chart, labelled segments: "google.* 82%" · "tiktok.com 9.3%"; remaining segments unlabelled (orange, green, olive, pink, purple slivers).

Shape: the google.* band occupies roughly 75–85% of the stack through the window; tiktok.com the next band — measured-by-us (read off axis).

Source line on image: none. Date range: from the axis, Jun 1 to about Jun 27 (year not printed).

Text cross-check: the text says the referrer-centric view covers "nearly the first four weeks of June 2025" and "referral traffic is dominated by search platform Google"; the 82% and 9.3% figures are not in the text.

## 07-blog-2836-image-8

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/07-blog-2836-image-8.png (814 × 648 px)

Chart type: stacked-area chart, same dataset as 06 with google.*, tiktok.com, chatgpt.com, scholar.google.*, claude.ai, chat.mistral.ai, perplexity.ai and gemini.google.com greyed out (deselected) in the legend; active series: bing.com · yandex.* · m.baidu.com · duckduckgo.com · cn.bing.com · baidu.com · safe.duckduckgo.com · html.duckduckgo.com · i.duckduckgo.com · start.duckduckgo.com · lite.duckduckgo.com · www2.bing.com · bing.com.br · beta.duckduckgo.com · next.duckduckgo.com.

Title / subtitle: as 06. Y axis: "Requests", 0% to 12% in 2% steps. X axis ticks: as 06.

Share bar beneath: "google.* 82%" · "tiktok.com 9.3%" (unchanged from 06).

Shape: the stacked active series total oscillates between ~6% and ~11% with a visible daily cycle; bing.com (orange, bottom band) ~2–3.5%, yandex.* (olive) next ~2%, m.baidu.com (green) ~1.5–2%, duckduckgo.com (pink) ~1% — measured-by-us (read off axis).

Text cross-check: text says "Clear diurnal patterns are also visible in the referral request shares of other search platforms, although the request shares are a fraction of what is seen from Google". No numeric figure in text for these series.

## 08-blog-2836-image-9

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/08-blog-2836-image-9.png (814 × 648 px)

Chart type: stacked-area chart, same dataset; active series: chatgpt.com · claude.ai · chat.mistral.ai · perplexity.ai · gemini.google.com; all search-platform hosts greyed out.

Title / subtitle: as 06. Y axis: "Requests", 0% to 0.4% in 0.05% steps. X axis ticks: as 06.

Share bar beneath: "google.* 82%" · "tiktok.com 9.3%" (unchanged).

Shape: the stacked AI-platform total sits mostly between ~0.1% and ~0.3%, peaks ~0.4% near Jun 5 and ~0.37% near Jun 26; chatgpt.com (red) is the dominant band; claude.ai, perplexity.ai, gemini.google.com, chat.mistral.ai are thin slivers on top — measured-by-us (read off axis).

Text cross-check: text says "Throughout June, the share of traffic referred by AI platforms was significantly lower, even in aggregate, than the share of traffic referred by search platforms". No numeric figure in text.

## 09-blog-2836-image-10

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/09-blog-2836-image-10.png (814 × 648 px)

Chart type: stacked-area chart (100 % share) with a share bar beneath.

Title: "Crawler HTML requests by user agent time series". Subtitle: "Share of AI & search platform HTML requests by user agent over time".

Legend (printed order): Googlebot · GPTBot · GoogleOther · ClaudeBot · Bingbot · YandexBot · ChatGPT-User · Bytespider · OAI-SearchBot · Baiduspider · PerplexityBot · Googlebot-Image · Google-CloudVertexBot · Perplexity-User · DuckDuckBot · Googlebot-Mobile · YandexImages · YandexMobileBot · DuckAssistBot · Googlebot-Video · YandexMarket · Claude-SearchBot · Claude-User · MistralAI-User.

Y axis: "Requests", 0% to 100% in 10% steps. X axis ticks: "Sun, Jun 1" · "Thu, Jun 5" · "Mon, Jun 9" · "Fri, Jun 13" · "Tue, Jun 17" · "Sat, Jun 21" · "Wed, Jun 25".

Share bar beneath, labelled segments: "Googlebot 55%" · "GPTBot 16%" · "ClaudeBot 11%" · (unlabelled orange segment) · "Bingbot 6.5%" · further unlabelled slivers.

Shape: Googlebot (dark blue, bottom band) ~60–65% early June, falling to ~25–45% by Jun 25–27; GPTBot (light blue) band widens over the month; several sharp dips in the GPTBot band — measured-by-us (read off axis).

Source line on image: none.

Text cross-check: text says the crawler-centric view covers "nearly the first four weeks of June 2025" and "the share of requests related to Google's crawling activity for both their Googlebot and GoogleOther identifiers falls over the course of the month". The 55% / 16% / 11% / 6.5% figures are not in the text.

## 10-blog-2836-image-11

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/10-blog-2836-image-11.png (814 × 648 px)

Chart type: area chart, same dataset as 09 with only GPTBot active (all other user agents greyed out in the legend).

Title / subtitle: as 09. Y axis: "Requests", 0% to 30% in 5% steps. X axis ticks: as 09.

Share bar beneath: "Googlebot 55%" · "GPTBot 16%" · "ClaudeBot 11%" · "Bingbot 6.5%" (unchanged from 09).

Shape: GPTBot share ~13–18% in the first week of June, ~15–23% mid-month, ~20–29% in the last week; the band drops to ~0% in several short spells (around Jun 2, Jun 5–6, Jun 8, Jun 15, Jun 21–22, Jun 24, Jun 26) — measured-by-us (read off axis).

Text cross-check: text says "OpenAI's GPTBot saw multiple periods where little-to-no crawling activity was observed throughout the month". No numeric figure in text.

## 11-blog-2836-image-12

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/11-blog-2836-image-12.png (1470 × 687 px)

Chart type: product screenshot — Radar "Bots Directory" listing page. No chart.

Title: "Bots Directory". Sub-line: "Search and view detailed information about bots". Controls: search box "Search bots...", dropdown "Filter by category", link "Add a bot". Count printed: "286 results".

Cards visible (name — description excerpt — operator — category tag — status):

- 360Monitoring — "Empowering Developers to Monitor Sites & Servers, Easily" — 360Monitoring — Monitoring & Analytics — Verified
- Apple App Site Association — "The Apple App Site Association is used to support "Universal Links" that can open in native iOS apps…" — Apple — Other — Verified
- Accessible Web Bot — "Accessible Web Bot crawls customer websites to discover pages and monitor for accessibility violations on regular basis…" — Accessible Web — Accessibility — Verified
- Adagio Bot — "Adagio demand optimization solutions help publishers leverage unlimited demand sources at unprecedented revenue level…" — Adagio — Monitoring & Analytics — Verified
- AddThis — "The AddThis bot crawls websites to gather and update content for its website marketing tools…" — AddThis — Search Engine Optimization — Verified
- Bing Ads — "The Bing Ads bot, also known as AdIdxBot, is a crawler used by Microsoft's advertising platform. It crawls advertiser landing pages to check for policy compliance and quality." — Microsoft — Advertising & Marketing — Verified

Source line: none. Date: none printed.

Text cross-check: text says "The Bots page on Cloudflare Radar includes a paginated list of Verified Bots, displaying the bot name, owner, category, and rank". The "286 results" count is not in the text.

## 12-blog-2836-image-13

image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/12-blog-2836-image-13.png (1471 × 763 px)

Chart type: product screenshot — Radar bot detail page with one line chart.

Title: "Bot Information for ChatGPT-User" · badge "Verified" · period selector "Last 7 days".

"About" panel, verbatim: "ChatGPT-User is for user actions in ChatGPT and Custom GPTs. When users ask ChatGPT or a CustomGPT a question, it may visit a web page to help answer and include a link to the source in its response." Category: "AI Assistant". Operator: "OpenAI". Documentation: "https://platform.openai.com/docs/bots".

"User agent" panel — HTTP requests: "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot". robots.txt: "User-Agent: ChatGPT-User / Disallow: /".

Chart: "HTTP traffic" — "HTTP requests from the specified bot over the selected time period". Series: "ChatGPT-User" (solid) · "Previous 7 days" (dashed). Y axis: "Max" / "0", no intermediate values. X axis ticks: "Fri, Jun 20" · "Sun, Jun 22" · "Mon, Jun 23" · "Wed, Jun 25" · "Thu, Jun 26".

Shape: the solid ChatGPT-User line runs below the dashed previous-7-days line for most of the window with a daily cycle, converging with it on Jun 25–26 — measured-by-us (read off axis, shape only).

Source line: none; year not printed (the page dateline is 2025-07-01).

Text cross-check: text describes the bot-specific page ("metadata about the bot, information on how the bot's user agent is represented in HTTP request headers and how it should be specified in robots.txt directives, and a traffic graph"). No numeric figure in text or on the chart.

## Pull notes — mechanical only

- All twelve PNGs opened and rendered; none truncated. Images 04, 05 and the chart in 12 carry a Max/0 axis only, so no numeric value is readable from them; images 06–10 carry percentage axes, and the "~" values above are eyeballed band positions.

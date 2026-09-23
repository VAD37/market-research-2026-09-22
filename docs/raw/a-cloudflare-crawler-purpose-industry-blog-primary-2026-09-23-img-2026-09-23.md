# Cloudflare — "AI crawler traffic by purpose and industry" (2025-08-28) — image read (IMG-1b)

```yaml
source:          Cloudflare (blog.cloudflare.com; author David Belson) — the eleven in-body images
url_or_doc_id:   https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/
published:       2025-08-28 (page dateline, per source raw file)
pull_date:       2026-09-23
pull_method:     image read (IMG-1b) — Read tool on the PNGs saved by curl in the source pull
pull_purpose:    evidence about a number
tier:            4
tier_reason:     inherits a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23.md
source_label:    analyst-derived (Cloudflare Radar charts; printed percentages are the chart's own); measured-by-us only where a value is read off an axis and marked "~"
lane:            A
sub_market:      n/a
engine:          multiple — OpenAI (GPTBot, ChatGPT-User, OAI-SearchBot), Anthropic (ClaudeBot, Claude-Web), Amazon (Amazonbot), Meta (Meta-ExternalAgent, Meta-ExternalFetcher, FacebookBot), ByteDance (Bytespider, TikTokSpider), Perplexity (PerplexityBot, Perplexity-User), Mistral (MistralAI-User), Apple (Applebot), xAI (Grok) and others as printed
metric_kind:     crawl volume share (HTTP requests by bot and by crawl purpose)
supersedes:      none — reads the images referenced in a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23.md; page text is in a-cloudflare-crawler-purpose-industry-blog-2026-09-22.md
captured:        eleven images, each transcribed below
```

Text cross-check note for the whole file: the page body text is in `a-cloudflare-crawler-purpose-industry-blog-2026-09-22.md` (the substitute); "text" below means that file's verbatim section.

## 01-blog-2893-image-1

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/01-blog-2893-image-1.png (2196 × 444 px)

Chart type: Radar UI screenshot, cropped — "HTTP traffic by bot" line chart (top part only) with the "Crawl purpose" dropdown open.

Title: "HTTP traffic by bot". Subtitle: "HTTP request trends for top five most active AI bots".

Series with printed share: GPTBot 25.1% · ClaudeBot 24.9% · Amazonbot 17.2% · Meta-ExternalAgent 15.3% · Bytespider 6.2%.

Dropdown "Crawl purpose" — options listed: "Training" (highlighted) · "Search" · "User action" · "Undeclared". Selector shows "Select...".

Y axis: "Max" only visible (chart cut off). X axis: not visible. Date range: none printed.

Text cross-check: the text lists the same four purposes ("Training, Search, User action, and Undeclared"). The five percentages are not in the text.

## 02-blog-2893-image-2

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/02-blog-2893-image-2.png (2196 × 824 px)

Chart type: line chart, five series, Radar UI.

Title: "HTTP traffic by bot". Subtitle: "HTTP request trends for top five most active AI bots". Filter chip: "Crawl purpose: User action". Selector reads "User action".

Series with printed share: ChatGPT-User 73.6% · TikTokSpider 24.1% · Perplexity-User 2.2% · MistralAI-User < 0.1% · Meta-ExternalFetcher < 0.1%.

Y axis: "Max" / "0", no intermediate values. X axis ticks: "Tue, Jul 1" · "Sat, Jul 5" · "Wed, Jul 9" · "Sun, Jul 13" · "Thu, Jul 17" · "Mon, Jul 21" · "Fri, Jul 25" (year not printed; text says July 2025).

Shape: ChatGPT-User (dark blue) shows a regular daily cycle whose peaks rise through the month, reaching "Max" around Jul 26–27; TikTokSpider (light blue) runs lower with step-downs around Jul 17 and Jul 23; Perplexity-User (orange) is a flat line near 0 — measured-by-us (read off axis, shape only).

Text cross-check: text says the graph "covers the first 28 days of July 2025. OpenAI's ChatGPT-User bot is responsible for nearly three quarters of the request traffic from this cohort" — chart: 73.6%. Text mentions "Perplexity-User also exhibits a similar pattern" — chart: 2.2%. TikTokSpider 24.1% is not in the text.

## 03-blog-2893-image-3

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/03-blog-2893-image-3.png (2196 × 756 px)

Chart type: line chart, Radar UI, two of four series active.

Title: "Crawl purpose". Subtitle: "Share of traffic by the purpose of the crawl".

Series with printed share: Training 79.5% (greyed out / deselected) · Search 16.5% (greyed out / deselected) · User action 3% (active, orange) · Undeclared 1% (active, olive).

Y axis: "Max" / "0", no intermediate values. X axis ticks: "Tue, Jul 1" · "Sat, Jul 5" · "Wed, Jul 9" · "Sun, Jul 13" · "Thu, Jul 17" · "Mon, Jul 21" · "Fri, Jul 25".

Shape: both active lines show a daily cycle; User action sits in the upper half of the plot, Undeclared in the lower third — measured-by-us (read off axis, shape only).

Text cross-check: text says "Training traffic, responsible for nearly 80% of the crawling from AI bots" — chart: 79.5%. Text says User action and Undeclared "account for less than 5% of AI bot traffic across this time period" — chart: 3% and 1% (printed separately). Search 16.5% is not in the text.

## 04-blog-2893-image-4

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/04-blog-2893-image-4.png (2750 × 1182 px)

Chart type: multi-series line chart with a share bar beneath (Radar Data Explorer).

Title: "AI bots by HTTP traffic time series". Subtitle: "Distribution of HTTP traffic by AI bot over time". Filter chip: "Crawl purpose: Training".

Legend (printed order): GPTBot · Meta-ExternalAgent · ClaudeBot · Bytespider · Applebot · Timpibot · AI2Bot · PanguBot · CCBot · Diffbot · omgili · DigitalOceanGenAICrawler · Cotoyogi · FacebookBot · Grok · Claude-Web.

Y axis: "Requests", "Max" / "0", no intermediate values. X axis ticks: "Tue, Jul 1" · "Sat, Jul 5" · "Wed, Jul 9" · "Sun, Jul 13" · "Thu, Jul 17" · "Mon, Jul 21" · "Fri, Jul 25".

Share bar beneath, labelled segments: "GPTBot 36%" · "ClaudeBot 29%" · "Meta-ExternalAgent 23%" · "Bytespider 7.4%" · "Applebot 4.5%" · unlabelled slivers.

Shape: GPTBot (dark blue) near "Max" through Jul 1–13 with several drops to 0, then declines to about the ClaudeBot level by Jul 21 and below it by Jul 25; ClaudeBot (orange) rises over the month; Meta-ExternalAgent (light blue) mid-range and spiky — measured-by-us (read off axis, shape only).

Source line on image: none. Year not printed.

Text cross-check: the text does not state per-bot shares for the Training purpose; none of the five figures is in the text.

## 05-blog-2893-image-5

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/05-blog-2893-image-5.png (2272 × 728 px)

Chart type: Radar UI screenshot, cropped — "AI bot & crawler traffic" card header, "HTTP traffic by bot" chart (top part), with the "Industry set" dropdown open.

Card title: "AI bot & crawler traffic". Card subtitle: "AI bots scan public websites to collect data used in search engines, AI model training, and other data processing tasks". Chart title: "HTTP traffic by bot" — "HTTP request trends for top five most active AI bots".

Series with printed share: GPTBot 27% · ClaudeBot 23.6% · Meta-ExternalAgent 15.4% · Amazonbot 14.3% · Bytespider 6.4%.

Dropdown "Industry set" — options visible: "Art" · "Business & Industry" · "Computer & Electronics" · "Education" · "Finance" (highlighted) · "Gaming & Gambling" · "Health" · "Internet & Telecom" · "Law & Government" (partly cut off); list scrolls further.

Y axis: "Max" only visible. X axis: not visible. Date range: none printed.

Text cross-check: the text says "select an industry set from the drop-down list at the top right of the card". The five percentages are not in the text.

## 06-blog-2893-image-6

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/06-blog-2893-image-6.png (2230 × 748 px)

Chart type: line chart, five series, Radar UI, no industry set or crawl purpose selected ("Select...").

Title: "HTTP traffic by bot". Subtitle: "HTTP request trends for top five most active AI bots".

Series with printed share: ClaudeBot 27.4% · GPTBot 22.3% · Meta-ExternalAgent 17.2% · Amazonbot 16.4% · Bytespider 6.3%.

Y axis: "Max" / "0", no intermediate values. X axis ticks: "Fri, Aug 1" · "Sat, Aug 2" · "Sun, Aug 3" · "Mon, Aug 4" · "Tue, Aug 5" · "Wed, Aug 6" · "Thu, Aug 7" (year not printed; text says first week of August 2025).

Shape: ClaudeBot (dark blue) top line with a peak to "Max" on Aug 2; GPTBot (light blue) second with short spikes; Meta-ExternalAgent (orange) spiky in the middle band; Amazonbot (olive) middle band; Bytespider (green) flat low — measured-by-us (read off axis, shape only).

Text cross-check: text says "across the first week of August, with no vertical or crawl purpose selected, ClaudeBot and GPTBot account for nearly half of the observed crawling activity, with Meta-ExternalAgent the only one among the top five exhibiting activity that remotely resembles a pattern" — chart: ClaudeBot 27.4%, GPTBot 22.3% (printed separately). The text's ratios for this default view (Anthropic nearly 50,000:1, OpenAI 887:1, Perplexity 118:1) are not on this image.

## 07-blog-2893-image-7

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/07-blog-2893-image-7.png (2272 × 794 px)

Chart type: line chart, five series, Radar UI. Filter chip: "Industry set: News & Publications". Crawl purpose selector: "Select...".

Title: "HTTP traffic by bot". Subtitle: "HTTP request trends for top five most active AI bots".

Series with printed share: GPTBot 17.4% · Meta-ExternalAgent 17.3% · Amazonbot 16.3% · ClaudeBot 15.3% · ChatGPT-User 14.9%.

Y axis: "Max" / "0". X axis ticks: "Fri, Aug 1" · "Sat, Aug 2" · "Sun, Aug 3" · "Mon, Aug 4" · "Tue, Aug 5" · "Wed, Aug 6" · "Thu, Aug 7".

Shape: five interleaved lines in a similar band; ClaudeBot (green) peaks to "Max" on Aug 2; Meta-ExternalAgent (olive) peaks Aug 3 and Aug 6; ChatGPT-User (orange) dips lowest on Aug 6 — measured-by-us (read off axis, shape only).

Text cross-check: text says "ranging from ChatGPT-User's 14.9% share of traffic to GPTBot's 17.4% share" — chart: 14.9% and 17.4% (same). The middle three shares (17.3%, 16.3%, 15.3%) are not in the text. The text's ratios for this set (Anthropic 2,500:1, OpenAI 152:1, Perplexity 32.7:1) are not on the image.

## 08-blog-2893-image-8

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/08-blog-2893-image-8.png (2272 × 794 px)

Chart type: line chart, five series, Radar UI. Filter chip: "Industry set: Computer & Electronics". Crawl purpose selector: "Select...".

Title / subtitle: as 07.

Series with printed share: GPTBot 22.1% · Amazonbot 19.2% · ClaudeBot 13.9% · Meta-ExternalAgent 13.9% · Bytespider 11.2%.

Y axis: "Max" / "0". X axis ticks: "Fri, Aug 1" · … · "Thu, Aug 7" (as 07).

Shape: GPTBot (dark blue) top line most of the week; Amazonbot (light blue) second, one spike to "Max" on Aug 6; ClaudeBot (olive) spike Aug 2; Bytespider (green) lowest — measured-by-us (read off axis, shape only).

Text cross-check: text says "GPTBot was again the most active AI bot, Amazonbot moved up into second place; together these bots now account for over 40% of crawling traffic. ClaudeBot and Meta-ExternalAgent both had a 13.9% share of the crawling traffic, with ByteDance's ByteSpider rounding out the top five" — chart: GPTBot 22.1%, Amazonbot 19.2% (printed separately), ClaudeBot 13.9%, Meta-ExternalAgent 13.9% (same), Bytespider 11.2% (not in text). The text's ratios (Anthropic 8,800:1, OpenAI 401.7:1, Perplexity 88:1) are not on the image.

## 09-blog-2893-image-9

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/09-blog-2893-image-9.png (1600 × 1362 px)

Chart type: multi-series line chart with share bar beneath, Cloudflare Radar export.

Title: "AI bots by HTTP traffic time series". Subtitle: "Distribution of HTTP traffic by AI bot over time". Filter chips: "Vertical: Finance" · "Industry: Cryptocurrency".

Legend (printed order): ClaudeBot · GPTBot · Amazonbot · Meta-ExternalAgent · ChatGPT-User · Bytespider · Applebot · OAI-SearchBot · AI2Bot · CCBot · PerplexityBot · TikTokSpider · Perplexity-User · imgproxy · EchoboxBot · MistralAI-User · Timpibot · omgili · Google-CloudVertexBot · Other.

Y axis: "Requests", "Max" / "0". X axis ticks: "Fri, Aug 1, 00:00" · "Sat, Aug 2, 00:00" · "Sun, Aug 3, 00:00" · "Mon, Aug 4, 00:00" · "Tue, Aug 5, 00:00" · "Wed, Aug 6, 00:00" · "Thu, Aug 7, 00:00".

Share bar beneath, labelled segments: "ClaudeBot 31%" · "GPTBot 24%" · "Meta-ExternalAgent 15%" · "Amazonbot 12%" · unlabelled segments (green, pink, purple, red, and slivers).

Footer printed: "Cloudflare Radar" · "Aug 1, 2025, 00:00 UTC → Aug 7, 2025, 23:45 UTC".

Shape: ClaudeBot (dark blue) top line, peak to "Max" on Aug 2; GPTBot (light blue) second; Meta-ExternalAgent (olive) and Amazonbot (orange) in the middle band; the remainder low — measured-by-us (read off axis, shape only).

Text cross-check: text says for "sites within the Cryptocurrency industry under the Finance vertical … three-quarters of that traffic during the first week of August was concentrated in just four bots" — chart prints ClaudeBot 31%, GPTBot 24%, Meta-ExternalAgent 15%, Amazonbot 12% (separately; not summed here).

## 10-blog-2893-image-10

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/10-blog-2893-image-10.png (1600 × 1238 px)

Chart type: four-series line chart with share bar beneath, Cloudflare Radar export.

Title: "AI bot crawl purposes by HTTP traffic time series". Subtitle: "Distribution of HTTP traffic by AI bot crawl purpose over time". Filter chips: "Vertical: Finance" · "Industry: Cryptocurrency".

Legend: Training · Search · Undeclared · User action.

Y axis: "Requests", "Max" / "0". X axis ticks: "Fri, Aug 1, 00:00" · … · "Thu, Aug 7, 00:00" (as 09).

Share bar beneath, labelled segments: "Training 80%" · "Search 14%" · unlabelled olive segment (User action) · unlabelled sliver (Undeclared).

Footer printed: "Cloudflare Radar" · "Aug 1, 2025, 00:00 UTC → Aug 7, 2025, 23:45 UTC".

Shape: Training (dark blue) occupies the upper part of the plot, touching "Max" on Aug 5; Search (light blue) a low band; User action (olive) below it; Undeclared (orange) flat near 0 — measured-by-us (read off axis, shape only).

Text cross-check: text says "80% of it was for gathering information to train models" — chart: Training 80% (same). Search 14% is not in the text.

## 11-blog-2893-image-11

image: docs/raw/img/a-cloudflare-crawler-purpose-industry-blog-primary-2026-09-23/11-blog-2893-image-11.png (1600 × 1362 px)

Chart type: multi-series line chart with share bar beneath, Cloudflare Radar export.

Title: "AI bots by HTTP traffic time series". Subtitle: "Distribution of HTTP traffic by AI bot over time". Filter chip: "Industry: Computer Games; Gambling & Casinos; Gambling and Casinos; Recreation; Gaming".

Legend (printed order): Meta-ExternalAgent · ClaudeBot · GPTBot · Amazonbot · Applebot · Bytespider · imgproxy · ChatGPT-User · OAI-SearchBot · TikTokSpider · PerplexityBot · CCBot · AI2Bot · iaskspider · PanguBot · Perplexity-User · Timpibot · EchoboxBot · MistralAI-User · Other.

Y axis: "Requests", "Max" / "0". X axis ticks: "Fri, Aug 1, 00:00" · … · "Thu, Aug 7, 00:00" (as 09).

Share bar beneath, labelled segments: "Meta-ExternalAgent 30%" · "ClaudeBot 28%" · "Amazonbot 16%" · "GPTBot 15%" · unlabelled segments (pink, purple, green, red, slivers).

Footer printed: "Cloudflare Radar" · "Aug 1, 2025, 00:00 UTC → Aug 7, 2025, 23:45 UTC".

Shape: Meta-ExternalAgent (dark blue) spiky with peaks to "Max" on Aug 4 and Aug 5; ClaudeBot (light blue) smoother, second; GPTBot (orange) and Amazonbot (olive) interleaved in the middle band; Bytespider (pink) low — measured-by-us (read off axis, shape only).

Text cross-check: the text does not name a Gaming industry example; none of the four figures is in the text. (Text says clicking through from a curated Industry set "will pre-populate the Industry selector with the relevant entries", which matches the multi-entry chip.)

## Pull notes — mechanical only

- All eleven PNGs opened and rendered. Images 01 and 05 are cropped UI screenshots (chart bodies cut off). All charts carry a Max/0 y-axis only, so no line value is readable; the figures recorded are the percentages printed in legends and share bars.

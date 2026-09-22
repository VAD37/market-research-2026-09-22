# Cloudflare Blog — "The crawl before the fall... of referrals" (crawl-to-refer ratio launch post)

```yaml
source:          Cloudflare Blog (David Belson and Sam Rhea)
url_or_doc_id:   https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar/
published:       2025-07-01 (dateline "JULY 1, 2025" on page)
pull_date:       2026-09-22
pull_method:     fetch (browser extension used for chart/table capture; article text loaded on plain navigation)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default per channels.md C27 — telemetry with method disclosed in the same post (denominator/numerator defined, population stated)
source_label:    analyst-derived
lane:            A
sub_market:      n/a
engine:          multiple — Anthropic (Claude), OpenAI, Perplexity, Microsoft, Yandex, Google, ByteDance, Baidu, DuckDuckGo, Mistral (all named in the ratio table)
metric_kind:     traffic
supersedes:      none
captured:        full page, plus the embedded "Crawl-to-refer ratio" widget captured by screenshot/zoom (widget renders live current data, not the article's static June 2025 example — see pull notes)
note:            source crosses metrics — recorded as traffic. The crawl-to-refer ratio's numerator (HTML crawl requests) is explicitly NOT traffic per glossary.md ("Is NOT: ... Crawler or bot requests from an AI vendor's crawler"); its denominator (HTML requests carrying a Referer header naming the platform) IS traffic per glossary.md's definition ("session on the brand's own property whose referrer is an AI surface"). The ratio itself is a distinct diagnostic metric Cloudflare defines and names "crawl-to-refer ratio" — recorded here as its own thing, not folded into visibility, traffic, or sales. Cloudflare's own words on the crossing risk: "we've found that very few users actually click through relative to how often the AI bot scrapes a given website."
```

## Verbatim

Title: "The crawl before the fall… of referrals: understanding AI's impact on content providers"
Byline: David Belson and Sam Rhea. Tags: AI, Bots, Internet Traffic, Pay Per Crawl, Radar. Dateline: JULY 1, 2025. "8 MINUTE READ."

"Content publishers welcomed crawlers and bots from search engines because they helped drive traffic to their sites. The crawlers would see what was published on the site and surface that material to users searching for it. Site owners could monetize their material because those users still needed to click through to the page to access anything beyond a short title.

Artificial Intelligence (AI) bots also crawl the content of a site, but with an entirely different delivery model. These Large Language Models (LLMs) do their best to read the web to train a system that can repackage that content for the user, without the user ever needing to visit the original publication.

The AI applications might still try to cite the content, but we've found that very few users actually click through relative to how often the AI bot scrapes a given website. We have discussed this challenge in smaller settings, and today we are excited to publish our findings as a new metric shown on the AI Insights page on Cloudflare Radar.

Visitors to Cloudflare Radar can now review how often a given AI model sends traffic to a site relative to how often it crawls that site."

**How does this measurement work?**

"As HTML pages are arguably the most valuable content for these crawlers, the ratios displayed are calculated by dividing the total number of requests from relevant user agents associated with a given search or AI platform where the response was of `Content-type: text/html` by the total number of requests for HTML content where the `Referer` header contained a hostname associated with a given search or AI platform."

"The diagrams below illustrate two common crawling scenarios, and show that companies may use different user agents depending on the purpose of the crawler. The top one represents a simple transaction where the example AI platform is requesting content for the purposes of training an LLM, representing itself as `AIBot`. The bottom one represents a scenario where the example AI platform is requesting content to service a user request — looking for flight information, for example. In this case, it is representing itself as `AIBot-User`. Request traffic from both of these user agents would be aggregated under a single platform name for the purposes of our analysis."

"When a user clicks on a link on a website or application, the client will often send a `Referer:` header as part of the request to the target site... Hostnames are associated with their respective platforms for the purpose of our analysis."

**Observations — Reviewing the ratios**

"The new metric is presented as a simple table, comparing the number of aggregate HTML page requests from crawlers (user agents) associated with a given platform to the number of HTML page requests from clients referred by a hostname associated with a given platform. The calculated ratio is always normalized to a single referral request.

The table below shows that for the period June 19-26, 2025, as an example, the ratios range from Anthropic's 70,900:1 down to Mistral's 0.1:1. This means that Anthropic's AI platform Claude made nearly 71,000 HTML page requests for every HTML page referral, while Mistral sent 10x as many referrals as crawl requests. (However, traffic referred by Claude's native app does not include a `Referer:` header, and we believe that the same holds true for traffic generated from other native apps as well. As such, because the referral counts only include traffic from the Web-based tools from these providers, these calculations may overstate the respective ratios, but it is unclear by how much.)

Of course, due in part to changes in crawling patterns, these ratios will change over time. The table above also displays the ratio changes as compared to the previous period, with changes ranging from increases of over 6% for DuckDuckGo and Yandex to Google's 19.4% decrease. The week-over-week drop in Google's ratio is related to an observed drop in crawling traffic from GoogleBot starting on June 24, while Yandex's week-over-week growth is related to an observed increase in YandexBot crawling activity that started on June 21."

**"Crawl-to-refer ratio" embedded widget, captured live at pull time 2026-09-22** (this widget renders Radar's current default period, not the article's static June 2025 numbers — see pull notes for the discrepancy):

| Platform | Ratio | Change vs. prior period | User-agent breakdown |
|---|---|---|---|
| Anthropic | 70.9K : 1 | ↓ -5.7% | ClaudeBot 100% (bar), Claude-SearchBot <0.1%, Claude-User <0.1% |
| OpenAI | 1.6K : 1 | ↓ -13.1% | GPTBot 94.2%, ChatGPT-User 3.7%, OAI-SearchBot 2.1% |
| Perplexity | 202.4 : 1 | ↓ -3.6% | PerplexityBot 85.1%, Perplexity-User 14.9% |
| Microsoft | 40 : 1 | ↓ -4.4% | Bingbot 100% |
| Yandex | 18 : 1 | ↑ +6.4% | YandexBot 99.4%, YandexMobileBot 0.3%, YandexImages 0.3%, Other <0.1% |
| Google | 9.4 : 1 | ↓ -19.4% | Googlebot 92.7%, GoogleOther 6.5%, Googlebot-Mobile 0.4%, Other 0.4% |
| ByteDance | 1.4 : 1 | ↓ -7.8% | Bytespider 100% |
| Baidu | 1 : 1 | ↓ -17.2% | Baiduspider 100% |
| DuckDuckGo | 0.3 : 1 | ↑ +6.8% | DuckDuckBot 66.7%, DuckAssistBot 33.3% |
| Mistral | 0.1 : 1 | ≈ 0% | MistralAI-User 100% |

**Patterns in referral traffic** — "Changes and trends in the underlying activity can be seen in the associated Data Explorer view, as well as in the raw data available via API endpoints (timeseries, summary). Note that the shares of both referral and crawl traffic are relative to the sets of referrers and crawlers included in the graphs, and not Cloudflare traffic overall. For example, in the referrer-centric view below, covering nearly the first four weeks of June 2025, we can see that referral traffic is dominated by search platform Google, with a fairly consistent diurnal pattern visible in the data... Because of prefetching driven by the use of speculation rules, referral traffic coming from Google's ASN (AS15169) is specifically excluded from analysis here, as it doesn't represent active user consumption of content. Clear diurnal patterns are also visible in the referral request shares of other search platforms, although the request shares are a fraction of what is seen from Google. Throughout June, the share of traffic referred by AI platforms was significantly lower, even in aggregate, than the share of traffic referred by search platforms."

**Changes in crawling traffic** — "In the crawler-centric view below, covering nearly the first four weeks of June 2025, we can see that the share of requests related to Google's crawling activity for both their Googlebot and GoogleOther identifiers falls over the course of the month, with several peak/valley periods. A similar pattern observed in HTTP request traffic from Google's AS15169 during that same time period loosely matches this observed drop in share. In addition, it appears that OpenAI's GPTBot saw multiple periods where little-to-no crawling activity was observed throughout the month."

**What this means for content providers** — "These ratios directly impact the viability of content publication on the Internet. While they will vary over time, the trend continues to be more crawls and fewer referrals when compared in relation to each other. Legacy search index crawlers would scan your content a couple of times, or less, for each visitor sent. A site's availability to crawlers made their revenue model more viable, not less. The new data we are observing suggests that is no longer the case. These models continue to consume more content, more frequently, despite sending the same or less traffic to the source of its content."

"We have released new tools over the last year to help site owners take control back. With a single click, publishers can block the kinds of AI crawlers that train against their content... However, we continue to recommend that content creators audit and then enforce their preferred policies for AI crawlers."

**One more thing…** — "we've also taken the opportunity to launch expanded Verified Bots content. The Bots page on Cloudflare Radar includes a paginated list of Verified Bots, displaying the bot name, owner, category, and rank (based on request volume)... Clicking on a bot name within a card brings up a bot-specific page that includes metadata about the bot, information on how the bot's user agent is represented in HTTP request headers and how it should be specified in robots.txt directives, and a traffic graph that shows associated HTTP request volume trends for the selected time period."

## Pull notes — mechanical only

- Article text captured via `get_page_text` on plain navigation (loaded without a 403 in this session, contrary to `channels.md` C27's "200" expectation being confirmed, not contested).
- The embedded "Crawl-to-refer ratio" table did **not** render as extractable text (`get_page_text` skipped it — it is a client-side chart/table widget); captured instead via screenshot + zoom. This widget is **live** and reflects Radar's current query window at pull time (2026-09-22), not the article's own worked example of "June 19-26, 2025" — the two sets of figures for Anthropic and Mistral differ (article: Anthropic 70,900:1, Mistral 0.1:1 for June 2025; live widget at pull time: Anthropic 70.9K:1, Mistral 0.1:1 — coincidentally close for these two, but the live widget also names five more platforms not in the article's two-name example, and the live widget's window is not independently labeled with a date range on this page — see `a-cloudflare-radar-ai-insights-2026-09-22.md` for a dated "Last 7 days" pull of the same live widget from `radar.cloudflare.com/ai-insights` directly).
- **Stale per query-book.md date rule**: published 2025-07-01 (or possibly a mislabeled/retained 2025 dateline — page literally reads "JULY 1, 2025"), more than one quarter before this 2026-09-22 pull date. Flagged `stale — published 2025-07-01`. Re-checked against the current page at pull time: the live embedded widget (see above) supersedes the article's static numeric example as of 2026-09-22, and is captured separately in `a-cloudflare-radar-ai-insights-2026-09-22.md`.
- No login wall, no truncation. Time-series charts illustrating "Patterns in referral traffic" and "Changes in crawling traffic" are rendered as images/interactive charts, not captured as data — only the prose describing them is captured above [note: referrer-centric and crawler-centric June-2025 timeseries charts are images, not captured as data].

# Cloudflare Blog — "A deeper look at AI crawlers: breaking down traffic by purpose and industry"

```yaml
source:          Cloudflare Blog (David Belson)
url_or_doc_id:   https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/
published:       2025-08-28 (dateline "AUGUST 28, 2025" on page)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default per channels.md C27 — telemetry with method disclosed (crawl purpose taxonomy and industry-set definition given inline)
source_label:    analyst-derived
lane:            A
sub_market:      n/a
engine:          multiple — Anthropic (Claude), OpenAI, Perplexity, and others named per industry-set example
metric_kind:     traffic
supersedes:      none
captured:        full page (embedded charts described in prose only, not captured as data — see pull notes)
note:            source crosses metrics — recorded as traffic. Same crossing as the companion post: crawl-to-refer ratios mix crawl volume (not traffic) with referral volume (traffic). This post additionally reports "Training traffic, responsible for nearly 80% of the crawling from AI bots" — a crawl-purpose share, which is crawl volume, not traffic; recorded as crawl volume, not folded into the traffic label above. Quoted verbatim below.
```

## Verbatim

Title: "A deeper look at AI crawlers: breaking down traffic by purpose and industry"
Byline: David Belson. Tags: AI, AI Week, Bots, Radar, Traffic. Dateline: AUGUST 28, 2025. "8 MINUTE READ."

"Search platforms historically crawled web sites with the implicit promise that, as the sites showed up in the results for relevant searches, they would send traffic on to those sites — in turn leading to ad revenue for the publisher... However, the emergence of AI platforms over the last several years, and the incorporation of AI "overviews" into classic search platforms, has turned the model on its head. When users turn to these AI platforms with queries that used to go to search engines, they often won't click through to the original source site once an answer is provided — and that assumes that a link to the source is provided at all! No clickthrough, no eyeballs, and no ad revenue."

"To provide a perspective on the scope of this problem, Radar launched crawl/refer ratios on July 1, based on traffic seen across our whole customer base. These ratios effectively compare the number of crawling requests for HTML pages from the crawler associated with a given platform, to the number of HTML page requests referred by that platform (measuring human traffic). This data complements insights into AI bot & crawler traffic trends that were launched during Birthday Week 2024."

"Today, we're adding two new capabilities to the AI Insights page on Cloudflare Radar to give you more insight into this activity: industry-focused AI bot traffic data, and a new breakdown of AI bot traffic by its purpose."

**Traffic by type**

"Since the launch of LLMs into the public consciousness in November 2022, much of the crawling traffic seen from user agents associated with AI platforms has been to collect content used to train AI models. This crawling activity can be aggressive at times, often ignoring directives found in robots.txt files. In addition to offering chatbots trained on this scraped content, AI platforms have emerged that aim to replace classic search tools, while those tools have themselves integrated AI-powered summaries as part of their results. These platforms may crawl your site to build indexes for their search engines. And some AI platforms may crawl your site in response to a specific user prompt, such as looking for flights to plan a vacation."

"The new Crawl purpose selector within the AI bot & crawler traffic card allows users to select between Training, Search, User action, and Undeclared. (The latter is for crawlers where no information is available from the operator or other industry sources regarding its purpose.)"

"Once a purpose is selected, the HTTP traffic by bot graph updates to show traffic trends over the selected time period for the top five most active AI bots that crawl for the selected purpose. As an example, selecting User action results in a graph like the one below, which covers the first 28 days of July 2025. OpenAI's ChatGPT-User bot is responsible for nearly three quarters of the request traffic from this cohort of crawlers. A daily cycle is clearly evident, suggesting regular usage of ChatGPT in that fashion, with such usage gradually increasing throughout the month. If ChatGPT-User is removed from the chart, Perplexity-User also exhibits a similar pattern."

"A new Crawl purpose graph has also been added to Radar, breaking out traffic trends by purpose. **Training traffic, responsible for nearly 80% of the crawling from AI bots**, is somewhat erratic in nature, with no clear cyclical pattern. However, such patterns are visible for the User action and Undeclared purposes, as shown in the graph below, although they account for less than 5% of AI bot traffic across this time period."

"Within the Data Explorer view for the AI Bots & Crawlers dataset, you can now break the data down by Crawl purpose to explore how the activity has changed over time. Alternatively, you can break the data down by User agent, and filter by Crawl purpose, to explore traffic trends across a larger set of bots (beyond the top five). Comparisons with previous time periods are available here as well."

**Visibility by industry**

"You can use your own traffic data to see how aggressively crawlers scrape your content. You can also see how frequently they refer traffic back to you. However, you may also want to understand how those measurements compare with your peer group — are you being crawled more or less frequently, and are the platforms referring more or less traffic back to your sites? The new industry set filtering available for the HTTP traffic by bot graph and the Crawl-to-refer ratio table in the AI Insights section of Radar can provide you with this perspective."

"Within the AI bot & crawler traffic card on the AI Insights page, select an industry set from the drop-down list at the top right of the card. The graphs in the HTTP traffic by bot and Crawl purpose sections of the card update to reflect the selection, as does the Crawl-to-refer ratio table."

"It is interesting to observe how the crawling patterns change between industry sets, along with the mix of most active bots and crawl-to-refer ratios. For example, across the first week of August, with no vertical or crawl purpose selected, ClaudeBot and GPTBot account for nearly half of the observed crawling activity, with Meta-ExternalAgent the only one among the top five exhibiting activity that remotely resembles a pattern. **For the default view, Anthropic had the highest crawl-to-refer ratio at nearly 50,000:1, followed by OpenAI at 887:1 and Perplexity at 118:1.**"

"However, when the News and Publications industry set is selected, we see a much tighter distribution of traffic among the top five, ranging from ChatGPT-User's 14.9% share of traffic to GPTBot's 17.4% share. ChatGPT-User's presence among the top five suggests that a significant number of users may have been asking questions about current events during that period of time. **For these News and Publications sites, the crawl-to-refer ratios are lower than the default view, with Anthropic at 2,500:1, OpenAI at 152:1, and Perplexity at 32.7:1.**"

"As a third example, we find that the mix again shifts for the Computer and Electronics industry set. While GPTBot was again the most active AI bot, Amazonbot moved up into second place; together these bots now account for over 40% of crawling traffic. ClaudeBot and Meta-ExternalAgent both had a 13.9% share of the crawling traffic, with ByteDance's ByteSpider rounding out the top five. **The crawl-to-refer ratios for this vertical are again lower than for the unfiltered view, with Anthropic down to 8,800:1, OpenAI at 401.7:1, and Perplexity at 88:1.**"

"Within Data Explorer, you can now break down AI Bots & Crawler data by Vertical and Industry. (A vertical is a pre-defined collection of multiple related industries), and you can also filter Crawl purpose and User agent breakdowns by Vertical and Industry. For example, the graphs below illustrate the traffic trends by AI crawler for sites within the Cryptocurrency industry under the Finance vertical, as well as the traffic trends by crawl purpose for that industry/vertical pair. While these sites see crawling traffic from quite a few bots, three-quarters of that traffic during the first week of August was concentrated in just four bots, and 80% of it was for gathering information to train models."

"Because the Industry sets shown on the main AI Insights page are manually curated collections of related industries, clicking through to the Data Explorer view from one of those graphs will pre-populate the Industry selector with the relevant entries."

**Conclusion** — "AI crawler traffic has become a fact of life for content owners, and the complexity of dealing with it has increased as bots are used for purposes beyond LLM training. Work is underway to allow website publishers to declare how automated systems should use their content. However, it will take some time for these proposed solutions to be standardized, and for both publishers and crawlers to adopt them. As the space evolves, we'll continue to expand Cloudflare Radar's insights into AI crawler activity."

## Pull notes — mechanical only

- Fetched by plain navigation; no 403, no login wall, article text loaded in full via `get_page_text`.
- **Stale per query-book.md date rule**: published 2025-08-28, more than one quarter before this 2026-09-22 pull. Flagged `stale — published 2025-08-28`. This post's own crawl-to-refer figures (Anthropic ~50,000:1 default / 2,500:1 News&Pubs / 8,800:1 Computer&Electronics, "first week of August" 2025) are superseded by the live figures captured directly from Radar at pull time in `a-cloudflare-radar-ai-insights-2026-09-22.md` (default "Last 7 days" as of 2026-09-22: Anthropic 581.7:1; News & Publications: Anthropic 11.7K:1) — both sets are kept side by side, never averaged, per root `CLAUDE.md`.
- Embedded charts (the "User action" bot-share graph, the "Crawl purpose" stacked-area graph, the Cryptocurrency-industry examples) are images/interactive widgets on this post and were not separately screenshotted — the article's own prose descriptions of them are captured verbatim above [note: illustrative charts for "User action" crawl purpose and the Cryptocurrency/Finance vertical example are images, not captured as data].
- This post is the source for the crawl-purpose taxonomy (Training / Search / User action / Undeclared) that Radar's live "Crawl purpose" card (captured in the Radar pull) also uses, confirming continuity of definition between the 2025 post and the 2026-09-22 live product.

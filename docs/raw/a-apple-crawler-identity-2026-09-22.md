# Apple Support — crawler identity (Applebot, Applebot-Extended) — surfaced, not on the priority engine matrix

```yaml
source:          Apple Support
url_or_doc_id:   https://support.apple.com/en-us/119829
published:       2026-09-04 ("Published Date: September 04, 2026", stated at foot of page)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own crawler documentation
source_label:    company-stated
lane:            A
sub_market:      n/a
engine:          Apple (not on plan.md's priority-1/2/3/4 engine matrix; pulled because Applebot surfaced at 9.3% share of top-5 AI-bot HTTP traffic on Cloudflare Radar AI Insights, default industry view, "Last 7 days" as of this pull date — see a-cloudflare-radar-ai-insights-2026-09-22.md)
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Title: "About Applebot - Apple Support"

"The data crawled by Applebot is used to power various features, such as the search technology integrated into many user experiences in Apple's ecosystem including Spotlight, Siri, and Safari. Enabling Applebot in robots.txt allows website content to appear in search results for Apple users around the world in these products."

"The data crawled by Applebot may also be used to help train Apple foundation models powering generative AI features across Apple products, including Apple Intelligence, Services, and Developer Tools. Web publishers can opt-out from having their content used to train generative foundation models by disallowing Applebot-Extended in the robots.txt file."

"Applebot crawled data may be used to provide additional context and up-to-date content when AI models are used to generate output for display in Apple products and services. For example, answering broad world knowledge questions in Siri and Search that may include links to sources and websites used to help generate the answer. Web publishers can opt out of their content being used in these broad world knowledge answers by applying the nosnippet meta tag to specific content."

"Even if you disallow Applebot-Extended and tag website content with the nosnippet meta tag, your website instructions may still allow Applebot to crawl your webpages. Your content will remain discoverable through Spotlight, Siri, and Safari, as well as other system-wide features on Apple devices."

**Identifying Applebot** — "Traffic coming from Applebot is generally identified by using reverse DNS in the *.applebot.apple.com domain." Example: `host 17-58-101-179.applebot.apple.com` → `17.58.101.179`. Reverse check: `host 17.58.101.179` → `179.101.58.17.in-addr.arpa domain name pointer 17-58-101-179.applebot.apple.com`. Also identifiable via IP CIDR match against the published "Applebot IP CIDRs" JSON file.

**User agents** — "Applebot powers several user agents, including Search and Podcasts."

Search format: `Mozilla/5.0 (Device; OS_version) AppleWebKit/WebKit_version (KHTML, like Gecko)Version/Safari_version [Mobile/Mobile_version] Safari/WebKit_version (Applebot/Applebot_version; +http://www.apple.com/go/applebot)`

Desktop example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)`

Mobile example: `Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1 (Applebot/0.1; +http://www.apple.com/go/applebot)`

**Special crawlers — Apple online properties** — "iTMS traffic may come from applebot.apple.com hosts, and will be identified by the following user agent: User-Agent: iTMS. The iTMS user agent does not follow robots.txt, as it is not a general search crawler. The iTMS user agent only crawls URLs associated with registered content on Apple Podcasts."

**Customizing robot.txt rules** — Applebot respects standard robots.txt directives. Example given:
```
User-agent: Applebot
Allow: /
Disallow: /private/
Disallow: /not-allowed/
User-agent: *
Disallow: /not-allowed/
```
"If robots instructions don't mention Applebot but mention Googlebot, the Apple robot will follow Googlebot instructions. Applebot does not follow crawl-delay." "Applebot is engineered for efficiency and will adjust to minimize the impact on site owners... to avoid overloading site servers, Applebot's crawl rate adjusts automatically when a site slows down or returns errors. Apple also caches crawled content to reduce unnecessary crawling."

**Customizing indexing rules for Applebot** — supports standard robots meta tags (`noindex`, `nosnippet`, `nofollow`, `none`, `all`) and the `X-Robots-Tag` HTTP header, e.g. `X-Robots-Tag: applebot: nosnippet`. "nosnippet: Applebot won't generate a description or web answer for the page... Apple will not use data tagged nosnippet as additional context and up-to-date content when AI models are used to generate output for display in Apple products and services."

**Marking paywalled content** — supports schema.org `isAccessibleForFree` in page-level JSON-LD structured data. "Pages marked isAccessibleForFree: false are eligible to appear in search results, but Applebot will not use that content as additional context when AI models are used to generate output... Section-level markup using hasPart is not supported. To opt out of having your content used to train Apple's foundation models, use Applebot-Extended described in the next section."

**Applebot-Extended and controlling data usage** — "In addition to following all robots.txt rules and directives, Apple has a secondary user agent, Applebot-Extended, that gives web publishers additional controls over how their website content can be used by Apple. With Applebot-Extended, web publishers can choose to opt out of their website content being used to train Apple's general purpose foundation models powering generative AI features across Apple products, including Apple Intelligence, Services, and Developer Tools." Example rule: `User-agent: Applebot-Extended` / `Disallow: /private/`. "Applebot-Extended does not crawl webpages. Webpages that disallow Applebot-Extended can still be included in search results. Applebot-Extended is only used to determine how to use the data crawled by the Applebot user agent. Allowing Applebot-Extended will help improve the capabilities and quality of Apple's generative AI models over time."

**About search rankings** — factors: "Aggregated user engagement with search results; Relevancy and matching of search terms to webpage topics and content; Number and quality of links from other pages on the web; User location based signals (approximate data); Webpage design characteristics." "Search results may use the factors above with no (pre-determined) importance of ranking... Site rules for Applebot-Extended are not considered in ranking for Search."

"Published Date: September 04, 2026"

## Pull notes — mechanical only

- Reached via `WebSearch` (query: `Applebot-Extended crawler documentation support.apple.com AI training`) since `support.apple.com` is not a channel named in `channels.md` for this cluster — pulled anyway because Applebot appeared at 9.3% share on Cloudflare Radar's live "HTTP traffic by bot" card during the P2-c2 radar pull, and the task brief names "Apple if surfaced." Recorded as an addition beyond the fixed shortlist pull list, per `shortlist.md`'s "every cluster's pull list is a floor, not a ceiling" caveat.
- Fetched via Chrome extension; loaded on first navigation.
- Applebot is Apple's only web crawler naming three functions (search/Siri/Spotlight indexing, generative-model training via the Applebot-Extended token, and "additional context" grounding governed by the `nosnippet` tag) — a three-way split structurally similar to OpenAI's, Anthropic's and Amazon's, but Apple's training-opt-out (`Applebot-Extended`) rides on the **same** crawl as the search-indexing use (Applebot itself), rather than being a separately-crawling bot: "Applebot-Extended does not crawl webpages... it is only used to determine how to use the data crawled by the Applebot user agent."
- Apple is not named anywhere in `plan.md`'s engine matrix (priority 1-4) or in `docs/sources/channels.md`'s platform-primary rows. This pull does not add Apple to the engine matrix — that reweight is `P2-c1`'s / `P2-reweight`'s call, not this cluster's.

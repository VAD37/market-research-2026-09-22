# Google Search Central — crawler docs (common crawlers)

```yaml
source:          Google for Developers — Google Crawling Infrastructure
url_or_doc_id:   https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers -> resolved to https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers
published:       undated — no date on page (Google Search Central docs do not carry a byline date; page is continuously maintained per channels.md C8 "Continuous" refresh)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own crawler documentation
source_label:    company-stated
lane:            A
sub_market:      n/a
engine:          Google — AI Overviews, AI Mode, Gemini (crawler infrastructure is shared across Google Search and Gemini grounding; page does not name a model version)
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Title: "Google's common crawlers | Google Crawling Infrastructure | Crawling infrastructure | Google for Developers"

Google's common crawlers are used to find information for building Google's search indexes, perform other product specific crawls, and for analysis. They always obey robots.txt rules when crawling automatically. The general technical properties of Google's crawlers also apply to the common crawlers.

The common crawlers generally crawl from the IP ranges published in the common-crawlers.json object, and the reverse DNS mask of their hostname matches `crawl-***-***-***-***.googlebot.com` or `geo-crawl-***-***-***-***.geo.googlebot.com`.

The following list shows the common crawlers, their user agent strings as they appear in the HTTP requests, their user agent tokens for the `User-agent:` line in robots.txt, and the products that are affected by crawl preferences for the crawler. Some crawlers have more than one user agent token; you need to match only one crawler token for a rule to apply. The list is not exhaustive, it only covers the requestors that are more likely to show up in log files and that we've received questions about.

Caution: The HTTP user agent string can be spoofed. Learn how to verify if a visitor is a Google crawler.

**Googlebot**
- User-Agent (Smartphone): `Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`
- User-Agent (Desktop): `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36`
- Rarely: `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`; `Googlebot/2.1 (+http://www.google.com/bot.html)`
- robots.txt token: `Googlebot`
- Affected products: Crawling preferences addressed to the Googlebot user agent affect Google Search (including Discover and all Google Search features), as well as other products such as Google Images, Google Video, Google News, and Discover.

**Googlebot Image** — `Googlebot-Image/1.0`; token `Googlebot-Image`; affects Google Images, Discover, Google Video, and all features in Google Search where images, logos, and favicons are presented.

**Googlebot Video** — `Googlebot-Video/1.0`; token `Googlebot-Video`; affects video-related Google Search features and other products dependent on videos.

**Googlebot News** — no separate HTTP user agent string, crawls with various Googlebot strings; token `Googlebot-News`; affects the Google News product, including news.google.com and the Google News app.

**Google StoreBot** — Desktop: `Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Safari/537.36`; Mobile: `Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36`; token `Storebot-Google`; affects all surfaces of Google Shopping (for example, the Shopping tab in Google Search and Google Shopping).

**Google-InspectionTool** — Desktop: `Mozilla/5.0 (compatible; Google-InspectionTool/1.0)`; Mobile variant given; token `Google-InspectionTool`; affects Search testing tools such as the Rich Result Test and URL inspection in Search Console. "It has no effect on Google Search or other products."

**GoogleOther** — `Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; GoogleOther)` and a desktop equivalent; token `GoogleOther`; "Crawling preferences addressed to the GoogleOther user agent don't affect any specific product. GoogleOther is the generic crawler that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development."

**GoogleOther-Image** — `GoogleOther-Image/1.0`; token `GoogleOther-Image`; same non-product-specific framing as GoogleOther, optimized for image URLs.

**GoogleOther-Video** — `GoogleOther-Video/1.0`; token `GoogleOther-Video`; same framing, optimized for video URLs.

**Google-CloudVertexBot** — User-Agent substring `Google-CloudVertexBot`; token `Google-CloudVertexBot`; "Crawling preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by the site owners' for building Vertex AI Agents. It has no effect on Google Search or other products."

**Google-Extended** — no separate HTTP request user agent string; crawling is done with existing Google user agent strings, the robots.txt token is control-only. Token `Google-Extended`. Affected products: "Google-Extended is a standalone product token that web publishers can use to manage whether content Google crawls from their sites may be used for training future generations of Gemini models that power Gemini Apps and Vertex AI API for Gemini and for grounding (providing content from the Google Search index to the model at prompt time to improve factuality and relevancy) in Gemini Apps and Grounding with Google Search on Vertex AI. Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search."

"A note about Chrome/W.X.Y.Z in user agents — The string Chrome/W.X.Y.Z in the user agent strings in the list is a placeholder that represents the version of the Chrome browser used by that user agent: for example, 41.0.2272.96. This version number increases over time to match the latest Chromium release version used by Googlebot. If you are searching your logs or filtering your server for a user agent with this pattern, use wildcards for the version number rather than specifying an exact version number."

## Pull notes — mechanical only

- Navigated to `developers.google.com/search/docs/crawling-indexing/google-common-crawlers` per shortlist; browser resolved to canonical `developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers`. Same content, recorded per the pull-list substitution rule.
- Fetched via Chrome extension; loaded on first navigation.
- **Google-Extended is the crawler token most directly relevant to H1/H13 context**: it is the one Google-named mechanism a site can use to separate "in Google Search" from "used for Gemini training/grounding" — no separate HTTP identity, robots.txt-only control.
- No crawl-volume, crawl-to-refer, or traffic-share figures on this page — identity and policy only.

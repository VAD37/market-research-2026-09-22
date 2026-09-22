# Bing Webmaster Tools — crawler identity (Bingbot, and Copilot's absence as a separate token)

```yaml
source:          Bing Webmaster Tools (Microsoft)
url_or_doc_id:   https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own crawler documentation
source_label:    company-stated
lane:            A
sub_market:      n/a
engine:          Microsoft Copilot (priority-2) — page is Bing's crawler doc; no separate Copilot-named crawler appears on it (see pull notes)
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Title: "Which Crawlers Does Bing Use? - Bing Webmaster Tools"

"Overview of Bing crawlers (user agents). Bing operates the following main crawlers today:"

**Crawler table:**

| Crawler | Role | User agent string(s) |
|---|---|---|
| Bingbot | "Bingbot is our standard crawler and handles most of our crawling needs each day. Bingbot uses different types of user agent strings." | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/W.X.Y.Z Safari/537.36`; `Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) W.X.Y.Z Safari/537.36`; `Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)". "We regularly update our web page rendering engine to the most recent stable version of Microsoft Edge. Thus, "W.X.Y.Z" will be substituted with the latest Microsoft Edge version we are using, for example "80.0.345.0"." |
| AdIdxBot | "AdIdxBot is the crawler used by Bing Ads. AdIdxBot crawls ads and follows the websites from those ads for quality control. Just like Bingbot, AdIdxBot has both "desktop" and "mobile" variants." | `Mozilla/5.0 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)`; iPhone and Windows Phone variants also given. |
| BingPreview | "BingPreview generates page snapshots for Bing." Desktop and mobile variants. | Same format as Bingbot strings, with `bingbot/2.0` token. |
| MicrosoftPreview | "MicrosoftPreview generates page snapshots for Microsoft products." Desktop and mobile variants. | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MicrosoftPreview/2.0; +https://aka.ms/MicrosoftPreview) Chrome/W.X.Y.Z Safari/537.36` and mobile equivalent. |
| BingVideoPreview | "BingVideoPreview is a crawler used by Microsoft to provide previews of videos only in Bing." Desktop and mobile variants. | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; BingVideoPreview/1.0; +https://aka.ms/microsoftbots) Chrome/W.X.Y.Z Safari/537.36` and mobile/compact equivalents. |

"Verifying authenticity — You can identify Bing crawlers with the user agent string. But user agent strings are easy to spoof, so not every request with these user agent strings may be coming from a real Bing crawler. To determine if a request is from a Bing crawler, look for the user agent string, but keep in mind that user agent strings can be faked. To ensure the IP is authentic, use the Verify Bingbot tool or learn about all verification methods we offer."

"Controlling crawl and crawl rates — To control how our crawlers interact with your website, you have two options: Robots.txt files can be configured to tell Bing crawlers how to interact with your website. Bing Webmaster Tools allow you to control crawl rates by the hour using the Crawl control tool."

"Reporting problems — If you notice crawl issues with Bingbot or any of our other crawlers, follow the steps outlined in How to report an issue with Bingbot."

## Pull notes — mechanical only

- Navigated directly (`bing.com/webmasters/help/...`); loaded via Chrome extension on first navigation, no redirect.
- **No user agent named "Copilot" appears on this page.** Five crawlers are listed: Bingbot, AdIdxBot, BingPreview, MicrosoftPreview, BingVideoPreview. This is recorded as the engine's own page naming no separate Copilot crawler token, not as proof one does not exist elsewhere — `unknown — checked https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0 2026-09-22` for a distinct "Copilot" identity token. A secondary (non-platform-primary) source found by `WebSearch` during this pull states Copilot answers are grounded in the Bing index that Bingbot builds, rather than via a separate declared crawler — recorded here as an unverified secondary claim, not pulled as a raw file, and not used as the tier-3 answer.
- No crawl-volume or crawl-to-refer figures on this page — identity and policy only. Cloudflare's crawl-to-refer figures below list the aggregate platform as "Microsoft" (Bingbot at 100% share of the counted user agents in every period captured), consistent with this page naming Bingbot as the crawler that "handles most of our crawling needs."

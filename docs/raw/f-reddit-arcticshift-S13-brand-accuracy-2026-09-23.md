# Reddit (Arctic Shift archive) — S13 brand-accuracy community-thread sweep: r/smallbusiness, r/SEO, r/marketing, r/bigseo

```yaml
source:          Reddit posts and comments, via the Arctic Shift open archive API (arctic-shift.photon-reddit.com); reddit.com not accessed
url_or_doc_id:   https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=smallbusiness&query=ChatGPT&after=1772323200&limit=10 ; .../posts/search?subreddit=SEO&query=incorrect&after=1772323200&limit=10 ; .../posts/search?subreddit=bigseo&query=%22ChatGPT%20says%22&limit=10 ; .../posts/search?subreddit=marketing&query=%22AI%20reputation%22&limit=10 ; .../comments/search?subreddit=SEO&body=%22wrong%20about%20our%22&after=1772323200&limit=10
published:       posts 2025-01-22 to 2026-09-22 (per created_utc)
pull_date:       2026-09-23
pull_method:     curl, one call per 90 s (shared API with another agent); HTTP 422 "Timeout" retried once after 150 s
pull_purpose:    evidence about a number (S13 community signal: thread existence and engagement counts)
tier:            5
tier_reason:     archive copy of a forum, counts are the archive's not the platform's, no permalink verified live (same reasoning as docs/raw/f-reddit-S5-counts-repull2-2026-09-23.md); community content is attention-class
source_label:    measured-by-us
lane:            F
sub_market:      organic recommendation
engine:          ChatGPT (as named by posters)
metric_kind:     none
supersedes:      none
captured:        every post returned per query (date | author | score | comments | title | permalink); selftext verbatim for the three on-topic threads; comment rows for the comment query
```

## Query log

| call | HTTP | result |
|---|---|---|
| r/smallbusiness, query `ChatGPT`, after 2026-03-01, limit 10 | 422 → retry 200 | 10 posts (newest-first) |
| r/SEO, query `incorrect`, after 2026-03-01, limit 10 | 200 | 10 posts |
| r/bigseo, query `"ChatGPT says"`, limit 10 | 422 → retry 422 | **failed** ("Timeout"), not retried further |
| r/marketing, query `"AI reputation"`, limit 10 | 200 | 10 posts |
| r/SEO comments, body `"wrong about our"`, after 2026-03-01, limit 10 | 200 | 10 comments |

[note: `after=1772323200` is 2026-03-01T00:00Z. The limit-10 result is the newest ten matches, not a count; no aggregate endpoint was called for these terms.]

## Verbatim — r/smallbusiness, `ChatGPT`, newest 10

```
2026-09-22 | Bangmydrum33 | 1 | 1 | What AI have you guys noticed is best for business help? | /r/smallbusiness/comments/1wnn24m/
2026-09-22 | anshhh_0 | 1 | 1 | I think founders are massively underestimating ChatGPT Ads right now. | /r/smallbusiness/comments/1wnm9oe/
2026-09-22 | joshbreda | 1 | 1 | Anyone using tools they made with ChatGPT or Claude at work? How did you share them with your team? | /r/smallbusiness/comments/1wneu8w/
2026-09-21 | anshhh_0 | 1 | 1 | We got blocked 60 seconds into an international client meeting because we were Indian. | /r/smallbusiness/comments/1wmr9e9/
2026-09-21 | batitola17 | 0 | 5 | Making small business acquisition simple and straighforward | /r/smallbusiness/comments/1wmfu2f/
2026-09-21 | LionZealousideal3355 | 0 | 31 | I checked how AI describes 5 small businesses I know. Only 1 came up looking good. | /r/smallbusiness/comments/1wm7akj/
2026-09-20 | Outside-Force-103 | 9 | 36 | How do u deal with such demoralisation when running a business? | /r/smallbusiness/comments/1wlmx0m/
2026-09-18 | 12gallonwiener | 6 | 24 | Are gym bussiness volatile? | /r/smallbusiness/comments/1wjl480/
2026-09-17 | KissP | 1 | 4 | ChatGPT Ads now connects to HubSpot and Shopify. Would you actually move some of your Google or Meta budget th… | /r/smallbusiness/comments/1wj0pet/
2026-09-16 | KissP | 1 | 7 | Meta just made WhatsApp Business setup talkable via Claude/Cursor/Codex — anyone actually using WhatsApp as th… | /r/smallbusiness/comments/1whs4wj/
```

Selftext, post 1wm7akj (2026-09-21, 0 score, 31 comments), verbatim:
> Been testing something out of curiosity: asking ChatGPT "who's the best \[service\] near \[city\]" for businesses I actually know. The results were eye-opening.  One business, run by a friend, has a perfect 5-star rating... but only 4 reviews. AI wouldn't confidently recommend it. Meanwhile a competitor with a 4.9 and over 2,000 reviews got picked instantly, and the AI even cited a local "best of" list as backup.   The lesson that stuck with me: a killer rating means nothing to AI if there's not enough volume and third-party proof behind it. Most owners I know are still checking their Google Maps ranking and have never once checked what ChatGPT actually says about them.  If anyone wants to try this on their own business, it's a 10-second test: just ask ChatGPT "who's the best \[your service\] in \[your city\]" and see if you even show up.

## Verbatim — r/marketing, `"AI reputation"`, newest 10

```
2026-05-20 | skankocean | 2 | 1 | manager messing up approved social posts (tone + AI + edits after posting) | /r/marketing/comments/1ti5agx/
2026-04-06 | Unusual_Ad5663 | 0 | 6 | I asked AI 3 questions about my company. The answers were more accurate than I expected. | /r/marketing/comments/1se1zdd/
2025-06-20 | phb71 | 1 | 3 | 40 todos to help with AI search | /r/marketing/comments/1lg2un0/
2025-05-30 | SherbetLongjumping43 | 1 | 0 | [INFO] How We Used AI to Instantly Dominate Digital Reputation (And Why You Should Too) | /r/marketing/comments/1kysmcq/  (selftext "[removed]")
2025-03-26 | Ceglerk | 1 | 0 | How are you managing brand reputation with LLMs and AI search? | /r/marketing/comments/1jkhckz/  (selftext "[removed]")
2025-03-19 | BogdanK_seranking | 23 | 4 | SEO & Marketing News: Google Launches March Core Update, Over 60% of AI Search Answers Are Wrong, Google Disrupts Reserv… | /r/marketing/comments/1jew85k/
2025-02-04 | SERanking_news | 19 | 5 | SEO News: OpenAI Launches Deep Research AI Agent, Google Calls Businesses for You, AIO Ranking Data Available in GSC for… | /r/marketing/comments/1ihhgkv/
2025-02-01 | keg1222 | 1 | 1 | Restaurant Marketers | /r/marketing/comments/1if8wy0/  (selftext opens "Who is your recommended brand reputation software company? I see a lot of talk about Birdeye and I am currently with Chatmeter.")
2025-01-28 | SERanking_news | 23 | 6 | Marketing News: DeepSeek Surpasses ChatGPT in Apple Store, Search Quality Raters Guidelines Update, Google Expands Site… | /r/marketing/comments/1ibzz4s/
2025-01-22 | SERanking_news | 12 | 6 | SEO News: Anti-Scraping Measures Amid Search Volatility, Vulnerability in Google Maps Fixed, New Manual Actions to Comba… | /r/marketing/comments/1i78qgg/
```

Selftext, post 1se1zdd (2026-04-06, 0 score, 6 comments), verbatim:
> Been working on our positioning for the last year. Website copy, case studies, content, all of it.  The other day I asked an AI model 3 questions about our company based only on what it could find online:  1. What does \[Company\] excel at? 2. What should I not use them for? 3. Who are their major competitors and how do they compare?  The answers were a lot more useful than I expected.  It gave me a pretty clear read on what seems to have landed, where people might hesitate, and who we're likely getting compared to.  Basically, it reflected the reputation we've built online, not necessarily the one we think we have internally.  That part was worth seeing.  Anyone else tried this? Did it line up with how you've been positioning your company, or did it show a gap?

## Verbatim — r/SEO, `incorrect`, newest 10 (titles only; none concerns an AI assistant's description of a brand)

```
2026-09-17 | ArtAllDayLong | 6 | 17 | SEOPress Pro, Redirections, Search Console - all the same issue, I swear.
2026-08-27 | darrenshaw_ | 2 | 1 | Sorry y'all. I tested SAB map pin hack and it didn't work.
2026-07-20 | Key_Zucchini_6704 | 5 | 9 | Google Web impressions suddenly dropped by 90% sitewide, but pages remain indexed — adult niche issue?
2026-06-26 | JamieHBrown | 0 | 10 | what's one SEO myth that people still preach yet is blatantly incorrect?
2026-06-09 | rsclmumbai | 1 | 0 | Bing Webmaster Tool > Incorrect Crawl Results
2026-05-20 | Aggravating_Fault_22 | 17 | 46 | I QUIT ahrefs!!!
2026-05-11 | Just_Handle2505 | 1 | 0 | Anyone having issues with SE Ranking Dynamics data being incorrect based on date range?
2026-05-06 | Papa40 | 3 | 7 | GSC data anomalies from the period May 2025 to April 2026:
2026-04-09 | Kumar_abhiii | 6 | 7 | Need help in lastmod date for Sitemap xml
2026-03-15 | zaitovalisher | 8 | 21 | Pagerank NS questions /summon @weblinkr
```

## Verbatim — r/SEO comments, body `"wrong about our"`, newest 10 (none concerns an AI assistant's description of a brand)

```
2026-09-22 | Illustrious-Wheel876 | /r/SEO/comments/1wmval7/…/pbed3nr/ | "Very common for sites to perform abnormally well briefly after launch…"
2026-09-22 | RyanJones | /r/SEO/comments/1wncygv/…/pbecsk2/ | "keyword density was NEVER a factor…"
2026-09-22 | sumizeit | /r/SEO/comments/1wncygv/…/pbe568a/ | "Keyword density as a ranking factor died years ago…"
2026-09-22 | 1hourphotography | /r/SEO/comments/1wncygv/…/pbe44n2/ | "I don't think you're wrong to push back…"
2026-09-21 | WebLinkr | /r/SEO/comments/1wjhb85/…/pb7qjqa/ | ">You discredit page speed which IS important…"
2026-09-20 | MuddaFrakker | /r/SEO/comments/1wf47jb/…/pav7zt9/ | "It will take time for you to even figure out how to use those tools…"
2026-09-17 | WebLinkr | /r/SEO/comments/1wj0t16/…/pafx9q3/ | "Happy to help you correct this but your concept is 50% there…"
2026-09-17 | RipMySleepSchedule | /r/SEO/comments/1wj0t16/…/pafgubv/ | "Maybe niche is the wrong here…"
2026-09-17 | PMDevSolutions | /r/SEO/comments/1wirxaq/…/pade8h3/ | "I maintain sites for small businesses that have been blogging…"
2026-09-16 | mediamuesli | /r/SEO/comments/1wi44rj/…/pa7jldz/ | "Programming websites and SEO is definitely a very good fit…"
```

[note: the archive's `query`/`body` matching is token-based and undocumented; "wrong about our" matched comments containing "wrong" without the phrase. Quoted phrases do not reliably restrict to phrase matches.]

## Pull notes — mechanical only

- Five calls, one failed twice with HTTP 422 (r/bigseo). Pacing 90 s between calls per the brief; a second agent used the same API concurrently.
- Permalinks are as stored by the archive; none opened on reddit.com.

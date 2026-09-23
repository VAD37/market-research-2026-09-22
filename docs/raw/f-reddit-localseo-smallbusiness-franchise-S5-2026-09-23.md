# Reddit (Arctic Shift archive) — S5 thread counts and recent threads for AI-visibility terms in r/localseo, r/franchise, r/smallbusiness, March–September 2026

```yaml
source:          Reddit posts and comments, via the Arctic Shift open archive API (arctic-shift.photon-reddit.com)
channel:         Arctic Shift archive of reddit.com
url_or_doc_id:   https://arctic-shift.photon-reddit.com/api/posts/search/aggregate?aggregate=created_utc&frequency=month&subreddit=<sub>&query=<term>&after=2026-03-01&before=2026-09-24 ; .../api/posts/search?subreddit=<sub>&query=<term>&after=<d>&before=<d>&limit=10&sort=desc ; .../api/comments/search?subreddit=localseo&body=%22AI%20visibility%22&after=2026-08-24&before=2026-09-24&limit=10&sort=desc — 24 calls, each listed in the log below
published:       archive counts as of the pull; posts created 2026-03-01 to 2026-09-23
pull_date:       2026-09-23
pull_method:     curl (User-Agent "market-research-bot contact: research@example.invalid"), one call per 90 s, API shared with P16-c3; archive copy, not live
pull_purpose:    evidence about a number
tier:            5
tier_reason:     demand-signals.md S5 default is 4 when the platform publishes counts; these are an archive's counts, coverage unverified; held at 5 per f-reddit-S5-counts-repull2-2026-09-23.md
source_label:    measured-by-us (counts computed by the archive API on our query)
lane:            F
sub_market:      organic recommendation
engine:          n/a — threads name ChatGPT, Perplexity, Gemini, AI Overviews
metric_kind:     none
supersedes:      none — extends f-reddit-S5-counts-repull2-2026-09-23.md (ten practitioner subreddits) with three local / franchise / small-business subreddits
captured:        monthly thread counts per subreddit × query; 10 most recent r/localseo threads matching `ChatGPT` (title, author, score, comments, permalink, selftext excerpt); 10 most recent r/localseo comments whose body matches "AI visibility"
verbatim:        full (API values and text as returned; selftext truncated at ~900 characters where marked)
```

## Call log — 24 calls (UTC), HTTP code, name

```
08:27:54 422 agg-smallbusiness-aivis   (query "AI visibility", Mar 1–Sep 24)   → {"data":null,"error":"Timeout. Maybe slow down a bit"}
08:29:33 422 agg-smallbusiness-aeo
08:31:04 422 agg-smallbusiness-geo
08:32:38 200 agg-localseo-aivis
08:34:13 200 agg-localseo-aeo
08:35:47 200 agg-localseo-geo
08:37:19 200 agg-franchise-aivis
08:38:51 200 agg-franchise-aeo
08:40:24 200 agg-franchise-geo
08:42:00 422 posts-localseo-aivis        (Jun 24–Sep 24)
08:43:38 200 posts-localseo-chatgpt     (Jun 24–Sep 24, 10 records)
08:45:10 422 posts-smallbusiness-aivis
08:46:47 422 posts-smallbusiness-chatgpt-seo
08:48:2x 422 posts-franchise-chatgpt
08:49:54 200 posts-franchise-aisearch   (0 records)
08:51:26 400 comments-localseo-aivis    → {"data":null,"error":"Unknown query parameter: 'query'"}
08:52:57 400 comments-smallbusiness-aeo → same error
08:56:14 422 posts-smallbusiness-aivis-1m (Aug 24–Sep 24)
08:57:45 422 posts-smallbusiness-chatgpt-seo-1m
08:59:16 422 posts-localseo-aivis-1m
09:00:57 200 agg-smallbusiness-aivis-3m (Jun 24–Sep 24)
09:02:36 200 agg-smallbusiness-aeo-3m
09:04:07 400 comments-localseo-aivis-1m (query= again) → same error
09:07:20 200 comments-localseo-aivis-body (body= parameter, Aug 24–Sep 24, 10 records)
```

Tally: 24 calls; 200 × 11; 422 "Timeout" × 10; 400 "Unknown query parameter: 'query'" × 3 (the comments endpoint takes `body=`, not `query=`).

## Threads per month — `aggregate=created_utc&frequency=month`, bucket labels verbatim

[note: bucket labels are the API's `created_utc` strings; 2026-02-28T23:00:00.000Z is 2026-03-01 in UTC+1, so buckets read March to September 2026; September runs to 2026-09-24.]

| subreddit | query sent | Mar | Apr | May | Jun | Jul | Aug | Sep to 09-23 | window total |
|---|---|---|---|---|---|---|---|---|---|
| r/localseo | `"AI visibility"` | 9 | 9 | 21 | 13 | 6 | 12 | 3 | 73 |
| r/localseo | `AEO` | 6 | 7 | 10 | 7 | 3 | 5 | 9 | 47 |
| r/localseo | `"generative engine optimization"` | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 4 |
| r/franchise | `"AI visibility"` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| r/franchise | `AEO` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| r/franchise | `"generative engine optimization"` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| r/smallbusiness | `"AI visibility"` (3-month window only; buckets 2026-06-23T22Z, 07-23T22Z, 08-23T22Z) | — | — | — | — | 0 | 0 | 0 | 0 |
| r/smallbusiness | `AEO` (same window) | — | — | — | — | 0 | 0 | 0 | 0 |
| r/smallbusiness | `"generative engine optimization"` | not obtained — 422 on the 7-month window; 3-month window not retried | | | | | | | — |

[note: unique-author aggregates not pulled this run (pacing). `query` semantics are the archive's; "GEO" bare token not sent here because of geo-targeting noise recorded in the earlier pull.]

## r/localseo — 10 most recent threads matching `ChatGPT`, 2026-06-24 to 2026-09-24 (`sort=desc`)

| created | author | score | comments | title | permalink |
|---|---|---|---|---|---|
| 2026-09-19 | BadisteJealouse-48 | 0 | 0 | is hubspot aeo pricing actually worth $50 a month for tracking ai search visibility? | /r/localseo/comments/1wkirvw/is_hubspot_aeo_pricing_actually_worth_50_a_month/ |
| 2026-09-17 | Gold_Pop_8708 | 0 | 6 | Do not sleep on reviews. Get as many genuine reviews as you can on your Google Business Profile. | /r/localseo/comments/1wizw5o/do_not_sleep_on_reviews_get_as_many_genuine/ |
| 2026-09-17 | ZonicMedia | 1 | 2 | How do you get a local home inspection company to show up in ChatGPT and Gemini? | /r/localseo/comments/1wiw2ye/how_do_you_get_a_local_home_inspection_company_to/ |
| 2026-09-16 | myaboutpage | 0 | 5 | Got my website referenced on ChatGPT | /r/localseo/comments/1whvxmz/got_my_website_referenced_on_chatgpt/ |
| 2026-09-15 | firoz6033 | 38 | 41 | I Lost a Local SEO Client to ChatGPT | /r/localseo/comments/1wh5qfe/i_lost_a_local_seo_client_to_chatgpt/ |
| 2026-09-11 | Beginning-Hat-885 | 1 | 2 | Are third-party listicles helping your clients show up in ChatGPT results? | /r/localseo/comments/1wdcaz0/are_thirdparty_listicles_helping_your_clients/ |
| 2026-09-10 | freshcove8571 | 1 | 0 | What are you guys actually looking for in a local SEO company now? | /r/localseo/comments/1wcrsl4/what_are_you_guys_actually_looking_for_in_a_local/ |
| 2026-09-10 | ConstructionDear2873 | 0 | 3 | How do you find time for new clients when tracking AI citations eats your whole week? | /r/localseo/comments/1wcnx6k/how_do_you_find_time_for_new_clients_when/ |
| 2026-09-10 | ConstructionDear2873 | 1 | 0 | (same title, duplicate post) | /r/localseo/comments/1wcnvce/how_do_you_find_time_for_new_clients_when/ |
| 2026-09-10 | Harkirat101 | 8 | 44 | SEO + AI Search: Ask Me Anything | /r/localseo/comments/1wcm0cs/seo_ai_search_ask_me_anything/ |

### Selftext excerpts, verbatim (first ~900 characters)

**is hubspot aeo pricing actually worth $50 a month …** — "we have been looking at hubspot aeo pricing as we explore ways to track how chatgpt, perplexity, and gemini cite our brand. at a flat $50 a month, it is definitely cheaper than enterprise tracking platforms, and you do not need a full marketing hub subscription to run it. but the entry tier caps you at tracking 25 prompts, which fills up pretty fast once you start plugging in core product keywords and competitor checks."

**Do not sleep on reviews …** — "I recently noticed something interesting while working on a few Google Business Profiles and checking how they show up in ChatGPT recommendations. One of my clients has their website ranking on page 1 for almost all their target keywords. Their GBP has a 4.4 rating with around 150 reviews. But most of their competitors have 300+ reviews and an average rating of around 4.7. Interestingly, my client's GBP is hardly showing up in ChatGPT when people search for location based terms like roofing in NYC. another client of mine that is not even ranking on page 1 or page 2 for most of their keywords. But their GBP has around 200 reviews with a 4.8 rating, while their competitors have less than 100 reviews on average. That business is showing up near the top in ChatGPT recommendations for location based searches. In both cases, everything else was properly optimized. Citations were …"

**How do you get a local home inspection company to show up in ChatGPT and Gemini?** — "We've been experimenting with this for local service businesses, and one thing I've noticed is that getting a home inspection company discovered by AI systems is a little different from traditional local SEO. You can't simply "submit your business to ChatGPT" and expect it to start recommending you. The foundation is still the same: make sure the business has a legitimate, well optimized Google Business Profile, a crawlable website, consistent business information, strong local citations, and genuine reviews. …"

**Got my website referenced on ChatGPT** — "It's the first time I saw my website was suggested why looking for something on ChatGPT. Yesterday night, I decided to make test if my 2 years old website will be suggested based on the queries. My website is on gardening services. So, I looked gardening in my city, and my website was among the suggestions. It's funny because last week, I submitted my URL to an indexer (indexyour.link) for the first time, which pings AI agents using the IndexNow technologies. Apparently, this was the reason why I saw my website listed by AI. …"

**I Lost a Local SEO Client to ChatGPT** — "I want to share a real experience with the local SEO community. Niche: Construction · Location: New York City · Project duration: Two months. When I onboarded the client, I rebuilt the website structure, optimized the landing pages and Google Business Profile, and created citations and profile links. The early results were promising. However, my profit was low because I invested most of my time and resources into development and building a strong foundation. Then the client told me: "I bought ChatGPT, so I can do everything myself now." He had also stopped paying my previous invoice. Throughout the project, he regularly checked my work with ChatGPT and asked me to make changes based on its suggestions. Some recommendations were helpful, but others were generic and didn't fit the business or the NYC market. I'm not against AI. It can be a useful tool, but it doesn't …"

**Are third-party listicles helping your clients show up in ChatGPT results?** — "During a recent client audits and AI visibility tracking, we noticed that one of our clients had been included in this: https://www.newsinsights.ca/best-asbestos-removal-companies-in-vancouver/. The mention appears to be recent, and we're now seeing ChatGPT cite this page when recommending companies in that area. I've attached a screenshot showing News Insights cited more than once within the same response. What caught my attention was how a single listicle could become a source for multiple business recommendations. … This is only one example, so I wouldn't say it proves listicles are the most effective way to improve AI visibility. …"

**What are you guys actually looking for in a local SEO company now?** — "… Some are still mostly focused on Google Maps, rankings and backlinks. Others are pushing more into AI search, ChatGPT visibility and GEO. I've seen companies like WebFX, HigherVisibility and Anew Media Group taking pretty different approaches to it. For the people actually hiring SEO companies right now, what matters most to you? Are you still mostly judging them on leads and Maps rankings, or are you starting to care about whether your business shows up in AI results too? …"

**How do you find time for new clients when tracking AI citations eats your whole week?** — "Been doing SEO for about 8 years, freelance the last year. Then clients started asking if they show up in ChatGPT and Perplexity answers. Now I'm neck deep in AEO work too. Problem is tracking that stuff eats my whole week. I run the same prompt sets by hand across 4 models, log which ones mention my clients, screenshot it for the report. Otterly.ai would automate some of it but the pricing doesn't make sense for 2 clients yet. Found some experiment writeups from HumansWith.AI on tracking citation share of voice. … I've got 2 solid retainer clients and one warm referral lead. That's the whole pipeline. …"

**SEO + AI Search: Ask Me Anything** — "I work with businesses on SEO, local SEO, and AI search visibility, and lately I've been seeing a shift in what actually matters for getting discovered online. Traditional rankings are still important, but now there's another layer: Google AI Overviews, ChatGPT, Perplexity, Gemini, etc. A business can rank well in traditional search and still not be mentioned or recommended by AI when potential customers ask for businesses in their area or industry. … Not appearing in Google AI Overviews. Not being mentioned in ChatGPT/Perplexity. Unsure how to approach AI SEO/GEO. …"

## r/localseo — 10 most recent comments with body matching "AI visibility", 2026-08-24 to 2026-09-24

| created | author | score | body excerpt (first ~260 characters) | permalink |
|---|---|---|---|---|
| 2026-09-21 | aspk | 1 | "I'm looking into this right now actually. I'll probably give Local Dominator a go as it looks into rankings + AI visibility too which is where local SEO is heading. I tried Local Falcon but I didn't find it very useful. They inject AI recommendations into rep…" | /r/localseo/comments/1wm1n6t/brightlocal_alternative_that_does_the_work_not/pb9nt97/ |
| 2026-09-18 | Positive-Ad7666 | 1 | "Congrats! But how do you measure AI visibility? And how do you arrive at that percentage?" | /r/localseo/comments/1wipwj0/from_35_to_39_growth_in_2_days_almost_40_up_in/paimvur/ |
| 2026-09-14 | Strong_Teaching8548 | 1 | "Start with an accurate GBP primary category and service area, then make the matching page on your site genuinely useful …" | /r/localseo/comments/1wfyyqo/any_advice_on_improving_my_websites_gbp_visibility/p9ub3qf/ |
| 2026-09-14 | firefuelseo | 1 | "Your GBP performance baseline in terms of which keywords you show up for is going to be primarily determined by your primary category. …" | same thread /p9s1mn3/ |
| 2026-09-14 | G-WEB_GROUP | 1 | "… For AI visibility, focus on useful, well[-structured content]…" | same thread /p9rqzed/ |
| 2026-09-14 | BrandLoom-Consulting | 1 | "If you're just starting out, we'd avoid trying to fix everything at once. … make the business easy for Google and AI platforms to understand. …" | same thread /p9qmjcr/ |
| 2026-09-14 | Typical-Most | 1 | "found a reliable AI visibility tool for local businesses" | /r/localseo/comments/1qn00m4/has_anyone_found_a_reliable_ai_visibility_tool/p9panej/ |
| 2026-09-13 | Harkirat101 | 1 | "… For AI visibility, I'd focus on whether ea[ch page]…" | /r/localseo/comments/1wcm0cs/seo_ai_search_ask_me_anything/p9lt6gy/ |
| 2026-09-13 | Pleasant-Concept-385 | 1 | "so i have multiple pages for my business webiste like service pages and then tools separatly now i ma confused how to improve my ranking … how to improve ai visibility for all those" | same thread /p9jw2qd/ |
| 2026-09-12 | Individual_Clerk_925 | 1 | "One thing I've noticed is that a lot of businesses focus heavily on rankings but don't really look at why competitors are being trusted and mentioned. …" | same thread /p9c6bxx/ |

## Pull notes — mechanical only

- Paced at one call per 90 s throughout; ten calls still returned 422 "Timeout. Maybe slow down a bit" — all seven r/smallbusiness calls on 7-month or 1-month windows and three r/localseo / r/franchise post searches. The two r/smallbusiness aggregates that answered used a 3-month window.
- `comments/search` rejects `query=`; `body=` accepted on the last call.
- r/franchise `"AI search"` posts search returned 0 records on a 200.
- No reddit.com URL was fetched; permalinks kept as the archive returned them.
- Subreddit names sent lowercase (`localseo`, `franchise`, `smallbusiness`); the API returned `subreddit: localseo` on records.

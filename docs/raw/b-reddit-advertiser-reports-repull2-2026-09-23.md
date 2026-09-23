# Reddit (Arctic Shift archive) — advertiser-reported results from ChatGPT / OpenAI ads, Perplexity sponsored, Google AI Mode / AI Overviews ads

```yaml
source:          Reddit posts and comments, via the Arctic Shift open archive API (arctic-shift.photon-reddit.com)
channel:         Arctic Shift archive of reddit.com
url_or_doc_id:   https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>&query=<terms>|title=<term>&after=<date>&before=<date>&limit=100&fields=... ; https://arctic-shift.photon-reddit.com/api/comments/search?subreddit=<sub>&body=<terms>&after=<date>&before=<date>&limit=100 ; per-item reddit permalinks below
published:       items dated 2026-01-16 to 2026-09-23 (created_utc per item)
pull_date:       2026-09-23
pull_method:     curl / python urllib (User-Agent "Mozilla/5.0 research-pull/1.0"); no browser, no extension; archive copy, not live
pull_purpose:    evidence about a number
tier:            5
tier_reason:     archive copy, not live reddit; archive coverage unverified. Spot-check: Wayback CDX holds a capture only for 1tdviug (20260516140838), and that capture is a Reddit "Please wait for verification" page, not the post — no permalink verified by another path, so held at 5 per brief. Posters are anonymous accounts; figures are self-reported, unaudited
source_label:    company-stated (advertiser self-report); one item vendor-reported (1vsx4ep, author discloses employer Nile)
lane:            B
sub_market:      paid placement
engine:          ChatGPT (OpenAI Ads) for every metric-bearing item; Google AI Mode / AI Overviews and Perplexity: questions and relays only
metric_kind:     traffic (impressions, clicks, CTR, CPC, CPM); sales (signups, orders, paid conversions) where stated
supersedes:      none (reddit.com was blocked for P4-r on 2026-09-22 / 2026-09-23; no prior Reddit raw file)
captured:        full post selftext or comment body for each kept item; query log; counts
verbatim:        full for kept items (archive text as stored, markdown escapes kept)
```

## Scope and counts

- Subreddits searched: r/PPC, r/marketing, r/SEO, r/digital_marketing, r/advertising, r/bigseo, r/adops, r/ecommerce, r/SaaS, r/startups. Window 2026-01-01 to 2026-09-23.
- Posts, `query=` full text: r/PPC, r/marketing, r/SEO, r/digital_marketing × "chatgpt ads", "openai ads", "perplexity ads", "perplexity sponsored", "AI Mode ads", "AI Overviews ads"; r/advertising × "chatgpt ads", "openai ads" (partial). Posts, `title=` (faster index, used after repeated timeouts): r/advertising, r/bigseo, r/adops, r/ecommerce, r/SaaS, r/startups × "chatgpt", "openai", "perplexity", "AI Mode". Comments, `body=` "chatgpt ads": r/PPC, r/marketing.
- Records returned (deduplicated by id): 852 (posts 580, comments 272). Records whose title+text name an engine (ChatGPT/OpenAI/Perplexity/AI Mode/AI Overview) and an ad term: 499. Items read in full and kept below: 38.
- Classes (kept items): metric-moved (number + window) 14 records covering 10 advertiser reports (g_hock 1tdviug + 1tpfmlb one advertiser, two windows; EssenzaVital post + 2 comments one report); metric stated, window unstated 9; claim-without-metric 8; third-party measurement 1; question/complaint 6 (examples; the remaining engine+ad-context records were not individually classified — news relays, setup and tracking questions, vendor promotion).
- No advertiser-reported metric for Perplexity sponsored or Google AI Mode / AI Overviews ads was found; r/PPC AI Mode posts relay third-party figures only (e.g. 1tju70g, "ads appearing in roughly 25.5% of AI Mode results ... 35% higher CPC", linked to digitalapplied.com) and are not kept.
- Gaps (timeouts after 4–8 retries, "Timeout. Maybe slow down a bit" / HTTP 422): r/advertising title "chatgpt", "perplexity"; r/bigseo "perplexity", "AI Mode"; r/adops, r/ecommerce "perplexity"; r/SaaS "openai"; r/startups "chatgpt", "perplexity"; first full-window r/PPC "chatgpt ads" (re-run in chunks, returned). Comments in the other eight subreddits not searched.

## Query log

| run | endpoint | subreddit | param | term | window | returned | error |
|---|---|---|---|---|---|---|---|
| 1 full window, sort=desc | posts/search | PPC | query | chatgpt ads | from 2026-01-01 | — | HTTP Error 422: Unprocessable Entity |
| 1 full window, sort=desc | posts/search | PPC | query | openai ads | from 2026-01-01 | 30 |  |
| 1 full window, sort=desc | posts/search | PPC | query | perplexity ads | from 2026-01-01 | 6 |  |
| 1 full window, sort=desc | posts/search | PPC | query | perplexity sponsored | from 2026-01-01 | 1 |  |
| 1 full window, sort=desc | posts/search | PPC | query | AI Mode ads | from 2026-01-01 | 19 |  |
| 1 full window, sort=desc | posts/search | PPC | query | AI Overviews ads | from 2026-01-01 | 7 |  |
| 1 full window, sort=desc | posts/search | marketing | query | chatgpt ads | from 2026-01-01 | 15 |  |
| 1 full window, sort=desc | posts/search | marketing | query | openai ads | from 2026-01-01 | 4 |  |
| 1 full window, sort=desc | posts/search | marketing | query | perplexity ads | from 2026-01-01 | 1 |  |
| 1 full window, sort=desc | posts/search | marketing | query | perplexity sponsored | from 2026-01-01 | 0 |  |
| 1 full window, sort=desc | posts/search | marketing | query | AI Mode ads | from 2026-01-01 | 0 |  |
| 1 full window, sort=desc | posts/search | marketing | query | AI Overviews ads | from 2026-01-01 | 1 |  |
| 1 full window, sort=desc | posts/search | SEO | query | chatgpt ads | from 2026-01-01 | 15 |  |
| 1 full window, sort=desc | posts/search | SEO | query | openai ads | from 2026-01-01 | 3 |  |
| 1 full window, sort=desc | posts/search | SEO | query | perplexity ads | from 2026-01-01 | 3 |  |
| 1 full window, sort=desc | posts/search | SEO | query | perplexity sponsored | from 2026-01-01 | 0 |  |
| 1 full window, sort=desc | posts/search | SEO | query | AI Mode ads | from 2026-01-01 | 1 |  |
| 1 full window, sort=desc | posts/search | SEO | query | AI Overviews ads | from 2026-01-01 | 5 |  |
| 2 three-month chunks | posts/search | PPC | query | chatgpt ads | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 2 three-month chunks | posts/search | PPC | query | chatgpt ads | from 2026-04-01 | 36 |  |
| 2 three-month chunks | posts/search | PPC | query | chatgpt ads | from 2026-07-01 | 43 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | chatgpt ads | from 2026-01-01 | 8 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | chatgpt ads | from 2026-04-01 | 16 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | chatgpt ads | from 2026-07-01 | 8 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | openai ads | from 2026-01-01 | 3 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | openai ads | from 2026-04-01 | — | Timeout. Maybe slow down a bit |
| 2 three-month chunks | posts/search | digital_marketing | query | openai ads | from 2026-07-01 | 1 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | perplexity ads | from 2026-01-01 | 2 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | perplexity ads | from 2026-04-01 | 4 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | perplexity ads | from 2026-07-01 | 1 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | perplexity sponsored | from 2026-01-01 | 0 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | perplexity sponsored | from 2026-04-01 | 0 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | perplexity sponsored | from 2026-07-01 | 0 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | AI Mode ads | from 2026-01-01 | 2 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | AI Mode ads | from 2026-04-01 | 3 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | AI Mode ads | from 2026-07-01 | 0 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | AI Overviews ads | from 2026-01-01 | 2 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | AI Overviews ads | from 2026-04-01 | 1 |  |
| 2 three-month chunks | posts/search | digital_marketing | query | AI Overviews ads | from 2026-07-01 | 1 |  |
| 2 three-month chunks | posts/search | advertising | query | chatgpt ads | from 2026-01-01 | 18 |  |
| 2 three-month chunks | posts/search | advertising | query | chatgpt ads | from 2026-04-01 | 4 |  |
| 2 three-month chunks | posts/search | advertising | query | chatgpt ads | from 2026-07-01 | 8 |  |
| 2 three-month chunks | posts/search | advertising | query | openai ads | from 2026-01-01 | 3 |  |
| 3 three-month chunks | posts/search | advertising | query | openai ads | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 3 three-month chunks | posts/search | advertising | query | openai ads | from 2026-04-01 | — | Timeout. Maybe slow down a bit |
| 3 three-month chunks | posts/search | advertising | query | openai ads | from 2026-07-01 | 3 |  |
| 3 three-month chunks | posts/search | advertising | query | perplexity ads | from 2026-01-01 | 0 |  |
| 3 three-month chunks | posts/search | advertising | query | perplexity ads | from 2026-04-01 | 1 |  |
| 4 title / comment chunks | posts/search | advertising | title | chatgpt | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | advertising | title | openai | from 2026-01-01 | 9 |  |
| 4 title / comment chunks | posts/search | advertising | title | perplexity | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | advertising | title | AI Mode | from 2026-01-01 | 0 |  |
| 4 title / comment chunks | posts/search | bigseo | title | chatgpt | from 2026-01-01 | 68 |  |
| 4 title / comment chunks | posts/search | bigseo | title | openai | from 2026-01-01 | 1 |  |
| 4 title / comment chunks | posts/search | bigseo | title | perplexity | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | bigseo | title | AI Mode | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | adops | title | chatgpt | from 2026-01-01 | 2 |  |
| 4 title / comment chunks | posts/search | adops | title | openai | from 2026-01-01 | 2 |  |
| 4 title / comment chunks | posts/search | adops | title | perplexity | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | adops | title | AI Mode | from 2026-01-01 | 0 |  |
| 4 title / comment chunks | posts/search | ecommerce | title | chatgpt | from 2026-01-01 | 65 |  |
| 4 title / comment chunks | posts/search | ecommerce | title | openai | from 2026-01-01 | 2 |  |
| 4 title / comment chunks | posts/search | ecommerce | title | perplexity | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | ecommerce | title | AI Mode | from 2026-01-01 | 0 |  |
| 4 title / comment chunks | posts/search | SaaS | title | chatgpt | from 2026-01-01 | 100 |  |
| 4 title / comment chunks | posts/search | SaaS | title | openai | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | SaaS | title | perplexity | from 2026-01-01 | 100 |  |
| 4 title / comment chunks | posts/search | SaaS | title | AI Mode | from 2026-01-01 | 17 |  |
| 4 title / comment chunks | posts/search | startups | title | chatgpt | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | startups | title | openai | from 2026-01-01 | 10 |  |
| 4 title / comment chunks | posts/search | startups | title | perplexity | from 2026-01-01 | — | Timeout. Maybe slow down a bit |
| 4 title / comment chunks | posts/search | startups | title | AI Mode | from 2026-01-01 | 1 |  |
| 4 title / comment chunks | comments/search | PPC | body | chatgpt ads | from 2026-01-01 | 68 |  |
| 4 title / comment chunks | comments/search | PPC | body | chatgpt ads | from 2026-04-01 | 82 |  |
| 4 title / comment chunks | comments/search | PPC | body | chatgpt ads | from 2026-07-01 | 100 |  |
| 4 title / comment chunks | comments/search | marketing | body | chatgpt ads | from 2026-01-01 | 13 |  |
| 4 title / comment chunks | comments/search | marketing | body | chatgpt ads | from 2026-04-01 | 2 |  |
| 4 title / comment chunks | comments/search | marketing | body | chatgpt ads | from 2026-07-01 | 7 |  |

[note: limit=100 was used; no `"data":null` from the limit itself was seen — nulls came from server timeouts. Run 1 was stopped part-way; runs 2–4 resumed with smaller windows or the title index.]

# Kept items, verbatim

## Class — metric-moved (number + window)

### post 1w7fbzt — r/PPC, 2026-09-04 20:07 UTC, u/Michael-Traction, score 0, num_comments 7

- permalink: https://www.reddit.com/r/PPC/comments/1w7fbzt/
- matched query terms: chatgpt ads
- title: "Ran $707 through ChatGPT Ads (the new beta)."

> We run paid search for a US visa/passport expediting service. AOV around $650, high-consideration purchase, long-ish consideration window. Got started with ChatGPT Ads and ran an 8-day test. Posting the numbers because I couldn't find anyone else publishing real ones, and then a methodology note that I think is the more useful half.
>
>
>
> **THE NUMBERS (Aug 28 – Sep 4)**
>
> \- Spend: $707
>
> \- Impressions: \~25,500
>
> \- Clicks: \~200
>
> \- CTR: 0.75%
>
> \- CPC: $3.37
>
> \- Form sessions started: 20
>
> \- Quotes reached: 1
>
> \- Orders: 0
>
> The one quote was a $1,848 order — genuinely top-decile for us. It abandoned at the details screen.
>
>
>
> **THE MISTAKE I ALMOST MADE**
>
> Our ads landed on a marketing page with one hop to the intake form. Obvious hypothesis: the hop is killing it, point the ads straight at the form. I was about to spend another $300 testing exactly that.
>
> Then I checked what our Google campaign's final URL was.
>
> Same page. Identical URL. It had been running the whole time.
>
> So I already had a control group on the exact variable I was about to buy an experiment for. Same landing page, same link decoration, same form, same six-day window:
>
>
>
> ||clicks|sessions                   |click→session|
> |:-|:-|:-|:-|
> |Google     |426       |127         |  29.8%|
> |ChatGPT             |165        |15          |  9.1%|
>
> 3.3x apart with the landing page held constant. The hop is not the problem. It cannot be - the control clears the same hop at 30%.
>
> Session recordings said the same thing independently: median session 5.5s vs 80.5s for paid search on the same page, and 30% of ChatGPT sessions ended inside 2 seconds with zero clicks (paid search: 8%). Two unrelated measurement systems, same answer.
>
>
>
> **THE NUMBER THAT ACTUALLY SETTLED IT**
>
> Cost per session that got past the first screen:
>
> *   Google:   \~$92
> *   ChatGPT:  \~$555
>
> \~6x off the channel it has to beat. That's not a gap you optimize your way out of with budget.
>
>
>
> **WHAT I'D TELL SOMEONE TESTING IT**
>
> 1. Before you buy an experiment, check whether an existing campaign already varies the thing you're testing. Mine did, on the identical URL, and I only noticed because I went to confirm the URL before editing it. That check cost two minutes and saved $300.
>
> 2. Write the kill line before you spend. Ours was "$600 with zero attributed orders = stop," registered before launch. When you hit it there's nothing to argue about — which matters, because the $1,848 quote made a very persuasive case for "just one more week."
>
> 3. Sample size honesty: \~200 clicks can't tell you a conversion rate. It CAN tell you a click-to-engagement rate, because that's a much higher-frequency event. Pick the metric your sample can actually resolve.
>
> 4. CTR looked fine. 0.75% on a new placement isn't alarming. Everything bad happened after the click, which is the part the platform doesn't report.
>
>
>
> **OPEN QUESTION FOR THE ROOM**
>
> That 30%-under-2-seconds figure is the one I can't explain. Same page, same week, same tracking - paid search runs 8%. Is anyone else seeing that shape on ChatGPT Ads, and is it a placement thing, an intent thing, or something else? Genuinely asking, not implying.
>
>
>
> Happy to answer questions on setup, targeting, or measurement.

### post 1w7zdpg — r/PPC, 2026-09-05 12:25 UTC, u/EssenzaVital, score 1, num_comments 7

- permalink: https://www.reddit.com/r/PPC/comments/1w7zdpg/
- matched query terms: chatgpt ads
- title: "160 ChatGPT Ads clicks in Spain, €37.61 spend, 0 purchases — anyone else seeing very short sessions?"

> Running an early ChatGPT Ads test for a premium DTC supplement brand in Spain.
>
> So far:
>
> \- 5,590 impressions  
> \- 160 clicks  
> \- €37.61 spend  
> \- €0.24 CPC  
> \- 2.86% CTR  
> \- 0 conversions
>
> The bigger concern is traffic quality: many recorded sessions are only around 1–10 seconds.
>
> We’re now tightening the Context Hints around high-intent buyers looking for premium liquid hydrolysed collagen, higher dose, and comparing products before purchase.
>
> Curious if others are seeing the same:
>
> \- click vs actual session discrepancies?  
> \- very short sessions?  
> \- better results after tightening Context Hints?  
> \- any real ecommerce purchases yet?
>
> Especially interested in supplement / health & wellness advertisers.

### comment paivgci — r/PPC, 2026-09-18 06:41 UTC, u/EssenzaVital, score 1

- permalink: https://www.reddit.com/r/PPC/comments/1w7zdpg/_/paivgci/
- matched query terms: chatgpt ads

> **UPDATE — We received an official response from OpenAI Ads Support**
>
> Quick update for everyone following this or experiencing similar issues.
>
> We submitted a formal support case to OpenAI with our Ads Manager data, GA4 data and supporting screenshots, specifically asking them to investigate the large discrepancy between reported ad clicks and actual website sessions, as well as the traffic geography and billed interactions.
>
> OpenAI Ads Support has now responded and confirmed that the numbers we reported for the original campaign match their internal reporting:
>
> **5,590 impressions**  
> **160 clicks**  
> **€37.61 spend**
>
> Their response:
>
> “Thank you for the detailed information and supporting screenshots. We have confirmed that the Ads Manager figures you shared for 4 September—5,590 impressions, 160 clicks, and €37.61 in spend—match our internal reporting for that campaign.
>
> Your case still requires specialist review of the reported difference between Ads Manager clicks and your GA4 sessions, including the delivery-geography, tracking, and billed-interaction questions you raised. Ads clicks and website analytics sessions measure different stages of a visit, so they do not always match one-to-one. We have not yet reached a conclusion about the cause of the discrepancy or whether any billing adjustment is appropriate.
>
> We will follow up after the specialist review is complete.”
>
> Ozone | OpenAI Ads Support
>
> So at this point, **OpenAI has not concluded that anything was wrong, but they also have not dismissed the discrepancy as simply a GA4 issue.** 
>
> The case has been escalated for specialist review covering:
>
> click vs GA4 session discrepancy  
> delivery geography  
> tracking  
> billed interactions  
> whether any billing adjustment may be appropriate
>
> We also ran a second, smaller validation campaign after the original test and unfortunately saw a similar click-to-session discrepancy again. We are sending that additional dataset to the same support case so they can compare both campaigns.
>
> For now, we’ve **paused further ChatGPT Ads spend** until the specialist review comes back.  
> I’ll update this thread again when OpenAI gives us their final findings. If anyone else running ChatGPT Ads is seeing a similar discrepancy, especially between **Ads Manager clicks and GA4/Shopify sessions**, please share your numbers — it would be useful to compare datasets.
>
> Hope all these shared informations helps open ai to develop a better version and what is more important other entrepreneurs and businesses out there to not to burn their hard earned money and also hope this openai tool will finally work well as we believe the potential behind the idea is huge! 🙏🏽

### comment paivsjd — r/PPC, 2026-09-18 06:45 UTC, u/EssenzaVital, score 1

- permalink: https://www.reddit.com/r/PPC/comments/1w7zdpg/_/paivsjd/
- matched query terms: chatgpt ads

> Thank you. This is really useful, and your relevancy experience sounds quite similar to what we’ve been seeing.  
> We initially thought the 1–10 second sessions might simply be a landing-page or targeting issue, which is why we tightened the Context Hints significantly and ran a second, smaller validation campaign. Unfortunately, we still saw a substantial discrepancy between reported ChatGPT Ads clicks and the sessions we could actually observe.  
> We’ve now raised this formally with OpenAI. 
>
> Support confirmed that our original campaign numbers (**5,590 impressions, 160 clicks and €37.61 spend)** match their internal reporting, but they have escalated the case for specialist review specifically covering the **click vs GA4 session discrepancy, delivery geography, tracking and billed interactions**. They also said they haven’t yet determined the cause or whether any billing adjustment is appropriate.
>
> So for now we’ve paused further spend until we get their findings.
>
> Your point about the prompts is really interesting though. Unfortunately, as advertisers we don’t get visibility into the actual prompts/conversations that generated individual clicks, so it’s difficult to correlate those 1–10 second sessions with specific prompt types.
>
> If you don’t mind sharing: **roughly what percentage of your reported ad clicks turned into actual trackable website sessions, and what kind of signup rate did you see?** It would be really useful to compare that with our data.

### post 1tdviug — r/PPC, 2026-05-15 12:54 UTC, u/g_hock, score 62, num_comments 67

- permalink: https://www.reddit.com/r/PPC/comments/1tdviug/
- matched query terms: chatgpt ads
- title: "ChatGPT Ads beta — early CTR: 0% / 1.15% / 2.4%"

> Sharing some very early data from the ChatGPT Ads beta in case anyone else is poking at it. Caveat up front: 228 impressions across 3 ad groups is way under stat-sig.
>
>  **Setup:**
>
> * 3 ad groups, same product, same landing page, three positioning angles
> * Same daily budget cap on each
> * Time period: Went live 3 days ago
>
> **Early Results:**
>
> https://preview.redd.it/as7k3vmora1h1.png?width=1399&format=png&auto=webp&s=7e1d240c2590168ba0e3c133913a0fd7d8bafb4d
>
>  **A couple things I noticed:**
>
> 1.  Impression distribution is wildly uneven. The "Stack Replacement" angle barely got served; 16 impressions vs 125 for the top one. Either the algo is throttling based on early CTR, or that ad's failing some quality threshold I can't see. No transparency in the UI on what it could be.
> 2. The winning angle's 2.40% CTR is \~2-3x what I see on Google Display, but well under my Search benchmarks. I think that makes sense? These are conversational placements, not search-intent per se, though the platform serves these placements based on "prompt and conversation angles" that we set up.
>
> **What I still don't know:** 
>
> * Is 1-2.5% CTR good, bad, average? 
> * Whether the conversational context (what the user just asked ChatGPT) matters more than the ad copy itself
> * Click quality: I don't have any conversions yet, so we'll see how this plays out
>
>
> Anyone else running ads on ChatGPT? I'm specifically curious what you're seeing on CTR results because I'm not sure what to think about our ranges yet.

### comment olyxgon — r/PPC, 2026-05-15 15:51 UTC, u/g_hock, score 1

- permalink: https://www.reddit.com/r/PPC/comments/1tdviug/_/olyxgon/
- matched query terms: chatgpt ads

> Running an equivalent campaign on Google Search which sees 8-10%+ CTR. I'm not expecting that ChatGPT ads will have similar CTR to Google Search (different audience, intent, ad medium)

### post 1tpfmlb — r/PPC, 2026-05-27 19:17 UTC, u/g_hock, score 12, num_comments 16

- permalink: https://www.reddit.com/r/PPC/comments/1tpfmlb/
- matched query terms: chatgpt ads
- title: "Performance Update: ChatGPT Ads beta - CTR: 0.43% / 1.31% / 2.16%"

> Update on my [original /PPC post](https://www.reddit.com/r/PPC/comments/1tdviug/chatgpt_ads_beta_early_ctr_0_115_24/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
>
> **2 weeks of performance for our** [**Vibe Marketing campaign**](https://launch10.com/vibe-marketing)**:** we set up the campaign to spend $500 over 3 weeks and based on current pacing, we won't have fully deployed the budget
>
> https://preview.redd.it/124v2m31cq3h1.png?width=1594&format=png&auto=webp&s=60268d8e0d48d212e3b6ea0b30912cbe36cb4db2
>
> * **Ad Group 1: Vibe Marketing at Speed**
>    * Impressions: 2,058
>    * Clicks: 27
>    * CTR: 1.31%
>    * Avg CPC: $2.98
>    * Conversions: 4
> * **Ad Group 2: Replace the Marketing Stack**
>    * Impressions: 1,432
>    * Clicks: 31
>    * CTR: 2.16%
>    * Avg CPC: $3.23
>    * Conversions: 6
> * **Ad Group 3: Skip the Tag Manager**
>    * Impressions: 461
>    * Clicks: 2
>    * CTR: 0.43%
>    * Avg CPC: $3.23
>    * Conversions: 0
>
> A couple observations/learnings:
>
> 1. Ad Group 2 took a while to start serving and has now emerged as our top performing group
> 2. Ad Group 3 started serving impressions immediately post-launch, saw its click-thru stagnant and then decline, and then it appears to have been almost entirely suppressed
> 3. Overall, I've been happy with click-to-conversion, and I think there are a few things we'll continue to tweak to improve CTR
>
>
> Anyone else seeing CTR and conversion data start to settle into ranges that you expected or may be surprised by?

### post 1uex15e — r/PPC, 2026-06-25 02:07 UTC, u/Any_Bee_413, score 9, num_comments 7

- permalink: https://www.reddit.com/r/PPC/comments/1uex15e/
- matched query terms: chatgpt ads
- title: "1 Week Running ChatGPT Ads — 2 Early Learnings"

> Been running ChatGPT Ads for about a week now. Still no event conversions yet, so definitely too early to call it a success or failure, but I’ve picked up two things that might help others testing.
>
> **1. Context hints were too detailed at first.**
>
> My first setup was super comprehensive — I included age, gender, industries, business types, pain points, and even a long list of possible questions users might ask. Probably around 1,000 words.
>
> The result? Almost no delivery.
>
> I’m guessing I over-constrained the model.
>
> So I simplified it heavily. Cut it down to a few hundred words, removed most demographic restrictions (age/gender), and kept it more focused on business type + intent + use cases.
>
> After that, delivery started almost immediately and my full **$25/day budget** began spending consistently.
>
> **2. Personal/professional photos outperform logos by a lot.**
>
> This one surprised me.
>
> At first I used company logos and service graphics — CTR was around **0.5%**.
>
> Then I swapped in professional headshots / personal brand style images and CTR jumped to **around 5%**.
>
> Huge difference.
>
> My guess is that in a conversational environment like ChatGPT, human faces build trust faster and feel more native than brand creatives.
>
> Still very early, and no conversion events yet, but thought I’d share in case it helps others testing.
>
> Curious what others are seeing so far?

### post 1wixjbj — r/PPC, 2026-09-17 15:42 UTC, u/dmdbGroup, score 3, num_comments 7

- permalink: https://www.reddit.com/r/PPC/comments/1wixjbj/
- matched query terms: chatgpt ads
- title: "ChatGPT Ads optimizing for signups went straight to the cheapest countries: 73 signups, 0 paying customers"

> Sharing numbers from a worldwide ChatGPT Ads campaign we ran this week, because the pattern is the same trap Meta and Google have, and it showed up fast.
>
> **Setup:** worldwide geo, bidding on a signup conversion sent server side. SaaS product with a free tier, so a signup costs the user nothing.
>
> **What happened in 4 days:**
>
> * 73 signups, 0 of them became paying customers.
> * India was 59 of the 73, at roughly 1.36 CAD per signup. 47 of those arrived in one burst right after the daily budget reset at midnight New York time.
> * Once India, Egypt, Algeria, Morocco and Tunisia stopped delivering, the UAE picked up: 36 signups in about five hours in another campaign, from a country that had not delivered at all the day before.
> * Brazil and Iraq each took 88 clicks with zero conversions.
>
> **These were real people, not bots.** Distinct addresses, some real small businesses. They just weren't going to pay. In the UAE batch, about one in five did anything at all after signing up.
>
> **What we took from it:**
>
> 1. If you bid on a free action, the bidder finds whoever does that free action cheapest. Every cheap signup you report teaches it to find more of them.
> 2. Judge a country by payers, not by signups. On signups alone, India looked like the best market in the account.
> 3. Watch the hour after the budget reset. That's when a cheap country can eat most of a day's budget before you look.
> 4. The paying customers we did get came from the US, Australia and Canada. So we're moving to a country list plus optimizing on a paid event, even though that event is much rarer.
>
> Has anyone tried optimizing ChatGPT Ads on a purchase event yet? Curious whether it has enough volume to learn.

### post 1v7z6ik — r/marketing, 2026-07-27 12:37 UTC, u/dutchking90, score 23, num_comments 45

- permalink: https://www.reddit.com/r/marketing/comments/1v7z6ik/
- matched query terms: chatgpt ads, openai ads
- title: "Anyone Seeing Success with OpenAI Ads?"

> We started some light testing for a broad topic and we're seeing a CPM of $47 over the last month. I don't see this as a beneficial ad platform for our demographic anyways so likely shutting it down, but curious if anyone has found any success with ChatGPT ads.

### post 1te9kan — r/PPC, 2026-05-15 21:19 UTC, u/Single-Sea-7804, score 9, num_comments 20

- permalink: https://www.reddit.com/r/PPC/comments/1te9kan/
- matched query terms: chatgpt ads
- title: "My Experience with Chat GPT Ads"

> https://preview.redd.it/zz8cewrwad1h1.png?width=2277&format=png&auto=webp&s=ce630b7edd22d92d5855cac0a3c523849820492e
>
> There's alot of freelancers and agencies here looking to scale their ads but don't spend on PPC because CPC's are like, $500+, and facebook is a minimum $500 CPA for a qualified lead nowadays. So i though i might try ChatGPT Ads  
>
> Now i've only been running this for a couple days, but this has been doing okay-ish and I managed to get clicks for less than $6 CPC . Which is actually pretty awesome, if the traffic was equally as awesome. 
>
> I got one conversion from France, even though my location was set to USA. My CTA was a free PPC Audit, I didn't put crazy effort into it, but it seems as more people join, the CPCs increase. I only managed to spend on the $6 CPCs until yesterday where it stopped spending. 
>
> Not bad, not great, but i expected the results to be more intent. Sharing for transparency, and want to hear what others have experienced!

### post 1wenxp3 — r/PPC, 2026-09-12 20:53 UTC, u/dmdbGroup, score 2, num_comments 9

- permalink: https://www.reddit.com/r/PPC/comments/1wenxp3/
- matched query terms: chatgpt ads
- title: "ChatGPT Ads: Ads Manager and the conversions API gave different numbers for the same day. Here's how we checked which one was right"

> We're running conversion campaigns on ChatGPT Ads and hit something that might save someone a few hours.
>
> For Sept 11 (account time zone), Ads Manager shows 4 conversions. The conversions insights endpoint in their API returns 18 for the same day. When we pulled single days for a week earlier on, the daily API totals added up to more than the API's own total for that week, so we don't trust the daily API number yet.
>
> How we worked out the real number:
>
> 1. **Log every server-side conversion you send**, including whether it carried the ad click id from the landing page URL. That log is the ground truth, not either dashboard.
> 2. **The click id on the landing URL has the click time inside it.** It's a Fernet token, and bytes 1 to 8 of the decoded token are a unix timestamp. Our signups were 1 to 2 minutes after the click, same day, so "it got attributed to a different day" wasn't the answer.
> 3. **Send the same event id from the pixel and the server.** We use one id per account for the signup, so if both fire it counts once, not twice.
> 4. **Don't send EU, UK or Swiss visitors who haven't consented.** If you target those countries, your signup count and your conversion count won't match, and that's expected.
>
> Result: 3 signups that day carried the click id. Ads Manager's 4 lines up with that plus one more we think they matched through their cookie. For now we read Ads Manager once the day is over and ignore the API's single-day number.
>
> Anyone else on ChatGPT Ads seeing the API and Ads Manager disagree?

### comment pbgyj7z — r/PPC, 2026-09-23 00:05 UTC, u/potatodrinker, score 1

- permalink: https://www.reddit.com/r/PPC/comments/1wnnyry/_/pbgyj7z/
- matched query terms: chatgpt ads

> Yep give it a go. My local Sydney ChatGPT ads manager suggested not repeating the words too much in each adgrounds context hint text box. For me I'm in home services so phrased the same thing in slightly different ways 
>
> *Homeowner or landlord looking for painters for their property to boost sale price, (2nd prompt starts here) painting services to retouch a house or apartment ahead of putting it to market for selling.*
>
> The same thing worded in 2 different ways and using only ONE comms to separate the first prompt from the second. Been running this about 4 days and CTR is a bit better. Around 0.8% now. Apparently 1% is the target to aim for

### comment om0w6fi — r/PPC, 2026-05-15 21:29 UTC, u/Munalytics, score 2

- permalink: https://www.reddit.com/r/PPC/comments/1tdviug/_/om0w6fi/
- matched query terms: chatgpt ads

> Started with chatgpt ads, definitely notice CTR is "lower" than other channels such as google ads. Only been a few days for us as well so too early to really say these are solid results (currently sitting at around 0.8%). 
>
> Couple of things I have noticed/assumptions:  
> \- Targeting is a little broad, not super stoked by what queries our ads are showing against  
> \- People tend to go to chatgpt for answers, I am not sure if they are actively looking for solutions, consider they're asing "How should I manage the emails I receive as a lawyer" they may not be looking for a product, but rather how they can organize their inbox.  
> \- Intent - ties into the last point. Some of the queries I see us showing up against aren't really people looking for a product or solution but rather information. Trying to get them to purchase a product at this point probably won't work. 
>
> Still definitely testing and trying to tighten up what queries the ads themselves show up against I think will be key to improving CTR and generating conversions. For the time being treating it more similar to "awareness" almost more top of the funnel.


## Class — metric stated, window unstated

### comment pacw1r4 — r/PPC, 2026-09-17 12:39 UTC, u/Economy_Pay_7487, score 1

- permalink: https://www.reddit.com/r/PPC/comments/1v961ix/_/pacw1r4/
- matched query terms: chatgpt ads

> Yeah, we tested ChatGPT Ads for ZapDigits mainly around client reporting / agency reporting and ended up getting some pretty interesting results.
>
> We were targeting people searching for ways to automate client reports, white-label reporting, marketing dashboards, etc.
>
> Rough numbers from the test:
>
> * Spend: \~$4,800
> * Impressions: \~310k
> * Clicks: \~8,900
> * CTR: \~2.9%
> * Avg. CPC: \~$0.54
> * Signups: 620
> * Paid conversions: 87
> * CAC: \~$55
>
> The biggest thing we noticed was that the traffic was pretty relevant. A lot of the people coming in were agency owners or account managers who were specifically looking for ways to make client reporting less painful.
>
> We also found that the more specific the messaging was around agency/client reporting, the better it performed. Generic "marketing reporting software" ads weren't nearly as good.
>
> Still relatively early for us, but we've kept running tests because the CAC was reasonable compared with some of the other channels we've tried.

### post 1w4nmuv — r/PPC, 2026-09-01 20:05 UTC, u/Chiefer2, score 4, num_comments 7

- permalink: https://www.reddit.com/r/PPC/comments/1w4nmuv/
- matched query terms: chatgpt ads, openai ads
- title: "Open AI Ad Platform Metrics Vs GA4"

> Looking to hear from others currently running campaigns on ChatGPT. 
>
> We have, in recent weeks, gained access to OpenAI Ads. Our company has put a small amount of dollars towards testing the platform. 
>
> Following roughly the same sentiment we would follow on other platforms, we are running with Page Viewed conversions as our Conversion goal (just for now as we see the quality of traffic being sent over). 
>
> However, only 70.2% of clicks get recorded as a Page Viewed conversion. I figure this would be misclicks or people who couldn't load the page and gave up - fine. 
>
> The more concerning part to me is the variance of Page Viewed Conversions to GA4 metrics between each ad group we are testing (all one campaign with same tracking parameters). 
>
> Ad Group A has GA4 reporting at 97.2% of what Open AI is reporting for Conversions (Awesome!), Ad Group B shows 63.5% representation, and Ad Group C only records at 39%. 
>
> I have QA'd all ads using a Pixel Helper to ensure that the Page Viewed conversion is firing, and it is indeed correctly attributing on my tests. 
>
> Is anyone else experiencing such discrepancies? Let me know your experience so far.

### post 1vfj2yv — r/PPC, 2026-08-04 18:41 UTC, u/Cosmonaut_17, score 0, num_comments 4

- permalink: https://www.reddit.com/r/PPC/comments/1vfj2yv/
- matched query terms: chatgpt ads, openai ads
- title: "ChatGPT Ads data archive"

> I’ve been hearing very mixed things on ChatGPT/OpenAI ads CPC and conversion metrics. No real case studies exist yet and data is all over the place, mostly buried deep in subreddits.
>
> I’ve figured let’s change this. Everybody that has tried running ChatGPT ads, post your data here, so we have an archive that can be used as a benchmark for anyone that is considering giving it a try. Please share:
>
> \- CPM/CPC and conversions data if you have  
> \- what industry the brand is in  
> \- campaign setup (if anything special)
>
> I’ll start:
>
> I ran one small campaign:  
> \- CPC $7-8, don’t have conversion data yet  
> \- software, developer focused  
> \- kept it deliberately broad but I actually doubt this is the best channel to reach my audience

### comment p9xhasr — r/PPC, 2026-09-15 10:19 UTC, u/potatodrinker, score 13

- permalink: https://www.reddit.com/r/PPC/comments/1wggcah/_/p9xhasr/
- matched query terms: chatgpt ads

> If you export your ad results you'll find the contextual hints will break each comma into its own prompt. So "target homeowners looking for painters, color guides" has two prompts:
>
> 1. Target homeowners looking for paints
> 2. Colour guides (which is vague AF)
>
> Be careful with comma use. I only realised too late and copped a weak CTR of 0.65%, extreme CPA so ChatGPT ads is off my media plan for a while.
>
> 2 cents from this home services marketplace PPC team lead.

### post 1vor980 — r/PPC, 2026-08-15 02:52 UTC, u/TreePube, score 10, num_comments 12

- permalink: https://www.reddit.com/r/PPC/comments/1vor980/
- matched query terms: chatgpt ads
- title: "ChatGPT Ads"

> They seem to be really disappointing so far, supposed CPC comes in cheap for my industry but the over attribution is lunacy. Says 50 clicks a day but in a controlled test environment I know it’s more like 5-10. 
>
> Anyone actually having success here?

### post 1ti2rjq — r/PPC, 2026-05-19 22:35 UTC, u/potatodrinker, score 18, num_comments 15

- permalink: https://www.reddit.com/r/PPC/comments/1ti2rjq/
- matched query terms: chatgpt ads
- title: "How's ChatGPT ads going for advertisers?"

> Hi community. Aussie here (in-house corporate PPC).
>
> Our media agency got invited to trial out ChatGPT ads (CPM only buy) and I'm curious how others already advertising (US I imagine) are going. Is it pretty expensive CPA wise compared to Google ads search, or going ok?  Not fussed about industry or B2C/B2B. Looking for snippets of anecdotes and any tips if you can spare some.
>
> The trial I have is $5k USD minimum outlay, no time frame, $50 USD CPM which is quite steep ($15 USD is "normal" here in AU).
>
> Thanks in advance!

### post 1u79yzb — r/PPC, 2026-06-16 10:43 UTC, u/Leading-Praline7927, score 1, num_comments 5

- permalink: https://www.reddit.com/r/PPC/comments/1u79yzb/
- matched query terms: chatgpt ads
- title: "Zero impressions/clicks in chatgpt ads"

> I recently created chatgpt ads account and launched a campaign with the total budget for the campaign(goal - clicks) is ($20) .included (usa,uk, Aus,,NZ) . My budget got spent with an hour but got zero impressions and clicks. As far as I checked there is nothing seemed to be an issue from my end. Had setup based pixel using gtm. Is there any reporting lag in the dashboard or am I doing something wrong here  but there should have been impressions for the budget that spent. But i got nothing.
>
> The reporting seems blunt . But y te dashboard shows nothing even though the budget got spent for the campaign.

### comment os1rr7m — r/PPC, 2026-06-16 19:53 UTC, u/Leading-Praline7927, score 1

- permalink: https://www.reddit.com/r/PPC/comments/1u79yzb/_/os1rr7m/
- matched query terms: chatgpt ads

> Yeah it's $3/click. I had setup the base pixel tag using gtms and ran a campaign. It's just budget got over within an hour for a cpc campaign. But I didnt see any impression or clicks. The ads dashboard shows zero..but  I can see the traffic in GA4 for chatgpt ads. it could be a reporting delay of 7hrs in ads dashboard ig

### post 1w1nake — r/PPC, 2026-08-29 13:59 UTC, u/cole-interteam, score 1, num_comments 0

- permalink: https://www.reddit.com/r/PPC/comments/1w1nake/
- matched query terms: openai ads
- title: "OpenAI Ads can spend 7x your daily budget"

> Had a day recently where both of our OpenAI Ads accounts had campaigns that 2x'd their daily budget so I reached out to their team asking for a refund.
>
> They told me that OpenAI Ads will spend 7x your daily budget if they want to 😮
>
> I know Google has similar budget rules, but caps at 50% I believe. 7x is outrageous. 
>
> Anyways, this pissed me off so I thought I'd share with the community and hopefully warn people.
>
> Ignoring daily ad budgets should be illegal.


## Class — claim-without-metric

### post 1uf870t — r/PPC, 2026-06-25 12:09 UTC, u/Fractionalcmoz, score 24, num_comments 24

- permalink: https://www.reddit.com/r/PPC/comments/1uf870t/
- matched query terms: chatgpt ads
- title: "My thoughts on ChatGPT Ads"

> From where they started to now, they have already made a lot of improvements. However, only a few niches have worked well for us. Here are some points I’ve gathered after spending around 34,000 usd across different niches. 
>
> 1. Niches that did well: home services, car rental, international real estate, PI and DWI law
>
> 2. Niches that did not do well: criminal defense law, tours, employment law, saas startup, dental
>
> 3. We followed a simple playbook where we define all the questions someone would ask before, during, after. Before they need the service, during the moments they feel they might need the service/ product, and after they decide they are going to need it. 
>
> 4. It seems to work in pulses. We typically noticed it would have incremental effects in regards to clicks and conversions, then drop off for a bit… then pick up again. Almost like 3 days on, 1-2 days off. 
>
> 5. We added the top performing queries into our Google ads campaigns and noticed they performed much better there as well(we have revisited the way we set up campaigns in Google ads because of this… not enough data to determine anything yet.) 
>
> 6. We used this data to help us create content for aeo purposes and schema updates for seo. 
>
> Overall, not too bad and making sure to use it for other marketing purposes. I feel it gives you the best true view of what your audience is actually searching and clicking on/ converting on.

### post 1ueoci2 — r/PPC, 2026-06-24 20:04 UTC, u/TheADLeaf, score 33, num_comments 40

- permalink: https://www.reddit.com/r/PPC/comments/1ueoci2/
- matched query terms: chatgpt ads, openai ads
- title: "Thoughts on ChatGPT Ads 3+ Weeks In"

> Got access to Openai's Ad Manager a few weeks ago and dropped everything to go play around with OpenAI's new tool. Immediately got some campaigns set up with a few core services to see how the platforms would be. Overall, it's pretty standard compared to other ad management platforms but definitely on the bare side (I guess this makes sense being that it's still in beta). 
>
> Tested two campaigns at the start - one on a lifetime budget to see how pacing would be managed and the other on a daily. I won't go too in-depth on setup specifics here but happy to discuss if someone wants to reach out.
>
> I did find the targeting portion interesting as there are you're typical location and demographic settings, and instead you have a large contextual targeting text block. Fast forward post creative and copy setup (there's no video option at the moment), traffic and form submissions started coming in that same evening. 
>
> OpenAI's tracknig isn't all there yet but with a standard UTM and some backend tools it's not an issue. Quality from conversions is mid-to-bottom funnel for a much better cost compared to Google in the past. We've closed a few new clients already in the first few weeks so we're seeing a huge success.
>
> Week 3 Update: 
>
> Lifetime budget pacing is not optimized - waiting for OpenAI to come out with a ad schedule setting (fingers crossed). Daily is still the way to go for most platforms in my eyes. We've also found the ads convert better with some form of chatbot configured with the landing page which you'd think would be true in most cases but definitely outshined here.
>
> Curious to know how others exepriences are going?

### post 1wggcah — r/PPC, 2026-09-14 21:14 UTC, u/NoArticle1930, score 10, num_comments 20

- permalink: https://www.reddit.com/r/PPC/comments/1wggcah/
- matched query terms: chatgpt ads
- title: "Been testing ChatGPT Ads, a few things I didn’t expect"

> I’ve been trying ChatGPT Ads on one of my own products and thought I’d share what I’ve noticed so far.
>
> The first thing is that the Context Hints don’t seem to make a huge difference to the exact prompts where the ad shows up. I thought adding more specific hints would make it appear on more relevant questions, but that hasn’t really been the case for me.
>
> What surprised me more is that the actual content on the website seems to matter a lot. The way the homepage and landing page are written seems to affect which prompts the ad appears on more than I expected.
>
> The other weird thing is the traffic pattern. It’s not steady at all. I’ll suddenly get a bunch of impressions and a few clicks, then nothing for a couple of hours, then it starts again.
>
> So far I’d say it does work I’ve had clicks and a few signups but it still feels a bit unpredictable.
>
> Would be interested to know if anyone else is seeing the same thing, especially with the website content affecting where the ad appears.

### post 1uw727c — r/PPC, 2026-07-14 12:18 UTC, u/Capable_Report4502, score 2, num_comments 8

- permalink: https://www.reddit.com/r/PPC/comments/1uw727c/
- matched query terms: chatgpt ads
- title: "ChatGPT Ads for B2B"

> Hey folks, I've been testing ChatGPT Ads a few weeks for a B2B Industrial/Manufacturing business and I'm getting very low conversion rates and poor lead quality. We're pointing it to a dedicated LP that we know works well on paid search and paid social
>
> Is anyone else seeing the same issues?

### post 1w7xyea — r/PPC, 2026-09-05 11:15 UTC, u/code_x_7777, score 3, num_comments 12

- permalink: https://www.reddit.com/r/PPC/comments/1w7xyea/
- matched query terms: chatgpt ads
- title: "Anybody positive experience with ChatGPT ads?"

> Hi, we have been moving some of our businesses' Meta ad budget to ChatGPT ads. I made a few hundred ads so far but my cost per conversion has been higher than Meta - significant higher. I'm sure it's just my incapability to make it work. Any "secret" tips that has been working for you?

### comment p0ahclu — r/marketing, 2026-07-28 16:16 UTC, u/katefromqueens, score 3

- permalink: https://www.reddit.com/r/marketing/comments/1v7z6ik/_/p0ahclu/
- matched query terms: chatgpt ads

> 47 CPM is brutal. We tested ChatGPT ads for a B2B SaaS and pulled the plug fast. The inventory is thin and targeting is nonexistent vs Meta or LinkedIn. Might work for high-ticket enterprise where one deal covers the spend, but for volume it makes no sense right now.

### comment pb7ulhg — r/PPC, 2026-09-21 18:49 UTC, u/kokoshkatheking, score 1

- permalink: https://www.reddit.com/r/PPC/comments/1wmaxss/_/pb7ulhg/
- matched query terms: chatgpt ads

> I think they are trying to have high CPC a bit too early. They should first let us get real value from inventory, get hooked and then Google us in the ass.  
> I made some test and some users seems genuinely with actual intent like from Google Ads, but most look like my ads was shown on something that was not related.  
> So I get very bad conversion from landing page, very bad activation from subscriptions (like users subscribe and realize quite fast that they have no idea why they are here) but the few that activate are the real thing.
>
> Also I’m wondering if the fact that ads are shown only to free users is not making users from ChatGPT Ads less willing to pay than the one on Google. I mean users with money just pay for chatGPT … \~$30 per month for a chatbot with one of the best LLM model is a very good deal right now.

### comment p81b6jg — r/PPC, 2026-09-05 20:13 UTC, u/EssenzaVital, score 1

- permalink: https://www.reddit.com/r/PPC/comments/1w7zdpg/_/p81b6jg/
- matched query terms: chatgpt ads

> Thanks for your comment. 
>
> We stopped the ads for now. A friend of mine runs ads for his company as well and has already spent over €1,000 on ChatGPT Ads, and they’re seeing basically the same issue.  
> I completely understand that ads need time to optimize. We’ve run Google Ads before and it took around two weeks before performance really started to improve. The difference is that with Google, the clicks we were being charged for actually showed up in Shopify/analytics as real visits.
>
> With ChatGPT Ads, a large part of the reported clicks simply doesn’t seem to match the actual traffic we can verify, and many of the visits we do see are only 1–5 seconds long. That’s the part that concerns us, not simply the fact that there were no conversions yet.  
> So for now we paused everything until we understand what’s happening with the traffic and reporting.


## Class — third-party measurement (not an advertiser's own result)

### post 1vsx4ep — r/PPC, 2026-08-19 19:51 UTC, u/zhao_hanbo, score 1, num_comments 11

- permalink: https://www.reddit.com/r/PPC/comments/1vsx4ep/
- matched query terms: chatgpt ads
- title: "I analyzed 3,602 ChatGPT ad placements. Paying did NOT get brands into the answer."

> Short version: paying for a ChatGPT ad puts you next to the answer. In this data it did
> not put you into it.
>
> Disclosure: I work at Nile, which sells product data infrastructure for AI commerce. The
> dataset is not ours, it is public, and everything below is reproducible.
>
> The data: 3,602 ChatGPT ad placements, 191 advertisers, 139 prompts, collected March 8 to
> April 12 2026 by researchers at Penn and Haverford and released publicly. They asked who
> gets shown which ads. I asked whether the brand paying shows up in the answer text.
>
> Raw result: **8.0%** of paid placements had the advertiser named in the response.
>
> That number has an obvious problem, so let me deal with it before anyone raises it. Nike
> ads run on shoe questions, and shoe answers name Nike whether Nike paid or not. So I
> paired every (brand, prompt) combination and compared naming rates with the ad running
> against the same prompt with it not running. Same question, same brand.
>
> 91 comparable pairs. Average difference: **-0.3 percentage points**.
>
> Where the spend lands matters much more than whether you paid:
>
> | Topic | Ad placements | Advertiser named |
> |---|---|---|
> | purchasable_products | 665 | **32.0%** |
> | specific_info | 314 | 7.6% |
> | cooking_and_recipes | 500 | **0%** |
> | how_to_advice | 441 | **0%** |
> | health_fitness_beauty | 385 | **0%** |
>
> **49.8% of all placements** landed on topics where advertisers were named zero times. If you
> are buying broad, roughly half your impressions are in conversations that never produce a
> brand name at all.
>
> Of 32 brands that paid inside purchasable_products, 15 never appeared in a single answer.
>
> Two numbers from opposite ends: Zoom paid for zero placements and was named 101
> times. Mercari paid for 66 placements and was named zero times.
>
> Limits: this window predates the international rollout and the multi-product carousel, so
> treat it as a Q1 2026 baseline. 91 pairs is thin. Text matching cannot detect a carousel
> that shows a brand without naming it in prose, so "named in the answer" is narrower than
> "shown to the user".
>
> My read, and this part is inference rather than something the data proves: the ad slot and
> the recommendation slot look like separate systems with separate inputs, and paying is an
> input to the first one only.
>
> Full methodology, the complete topic table, and credits to the original researchers:
> https://nile.app/blog/chatgpt-ads-paid-vs-recommended/?utm_source=reddit&utm_medium=social&utm_campaign=chatgpt-ads-paid-vs-recommended&utm_content=r-ppc
>
> If you are running ChatGPT Ads right now, I would like to know whether your own
> placement-to-mention numbers look anything like this.


## Class — question/complaint

### post 1v961ix — r/PPC, 2026-07-28 18:00 UTC, u/OctaviusTrail, score 7, num_comments 35

- permalink: https://www.reddit.com/r/PPC/comments/1v961ix/
- matched query terms: chatgpt ads
- title: "Anyone that have had success with ChatGPT ads?"

> Hello    
> I feel like ChatGPT ads have been around for a bit, but I rarely hear anybody talk about them. Anyone that have any experience or insights they want to share?    
> Also very keen to know if anybody has successfully created a campaign with good ROAS.

### post 1u96mov — r/PPC, 2026-06-18 13:42 UTC, u/crimsonparkdigital, score 17, num_comments 22

- permalink: https://www.reddit.com/r/PPC/comments/1u96mov/
- matched query terms: chatgpt ads
- title: "Is anyone actually seeing meaningful results from ChatGPT Ads yet?"

> We’ve been considering testing ChatGPT Ads across a few accounts and are curious what others are seeing...
>
>
>
> Right now it still feels pretty experimental. Wondering if anyone is getting different results so far.
>
>
>
> Are you getting:
>
>
>
> 1. Quality traffic that actually converts?
>
> 2. Just curiosity clicks / low-intent users?
>
> 3. Mostly test budgets with unclear performance so far?
>
>
>
> Would love to hear what other agencies and marketers are seeing, and if any verticals are actually performing well yet.

### post 1u8cgkv — r/PPC, 2026-06-17 14:55 UTC, u/Substantial-Kiwi8796, score 6, num_comments 12

- permalink: https://www.reddit.com/r/PPC/comments/1u8cgkv/
- matched query terms: chatgpt ads
- title: "ChatGPT ads"

> Anyone on here have experience with chatgpt ads? Trying to run them for my local service business. Need some basic info aswell as help setting up conversion tracking. Willing to pay.

### post 1whtozp — r/digital_marketing, 2026-09-16 10:44 UTC, u/rank_crafted, score 11, num_comments 19

- permalink: https://www.reddit.com/r/digital_marketing/comments/1whtozp/
- matched query terms: chatgpt ads
- title: "Has anyone here tried running ads on ChatGPT? What were your results compared to other ad platforms?"

> I’m thinking about running ChatGPT ads for one of my clients. They have a **home health care services business**, offering services like patient care, nursing care, elderly care, physiotherapy, and doctor consultations at home.
>
> Before I start, I’d like to know:
>
> * Has anyone actually run ChatGPT ads for a service-based business?
> * What kind of results did you get leads, conversions, cost per lead, etc.?
> * How does it compare with Google Ads and Meta Ads?
> * Is ChatGPT advertising useful for **local home healthcare services**, where people are actively looking for a service?
> * What should I keep in mind before spending money?
>
> I’m mainly looking for **real experiences and honest feedback**, especially from people who have already tested ChatGPT ads for lead generation or local services.

### post 1whn673 — r/PPC, 2026-09-16 04:37 UTC, u/Accomplished_Pay_948, score 1, num_comments 6

- permalink: https://www.reddit.com/r/PPC/comments/1whn673/
- matched query terms: AI Overviews ads
- title: "Is anyone actually getting anything out of ads in AI Overviews, or is it just a reason to sell you broad match?"

> Honest question, because I can't get a straight answer out of anyone including our rep.
>
> We're a clinic chain in India, 8-10 locations in each of the big cities. GMBs are well rated so the map pack already does most of the work for us. Paid is there to plug the gaps, push the location assets in the pockets where we just don't show up. Bidding is max clicks, not conversions, with a CPC ceiling we work out ourselves from the funnel, so we're never paying more for a click than it's worth to us.
>
> Every AI Max pitch I've sat through is basically, do this and you'll turn up in AI Overviews. Then I go and read the docs and search term matching needs conversion based smart bidding, so on max clicks I can't get in anyway. So the actual ask is change how we bid altogether, which is a much bigger conversation than trying out a new placement.
>
> Also there's no opt out and it isn't split out in reporting, so it could already be happening to me and I'd have no idea.
>
> So is anyone getting real volume out of AIO? Not impressions, traffic you can actually point at. Particularly anyone local, on near me type queries where the person already knows what they want and just wants the closest one.

### post 1va4i23 — r/PPC, 2026-07-29 18:23 UTC, u/psydencrafts, score 1, num_comments 3

- permalink: https://www.reddit.com/r/PPC/comments/1va4i23/
- matched query terms: chatgpt ads
- title: "First time testing ChatGPT Ads for a B2B software company,  any advice?"

> I’m planning my first ChatGPT Ads test for a B2B software company and would appreciate input from anyone who has already used the platform.
>
> My current strategy is intentionally simple:
>
> \* One campaign
>
> \* One ad group
>
> \* One ad
>
> \* US targeting
>
> \* CPC bidding
>
> \* Minimum budget of around $25 per day
>
> \* 14-day initial test
>
> \* Existing dedicated landing page
>
> \* Confirmed demo booking as the primary conversion
>
> For targeting, I’m planning to use conversational context hints around:
>
> \* Businesses replacing spreadsheets or manual processes
>
> \* Teams looking for simpler software
>
> \* Companies trying to centralize records and workflows
>
> \* Operations managers comparing B2B software options
>
> \* Growing businesses that have outgrown manual tracking
>
> I’ll use separate ChatGPT Ads UTMs, GA4, GTM and confirmed booking tracking. I’m not planning to judge performance only by CTR. The main metric will be the cost per qualified demo booking and sales feedback about lead quality.
>
> Since ChatGPT Ads are still relatively new and reliable B2B benchmarks are limited, I’m treating this as a controlled learning test rather than expecting immediate scale.
>
> For anyone already running ChatGPT Ads:
>
> \* Are broad problem-based context hints working better than product-specific hints?
>
> \* Are you getting meaningful B2B leads or mostly low-intent clicks?
>
> \* Have shorter context hints delivered better than detailed ones?
>
> \* What attribution or tracking problems have you experienced?
>
> \* How long did it take before your campaign started delivering consistently?
>
> \* What mistakes should a first-time advertiser avoid?
>
> I’d appreciate practical feedback from anyone who has tested the platform with a real budget.

## Pull notes — mechanical only

- Timestamps converted from `created_utc` to UTC dates; permalinks built from subreddit + id (+ link_id for comments); not opened live.
- `query=` search on Arctic Shift matched words, not exact phrases; `title=` search matched title words only, so posts naming the engine only in the body were missed in runs 4.
- Another agent's Arctic Shift job (process `rs3.py`, /tmp/reddit) ran concurrently on the same API; timeouts may be partly load from both.
- Unreachable this pull: live reddit.com (extension refuses the domain; not tried per rule); Wayback capture of any kept permalink (only a verification page found); r/SaaS S5 aggregates (see the S5 file).

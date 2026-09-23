# Reddit (Arctic Shift archive) — S5 community-thread counts for GEO / AEO / AI-visibility terms in ten practitioner subreddits, March–September 2026

```yaml
source:          Reddit posts, counted by the Arctic Shift open archive API aggregate endpoint (arctic-shift.photon-reddit.com)
channel:         Arctic Shift archive of reddit.com
url_or_doc_id:   https://arctic-shift.photon-reddit.com/api/posts/search/aggregate?aggregate=created_utc&frequency=month&subreddit=<sub>&query=<term>&after=2026-03-01&before=2026-09-24 ; .../aggregate?aggregate=author&subreddit=<sub>&query=<term>&after=2026-03-01&before=2026-09-24&limit=5000
published:       archive counts as of the pull; posts created 2026-03-01 to 2026-09-23
pull_date:       2026-09-23
pull_method:     curl / python urllib (User-Agent "Mozilla/5.0 research-pull/1.0"); no browser; archive copy, not live
pull_purpose:    evidence about a number
tier:            5
tier_reason:     demand-signals.md S5 default is 4 when the platform publishes counts; these are an archive's counts, not Reddit's — archive copy, not live reddit; archive coverage unverified; no permalink verified by another path (see b-reddit-advertiser-reports-repull2-2026-09-23.md). Held at 5 per brief
source_label:    measured-by-us (counts computed by the archive API on our query)
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      docs/raw/f-signal-hr-S5-community-2026-09-22.md (reddit.com 403) for the Reddit component only
captured:        monthly thread counts and window unique-author counts per subreddit × query
verbatim:        full (API values as returned)
```

## Exact queries

- Subreddits: r/PPC, r/marketing, r/SEO, r/digital_marketing, r/advertising, r/bigseo, r/adops, r/ecommerce, r/SaaS, r/startups. Consumer subreddits (r/insurance, legal-advice subs) not queried, per brief.
- `query` values sent, each separately: `"generative engine optimization"` (with quotes), `GEO`, `"AI visibility"` (with quotes), `AEO`. Posts only (threads), not comments.
- Thread count per month = `aggregate=created_utc&frequency=month`. Unique posters = number of distinct `author` keys from `aggregate=author` over the whole window 2026-03-01 to 2026-09-24 ([deleted] counted as one key). Unique posters per month were not pulled (run 1, which pulled per-month authors, was stopped for time).
- Cross-check: for every row with both aggregates, the sum of the monthly buckets equals the author-aggregate total.

[note: `GEO` is a bare token and also matches geo-targeting and geography threads, especially in r/PPC and r/adops; no disambiguation was applied. `query` semantics (word vs phrase match for quoted terms) are the archive's and are not documented on the response.]

## Threads per month — `aggregate=created_utc&frequency=month`, bucket labels verbatim

[note: bucket labels are the API's own `created_utc` strings. 2026-02-28T23:00:00.000Z is 2026-03-01 00:00 in UTC+1, so the seven buckets are March to September 2026 in the archive's local month; September runs to the `before` bound 2026-09-24.]

| subreddit | query sent | Mar (2026-02-28T23Z) | Apr (2026-03-31T22Z) | May (2026-04-30T22Z) | Jun (2026-05-31T22Z) | Jul (2026-06-30T22Z) | Aug (2026-07-31T22Z) | Sep to 09-23 (2026-08-31T22Z) | window total | unique authors, window | rows by [deleted] | error |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| r/PPC | `"generative engine optimization"` | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | |
| r/PPC | `GEO` | 10 | 6 | 13 | 5 | 2 | 7 | 7 | 50 | 47 | 0 | |
| r/PPC | `"AI visibility"` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | |
| r/PPC | `AEO` | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 3 | 3 | 0 | |
| r/marketing | `"generative engine optimization"` | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 2 | 0 | |
| r/marketing | `GEO` | 12 | 14 | 4 | 4 | 5 | 0 | 1 | 40 | 36 | 4 | |
| r/marketing | `"AI visibility"` | 2 | 6 | 3 | 0 | 1 | 1 | 2 | 15 | 14 | 2 | |
| r/marketing | `AEO` | 0 | 5 | 2 | 2 | 1 | 2 | 0 | 12 | 12 | 1 | |
| r/SEO | `"generative engine optimization"` | 7 | 5 | 12 | 10 | 4 | 5 | 1 | 44 | 37 | 2 | |
| r/SEO | `GEO` | 84 | 123 | 86 | 85 | 65 | 49 | 33 | 525 | 418 | 17 | |
| r/SEO | `"AI visibility"` | 26 | 31 | 18 | 30 | 27 | 20 | 16 | 168 | 140 | 15 | |
| r/SEO | `AEO` | 35 | 52 | 41 | 38 | 41 | 28 | 24 | 259 | 210 | 18 | |
| r/digital_marketing | `"generative engine optimization"` | 2 | 1 | 5 | 3 | 3 | 0 | 1 | 15 | 14 | 0 | |
| r/digital_marketing | `GEO` | 20 | 16 | 22 | 19 | 13 | 4 | 1 | 95 | 82 | 2 | |
| r/digital_marketing | `"AI visibility"` | 19 | 11 | 24 | 7 | 13 | 5 | 3 | 82 | 70 | 3 | |
| r/digital_marketing | `AEO` | 13 | 8 | 18 | 14 | 9 | 3 | 3 | 68 | 54 | 3 | |
| r/advertising | `"generative engine optimization"` | 1 | 2 | 0 | 1 | 0 | 0 | 0 | 4 | 4 | 0 | |
| r/advertising | `GEO` | 5 | 4 | 3 | 5 | 0 | 1 | 1 | 19 | 17 | 1 | |
| r/advertising | `"AI visibility"` | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | |
| r/advertising | `AEO` | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 4 | 0 | |
| r/bigseo | `"generative engine optimization"` | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 4 | 1 | 4 | |
| r/bigseo | `GEO` | 10 | 7 | 10 | 12 | 10 | 5 | 16 | 70 | 62 | 5 | |
| r/bigseo | `"AI visibility"` | 4 | 7 | 3 | 3 | 4 | 4 | 2 | 27 | 21 | 5 | |
| r/bigseo | `AEO` | 6 | 8 | 8 | 5 | 3 | 6 | 5 | 41 | 37 | 3 | |
| r/adops | `"generative engine optimization"` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | |
| r/adops | `GEO` | 9 | 4 | 2 | 1 | 2 | 4 | 6 | 28 | 24 | 0 | |
| r/adops | `"AI visibility"` | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | |
| r/adops | `AEO` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | |
| r/ecommerce | `"generative engine optimization"` | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 4 | 4 | 0 | |
| r/ecommerce | `GEO` | 4 | 1 | 8 | 6 | 2 | 1 | 1 | 23 | 22 | 0 | |
| r/ecommerce | `"AI visibility"` | 5 | 3 | 3 | 2 | 0 | 2 | 0 | 15 | 15 | 0 | |
| r/ecommerce | `AEO` | 0 | 1 | 3 | 3 | 1 | 0 | 0 | 8 | 7 | 0 | |
| r/startups | `"generative engine optimization"` | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 3 | 3 | 0 | |
| r/startups | `GEO` | 1 | 2 | 3 | 4 | 3 | 1 | 0 | 14 | 12 | 0 | |
| r/startups | `"AI visibility"` | 1 | 3 | 1 | 2 | 0 | 3 | 0 | 10 | 9 | 0 | |
| r/startups | `AEO` | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 4 | 4 | 0 | |
| r/SaaS | `"generative engine optimization"` | — | — | — | — | — | — | — | — | — | — | Timeout. Maybe slow down a bit / Timeout. Maybe slow down a bit |
| r/SaaS | `GEO` | — | — | — | — | — | — | — | — | — | — | Timeout. Maybe slow down a bit / Timeout. Maybe slow down a bit |
| r/SaaS | `"AI visibility"` | — | — | — | — | — | — | — | — | — | — | Timeout. Maybe slow down a bit / Timeout. Maybe slow down a bit |
| r/SaaS | `AEO` | — | — | — | — | — | — | — | — | — | — | Timeout. Maybe slow down a bit / Timeout. Maybe slow down a bit |

## Top three authors by thread count, per query (API `aggregate=author`, first three rows as returned)

- r/PPC `"generative engine optimization"`: Huge_Strawberry7888 1; Samarjith147 1
- r/PPC `GEO`: Crescitaly 3; whyvalue 2; Ancient-Day-6682 1
- r/PPC `AEO`: Ben1296 1; Fractionalcmoz 1; Samarjith147 1
- r/marketing `"generative engine optimization"`: CardiologistNew5480 1; filobtc 1
- r/marketing `GEO`: [deleted] 4; Strict-Interview-294 2; AffectOk 1
- r/marketing `"AI visibility"`: [deleted] 2; ap-oorv 1; Automatic-Mix8798 1
- r/marketing `AEO`: [deleted] 1; Gallowayyy98 1; Hughie_55 1
- r/SEO `"generative engine optimization"`: OutrageousPatient195 3; mohsin-ali-1 2; RagingTop 2
- r/SEO `GEO`: WebLinkr 38; [deleted] 17; Upset_Syrup_736 4
- r/SEO `"AI visibility"`: [deleted] 15; WebLinkr 4; Tarek_RiffinAI 2
- r/SEO `AEO`: [deleted] 18; WebLinkr 9; VisRank 3
- r/digital_marketing `"generative engine optimization"`: digital_sumit 2; ban3naf1sh 1; CardiologistNew5480 1
- r/digital_marketing `GEO`: Integral_Europe 4; Legitimate_Sell6215 3; Open_Ad_5741 3
- r/digital_marketing `"AI visibility"`: Stunning-Rush-6468 4; nrseara 4; Open_Ad_5741 3
- r/digital_marketing `AEO`: Electrical-Tear-308 4; Legitimate_Sell6215 4; [deleted] 3
- r/advertising `"generative engine optimization"`: ban3naf1sh 1; CardiologistNew5480 1; One_Suit_2055 1
- r/advertising `GEO`: Upbeat_Quit7362 2; Amazing_Draft_3951 2; bartradv 1
- r/advertising `"AI visibility"`: CardiologistNew5480 1; [deleted] 1
- r/advertising `AEO`: CardiologistNew5480 1; EconomyAgency8423 1; MomentChemical 1
- r/bigseo `"generative engine optimization"`: [deleted] 4
- r/bigseo `GEO`: [deleted] 5; sumitdigital_wd 2; Suspicious-Slot 2
- r/bigseo `"AI visibility"`: [deleted] 5; Poowatereater 2; Zaillor 2
- r/bigseo `AEO`: [deleted] 3; Wooden_Assistance547 2; Commercial-Cress3796 2
- r/adops `GEO`: Slow_Progress_3838 3; Dependent-Use-3215 3; b_renat 1
- r/adops `"AI visibility"`: DataBeat_adtech 1
- r/ecommerce `"generative engine optimization"`: dennismant 1; jvbeats 1; Ok_Today_4319 1
- r/ecommerce `GEO`: EngineeringBasic9707 2; Academic_Flamingo302 1; AdFeeling7617 1
- r/ecommerce `"AI visibility"`: Academic_Branch948 1; Adapowers 1; Adventurous-Day2227 1
- r/ecommerce `AEO`: EngineeringBasic9707 2; friendlyecomreviewer 1; Haile_Haiona 1
- r/startups `"generative engine optimization"`: ban3naf1sh 1; blimy20 1; Sanbi_Ai 1
- r/startups `GEO`: egudegi 2; dooddyman 2; blimy20 1
- r/startups `"AI visibility"`: No-Leading6008 2; Few-Guava-6976 1; Independent-Catch624 1
- r/startups `AEO`: joy_hay_mein 1; Past-Quarter-2316 1; UpstairsMap6263 1

## Request URLs (one per aggregate, as sent)

- https://arctic-shift.photon-reddit.com/api/posts/search/aggregate?aggregate=created_utc&frequency=month&subreddit=PPC&query=%22generative+engine+optimization%22&after=2026-03-01&before=2026-09-24
- https://arctic-shift.photon-reddit.com/api/posts/search/aggregate?aggregate=author&subreddit=PPC&query=%22generative+engine+optimization%22&after=2026-03-01&before=2026-09-24&limit=5000
- https://arctic-shift.photon-reddit.com/api/posts/search/aggregate?aggregate=created_utc&frequency=month&subreddit=PPC&query=GEO&after=2026-03-01&before=2026-09-24
- https://arctic-shift.photon-reddit.com/api/posts/search/aggregate?aggregate=author&subreddit=PPC&query=GEO&after=2026-03-01&before=2026-09-24&limit=5000
- (same pattern for every subreddit × query; `query` values URL-encoded as sent)

## Pull notes — mechanical only

- r/SaaS: all 8 aggregate calls (4 terms × 2) returned "Timeout. Maybe slow down a bit" on two separate runs of 4 retries each; `unknown — checked Arctic Shift aggregate API 2026-09-23`.
- r/bigseo `"generative engine optimization"`: 4 threads, 1 author key, 4 rows by [deleted] — every matching thread's author deleted.
- No vertical term (insurance, skincare, SaaS etc.) was combined with the category terms; counts are subreddit-level, not vertical-level.
- Another agent's Arctic Shift job ran concurrently; the archive's coverage of 2026 Reddit is not published on the response.

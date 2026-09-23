# Reddit (Arctic Shift archive) — S5 community threads on national subreddits: UK, France, Spain, Italy, Netherlands; subreddit-name search for national SEO subs

```yaml
source:          Reddit posts, via the Arctic Shift open archive API (arctic-shift.photon-reddit.com); reddit.com not accessed
url_or_doc_id:   https://arctic-shift.photon-reddit.com/api/subreddits/search?subreddit_prefix=seo&limit=10 ; .../posts/search/aggregate?aggregate=created_utc&frequency=month&subreddit=smallbusinessuk&query=ChatGPT&after=1772323200&before=1758672000 ; .../posts/search/aggregate?aggregate=created_utc&frequency=month&subreddit=france&query=%22generative%20engine%20optimization%22&after=1772323200&before=1758672000 ; .../posts/search?subreddit=spain&query=ChatGPT%20negocio&after=1772323200&limit=10 ; .../posts/search?subreddit=italy&query=ChatGPT%20azienda&after=1772323200&limit=10 ; .../posts/search?subreddit=thenetherlands&query=ChatGPT%20bedrijf&after=1772323200&limit=10
published:       archive state at pull; posts created 2026-03-01 to 2026-09-23 where returned
pull_date:       2026-09-23
pull_method:     curl, one call per 90 s; HTTP 422 retried once after 150 s
pull_purpose:    evidence about a number (S5 per country)
tier:            5
tier_reason:     archive copy of a forum; counts are the archive's, not the platform's (same reasoning as docs/raw/f-reddit-S5-counts-repull2-2026-09-23.md)
source_label:    measured-by-us
lane:            F
sub_market:      organic recommendation
engine:          ChatGPT (as named by posters)
metric_kind:     none
supersedes:      none
captured:        API results verbatim; the one post returned with its fields
```

## Call log

| # | call | HTTP | result |
|---|---|---|---|
| 1 | subreddits/search, `subreddit_prefix=seo`, limit 10 | 200 | 10 subreddits: "Search Engine Optimization: The Latest SEO News" (2008), "Seoul" (2009), "Extreme SEO" (2017), "SEO Growth" (2021), "Best SEO Infographics 2021" (2015), "For fans of Seolhyun" (2014), "SEO Tools Reviews" (2023), "SEO_Marketing_Offers" (2022), "SeoulOfLinda" (2021), "Seoul Food" (2013) — **no national (UK/FR/ES/IT/NL) SEO subreddit surfaced** |
| 2 | aggregate by month, r/smallbusinessuk, query `ChatGPT`, 2026-03-01 to 2026-09-24 | 200 | `{"data":[]}` — 0 posts |
| 3 | aggregate by month, r/france, query `"generative engine optimization"`, same window | 200 | `{"data":[]}` — 0 posts |
| 4 | posts, r/spain, query `ChatGPT negocio`, after 2026-03-01, limit 10 | 422 → retry 200 | `{"data":[]}` — 0 posts |
| 5 | posts, r/italy, query `ChatGPT azienda`, after 2026-03-01, limit 10 | 200 | 1 post (below) |
| 6 | posts, r/thenetherlands, query `ChatGPT bedrijf`, after 2026-03-01, limit 10 | 422 → retry 200 | `{"data":[]}` — 0 posts |

[note: `before=1758672000` is 2025-09-24, i.e. before `after` — the two aggregate calls (2, 3) therefore describe an empty window and their 0 is not evidence of absence. The three posts calls (4–6) carried only `after` and are valid for 2026-03-01 onward. An empty `subreddits/search` match for a national SEO sub means none exists under the `seo` prefix, not that none exists under another name.]

## Verbatim — r/italy, `ChatGPT azienda`, 1 post

```
2026-03-22 | r/italy | score 138 | 35 comments | "Il Tribunale di Roma annulla la sanzione da 15 milioni di euro inflitta dal Garante Privacy a OpenAI" | /r/italy/comments/1s0fzf4/il_tribunale_di_roma_annulla_la_sanzione_da_15/
```

[note: a news-link post (Rome court annulling the Italian Garante's EUR 15 million fine on OpenAI); not a brand-visibility thread. The underlying court or Garante document was not pulled.]

## Pull notes — mechanical only

- Six calls, two 422 "Timeout" responses retried successfully; the API was shared with another agent throughout.
- Query semantics (space-separated tokens vs phrase) are the archive's and undocumented; `ChatGPT negocio` / `ChatGPT azienda` / `ChatGPT bedrijf` were sent as two tokens.

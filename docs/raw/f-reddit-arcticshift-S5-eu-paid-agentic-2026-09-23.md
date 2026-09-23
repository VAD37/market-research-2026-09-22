# Reddit (Arctic Shift archive) — S5 community threads on national subreddits with paid-placement and agentic-commerce terms: UK, France, Spain, Italy, Netherlands; 17 queries, 28 calls

```yaml
source:          Reddit posts, via the Arctic Shift open archive API (arctic-shift.photon-reddit.com); reddit.com not accessed
url_or_doc_id:   https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>&query=<terms>&after=1772323200&before=1790208000&limit=10 — subs smallbusinessuk, france, spain, italy, thenetherlands, unitedkingdom, ukbusiness; terms per sub listed below
published:       archive state at pull; window 2026-03-01 to 2026-09-24 (after < before)
pull_date:       2026-09-23
pull_method:     curl, one call per 90 s; HTTP 422 retried once after 150 s; API shared with another agent throughout
pull_purpose:    evidence about a number (S5 per country, paid placement and agentic commerce)
tier:            5
tier_reason:     archive copy of a forum; counts are the archive's, not the platform's (as docs/raw/f-reddit-S5-counts-repull2-2026-09-23.md)
source_label:    measured-by-us
lane:            F
sub_market:      paid placement; agentic commerce
engine:          ChatGPT (as sent in the query terms)
metric_kind:     none
supersedes:      none (docs/raw/f-reddit-arcticshift-S5-eu-national-subs-2026-09-23.md is the organic-term cut; its inverted-window fault is not repeated here)
captured:        call log verbatim; every post returned, with title, date, score, comments, permalink, removal flag and the opening of its body
```

## Call log — 17 queries, 28 calls (11 retries)

| # | sub | query | HTTP first / retry | result |
|---|---|---|---|---|
| 1 | smallbusinessuk | `ChatGPT ads` | 200 | 0 posts |
| 2 | smallbusinessuk | `agentic commerce` | 422 / 422 | **unresolved** — "Timeout. Maybe slow down a bit" twice |
| 3 | smallbusinessuk | `AI ads` | 200 | 10 posts (below) — token match on "AI" and "ads" |
| 4 | france | `ChatGPT publicité` | 422 / 422 | **unresolved** |
| 5 | france | `agentic commerce` | 200 | 0 posts |
| 6 | france | `ChatGPT ads` | 200 | 0 posts |
| 7 | spain | `ChatGPT publicidad` | 422 / 422 | **unresolved** |
| 8 | spain | `agentic commerce` | 422 / 200 | 0 posts |
| 9 | spain | `ChatGPT ads` | 422 / 422 | **unresolved** |
| 10 | italy | `ChatGPT pubblicità` | 422 / 200 | 0 posts |
| 11 | italy | `agentic commerce` | 200 | 0 posts |
| 12 | italy | `ChatGPT ads` | 422 / 422 | **unresolved** |
| 13 | thenetherlands | `ChatGPT advertenties` | 200 | 0 posts |
| 14 | thenetherlands | `agentic commerce` | 422 / 422 | **unresolved** |
| 15 | thenetherlands | `ChatGPT ads` | 422 / 200 | 0 posts |
| 16 | unitedkingdom | `ChatGPT ads` | 422 / 200 | 0 posts |
| 17 | ukbusiness | `ChatGPT` | 422 / 200 | 0 posts |

17 of 28 responses were HTTP 422; 6 queries stayed unresolved after one retry: UK `agentic commerce`, FR `ChatGPT publicité`, ES `ChatGPT publicidad`, ES `ChatGPT ads`, IT `ChatGPT ads`, NL `agentic commerce`.

## Verbatim — r/smallbusinessuk, `AI ads`, 10 posts, 2026-05-12 to 2026-08-31

```
2026-08-31 | score 0 | 13 comments | "Customer acquisition is becoming the hardest part of running my repair business" | /r/smallbusinessuk/comments/1w3lszd/… | removal: reddit | "I run a device repair business in Luton and lately the hardest part isn't actually repairing devices, it's getting customers consistently. We've rebuilt the website properly, invested heavily in SEO, launched UK-wide mail-in repairs, and built something we're genuinely proud of: a free AI device di…"
2026-08-30 | score 1 | 3 comments | "Need advice for my agency" | /r/smallbusinessuk/comments/1w2v3e5/… | removal: moderator | "…I am a computer science grad. I worked a few tech internships, and then I was very interested in sales…"
2026-07-07 | score 0 | 9 comments | "Looking for someone who wants to help build a UK digital marketing agency" | /r/smallbusinessuk/comments/1uppkmq/… | removal: moderator | "…helps businesses generate leads through Google Ads, Meta Ads, SEO, AI automations and B2B outbound/email automation…"
2026-07-03 | score 2 | 11 comments | "Starting a carpet cleaning business?" | /r/smallbusinessuk/comments/1umtb5r/… | removal: none | "…would like advice on how to advertise and scale a carpet cleaning business… budget of £2k…"
2026-06-29 | score 0 | 27 comments | "Need Help! Spent two years building UK company database but no struggling to sell it" | /r/smallbusinessuk/comments/1uipi8g/… | removal: deleted | "…OCR/AI translation scripts feeding a 15TB database…"
2026-06-18 | score 2 | 6 comments | "Solo dev with a validated B2B product, but I'm completely failing at distribution." | /r/smallbusinessuk/comments/1u92yrw/… | removal: automod_filtered
2026-06-09 | score 1 | 1 comment | "Have you bought out someone's business and did it work out?" | /r/smallbusinessuk/comments/1u14wc8/… | removal: moderator | "…Looking at some ads on Rightmove…"
2026-05-24 | score 1 | 17 comments | "Are there any actually useful AI apps out there?" | /r/smallbusinessuk/comments/1tm889g/… | removal: moderator | "Do any of you actually use AI software for your business? … Lately I've been seeing more ads in different subreddits for tools aimed at small businesses, so I tried a fe…"
2026-05-19 | score 8 | 7 comments | "The first time in my life that I've reached £10k in savings" | /r/smallbusinessuk/comments/1thl0jz/… | removal: moderator
2026-05-12 | score 0 | 0 comments | "Meta restricted our 69k Facebook page for "fraud/scam" despite showing "NO violations" — 20 days later and we're drowning…" | /r/smallbusinessuk/comments/1tav1ws/… | removal: deleted
```

[note: none of the ten posts concerns advertising inside an AI assistant or agentic checkout; the archive matched the tokens "AI" and "ads" separately. 8 of 10 carry a removal flag in the archive's `_meta`.]

## Pull notes — mechanical only

- Window bounds checked before the run: after 1772323200 (2026-03-01) < before 1790208000 (2026-09-24).
- 422 responses carried `{"data":null,"error":"Timeout. Maybe slow down a bit"}`; the API was shared with another agent (P16-c4) for the whole run, one call per 90 s from this agent.
- Query semantics (space-separated tokens vs phrase) are the archive's and undocumented; all terms were sent unquoted.

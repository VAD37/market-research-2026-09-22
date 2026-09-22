# Hacker News via Algolia API — community thread volume, B2B SaaS GEO/AEO mentions

```yaml
source:          Hacker News (via Algolia Search API)
url_or_doc_id:   https://hn.algolia.com/api/v1/search?query=%22generative%20engine%20optimization%22%20SaaS ; https://hn.algolia.com/api/v1/search?query=%22AI%20visibility%22%20B2B ; https://hn.algolia.com/api/v1/search?query=GEO%20SaaS%20marketing (unquoted, noisy) ; https://hn.algolia.com/api/v1/search?query=%22answer%20engine%20optimization%22
published:       n/a — live search index over dated HN stories, each item's own date given below
pull_date:       2026-09-22
pull_method:     fetch (curl, no key needed, no browser extension)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default — "4 if the platform publishes counts"; Algolia's API publishes points and num_comments per story directly
source_label:    company-stated (each story is a self-report by its poster; points/comments are platform-measured engagement counts)
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        title, points, num_comments, created_at, url for every hit returned by each query (no truncation — all hits under each query's nbHits were within the default page size)
```

## Verbatim

Query `"generative engine optimization" SaaS`: `nbHits: 3`.
1. "Show HN: Amplift – AI agent for influencer marketing, GEO, and social listening" — points 3, num_comments 1, created_at 2025-12-11T20:53:09Z, url https://amplift.ai/
2. "Are people building GEO tools? (SEO for AI search)" — points 3, num_comments 0, created_at 2024-12-27T05:05:10Z
3. "Show HN: ReachLLM to track, analyze and improve AI Search visibility" — points 2, num_comments 1, created_at 2025-08-25T22:31:24Z, url https://reachllm.com

Query `"AI visibility" B2B`: `nbHits: 4`.
1. "Open prompt pack for testing AI visibility stability across assistants (v0.1" — points 1, num_comments 1, created_at 2025-10-31T15:50:21Z
2. "Show HN: GeoRankers – See how AI models like ChatGPT describe your SaaS" — points 1, num_comments 0, created_at 2026-02-02T12:46:20Z, url https://dashboard.georankers.co/register
3–4. two further items dated 2026-02-02, titles not fully captured in this extraction pass.

Query `"answer engine optimization"` (quoted phrase): `nbHits: 41`. Full title list captured (first 15 by relevance, HN Algolia default sort):
- "Answer Engine Optimization" — points 11, num_comments 2, created_at 2026-03-19T13:11:26Z
- "An experimental guide to Answer Engine Optimization" — points 9, num_comments 3, created_at 2026-04-01T15:57:28Z
- "Show HN: I built an Answer Engine Optimization tool to boost brand AI visibility" — points 3, num_comments 0, created_at 2025-07-15T08:52:51Z
- **"From Traditional SEO to AI-Driven Answer Engine Optimization in B2B SaaS"** — points 2, num_comments 1, created_at 2025-06-03T18:55:59Z
- "Answer Engine Optimization (AEO) – The Next Evolution of SEO?" — points 1, num_comments 1, created_at 2025-02-03T14:26:48Z
- "Show HN: Beginner's Guide to Answer Engine Optimization – The Future of Search?" — points 1, num_comments 0, created_at 2025-07-30T16:31:09Z
- "A B2B marketing agency grew to $1.5M ARR in 6 months by betting on AI" — points 6, num_comments 1, created_at 2026-07-20T15:58:42Z
- "Ask HN: How does ChatGPT decide which websites to recommend?" — points 5, num_comments 15, created_at 2026-02-05T23:49:40Z
- "Show HN: Scan domain for llms.txt LLMs-full.txt AI aware SEO tool" — points 5, num_comments 0, created_at 2026-04-19T13:01:05Z
- "We Built Mentionedby.ai to Track How AI Models Answer Questions" — points 4, num_comments 6, created_at 2025-05-09T04:13:16Z
- "After writing over 10k+ blogs, here's what I learned about AEO" — points 2, num_comments 4, created_at 2025-04-21T12:08:16Z
- "Show HN: We're tracking AI bot visits daily across our network" — points 2, num_comments 0, created_at 2025-10-19T17:39:19Z
- "Show HN: BetterAEO – Measure AI search readiness and get AI recommendations" — points 1, num_comments 2, created_at 2025-08-22T04:44:58Z
- **"Show HN: FlipAEO – Get your SaaS cited by Perplexity and AI search"** — points 1, num_comments 0, created_at 2026-04-15T05:17:33Z
- "Show HN: MentionedBy AI is now live" — points 1, num_comments 0, created_at 2025-05-18T06:44:51Z

Query `GEO SaaS marketing` (unquoted, no phrase operator): `nbHits: 1289` — not decomposed, recorded only as evidence that Algolia's default OR-matching on an unquoted bare `GEO` reproduces the glossary's warning about geographic-sense noise at scale; not used as a signal count.

## Pull notes — mechanical only

- `hn.algolia.com/api/v1/search` requires no API key and returned HTTP 200 on every query; no browser extension used.
- The one title that explicitly names both "B2B SaaS" and an organic-recommendation term ("From Traditional SEO to AI-Driven Answer Engine Optimization in B2B SaaS," 2025-06-03) is the strongest single vertical-attributed hit in this pull: tagged sub-market organic recommendation, vertical B2B SaaS (source's own title wording), buyer size **unassigned** — the title and available metadata name no company size or buyer band. Per `demand-signals.md`'s cell-attribution rule, this moves no specific buyer-size cell; it is recorded as a vertical-and-sub-market-level attention signal only.
- "Show HN: GeoRankers... describe your SaaS" and "Show HN: FlipAEO – Get your SaaS cited by Perplexity and AI search" both address a SaaS-building audience (practitioner attention aimed at SaaS founders) but are vendor/tool launch posts, not a buyer naming its own spend or role — recorded as S5 attention-class community-thread evidence, not S1/S2 spend evidence, and likewise buyer-size unassigned.
- Query construction followed the glossary's disambiguation rule (`GEO "AI search"`-style pairing) except for the deliberate unquoted control query, which was run specifically to confirm the noise problem rather than to find signal.
- Reddit (`reddit.com/r/SEO`, `/r/PPC`, `/r/bigseo`) was tried via both `old.reddit.com/.../search.json` and `www.reddit.com/.../search.json`, both with and without a browser User-Agent string: **every attempt returned HTTP 403.** Filed separately, per the task's instruction to record this explicitly — see `f-signal-bs-S5-reddit-2026-09-22.md`.

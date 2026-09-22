# Community thread volume — HN Algolia, reddit.com (blocked) — skincare and beauty × AI visibility

```yaml
source:          Hacker News (via Algolia search API); reddit.com (access attempt only, blocked)
url_or_doc_id:   hn.algolia.com/api/v1/search; hn.algolia.com/api/v1/search_by_date; reddit.com/r/SkincareAddiction; reddit.com/r/beauty
published:       undated — live search index
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default per demand-signals.md S5 ("4 if the platform publishes counts") for the HN Algolia counts; reddit.com yielded no data at all (access blocked), recorded as unknown, not tiered
source_label:    analyst-derived
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        API JSON responses — nbHits counts and top-10 hit titles/dates per query; full result sets not paged through
```

## Query — verbatim

HN Algolia (`hn.algolia.com/api/v1/search`, default relevance sort, and `search_by_date` where noted), each run 2026-09-22:

| Query string | nbHits | Notes on top hits |
|---|---|---|
| `generative engine optimization beauty` | 1 | Single hit dated 2011-12-29 — pre-dates the category entirely, false-positive keyword match |
| `AI visibility beauty` | 16 | Mix of dates 2021–2026; one on-topic vendor post: "Show HN: AI Brand Visibility for Free Forever" (`app.geosurge.ai/login`), 2026-09-10 — a vendor demo/launch post, not a beauty-specific practitioner discussion; remaining hits are off-topic (Svelte starter kit, AI headshots, etc.) |
| `GEO skincare` | 1934 | Top hits are unrelated (trademark question, hand-sanitizer Show HN, influencer-search tool) — `GEO` matching geographic and unrelated uses, confirms the glossary.md ambiguity warning; not usable |
| `skincare AEO` | 113 | Not manually reviewed past nbHits given the `GEO skincare` false-positive pattern above; token-OR matching suspected |
| `cosmetics LLM visibility` | 0 | No hits |
| `beauty brand ChatGPT recommendation` | 0 | No hits |
| `"GEO manager" beauty` | 0 | No hits |
| `"answer engine optimization" skincare` | 0 | No hits |
| `beauty brand "generative engine optimization"` (search_by_date) | 0 | No hits |

reddit.com: `reddit.com/r/SkincareAddiction/search.json?q=GEO%20AI%20visibility` → HTTP 403. `reddit.com/r/beauty/.json` → HTTP 403. Both checked 2026-09-22 with a plain fetch (curl, `Mozilla/5.0` User-Agent, no auth, 10-second timeout); no browser-extension retry was made for reddit within this cluster's task scope (the task brief names reddit.com unreachable this session and directs recording that, not retrying via browser). Per `channels.md` C39, this is consistent with the "JSON API blocked in predecessor sessions" bias already on file.

## Verbatim

HN Algolia hit, verbatim JSON fragment, the one on-topic result found across all queries:

```json
{"created_at":"2026-09-10T13:16:59Z","title":"Show HN: AI Brand Visibility for Free Forever","url":"https://app.geosurge.ai/login"}
```

reddit.com response body, `r/SkincareAddiction/search.json`: HTTP 403, standard Reddit block page (no JSON body returned to this client).

## Pull notes — mechanical only

- No practitioner thread specifically discussing AI-visibility/GEO/AEO tooling or tactics *for the skincare-and-beauty vertical* was found on Hacker News at this pull — the one on-topic hit is a vendor's own product-launch post (Geosurge, a general AI-visibility tool, not beauty-specific), which is S2/vendor-reported in character, not a practitioner community signal.
- HN Algolia's relevance search does not appear to perform strict phrase matching even where the query itself uses no quotes: bare multi-word queries (`GEO skincare`) returned thousands of loosely-related hits, consistent with token-level OR matching. Quoted-phrase queries (`"GEO manager" beauty`, `"answer engine optimization" skincare`) returned 0, which is a cleaner but stricter signal and is the reading relied on for the `nil`/`none` calls in the census.
- reddit.com blocked outright (HTTP 403) on both a subreddit JSON search endpoint and a subreddit index JSON endpoint; no content reached for r/SkincareAddiction, r/MakeupAddiction, r/30PlusSkinCare, r/beauty, r/SEO, r/PPC, or r/bigseo this pull. Recorded per task brief as `unknown — checked reddit.com 2026-09-22, blocked (HTTP 403)`.
- No login wall on HN Algolia. Full result sets were not paged past the first page (20 hits) for any query; nbHits totals are as returned by the API.

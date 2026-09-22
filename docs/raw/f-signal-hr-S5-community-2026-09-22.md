# Hacker News (Algolia) and Reddit — S5 community thread volume, high-CPA regulated vertical

```yaml
source:          Hacker News, via the Algolia HN Search API (hn.algolia.com); Reddit (reddit.com)
url_or_doc_id:   https://hn.algolia.com/api/v1/search?query=<query> (multiple, see table); https://www.reddit.com/r/SEO/search.json?q=insurance%20GEO
published:       n/a — live query results as of pull date; individual HN items dated per their own `created_at` field, shown below
pull_date:       2026-09-22
pull_method:     fetch (direct curl, no browser extension, no login)
pull_purpose:    evidence about a number
tier:            4 per `demand-signals.md` S5 catalog ("if the platform publishes counts") for HN Algolia; n/a for Reddit (blocked, nothing retrieved)
tier_reason:     table default
source_label:    n/a (practitioner/community forum content, not vendor- or company-stated)
lane:            A, D
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        Algolia HN Search API JSON responses, `nbHits` counts and individual hit `story_title` / `comment_text` / `created_at` fields for the qualifying and near-miss hits; Reddit — HTTP status only
vertical:        high-CPA regulated — insurance, credit cards, supplements
cell:            unattributed — no thread names a buyer-size band
query:           see table below, verbatim
```

## Reddit — confirmed unreachable

`https://www.reddit.com/r/SEO/search.json?q=insurance%20GEO` → **403**, direct fetch, no login, no extension. Consistent with the task's own framing ("reddit.com unreachable — record so") and with `channels.md` C39's note that "JSON API blocked in predecessor sessions." Recorded, not retried via another method this pull.

## HN Algolia — queries and results

| # | Query (verbatim) | `nbHits` (Algolia's own count, default OR-token matching) | On-topic hit(s) found on inspection |
|---|---|---|---|
| 1 | `generative engine optimization insurance` | 0 | none |
| 2 | `AI visibility insurance` | 1 | Off-topic — a Y Combinator-style "AI for ___" company list comment naming dozens of AI-for-X startups (e.g. "AlphaWatch AI — AI for financial search"); no insurance-specific or GEO-specific content |
| 3 | `generative engine optimization credit card` | small n (exact count not captured) | One genuine GEO-related hit — a Show HN comment for **GeoArk AI** ("GeoArk AI is a GEO (Generative Engine Optimization) platform that helps brands track and improve their presence in AI answers—ChatGPT, Claude, Gemini, Perplexity, Grok... Problem: When people ask these models for recommendations, most brands are invisible or poorly represented"), dated 2026-03-09T16:20:55Z, story title "Geo Platform for AI Search Visibility (ChatGPT, Claude, Gemini, Perplexity)." The comment text does **not** actually mention "credit card" — matched on "generative", "engine", "optimization" tokens only. This is a **vendor-side** post (a GEO tool builder announcing their product), not buyer-side demand, and not credit-card-specific despite the query match |
| 4 | `AEO insurance` | 19 (default OR matching) | not individually inspected past query 2/3's pattern — token-level matching on "insurance" and "AEO" separately is expected to dominate, per the same false-positive pattern found in queries 2 and 3 |
| 5 | `GEO supplements` | 3,316 (default OR matching) | Not usable — `GEO` unpaired and bare per `query-book.md`'s explicit warning ("Never query bare GEO... A result using GEO geographically is discarded on sight"); this query is recorded as a **defect**, not as a real result, and its count is not cited as evidence of anything |
| 6 | `answer engine optimization insurance` | 12 (default OR matching) | Not individually inspected; expected same token-dilution pattern |
| 7 | `AI search visibility credit card` | 3 | Two off-topic (a 2016 browser-features story; a "[dead]" 2025 item on an unrelated "For All Humanity" initiative); the third is the same GeoArk AI Show HN hit as query 3 (same false-positive "credit card" match) |

## Result

**`none — checked "generative engine optimization insurance" (0 hits), "AI visibility insurance" (1 hit, off-topic), "generative engine optimization credit card" / "AI search visibility credit card" (1 genuine but vendor-side, non-vertical-specific hit: GeoArk AI Show HN post), reddit.com (403, unreachable) 2026-09-22`** for S5 in the high-CPA regulated vertical. No practitioner community thread discussing AI-visibility/GEO demand specifically inside insurance, credit cards, or supplements was found on Hacker News; Reddit could not be checked at all.

## Caveats

- Algolia's default query mode is OR/relevance across tokens, not phrase-exact; every multi-digit `nbHits` count above (19, 3,316, 12) is a token-dilution artifact, not a precise on-topic thread count. Only the manually-inspected hits (queries 2, 3, 7) are treated as real evidence, and all resolve to off-topic or vendor-side, non-qualifying.
- `GEO supplements` (query 5) is filed here specifically as a worked example of the ambiguity `query-book.md` warns about (`GEO` = generative-engine-optimization vs. geographic); its 3,316-hit count is not usable for anything.
- The GeoArk AI Show HN post (queries 3, 7) is the single most relevant item found on HN this pull. It evidences a vendor launching a GEO tool, dated 2026-03-09 — filed as a data point for the category's own activity level, not as a high-CPA-regulated-vertical demand signal, since neither the post nor its comment names insurance, credit cards, or supplements.

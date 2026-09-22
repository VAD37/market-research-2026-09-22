# Google — Reviews system and "Write high-quality reviews" guidance (checked for fake/manufactured-review language)

```yaml
source:          Google Search Central (developers.google.com)
url_or_doc_id:   https://developers.google.com/search/updates/reviews-update ; https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews
published:       both pages "Last updated 2025-12-10 UTC" per each page's own timestamp
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own documentation; stale — last-updated 2025-12-10, before 2026-06-22, per query-book.md date rule. Platform-primary docs are exempt from the recency filter per that same rule ("the changelog's own history is the evidence")
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Google — Search (Reviews system is named on Google's own ranking-systems guide, developers.google.com/search/docs/appearance/ranking-systems-guide, as a distinct ranking system; not scoped by either page to AI Overviews/AI Mode specifically)
metric_kind:     none
supersedes:      none
captured:        full content as returned by the fetch tool for both pages
technique:       review and listicle manufacture
models_tested:   n/a
date_window:     n/a
measured_effect: n/a — policy/guidance pages, not a measurement
vertical:        n/a — applies to all content categories the Reviews system evaluates
```

## Verbatim

### Reviews system page (`/search/updates/reviews-update`)

What the system evaluates, quoted as returned by the fetch tool:

"[The reviews system] aims to better reward high quality reviews, content that provides insightful analysis and original research, and is written by experts or enthusiasts who know the topic well." The system evaluates "articles, blog posts, pages or similar first-party standalone content" on a page-level basis, though the fetch tool notes sites with substantial review content may face site-wide evaluation.

Guidance pointer, quoted as returned by the fetch tool:

"To learn more about how to create content that's successful with the reviews system, see our help page on how to write high quality reviews," linking to `/search/docs/specialty/ecommerce/write-high-quality-reviews`.

Per the fetch tool's explicit check: **"The page contains no statement addressing manufactured, fake, or AI-generated reviews."** The page's content is described by the tool as focused on "system mechanics and recovery possibilities rather than addressing these specific content categories."

### "Write high-quality reviews" page (`/search/docs/specialty/ecommerce/write-high-quality-reviews`)

Best-practice list, quoted as returned by the fetch tool:

"Evaluate from a user's perspective"; "Demonstrate that you are knowledgeable about what you are reviewing — show you are an expert"; provide supporting evidence (visuals, audio, links); include quantitative measurements and comparisons; discuss both benefits and drawbacks based on original research; share first-hand supporting evidence when making recommendations.

Affiliate-link clause, quoted as returned by the fetch tool:

"Reviews often use affiliate links, so that if someone finds a review useful and follows the provided link to purchase, the creator of the review is rewarded by the seller."

Per the fetch tool's explicit check, this page **does not contain**: "Any warnings about fake, manufactured, or purchased reviews"; "Statements regarding AI-generated review content"; or "Information about how the reviews system detects or penalizes low-quality or manipulative reviews."

## Pull notes — mechanical only

- Both pages fetched via WebFetch, 200, no login gate.
- Located by following the internal link chain from `developers.google.com/search/docs/appearance/ranking-systems-guide` (fetched first to confirm the Reviews system's existence as a named Google ranking system and locate its own page) -> `/search/updates/reviews-update` -> `/search/docs/specialty/ecommerce/write-high-quality-reviews`.
- **This is a documented absence, not a partial confirmation**: Google's general spam policy (`docs/raw/d-review-google-spam-policies-2026-09-22.md`, already in raw, P5-c2) names "scaled content abuse" — including "using generative AI tools... to generate many pages without adding value" — as a policy category that would structurally cover mass-produced fake reviews, but that policy page does not use the words "review," "fake," or "manufactured." This pull went one level deeper, to Google's own dedicated Reviews-system pages, specifically to check whether the more targeted guidance names fake/manufactured reviews — it does not, at either page. Both absences are recorded together here because they answer the same census cell.
- Neither page distinguishes AI Overviews/AI Mode citation behavior from classic web ranking with respect to reviews; `unknown — checked these two pages only, 2026-09-22`, on that specific cross-surface question.
- No date filter or enforcement-action description appears on either page — both are purely descriptive/instructional.

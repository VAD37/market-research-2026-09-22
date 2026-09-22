# Agency service pages — S6, naming finance / insurance / supplements clients

```yaml
source:          docs/raw/f-agency-census-c5-2026-09-22.md (this repo, cross-referenced, not re-pulled); DuckDuckGo (lite.duckduckgo.com/lite/), fresh discovery this pull; apexmediasol.com, geojet.io (spot-checked)
url_or_doc_id:   docs/raw/f-agency-census-c5-2026-09-22.md ; https://lite.duckduckgo.com/lite/?q=<query> ; https://apexmediasol.com/case-studies/insurance ; https://geojet.io/blog/insurance-industry-geojet-case-study/
published:       f-agency-census-c5 published 2026-09-22 (this repo); geojet.io case study dated 2023-06-03 on its own page
pull_date:       2026-09-22
pull_method:     fetch (direct curl; lite.duckduckgo.com/lite worked where html.duckduckgo.com/html 403'd under repeated queries this pull)
pull_purpose:    evidence about a number (cross-reference) and evidence about category noise (the geojet.io false positive)
tier:            n/a — cross-reference to an existing tier-mixed census file for the primary claim (no cell reads spend from S6 in this file); 7 for geojet.io per `trust-rubric.md` (stale, off-vertical, filed only as noise)
tier_reason:     the cross-referenced census (f-agency-census-c5) carries its own per-row tiers; nothing here upgrades or re-tiers that file
source_label:    n/a
lane:            A, F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        cross-reference read of f-agency-census-c5's roster table (§2) and screened/held lists (§3, §4); DuckDuckGo-lite search-result URL list; full-page grep of two spot-checked results
vertical:        high-CPA regulated — insurance, credit cards, supplements
cell:            unattributed — no qualifying agency-client pairing found
query:           `GEO agency insurance client case study` (lite.duckduckgo.com); direct fetch of the two spot-checked URLs
```

## Cross-reference — the five P3-c5-rostered agencies

Per `docs/raw/f-agency-census-c5-2026-09-22.md` §2 (roster of 5 agencies cleared against the Pass 3 roster rule: Onfolio/Pace Generative, Direct Digital Holdings/Orange142, Intero Digital, Seer Interactive, Fire&Spark), none names a finance, insurance, or supplements client:

| Agency | Named clients per f-agency-census-c5 | Vertical match |
|---|---|---|
| Onfolio Holdings / Pace Generative | 0 named (one anonymized "publicly traded enterprise client") | none |
| Direct Digital Holdings / Orange142 | 0 named (an unnamed "Green Energy Client") | none |
| Intero Digital | Freshpet (pet food, not this vertical), "Window Well Supply," "Sticker Mountain," unnamed sporting-goods and cloud-software brands | none |
| Seer Interactive | No client named on its own GEO page; a separate Search Engine Land "Home Depot" case-study headline (retail, not this vertical) was blocked by Cloudflare on every attempt in that pull | none |
| Fire&Spark | Hinge Health (digital health benefits/insurance-adjacent, but a testimonial with no metric, and health-benefits navigation rather than insurance/cards/supplements as this vertical is scoped) | borderline, not counted — testimonial only, no metric, per that file's own grading |

**Result from the rostered five: `none — checked f-agency-census-c5-2026-09-22.md §2 2026-09-22`.**

## Fresh discovery this pull — DuckDuckGo-lite sweep

`html.duckduckgo.com/html/` returned 403 on every attempt this pull (three tries, spaced), reproducing `f-agency-census-c5`'s own note that the endpoint "403-rate-limited under rapid successive queries." `lite.duckduckgo.com/lite/` succeeded (200) for the same query text.

Query: `GEO agency insurance client case study` → top results (URL list, via the `uddg=` redirect parameter): `firstpagesage.com/seo-blog/the-top-insurance-geo-agencies/` (a listicle/roundup by its own title — tier 7, not pulled), `onxeera.com/geo-case-study-agency-client-retention/`, `apexmediasol.com/case-studies/insurance`, `getgeology.com/case-studies`, `321webmarketing.com/case-studies/insurance-marketing/`, `aivisibilitypartners.com/case-studies`, `geodocs.dev/case-studies/agency-geo-offering`, `joinstratosphere.com/case-studies`, `lsaglobal.com/case-studies/building-brand-customer-loyalty-insurance/`, `geojet.io/blog/insurance-industry-geojet-case-study/`.

Two spot-checked in full:

1. **`apexmediasol.com/case-studies/insurance`** — HTTP 200, 26,862 bytes. Grepped for `generative engine|answer engine|AI visibility|AI search|GEO|AEO` (case-insensitive): **zero matches**. This is a generic insurance-marketing case-study page (traditional SEO/PPC framing), not a GEO/AEO/AI-visibility service. Discarded — false positive from the query's broad term matching.

2. **`geojet.io/blog/insurance-industry-geojet-case-study/`** — HTTP 200, 295,066 bytes; text contains 85 instances of "geo" and 4 of "aeo." **This is the exact ambiguity trap `query-book.md` warns against**: "Geojet" is a **local-listings / Google-Maps / Google-Business-Profile management tool** (its own case study: "insurance company... over 700 locations... data completeness across all locations... Google Maps, Yandex Maps, and 2GIS... brick-and-mortar locations... 99% data accuracy"). "GEO" here means geographic/local listings, not generative-engine-optimization. The case study is also dated **2023-06-03** on its own page — before this category (per `scope.md`'s caveats, "roughly two years old as of 2026-09") existed at all. Discarded on both grounds: term ambiguity and staleness pre-dating the category.

**Result from the fresh sweep: `none — checked lite.duckduckgo.com/lite query "GEO agency insurance client case study", two results opened in full, both discarded (generic marketing / geographic-GEO ambiguity) 2026-09-22`.**

## Credit-card and supplement sub-verticals

No separate DDG sweep was run for credit-card or supplement-specific agency case studies this pull (time-budgeted); cross-reference to `f-agency-census-c5` above already covers the rostered five agencies across all three sub-verticals and found no qualifying client in any of them.

## Overall S6 result, high-CPA regulated

**`none — checked f-agency-census-c5-2026-09-22.md (5 rostered agencies), lite.duckduckgo.com/lite fresh sweep (2 results opened in full, both discarded) 2026-09-22`.**

## Caveats

- This is a negative result built on a small, already-screened agency roster (5 of a target 8) plus one fresh 10-result search spot-checked at 2 of 10. A larger fresh sweep, or a Chrome-extension retry of `html.duckduckgo.com/html/`, could still surface a qualifying agency; this file does not claim exhaustiveness.
- The geojet.io false positive is filed here specifically because it is a clean, documented instance of the GEO/geographic ambiguity this repo's own query book flags as "the single highest-cost query defect in this book" (`query-book.md` caveats) — worth keeping as a concrete example, not only as a discard.

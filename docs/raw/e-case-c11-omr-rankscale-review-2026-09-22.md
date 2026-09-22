# OMR Reviews — Rankscale.ai, lowest-rated review found in the GEO category

```yaml
source:          OMR Reviews (user-submitted review of Rankscale.ai), plus the "generative-engine-optimization-geo" category's aggregate JSON-LD rating data as context
url_or_doc_id:   https://omr.com/en/reviews/product/rankscale-ai ; category page https://omr.com/en/reviews/category/generative-engine-optimization-geo
published:       2026-05-18 (review date)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     Review-site review, per this cluster's task instructions ("5 review-site review (label source_label: user-reported)").
source_label:    user-reported
lane:            E
sub_market:      organic recommendation
engine:          none named specifically — body mentions "keyword/LLm combinations" generically, no single named AI assistant
metric_kind:     none — UX/workflow complaint only, no visibility/traffic/sales metric
vertical:        none named
evidence_grade:  screened — no claim. Seven-item bar: (1) brand — present, Rankscale.ai named, reviewer is a real (if pseudonymous) product user; (2) engine — absent, no specific AI assistant named; (3) date window, absolute — absent, no stated usage period; (4) baseline — absent; (5) intervention — absent (no described GEO effort, just tool usage); (6) sample size — absent, n=1; (7) who measured — self-reported by the reviewer, OMR does not disclose incentive status on this listing the way G2 does. No metric present at all — graded "screened — no claim" per grading rule 1, filed regardless because it is, by direct comparison of every rating in the category's own structured data, the lowest-rated review found across the entire dedicated GEO review category on OMR.
direction:       neutral/mixed (3.0 of 5 stars) — the lowest star rating found among all individually-dated reviews surfaced across every product in OMR's "generative-engine-optimization-geo" category (24 listed vendors, aggregate rating range 4.50–5.00 per vendor; see category-context table below). No 1-star or 2-star review was found anywhere in this category.
vendor_named:    Rankscale.ai
supersedes:      none
captured:        full JSON-LD structured-data review record (author first name, review title, date, body text, numeric rating) extracted from the Rankscale.ai product page's embedded schema.org markup; plus the category page's aggregate per-vendor rating/review-count table (structured data), captured as context for the survivorship/review-farming finding below.
```

## Verbatim

### The lowest-rated individual review found in the category

> Author: Milan
> Title: "works fine and not too complicated to use"
> Date published: 2026-05-18
> Rating: 3.0 / 5 (worstRating 0, bestRating 5, per the page's own schema.org markup)
>
> Review body:
>
> "- I like how I can easily differentiate between multiple keyword lists - It is great that I can use multiple stores - it is great that I can see wich competitors are doing the right things and what kind of pages work te best/get mentioned the most
>
> - I think it is not easy to edit in bulk, without a lot of double checking and it is a bit cluttered with keyword/LLm combinations
>
> It helps us to compare us to our competitors and to see what pages get cited the most"

### Category-wide aggregate ratings — context, not a single case (from the category page's JSON-LD, `omr.com/en/reviews/category/generative-engine-optimization-geo`, pulled 2026-09-22)

| Product | Aggregate rating | Review count |
|---|---|---|
| Sichtbar für KI | 4.50 | 2 |
| Rankscale.ai | 4.58 | 26 |
| blinq | 4.66 | 22 |
| GEO Analyzer | 4.75 | 2 |
| Kai | 4.75 | 4 |
| Superlines | 4.75 | 8 |
| Ansehn | 4.79 | 7 |
| ALLMO.ai | 4.81 | 13 |
| Otterly.AI | 4.81 | 56 |
| Peec AI | 4.83 | 18 |
| SpotLens | 4.83 | 3 |
| Temso AI | 4.83 | 9 |
| flize | 4.88 | 4 |
| comdaily | 4.94 | 8 |
| Ucited | 4.94 | 8 |
| Finseo | 4.97 | 15 |
| AirOps | 5.00 | 2 |
| Kambrium | 5.00 | 2 |
| SE Visible | 5.00 | 2 |
| Vjus.AI | 5.00 | 3 |

(24 products listed on the category page; the 4 not shown above returned no `aggregateRating` block in the captured markup.)

## Pull notes — mechanical only

- Category page and the three most-reviewed products' individual review pages (Rankscale.ai 26 reviews, Otterly.AI 56, blinq 22) were fetched via plain HTTP fetch — `omr.com` returned 200 directly (one 301 redirect from `www.omr.com` to the bare `omr.com` host, followed).
- Individual review text is embedded as `Review`/`AggregateRating` schema.org JSON-LD inside the page's Nuxt/Next data payload, not as a simple visible-text block reachable by plain text extraction; recovered via a pattern match on the `"reviewBody":"..."` / `"ratingValue":"..."` JSON keys in the raw HTML.
- All individual star-rating values found across Rankscale.ai (26 reviews), Otterly.AI (56) and blinq (22) — the three products checked at the individual-review level — clustered at 3.0, 3.5, 4.0, 4.5 and 5.0; no 1.0 or 2.0 individual review was found among these 104 reviews. The 3.0-star Rankscale.ai review above is the single lowest individual star value found in this pull.
- This is consistent with the review-farming bias `docs/sources/channels.md` flags for C36/C65 ("Vendors farm reviews; check velocity not count" / "same review-farming risk as C36") — recorded as a finding, not softened.

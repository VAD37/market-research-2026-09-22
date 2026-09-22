# OMR Reviews — AI category and Otterly.AI product page — review velocity

```yaml
source:          OMR Reviews (omr.com)
url_or_doc_id:   https://omr.com/en/reviews/category/ai ; https://omr.com/en/reviews/product/otterly-ai
published:       n/a — live category/product page, dated reviews within
pull_date:       2026-09-22
pull_method:     fetch (curl with a browser User-Agent; no browser extension needed)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     dropped one tier from the table default (5 verified-buyer, 6 unverified) — no reviewer verification badge or reviewer-industry/company-size field was found in the fetched HTML, so reviews cannot be confirmed as purchase-verified; treated as unverified per `demand-signals.md` S4 row
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        JSON-LD review blocks (reviewCount, ratingValue, datePublished, author type) on the Otterly.AI product page; vendor-name list only on the category page (full page render not captured beyond the initial vendor-name list)
```

## Verbatim

Category page (`omr.com/en/reviews/category/ai`, "AI Software Comparison 2026 | OMR Reviews") — vendor names present in the page's structured data, in order: fonio.ai, neuroflash, melibo, Superchat, moinAI, Lime Connect (ehemals Userlike), **Otterly.AI**, ChatGPT, Conversionmaker.ai, LoyJoy, OMQ Chatbot und Kundenservice Software, homie, BOTfriends, innoGPT, Callioo, Creaitor, amplifa, DeutschlandGPT, whaaat.ai, Telfo. This is a general "Artificial Intelligence" category, not a dedicated GEO/AEO/AI-visibility category — Otterly.AI (a Pass-3-rostered AI-visibility vendor per this repo's `a-vendor-roster-2026-09-22.md`) is the only AI-visibility-specific tool visible in this list; the rest are chatbot/content/OMS tools.

Otterly.AI product page (`omr.com/en/reviews/product/otterly-ai`) JSON-LD review data, extracted fields:
```
"reviewCount":56
"ratingValue":"4.81"
```
Ten sampled individual review `datePublished` values from the structured data (not all 56 extracted, first ten in document order): 2026-06-19, 2026-03-19, 2025-07-29, 2025-05-14, 2026-09-02, 2026-08-26, 2026-06-08, 2026-06-04, 2026-06-04, plus one more 2026-06-04-adjacent entry with `ratingValue` 4.5. Individual review `ratingValue`s sampled: 5.0, 4.0, 5.0, 5.0, 5.0, 3.5, 5.0, 5.0, 5.0, 4.5. Every sampled review's `"author"` field is typed `{"@type":"Person"}` with no name, company, industry, or job-title field present in the JSON-LD as fetched.

## Pull notes — mechanical only

- OMR (`omr.com`) is directly fetchable without a browser extension or login, unlike G2 and Capterra (both 403 — see `f-signal-bs-S4-g2-capterra-2026-09-22.md`).
- **Reviewer-industry filter not obtainable from this pull.** The task's S4 spec requires review velocity "where the reviewer's industry is software." The JSON-LD review blocks captured here carry no industry, company, job-title, or company-size field for any reviewer — only `@type":"Person"` with a rating and a date. No `Branche` (industry), `Unternehmensgröße` (company size), or `verifiziert`/`verified` string was found anywhere in the fetched HTML via a direct grep for those terms. This may be present behind client-side JS hydration or a separate API call not captured by a static fetch; not confirmed either way.
- **Because the reviewer-industry field could not be confirmed, this signal is recorded as checked-but-not-cell-attributable per `demand-signals.md`'s cell-attribution rule** ("nothing is inferred... a signal that names a buyer size the source does not define is recorded... unmappable, it is recorded against the vertical and sub-market with buyer size `unassigned`"). Applying that same logic one level up: since no B2B SaaS or "software" industry tag is stated for any individual reviewer, this pull is recorded as `checked — 56 reviews, 4.81 avg rating (tier 6, unverified) — reviewer industry/company size not disclosed in the fetched HTML, so not attributable to the B2B SaaS vertical` rather than assigned to any cell.
- The review-count and date-span data (dates from 2025-05-14 through 2026-09-02) is retained in this file as evidence that the channel and this specific AI-visibility vendor (Otterly.AI) carry an active, dated review corpus — useful for a future pull if OMR's reviewer-industry data can be reached (e.g. via a browser session that renders any client-side reviewer-profile panel).
- No B2B-SaaS-vertical-specific OMR category or filter was found or tried beyond the general "AI" category page in the time available to this pull.

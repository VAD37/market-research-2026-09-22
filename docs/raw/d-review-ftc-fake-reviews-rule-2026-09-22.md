# FTC — 16 CFR Part 465, Rule on the Use of Consumer Reviews and Testimonials (fake reviews rule)

```yaml
source:          eCFR (Electronic Code of Federal Regulations), codifying the FTC's Trade Regulation Rule
url_or_doc_id:   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465 ; https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465/section-465.2 (16 CFR Part 465, § 465.2)
published:       Source line on page: "89 FR 68077, Aug. 22, 2024, unless otherwise noted"; page's own change timeline shows the section "introduced" 10/21/2024
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — codified federal regulation, current-as-published by eCFR, functionally equivalent to filed/binding text (matches the tier already assigned to the adjacent 16 CFR Part 255 pull in this repo)
source_label:    filed
lane:            D
sub_market:      organic recommendation
engine:          n/a — cross-engine regulatory text; does not name any AI assistant, chatbot, or AI search product
metric_kind:     none
supersedes:      none
captured:        § 465.2 "Fake or false consumer reviews, consumer testimonials, or celebrity testimonials" — heading, citation/agency/authority/source metadata, and the operative prohibition text and its sub-clauses, as rendered by the accessibility tree (partial — see truncation note below)
technique:       review and listicle manufacture
models_tested:   n/a
date_window:     n/a
measured_effect: no — this is a binding legal rule, not a measurement
vertical:        none named — the rule is written in business/product-neutral terms and names no industry vertical
```

## Verbatim

### Citation and authority (from the Part 465 landing page, read 2026-09-22)

"URL: https://www.ecfr.gov/current/title-16/part-465/section-465.2
Citation: 16 CFR 465.2
Agency: Federal Trade Commission
Part 465"

"Authority: 15 U.S.C. 57a"

"Source: 89 FR 68077, Aug. 22, 2024, unless otherwise noted."

Change timeline shown on the page: one entry, dated "10/21/2024", labelled "introduced".

### § 465.2 Fake or false consumer reviews, consumer testimonials, or celebrity testimonials.

Heading: "§ 465.2 Fake or false consumer reviews, consumer testimonials, or celebrity testimonials."

First prohibition (writing/creating fake reviews):

"It is an unfair or deceptive act or practice and a violation of this part for a business to write, c[reate...]" [note: truncated at tool output limit — the accessibility-tree extraction used for this pull caps each text node at roughly 100 characters; the verb after "write, c—" is almost certainly "create" based on the section title, but the full sentence was not captured]

Followed by three sub-clauses (rendered as separate list-item nodes, each independently truncated):

"That the reviewer or testimonialist exists;"

"That the reviewer or testimonialist used or otherwise had experience with the product, service, or b[usiness...]" [note: truncated at tool output limit]

"The reviewer's or testimonialist's experience with the product, service, or business that is the sub[ject of the review...]" [note: truncated at tool output limit]

Second prohibition (purchasing fake reviews):

"It is an unfair or deceptive act or practice and a violation of this part for a business to purchase [...]" [note: truncated at tool output limit — heading and the first prohibition's parallel structure indicate this clause bars purchasing consumer reviews that misrepresent the three items below]

"That the reviewer or testimonialist exists;"

"That the reviewer or testimonialist used or otherwise had experience with the product, service, or b[usiness...]" [note: truncated at tool output limit]

"The reviewer's or testimonialist's experience with the product, service, or business that is the sub[ject...]" [note: truncated at tool output limit]

Third prohibition (procuring fake reviews, e.g. through a review-generation intermediary):

"It is an unfair or deceptive act or practice and a violation of this part for a business to procure [...]" [note: truncated at tool output limit]

"That the reviewer exists;"

"That the reviewer used or otherwise had experience with the product, service, or business that is th[e subject...]" [note: truncated at tool output limit]

"The reviewer's experience with the product, service, or business that is the subject of the review."

Exemptions:

"However, and of this section do not apply to:" [note: this sentence renders with the cross-reference links "paragraphs (b)" and "(c)" stripped of their surrounding words by the extraction — the intended sentence is "However, paragraphs (b) and (c) of this section do not apply to:"]

"Reviews or testimonials that resulted from a business making generalized solicitations to purchasers [...]" [note: truncated at tool output limit]

"Reviews that appear on a website or platform as a result of the business merely engaging in consumer[...]" [note: truncated at tool output limit]

## Pull notes — mechanical only

- `WebFetch` to `www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-465` (the URL as originally guessed, under the old Subchapter B numbering) returned a 302 redirect to `unblock.federalregister.gov`, a bot-check redirect; the correct current path is `subchapter-D/part-465`. This pull used the Chrome extension (`claude-in-chrome`) instead of plain fetch throughout, consistent with the earlier 16 CFR Part 255 pull in this repo (`docs/raw/b-us-regulator-endorsement-guides-2026-09-22.md`), which hit the same redirect.
- Same capture-tool constraint as that earlier pull: `read_page`'s accessibility-tree extraction truncates each individual text node at roughly 100 characters. Long sentences are cut mid-word and marked `[note: truncated at tool output limit]` above rather than completed from memory. `get_page_text` (the plain-text extractor) returned only the site's search-navigation chrome on this page, not the section body, on both the Part-465 landing page and the section-465.2 page — the section text was recovered only via the accessibility-tree (`read_page`) route.
- Other sections of Part 465 — § 465.1 (definitions), § 465.3 (misuse of fake indicators of social media influence), § 465.4 (buying positive or negative reviews), § 465.5 (insider reviews and consumer testimonials), § 465.6 (company-controlled review websites), § 465.7 (review suppression), § 465.8 (effective date and severability) — were not pulled in this task; only § 465.2 (the core fake-review prohibition, most directly on point for "review and listicle manufacture") was captured, given this cluster's time budget. `unknown — checked ecfr.gov Part 465 table of contents only 2026-09-22` for the remaining sections' exact text.
- Enforcement-action search: `ftc.gov/news-events/news/press-releases` was queried (via `WebFetch`, not the browser) with `?query=fake+reviews`, `?query=reviews`, and `?query=supplement+reviews`; all three returned the same generic recent-press-release list (FleetCor, Amway, Amazon Prime, etc., dated 2026-08-17 through 2026-09-17), indicating the `query=` parameter is not honored by a plain fetch of that URL (the page is JS-driven and the query likely needs client-side execution or a different API endpoint). No FTC enforcement action naming a specific company for fake or manufactured reviews was located by this method. `unknown — checked ftc.gov/news-events/news/press-releases with query params via WebFetch only, not via browser, 2026-09-22`.

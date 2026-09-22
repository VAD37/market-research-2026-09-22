# Review-site velocity — G2 (blocked), Capterra (blocked), OMR — GEO/AI-visibility tools, beauty-industry reviewers

```yaml
source:          OMR Reviews (omr.com); G2 (g2.com, blocked); Capterra (capterra.com, blocked)
url_or_doc_id:   https://omr.com/en/reviews/category/generative-engine-optimization-geo; https://omr.com/en/reviews/product/rankscale-ai; https://omr.com/en/reviews/product/otterly-ai; https://omr.com/en/reviews/product/peec-ai; https://www.g2.com/categories/ai-search-visibility
published:       undated — live review-listing pages, individual reviews dated only by OMR's own relative bucket ("in the last 6 months")
pull_date:       2026-09-22
pull_method:     browser extension (MCP_DOCKER Playwright) for all pages in this file; a prior plain-fetch attempt is also recorded for comparison
pull_purpose:    evidence about a number
tier:            5
tier_reason:     table default per demand-signals.md S4 ("5 verified-buyer, 6 unverified") — the Rankscale.ai reviewer below is OMR's "Validated Reviewer" designation, which is an identity/account check, not a confirmed-purchase verification, so recorded at tier 5 with this caveat rather than assumed tier-6 unverified
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          n/a — reviews are of a third-party AI-visibility monitoring tool (Rankscale.ai), not of an AI assistant engine
metric_kind:     none
supersedes:      none
captured:        full rendered review section per product page (DOM text, JS-hydrated), category listing page (JSON-LD product/rating block), G2 category page (blocked, empty body)
```

## Query — verbatim

- `https://www.g2.com/categories/ai-search-visibility` — plain `curl` fetch (no UA): HTTP 403 (matches `channels.md` C36 expectation). Browser-extension retry (MCP_DOCKER Playwright, new tab): page loads to a bare `g2.com` title with an **empty DOM body** (`document.body.innerText` returns `""`) — blocked both ways.
- `https://www.capterra.com/p/ai-search-visibility/` — plain `curl` fetch: HTTP 403 (matches `channels.md` C37/C38 expectation). No browser-extension retry attempted this pull (time-boxed; G2's identical blocked pattern made a second identical check low-value).
- `https://omr.com/en/reviews/category/generative-engine-optimization-geo` — plain `curl` fetch: HTTP 200, extension-free. Returns a JSON-LD `ItemList` of 20 GEO-category products with `aggregateRating` (value and `reviewCount`) each — no per-review reviewer-industry data at this level.
- Product review pages opened via browser (JS-hydrated; plain `curl` returns the page shell without review content): `https://omr.com/en/reviews/product/rankscale-ai`, `https://omr.com/en/reviews/product/otterly-ai`, `https://omr.com/en/reviews/product/peec-ai`. Each page's rendered review list was scanned via `document.body.innerText` for `Industry:` fields (OMR's own per-review reviewer-company field) and for the strings `beauty`, `cosmetic`, `kosmetik`.

## Verbatim

OMR GEO-category listing (`generative-engine-optimization-geo`), JSON-LD `aggregateRating`, 20 products, review counts: Otterly.AI 4.81 (56), Rankscale.ai 4.58 (26), Peec AI 4.83 (18), Finseo 4.97 (15), ALLMO.ai 4.81 (13), Temso AI 4.83 (9), Ucited 4.94 (8), comdaily 4.94 (8), blinq 4.66 (22), Ansehn 4.79 (7), Superlines 4.75 (8), flize 4.88 (4), Vjus.AI 5.00 (3), Kai 4.75 (4), SpotLens 4.83 (3), SE Visible 5.00 (2), AirOps 5.00 (2), Kambrium 5.00 (2), GEO Analyzer 4.75 (2), Sichtbar für KI 4.50 (2).

**Rankscale.ai reviewer, industry match found**, rendered review-section text, verbatim:

> "'Good tool, helpful support'
> Source of review 3.5
> In the last 6 months
> Heidi
> Validated Reviewer
> GEO Consultant at Marcvs Group
> 1-50 employees
> Industry: Cosmetics
> Use cases: Generative Engine Optimization (GEO)
>
> What did you like? The prompt research is really helpful. And UX is also easy and straight forward. Page audit tool is also helpful for tips to improve your content
>
> What did you not like? Missing some helpful details that I've found on other tools like AthenaHQ of some helpful citation data and some content creation and tracking functions.
>
> Which problems are you solving with the product? I worked with them to test GEO strategies"

Rankscale.ai product header, same page: "Rankscale.ai 4.6 (26)... Rankscale.ai is a tool for optimizing and monitoring the visibility of AI search queries... Prices start at €20 per month." (list price, vendor-stated — not a willingness-to-pay observation per `demand-signals.md`, not used for S11).

All `Industry:` values found across the three product pages checked (15 reviews rendered per page at initial page-load, not paginated further this pull):

- **Rankscale.ai** (26 reviews total, 15 rendered): Information Technology and Services, Financial Services, Computer Software, Electrical/Electronic Manufacturing, Marketing and Advertising (×5), **Cosmetics**, Financial Services, Retail, Öffentliche Ordnung (German: "public order/administration")
- **Otterly.AI** (56 reviews total, 15 rendered): Versicherung (German: "Insurance"), Information Services, Marketing and Advertising (×2), Information Technology and Services (×2), Computer Software (×2), Electrical/Electronic Manufacturing, Sport, Möbel (German: "Furniture"), Halbleiterindustrie (German: "Semiconductor industry"), Professional Training & Coaching, Leisure Travel & Tourism, Biotechnology
- **Peec AI** (18 reviews total, 15 rendered): Internet, Consumer Goods (×2), Consumer Electronics, Events Services, Retail (×2), PR & Kommunikation, Internet, Marketing and Advertising (×2), Computer Software, Information Technology and Services, E-Learning, Real Estate

No `beauty` or `kosmetik` string match on Otterly.AI's or Peec AI's rendered review sets. "Consumer Goods" appears twice on Peec AI but is not itself the vertical the source names — per the cell-attribution rule, not mapped to skincare-and-beauty.

## Pull notes — mechanical only

- G2's category page under the browser extension returned an empty `document.body.innerText` with a generic `g2.com` page title — consistent with a bot-detection block that suppresses content rather than showing a labelled challenge page. No G2 review data reached this pull by either access path.
- OMR's product review pages are JS-hydrated: a plain `curl` fetch returns only page shell/JSON-LD, not the rendered review list: the browser extension was required to read `Industry:` and company-size fields. Only the first page of reviews (15 of each product's total) rendered without further "load more" interaction; higher review counts (Otterly.AI 56, Rankscale.ai 26, Peec AI 18) were not paginated through in full.
- Review dates on OMR are shown only as a relative bucket ("In the last 6 months") in the rendered text, not an absolute date; no absolute date was recoverable from the DOM text for the Cosmetics-industry review without a further per-review detail view, which was not opened this pull.
- Cell attribution: the Rankscale.ai/Cosmetics review states the reviewer's employer size as "1-50 employees" (OMR's own field) — this maps to the SMB band per `demand-signals.md`'s headcount-primary rule. Sub-market is organic recommendation per the review's own "Use cases: Generative Engine Optimization (GEO)" tag.

# EMARKETER — "US Search Advertising Forecast 2026" (primary landing page: abstract, key stat, headline chart)

```yaml
source:          EMARKETER — report by Nate Elliott; contributors listed on page (Shelleen Shum, Andrew Spink, Sakina Thanawala, Johann Valderrama, Emman Velasco, Max Willens, Julia Woolever, Yoram Wurmser)
url_or_doc_id:   https://www.emarketer.com/content/us-search-advertising-forecast-2026
published:       2026-05-14 ("May 14, 2026")
pull_date:       2026-09-23
pull_method:     browser (claude-in-chrome, paywall-bypass extension active); chart image by curl with DNS-over-HTTPS
pull_purpose:    evidence about a number
tier:            4
tier_reason:     named-analyst forecast, no published method; body behind EMARKETER PRO+ (client seat); only abstract, one key stat and a partially redacted headline chart are public
source_label:    analyst-derived
lane:            E
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      e-market-size-emarketer-searchad-paid-2026-09-22.md
captured:        public landing page in full (title, subtitle, byline, abstract, key question, key stat, headline chart image, wall text, authors); report body and table of contents not shown on this load
verbatim:        partial — [note: paywalled; figures and short quotes only]
```

## Verbatim

[note: paywalled; figures and short quotes only — the free landing text is reproduced in full below because it is the public abstract]

Title: "US Search Advertising Forecast 2026"
Subtitle: "Spending Grows Consistently as Amazon and AI Offset Traditional Search’s Deceleration"
"Report by Nate Elliott | May 14, 2026"

> Search ad spending is rising as search behavior spreads across more platforms and AI boosts discovery. But growth is decelerating, and search’s share of digital ad spending is slipping as budgets fragment across retail media, AI, and traditional search.

> Key Question: How are AI and retail media changing the search advertising market?

> Key Stat: Google will earn 48.5% of search ad spending in 2026, the first time in more than 20 years that number has fallen below half—and Amazon is taking the biggest chunk of its lead.

"Clients can find the full version of this chart later in the report."

Headline chart (image, alt "Google's Share of Search Advertising Will Fall Below 50% as Amazon Continues Its Rise"):

[image: docs/raw/img/e-market-size-emarketer-searchad-primary-2026-09-23/01-google-share-of-search-advertising-below-50pct.png]

[note: chart values other than those in the key stat are not transcribed here; the image is saved for IMG-1]

Wall text: "READ THIS WITH EMARKETER PRO+ … These insights are limited to EMARKETER PRO+ subscribers."

No total US search ad spend figure, no AI share of search ad spend, and no SEO-budget figure is on the public page.

## Pull notes — mechanical only

- Same access path as `e-market-size-emarketer-aiads-primary-2026-09-23.md`: tab resolved the domain; curl needed DoH. One load through the extension; PRO+ wall unchanged; the extension did not alter the page. No login, no form.
- The 2026-09-22 substitute recorded a table of contents (six section headings); this load rendered an abstract and key stat instead of the TOC. Both are recorded as seen on their dates.
- Chart image saved by curl (HTTP 200, image/png). INDEX row added.
- Comparison with substitute: substitute carried no figure; primary public page carries one figure (Google 48.5% of US search ad spending in 2026). The proxy the plan names (AI share of search ad spend / SEO budget shift) remains `unknown — checked emarketer.com 2026-09-23`.

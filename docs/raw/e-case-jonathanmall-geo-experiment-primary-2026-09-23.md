# Jonathan Mall — "GEO experiment: AI citation test" — the two inline SVG charts extracted, with their text values

```yaml
source:          jonathanmall.com (practitioner blog, English edition)
url_or_doc_id:   https://jonathanmall.com/en/geo-experiment-ai-citation-test/
published:       undated in captured text; experiment window July 2 to July 9 (as recorded in the substitute)
pull_date:       2026-09-23
pull_method:     fetch (curl, HTTP 200, 74,832 bytes); charts are inline `<svg role="img">` elements in the page HTML, saved as .svg files
pull_purpose:    evidence about a number
tier:            5
tier_reason:     practitioner self-measurement, as graded in the substitute
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT only (as in the substitute)
metric_kind:     visibility (citations, mentions)
supersedes:      e-case-jonathanmall-geo-experiment-2026-09-23.md (text complete; Jaccard chart and per-page bar chart not captured)
captured:        the two SVG charts (file + the text nodes they contain) and their figcaptions; body text is in the substitute and not duplicated
```

## Verbatim

Chart 1 — [image: docs/raw/img/e-case-jonathanmall-geo-experiment-primary-2026-09-23/01-citations-gained-171-versus-lost-32-mentions-gaine.svg] — aria-label "Citations gained 171 versus lost 32; mentions gained 32 versus lost 27"

Text nodes in the SVG: "Citations: a real shift" · "+171 gained" · "−32 lost" · "Mentions: inside the noise" · "+32 gained" · "−27 lost"

Figcaption: "Same intervention, two different outcomes: citations moved 5.3:1 beyond churn, mentions did not move at all."

Chart 2 — [image: docs/raw/img/e-case-jonathanmall-geo-experiment-primary-2026-09-23/02-eight-anonymized-pages-ranked-by-citation-gained-q.svg] — aria-label "Eight anonymized pages ranked by citation-gained queries, from 58 down to 11"

Text nodes in the SVG: "Page A (decision-stage)" 58 · "Page B (decision-stage)" 26 · "Page C (decision-stage)" 25 · "Page D (decision-stage)" 23 · "Page E (decision-stage)" 21 · "Page F (decision-stage)" 17 · "Page G (vs Expert B)" 17 · "Page H (decision-stage)" 11

Figcaption: "Citation-gained queries per page, week 1. All eight top gainers belong to the same family: pages built for a buying decision. The site's informational explainers are absent."

Featured image: `/static/illustrations/geo-experiment-ai-citation-test-featured.jpg` (alt "Brass laboratory balance scale weighing a stack of glowing web-page cards…") — illustration, not saved. The page's "Key takeaways" line reads "A controlled before/after test on 1,353 identical ChatGPT queries…" (body in the substitute).

## Pull notes — mechanical only

- curl HTTP 200; the charts are inline SVG with `role="img"` and `aria-label`, so the text values above are read from the markup, not from pixels. Saved as `.svg` with an XML header; rows in `docs/raw/img/INDEX.csv`. No wall; the bypass extension was not involved.
- The substitute's "Jaccard chart" is not a separate raster image on this page; the two SVGs are the only `role="img"` elements.

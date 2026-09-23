# 5W AI Communications — beauty AI-citation report — primary not located (one attempt)

```yaml
source:          5W Public Relations / 5W AI Communications (attempted; not reached)
url_or_doc_id:   unknown — cited by Glossy as "data from 5W AI Communications" (`raw/e-case-c8-glossy-5w-ai-beauty-citations-2026-09-22.md`); no 5wpr.com report URL found
published:       unknown — Glossy's relay published 2026-07-15
pull_date:       2026-09-23
pull_method:     fetch (curl, browser User-Agent) against 5wpr.com/new/news/, 5wpr.com/ homepage, and a site search
pull_purpose:    evidence about a number
tier:            n/a — primary not reached, no number pulled
tier_reason:     n/a
source_label:    n/a
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Claude, Perplexity, Google AI Overviews (named in the Glossy relay)
metric_kind:     n/a
supersedes:      none
captured:        n/a — wall confirmed (page never located), one adjacent finding recorded below
```

## Verbatim

Not applicable — primary not located.

## Adjacent finding — 5wpr.com does carry an AI-visibility research section, but no matching report

The 5wpr.com homepage (fetched HTTP 200, 49,869 bytes, `--compressed`) links a `/research/` section with named AI-citation studies, none titled or scoped to "ingredient-led beauty brands" or matching the Glossy-quoted figures ("The Ordinary... 7%", "Charlotte Tilbury... 4.5%", "Estée Lauder... No. 18"):

- `/research/ai-search-visibility-for-hair-styling-tools-2026-brand-study/`
- `/research/conde-nast-ai-citation-portfolio-2026/`
- `/research/tilly-norwood-ai-visibility-study-2026/`
- `/research/trade-press-ai-index-2026/`
- `/ai-citation-audit/`, `/ai-visibility-index/` (product/service pages, not the specific report)

None of these five titles names skincare, colour cosmetics, or "ingredient-led brands" — the specific report Glossy cites (or the beauty-citation data set behind Torossian's quotes) is not among the publicly linked research pages as of this pull. `https://www.5wpr.com/new/news/` (the URL previously tried and recorded 404 in the prior pull) returned HTTP 404 again this pull.

## Pull notes — mechanical only, one attempt per task instruction

- `5wpr.com/new/news/` — HTTP 404 (confirmed, same as prior pull).
- `5wpr.com/?s=AI+beauty+citations` — redirected (HTTP 301 → 200) to the plain homepage; no dedicated search-results page reached, WordPress-style query-string search not implemented at this path.
- `5wpr.com/` homepage — HTTP 200, `--compressed` needed (gzip response); five `/research/` links extracted (listed above), none matching.
- Wall confirmed standing: the specific report or dataset behind the Glossy article's "5W AI Communications" citation is not discoverable via homepage navigation or the one known dead URL in this one attempt. No further attempt made per task scope.

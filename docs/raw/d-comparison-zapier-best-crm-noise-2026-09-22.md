# Zapier — "The 11 best CRM apps" (one sample of the farmed/listicle corpus itself)

```yaml
source:          Zapier (company blog)
url_or_doc_id:   https://zapier.com/blog/best-crm-app/
published:       "originally published in 2014 by Matthew Guay... most recent update was in June 2026" (per page's own byline)
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about category noise
tier:            7
tier_reason:     listicle / roundup format — trust-rubric.md table default for tier 7. Pulled only as one sample of the "best X for Y" content type the technique produces at scale, per this cluster's task instruction ("the farmed corpus itself may be pulled only as pull_purpose: evidence about category noise ... one or two samples with the query that surfaced them"). Not cited as evidence about any number in this census
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          n/a — this pull does not test or observe any AI engine's citation of this page; it captures the page itself as a specimen of the content type
metric_kind:     none
supersedes:      none
captured:        intro paragraph, stated methodology passage, byline/update-date line
technique:       comparison-page farming — this is a specimen of the "best X for Y" sub-type named in the task definition, produced on an owned company domain (Zapier's own blog) as one of what a companion practitioner source (see pull notes) describes as a large, repeated content operation across many product categories
models_tested:   n/a
date_window:     n/a
measured_effect: no — not pulled as a measurement; no claim here is used as evidence about any number
vertical:        B2B SaaS — CRM software is explicitly the page's subject
```

## Verbatim

### Intro (quoted as returned by WebFetch)

"We put dozens of Salesforce alternatives through the wringer and came up with the 11 best CRM apps on the market."

### Stated methodology (quoted as returned by WebFetch)

"I considered a grand total of 150 CRMs, from basic solutions to enterprise-ready suites," testing by "signing up for each platform" and evaluating it by "managing a fictional marketing agency, adding contacts, scheduling activities, and evaluating how extra features improved the experience."

### Byline / update line (quoted as returned by WebFetch)

"This article was originally published in 2014 by Matthew Guay and has also had contributions from Chris Hawkins. The most recent update was in June 2026."

## Pull notes — mechanical only

- Fetched via `WebFetch` against `zapier.com/blog/best-crm-app/`, 200.
- Query that surfaced this page: this URL was located after `guptadeepak.com`'s "Programmatic SEO as Early-Growth Infrastructure for B2B SaaS Startups" article (found via HN Algolia `query=programmatic SEO`, item "Programmatic SEO as Early-Growth Infrastructure for B2B SaaS Startups," author guptadeepak, 2025-06-27) named Zapier as ranking "for millions of long-tail keywords" through this content pattern; this file is a direct fetch of one such Zapier page, not a re-pull of the guptadeepak.com article itself.
- This single page, on its own, discloses a hands-on testing methodology (150 CRMs considered, each signed up for and used) rather than reading as pure AI-generated or template-stuffed content; it is filed as a specimen of the "best X for Y" *format* the technique produces at scale — one editorially-produced instance, not proof that this specific page was produced by mass/automated means. This distinction is preserved here and not resolved into either direction.
- Two attempts to pull a comparable specimen in the high-CPA regulated vertical (`forbes.com/advisor/credit-cards/best-credit-cards/`, `investopedia.com/best-credit-cards-4842373`) were blocked — see this cluster's census "browser backlog" list. Only one vertical (B2B SaaS) is represented by an actual pulled specimen in this cluster; this is recorded as a gap, not filled by a second sample outside the "one or two samples" instruction.

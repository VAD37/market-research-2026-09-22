# DSA Transparency Database — homepage overview

```yaml
source:          European Commission, DSA Transparency Database (transparency.dsa.ec.europa.eu)
url_or_doc_id:   https://transparency.dsa.ec.europa.eu/
published:       undated — no date on page; live statistics counter
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — official Commission-operated database, regulator-published
source_label:    filed
lane:            B
sub_market:      paid placement
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page, summarized by WebFetch (model-mediated, not raw HTML dump — see pull notes)
```

## Verbatim / as reported by the fetch tool

"The Digital Services Act (DSA), obliges providers of hosting services to inform their users of the content moderation decisions they take and explain the reasons behind those decisions in so-called **statements of reasons**."

Menu item confirmed present under "Explore Data": "Research API" (no functional description given on the homepage itself).

Page includes a search function labelled "Search for Statements of Reasons" and references "various tools for accessing, analysing, and downloading the information."

Reported live statistics shown on the page at pull time: nearly 4 billion statements submitted; 373 active platforms; 43% of fully automated decisions; most common violations cited as terms-of-service violations and unsafe products.

**No mention of advertising, ad repositories, or Article 39 anywhere on the homepage**, per the fetch tool's read of the page.

## Pull notes — mechanical only

- Pulled via WebFetch (model-mediated HTML-to-markdown conversion + summarization against a prompt), not a verbatim raw HTML/text dump — quoted lines above are the tool's direct quotations from the page; unquoted lines are the tool's paraphrase of page content and are flagged as such in this file.
- This finding — that the central transparency database carries no advertising content and is statements-of-reasons only — corroborates the correction already recorded in `docs/sources/channels.md` row C60 (a prior agent's read, dated 2026-09-22) and in `docs/sources/shortlist.md` cluster P2-c10's done-when text. Independently confirmed here by direct pull, not inherited.

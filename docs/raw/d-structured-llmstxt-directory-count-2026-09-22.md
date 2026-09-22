# directory.llmstxt.cloud — self-submitted llms.txt directory, live count

```yaml
source:          directory.llmstxt.cloud
url_or_doc_id:   https://directory.llmstxt.cloud/
published:       n/a — live, continuously updated count page
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     disclosed method (self-submission, "Submit your llms.txt" call-to-action present on every page) but no crawl-based or random-sample methodology, no independent verification of the count, no date-of-count stamp. Sits with "vendor or agency study with n, dates, method" per trust-rubric.md's tier-5 band, downgraded from tier-4-adjacent "directory with method disclosed" because the disclosed method is voluntary self-submission, a strong selection bias, not a population-representative crawl
source_label:    vendor-reported
lane:            D
sub_market:      organic recommendation
engine:          n/a — cross-site directory count, not engine-specific
metric_kind:     none
supersedes:      none
captured:        homepage total-count figure and "Submit your llms.txt" mechanism text; full per-site listing not captured
```

## Verbatim

Homepage count widget, as rendered 2026-09-22: "All **3,829** websites — Directory →"

Site-wide call to action, present in the header/navigation on every page: "Submit your llms.txt"

Category breakdown visible in navigation (partial, as captured): "Finance 275" [category count for one vertical; other category counts present in the same navigation block but not individually captured in this pull]

## Pull notes — mechanical only

- Fetched via `curl`; the homepage total renders in static HTML (no JS-rendering wall needed for the headline count itself), though the full per-site listing appeared to be a larger interactive table not fully captured by this pull's plain-text extraction.
- **This directory is explicitly self-submission-based** ("Submit your llms.txt" is the site's own primary call to action, present sitewide) — not a crawl of the open web. This is the same directory `d-structured-llmstxt-org-spec-2026-09-22.md`'s own spec page names as one of three community-maintained llms.txt directories (alongside `llmstxt.site` and `llmstxthub.com`), and the same one `d-structured-llmstxtio-adoption-blog-2026-09-22.md` cites secondhand at "approximately 684 implementations" as of roughly mid-2025.
- **Directly comparable, same source, two dates**: ~684 (mid-2025, per the llms-txt.io blog's secondhand citation, not independently re-verified) → 3,829 (2026-09-22, this pull, direct). A roughly 5.6× increase over about 14 months on the same directory, **if** the earlier figure is accurate — the earlier figure was not independently re-verified in this pull (no archived snapshot of directory.llmstxt.cloud from mid-2025 was checked), so this comparison is recorded as directional only, not as a precise growth rate.
- Self-submission bias runs in **both** directions and is not sign-determinate: it undercounts the true population of sites carrying llms.txt (most site owners never submit to a directory), while simultaneously overrepresenting llms.txt-adopters/enthusiasts relative to the general web (only sites whose owners are aware of and motivated to use this specific directory appear at all). Neither this count nor the Borysenko/Redocly/Google findings on whether engines *read* the file are comparable numbers — this file measures publisher-side adoption (how many sites have the artefact and chose to list it), not engine-side consumption.
- `llmstxt.site` (the other directory named in the spec) returned HTTP 200 but a very large (2.66MB) client-side-rendered page; its own stated total count was not successfully extracted by this pull's plain-text method and is recorded as `unknown — checked https://llmstxt.site/ 2026-09-22, page requires JS rendering not available to this fetch-only pull` — a browser-backlog item.

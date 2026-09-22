# Coty Inc. — FY2026 Form 10-K — generative engine optimization mention

```yaml
source:          Coty Inc. (SEC filer, ticker COTY)
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1024305/000102430526000048/coty-20260630.htm (accession 0001024305-26-000048)
published:       2026-08-20
pull_date:       2026-09-22
pull_method:     fetch (efts.sec.gov EDGAR full-text search API, then direct document fetch from sec.gov/Archives)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — SEC-filed 10-K (Item 1 Business section), filed source per trust-rubric.md tier table
source_label:    filed
lane:            F
sub_market:      organic recommendation
engine:          n/a — no engine named
metric_kind:     none
supersedes:      none
captured:        section "Item 1. Business — Marketing" excerpt, ~2400-character window around the matched phrase; full document (678,345 characters of extracted text) searched for the alias-set (O) terms
```

## Query — verbatim

EDGAR full-text search API: `https://efts.sec.gov/LATEST/search-index?q=%22generative%20engine%20optimization%22&entityName=Coty%20Inc` — 1 of 1 hit, form 10-K, filed 2026-08-20, period ending 2026-06-30.

Same entity also queried (0 hits each, run 2026-09-22): `"AI visibility"`, `"citation rate"`, `"share of voice in AI answers"`, `"LLM SEO"`, `"AI SEO"`, `"AI search optimization"`, `"AI discoverability"`, `"answer engine optimization"`, `"ChatGPT"`, `"AI Overviews"`.

Same alias-set terms also queried against `entityName=Estee Lauder`, `entityName=elf Beauty`, `entityName=Ulta Beauty`, `entityName=Inter Parfums` — 0 hits each, run 2026-09-22.

## Verbatim

From Item 1, Business — Marketing section:

> "We have implemented artificial intelligence (AI) tools to power our media allocation models and support content creation and optimization, including search engine optimization copy generation and translation, to improve efficiency and reach of our marketing campaigns. We are also deploying improvements across touchpoints to drive generative engine optimization, to strengthen our brands visibility and recommendations by top AI platforms."

No dollar figure, headcount, or budget line is attached to this sentence or within the surrounding ~2,400-character window (Marketing section through the start of "Distribution Channels and Retail Sales"). The passage is the only occurrence of "generative engine optimization" in the filing (single match, EDGAR full-text search, exact phrase).

Company context, same filing: Coty Inc., NYSE: COTY, SIC 2844 (Perfumes, Cosmetics & Other Toilet Preparations), fiscal year ended 2026-06-30, business locations New York, NY. Company sells in approximately 122 countries and territories per the same section (company-stated scale, not independently re-verified this pull).

Buyer-size proxy, same filing, Item 1 "Human Capital" section: "As of June 30, 2026, we had approximately 11,335 employees in over 37 countries." Per `demand-signals.md`'s headcount-primary buyer-size rule, 11,335 employees maps to the **Enterprise** band (1000 or more). This is the filing's own disclosure, in the same document as the generative-engine-optimization passage, and is used to attribute this signal's cell.

## Pull notes — mechanical only

- EDGAR full-text search API queried directly via `efts.sec.gov/LATEST/search-index`, one query per alias term, `entityName` parameter used to scope to the named filer. Full document then fetched from its `sec.gov/Archives/edgar/data/...` URL, HTML tags stripped programmatically, and searched for the phrase to extract surrounding context.
- No paywall, login wall, or truncation encountered. Full 10-K document retrieved (4.3 MB raw HTML, ~678K characters after tag-stripping).
- `entityName` filtering behaves as a keyword match against `display_names`, not a strict CIK filter — verified against the returned `display_names` field on each hit, which named only "COTY INC. (COTY) (CIK 0001024305)".
- No search was made for a dollar figure elsewhere in the 10-K tied to this specific initiative (e.g., a marketing technology or AI capex line) — the "Marketing" section text above is the full context captured for this mention. A wider search of the same filing for AI-specific spend lines was not performed this pull; flagged as a gap.

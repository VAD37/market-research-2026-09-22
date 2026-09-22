# DSA Transparency Database — Research API

```yaml
source:          European Commission, DSA Transparency Database (transparency.dsa.ec.europa.eu)
url_or_doc_id:   https://transparency.dsa.ec.europa.eu/page/research-api
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — official Commission-operated database documentation
source_label:    filed
lane:            B
sub_market:      paid placement
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page, summarized by WebFetch (model-mediated — see pull notes)
```

## Verbatim / as reported by the fetch tool

"The DSA Transparency Database Research API empowers interested stakeholders with the relevant technical knowledge to retrieve specific subsets of data." Stated purpose: "facilitates longitudinal and cross-platform studies of content moderation patterns and trends."

Access steps reported: create an EU Login account; visit the DSA Transparency Database; contact `CNECT-DSA-HELPDESK@ec.europa.eu` with login details; receive a Bearer-token credential.

Endpoints reported:
- POST `/api/v1/research/search` — complex OpenSearch DSL queries
- POST `/api/v1/research/sql` — SQL-like analysis queries
- POST `/api/v1/research/count` — document counting
- POST `/api/v1/research/query` — OpenSearch DQL filtering
- GET `/api/v1/research/aggregates/{date}` — trend analysis
- GET `/api/v1/research/labels` — classification values
- GET `/api/v1/research/platforms` — platform metadata

Query filters reported as available: category, decision type, automation status, territorial scope, content language, date ranges. "The index contains statements from the last 6 months only."

Constraints reported: maximum 1,000 rows per query (no pagination); 5 MB maximum response size; 30-second maximum execution time; read-only access.

**"No mention of advertising data" appears in this documentation, per the fetch tool's read.**

## Pull notes — mechanical only

- Pulled via WebFetch (model-mediated), not a verbatim raw dump.
- Confirms the Research API queries the same statements-of-reasons content-moderation index described in `b-eu-dsa-api-documentation-2026-09-22.md` — it is not a separate advertising dataset and exposes no Article 39 fields.

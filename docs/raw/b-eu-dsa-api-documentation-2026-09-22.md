# DSA Transparency Database — API and schema documentation

```yaml
source:          European Commission, DSA Transparency Database (transparency.dsa.ec.europa.eu)
url_or_doc_id:   https://transparency.dsa.ec.europa.eu/page/api-documentation
published:       schema stated as "updated on 1 July 2025"; page itself undated beyond that
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — official Commission-operated database schema documentation
source_label:    filed
lane:            B
sub_market:      paid placement
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page, summarized by WebFetch (model-mediated — see pull notes)
```

## Verbatim / as reported by the fetch tool

API endpoints listed: `https://transparency.dsa.ec.europa.eu/api/v1/statement` (POST, single statement creation); `https://transparency.dsa.ec.europa.eu/api/v1/statements` (POST, multiple statements creation); `https://transparency.dsa.ec.europa.eu/api/v1/statement/existing-puid/<PUID>` (GET, PUID verification).

Statement-of-reasons schema field list, as reported by the tool, grouped by the page's own headings:

- Decision-related: `decision_visibility` (array), `decision_visibility_other` (text, max 500 chars), `decision_monetary` (enum), `decision_monetary_other` (text, max 500 chars), `decision_provision` (enum), `decision_account` (enum), `decision_ground` (enum), `decision_ground_reference_url`, `decision_facts` (required, max 5000 chars)
- Content classification: `content_type` (array), `content_type_other` (text, max 500 chars), `category` (required, enum), `category_addition` (optional, enum), `category_specification` (array of keywords), `category_specification_other` (text, max 500 chars)
- Content details: `content_id` (key-value, e.g. "EAN-13"), `content_language` (ISO 639-1), `content_date` (YYYY-MM-DD)
- Legal/compliance: `illegal_content_legal_ground` (text, max 500 chars), `illegal_content_explanation` (text, max 2000 chars), `incompatible_content_ground` (text, max 500 chars), `incompatible_content_explanation` (text, max 2000 chars), `incompatible_content_illegal` ("Yes"/"No")
- Temporal: `application_date` (required, YYYY-MM-DD), `end_date_visibility_restriction`, `end_date_account_restriction`, `end_date_monetary_restriction`, `end_date_service_restriction` (all YYYY-MM-DD, optional)
- Source & automation: `source_type` (required, enum), `source_identity` (text, max 500 chars, optional), `automated_detection` (required, "Yes"/"No"), `automated_decision` (required, enum)
- Geographic & identifier: `territorial_scope` (required, array of 2-letter ISO country codes), `account_type` (optional, enum), `puid` (required, max 500 chars, alphanumeric/hyphens/underscores)

"The submission schema was updated on 1 July 2025 to reflect the requirements laid down in the Implementing Regulation on Transparency Reporting. Statements of reasons submitted before 1 July 2025 remain available according to the old schema."

**No field in this schema is advertising-related** — no `ad_status`, no ad category, no ad-content or ad-targeting field of any kind, per the tool's read.

## Pull notes — mechanical only

- Pulled via WebFetch (model-mediated), not a verbatim raw dump of the schema page's markup; field names quoted above are the tool's direct transcription and should be treated as reliable for field *names* but re-verified against the live page before any compiled file cites exact character limits.
- This is the content-moderation statement-of-reasons schema, not an advertising schema — confirms (independently of `channels.md` C60's prior note) that the central DSA Transparency Database carries no Article 39 ad-repository data or fields at all. Ad repositories are per-service, reached through each engine's own page — see the individual engine files in this cluster.

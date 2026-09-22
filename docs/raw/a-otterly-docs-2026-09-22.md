# Otterly.AI — docs / changelog

```yaml
source:          Otterly.AI (docs.otterly.ai — "OtterlyAI Public API," built on Mintlify)
url_or_doc_id:   https://docs.otterly.ai/
published:       undated
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary developer documentation
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        docs homepage in full
```

## Verbatim

"Introduction - OtterlyAI Public API

Documentation Index — Fetch the complete documentation index at: /llms.txt — Use this file to discover all available pages before exploring further.

# Introduction

Welcome to the OtterlyAI Public API

The OtterlyAI Public API lets you programmatically access brand reports, prompts, citations, agent analytics (AI crawler traffic on your own domains), and workspace data from the OtterlyAI platform.

## Base URL
https://data.otterly.ai
All endpoints are prefixed with /v1.

## OpenAPI Spec
The full machine-readable spec is published at:
https://data.otterly.ai/v1/openapi.json
This documentation is generated directly from that spec, so it is always in sync with the deployed API.

## Quick Start
1. Generate an API key from your OtterlyAI dashboard.
2. Send it as a Bearer token in the Authorization header.
3. Call any endpoint listed in the API Reference.

curl https://data.otterly.ai/v1/health -H 'Authorization: Bearer YOUR_API_KEY'

Navigation: Guides | API Reference | Getting Started. Footer: Product (Dashboard, Get API Key), Resources (Blog, Help Center), Legal (Terms, Privacy, Imprint). 'This documentation is built and hosted on Mintlify, a developer documentation platform.'"

## Pull notes — mechanical only

- Unlike Scrunch, Brandlight, Change Agents Corp, and Locafy, Otterly.AI has a real, dedicated, publicly-reachable documentation subdomain (`docs.otterly.ai`) with a published OpenAPI spec (`data.otterly.ai/v1/openapi.json`, not independently fetched this pull) and an `/llms.txt` machine-readable index (also not independently fetched this pull — noted as existing, not verified further).
- No changelog page specifically was located within this single-page pull of the docs homepage; the docs site's own sitemap (`docs.otterly.ai/sitemap.xml`, referenced in `otterly.ai/sitemap.xml`) was not separately crawled this task for a changelog entry — recorded as `unknown — checked docs.otterly.ai homepage only, changelog page not individually located, 2026-09-22`.
- This is the strongest "docs" page found across all six vendors in this cluster.

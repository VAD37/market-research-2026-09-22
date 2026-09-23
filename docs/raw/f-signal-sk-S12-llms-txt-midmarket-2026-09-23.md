# Measured-by-us — /llms.txt on two SEC-confirmed mid-market beauty domains (S12), plus one corporate-domain block

```yaml
source:          our own HTTP checks against olaplex.com, hydrafacial.com, beautyhealth.com
url_or_doc_id:   https://olaplex.com/llms.txt; https://www.olaplex.com/llms.txt; https://www.hydrafacial.com/llms.txt; https://hydrafacial.com/llms.txt; https://www.beautyhealth.com/llms.txt; https://beautyhealth.com/llms.txt
published:       undated — live domain checks
pull_date:       2026-09-23
pull_method:     fetch (curl, browser User-Agent header, redirects followed — same method as `f-signal-sk-S12-llms-txt-beauty-domains-2026-09-22.md`)
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us per demand-signals.md S12
source_label:    measured-by-us
lane:            F
sub_market:      organic recommendation
engine:          n/a — artifact readable by any crawler naming itself, not engine-specific
metric_kind:     none
supersedes:      none
captured:        HTTP status code and first ~300–500 characters of response body per domain
```

<!-- measured-by-us pulls add these four lines: -->
prompt_set: n/a — not a panel run
runs_n: 3 domains (6 hostname variants: bare and `www.`)
surface: n/a — HTTP artifact check, not a chat surface
region: n/a — single unauthenticated check per domain, no region parameter set

## Query — verbatim

`curl -s -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" https://<domain>/llms.txt` run against each of six hostnames (bare and `www.` for each of three companies), redirects followed.

## Verbatim — results table

| Domain | Company (SEC-filed headcount, band) | Status | Body first bytes |
|---|---|---|---|
| olaplex.com | OLAPLEX Inc. (278 employees, mid-market) | 200 | `# Agent Instructions — OLAPLEX Inc.` — "This document describes how AI agents can interact with OLAPLEX Inc.'s online store at https://olaplex.com. ## For Personal Shopping Assistants and Agents Acting On Behalf of a User If you are reading this on behalf of your user and you act as a personal assi[stant]..." — genuine, brand-authored agent-instructions artifact |
| www.olaplex.com | same | 200 | identical content (redirects to same page) |
| hydrafacial.com | The Beauty Health Company (613 employees, mid-market) | 200 | `# Agent Instructions — Hydrafacial North America Marketing` — "This document describes how AI agents can interact with Hydrafacial North America Marketing's online store at https://www.hydrafacial.com. ## For Personal Shopping Assistants and Agents Acting On Behalf of a User If you are reading this..." — genuine, brand-authored agent-instructions artifact |
| www.hydrafacial.com | same | 200 | identical content |
| beautyhealth.com | The Beauty Health Company, corporate/IR domain | 403 | Akamai "Access Denied" — "You don't have permission to access "http://www.skinhealthsystems.com/" on this server." (internal redirect target named in the block page), `Reference #18.1e042c17...` — not reached, access-blocked |
| www.beautyhealth.com | same | 403 | same Akamai block |

Tally: 2 of 2 SEC-confirmed mid-market beauty companies (Olaplex, Beauty Health) serve a genuine, brand-authored llms.txt artifact on their consumer/commerce domain (olaplex.com, hydrafacial.com). The corporate/IR domain for one of the two (beautyhealth.com) is access-blocked (Akamai 403) and was not reached at all — recorded as **not present, access-blocked**, not counted against the consumer-domain result.

## Pull notes — mechanical only

- Same request profile as the enterprise-tier sample in `f-signal-sk-S12-llms-txt-beauty-domains-2026-09-22.md` (browser UA, `-L`), for consistency. No JavaScript rendering needed — both genuine artifacts served as static HTTP content.
- `beautyhealth.com`'s block page names `skinhealthsystems.com` as its internal redirect target, suggesting the corporate domain sits behind an Akamai WAF unrelated to the consumer-facing Hydrafacial storefront (which is unblocked). Not retried under a different header profile — out of this pull's scope, which targets the two companies' primary commerce/brand domains, already answered by hydrafacial.com.
- No login wall or paywall on any of the six checks.

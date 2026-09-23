# Adthena "Monthly AI Data Pulse" June 2026 — locate check (re-pull 2)

```yaml
source:          Adthena — resources page crawl
url_or_doc_id:   https://www.adthena.com/resources/ (checked for a link to the June 2026 "Monthly AI Data Pulse"); primary is LinkedIn-distributed, URL still not located
published:       unknown — no day/month beyond "June 2026" from prior PPC Land pointer pull
pull_date:       2026-09-23
pull_method:     fetch (curl) — Chrome extension unavailable this session, see Pull notes
pull_purpose:    evidence about a number
tier:            6
tier_reason:     hidden method drops from vendor-reported default — primary document still unlocated, this pull is a negative check only
source_label:    vendor-reported
lane:            B
sub_market:      paid placement
engine:          n/a
metric_kind:     none
supersedes:      none — b-pointer-ppcland-uk-chatgpt-ad-share-2026-09-22.md is the PPC Land pointer pull; this is a separate locate attempt, not a re-pull of that source
captured:        HTTP status and page text only, no document found
```

## Verbatim

`https://www.adthena.com/resources/` returned HTTP 200 (103,936 bytes). Page text searched (case-insensitive) for "data pulse" and "June 2026": zero matches for either string.

## Pull notes — mechanical only

- Chrome browser extension (`ext`) was unavailable for this pull: `tabs_context_mcp` returned "Browser extension is not connected" on three attempts (2026-09-23). Fell back to `curl` per the assigning task's "only if cheap" allowance; stopped after one round since the primary source (LinkedIn-distributed) is a login wall, which stays untouched under the repo's browser rules regardless of `ext` availability.
- No lift possible without the primary document. Status unchanged from `repull-audit-2-2026-09-23.md` row 37 ("doc not found").

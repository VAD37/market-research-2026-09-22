# AthenaHQ — primary funding record (attempted — Crunchbase, PitchBook blocked)

```yaml
source:          Crunchbase (attempted), PitchBook (attempted) — both returned HTTP 403 to this pull's fetch tool; Tracxn not attempted (same access pattern expected, no browser extension available to work around it)
url_or_doc_id:   https://www.crunchbase.com/organization/athenahq ; https://pitchbook.com/profiles/company/759029-50 ; https://tracxn.com/d/companies/athenahq/ (not attempted, path truncated in docs/raw/a-vendor-roster-2026-09-22.md row 8)
published:       n/a — no content retrieved
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            n/a — no content retrieved to tier
tier_reason:     both attempted URLs returned HTTP 403 (bot-blocked) to plain fetch; browser extension unavailable this session (reported "not connected"); WebSearch tool budget exhausted this session (200/200) before an alternative source could be located
source_label:    n/a
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        none — this file documents the blocked pull attempt, per task instruction to record a missing/inaccessible page rather than skip it silently
```

## Verbatim

No content retrieved. Both attempted fetches returned:

`https://www.crunchbase.com/organization/athenahq` — HTTP 403
`https://pitchbook.com/profiles/company/759029-50` — HTTP 403

`docs/raw/a-vendor-roster-2026-09-22.md` row 8 (AthenaHQ) itself cites Crunchbase, PitchBook and Tracxn as the sources that rostered this vendor under limb (a) (four independent non-listicle sources), but records no funding amount, round stage, or date from any of them in its own "what the source says it sells" column — meaning no dollar figure for AthenaHQ's funding has been captured by this research programme at any point, including at roster-build time.

AthenaHQ's own site (pricing and careers pages, both pulled this session — `a-athenahq-pricing-2026-09-22.md`, `a-athenahq-careers-2026-09-22.md`) states no funding figure, no investor name, and no founding date anywhere.

## Pull notes — mechanical only

- Fetched via plain fetch tool (raw=false). Browser extension reported "not connected" at the start of this session (see this cluster's other vendor files for the same note) and was not available to work around Crunchbase's or PitchBook's bot-blocking.
- WebSearch tool returned: "Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls)" when queried for "AthenaHQ athenahq.ai funding round amount seed Series A 2026" — no alternative source was located as a result.
- Tracxn (`tracxn.com/d/companies/athenahq/...`) was not attempted directly — the roster file's URL for it is truncated with an ellipsis and the exact path is not known; given Crunchbase and PitchBook both blocked plain fetch, and Tracxn is a similar paywalled company-data aggregator, it was judged unlikely to succeed and was not attempted, to conserve remaining fetch calls for the other seven vendors and remaining page types in this cluster.

## Caveats

- AthenaHQ's funding total, round stage, lead investor and date are all recorded `unknown — checked crunchbase.com (403), pitchbook.com (403), athenahq.ai/pricing, athenahq.ai/careers 2026-09-22` in the census summary. This is a genuine absence in this research programme as of 2026-09-22, not merely this cluster's own gap — the roster file that rostered AthenaHQ under limb (a) also carries no dollar figure for it.

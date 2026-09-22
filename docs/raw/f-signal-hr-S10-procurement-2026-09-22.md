# SAM.gov, UK Contracts Finder, TED — S10 procurement records, high-CPA regulated vertical

```yaml
source:          SAM.gov (sam.gov), UK Contracts Finder (contractsfinder.service.gov.uk), TED — Tenders Electronic Daily (ted.europa.eu)
url_or_doc_id:   https://sam.gov/api/prod/sgs/v1/search/?q=%22generative+engine+optimization%22 ; https://sam.gov/api/prod/sgs/v1/search/?q=%22AI+visibility%22 ; https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search?keyword=generative+engine+optimization ; https://ted.europa.eu/en/search/result?scope=ALL&query=generative+engine+optimization
published:       n/a — live registry query results as of pull date
pull_date:       2026-09-22
pull_method:     fetch (direct curl, no browser extension)
pull_purpose:    evidence about a number
tier:            2 per `demand-signals.md` S10 catalog (table default), applied to the access/method record below — no qualifying award was found to tier
tier_reason:     table default
source_label:    filed
lane:            A, F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        JSON API responses (SAM.gov, UK Contracts Finder) and HTML challenge response (TED); title fields grepped from each response
vertical:        high-CPA regulated
cell:            n/a — no qualifying award found
query:           see table below, verbatim
```

## SAM.gov — accessible, no qualifying result

API endpoint `sam.gov/api/prod/sgs/v1/search/?random=1&index=opp&q=<query>&is_active=true&page=0` returned **200** for both queries tried:

- `q="generative engine optimization"` — top titles returned: "Generative Artificial Intelligence (GenAI) Electronic Performance Support System (EPSS)," "Schriever Cyber Threat Intelligence Software," "Generative Unconstrained Intelligence Drug Engineering (GUIDE)," "Self-Paced Military/Leadership AI Training," "Integrated Air and Missile Defense (IAMD) Battle Command System" — the query matched "generative," "optimization" as separate tokens across unrelated defense/GenAI procurements; none is a GEO/AI-visibility purchase, and none names insurance, credit cards, or supplements.
- `q="AI visibility"` — top titles returned: "AEMS Think Trends Licenses," "RFI - DCSA Personnel Security Alert Management Platform," "Enterprise Artificial Intelligence (AI) Strategy," "Clearview AI for facial recognition technology," "NSF X-Labs Initiative – AI for Physical Systems" — same pattern, no qualifying match.

This is consistent with S10's own catalog bias line: "Public-sector and large-buyer only; private demand invisible here." Insurance, credit cards, and supplements are overwhelmingly private-sector purchasing categories; SAM.gov's federal-procurement scope structurally cannot see them.

## UK Contracts Finder — accessible, but keyword filter did not apply

`contractsfinder.service.gov.uk/Published/Notices/OCDS/Search?keyword=generative%20engine%20optimization` returned **200** and a well-formed OCDS (Open Contracting Data Standard) JSON payload, but on inspection the 100 returned records are a **generic, unfiltered recent-notices feed** — the first record inspected is "WSCC Route 70021 Poulbourgh to Minerva May School - 4 seats, no PA, REGULAR TEAM" (a West Sussex school-transport contract), with no relationship to the query text. The `keyword` query parameter does not appear to filter this particular API surface as this pull invoked it.

**Result: `unknown — checked contractsfinder.service.gov.uk OCDS search API 2026-09-22; keyword parameter did not filter results (returned unrelated generic notices); correct filtering parameter/endpoint not identified this pull`.**

## TED (EU tenders) — blocked

`ted.europa.eu/en/search/result?scope=ALL&query=generative+engine+optimization` returned **405**, with response body titled "Human Verification" — consistent with `channels.md` C20's recorded access code ("405 to plain GET — search API or ext"). Not resolved this pull; recorded as a **browser backlog** item.

## Result, high-CPA regulated

**`none — checked sam.gov API (200, no qualifying match) 2026-09-22`**; **`unknown — checked contractsfinder.service.gov.uk (200, keyword filter appears non-functional as invoked) 2026-09-22`**; **`unknown — checked ted.europa.eu (405, human-verification block) 2026-09-22`**.

## Caveats

- S10's own catalog entry predicts this outcome for a heavily private-sector vertical: "Public-sector and large-buyer only; private demand invisible here." A `none` or `unknown` result on this signal is the expected shape for this vertical, not a search failure.
- The UK Contracts Finder result is recorded as `unknown` rather than `none` specifically because the filter itself could not be confirmed working — a `none` read requires confidence that a real search ran and returned nothing, which this pull cannot support.

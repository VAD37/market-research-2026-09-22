# S2 vendor customer counts and S3 funding/ARR — citation of Pass 3 vendor census, B2B SaaS filter

```yaml
source:          this repo's own docs/raw/ — Pass 3 vendor census files a-vendor-census-c1 through c4
url_or_doc_id:   docs/raw/a-vendor-census-c1-2026-09-22.md ; a-vendor-census-c2-2026-09-22.md ; a-vendor-census-c3-2026-09-22.md ; a-vendor-census-c4-2026-09-22.md
published:       2026-09-22 (all four cited files landed same day, Pass 3)
pull_date:       2026-09-22
pull_method:     manual (citation of prior same-day raw pulls; this file re-checked all four census files directly for the literal string "SaaS", no new fetch)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     table default for S2 ("5 with n and date, 6 without") and S3 ("2 filed, 5 stated") — inherited from whichever underlying vendor pull is cited; this file adds no new pull of its own
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        n/a — cross-reference only; grep run directly against the four cited census files for "SaaS"
```

## Verbatim

Direct string search for `SaaS` run against all four census files:

- `a-vendor-census-c1-2026-09-22.md`: one match, in a long context line not reproduced verbatim by the search tool's line-omission behaviour (the match itself was in a table row too long to display inline); on inspection this is a single occurrence, not a customer-roster entry naming a B2B SaaS customer with a count.
- `a-vendor-census-c2-2026-09-22.md`: **no match.**
- `a-vendor-census-c3-2026-09-22.md`: **no match.**
- `a-vendor-census-c4-2026-09-22.md`: one match — the roster row for **Onclusive**: "(1) existing G2 category listing (`a-vendor-roster-2026-09-22.md` §3a). (2) `find-and-update.company-information.service.gov.uk/search/companies?q=Onclusive` — 'ONCLUSIVE UK LIMITED, 08984741 - Incorporated on 8 April 2014...'" — this is a UK Companies House filing corroborating **Onclusive's own** incorporation (Onclusive is itself the AI-visibility vendor being rostered, not a customer of one), tagged in the roster row as meeting roster limb (a) and arguably (b). **It is not a customer-count or logo-roster entry, and it does not name any customer as B2B SaaS.**

No row in any of the four census files names a customer, logo, or case-study subject as a B2B SaaS company alongside a disclosed count, ARR figure, or funding amount, in the text captured by this string search.

## Pull notes — mechanical only

- **Result: `none — checked a-vendor-census-c1 through c4 2026-09-22` for both S2 (customer counts/logos tagged B2B SaaS) and S3 (funding/ARR tied to a B2B SaaS customer segment).** This is a genuine, disciplined absence: the Pass 3 census files list AI-visibility **vendors'** own funding, pricing and customer-roster data (e.g. Profound's $180M Series D per `a-vendor-census-c1`), but none of the vendor-reported customer logos/case-study rosters in these four files is itself tagged, in the source's own words, as a B2B SaaS company — per `demand-signals.md`'s cell-attribution rule, this repo does not infer a customer's vertical from a vendor's roster page without the source itself stating it.
- Contrast, recorded for completeness and not double-counted here: Pass 4's `e-case-census-c2-2026-09-22.md` (agency data posts) **does** carry a B2B SaaS-tagged case (Quattr's client CloudEagle, tagged "B2B SaaS (Spend Management)," Bronze grade) and `e-case-census-c4-2026-09-22.md` carries two more (RankPrompt/Humand, "B2B SaaS · HR technology," Bronze; Rankscale/"AI SMS Platform," "AI SMS Software / B2B SaaS," Fools gold) — these are Pass 4 success-story evidence, not Pass 3 vendor-census S2/S3 evidence, and are out of this file's remit; they are the caller's own case-file citations (per the task brief's read-only inputs) and are not re-pulled or re-graded here.
- Buyer size: not applicable — no cell is moved by this file's own finding (a clean `none`).
- No new fetch was performed by this file; it exists solely to give S2/S3 a dedicated citation entry in the B2B SaaS signal census with its own explicit finding, since the task brief names S2/S3 as inputs to read rather than re-pull.

# Trust rubric

Set 2026-09-22. How a source is scored before anything from it enters `docs/raw/`, and how it is labeled once it does. Applies to every pull. The global source labels in root `CLAUDE.md` — vendor-reported, analyst-derived, filed, company-stated, measured-by-us — say *what kind* of number it is. This file says *whether to keep it*.

This field sells measurement. A rubric is not optional overhead here; it is the product of the first pass.

## Tiers

| Tier | Source kind | Use |
|---|---|---|
| 1 | Measured by us, output in `raw/` | Highest. Cite freely |
| 2 | Filed — S-1, 10-K, court exhibit, funding filing | High |
| 3 | Platform primary — own docs, changelog, pricing page | Reliable on existence, biased on framing |
| 4 | Panel, clickstream, infrastructure telemetry | Usable if method published. Hidden method drops one tier |
| 5 | Vendor or agency study with n, dates, method | Usable, bias flagged inline |
| 6 | Vendor blog, no n | Marketing. Not a source |
| 7 | Listicle, roundup, affiliate comparison | Zero. Do not pull |

Tier 6 and 7 may be pulled as *evidence about the category's noise level*, filed under `raw/` and labeled as such. Never as evidence about a number.

## Discard on sight

- No n, no date window, or no method
- "Studies show" with no link
- Percentage with no base — plus 1200 percent from 3 to 39
- One screenshot of one AI answer offered as proof. Stochastic system, n equals one, that is noise
- Vendor measuring the thing it sells, no third-party replication
- A forecast presented as a measurement. When found, downgrade the whole author
- Referral traffic reported as influence
- Correlation reported as incrementality

## Trust rises when

- Prompt set, raw data, or method appendix is published
- Sample size, date window, and model versions are all stated
- Result runs against the publisher's commercial interest
- An unrelated party replicated it
- Uncertainty is quantified, or its absence is admitted

## Recording

Every `raw/` file states source, URL or document ID, pull date, pull method — per `docs/CLAUDE.md` — and adds one line: `tier: <1-7>` plus the reason if the tier was adjusted.

## Caveats

- Tiers rank provenance, not correctness. A tier 2 filing still carries the filer's framing.
- Tier 4 is where most of this field's public numbers live, and where method disclosure varies most. Check every time; do not inherit a prior judgment about a provider.

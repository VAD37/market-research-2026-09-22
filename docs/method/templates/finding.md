# Template — `docs/findings/<finding>.md`

**Budget: 100 lines** for the produced file (`../plan.md`). One question per file. Section order below is binding.

Rules: a finding cites the compiled files behind it, and through them `raw/`. A finding that cannot name its evidence is deleted, not softened (`docs/CLAUDE.md`). No new facts: a number appearing nowhere else in `docs/` means a pull is missing. Every claim carries a tier. Survivorship is stated once, with screened and cleared counts, wherever the finding rests on published cases. The verdict is the user's call — produce the evidence, not the go/no-go, unless asked.

No execution language anywhere: no dates for future work, no budgets, no recommendations, no build steps.

---

<!-- Copy from here down. Delete these guidance comments. -->

# <Finding title>

| | |
|---|---|
| File date | <YYYY-MM-DD> |
| Oldest pull depended on | <YYYY-MM-DD> — `raw/<file>.md`, via `<compiled file>` |
| Lane | <A-F> |
| Hypotheses touched | <H1..Hn from `../hypotheses.md`, or "none"> |
| Claims at tier 3 or better | <n of n> |

## Question

> <One question. The same one this file answers and nothing wider.>

## Answer

<Three sentences at most. States which of the three metrics it is about, per `../glossary.md`. States what the evidence supports, and stops there. An absence — "no Gold case exists as of <YYYY-MM-DD>" — is a legitimate answer and is written plainly.>

## Evidence

| # | Evidence | Metric | Compiled file | Raw behind it | Label | Tier |
|---|---|---|---|---|---|---|
| E1 | <12 words max, figure verbatim> | <visibility / traffic / sales> | `<markets\|competitors\|customers>/<file>.md` | `raw/<file>.md` | <label> | <1-7> |

Conflicting evidence sits here side by side, attributed, never averaged. Mark the pair: `E3 conflicts with E4 — not reconciled`.

## Claims

Each claim maps to the evidence rows carrying it. A claim with no evidence row is deleted.

| # | Claim | Evidence | Tier of the weakest row | Grade, if a success story | Load-bearing |
|---|---|---|---|---|---|
| C1 | <one sentence> | E1, E2 | <1-7> | <Gold / Silver / Bronze / Fools gold / n/a> | <yes / no> |

A claim's tier is its weakest evidence row, never its strongest. A metric crossing inside a claim (visibility → sales) is named and graded, per `../glossary.md`.

## Survivorship

<Required wherever the finding rests on published cases; otherwise one line: "Not case-based — survivorship does not apply.">

| | |
|---|---|
| Candidates screened | <n> |
| Cleared the evidence bar | <n> |
| Screen window | <YYYY-MM-DD to YYYY-MM-DD> |
| Channels searched | <channel, channel> |

Published cases are winners. A cleared count near zero is a result about the category, not a gap in the search — and it is reported as one.

## Unknowns

| Question | Channels checked | Date | Why it is not answerable from the channels used |
|---|---|---|---|
| <question> | <channel, channel> | <YYYY-MM-DD> | <one line> |

## Caveats

- <Which claims are load-bearing and rest on a single source.>
- <Any claim below tier 3, named.>
- <Metric crossings relied on, and their grade.>
- <Conflicts left unreconciled.>
- The oldest pull cited is <YYYY-MM-DD>; pulls older than one quarter at citation are re-checked and the re-check dated (`../plan.md` staleness rule).
- This file carries evidence, not a verdict.

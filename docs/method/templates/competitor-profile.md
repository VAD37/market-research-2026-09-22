# Template — `docs/competitors/<company>.md`

**Budget: 80 lines** (`../plan.md`). Every profile answers the same questions in the same order, per `docs/CLAUDE.md`. Section order below is binding.

Rules: every number carries its source label and its `raw/` path. Conflicting figures sit side by side, attributed, never averaged. No number enters without a `raw/` file. A field with nothing behind it reads `unknown — checked <channel> <date>`. A price not on a public page is `not disclosed — checked <channel> <date>`, never estimated. Every public claim of a result is graded per `../glossary.md`; ungraded claims do not appear. Negatives are sourced like any other claim — an absence found by checking is a negative, an absence assumed is not. No ranking against other companies here — cross-company reads are `findings/`. Profiles older than one quarter are stale (`scope.md`).

Filename: the company's own short name, slugified, lowercase — `<company>.md`. One file per company. The row in `INDEX.md` is written at the same time, per `index-row.md`.

---

<!-- Copy from here down. Delete these guidance comments. -->

# <Company>

| | |
|---|---|
| Profile date | <YYYY-MM-DD> |
| Oldest pull depended on | <YYYY-MM-DD> — `raw/<file>.md` |
| Lane | <A-F> |
| Sub-market | <organic recommendation / paid placement / agentic commerce> |
| Status | <operating | acquired | shut down | unknown — checked <channel> <date>> |

## Sells what, to whom

| Product | What it does | Buyer named by the vendor | Source | Raw |
|---|---|---|---|---|
| <name> | <12 words max> | <role or segment, vendor's own words> | <label> | `raw/<file>.md` |

<!-- The buyer column is the vendor's claim, not a demand finding. Demand is read in customers/. -->

## Model and pricing

| Model | Tier or SKU | Disclosed price | Unit | Contract shape | Source | Raw |
|---|---|---|---|---|---|---|
| <subscription / usage / retainer / rev-share> | <name> | <figure, or "not disclosed"> | <per month / per seat / per domain> | <self-serve / sales-led> | <label> | `raw/<file>.md` |

## Scale

| Measure | Figure | Layer | As of | Source | Raw |
|---|---|---|---|---|---|
| Revenue or ARR | <figure> | <group / product / segment> | <YYYY-MM> | <label> | `raw/<file>.md` |
| Headcount | <figure> | <total / engineering> | <YYYY-MM> | <label> | `raw/<file>.md` |
| Customers | <figure> | <paying / logos / free> | <YYYY-MM> | <label> | `raw/<file>.md` |
| Funding | <figure, round> | <cumulative / latest> | <YYYY-MM> | <label> | `raw/<file>.md` |

## Trajectory — a number and a direction

| Measure | From | To | Window | Direction | Source | Raw |
|---|---|---|---|---|---|---|
| <measure> | <figure> | <figure> | <YYYY-MM to YYYY-MM> | <up / flat / down> | <label> | `raw/<file>.md` |

## Per-engine coverage

One row per priority-1 engine, then priority 2. Absence is recorded, not omitted.

| Engine | Covered | Surface | Metric offered | Method disclosed | Source | Raw |
|---|---|---|---|---|---|---|
| <engine> | <yes / no / unknown — checked <channel> <date>> | <consumer chat / API / search-integrated> | <mention / citation / recommendation / traffic / sales> | <yes / no> | <label> | `raw/<file>.md` |

## Proof claims — graded against the evidence bar

| Claim, as published | Metric | Grade | Which of the seven bar items are missing | Source | Raw |
|---|---|---|---|---|---|
| <quoted or 12-word précis> | <visibility / traffic / sales> | <Gold / Silver / Bronze / Fools gold> | <list, or "none"> | <label> | `raw/<file>.md` |

<!-- No claim meeting the bar: replace the table with one line —
     `No claim clears the bar — <n> claims screened, 0 cleared, as of <YYYY-MM-DD>.` -->

## Positioning

| Against | How it positions itself | Vendor's own words | Raw |
|---|---|---|---|
| <category or type of rival> | <12 words max> | "<quote>" | `raw/<file>.md` |

## Negatives

| Negative | Evidence | Source | Raw |
|---|---|---|---|
| <what is weak, contested, or missing> | <what shows it> | <label> | `raw/<file>.md` |

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| <question> | <channel, channel> | <YYYY-MM-DD> |

## Caveats

- <Which figures are vendor-reported and unverifiable by a third party.>
- <Any conflicting figures above, and that they are not reconciled.>
- <Layer mismatches: group revenue standing in for product revenue, logos standing in for paying customers.>
- Category turnover is fast; this profile is stale one quarter after <profile date>.

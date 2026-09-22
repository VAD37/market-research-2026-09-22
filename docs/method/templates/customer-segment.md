# Template — `docs/customers/<vertical>.md`

**Budget: 100 lines** for the produced file (`../plan.md`). One file per vertical. Section order below is binding.

Rules: one row per sub-market × buyer-size cell — nine cells, all present, none dropped for being empty. Every signal comes from the catalogue in `../demand-signals.md`, with its `raw/` path and tier. Each cell reads exactly one word: **spend**, **attention**, or **none**. Attention never stands in for spend. Nothing is inferred from a vendor's target-customer page — that is a sell-side claim and belongs in `competitors/`. Willingness to pay is a disclosed price actually paid, or `unknown`; it is never inferred from a list price.

---

<!-- Copy from here down. Delete these guidance comments. -->

# <Vertical>

| | |
|---|---|
| File date | <YYYY-MM-DD> |
| Oldest pull depended on | <YYYY-MM-DD> — `raw/<file>.md` |
| Cells | 3 sub-markets × 3 buyer sizes = 9 |
| Cells with a spend signal | <n of 9> |
| Signals in the catalogue checked | <n of n> |

## Segment definition

| | |
|---|---|
| What counts as this vertical | <boundary, one line> |
| Excluded and why | <adjacent thing, where it is handled instead> |
| SMB, as the sources define it | "<quoted definition>" — `raw/<file>.md` |
| Mid-market, as the sources define it | "<quoted definition>" — `raw/<file>.md` |
| Enterprise, as the sources define it | "<quoted definition>" — `raw/<file>.md` |

Where sources disagree on a size band, both definitions sit here, attributed, never merged.

## Cell reads

| Sub-market | Buyer size | Read | Signals behind it | Strongest signal tier | Spend evidence present |
|---|---|---|---|---|---|
| Organic recommendation | SMB | <spend / attention / none> | <n> | <1-7> | <yes / no> |
| Organic recommendation | Mid-market | | | | |
| Organic recommendation | Enterprise | | | | |
| Paid placement | SMB | | | | |
| Paid placement | Mid-market | | | | |
| Paid placement | Enterprise | | | | |
| Agentic commerce | SMB | | | | |
| Agentic commerce | Mid-market | | | | |
| Agentic commerce | Enterprise | | | | |

`none` means checked and nothing found, not unchecked. An unchecked cell is not filled in.

## Signals

One row per signal per cell where the signal yielded anything. Signal names are the catalogue's, unaltered.

| Cell | Signal | Observation | Proxies | Label | Tier | Raw |
|---|---|---|---|---|---|---|
| <sub-market> / <size> | <catalogue signal name> | <12 words max, figure verbatim> | <spend / attention> | <label> | <1-7> | `raw/<file>.md` |

Attention-class and spend-class signals are never summed into one score.

## Cells with no signal — channels checked

| Cell | Signals checked | Channels checked | Date | Result |
|---|---|---|---|---|
| <sub-market> / <size> | <n of n> | <channel, channel> | <YYYY-MM-DD> | none found |

## Willingness to pay

| Cell | Price actually paid | What it bought | Who disclosed it | Label | Raw |
|---|---|---|---|---|---|
| <sub-market> / <size> | <figure, or `unknown — checked <channel> <date>`> | <scope> | <buyer / vendor / filing> | <label> | `raw/<file>.md` |

A vendor list price is not a willingness-to-pay observation; it belongs in that vendor's profile.

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| <question> | <channel, channel> | <YYYY-MM-DD> |

## Caveats

- Every read here rests on internet-only proxies. No interviews, no outreach (`scope.md` R2). No signal observes a budget directly.
- Willingness to pay is a disclosed price paid or `unknown`; nothing here is inferred from a list price.
- Signal biases carry through: <name the biases of the signals that drove the reads, per `../demand-signals.md`>.
- Publication bias runs one way — quiet spending leaves no public trace, so `none` reads are weaker evidence than `spend` reads.
- <Any cell whose read rests on a single signal, or on a signal below tier 4.>

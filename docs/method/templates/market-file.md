# Template — `docs/markets/<sub-market>.md`

**Budget: 120 lines** for the produced file (`../plan.md`). One file per sub-market. Section order below is binding.

Rules: sizing is **bottom-up** per `../plan.md` Pass 6 — vendor count × disclosed price × disclosed customer count, each input labelled and traced to `raw/`. A top-down total is recorded with its author and base, never as the size. A forecast sits beside the size, labelled forecast, never as the size. Growth carries its base period. Conflicting figures side by side, attributed, never averaged. Individual company detail beyond what sizes the market belongs in `competitors/`. The four structural checks are each answered or marked `unknown — checked <channel> <date>`.

---

<!-- Copy from here down. Delete these guidance comments. -->

# <Sub-market>

| | |
|---|---|
| File date | <YYYY-MM-DD> |
| Oldest pull depended on | <YYYY-MM-DD> — `raw/<file>.md` |
| Lane | <A-F> |
| Engines covered | <priority-1 engines, then any priority-2 covered> |
| Geography | <global / US / EU, as the sources bound it> |

## Definition and boundary

| | |
|---|---|
| Definition | <one sentence, per `../glossary.md`> |
| Aliases in sources | <GEO / AEO / LLMO / AI ads / agentic commerce, as used> |
| In | <what counts> |
| Out | <what is adjacent and excluded, and where it is handled instead> |
| Metric the market is denominated in | <visibility / traffic / sales / spend — never mixed> |

## Sizing — bottom-up

| Input | Figure | As of | Label | Raw |
|---|---|---|---|---|
| Vendors counted | <n> | <YYYY-MM> | <label> | `raw/<file>.md` |
| Disclosed price, per vendor | <range> | <YYYY-MM> | vendor-reported | `raw/<file>.md` |
| Disclosed customer count, per vendor | <range> | <YYYY-MM> | vendor-reported | `raw/<file>.md` |
| Coverage of the count | <how many of the n disclose price / customers> | <YYYY-MM> | — | — |

**Build.** <How the inputs combine, one line. Every multiplied figure named above.>

| Result | Figure | Method | Coverage | Confidence limit |
|---|---|---|---|---|
| Bottom-up size | <figure> | bottom-up, disclosed inputs | <n of n vendors> | <what the build cannot see> |

**Proxy.** <One proxy per `../plan.md` Pass 6 — share of search or SEO budget, analyst-derived — with its author, base and `raw/` path. Labelled proxy, kept separate from the build.>

## Forecasts — side by side, never as the size

| Author | Forecast figure | Target year | Base and method | Label | Raw |
|---|---|---|---|---|---|
| <author> | <figure> | <YYYY> | <stated base, or "no base stated"> | analyst-derived | `raw/<file>.md` |

A forecast presented by its author as a measurement downgrades that author (`../trust-rubric.md`); note it in the row.

## Growth

| Measure | From | To | Base period | Label | Raw |
|---|---|---|---|---|---|
| <measure> | <figure> | <figure> | <YYYY-MM to YYYY-MM> | <label> | `raw/<file>.md` |

No growth figure without a base period. A percentage with no base is discarded on sight.

## Value chain — and where margin sits

| Stage | Who does it | What is charged | Margin evidence | Label | Raw |
|---|---|---|---|---|---|
| <stage> | <type of party, not a company profile> | <price or take rate> | <what shows it, or unknown — checked> | <label> | `raw/<file>.md` |

## Per-engine inventory and cells — priority-1 engines × this sub-market

Every cell is a figure or `unknown — checked <channel> <date>`. Absent evidence is recorded as absent.

| Engine | Surface | Does the sub-market exist here | Unit sold or measured | Price or rate | As of | Label | Raw |
|---|---|---|---|---|---|---|---|
| <engine> | <consumer chat / API / search-integrated> | <yes / no / unknown — checked <channel> <date>> | <unit> | <figure> | <YYYY-MM> | <label> | `raw/<file>.md` |

## Structural checks

| Check | Answer | As of | Label | Raw |
|---|---|---|---|---|
| Substitute — what the brand does instead; is "do nothing" the real competitor | <answer, 20 words max> | <YYYY-MM> | <label> | `raw/<file>.md` |
| Platform risk — which engine ships native tooling making third-party vendors redundant | <answer> | <YYYY-MM> | <label> | `raw/<file>.md` |
| Incumbent bundling — which SEO or analytics incumbent added this as a feature, at what price delta | <answer> | <YYYY-MM> | <label> | `raw/<file>.md` |
| Regulatory — ad-disclosure rules inside AI answers in force as of the pull date | <answer, naming the instrument> | <YYYY-MM> | filed | `raw/<file>.md` |

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| <question> | <channel, channel> | <YYYY-MM-DD> |

## Caveats

- <Coverage of the bottom-up build: how much of the market the disclosed inputs can see.>
- <Which inputs are vendor-reported and unverifiable.>
- <Any conflicting figures above, unreconciled by design.>
- <Whether any size figure here is a forecast in the source's own framing.>
- The category is roughly two years old as of 2026-09; every figure is a point reading, and the staleness rule in `../plan.md` applies to each pull cited.

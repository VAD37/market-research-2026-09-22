# Template — `docs/competitors/INDEX.md` row

One line per company, nothing else. `INDEX.md` is the entry point to `competitors/`, not a ranking — cross-company reads are `findings/`.

Rules: a row exists only where a profile exists, written in the same pass. Every cell is 12 words at most, and a cell with nothing behind it reads `unknown` (the profile carries the `— checked <channel> <date>` detail). Numbers in a row are copied from the profile, never recomputed here, and the profile is the only place they carry their source label and `raw/` path. Rows sort alphabetically by company.

## Columns

| # | Column | Content |
|---|---|---|
| 1 | Company | Link to the profile: `[<Company>](<company>.md)` |
| 2 | Sub-market | organic recommendation / paid placement / agentic commerce |
| 3 | Lane | A–F |
| 4 | Sells | What it sells, 12 words max |
| 5 | Buyer | Role or segment, the vendor's own words |
| 6 | Model | subscription / usage / retainer / rev-share |
| 7 | Entry price | Lowest disclosed price and its unit, or `not disclosed` |
| 8 | Scale | One figure with its layer — `<figure> <measure>, <layer>` |
| 9 | Best proof grade | Gold / Silver / Bronze / Fools gold / none |
| 10 | P1 engines covered | `<n> of <n>` |
| 11 | Profile date | YYYY-MM-DD |
| 12 | Oldest pull | YYYY-MM-DD |

Columns 9 and 12 are why the index is readable without opening a profile: grade says what the vendor can prove, oldest pull says whether the row is stale. A profile older than one quarter is stale (`scope.md`); the row is not deleted, and staleness is visible from column 11.

---

<!-- Copy the header and separator once, at the top of INDEX.md. Copy the row per company. -->

| Company | Sub-market | Lane | Sells | Buyer | Model | Entry price | Scale | Best proof grade | P1 engines covered | Profile date | Oldest pull |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [<Company>](<company>.md) | <sub-market> | <A-F> | <12 words max> | <role or segment> | <model> | <figure + unit \| not disclosed> | <figure, measure, layer> | <grade \| none> | <n of n> | <YYYY-MM-DD> | <YYYY-MM-DD> |

`INDEX.md` carries one line above the table — `Index of competitor profiles. Rows are copied from the profiles; the profile is the source.` — and no other prose, no totals row, no caveats section. Caveats live in the profiles.

# Templates

Set 2026-09-22. One template per compiled file kind. Section order and line budget in a template are binding: they come from `../plan.md` "Line budgets" and from `docs/CLAUDE.md`.

| Folder | Template | Budget |
|---|---|---|
| `docs/raw/` | `raw-pull.md` | none — exempt from compression |
| `docs/competitors/<company>.md` | `competitor-profile.md` | 80 lines |
| `docs/competitors/INDEX.md` | `index-row.md` | one line per company |
| `docs/markets/<sub-market>.md` | `market-file.md` | 120 lines |
| `docs/customers/<vertical>.md` | `customer-segment.md` | 100 lines |
| `docs/findings/<finding>.md` | `finding.md` | 100 lines |

Rules:

- The first file into a folder sets that folder's format against its template. Every later file in that folder matches it — same sections, same order, same names.
- Copy the skeleton below the `---` in a template, delete the `<!-- -->` guidance lines, fill every bracket. A bracket with nothing behind it becomes `unknown — checked <channel> <date>`, never a guess or a deletion.
- Every compiled template carries the same four mandatory blocks: source label on every number, the `oldest pull depended on` line, an unknowns table, and a caveats section. None is optional, none is empty.
- A template changes only in `../plan.md`-sanctioned ways; when it changes, the change is dated here and existing files are not retrofitted silently.
- Terms used in these templates are defined in `../glossary.md`. Tiers are in `../trust-rubric.md`.

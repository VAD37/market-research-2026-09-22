# STATE — scheduler state

Created 2026-09-22. The only interface between sessions and between agents. Updated by the main thread after every spawn, landing, and commit. Agents append only under "Landed — pending verify".

## Current pass

Pass 0 — Method completion. Gate: open (scope.md, trust-rubric.md exist).

## Live agents

| id | model | task | deliverable | spawned |
|---|---|---|---|---|
| P0-b | Opus | Pre-registered hypotheses and demand-signal catalogue with empty segment matrix | `docs/method/hypotheses.md`, `docs/method/demand-signals.md` | 2026-09-22 |
| P0-c | Opus | Pass 10 panel protocol | `docs/method/panel-protocol.md` | 2026-09-22 |

## Queue

Front first.

| id | pass | model | task | deliverable |
|---|---|---|---|---|
| P1-a | 1 | Opus | Channels, shortlist, query book | `docs/sources/channels.md`, `shortlist.md`, `query-book.md` |
| P1-b | 1 | Opus | Red-team query-book.md | `docs/sources/query-book-redteam.md` |

## Landed

| task | deliverable | verified | commit |
|---|---|---|---|
| P0-a glossary and templates | `docs/method/glossary.md`, `docs/method/templates/` (7 files) | 2026-09-22 | 5d2950d |

## Landed — pending verify

Agents append one block here on finish: deliverable path, pulls made (count), unknowns recorded (count), blockers.

## Pass 10 sampling log

| sample date | prompt-set version | engines | raw file |
|---|---|---|---|

## Decisions taken

| date | choice | reason |
|---|---|---|
| 2026-09-22 | Pass 0 split into three tasks (P0-a, P0-b, P0-c) rather than one agent | `panel-protocol.md` gates Pass 10, which needs elapsed calendar time; splitting lets it land sooner. P0-a first because glossary metric definitions feed the other two |
| 2026-09-22 | Session works in worktree `worktree-orchestrator`, master fast-forwarded after every commit | Background-session harness rejects edits in the shared checkout; root `CLAUDE.md` wants master only. Fast-forward keeps master current |

## Unknowns

| question | channels checked | date |
|---|---|---|

## Done conditions

| condition | bar | status |
|---|---|---|
| Load-bearing claims in `findings/` at tier 3 or better | 80 percent or more | not started |
| Priority-1 engine × sub-market cells | Every cell a number or `unknown — checked` | not started |
| Segment matrix | Every cell spend, attention, or none, with signals | not started |
| Success stories | One Silver per vertical, or documented absence with screened count | not started |
| Hypotheses | Every H confirmed, killed, or unresolved with channel checked | not started |
| Pass 10 | Three pre-registered predictions checked against the panel | not started |

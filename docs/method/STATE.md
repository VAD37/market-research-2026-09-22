# STATE — scheduler state

Created 2026-09-22. The only interface between sessions and between agents. Updated by the main thread after every spawn, landing, and commit. Agents append only under "Landed — pending verify".

## Current pass

Pass 1 — Sources. Gate: open (Pass 0 landed 2026-09-22). Pass 10 sampling runs in parallel from 2026-09-22 (day 0).

## Live agents

| id | model | task | deliverable | spawned |
|---|---|---|---|---|
| P1-a | Opus | Channels, shortlist, query book | `docs/sources/channels.md`, `shortlist.md`, `query-book.md` | 2026-09-22 |
| P10-d0-claude | Sonnet | Panel sample day 0, Claude, prompt set v1 | `docs/raw/e-claude-panel-2026-09-22.md` | 2026-09-22 |

## Queue

Front first.

| id | pass | model | task | deliverable |
|---|---|---|---|---|
| P1-b | 1 | Opus | Red-team query-book.md | `docs/sources/query-book-redteam.md` |
| P10-d0-gemini | 10 | Sonnet | Panel sample day 0, Gemini | `docs/raw/e-gemini-panel-2026-09-22.md` |
| P10-d0-google-aimode | 10 | Sonnet | Panel sample day 0, Google AI Mode + AI Overviews | `docs/raw/e-google-aimode-panel-2026-09-22.md` |
| P10-d0-perplexity | 10 | Sonnet | Panel sample day 0, Perplexity | `docs/raw/e-perplexity-panel-2026-09-22.md` |
| P10-d0-copilot | 10 | Sonnet | Panel sample day 0, Copilot | `docs/raw/e-copilot-panel-2026-09-22.md` |
| P10-d0-rufus-p3 | 10 | Sonnet | Panel sample day 0, Amazon Rufus + P3 existence checks | `docs/raw/e-rufus-panel-2026-09-22.md`, `docs/raw/e-p3-engines-existence-2026-09-22.md` |
| P10-d0-chatgpt-retry | 10 | Sonnet | Retry ChatGPT day 0 — blocked until Chrome extension holds site permission for chatgpt.com (user action) | `docs/raw/e-chatgpt-panel-<date>.md` |

## Landed

| task | deliverable | verified | commit |
|---|---|---|---|
| P0-a glossary and templates | `docs/method/glossary.md`, `docs/method/templates/` (7 files) | 2026-09-22 | 5d2950d |
| P0-b hypotheses and demand signals | `docs/method/hypotheses.md`, `docs/method/demand-signals.md` | 2026-09-22 | 7cfc7b9 |
| P0-c panel protocol | `docs/method/panel-protocol.md` | 2026-09-22 | f5a06cd |
| **Pass 0 done** | all five Pass 0 deliverables | 2026-09-22 | f5a06cd |
| P10-d0-chatgpt | `docs/raw/e-chatgpt-panel-2026-09-22.md` — surface blocked, 0 of 160 runs | 2026-09-22 | 58e469b |

## Landed — pending verify

Agents append one block here on finish: deliverable path, pulls made (count), unknowns recorded (count), blockers.

- task: P10-d0-chatgpt | deliverable: `docs/raw/e-chatgpt-panel-2026-09-22.md` | runs completed / planned: 0 / 160 (32 prompts x n=5) | prompts with achieved_n < 5: 32 (all) | unknowns recorded: 6 (model_version_shown, region_observed, login_state, search_toggle, arm-toggle state, screenshot_ref) | surface status: surface blocked — Chrome extension site permission not granted for chatgpt.com (navigate to https://chatgpt.com/ succeeds; every subsequent read/interact call — get_page_text, screenshot — returns "Permission denied for this action on this domain"; tab reverts to chrome://newtab/ between calls) | blockers: extension needs chatgpt.com site permission granted before this task can be re-run.

## Pass 10 sampling log

| sample date | prompt-set version | engines | raw file |
|---|---|---|---|
| 2026-09-22 (day 0) | v1 | ChatGPT — blocked, 0 runs | `docs/raw/e-chatgpt-panel-2026-09-22.md` |

## Decisions taken

| date | choice | reason |
|---|---|---|
| 2026-09-22 | Pass 0 split into three tasks (P0-a, P0-b, P0-c) rather than one agent | `panel-protocol.md` gates Pass 10, which needs elapsed calendar time; splitting lets it land sooner. P0-a first because glossary metric definitions feed the other two |
| 2026-09-22 | Pass 10 sampling split one agent per engine per sample date, run one at a time | 32 prompts × 5 runs per engine is too large for one agent and the browser extension is a single shared resource; per-engine files match the protocol's one-file-per-engine-per-date rule |
| 2026-09-22 | Panel raw files use lane `e` with `pass: P10` header | `templates/raw-pull.md` fixes lane slot to a–f; noted in panel-protocol.md |
| 2026-09-22 | Session works in worktree `worktree-orchestrator`, master fast-forwarded after every commit | Background-session harness rejects edits in the shared checkout; root `CLAUDE.md` wants master only. Fast-forward keeps master current |

## Unknowns

| question | channels checked | date |
|---|---|---|
| ChatGPT consumer surface — extension denied on chatgpt.com ("Permission denied for this action on this domain"), tab reverts to newtab; site permission not granted | fetch (403), Chrome extension ×3 | 2026-09-22 |

## Done conditions

| condition | bar | status |
|---|---|---|
| Load-bearing claims in `findings/` at tier 3 or better | 80 percent or more | not started |
| Priority-1 engine × sub-market cells | Every cell a number or `unknown — checked` | not started |
| Segment matrix | Every cell spend, attention, or none, with signals | not started |
| Success stories | One Silver per vertical, or documented absence with screened count | not started |
| Hypotheses | Every H confirmed, killed, or unresolved with channel checked | not started |
| Pass 10 | Three pre-registered predictions checked against the panel | not started |

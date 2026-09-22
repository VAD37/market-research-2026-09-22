# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A research repo, not a codebase. There is no build, no test suite, and no package manager. Every deliverable is markdown produced by a research pass. If a command is ever needed here it will be a one-off script under `docs/method/`, not an application.

**Subject: set 2026-09-22.** Demand for brand visibility and product recommendation inside AI assistants. Standing brief in `docs/method/scope.md`, charter in `MegaPlan.md`, pass sequence in `docs/method/plan.md`. Read all three before any research pass.

**Research only.** No execution planning in this repo: no dates, budgets, kill criteria, MVPs, build specs, or playbooks. A successful product is a hypothetical that guides which questions matter. Set by the user 2026-09-22; see `MegaPlan.md` non-goals.

Predecessor: `D:\researchs\market-research\` — three research passes and three MVPs on ads-injection, an agent dashboard, and AI attack/defense, plus an investment review. That repo is intact and read-only source material. Nothing in it is inherited as scope. Cite it as a source like any other, from `docs/raw/`, never from memory.

Sibling repos under `D:\researchs\` (`startup/`, `hobby/`) run the same conventions. Read `D:\researchs\startup\CLAUDE.md` if a convention below needs a worked example.

## Hierarchy

Research lives under `docs/`. The repo root holds this file, `MegaPlan.md`, and any generated tracker (a CSV plus its rendered markdown) once one exists. `projects/` is dormant.

```
CLAUDE.md          this file — global rules, and the hierarchy
MegaPlan.md        the research charter: what the programme is, and what it is not
docs/
  CLAUDE.md        what each subfolder below is for, and what may not go in it
  method/          how the research runs: scope, plan, rubric, templates, conventions
  sources/         where data comes from — channels, and who is worth profiling
  raw/             raw pulls, source-attributed, uncompressed
  markets/         per-market sizing and structure
  competitors/     one profile per company, plus INDEX.md
  customers/       demand side — segments, signal matrix per cell
  findings/        compiled tables, rankings, cross-market reads
projects/
  ORCHESTRATION.md agent spawning rules: cap, models, split rule — still in force
  CLAUDE.md, MVP-MANDATE.md   execution layer, dormant. No project opens here
```

Three layers, and work flows one way through them:

**sources → raw → compiled.** `sources/` decides what to pull. `raw/` holds the pull verbatim. `markets/`, `competitors/`, `customers/` and `findings/` are compiled from `raw/` and never from memory. `method/` governs all of it.

`docs/CLAUDE.md` is the authority on the research subfolders. Read it before writing any file into `docs/`.

## Rules

Evidence:

- Never compile from memory. Every compiled claim traces to a file in `docs/raw/`.
- Every number carries a source, labeled by kind: vendor-reported, analyst-derived, filed, company-stated, or measured-by-us.
- Absolute dates. "As of 2026-09", never "recently".
- `unknown — checked <channel> 2026-09` beats a guess. A guessed number survives into the compiled tables and poisons them.
- Conflicting figures sit side by side, attributed. Never averaged.
- Every compiled doc carries a caveats section.
- The verdict is the user's call. Produce the evidence, not the go/no-go, unless asked.
- Internet only. No interviews, no outreach. The Chrome browser extension is permitted for pulls and for measured-by-us sampling.

Compression — applies to files, not only to chat:

- Prose in `docs/` is compressed before a file is done. Cut hedging, filler and restatement; keep the substance.
- Compression kills prose, never evidence. Numbers, dates, source labels, quoted text and URLs survive verbatim.
- State each fact once per file. No section restating a table row in prose.
- Table cell: 12 words. A cell that wants a paragraph means the paragraph belongs in `docs/raw/` and the cell carries the number.
- `docs/raw/` is exempt. Raw stays raw, in the source's own words.
- Generated files are exempt and never hand-edited. Fix the input, re-run the generator.

## Git

A git repo, and it is a restore point, not a workflow — master only, no branch flow, no worktrees, no PRs. `.gitkeep` files hold the empty category folders. **Agents never run git. The main thread commits.**

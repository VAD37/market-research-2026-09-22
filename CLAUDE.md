# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A research repo, not a codebase. There is no build, no test suite, and no package manager. Every deliverable is markdown produced by a research pass. If a command is ever needed here it will be a one-off script under `docs/method/`, not an application.

**Subject: not yet set.** Opened 2026-09-22 as a clean restart. `docs/` holds the category skeleton and nothing else; `projects/` holds the execution-layer rules and no projects. Before the first research pass, ask the user to name the market, the geography, and the decision the research has to serve. Record that answer in `docs/method/scope.md` and treat it as the standing brief.

Predecessor: `D:\researchs\market-research\` — three research passes and three MVPs on ads-injection, an agent dashboard, and AI attack/defense, plus an investment review. That repo is intact and read-only source material. Nothing in it is inherited as scope. Cite it as a source like any other, from `docs/raw/`, never from memory.

Sibling repos under `D:\researchs\` (`startup/`, `hobby/`) run the same conventions. Read `D:\researchs\startup\CLAUDE.md` if a convention below needs a worked example.

## Hierarchy

Research lives under `docs/`. Execution lives under `projects/`. The repo root holds this file, `MegaPlan.md`, and any generated tracker (a CSV plus its rendered markdown) once one exists.

```
CLAUDE.md          this file — global rules, and the hierarchy
MegaPlan.md        the execution guideline: how a project runs from idea to MVP
docs/
  CLAUDE.md        what each subfolder below is for, and what may not go in it
  method/          how the research runs: scope, pipeline, templates, conventions
  sources/         where data comes from — channels, and who is worth profiling
  raw/             raw pulls, source-attributed, uncompressed
  markets/         per-market sizing and structure
  competitors/     one profile per company, plus INDEX.md
  customers/       demand side — segments, interviews, personas
  findings/        compiled tables, rankings, cross-market reads
projects/
  CLAUDE.md        execution-layer hierarchy and pipeline
  ORCHESTRATION.md who gets spawned, on what model, under what cap
  MVP-MANDATE.md   what must exist before a project is called done
  <project>/       one folder per project, self-contained, its own git repo
```

Three layers, and work flows one way through them:

**sources → raw → compiled.** `sources/` decides what to pull. `raw/` holds the pull verbatim. `markets/`, `competitors/`, `customers/` and `findings/` are compiled from `raw/` and never from memory. `method/` governs all of it.

Then, and only then, `projects/` builds from what `docs/` established.

`docs/CLAUDE.md` is the authority on the research subfolders. Read it before writing any file into `docs/`. `projects/CLAUDE.md` is the authority on the execution layer.

## Rules

Evidence:

- Never compile from memory. Every compiled claim traces to a file in `docs/raw/`.
- Every number carries a source, labeled by kind: vendor-reported, analyst-derived, filed, company-stated, or measured-by-us.
- Absolute dates. "As of 2026-09", never "recently".
- `unknown — checked <channel> 2026-09` beats a guess. A guessed number survives into the compiled tables and poisons them.
- Conflicting figures sit side by side, attributed. Never averaged.
- Every compiled doc carries a caveats section.
- The verdict is the user's call. Produce the evidence, not the go/no-go, unless asked.

Compression — applies to files, not only to chat:

- Prose in `docs/` is compressed before a file is done. Cut hedging, filler and restatement; keep the substance.
- Compression kills prose, never evidence. Numbers, dates, source labels, quoted text and URLs survive verbatim.
- State each fact once per file. No section restating a table row in prose.
- Table cell: 12 words. A cell that wants a paragraph means the paragraph belongs in `docs/raw/` and the cell carries the number.
- `docs/raw/` is exempt. Raw stays raw, in the source's own words.
- Generated files are exempt and never hand-edited. Fix the input, re-run the generator.

## Git

A git repo, and it is a restore point, not a workflow — no branch flow, no PRs. `.gitkeep` files hold the empty category folders. Each project under `projects/` is its own git repository; this repo does not track project contents. **Agents never run git. The main thread commits.**

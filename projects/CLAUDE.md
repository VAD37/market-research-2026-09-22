# projects/CLAUDE.md

Execution layer. `../docs/` is research (evidence, no verdict). `projects/` is what gets built from it.

One folder per project in `../MegaPlan.md`. A project folder is self-contained: an agent working in it reads `../../CLAUDE.md` (global rules), this file, and its own `CLAUDE.md`, and needs nothing else from chat.

**No projects exist yet.** Opened 2026-09-22. The first project folder is created only after `../docs/method/scope.md` names the idea and `../docs/` holds a market read on it.

## Shared hierarchy — every project folder

```
CLAUDE.md          project brief, constraints, what "done" means for this project
STATE.md           running log. Append-only. Written BEFORE and AFTER every work chunk
docs/
  explore/         what exists, what was read, what the terrain is
  plan/            what to do, in order
  design/          solution design — architecture, interfaces, tradeoffs
  review/          review against market evidence in ../../docs/, and self-review
  execution/       per-step execution notes, one file per step
  outcome/         success-vision.md first, then what shipped, what failed, what it cost
raw/               verbatim pulls: command output, page text, API responses, logs
prototype/         code. Smallest thing that proves or kills the idea
site/              index.html — the sales page. Single file, no build step
```

## Pipeline — same for every project

explore → idea → review against market → technical solution → daydream → vibe-code small MVP.

Technical sub-loop inside the MVP step: explore, plan, solution design, review, loop execution, outcome review, end-to-end user test.

Do not skip the review-against-market step. An idea that contradicts `../../docs/findings/` or `../../docs/markets/` is not automatically wrong, but the contradiction goes in `docs/review/` named.

## Rules inherited from `../../CLAUDE.md`

- Never compile from memory. Compiled claims trace to a file in `raw/` or `../../docs/raw/`.
- Every number carries a source, labeled: vendor-reported, analyst-derived, filed, company-stated, or measured-by-us.
- Absolute dates. `unknown — checked <channel> 2026-09` beats a guess.
- Conflicting figures sit side by side, attributed. Never averaged.
- Prose compressed before a file is done. `raw/` exempt. Table cell: 12 words.
- Verdict is the user's call. Produce evidence and a working or failed prototype, not a go/no-go.

## Rules specific to this layer

- **STATE.md is the anti-work-loss mechanism.** Write the plan into it before doing the work, write the result into it after. An agent that dies mid-run must leave a successor enough to continue.
- Prototype code is throwaway-grade but must RUN. A prototype that was never executed is a design doc — file it as one.
- Measured beats argued. A claim about what an AI crawler does, what an agent costs, what a defense catches — go measure it and put the output in `raw/`.
- Test only against infrastructure you control, or public material published for study. No third-party targeting.
- Agents do not commit. The main thread commits.

## Git

**Each project is its own git repository**, rooted at `projects/<project>/`. The parent research repo does not track project contents; it gitignores them and keeps only `CLAUDE.md`, `MVP-MANDATE.md` and `ORCHESTRATION.md`. Per-project history exists so each project can be reviewed and its quality checked on its own.

The predecessor repo wired projects in as git submodules and that was a mistake to inherit — submodules made the parent repo's state depend on three moving children for no gain. Separate repos, no submodule link. If a shared view is wanted later, it is a list of clone URLs in a markdown file.

**Agents never run git.** The main thread commits, into whichever project repo the work landed in, after every agent lands.

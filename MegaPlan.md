# MegaPlan

Source of truth for planning large execution tasks — making a test prototype and piloting an idea.

Each project runs differently and depends on the context of its market and its technical requirement. The final outcome is unclear and depends heavily on the explore and daydreaming phases. That is expected; do not resolve it by guessing early.

## Ideas under execution

**None yet.** Opened 2026-09-22. Ideas arrive here only after `docs/method/scope.md` names them and `docs/` holds a read on each. One section per idea, and the section states the open questions the build has to answer — not a design.

## Shared guideline — every project

- One subagent per project at a time. Sonnet for exploration and pulls, Opus for planning and review. Full policy in `projects/ORCHESTRATION.md`.
- Cache and write every subagent report and status into the repo state immediately, to prevent loss of work.
- Orchestration steps, in order: explore → idea → review against market → detect possible technical solution → daydream → vibe-code a small MVP to see whether we can make something similar.
- Use git, worktrees, and whatever tools this machine has.
- Every project shares the same hierarchy and the same `docs/` rules for planning, execution and exploration. See `projects/CLAUDE.md`.

## Technical execution steps — inside the MVP phase

explore → plan → solution design → review → loop execution → outcome review → edge-to-edge user test, end to end.

## Ordering rule — set 2026-09-17, carried forward

A project's `docs/outcome/success-vision.md` is written **before** its sales page and **before** its review, and every downstream agent reads it. Without a stated picture of what winning looks like, agents optimize against a spec and an acceptance checklist and produce something locally correct and globally pointless.

The vision doc grounds every present-tense claim in the build and e2e docs, reads the research verdicts honestly, and is allowed — encouraged — to conclude that the honest win is much smaller than the original ambition. Its ranked gap between what the e2e proves today and the win condition becomes the fix wave's work list.

# Orchestration

Main-thread record of who was spawned, on what model, for what — and the rules that govern it. Per `../MegaPlan.md`: one agent per project at a time. The main thread spawns only. No planning, no review done here.

Rules carried forward from the predecessor repo, each dated to when the user set it. The run log stayed behind.

## Model policy — set by the user 2026-09-17

| Model | Used for |
|---|---|
| Sonnet | Web and network exploration, pulls, small clear execution tasks |
| Opus | Planning, solution design, code review, plan review |
| Fable | Sales pages, voice, success-vision docs |

## Wave plan

| Wave | Model | Phase | Per project |
|---|---|---|---|
| 1 | Sonnet | explore | Terrain + measured pulls into `raw/`, inventory files into `docs/explore/` |
| 2 | Opus | idea → review vs market → solution design → daydream | Reads wave 1 output, writes `docs/plan/`, `docs/design/`, `docs/review/` |
| 3 | Fable | success vision | `docs/outcome/success-vision.md`. Precedes the sales page and the review |
| 4 | Sonnet | vibe-code MVP | Builds `prototype/` from wave 2's design, runs it, logs to `docs/execution/` |
| 5 | Opus | outcome review + end-to-end test read | Reviews code and result, writes `docs/outcome/` |

Waves gate on each other per project. A project may run ahead of the others.

## Concurrency cap — MANDATE, set by the user 2026-09-17

**Never more than 3 agents running at once, machine-wide.** The main thread is the scheduler and does not count toward the 3. Subagents of a subagent count. The cap is a hard ceiling, not a target — 2 is fine, 4 is a violation.

Read this before every spawn decision.

Why: six concurrent agents contend on one browser, one Docker daemon, and one set of ports, and the main thread cannot hold an accurate picture of six moving trees. Three is what stays reviewable.

### Scheduler rules

1. Before spawning, count live agents. If the count is already 3, do not spawn — queue.
2. Spawn only on a completion notification, and only up to the free slots.
3. One agent per project at a time is the default. Two agents on one project are allowed only when their file sets are provably disjoint AND a slot is free — and each must be told in its prompt that the other is live and which paths it may not touch.
4. `infra/` counts as a project for scheduling. It is not free.
5. A stopped agent is not a failed agent. Record the stop in that project's `STATE.md` so the next agent does not read an orphaned "starting work" entry as a crash, and restore the working tree with `git checkout` if the stop left it half-mutated.
6. Re-queued work goes back at the FRONT of the queue, not the back. Do not let a task starve because new waves keep jumping it.

## Task sizing — set by the user 2026-09-17

A wave is not one agent per project by default. A stage too big for one agent gets **split into smaller scoped tasks, each with its own agent, spawned in sequence** as the prior one lands. Quality and efficiency beat agent count.

**Split rule:** one agent per task that has a single deliverable file (or one tight cluster), a single question, and a clear done condition. When a stage's brief lists five unrelated deliverables, that is five tasks, not one.

**Carry-forward rule:** each successor agent reads `STATE.md` plus the specific files its predecessor wrote, never a chat handoff. `STATE.md` is the only interface between agents.

Explore is the one stage that may run as a single broad agent per project — it is fan-out reading with one shared output shape. Every stage after it is split by deliverable.

## Real input before polish — rule set 2026-09-17

First task per project, ahead of any cosmetic fix: **put real data through the tool once.** Then the page leads with a real `n=1` number and the fixture demo is demoted to "how it works".

The predecessor repo shipped three MVPs that were all correct against their own fixtures and none of which had ever seen real input. Every e2e doc named this as its own top gap, independently. It is the default failure mode of this pipeline, not an accident of those three projects.

Corollary: **do not give a demo more polish than the reality has.** Layout fixes are fine. New interactive flourishes on synthetic data are not.

## Runs

Nothing spawned yet. First entry goes below, dated, with model and brief.

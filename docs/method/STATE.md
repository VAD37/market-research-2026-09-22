# STATE — scheduler state

Created 2026-09-22. The only interface between sessions and between agents. Updated by the main thread after every spawn, landing, and commit. Agents append only under "Landed — pending verify".

## Current pass

Pass 2 — Raw wave A, infra and platform primary. Gate: open (Pass 1 landed 2026-09-22, query book red-teamed and amended). Passes 3–5 blocked by: P2-c1 assistant-share table and the reweight. Pass 10 sampling runs in parallel from 2026-09-22 (day 0).

## Live agents

| id | model | task | deliverable | spawned |
|---|---|---|---|---|
| P2-reweight | Opus | Engine priority reweight from the share table, dated, appended to plan.md engine matrix | `docs/method/plan.md` (append only) | 2026-09-22 |
| P2-c2 | Sonnet | CDN and crawler telemetry | `docs/raw/a-*-crawler-*-2026-09-22.md` per pull | 2026-09-22 |
| P10-d0-claude | Sonnet | Panel sample day 0, Claude, prompt set v1 | `docs/raw/e-claude-panel-2026-09-22.md` | 2026-09-22 |

## Queue

Front first. Pass 2 clusters run in any order; Passes 3–5 wait for P2-c1 and the reweight. One P10 sampler at a time (shared browser). Cluster rows are in `docs/sources/shortlist.md`.

| id | pass | model | task | deliverable |
|---|---|---|---|---|
| P10-d0-gemini | 10 | Sonnet | Panel sample day 0, Gemini | `docs/raw/e-gemini-panel-2026-09-22.md` |
| P10-d0-google-aimode | 10 | Sonnet | Panel sample day 0, Google AI Mode + AI Overviews | `docs/raw/e-google-aimode-panel-2026-09-22.md` |
| P10-d0-perplexity | 10 | Sonnet | Panel sample day 0, Perplexity | `docs/raw/e-perplexity-panel-2026-09-22.md` |
| P10-d0-copilot | 10 | Sonnet | Panel sample day 0, Copilot | `docs/raw/e-copilot-panel-2026-09-22.md` |
| P10-d0-rufus-p3 | 10 | Sonnet | Panel sample day 0, Amazon Rufus + P3 existence checks | `docs/raw/e-rufus-panel-2026-09-22.md`, `docs/raw/e-p3-engines-existence-2026-09-22.md` |
| P10-d0-chatgpt-retry | 10 | Sonnet | Retry ChatGPT day 0 — blocked until Chrome extension holds site permission for chatgpt.com (user action) | `docs/raw/e-chatgpt-panel-<date>.md` |
| P2-c3 | 2 | Sonnet | OpenAI platform primary | `docs/raw/b-openai-*-2026-09-22.md` |
| P2-c4 | 2 | Sonnet | Google platform primary | `docs/raw/b-google-*` |
| P2-c5 | 2 | Sonnet | Anthropic and Perplexity platform primary | `docs/raw/a-anthropic-*`, `b-perplexity-*` |
| P2-c6 | 2 | Sonnet | Microsoft and Amazon platform primary | `docs/raw/b-microsoft-*`, `b-amazon-*` |
| P2-c7 | 2 | Sonnet | Agentic commerce protocols | `docs/raw/c-*-protocol-*` |
| P2-c8 | 2 | Sonnet | Retail and e-commerce analytics publishing free | `docs/raw/c-*-analytics-*` |
| P2-c9 | 2 | Sonnet | Regulators — ad disclosure inside AI answers | `docs/raw/b-*-regulator-*` |
| P2-c10 | 2 | Sonnet | EU enforcement and mandated ad repositories | `docs/raw/b-eu-*` |
| P2-c11 | 2 | Sonnet | Litigation dockets and exhibits | `docs/raw/b-court-*` |
| P3-c0 | 3 | Sonnet | Vendor roster build by discovery | `docs/raw/a-vendor-roster-2026-09-22.md` |
| P3-c1 | 3 | Sonnet | Roster positions 1–8 | `docs/raw/a-<vendor>-*` per vendor |
| P3-c2 | 3 | Sonnet | Roster positions 9–16 | as above |
| P3-c3 | 3 | Sonnet | Roster positions 17–24 | as above |
| P3-c4 | 3 | Sonnet | Incumbent bundling | `docs/raw/a-<incumbent>-*` |
| P3-c5 | 3 | Sonnet | Agencies and service providers | `docs/raw/f-<agency>-*` |
| P3-c6 | 3 | Sonnet | Sell-side of paid and agentic commerce | `docs/raw/b-*`, `c-*` |
| P4-c1 | 4 | Sonnet | Earnings calls and investor decks | `docs/raw/e-case-*` graded on intake, screened count |
| P4-c2 | 4 | Sonnet | Agency data posts carrying client numbers | as above |
| P4-c3 | 4 | Sonnet | Conference talks with slides | as above |
| P4-c4 | 4 | Sonnet | Vendor case studies | as above |
| P4-c5 | 4 | Sonnet | Practitioner write-ups | as above |
| P4-c6 | 4 | Sonnet | Trade press that links primary data | as above |
| P5-c1 | 5 | Sonnet | Corpus seeding in high-citation sources | `docs/raw/d-*` |
| P5-c2 | 5 | Sonnet | Review and listicle manufacture | `docs/raw/d-*` |
| P5-c3 | 5 | Sonnet | Comparison-page farming | `docs/raw/d-*` |
| P5-c4 | 5 | Sonnet | Content written to satisfy known citation preferences | `docs/raw/d-*` |
| P5-c5 | 5 | Sonnet | Structured data and llms.txt-style signalling | `docs/raw/d-*` |
| P5-c6 | 5 | Sonnet | Prompt injection embedded in indexed content | `docs/raw/d-*` |
| P5-c7 | 5 | Sonnet | Engine countermeasures | `docs/raw/d-*-countermeasure-*` |
| P8-c1 | 8 | Sonnet | Demand-signal sweep per cell | `docs/raw/f-signal-*` |
| P6, P7, P8, P9, P10-analysis, P11 | 6–11 | Opus | Compile passes — split by file when gates open | per plan.md |

## Landed

| task | deliverable | verified | commit |
|---|---|---|---|
| P0-a glossary and templates | `docs/method/glossary.md`, `docs/method/templates/` (7 files) | 2026-09-22 | 5d2950d |
| P0-b hypotheses and demand signals | `docs/method/hypotheses.md`, `docs/method/demand-signals.md` | 2026-09-22 | 7cfc7b9 |
| P0-c panel protocol | `docs/method/panel-protocol.md` | 2026-09-22 | f5a06cd |
| **Pass 0 done** | all five Pass 0 deliverables | 2026-09-22 | f5a06cd |
| P10-d0-chatgpt | `docs/raw/e-chatgpt-panel-2026-09-22.md` — surface blocked, 0 of 160 runs | 2026-09-22 | 58e469b |
| P1-a channels, shortlist, query book | `docs/sources/channels.md` (145), `shortlist.md` (78), `query-book.md` (118); 29 clusters | 2026-09-22 | 9aca6b4 |
| P1-b red-team | `docs/sources/query-book-redteam.md` (120); 13 blind spots, verdict amend all three | 2026-09-22 | 34994b8 |
| P1-c amendments applied | `channels.md` (157), `shortlist.md` (101), `query-book.md` (151); 22 of 22 applied, 32 clusters | 2026-09-22 | f78663a |
| **Pass 1 done** | channels, shortlist, query book, red-team | 2026-09-22 | f78663a |
| P2-c1 assistant share | 11 pulls `docs/raw/a-*-share-*-2026-09-22.md` + `a-assistant-share-table-2026-09-22.md`; 29 screened out; Rufus unknown | 2026-09-22 | 4d05c71 |

## Landed — pending verify

Agents append one block here on finish: deliverable path, pulls made (count), unknowns recorded (count), blockers.

**P1-b — red-team of the query book.** Deliverable `docs/sources/query-book-redteam.md`, 120 lines. Queries tested: 28 (26 web searches, 2 EDGAR full-text fetches, 1 archive fetch that failed). Blind spots found: 13, numbered B1–B13. Amendments proposed: `channels.md` 8 new rows (C60–C67); `query-book.md` 8 amendments (2 corrections — exclusion scope and `-"vs"` — plus 6 additions covering alias sets O/P/X, grid rows, buyer-size overlay, negative-result row, EDGAR and academic venue lists, date rule); `shortlist.md` 3 new clusters (P2-c10, P2-c11, P8-c1), 1 roster-rule amendment, 2 pull-list additions (P2-c5, P5-c7). No `docs/raw/` files written; no reviewed file edited. Blockers: `web.archive.org` refused to plain fetch (`Claude Code is unable to fetch from web.archive.org`) — the archival channel proposed as C61 needs the Chrome extension; the search surface is US-only by its own description, so the EU coverage gap is measured by the instrument that causes it.

**P1-c — red-team amendments applied.** Files edited, in place, no file created or removed: `docs/sources/channels.md` 145 → **157** lines (budget 160), `docs/sources/shortlist.md` 78 → **101** (budget 200), `docs/sources/query-book.md` 118 → **151** (budget 160). Amendments applied: **22 of 22** — channels 8 (C60–C67), query book 8 (exclusion scope and `-"vs"` deletion as corrections, sets O and P appended, new set X, five grid rows plus the Google merged-surface token, buyer-size overlay, negative-result and buyer-side and EU and courts and archive query rows, EDGAR and UK and academic venue appends, split date rule), shortlist 6 (P2-c10, P2-c11, P8-c1, roster-rule rewrite, P2-c5 archival addition, P5-c7 extended to priority-2 engines). Not applied: **0**; no "amendments not applied" section was needed in any of the three files. Additionally closed beyond §6: the §3 H11 vertical gap, by a per-vertical tagging rule on every Pass 4 cluster. Recorded `unknown — checked` rather than closed: **2** — H16 forecast sizing (routed to the Pass 6 task, which has no cluster and sits outside this file set's remit; recorded in both `shortlist.md` and `query-book.md` caveats) and S12's brand sample frame (`panel-protocol.md`'s, not a query). URLs verified today by fetch: **36 distinct** — 30 returned 200; 5 recorded `403→ext` (`courtlistener.com`, `dl.acm.org`, `gartner.com/en/newsroom`, `upwork.com`, `indeed.com`); `ted.europa.eu` 405 to plain GET, as already recorded at C20. Corrections carried into the files because the check disagreed with the red-team: C62 CourtListener expected 200, observed 403; C63 `dl.acm.org` 403 and `ieeexplore.ieee.org` 418 to a default user-agent, 200 to a browser one; C66 Gartner and Upwork 403. One substantive correction on read: `transparency.dsa.ec.europa.eu` is the statements-of-reasons database plus a Research API and publishes **no** ad records — DSA ad repositories are per-service under Art. 39, reached through each designated engine's own transparency page. C60's row and P2-c10's done-when both say so. Blockers: none that stopped the task. `web.archive.org` root returned 200 to curl but plain fetch still refuses it, so C61 and the P2-c5 addition are both marked Chrome-extension-only; the five `403→ext` channels are fetch-path results, not closed channels, and need the extension at pull time.

**P2-c1 — assistant-share table, clickstream and panel publishers.** Deliverables: `docs/raw/a-similarweb-share-gen-ai-stats-2026-09-22.md`, `a-similarweb-share-zero-click-marketing-2026-09-22.md`, `a-statcounter-share-ai-chatbot-market-share-2026-09-22.md`, `a-statcounter-share-referral-press-release-2026-09-22.md` (stale, flagged), `a-statcounter-methodology-2026-09-22.md`, `a-comscore-share-q1-2026-ai-intelligence-2026-09-22.md`, `a-comscore-share-march-2026-rankings-2026-09-22.md`, `a-comscore-share-jan-2026-mobile-desktop-2026-09-22.md`, `a-sparktoro-share-brand-mentions-downstream-2026-09-22.md`, `a-sparktoro-share-zero-click-2026-09-22.md`, `a-ppc-land-share-datos-q1-2026-2026-09-22.md`, `a-searchenginejournal-share-ai-visibility-2026-09-22.md`; summary `docs/raw/a-assistant-share-table-2026-09-22.md`. Pulls made: **12**. Screened-out: **29** (26 non-channel marketing/listicle domains rejected on sight; 2 Datos primary report pages checked but form-gated with no public figure, substituted by a PPC Land pointer to the same study; 1 Comscore whitepaper landing page, no new content). Unknowns recorded: **1** — Amazon Rufus, `unknown — checked Similarweb, Comscore, Datos/SparkToro, StatCounter 2026-09-22`, no channels.md clickstream/panel publisher reports a Rufus figure. Engines with at least one figure: ChatGPT, Claude, Google (Gemini and AI Mode specifically), Perplexity, Copilot, Meta AI (thin — one publisher, one date), Grok, DeepSeek. Blockers: none stopped the task. Notes for the reweight task (P2-reweight): publishers use at least three incompatible "share" definitions (category web-visit share, referral-click share, single-engine desktop-population penetration) — flagged in the summary file's caveats, not resolved here. `radar.cloudflare.com/ai-insights` and Cloudflare-sourced crawler figures encountered inside the Similarweb zero-click article were left to the P2-c2 crawler-telemetry agent per task instructions (flagged in-line in that raw file, not filed as this cluster's evidence). `docs/raw/e-claude-panel-2026-09-22.md` and other `a-*-crawler-*` files were not read or written.

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
| 2026-09-22 | Red-team amendments applied by a third Pass 1 agent (P1-c), not by the scheduler | Scheduler does no research; amendments change source coverage and need the same rules as the original pass |
| 2026-09-22 | Session works in worktree `worktree-orchestrator`, master fast-forwarded after every commit | Background-session harness rejects edits in the shared checkout; root `CLAUDE.md` wants master only. Fast-forward keeps master current |

## Unknowns

| question | channels checked | date |
|---|---|---|
| Amazon Rufus assistant share | Similarweb, Comscore, Datos/SparkToro, StatCounter | 2026-09-22 |
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

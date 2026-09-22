# Research plan — AI ads and AI product placement

Set 2026-09-22. The execution plan for the standing brief in `scope.md`. Passes run in order, gated. Nothing here is a finding; findings live in `docs/findings/`.

Read before executing: root `CLAUDE.md`, `docs/CLAUDE.md`, `scope.md`, `trust-rubric.md`.

## What the research must answer

One question, stated once:

> Which companies have moved marketing into AI assistant surfaces, what did it measurably do for them, and what would a brand have to change to follow?

Everything below serves that. A pass that does not narrow it gets cut.

## Scope resolution — user answers 2026-09-22

| # | Decision | Answer |
|---|---|---|
| D1 | Decision served | Market understanding first, then a transition playbook for a brand moving marketing into AI surfaces. Build option stays open downstream |
| D2 | Geography | Global product, US and EU primary demand. APAC is engineering only, not a market |
| D3 | Sub-market | Both organic recommendation and paid placement. Not one |
| D4 | Engines | All, with OpenAI and Anthropic primary by assumed user share |
| D5 | Vertical | Skincare is one anchor. Widen deliberately, do not stay single-vertical |
| D6 | Evidence target | Competitor success stories with real metrics. Proof that AI ads, AI recommendation, and gaming of it exist and work |

D6 adds a lane `scope.md` did not carry: deliberate manipulation of AI recommendation. Recorded as Lane D below.

## Six lanes

Lanes are research tracks. Sub-markets are what gets sized. Not the same axis.

| Lane | Track | Core question | Compiles into |
|---|---|---|---|
| A | Organic recommendation — GEO, AEO, LLMO | How does a brand get named in an answer | `markets/`, `competitors/` |
| B | Paid placement — AI ads | What inventory exists, what it costs, who buys | `markets/` |
| C | Agentic commerce | Who controls checkout inside the agent | `markets/` |
| D | Manipulation and gaming | How recommendation is steered, and whether it works | `findings/` |
| E | Measurement and proof | Who demonstrates causal lift rather than correlation | `findings/`, cross-cutting |
| F | Transition inputs | What a brand changes: org, content ops, stack, budget | `customers/`, playbook |

E and F are cross-cutting. Every pass in A through D feeds them.

## Evidence bar — what counts as a success story

D6 is the hardest ask in this plan. Most published cases fail this bar. The bar is set before pulling so it cannot be relaxed to fit what turns up.

A case qualifies only when it names all seven:

1. The brand, or a credibly specified anonymised profile
2. The engine or engines
3. The date window, absolute
4. The baseline before intervention
5. The intervention itself
6. The sample size, or the traffic volume
7. Who measured, and whether they were paid by the outcome

Grades:

| Grade | Standard | Handling |
|---|---|---|
| Gold | Holdout, geo-split, or switchback. Causal | Cite as proof |
| Silver | Pre and post, baseline plus an unaffected control metric | Cite as evidence, label correlational |
| Bronze | Visibility or mention-rate change only, no revenue link | Cite as visibility only. Never as sales proof |
| Fools gold | Revenue claim, no baseline or no control | File in `raw/`, cite only as evidence of category noise |

A finding that the category produces no Gold cases is a legitimate and valuable result. Do not pad the table to avoid it.

## Engine matrix

Every lane is answered per engine. Absent evidence is recorded as absent, per root `CLAUDE.md`.

| Engine | Priority | Why | Known open question |
|---|---|---|---|
| ChatGPT — OpenAI | 1 | Assumed largest assistant share | Ad product status as of 2026-09 |
| Claude — Anthropic | 1 | User-named primary | Does it carry commercial recommendation at all |
| Google — AI Overviews, AI Mode, Gemini | 1 | Largest query volume, existing ad stack | Ad formats live in AI surfaces |
| Perplexity | 2 | Earliest mover on sponsored answers | Inventory scale, real spend |
| Microsoft Copilot | 2 | Existing Bing ad stack | Merchant program reach |
| Amazon Rufus | 2 | Transaction-adjacent | Closed corpus, own inventory |
| Meta AI, Grok, DeepSeek | 3 | Coverage | Commercial surface exists or not |
| Naver, Kakao, Baidu | 4 | Out of scope per D2 | Record as deferred, not as unknown |

Priority 1 gets full treatment in every pass. Priority 3 and 4 get one existence-check line each.

## Verticals

Anchor plus two, chosen for contrast, not for coverage.

| Vertical | Role | Why |
|---|---|---|
| Skincare and beauty | Anchor, per D5 | High consideration, review-driven, large blog corpus |
| B2B SaaS | Widen — contrast | Best-tool-for-X queries dominate. Long cycle, technical buyer |
| High-CPA regulated — cards, insurance, supplements | Widen — stress test | Affiliate-heavy. Lane D manipulation shows up hardest here |

Two more held in reserve: consumer electronics, travel. Open them only if the anchor set produces no Gold or Silver cases.

## Pass sequence

Each pass: one question, named deliverable files, a done condition. A pass without a done condition is not scheduled.

| # | Pass | Question | Deliverable | Gate — needs |
|---|---|---|---|---|
| 0 | Method completion | What are the rules and templates | `glossary.md`, `engine-matrix.md`, `evidence-bar.md`, `templates/`, `line-budgets.md` | scope, trust-rubric |
| 1 | Sources | Where does each lane get pulled from | `sources/channels.md`, `shortlist.md`, `query-book.md` | 0 |
| 2 | Raw wave A — infra and platform primary | What do the platforms and the pipes say | `raw/` per pull | 1 |
| 3 | Raw wave B — vendor census | Who sells this, at what price, on what claim | `raw/` per vendor | 1 |
| 4 | Raw wave C — success-story hunt | Who published a case that clears the bar | `raw/` per case | 0, 1 |
| 5 | Raw wave D — manipulation evidence | How is recommendation gamed, does it work | `raw/` per technique | 1 |
| 6 | Markets | How big is each sub-market, by what method | `markets/` one file per sub-market | 2, 3 |
| 7 | Competitors | Who are they, really | `competitors/` profiles plus `INDEX.md` | 3, 4 |
| 8 | Customers | Who buys, what they pay, who blocks | `customers/` | 4 |
| 9 | Findings | What does the evidence actually support | `findings/` proof scorecard, whitespace | 5, 6, 7, 8 |
| 10 | Measured by us | What do we observe ourselves | `raw/` panel output, `findings/` analysis | 0 — starts early, runs long |
| 11 | Transition playbook | What must a brand change, in what order | Playbook doc, then `MegaPlan.md` entry | 9, 10 |

**Pass 10 starts early and runs in parallel.** A visibility time series needs elapsed calendar time. Starting it at Pass 9 wastes a month. It begins as soon as Pass 0 fixes the engine matrix and the prompt set, then samples on a fixed schedule while Passes 1 through 9 run.

### Pass detail — the three that carry the weight

**Pass 2 — infrastructure and platform primary.** Cheapest hard numbers available. Crawler and referral telemetry, clickstream panels, retail analytics vendors publishing free, and every priority-1 platform's own docs, changelog, pricing and merchant terms. Tier 3 and tier 4 per `trust-rubric.md`. Method disclosure is checked per provider, every time.

**Pass 4 — success-story hunt.** The core ask, and the pass most likely to return little. Channels: earnings-call transcripts and investor decks where a brand names AI-surface performance, agency data posts carrying client numbers, conference talks with slides, vendor case studies, practitioner write-ups, and trade press that links to primary data. Every candidate is graded against the evidence bar on intake, before it is compiled. Ungraded cases do not enter `raw/`.

**Pass 5 — manipulation evidence.** Techniques to document: corpus seeding in high-citation sources, review and listicle manufacture, comparison-page farming, content written to satisfy known citation preferences, structured-data and `llms.txt`-style signalling, and prompt injection embedded in indexed content. For each: how it works, who is doing it, whether any measured evidence shows it moving an answer, and what the engines do about it.

Lane D is **research into manipulation, not execution of it.** Per `projects/MVP-MANDATE.md`, any measurement runs only against infrastructure we control or public material published for study. No third-party targeting, no live manipulation of a production answer surface, no testing against a brand we do not own.

## Line budgets

| File kind | Budget | Note |
|---|---|---|
| `raw/` pull | none | Exempt. Verbatim, uncompressed |
| Competitor profile | 80 lines | Same questions, same order, per template |
| Market file | 120 lines | Sizing method shown, not just the number |
| Customer segment | 80 lines | |
| Finding | 100 lines | Cites the compiled files behind it |
| `INDEX.md` | one line per company | Entry point, nothing else |

## Orchestration

Per `projects/ORCHESTRATION.md`: hard cap of 3 concurrent agents machine-wide, main thread is scheduler and does not count.

| Pass | Model | Shape |
|---|---|---|
| 0 | Opus | Single agent, method design |
| 1 | Opus | Single agent, channel and query design |
| 2, 3, 4, 5 | Sonnet | Split by deliverable. One agent per source cluster, sequential as slots free |
| 6, 7, 8 | Opus | Compile is synthesis. Split by file |
| 9 | Opus | Single agent, then a second for adversarial review |
| 10 | Sonnet to sample, Opus to analyse | Scheduled sampling, fixed prompt set |
| 11 | Fable to draft, Opus to review | Playbook is persuasion. Review it against `findings/` |

Split rule from `ORCHESTRATION.md` applies: one agent per task with a single deliverable file, one question, one done condition. Passes 2 through 5 are the exception that fans out widest — fan-out reading with one shared output shape.

Agents never run git. The main thread commits after every agent lands.

## Known failure modes

Each is scheduled against, not hoped away.

| Risk | Mitigation |
|---|---|
| Category results are mostly affiliate roundups | `query-book.md` at Pass 1 routes around them. Tier 7 not pulled |
| No vendor can demonstrate causal lift | "No Gold cases exist as of 2026-09" is a finding. Write it |
| Engine answers are stochastic | Pass 10 fixes prompt set, repeats, region, date. Model versions recorded per sample |
| Engines change monthly | Every file dated. Competitor file older than one quarter is stale per `scope.md` |
| Assistant cutoff 2026-05, now 2026-09 | Nothing from model memory enters `docs/`. Memory leads re-pulled or dropped |
| Visibility conflated with traffic conflated with sales | Three metric definitions fixed in `glossary.md` at Pass 0. No file crosses them silently |
| Lane D drifts into doing the thing | Constraint stated in Pass 5 detail. Review agent checks it |

## Out of this plan

- A go or no-go verdict. Root `CLAUDE.md` reserves that for the user
- Building anything. `projects/` opens only after Pass 9
- Classical SEO, except where it bounds or sizes the new market
- APAC as a demand market. Engineering location only, per D2

## Caveats

- Pass count is 12. A long research programme, not one pass. Passes 0 and 1 are cheap and gate everything; run them before estimating the rest.
- Gates are real. Compiling `markets/` before Passes 2 and 3 land produces exactly the memory-sourced file root `CLAUDE.md` forbids.
- The evidence bar may disqualify most of what the category publishes. That outcome is the answer to D6, not a failure of the pass.
- Vendor and practitioner names discussed in chat on 2026-09-22 came from model memory and are **not** recorded here. They enter research only as Pass 1 query seeds, and survive only if re-pulled into `raw/`.

# Research plan — demand for brand visibility and recommendation inside AI assistants

Set 2026-09-22, revised same day to research-only per `scope.md` revision 2. Passes run in order, gated. Nothing here is a finding; findings live in `docs/findings/`.

Read before executing: root `CLAUDE.md`, `MegaPlan.md`, `docs/CLAUDE.md`, `scope.md`, `trust-rubric.md`.

## What the research must answer

One question, stated once:

> Which segments show real-world demand for visibility and recommendation inside AI assistants, what evidence shows it works, and what did brands that moved actually change?

Everything below serves that. A pass that does not narrow it gets cut.

## Scope resolution

All decisions live in `scope.md` — brief, revision 1 (D1–D6), revision 2 (R1–R6). Consequences for this plan:

- Deliverable is evidence, not a playbook, not a build. Pass 11 compiles what brands changed; it does not prescribe.
- Internet-only. No interview pass. Demand is read from public signals (Pass 8).
- No dates, no cost caps. Gates are evidence gates only.
- Engine priority and vertical choice are defaults the user declined to weigh in on. They stand until Pass 2 share data reweights them.
- `projects/` does not open. Ever, in this repo.

## Six lanes

Lanes are research tracks. Sub-markets are what gets sized. Segments are what gets demand-read. Three axes, not one.

| Lane | Track | Core question | Compiles into |
|---|---|---|---|
| A | Organic recommendation — GEO, AEO, LLMO | How does a brand get named in an answer | `markets/`, `competitors/` |
| B | Paid placement — AI ads | What inventory exists, what it costs, who buys | `markets/` |
| C | Agentic commerce | Who controls checkout inside the agent | `markets/` |
| D | Manipulation and gaming | How recommendation is steered, and whether it works | `findings/` |
| E | Measurement and proof | Who demonstrates causal lift rather than correlation | `findings/`, cross-cutting |
| F | Transition evidence | What brands that moved actually changed: org, content ops, stack, budget | `customers/`, `findings/` |

E and F are cross-cutting. Every pass in A through D feeds them.

## Structural checks — one section in every `markets/` file

Added 2026-09-22 after plan review. Each is a question the file answers or marks `unknown — checked <channel> <date>`.

| Check | Question |
|---|---|
| Substitute | What does the brand do today instead. Is "do nothing" the real competitor |
| Platform risk | Which engine ships native tooling that makes third-party vendors redundant, and when |
| Incumbent bundling | Which SEO or analytics incumbent added this as a feature, at what price delta |
| Regulatory | Ad disclosure rules inside AI answers — EU DSA, EU AI Act, FTC — what is in force as of the pull date |

## Segments — what demand is read against

| Axis | Values |
|---|---|
| Sub-market | Organic, paid, agentic commerce |
| Vertical | Skincare and beauty (anchor), B2B SaaS, high-CPA regulated |
| Buyer size | SMB, mid-market, enterprise |

A segment is one cell. Pass 8 fills a demand-signal row per cell. Empty cells are recorded as empty, with the channels checked.

### Demand signals — internet-only

Fixed at Pass 0 in `demand-signals.md`. Each signal: what it proxies, where it is pulled, its bias, its tier.

| Signal | Proxies | Bias |
|---|---|---|
| Job postings naming AI visibility, GEO, AEO | Budgeted intent | Lags spend; large firms over-represented |
| Vendor customer counts, logos, case-study rosters | Paying demand | Vendor-reported; logos are not contracts |
| Vendor funding rounds and stated ARR | Investor belief, not buyer demand | Filed beats stated |
| Review-site volume and dates — G2, Capterra | Active buyers | Vendors farm reviews; check velocity not count |
| Community thread volume — r/SEO, r/PPC, GEO forums | Practitioner attention | Vocal minority |
| Agency service pages and rate cards | Sell-side belief in demand | Marketing |
| Earnings-call and investor-deck mentions by brands | Board-level attention | Rare, high value when present |
| Conference agenda counts | Category attention | Sponsor-driven |
| Search interest for category terms | Awareness, not spend | Term confusion across GEO meanings |

Attention signals never stand in for spend signals. A segment with attention and no spend is recorded as exactly that.

## Evidence bar — what counts as a success story

The hardest ask in this plan. Most published cases fail this bar. The bar is set before pulling so it cannot be relaxed to fit what turns up.

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

Survivorship is structural: published cases are winners. Every `findings/` scorecard states this once and reports the search volume behind the case count — how many candidates screened, how many cleared.

## Engine matrix

Every lane is answered per engine. Absent evidence is recorded as absent, per root `CLAUDE.md`.

| Engine | Priority | Why | Known open question |
|---|---|---|---|
| ChatGPT — OpenAI | 1 | Assumed largest assistant share | Ad product status as of 2026-09 |
| Claude — Anthropic | 1 | Default; user declined to weigh | Does it carry commercial recommendation at all |
| Google — AI Overviews, AI Mode, Gemini | 1 | Largest query volume, existing ad stack | Ad formats live in AI surfaces |
| Perplexity | 2 | Earliest mover on sponsored answers | Inventory scale, real spend |
| Microsoft Copilot | 2 | Existing Bing ad stack | Merchant program reach |
| Amazon Rufus | 2 | Transaction-adjacent | Closed corpus, own inventory |
| Meta AI, Grok, DeepSeek | 3 | Coverage | Commercial surface exists or not |
| Naver, Kakao, Baidu | 4 | Out of scope per D2 | Record as deferred, not as unknown |

Priority 1 gets full treatment in every pass. Priority 3 and 4 get one existence-check line each.

**Reweight rule.** Pass 2's first deliverable is an assistant-share table, tier-labeled. Priorities above are reassigned from it, dated, before Passes 3 through 5 spawn. Priorities are assumptions until then.

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
| 0 | Method completion | What are the rules and templates | `glossary.md`, `hypotheses.md`, `demand-signals.md`, `panel-protocol.md`, `templates/` | scope, trust-rubric |
| 1 | Sources | Where does each lane get pulled from | `sources/channels.md`, `shortlist.md`, `query-book.md` | 0 |
| 2 | Raw wave A — infra and platform primary | What do the platforms and the pipes say | `raw/` per pull; assistant-share table first | 1 |
| 3 | Raw wave B — vendor census | Who sells this, at what price, on what claim | `raw/` per vendor | 1 |
| 4 | Raw wave C — success-story hunt | Who published a case that clears the bar | `raw/` per case, screened count recorded | 0, 1 |
| 5 | Raw wave D — manipulation evidence | How is recommendation gamed, does it work | `raw/` per technique | 1 |
| 6 | Markets | How big is each sub-market, by what method | `markets/` one file per sub-market, structural checks included | 2, 3 |
| 7 | Competitors | Who are they, really | `competitors/` profiles plus `INDEX.md` | 3, 4 |
| 8 | Demand per segment | Which cells show spend, which show only attention | `customers/` one file per vertical, signal matrix | 1, 3 |
| 9 | Findings | What does the evidence actually support | `findings/` proof scorecard, demand map, whitespace, unknowns | 5, 6, 7, 8 |
| 10 | Measured by us | What do we observe ourselves | `raw/` panel output, `findings/` analysis | 0 — starts early, runs long |
| 11 | Transition evidence | What did brands that moved actually change | `findings/transition-evidence.md` | 9, 10 |

**Pass 10 starts early and runs in parallel.** A visibility time series needs elapsed calendar time. It begins as soon as Pass 0 fixes `panel-protocol.md`, then samples on a fixed schedule while Passes 1 through 9 run.

### Pass 0 additions — set 2026-09-22

**`hypotheses.md`.** Pre-registered. Each hypothesis states the claim, what evidence would confirm it, and what evidence would kill it. Pass 9 scores every hypothesis against `raw/`. Without this, findings become confirmation of whatever Pass 4 surfaced. Starter set:

| # | Hypothesis | Kills it |
|---|---|---|
| H1 | Referral from AI assistants converts above organic search | Any tier-4-or-better panel showing parity or worse |
| H2 | Paid inventory inside AI surfaces exists at scale as of 2026-09 | No P1 engine with a self-serve or IO-based product |
| H3 | At least one vendor demonstrates causal lift | Zero Gold cases after Pass 4 screen |
| H4 | Demand is attention-only in every SMB cell | Any SMB cell with a spend signal |
| H5 | Corpus seeding measurably moves an answer | No Pass 5 technique with published before-and-after |

**`panel-protocol.md`.** Fixes for Pass 10: prompt set per vertical, n per prompt, region, logged-in versus logged-out, web-search tool on versus off, model version recorded per sample, sampling calendar. Consumer chat surface is the primary measurement. API is a secondary surface and is labeled so — API answers are not what users see.

**`demand-signals.md`.** The signal catalogue above, plus the empty segment matrix.

### Pass detail — the passes that carry the weight

**Pass 1 — sources.** Includes the predecessor repo `D:\researchs\market-research\` as a channel: its `raw/` files, dated, tiered like any other source. Its conclusions are not inherited. The query book is red-teamed by a second agent before Pass 2 spawns — query design decides what gets found.

**Pass 2 — infrastructure and platform primary.** Cheapest hard numbers available. Crawler and referral telemetry, clickstream panels, retail analytics vendors publishing free, and every priority-1 platform's own docs, changelog, pricing and merchant terms. Tier 3 and tier 4 per `trust-rubric.md`. Method disclosure is checked per provider, every time.

**Pass 4 — success-story hunt.** The pass most likely to return little. Channels: earnings-call transcripts and investor decks where a brand names AI-surface performance, agency data posts carrying client numbers, conference talks with slides, vendor case studies, practitioner write-ups, and trade press that links to primary data. Every candidate is graded against the evidence bar on intake. Ungraded cases do not enter `raw/`. The count of candidates screened is recorded alongside the count that cleared.

**Pass 5 — manipulation evidence.** Techniques to document: corpus seeding in high-citation sources, review and listicle manufacture, comparison-page farming, content written to satisfy known citation preferences, structured-data and `llms.txt`-style signalling, and prompt injection embedded in indexed content. For each: how it works, who is doing it, whether any measured evidence shows it moving an answer, and what the engines do about it. Academic sources tiered per `trust-rubric.md`.

Lane D is **research into manipulation, not execution of it.** Any measurement runs only against infrastructure we control or public material published for study. No third-party targeting, no live manipulation of a production answer surface, no testing against a brand we do not own.

**Pass 6 — markets.** The category is roughly two years old. Every top-down TAM available is a forecast, and `trust-rubric.md` downgrades forecasts presented as measurement. Sizing method is therefore bottom-up: vendor count × disclosed pricing × disclosed customer count, each vendor-reported and labeled, plus one proxy — share of search or SEO budget, analyst-derived. Forecasts are recorded side by side as forecasts, never as the size.

**Pass 8 — demand per segment.** Internet-only. One file per vertical; inside it, one row per sub-market × buyer-size cell. Each row carries every signal from `demand-signals.md` with its pull and tier, and a one-word read: spend, attention, or none. Nothing is inferred from a vendor's target-customer page — that is a sell-side claim.

**Pass 11 — transition evidence.** Compiles, from Pass 4 cases and Pass 8 signals, what brands that moved actually changed. Descriptive, cited, per case. Not a recommendation. A playbook is out of scope per `MegaPlan.md`.

## Staleness rule

Engines change monthly. Any `raw/` pull older than one quarter at the time a compiled file cites it is re-checked first, and the re-check dated. Competitor profiles older than one quarter are stale per `scope.md`. Every compiled file states the oldest pull it depends on.

## Line budgets

| File kind | Budget | Note |
|---|---|---|
| `raw/` pull | none | Exempt. Verbatim, uncompressed |
| Competitor profile | 80 lines | Same questions, same order, per template |
| Market file | 120 lines | Sizing method shown, structural checks included |
| Customer segment file | 100 lines | Signal matrix per cell |
| Finding | 100 lines | Cites the compiled files behind it |
| `INDEX.md` | one line per company | Entry point, nothing else |

## Orchestration

Per `projects/ORCHESTRATION.md`: hard cap of 3 concurrent agents machine-wide, main thread is scheduler and does not count.

| Pass | Model | Shape |
|---|---|---|
| 0 | Opus | Single agent, method design |
| 1 | Opus | Single agent for channels and queries, second Opus agent red-teams the query book |
| 2, 3, 4, 5 | Sonnet | Split by deliverable. One agent per source cluster, sequential as slots free |
| 6, 7, 8 | Opus | Compile is synthesis. Split by file |
| 9 | Opus | Single agent, then a second for adversarial review against `hypotheses.md` |
| 10 | Sonnet to sample, Opus to analyse | Scheduled sampling, fixed prompt set, browser extension for consumer surfaces |
| 11 | Opus | Single agent, descriptive compile |

Split rule from `ORCHESTRATION.md` applies: one agent per task with a single deliverable file, one question, one done condition. Passes 2 through 5 fan out widest — fan-out reading with one shared output shape.

Agents never run git. The main thread commits after every agent lands, on master.

## Programme done — evidence conditions only

No dates, no budgets. The programme is done when every row holds.

| Condition | Bar |
|---|---|
| Load-bearing claims in `findings/` at tier 3 or better | 80 percent or more |
| Priority-1 engine × sub-market cells | Every cell filled with a number or an explicit `unknown — checked` |
| Segment matrix | Every cell reads spend, attention, or none, with signals behind it |
| Success stories | At least one Silver per vertical, or documented absence with screened count |
| Hypotheses | Every H scored confirmed, killed, or unresolved with the channel checked |
| Pass 10 | At least three pre-registered predictions checked against the panel |

## Known failure modes

Each is scheduled against, not hoped away.

| Risk | Mitigation |
|---|---|
| Category results are mostly affiliate roundups | `query-book.md` at Pass 1 routes around them. Tier 7 not pulled |
| No vendor can demonstrate causal lift | "No Gold cases exist as of 2026-09" is a finding. Write it |
| Survivorship — only winners publish | Screened count recorded next to cleared count. Stated once per scorecard |
| Confirmation — findings echo Pass 4 | `hypotheses.md` pre-registered. Adversarial review scores against it |
| Measuring the wrong surface | `panel-protocol.md` names consumer chat as primary, API as secondary |
| Engine answers are stochastic | Pass 10 fixes prompt set, repeats, region, date. Model versions recorded per sample |
| Engines change monthly | Staleness rule above. Every file dated |
| Assistant cutoff 2026-05, now 2026-09 | Nothing from model memory enters `docs/`. Memory leads re-pulled or dropped |
| Visibility conflated with traffic conflated with sales | Three metric definitions fixed in `glossary.md` at Pass 0. No file crosses them silently |
| Attention read as demand | Signal catalogue separates attention from spend. Cell read is one word |
| Lane D drifts into doing the thing | Constraint stated in Pass 5 detail. Review agent checks it |
| Research drifts into execution planning | `MegaPlan.md` non-goals. Any file naming a date, budget, or build step is cut |

## Out of this plan

- A go or no-go verdict. Root `CLAUDE.md` reserves that for the user
- Building anything. `projects/` does not open in this repo
- Dates, budgets, kill criteria, playbooks, MVPs
- Classical SEO, except where it bounds or sizes the new market
- APAC as a demand market. Engineering location only, per D2

## Caveats

- Twelve passes. Passes 0 and 1 are cheap and gate everything.
- Gates are real. Compiling `markets/` before Passes 2 and 3 land produces exactly the memory-sourced file root `CLAUDE.md` forbids.
- The evidence bar may disqualify most of what the category publishes. That outcome is the answer to D6, not a failure of the pass.
- Internet-only demand reads are proxies. `customers/` states this in its caveats every time. Willingness to pay is never inferred; it is either a disclosed price paid or `unknown`.
- Vendor and practitioner names discussed in chat on 2026-09-22 came from model memory and are **not** recorded here. They enter research only as Pass 1 query seeds, and survive only if re-pulled into `raw/`.

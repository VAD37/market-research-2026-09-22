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

### Scope resolution — addition 1, 2026-09-23

Per `STATE.md` §Decisions taken, lines 177–178, as read 2026-09-23. No bullet above is edited.

- **All three sub-markets are read for potential** — organic, paid, agentic commerce. Source: `STATE.md` line 177, reason: User: "researching potential for all markets... trends and user count regarding market size of organic vs paid vs agentic and future prediction".
- **Market size is read three ways, side by side, each with its tier:** trends, engine user counts over time, forecasts. A forecast is never presented as a size (`trust-rubric.md` line 42); forecasts stay labelled forecast, tier 6 (`STATE.md` line 177). Pass 13 carries it.
- **Builder-constraint question back in scope**, as a research question: `findings/whitespace.md` line 52 — "which of the gaps above, if any, is reachable by a team whose cost advantage is engineering rather than distribution?" This lifts `scope.md` line 88 ("now a hypothetical only … it is not researched as a decision") to researched as a question. The answer stays evidence, never a verdict (`MegaPlan.md` line 17). Source: `STATE.md` line 178, reason: "User items 5 and feedback 6".
- **Engineering-enabled new market potential and novel solutions in scope** as research questions: which capabilities exist in published work that no engine or vendor yet offers. Descriptive only; Pass 14 carries it. Source: `STATE.md` line 178.

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

### Structural checks — addition 1, 2026-09-22

Per `plan-review-1-2026-09-22.md` §6 and §7(e). Added to the table above; no row above is replaced.

- **Incumbent bundling also records: acquired by whom, on what date, per filing.** Evidence behind the addition, review §6: Semrush a wholly owned Adobe subsidiary from 2026-04-28 (8-K) — `docs/raw/a-vendor-census-c4-2026-09-22.md` row 4; Scrunch acquired by Sitecore 2026-06-03 — `docs/raw/a-vendor-census-c2-*` row 1.
- **Regulatory also names the designation status per engine** (review §6 directs this append here; §7 itemises only the bundling line): ChatGPT designated VLOSE 2026-08-31, 159.1M EU users, no Art. 39 repository yet — `docs/raw/b-eu-dsa-ad-repositories-table-2026-09-22.md`; EU AI Act Art. 50 in force 2026-08-02 — `docs/raw/b-regulators-ad-disclosure-table-2026-09-22.md`.

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

### Demand signals — none rule, 2026-09-23

Per `plan-review-2-2026-09-23.md` §5 and §8(e), line 110. Verbatim:

A signal marked `n/a` because it cannot apply to the sub-market by construction counts as checked. The Segment-matrix row is reported under the strict and loose readings until every cell has every applicable signal run; closing it needs S2, S3, S9 and S10 in high-CPA, S4, S6, S12 for skincare paid and agentic, S5 and S6 with paid and agentic terms in B2B SaaS.

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

### Evidence bar — grading rule 1, 2026-09-22

Per `plan-review-1-2026-09-22.md` §3 and §7(c). Applies to every Pass 4 brief and to the P4-c13 re-grade. The seven bar items and the grade table above are unchanged; this fixes how they are applied.

> **A grade is assigned only from the case's own full page with the seven bar items ticked one by one in the raw file; a case not opened is `screened — not opened`, a page with no metric is `screened — no claim`, neither is graded, and a case missing any of items 1–7 is Bronze at best.**

Why it is dated now, per review §3: five censuses operationalised one bar three ways — c1 graded metric-less testimonials Fools gold on intake and opened nothing; c2 screened the same items out as no-claim and did not grade them; c3 graded only opened pages and counted 26 unopened titles as screened; c4 assigned the one Silver without a visible seven-item checklist; c6 scored binary cleared / not-cleared with no Bronze or Fools gold grade at all. The "roughly 150 screened, 1 Silver" aggregate is a mixed count until P4-c13 re-grades it.

### Evidence bar — grading rule 1 reading fixed, 2026-09-23

Per `plan-review-2-2026-09-23.md` §3 and §8(c), line 108. Verbatim:

Every graded case carries `grade_raw`, as its census assigned it, and `grade_rule1`, the literal reading: any of items 1–7 absent on the case's own page caps it at Bronze. From Pass 11 on, counts, done rows and hypothesis marks use `grade_rule1` and cite `grade_raw` beside it. Neither is deleted. A grade moves only through a new dated raw file naming the item that changed.

### Evidence bar — evidence-quality reporting, 2026-09-23

Per `STATE.md` §Decisions taken line 181, reason: "User feedback 3". The grade table and grading rule 1 are unchanged; this fixes how cases are reported.

Every brief and every findings file citing transition or case evidence states, per case:

| Field | Values |
|---|---|
| Metric moved | yes — metric, from value, to value, window; or no |
| Design | experimental — holdout, geo-split, switchback, pre/post with control; or observational |

- A case with no moved metric is reported as **action named, outcome unknown**. Motivating count: `findings/transition-evidence.md`, 99 of 108 cases name a change (`STATE.md` line 124); a named change is not a measured outcome.
- The design category does not re-grade a case: pre/post with control stays Silver, labelled correlational, per the grade table.
- Briefs carry a section **Quality of evidence** with case counts per category: metric moved, experimental; metric moved, observational; action named, outcome unknown.
- Metric-moved experimental cases are what P4-r hunts (`STATE.md` line 26).

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

### Engine matrix — reweight 1, 2026-09-22 (Pass 2, P2-c1)

Reassigns the priorities above from `docs/raw/a-assistant-share-table-2026-09-22.md` and the eleven share pulls it cites. Oldest pull depended on: 2026-09-22 — every cited raw file. Oldest data window carried: May 2025, StatCounter press release, flagged stale in its own raw file and load-bearing in no row below.

| Engine | Prior | Reassigned | Share figures — verbatim, publisher, metric as the publisher names it, window, tier, raw path | Reason |
|---|---|---|---|---|
| ChatGPT — OpenAI | 1 | 1 — no change | Similarweb "share of worldwide generative AI web traffic" ~53%, May 2026, tier 4, `docs/raw/a-similarweb-share-gen-ai-stats-2026-09-22.md`; StatCounter "AI Chatbot Market Share" 79.4%, Aug 2026, tier 4, `docs/raw/a-statcounter-share-ai-chatbot-market-share-2026-09-22.md`; Datos via PPC Land "share of total desktop visits" US 34.80% Q1 2026, EU/UK 44.82% Mar 2026, tier 5 pointer, `docs/raw/a-ppc-land-share-datos-q1-2026-2026-09-22.md`; Comscore "US desktop unique visitors" 33.86M, Mar 2026, tier 5, `docs/raw/a-comscore-share-march-2026-rankings-2026-09-22.md` | First on all three share definitions. Assumption confirmed |
| Claude — Anthropic | 1 | 1 — no change | Similarweb "share of worldwide generative AI web traffic" ~2% Jun 2025 and ~9% May 2026, tier 4, `docs/raw/a-similarweb-share-gen-ai-stats-2026-09-22.md`; StatCounter "AI Chatbot Market Share" 2.57%, Aug 2026, tier 4, `docs/raw/a-statcounter-share-ai-chatbot-market-share-2026-09-22.md`; Datos via PPC Land "share of total desktop visits" US 8.54%, EU/UK 9.61%, Mar 2026, tier 5 pointer, `docs/raw/a-ppc-land-share-datos-q1-2026-2026-09-22.md`; Comscore "US desktop unique visitors" 2.66M (+130.1% MoM), Mar 2026, tier 5, `docs/raw/a-comscore-share-march-2026-rankings-2026-09-22.md` | Held at 1 by scope.md R4 user default; share also rose |
| Google — AI Overviews, AI Mode, Gemini | 1 | 1 — no change | Gemini: Similarweb "share of worldwide generative AI web traffic" ~27-28%, May 2026, tier 4, `docs/raw/a-similarweb-share-gen-ai-stats-2026-09-22.md`; StatCounter "AI Chatbot Market Share" 10.9%, Aug 2026, tier 4, `docs/raw/a-statcounter-share-ai-chatbot-market-share-2026-09-22.md`; Datos via PPC Land US 16.06%, EU/UK 18.88%, Mar 2026, tier 5 pointer, `docs/raw/a-ppc-land-share-datos-q1-2026-2026-09-22.md`. AI Mode: Similarweb "AI Mode query share" 0.34%, Jan-Apr 2026, tier 4, `docs/raw/a-similarweb-share-zero-click-marketing-2026-09-22.md`, corroborated at `docs/raw/a-sparktoro-share-zero-click-2026-09-22.md`; Datos via PPC Land "Google AI Mode, share of total desktop visits" US 0.16%, EU/UK 0.21%, Mar 2026, tier 5 pointer, same PPC Land file | Gemini second on every definition; AI Mode itself under 1% |
| Perplexity | 2 | **3** | StatCounter "AI Chatbot Market Share" 4.31%, Aug 2026, tier 4, `docs/raw/a-statcounter-share-ai-chatbot-market-share-2026-09-22.md`; StatCounter via SEJ "AI chatbot referral share" 7.91%, Jun 2026, tier 5 pointer, `docs/raw/a-searchenginejournal-share-ai-visibility-2026-09-22.md`; StatCounter press release "chatbot referral share" 11.8%, May 2025, tier 4, STALE, `docs/raw/a-statcounter-share-referral-press-release-2026-09-22.md`; Similarweb via SEJ "worldwide web visits" 1.3%, May 2026, tier 5 pointer, SEJ file; Comscore "US desktop unique visitors" 0.36M, Mar 2026, tier 5, `docs/raw/a-comscore-share-march-2026-rankings-2026-09-22.md` | Falls on every series carrying it; last of seven at Comscore |
| Microsoft Copilot | 2 | 2 — no change | StatCounter "AI Chatbot Market Share" 2.79%, Aug 2026, tier 4, `docs/raw/a-statcounter-share-ai-chatbot-market-share-2026-09-22.md`; Similarweb via SEJ "worldwide web visits" 1.3%, May 2026, tier 5 pointer, `docs/raw/a-searchenginejournal-share-ai-visibility-2026-09-22.md`; Comscore "US desktop unique visitors" 5.02M, Mar 2026, tier 5, `docs/raw/a-comscore-share-march-2026-rankings-2026-09-22.md`; Comscore "desktop unique visitors," CustomIQ 33.4M (-28% YoY), Dec 2025, tier 4, `docs/raw/a-comscore-share-jan-2026-mobile-desktop-2026-09-22.md` | Ahead of Perplexity on visitors, behind on referral. Mixed |
| Amazon Rufus | 2 | 2 — no change | `unknown — checked Similarweb, Comscore, Datos/SparkToro, StatCounter 2026-09-22`, per `docs/raw/a-assistant-share-table-2026-09-22.md` | No figure exists. Absent evidence is not a demotion |
| Meta AI | 3 | 3 — no change | Comscore "mobile unique visitors," CustomIQ 1.3M (+50% vs. May 2025 — different comparison base), Dec 2025, tier 4, `docs/raw/a-comscore-share-jan-2026-mobile-desktop-2026-09-22.md` | One publisher, one date. Too thin to move |
| Grok | 3 | **2** | Similarweb via SEJ "worldwide web visits" 2.4%, May 2026, tier 5 pointer, `docs/raw/a-searchenginejournal-share-ai-visibility-2026-09-22.md`; Comscore "US desktop unique visitors" 1.65M, Mar 2026, tier 5, `docs/raw/a-comscore-share-march-2026-rankings-2026-09-22.md`; StatCounter press release, not measured — "does not provide referral data in its header", May 2025, tier 4, `docs/raw/a-statcounter-share-referral-press-release-2026-09-22.md` | Outranks Perplexity at two publishers; invisible to referral measurement |
| DeepSeek | 3 | 3 — no change | StatCounter "AI Chatbot Market Share" 0.02%, Aug 2026, tier 4, `docs/raw/a-statcounter-share-ai-chatbot-market-share-2026-09-22.md`; Similarweb via SEJ "worldwide web visits" 4.1%, May 2026, tier 5 pointer, `docs/raw/a-searchenginejournal-share-ai-visibility-2026-09-22.md`; Comscore "US desktop unique visitors" 0.41M, Mar 2026, tier 5, `docs/raw/a-comscore-share-march-2026-rankings-2026-09-22.md` | 4.1% web-visit share against 0.02% referral share. Conflict unresolved |
| Naver, Kakao, Baidu | 4 | 4 — no change | No figure in the share table; no pulled publisher reports one | Deferred per scope.md D2. Recorded as deferred, not unknown |

**What the reweight does and does not do.**

- Reorders depth of treatment for Passes 3 through 5 only. It is not a finding, a sizing, or a verdict.
- Removes no engine. Every row above is still answered per lane, and absent evidence is still recorded as absent.
- Does not change the Claude P1 default — `scope.md` R4 fixes Anthropic at 1 by user default regardless of share, and the user has said nothing otherwise.
- Priority-4 engines stay deferred per `scope.md` D2.
- Perplexity at 3 keeps its existing matrix question ("earliest mover on sponsored answers", lane B). That is not a share question and this reweight does not touch it. Same for Grok at 2, whose promotion is a share reading only.
- Priority-1 rows are confirmed by the evidence, not replaced by it. A reweight 2 appends below this section and never overwrites it.

**Caveats.**

- Three incompatible definitions sit in the table and are never averaged: category web-visit share (Similarweb), referral-click share (StatCounter, whose own FAQ states it cannot directly measure chatbot queries — `docs/raw/a-statcounter-methodology-2026-09-22.md`), and single-engine desktop-population penetration (Datos via PPC Land). ChatGPT reads ~53%, 79.4% and 34.80% on the three. Rank order within one definition, not magnitude across them, is what moved any row here.
- Comscore rows are visitor and conversation counts, not shares at all. Used for rank order inside one publisher's own table only.
- Data windows before 2026-06-22, all pulled 2026-09-22: StatCounter press release May 2025 (flagged STALE in its raw file), Comscore CustomIQ Dec 2025, both Comscore Mar 2026 releases, Datos Mar 2026 and Q1 2026, Similarweb May 2026 and Jan-Apr 2026. Only StatCounter's Aug 2026 dashboard row sits inside the quarter.
- Pointer-tier rows, tier 5, primary not independently confirmed: every Datos figure, via PPC Land; the seven-engine Similarweb May 2026 table and the StatCounter Jun 2026 figure, both via Search Engine Journal. Grok's and DeepSeek's only category-share figures rest wholly on that SEJ pointer — the weakest evidence behind any move in this table.
- No figure at all: Amazon Rufus, and Naver, Kakao, Baidu.
- Every publisher here sells analytics adjacent to what it measures; no figure is independently audited, and none is a recruited-and-disclosed-sample-size consumer panel.

### Engine matrix — evidence notes 1, 2026-09-22

Per `plan-review-1-2026-09-22.md` §6 and §7(d). Notes against the matrix rows above. No row and no "Known open question" cell is edited; each stands until a pass closes it.

| Matrix row | Note, 2026-09-22 | Raw path |
|---|---|---|
| Claude — Anthropic, "Does it carry commercial recommendation at all" | Lane B answered at tier 3: "Claude will remain ad-free … nor will Claude's responses … include third-party product placements", 2026-02-04. Lanes A and C still open — no merchant program found | `docs/raw/b-anthropic-perplexity-platform-summary-2026-09-22.md` table 1 |
| Perplexity, "Earliest mover on sponsored answers" | No live ad product or advertiser page; merchant-terms page 404; 2024-11-12 launch post still live. Status is by absence, not by a statement | `docs/raw/b-anthropic-perplexity-platform-summary-2026-09-22.md` tables 1–2 |
| Amazon Rufus — the slug itself | Renamed "Alexa for Shopping" 2026-05-13; both names still on one page. Matrix slug unchanged; `panel-protocol.md` status note 1 carries both names | `docs/raw/b-microsoft-amazon-platform-summary-2026-09-22.md` naming table |
| ChatGPT — OpenAI | Designated VLOSE 2026-08-31, 159.1M EU users, no Art. 39 ad repository yet, and no repository distinguishes an ad inside an AI answer. EU AI Act Art. 50 in force 2026-08-02 | `docs/raw/b-eu-dsa-ad-repositories-table-2026-09-22.md`; `docs/raw/b-regulators-ad-disclosure-table-2026-09-22.md` |

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

### Pass 4 — second sweep, 2026-09-22

Per `plan-review-1-2026-09-22.md` §1 and §7(b). Seven sweep clusters added alongside the six channel clusters; the six are not re-cut. Cluster rows with pulls, tier and deliverable globs are in `../sources/shortlist.md` under "Pass 4 — second sweep, added 2026-09-22". Every cluster grades per "Evidence bar — grading rule 1, 2026-09-22" above.

| id | Task | Done when |
|---|---|---|
| P4-c7 | Brand-side corroboration — every brand a Pass 2/3 file names as a customer or pilot (Searchable 19 logos, Quattr / Men's Wearhouse, HubSpot Docebo/Fresha, Google Direct Offers Chewy/Gap/L'Oréal/Petco/e.l.f., Copilot Checkout Urban Outfitters/Etsy — c1, c4, c3, `b-google-platform-summary`, `c-vendor-census-c6`): the brand's own newsroom, IR page, case page | Each brand reads `corroborates / contradicts / silent — checked <URL>` |
| P4-c8 | Per-vertical sweep — skincare and beauty; brand blogs, vertical trade press linking primary, community write-ups, per the vertical overlays in `../sources/query-book.md` | Screened and cleared counts exist for that vertical, every case graded per grading rule 1 |
| P4-c9 | Per-vertical sweep — B2B SaaS; same channels | As P4-c8, for B2B SaaS |
| P4-c10 | Per-vertical sweep — high-CPA regulated (cards, insurance, supplements); same channels | As P4-c8, for high-CPA regulated |
| P4-c11 | Negative-result sweep — `query-book.md` amendment 7 rows (r/SEO, r/bigseo, r/PPC negatives; HN dissent; null-result papers), plus 1–2-star G2/OMR reviews naming no lift | Screened, negative-found and vendor-named counts are recorded |
| P4-c12 | EU-brand sweep — set X aliases (`query-book.md` amendment 4) against C64/C65: horizont.net, wuv.de, t3n.de, onlinemarketing.de, omr.com | Every alias run and recorded; hits graded per grading rule 1; screened and cleared counts per vertical |
| P4-c13 | Full-page re-grade of Pass 3 — every Bronze or better and every `screened — not opened` title in c1–c6, opened and graded per grading rule 1 | Every such title opened, or recorded unreachable, and regraded with the seven bar items ticked one by one |

**Pass 4 is done when the six channel clusters and the seven sweep clusters have landed and per-vertical screened/cleared counts exist for all three verticals.**

Why the sweep exists, per review §1: the six channel clusters are all publisher-typed and none asks the brand; the reserve-vertical trigger in "Verticals" above is live and untested because the one Silver found across roughly 150 vendor cases is apparel, outside all three verticals; no P4 cluster hunts failures; set X was never run; and Pass 3 screened roughly 150 titles from overview pages rather than from full pages.

### Pass 10 and Pass 11 — hold note, 2026-09-22

Pass 10 sampling held by user decision 2026-09-22 22:40; day 0 recorded per engine; done-row unchanged; HE2, HE3, HP1–HP4 marked `not produced` at Pass 9 if still held. Pass 11 gate reads: 9, and 10 or its recorded hold.

The Pass 11 gate cell in the pass-sequence table above is not edited; this note supersedes it. Source: `plan-review-1-2026-09-22.md` §2, §4 and §7.

### Pass 10 — closure map, 2026-09-23

Per `plan-review-2-2026-09-23.md` §4 and §8(d), line 109. Verbatim:

One neutral sampling date can close HE2, HP1, HP3 and confirm HE3; HP2 and HP4 need two dates ≥14 days apart. Day-0 confounds on record: Claude logged-in with Memory, Gemini Flash-Lite throttled, AI Mode IP-localised to Vietnam, ChatGPT and Perplexity blocked. No raw file records a US egress path. Recorded for the user's decision; the hold is unchanged.

### Pass 10 — skipped, 2026-09-23

Per `STATE.md` §Decisions taken line 174, reason: User: "pass 10 skip for now. We dont care about what observed ourself". Supersedes the hold note and closure map above on status; neither is edited, and the closure map stays as a record.

- Own-panel sampling does not run. HE2, HE3, HP1–HP4 stay `not produced`.
- The Pass 10 done row reads **skipped by owner**.
- The day-0 gap — the panel raw files dated 2026-09-22 listed in `plan-review-2-2026-09-23.md` §4 — is recorded and never back-filled.
- Hypothesis marks and Pass 10 done-row status are reported with this reading: `not produced — Pass 10 skipped by owner 2026-09-23`.
- Pass 11's gate, "9, and 10 or its recorded hold", reads the skip as the recorded hold.
- Third-party published measurement of engine surfaces is still pulled by other passes at its own tier; that is not Pass 10.

### Reporting layer, 2026-09-23

Per `plan-review-2-2026-09-23.md` §7 and §8(g), line 112. Verbatim:

`findings/executive-brief-<date>.md`, 70 lines, re-stated from compiled files only, per the review-2 §7 contains/excludes table. Rewritten under a new date whenever a finding it cites changes. Not a pass; no gate.

### Pass sequence — additions 2026-09-23

Per `STATE.md` §Decisions taken lines 175–179 and §Queue lines 25–30, as read 2026-09-23. The pass table above is not edited; rows below extend it.

| # | Pass | Question | Deliverable | Gate — needs |
|---|---|---|---|---|
| 12 | AI ads — engines selling ads | What AI-answer ad inventory exists, at what price, bought by whom | `findings/ai-ads-evidence.md`; `markets/paid-placement.md` append | 2, 6 |
| 13 | Market potential | How big and how fast, per sub-market, read three ways | `findings/market-potential.md`; three `markets/` appends | 2, 6, 12 |
| 14 | Frontier scan | Which published capabilities could steer or monetise recommendation | `findings/frontier-scan.md` | 1, 5 |
| 8-r | Demand re-run | Close blank and unrun segment cells | `customers/` appends; `findings/demand-map.md` append | 8, R-BLOCKED |
| 4-r | Success-story re-run | Metric-moved experimental cases, blocked channels included | `findings/proof-scorecard.md` append | 4, R-BLOCKED |
| 9-r | Findings re-run | Tier-3 re-evidence; score H17 onward | `findings/*.md` appends; `findings/unknowns.md` append | 8-r, 4-r, 12, 13, 14 |

Every pass below may pull by extension (`ext`) or Playwright (`pw`), including channels blocked on 2026-09-22 (`STATE.md` line 179). A channel needing registration or paid credentials is logged per "Orchestration — browser and search revision, 2026-09-23" and not worked around. `markets/` files each sit at 120 lines, their line budget (`wc -l` 2026-09-23); every `markets/` append below states its overrun in that file's caveats.

**Pass 12 — AI ads and AI engines selling ads.** Lane B. Source: `STATE.md` line 175, reason: User: "vastly important key details that we are missing"; live row `P12-ads`, line 17.

- Question: which engines sell placement inside AI answers, in what formats, at what price, to how many advertisers, for what revenue.
- Inputs: `markets/paid-placement.md`; `raw/b-*-platform-summary-2026-09-22.md`; `raw/b-eu-dsa-ad-repositories-table-2026-09-22.md`; `raw/b-regulators-ad-disclosure-table-2026-09-22.md`.
- Engines: ChatGPT; Google AI Overviews, AI Mode, Gemini; Microsoft Copilot; Amazon Rufus / Alexa for Shopping; Perplexity; Meta AI; any other engine found selling AI-answer placement.
- Pulls, per engine: inventory and formats; label wording, verbatim; targeting; pricing and bid guidance; advertiser counts and named advertisers; engine ad-revenue statements; agency and holding-company statements; third-party AI-ad networks, any found; advertiser-side spend evidence; published third-party measurement of ad presence; regulation in force.
- Channels: `sources/channels.md` C1, C2, C6, C7, C9, C10, C12 (platform primary, tier 3); C13, C43 (filings, earnings, tier 2); EU DSA ad repositories; agency and holding-company newsrooms; trade press linking primary.
- Deliverable: `findings/ai-ads-evidence.md`, 100 lines; dated appends to `markets/paid-placement.md`.
- Gate to open: Pass 2 platform summaries and Pass 6 `markets/paid-placement.md` landed — met 2026-09-22.
- Gate to close: the Pass 12 row in "Programme done — addition 2026-09-23" holds; H17–H20 scorable.
- Does not: open advertiser accounts, buy or test ads, sample engine answers itself (Pass 10 skipped), estimate revenue beyond stated figures, rank engines for purchase.

**Pass 13 — market potential, three sub-markets.** Lanes A, B, C; E for method. Source: `STATE.md` line 177; queue row `P13-size`, line 27.

- Question: what size and trajectory each sub-market shows, read from user counts, trends and forecasts side by side.
- Inputs: `raw/a-assistant-share-table-2026-09-22.md`; the three `markets/` files; `raw/e-market-size-table-2026-09-22.md`; Pass 12 output for paid.
- Pulls: MAU, WAU or DAU statements per engine, as the engine names them, each with its date, two or more dated points per engine; share trends, one definition per series; AI-referral trends; forecasts per sub-market with publisher, base year, target year, definition and tier; bottom-up floors per Pass 6 detail above (vendor count × disclosed pricing × disclosed customer count).
- Channels: engine newsrooms and IR (tier 3); C13, C43 filings and earnings (tier 2); C21 Similarweb and other panels (tier 4); report-sales firms (tier 6).
- Deliverable: `findings/market-potential.md`, 100 lines; one dated append per `markets/` file.
- Gate to open: Passes 2 and 6 landed; Pass 12 landed for the paid sub-market.
- Gate to close: the Pass 13 row in "Programme done — addition 2026-09-23" holds; H21, H22 scorable.
- Does not: present a forecast as a size; average or reconcile forecasts; fit or extrapolate a trend into a forecast of its own; mix share definitions in one series.

**Pass 14 — frontier scan.** Lane D, plus the builder-constraint question (`findings/whitespace.md` line 52). Source: `STATE.md` line 178; queue row `P14-papers`, line 28.

- Question: which published capabilities in retrieval, recommendation, agent commerce and ad auctions inside LLMs a party could use to steer or monetise recommendation, and which no engine or vendor yet offers.
- Inputs: Pass 5 technique files `raw/d-*`; H13's countermeasure evidence; `findings/whitespace.md`.
- Pulls, per paper: venue and review status, date, model versions, code and data availability, capability described, results with n, whether a P1 engine document names a countermeasure, whether code and models are public or access-gated.
- Channels: C47 arXiv; C48 ACL Anthology; C49 Semantic Scholar; C50 Google Scholar; C63 ACM DL, OpenReview (NeurIPS, ICLR), USENIX, IEEE Xplore, DBLP; engine research blogs.
- Tiering: `trust-rubric.md` academic table, lines 25–31. Screened count stated beside kept count.
- Deliverable: `findings/frontier-scan.md`, 100 lines; raw per paper `raw/d-paper-*-2026-09-23.md`.
- Gate to open: Passes 1 and 5 landed — met 2026-09-22.
- Gate to close: the Pass 14 row in "Programme done — addition 2026-09-23" holds; each kept capability read against P1 countermeasure docs or `unknown — checked`; H23–H25 scorable.
- Does not: run, reproduce or adapt any technique; test against production surfaces or third-party brands (Lane D rule, Pass 5 detail above); rank capabilities as opportunities; judge feasibility for a builder. The builder-constraint question is answered by recording which capabilities rest on public code and models, never by a verdict.

**Re-runs — what counts as qualified this time.** Source: `STATE.md` line 176, reason: User: "apply review-2 and then rerun whatever tasks failed to qualified"; queue rows lines 25, 26, 29.

- **P8-r.** Scope, line 25: the 8 blank high-CPA cells; unrun S2, S3, S9, S10; skincare S4, S6, S12; B2B SaaS S5, S6 with paid and agentic terms. Qualified when: all 27 cells read spend, attention or `none — checked` under the `demand-signals.md` cell-read rule; every signal named in "Demand signals — none rule, 2026-09-23" is run or `n/a` by construction; strict and loose readings report the same count, or both are reported with the differing cells named; a channel still blocked after browser retry has a `blocked-channels.md` row and its cell reads blocked, not exhausted.
- **P4-r.** Scope, line 26: Reddit, G2, sec.gov, ~107 unchecked brand pages (`raw/e-case-census-c7-2026-09-22.md`), 25 unopened titles; metric-moved experimental cases only. Qualified when: every opened case carries `grade_raw`, `grade_rule1` and the evidence-quality fields; every brand page reads corroborates, contradicts or silent, with URL; every unopened title is opened or recorded unreachable; screened and cleared counts stated per vertical and per channel; blocked channels logged.
- **P9-r.** Scope, line 29. Qualified when: every re-evidenced claim cites a new dated raw file at tier 3 or better; the tier-3 share is recounted on both the Pass 9 and review-1 lists, each reported three ways per "Tier-3 share — reporting splits, 2026-09-23" and itemised file:claim; H17 onward scored where the producing pass landed, `not produced` otherwise; prior marks kept beside new ones.

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

### Orchestration — cap revision 1, 2026-09-22

Cap 10 live agents machine-wide per user 2026-09-22 22:30, superseding line 244. One browser-extension holder and one Playwright holder at a time. Spawn on completion notifications only. Deliverable globs disjoint per spawn.

Line 244 as numbered at review time is the sentence opening this section: "Per `projects/ORCHESTRATION.md`: hard cap of 3 concurrent agents machine-wide, main thread is scheduler and does not count." That line is not edited; this note supersedes it. Companion append: `projects/ORCHESTRATION.md` "Concurrency cap — revised by the user 2026-09-22". Source: `plan-review-1-2026-09-22.md` §7.

### Orchestration — browser and search revision, 2026-09-23

Per `STATE.md` §Decisions taken lines 179–180, reasons: User: "Allow chrome extension and browser access", "I allow 5000+ websearch budget now"; User: "if any channels require registration then feedback to user"; "append to blocked list for human to review". The Pass 10 row in the table above is not edited.

- Browser allowed for every agent, including channels blocked on 2026-09-22: extension `ext`, Playwright `pw`.
- One `ext` holder at a time; the extension is one shared browser. One `pw` holder at a time, per cap revision 1 above.
- WebSearch budget: 5000+ calls.
- A channel needing registration or paid credentials gets a row in `docs/method/blocked-channels.md`, owned by R-BLOCKED.
- Reddit, 2026-09-23 default: pulled through an open archive API (Arctic Shift, `arctic-shift.photon-reddit.com/api/posts/search` and `/api/comments/search`, current to the pull date; any other open-source Reddit archive is equivalent), never through the browser or extension. The extension refuses reddit.com by its own policy on both `www.` and `old.` URLs, login or not; reddit `.json` gives 403; pullpush.io gives 429. Raw header: `channel: Arctic Shift archive of reddit.com`, `method: curl`, `archive copy, not live`, reddit permalink kept. User decision 2026-09-23. It is never worked around by guessing; the cell or claim it would feed reads `unknown — blocked, see blocked-channels.md`.

`blocked-channels.md` columns:

| Column | Holds |
|---|---|
| channel | Name, with `sources/channels.md` code if any |
| URL | The URL tried |
| what was needed | Data or document sought |
| block type | registration, paid, login, WAF, rate limit, other |
| credential that would unblock | Account or subscription named |
| status | open, unblocked, dropped |
| date | Absolute date of the attempt |

Cap in force is the latest cap line in `STATE.md` §Decisions taken; as read 2026-09-23, line 169: 3 live agents. `plan.md` line 312 (10) and `MegaPlan.md` line 32 (3) are not edited; the STATE line governs where they differ (`plan-review-2-2026-09-23.md` §6, last row).

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

### Programme done — arithmetic note 1, 2026-09-23

Per `plan-review-2-2026-09-23.md` §1 and §8(a), line 106. Verbatim:

While the Pass 10 hold stands, the Hypotheses row has a ceiling of 17 of 23 and the Pass 10 row 0 of 3; neither is reachable. The tier-3, segment-matrix, P1-cell and success-story rows are reachable by internet pulls. Each done-row status names both counts where two exist. Source: `plan-review-2-2026-09-23.md` §1.

### Tier-3 share — reporting splits, 2026-09-23

Per `plan-review-2-2026-09-23.md` §2 and §8(b), line 107. Verbatim:

Bar unchanged at 80%. Every count reports three figures: all load-bearing claims; claims excluding the Lane E case corpus; claims excluding meta-claims with no raw tier. Every count itemises its claims file:claim so a second count can be diffed against it. Source: review-2 §2.

### Programme done — addition 2026-09-23

Per `STATE.md` §Decisions taken lines 174–178. The table above is not edited; these rows extend it, and the Pass 10 row's status wording is fixed.

| Condition | Bar |
|---|---|
| Pass 10 | Status reads "skipped by owner"; 0 of 3, not reachable while skipped |
| Pass 12 | P1 engine × {inventory, price, advertiser count, revenue}: number or `unknown — checked` |
| Pass 13 | Sub-market × {user-count trend, forecast, bottom-up floor}: filled or `unknown — checked` |
| Pass 14 | Screened count stated; each kept paper tiered per `trust-rubric.md` |

Hypotheses row: with H17–H25 registered (`hypotheses.md` "Additions 2026-09-23"), the row counts 32. HE2, HE3, HP1–HP4 stay `not produced` under the skip; the row reports scored-of-32 with those six named, and cannot hold in full while Pass 10 is skipped.

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

### Known failure modes — addition 1, 2026-09-23

Per `plan-review-2-2026-09-23.md` §6 and §8(f), line 111. Rows verbatim:

| Risk | Mitigation |
|---|---|
| Search budget exhausted | briefs carry seed URLs and substitute endpoints |
| Filing host blocked | filing via relay is tier 5, via IR copy tier 3, never tier 2 |
| Channel blocked | done rows mark blocked, not exhausted |
| Paraphrased or summarised pull | raw header `verbatim: partial`, no compiled quote from that part |
| Raw file edited after landing | re-pulled as a new dated file, old kept |
| Count untraceable | every count cites the raw line it sums |
| Tier misread | briefs state lower tier number is stronger |
| Cap figures disagree | STATE decision line is the cap in force |

### Known failure modes — addition 2, 2026-09-23

Per `plan-review-2-2026-09-23.md` §6, lines 75–85, and `STATE.md` §Decisions taken line 182, reason: "User feedback 4". Maps each of the nine §6 debts to the row carrying it; rows A–G are added where addition 1 carries a debt only in part.

| §6 debt, review-2 line | Carried by |
|---|---|
| WebSearch calls exhausted, 77 | addition 1 row 1; row A |
| sec.gov 403 then 503, 78 | addition 1 row 2; row B |
| G2, Capterra, Reddit, Indeed, Upwork, Trends blocked, 79 | addition 1 row 3; row C |
| MozCon abstracts paraphrased, 80 | addition 1 row 4; row D |
| WebFetch summarises, 81 | addition 1 row 4; row E |
| S7 Coty raw edited after creation, 82 | addition 1 row 5; row F |
| Untraceable counts, 83 | addition 1 row 6, in full |
| P8 censuses read tier-5 floor as ceiling, 84 | addition 1 row 7; row G |
| Cap: two figures in force, 85 | addition 1 row 8; Orchestration revision 2026-09-23 |

| Risk | Mitigation |
|---|---|
| A — WebSearch calls run short again | WebSearch budget 5000+ per `STATE.md` line 179; exhaustion logged in STATE |
| B — sec.gov still refuses fetch | Browser retry first; failure gets a `blocked-channels.md` row |
| C — Channel needs an account or payment | `blocked-channels.md` row; cell reads blocked; never guessed around |
| D — Source bars verbatim copy (copyright) | Raw marks paraphrase, keeps URL; compiled files cite, never quote |
| E — WebFetch returns a summary, not text | Browser pull where quoted text is load-bearing; header names method |
| F — Raw edit goes unnoticed | Main-thread verify checks raw files unchanged since landing commit |
| G — Tier floor read as ceiling | Brief text: named tier is a floor; higher tiers sought first |

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

### Pass sequence — addition 2, 2026-09-23

Per user instruction 2026-09-23: the brief bake-off is "a real evaluation report … part of this project … final step of this project research", not tooling. No row above is edited; this row extends the additions table. Full plan: `brief-bakeoff/README.md`.

| # | Pass | Question | Deliverable | Gate — needs |
|---|---|---|---|---|
| 15 | Brief-method evaluation | Which brief-writing method turns the evidence into a cold-readable director brief with zero invented numbers | `findings/brief-method-eval-<date>.md`; `method/brief-bakeoff/runs/`, `judge/`, `scoresheet.csv` | 9-r landed; every other pass row landed or recorded skipped |

**Pass 15 — brief-method evaluation.** Lane E, reporting layer.

- Question: one input (the failed `findings/director-brief-2026-09-23.md`), one shared instruction, one agent per method — seven external brief-writing methods, pulled 2026-09-23 with commit and license recorded in `brief-bakeoff/README.md`, plus the user's own template as control and one control repeat for variance. Which produced the brief a cold director reads in 10 minutes, and which invented a number.
- Inputs: `brief-bakeoff/README.md`, `shared-instruction.md`, `baseline-template.md`; the failed brief; `findings/`, `markets/`, `competitors/INDEX.md`, `customers/`, `raw/` read-only; `trust-rubric.md`.
- Runs: R0 control, R1–R9 one method each, R0b control repeat, R10 = BRIEF-4 output if landed. Each run writes `brief.md`, `notes.md`, `trace.md` into `brief-bakeoff/runs/<id>/` and nowhere else.
- Scoring: blind judge agent, then the user, same 14 columns in `brief-bakeoff/scoresheet.csv`; disagreement ≥2 is the read.
- Deliverable: `findings/brief-method-eval-<date>.md`, 100 lines, per `templates/finding.md`; evidence is the scoresheet and trace files, raw is `runs/`.
- Gate to open: 9-r landed and every other pass row landed or recorded skipped — it is the last pass. BRIEF-4 may land before or after; if before, its brief is judged as R10.
- Gate to close: every run has three files and a judge row; user rows filled; finding landed.
- Does not: pick a method for the user; create a skill under `.claude/`; copy unlicensed method text (StrategyU, aapersh) into `docs/`; use the web inside a run; run any method's own commands.
- Orchestration: cap in force per `STATE.md`; one model for all runs; agents never run git; main thread adds queue row `P15-brief-eval` and commits after each wave.
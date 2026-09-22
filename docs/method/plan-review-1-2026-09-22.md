# Plan review 1 — orchestration and plan against the 2026-09-22 22:40 context

Task REVIEW-1, 2026-09-22. Method review only: what the scheduler should change in `plan.md`, `ORCHESTRATION.md`, `panel-protocol.md`, `shortlist.md`, `hypotheses.md`, and what it should not. No market claim below goes beyond a cited `docs/raw/` summary. Nothing existing is edited; every amendment is a dated append the scheduler can paste. Inputs: the method set, `STATE.md` as of 22:40 HCM, and the 19 raw summaries the brief named.

Context judged against: user priority 22:40 (success-story hunt first; own model-output sampling low value now), cap 10 from 22:30, WebSearch budget exhausted, sec.gov 403 all session, extension dropped once, Playwright bot-blocked on google.com and perplexity.ai, three 429 kills, Pass 2 and 3 done, one Silver (Quattr / Men's Wearhouse, `a-vendor-census-c4-2026-09-22.md` row 3) and zero Gold across ~150 vendor cases.

## 1. Pass ordering and slot allocation under cap 10

Live now (`STATE.md` §Live agents, lines 13–24): P4-c1–c6, P5-c1, P5-c2, P10 AI Mode retry, REVIEW-1 = 10. No free slot until a landing. Order below is the queue front as slots free; it supersedes the `STATE.md` §Queue order (lines 30–44) and is spawn-on-completion, never a burst.

| Order | Task | Why now, or why wait |
|---|---|---|
| 1 | **P4-c7 brand-side corroboration** — every brand a Pass 2/3 file names as a customer or pilot (Searchable 19 logos, Quattr / Men's Wearhouse, HubSpot Docebo/Fresha, Google Direct Offers Chewy/Gap/L'Oréal/Petco/e.l.f., Copilot Checkout Urban Outfitters/Etsy — c1, c4, c3, `b-google-platform-summary`, `c-vendor-census-c6`): the brand's own newsroom, IR page, case page. Done when each brand reads `corroborates / contradicts / silent — checked <URL>` | The six clusters (`shortlist.md` lines 60–65) are all publisher-typed; none asks the brand. A vendor claim confirmed on the brand's own site is the only route from tier 5–6 to a cross-source case without outreach. Highest yield per slot for the user's priority |
| 2 | **P4-c8 / c9 / c10 per-vertical sweeps** — skincare-beauty, B2B SaaS, high-CPA regulated; brand blogs, vertical trade press linking primary, community write-ups, per the vertical overlays in `query-book.md` | H11 and the "Success stories" done row (`plan.md` line 269) need one Silver **per vertical**; the tagging rule (`shortlist.md` line 56) only labels what channel clusters happen to find. The one Silver is apparel — outside all three verticals — so the reserve-vertical trigger (`plan.md` line 170) is live and untested |
| 3 | **P4-c11 negative-result sweep** — `query-book.md` amendment 7 rows (r/SEO, r/bigseo, r/PPC negatives; HN dissent; null-result papers), plus 1–2-star G2/OMR reviews naming no lift. Done when screened, negative-found, and vendor-named counts are recorded | Survivorship is scheduled against only by counting screens (`plan.md` line 104, 281). Redteam B10 found no P4 cluster hunts failures; still none. A negative case set is what makes "1 Silver in ~150" readable |
| 4 | **P4-c12 EU-brand sweep** — set X aliases (`query-book.md` amendment 4) against C64/C65 (horizont.net, wuv.de, t3n.de, onlinemarketing.de, omr.com) | EU is primary geography (`scope.md` line 10); roster §7 records set X never run. Extension-free channels |
| 5 | **P4-c13 full-page re-grade of Pass 3** — every Bronze or better and every `screened — not opened` title in c1–c6, opened and graded per §3 rule | P4-c4 (live) covers 8–12 cases; Pass 3 screened ~150 from overview pages. Without this the scorecard's screened/cleared count mixes two grading methods |
| 6 | **P8-c1 split by vertical** — P8-c1-sk, P8-c1-bs, P8-c1-hr, same done condition as `shortlist.md` line 87 | Gate 1+3 open. 27 cells in one agent is the shape the split rule (`ORCHESTRATION.md` line 48) forbids. Needs extension for indeed/upwork/gartner (403→ext) — one holder at a time, see §5 |
| 7 | **P6-c0 published-size pull** (Sonnet, raw) then **P6 compile ×3** (Opus) — §4 | Gate open; H16 has no cluster (`shortlist.md` line 100). Compile competes for no browser or search |
| 8 | P5-c7 engine countermeasures, then P5-c3–c6 | H13 needs c7; c3–c6 are academic-channel pulls, extension-free, lower priority than Pass 4 under the user's ordering |
| wait | P3-repull-sec | Probe-gated: first action one EDGAR fetch; 403 → append `blocked` and stop |
| hold | P10-d0-copilot, rufus-p3, gemini-remainder, claude-remainder, chatgpt-retry | §2. Their browser slot lends to P8-c1 and P4-c7 |

Pass 4 needs both: more clusters (rows 1–4) and a second sweep of what Pass 3 already touched (row 5). It does not need re-cutting the six live clusters.

## 2. Pass 10 panel

| Question | Judgement | Cites |
|---|---|---|
| Hold, shrink, or continue | **Hold.** Not shrink: a smaller panel on a confounded day 0 buys nothing. Not continue: day 0 is Claude 83/160 logged-in with Memory localising every answer to Vietnam (`e-claude-panel` deviations, file header and line 871), Gemini 24/160 logged-out on Flash-Lite with a silent throttle (`e-gemini-panel` deviations), ChatGPT/AI Mode/Perplexity 0 runs. The extension is one resource and Passes 4 and 8 need it for 403→ext channels |
| Day-0 status | Recorded per engine as sampled / partial / blocked (`STATE.md` decision line 158); the hold is a **gap, not a back-fill** per `panel-protocol.md` line 157 — append one gap row to the sampling log with reason "user hold 2026-09-22" |
| Claude day-0 usability | `region_intended: US` failed for every run; HR-01 returned Vietnamese issuers 5/5. Usable only for HP3 (citation-to-mention ratio, region-insensitive) and only labelled `personalised — logged-in, Memory on`; excluded from HP1/HP2 rates. A neutral day 0 needs a logged-out private window (`STATE.md` decision line 154) |
| "Programme done — Pass 10" row (`plan.md` line 271) | Row stands unchanged; it is not satisfiable while held, and run-prompt step 8 lets a row lapse only when channels are exhausted — they are not. At Pass 9 the six panel-checkable rows (HE2, HE3, HP1–HP4) take the mark **`not produced`** (`hypotheses.md` line 82), distinct from unresolved. The done table then reads five rows satisfiable, one deferred by user decision — stated, not softened |
| Minimum panel that still scores HP1–HP4 honestly | HP1: two P1 engines, same date, same surface, 14 C prompts × n=5 = 140 runs. HP2: one engine, 14 C × n=5 on two dates ≥14 days apart (+70 runs). HP3: coded from the same records. HP4: needs a toggle both engines expose — Gemini logged-out exposes none (`e-gemini-panel` deviations); mark `unresolved — checked <engines> <date>`. Total ~210 runs ≈ 3 sampler sessions at the observed 83 runs/session. C prompts only; X and P prompts add slot-fill dependence and refusals without moving HP1–HP3 |
| `panel-protocol.md` line 179 | `predictions checked: per hypotheses.md panel-checkable set` is a placeholder. Append the six IDs and the bar of three (`hypotheses.md` line 42) |

## 3. Evidence bar and grading consistency

| Cluster | How cases were graded | Effect on the count |
|---|---|---|
| c1 (`a-vendor-census-c1` line 72) | "every case study on every customers/pricing/home page … graded on intake"; metric-less testimonials graded Fools gold (Searchable 2, Peec AI 2) | Fools gold inflated by no-claim items; nothing opened |
| c2 (Scrunch, Brandlight rows) | "11 screened, 8 graded, 3 screened-out-as-no-claim"; Brandlight "3 testimonial quotes screened … none clears Bronze" — no-claim not graded | Same items c1 would call Fools gold are excluded here |
| c3 (AirOps, Conductor rows) | "29 titles + 1 testimonial screened / 3 pulled and graded"; grades only opened pages, 26 titles unopened counted as screened | Bronze deflated; screened total inflated relative to c1 |
| c4 (BrightEdge, Quattr rows) | "5 identified / 3 opened and graded, 2 screened-not-opened"; Silver assigned on an unaffected control cohort — the summary does not state whether bar items 3, 6, 7 (date window, n, who measured and paid by outcome) were named | The one Silver lacks a visible seven-item checklist; P4-c4's done condition (`shortlist.md` line 63) requires item 7 explicit |
| c6 (Feedonomics, Pacvue rows) | Binary "cleared = names all seven" with no Bronze/Fools gold grade at all; "22 screened, 0 cleared" | Not comparable with c1–c4 grades |

Three operationalisations of one bar (`plan.md` lines 83–104). The "~150 screened, 1 Silver" aggregate is therefore a mixed count. One-line rule for every P4 brief and the P4-c13 re-grade:

> **A grade is assigned only from the case's own full page with the seven bar items ticked one by one in the raw file; a case not opened is `screened — not opened`, a page with no metric is `screened — no claim`, neither is graded, and a case missing any of items 1–7 is Bronze at best.**

## 4. Gates and compile tasks to push

| Pass | Gate (`plan.md` lines 184–189) | Status 2026-09-22 | Push now |
|---|---|---|---|
| 6 markets | 2, 3 | **open** — both done (`STATE.md` lines 72, 82) | P6-c0 (Sonnet, raw: every published sub-market size, labelled forecast/measured, for H16); then P6-organic → `markets/organic-recommendation.md`, P6-paid → `markets/paid-placement.md`, P6-agentic → `markets/agentic-commerce.md` (Opus, 120 lines each, four structural checks each) |
| 7 competitors | 3, 4 | blocked — Pass 4 live | Pre-stage rows, spawn when Pass 4 lands: P7-INDEX; P7-organic-a (roster 1–8), P7-organic-b (9–13 + Scrunch), P7-incumbent-a (c3 six), P7-incumbent-b (c4 five + four cleared held), P7-agency (c5 five), P7-sellside (c6 seven) — 80 lines per profile |
| 8 customers | 1, 3 | **open** for the raw sweep; compile waits on it | P8-c1-sk / -bs / -hr (Sonnet, raw, §1 row 6); then P8-skincare, P8-b2b-saas, P8-high-cpa (Opus, 100 lines, nine cells each) as each sweep lands |
| 9 findings | 5, 6, 7, 8 | blocked | none |
| 10 analysis | day-0 data | held with the panel | none; `findings/panel-read.md` waits for a neutral day 0 |
| 11 transition | 9, 10 | blocked; Pass 10 hold makes this gate unsatisfiable as written | Append to `plan.md`: gate reads "9, and 10 or its recorded hold" — descriptive compile from Pass 4 cases does not need panel data |

Slot picture once the nine live agents land: Pass 4 second sweep 5–6, P8 raw 3, P6 4 — thirteen tasks for ten slots; the order in §1 resolves it.

## 5. Risks to schedule against now

| Risk | One mitigation |
|---|---|
| WebSearch exhausted (`STATE.md` decision line 160) | Every brief carries its cluster's seed URLs from `query-book.md` and the substitute endpoints (DuckDuckGo HTML, EDGAR full-text, HN Algolia); every 403 from a substitute is logged in the raw pull notes; a name with no URL in the same row is cut at verify |
| sec.gov 403 (`STATE.md` unknowns lines 176–177) | P3-repull-sec is probe-gated (§1); meanwhile filings enter only as IR-site copies (tier 3, as c3 did) or aggregator relays labelled tier 5, never as tier 2 |
| Browser instability | A `browser` column in `STATE.md` Live agents: `ext`, `playwright`, `none`. One `ext` holder and one `playwright` holder at a time; every other agent uses fetch and writes browser-needing URLs to a `browser backlog` list in its summary for a follow-up task |
| Rate limits (three 429 kills, decision line 152) | Spawn only on completion notifications (`ORCHESTRATION.md` rule 2); no burst above the count that landed last; every raw file written on completion of its pull, so a killed agent's partial cluster is a landed partial, and the successor's brief lists the files already written |
| File collision at 10 writers | P4-c1–c5 all write `docs/raw/e-case-*` (`STATE.md` lines 15–20). Filenames carry the cluster id: `e-case-c<N>-<slug>-<date>.md`; scheduler checks glob disjointness before every spawn |
| STATE.md append races | Agents append their landing block with a single shell append of a pre-written file, never with an edit tool that reads-modifies-writes; block ≤12 lines; the main thread is the only editor of every other section |
| Memory-sourced names under budget pressure | Brief line: "If a channel yields nothing, record `unknown — checked`; never substitute a name you remember." Verify step 4b adds: every vendor, brand, or paper named in a raw file carries the URL it was found at in the same file. The roster's 70 held names (`a-vendor-roster` §3) are the sanctioned seed pool |

## 6. Landed evidence that changes plan assumptions

| Assumption | Evidence, raw path | Append where |
|---|---|---|
| Engine matrix Claude row "Does it carry commercial recommendation at all" (`plan.md` line 113) | Lane B answered at tier 3: "Claude will remain ad-free … nor will Claude's responses … include third-party product placements", 2026-02-04 — `b-anthropic-perplexity-platform-summary-2026-09-22.md` table 1. Lanes A and C still open (no merchant program found) | `plan.md` engine matrix, dated "evidence notes 1" |
| Engine matrix Perplexity "earliest mover on sponsored answers" (line 115) | No live ad product or advertiser page; merchant-terms page 404; 2024-11-12 launch post still live — same summary, table 1–2. Status is by absence | same append |
| Engine matrix / protocol slug "Amazon Rufus" (line 117; `panel-protocol.md` lines 29, 141) | Renamed "Alexa for Shopping" 2026-05-13; both names still on one page — `b-microsoft-amazon-platform-summary-2026-09-22.md` naming table | `plan.md` append; `panel-protocol.md` status note carries both names |
| Structural check "Regulatory" (line 49) | ChatGPT designated VLOSE 2026-08-31, 159.1M EU users, no Art. 39 repository yet; no repository distinguishes an ad inside an AI answer — `b-eu-dsa-ad-repositories-table-2026-09-22.md`. EU AI Act Art. 50 in force 2026-08-02 — `b-regulators-ad-disclosure-table-2026-09-22.md` | `plan.md` structural-checks append: regulatory row names designation status per engine |
| Structural check "Incumbent bundling" (line 48) asks price delta only | Semrush a wholly owned Adobe subsidiary from 2026-04-28 (8-K); Scrunch acquired by Sitecore 2026-06-03 — `a-vendor-census-c4` row 4, `a-vendor-census-c2` row 1 | `plan.md` append: check also asks "acquired by whom, when" |
| Google surfaces as two rows (line 114; `panel-protocol.md` lines 25–26) | P2-c4 landed `a-google-search-io2026-naming-2026-09-22.md` (STATE line 84; not read here); redteam B12 records a 2026-05-19 merged-surface announcement | `panel-protocol.md` status note: sampler records the surface name as shown; no matrix edit until the naming pull is read |
| Verticals: reserve trigger "no Gold or Silver from the anchor set" (line 170) | The single Silver is apparel (Men's Wearhouse) — none of the three verticals; per-vertical counts do not exist for Pass 3 because the tagging rule post-dates it | No append yet; §1 rows 2 and 5 produce the per-vertical count the trigger needs |
| Sub-market "agentic commerce" sell-side | Roster §6: "this sub-market thin"; c6: 7 rostered, none clears the bar; protocols table: ACP fully published, AP2 to FIDO 2026-04-28, fee clauses unknown across all five | No append; H8/H9 evidence exists at floor, Pass 9 scores |
| Hypotheses at floor, not scored here | H2/HE1: self-serve Ads Manager, tier 3 (`b-openai-platform-summary`); H15: 0 of 14 vendors disclose a prompt set (c1 0/8, c2 0/6); H1: Adobe "AI Conversion Now 42% Higher" Mar 2026, 54% May 2026, tier 4, comparator "non-AI visits" not organic search (`c-retail-analytics-table`) | `hypotheses.md` log row only (§7); register frozen |
| `scope.md` | Nothing landed contradicts the brief, revisions, or the three-way split | none |

## 7. Verdict per document — paste-ready appends

| File | Verdict | Append (dated 2026-09-22, below the last section) |
|---|---|---|
| `plan.md` | **amend, 6 appends** | (a) `### Orchestration — cap revision 1, 2026-09-22`: "Cap 10 live agents machine-wide per user 2026-09-22 22:30, superseding line 244. One browser-extension holder and one Playwright holder at a time. Spawn on completion notifications only. Deliverable globs disjoint per spawn." (b) `### Pass 4 — second sweep, 2026-09-22`: rows P4-c7–c13 as in §1 with the done conditions there; "Pass 4 is done when the six channel clusters and the seven sweep clusters have landed and per-vertical screened/cleared counts exist for all three verticals." (c) `### Evidence bar — grading rule 1, 2026-09-22`: the §3 one-liner verbatim. (d) `### Engine matrix — evidence notes 1, 2026-09-22`: the four §6 rows (Claude, Perplexity, Amazon naming, ChatGPT VLOSE) with their raw paths. (e) `### Structural checks — addition 1, 2026-09-22`: "Incumbent bundling also records: acquired by whom, on what date, per filing." (f) `### Pass 10 and Pass 11 — hold note, 2026-09-22`: "Pass 10 sampling held by user decision 2026-09-22 22:40; day 0 recorded per engine; done-row unchanged; HE2, HE3, HP1–HP4 marked `not produced` at Pass 9 if still held. Pass 11 gate reads: 9, and 10 or its recorded hold." |
| `ORCHESTRATION.md` | **amend, 1 append** | `## Concurrency cap — revised by the user 2026-09-22`: "10 live agents machine-wide, main thread not counted, subagents counted. The 2026-09-17 reasoning (one browser, one Docker daemon) still binds the browser: one extension holder and one Playwright holder at a time. Scheduler rules 1–6 stand with 3 read as 10. Agents append to `STATE.md` by shell append of a pre-written block, never by read-modify-write. Wave plan remains dormant." |
| `panel-protocol.md` | **amend, 1 append; prompt set v1 untouched** | `## Status note 1 — 2026-09-22`: "Sampling held by user decision 2026-09-22 22:40; hold recorded as gap rows, never back-filled. Day 0: Claude 83/163 logged-in with Memory on — every run labelled `personalised`, excluded from HP1/HP2 rates, usable for HP3 only; Gemini 24/160 logged-out, model `Flash-Lite`, toggle `not exposed` — toggle arm counts as not-sampled for HP4; ChatGPT, AI Mode, Perplexity blocked, 0 runs. On resumption: logged-out private window first for every engine; the Amazon row carries both names `Rufus / Alexa for Shopping` as the surface shows; the Google rows record the surface name as displayed. Minimum panel to score HP1–HP3: two P1 engines × 14 C prompts × n=5 on one date, one engine repeated on a second date. Predictions checked (line 179): HE2, HE3, HP1, HP2, HP3, HP4 against a bar of three." |
| `shortlist.md` | **amend, 3 appends** | (a) `## Pass 4 — second sweep, added 2026-09-22`: cluster rows P4-c7–c13 in the file's own column format (id, lane E/F, target, pulls, tier, moves H3/H6/H10/H11, done when — from §1). (b) `## Pass 8 — split, 2026-09-22`: P8-c1-sk, -bs, -hr, each nine cells, same pulls and done condition. (c) `## Pass 6 — pull, 2026-09-22`: P6-c0, lane E, every published sub-market size with author label forecast/measured, tier 3–5, moves H16, done when each size carries base period and label. Cluster count line: 32 → 42 |
| `hypotheses.md` | **keep; 1 log row** | `| 2026-09-22 | HE2, HE3, HP1–HP4 | Producing pass 10 held by user decision 2026-09-22 22:40. If unsampled at Pass 9, mark not produced. No post-hoc row added |` |
| `run-prompt.md` | **amend, 1 append** (not in the brief's five; blocks the scheduler otherwise) | `## Revision 1 — 2026-09-22`: "Hard rule 'never more than 3' reads 10. Loop step 3 'live agents < 3' reads 10. Loop step 5 'never skip a sampling date' is suspended while the user's Pass 10 hold stands; gaps are recorded. AGENT BRIEF adds: cluster id in every filename; browser column value; `unknown — checked` over any remembered name; landing block by shell append." |
| `demand-signals.md`, `scope.md`, `trust-rubric.md` | keep | none |

## Caveats

- One reviewer, one reading, 2026-09-22, of summaries only — no raw case file behind any census was opened, so §3 judges grading *as reported*, not the grades themselves. The Silver may hold all seven items on its own page.
- Live agents' outputs (P4-c1–c6, P5-c1–c2, the AI Mode retry) were not read; §1 assumes the six live clusters land as briefed.
- Slot counts in §1 and §4 are orderings, not a schedule; no row carries a date, and nothing here is a verdict on the market or on any vendor.
- `a-google-search-io2026-naming-2026-09-22.md` is cited by its STATE.md landing row and was not read; the Google-surface note in §6 rests on the redteam file, a method document.
- The minimum panel in §2 is a method floor for three hypotheses, not an endorsement of resuming; the user's stance stands until the user changes it.

# Pre-registered hypotheses

Registered 2026-09-22, Pass 0, per `plan.md` "Pass 0 additions". Pass 9 scores every row against `docs/raw/`; a second agent reviews the scoring adversarially (`plan.md` orchestration). Terms are `glossary.md`'s. Tiers are `trust-rubric.md`'s. Grades (Gold, Silver, Bronze, Fools gold) are the `plan.md` evidence bar's.

These are claims to test, not beliefs. Nothing here asserts a market fact, and no row is argued for or against. Thresholds in HP1–HP4 are pre-registered method choices set 2026-09-22 with no evidence behind them: they fix the bar, they do not predict where it falls.

## Registration rule

- Registered before any pull. A row may **not** be edited after registration — not its claim, not its conditions, not its pass. The only permitted change is an appended dated note in the log below.
- A hypothesis first written after a pull is appended with its own date and marked **post-hoc**. Post-hoc rows are scored like any other but never counted toward the `plan.md` "three pre-registered predictions checked against the panel" condition.
- H1–H5: claim text and the "kills it" condition are verbatim from `plan.md`. The "confirms it" condition, the tier floors, the lane and the pass are added here at registration.
- Status in the register is the registration-time status and is frozen at `unresolved`. Pass 9 writes scores into `findings/`, not into this column.

## Register

| ID | Claim | Lane | Sub-market | Pass | Panel | Status |
|---|---|---|---|---|---|---|
| H1 | Referral from AI assistants converts above organic search | E | cross | 2, 8 | no | unresolved |
| H2 | Paid inventory inside AI surfaces exists at scale as of 2026-09 | B | paid | 2 | no | unresolved |
| H3 | At least one vendor demonstrates causal lift | E | cross | 4 | no | unresolved |
| H4 | Demand is attention-only in every SMB cell | F | cross | 8 | no | unresolved |
| H5 | Corpus seeding measurably moves an answer | D | organic | 5 | no | unresolved |
| H6 | A brand action on a property it controls precedes a measured visibility change on a P1 engine | A | organic | 4, 10 | no | unresolved |
| H7 | Organic carries spend signals in more segment cells than paid or agentic commerce | A | organic | 8 | no | unresolved |
| H8 | At least one agentic-commerce protocol is published fully enough to implement without a contract | C | agentic | 2 | no | unresolved |
| H9 | Within agentic commerce, spend signals sit in enterprise cells and are absent from SMB cells | C | agentic | 8 | no | unresolved |
| H10 | Brands that moved name org or content-ops changes more often than paid-media changes | F | cross | 11 | no | unresolved |
| H11 | Transition evidence at tier 3 or better exists for at least one brand in each vertical | F | cross | 4, 11 | no | unresolved |
| H12 | Where paid inventory exists, its price is disclosed publicly rather than only under contract | B | paid | 2, 3 | no | unresolved |
| H13 | At least one P1 engine publishes a countermeasure naming a technique documented in Pass 5 | D | organic | 5 | no | unresolved |
| H14 | Manipulation evidence is denser in the high-CPA regulated vertical than in the anchor vertical | D | cross | 5 | no | unresolved |
| H15 | Vendors publishing a composite visibility score disclose the prompt set behind it | E | organic | 3 | no | unresolved |
| H16 | Every published sub-market size available is a forecast rather than a measurement | E | cross | 6 | no | unresolved |
| HE1 | Engine matrix P1 "ChatGPT — OpenAI": a paid placement product is live and documented on the engine's own surface as of the pull date | B | paid | 2 | no | unresolved |
| HE2 | Engine matrix P1 "Claude — Anthropic": the consumer chat surface returns brand-level recommendations to buying-shaped prompts | A | organic | 10 | **yes** | unresolved |
| HE3 | Engine matrix P1 "Google — AI Overviews, AI Mode, Gemini": ad-labelled formats render inside AI surfaces for the panel's prompt set | B | paid | 2, 10 | **yes** | unresolved |
| HP1 | Recommendation rate for the fixed prompt set differs across P1 engines by more than the within-engine spread across repeats | A | organic | 10 | **yes** | unresolved |
| HP2 | The recommended brand set for a fixed prompt is unstable between consecutive sampling dates | A | organic | 10 | **yes** | unresolved |
| HP3 | A brand mentioned in an answer is cited in fewer than half the runs where it is mentioned | E | organic | 10 | **yes** | unresolved |
| HP4 | Citation rate is higher with the engine's web-search tool on than off, same prompt set, engine, surface and date | E | organic | 10 | **yes** | unresolved |

Coverage at registration: lane A — H6, H7, HE2, HP1, HP2; B — H2, H12, HE1, HE3; C — H8, H9; D — H5, H13, H14; E — H1, H3, H15, H16, HP3, HP4; F — H4, H10, H11. Each sub-market carries at least two rows. P1 engine open questions: HE1, HE2, HE3. Panel-checkable: six, against a bar of three.

## Decision conditions

Evidence kind first, minimum tier second. A condition is met only by evidence at or above its tier floor, filed in `docs/raw/` with its tier line.

| ID | Confirms it | Kills it |
|---|---|---|
| H1 | Panel or clickstream, conversion by referrer, tier 4 | Any tier-4-or-better panel showing parity or worse |
| H2 | Platform primary — self-serve or IO ad product, tier 3, ≥1 P1 engine | No P1 engine with a self-serve or IO-based product |
| H3 | One Gold case clearing all seven bar items, tier 5 | Zero Gold cases after Pass 4 screen |
| H4 | All 9 SMB cells checked, every one reads attention or none | Any SMB cell with a spend signal |
| H5 | Before-and-after with prompt set and n published, tier 4 | No Pass 5 technique with published before-and-after |
| H6 | Silver-or-better case tier 5, or panel tier 1; action dated before change | Passes 4 and 10 yield zero dated action-then-change pairs, channels recorded |
| H7 | All 27 cells checked; organic spend-cell count exceeds each other sub-market | Either other sub-market ties or exceeds organic, all cells checked |
| H8 | Platform primary spec, tier 3, publicly readable, no access gate | Every protocol found at tier 3 is contract- or partner-gated |
| H9 | ≥1 enterprise agentic cell reads spend, no SMB agentic cell does, all 6 checked | Any SMB agentic cell reads spend, or no agentic cell reads spend |
| H10 | Cited cases naming org or content-ops change outnumber paid-media ones, each tier 3 | Paid-media changes equal or outnumber them across the same case set |
| H11 | Three cases, one per vertical, tier 3, each naming the change | Any vertical with zero tier-3 transition cases, channels recorded |
| H12 | Platform primary rate card or pricing page, tier 3, ≥1 P1 engine | Every P1 engine with an ad product discloses no price at tier 3 |
| H13 | Platform primary policy or changelog naming the technique, tier 3 | No P1 engine document at tier 3 names any Pass 5 technique |
| H14 | Cleared-case count higher for regulated at equal screen effort, tier 4 per case | Anchor vertical equals or exceeds it at equal screen effort |
| H15 | Majority of censused vendors disclose prompt set and n, tier 3 | Majority publish a composite with prompt set undisclosed, tier 3 |
| H16 | Every size found is author-labelled forecast or has a future base period, tier 3 | One size at tier 3 measured over a closed historical window |
| HE1 | Platform primary — ad doc, pricing, or merchant terms, tier 3 | Engine's own docs state no ad product, or all channels return none, tier 3 |
| HE2 | Panel, tier 1: ≥1 recommendation per `glossary.md` across the prompt set | Zero recommendations across the full prompt set at protocol n, tier 1 |
| HE3 | Panel capture tier 1, plus platform primary format doc tier 3 | Zero ad-labelled units across the prompt set tier 1, no format doc tier 3 |
| HP1 | Panel tier 1: largest between-engine gap exceeds largest within-engine range, same date and surface | Every between-engine gap sits inside the within-engine range |
| HP2 | Panel tier 1: churn (symmetric difference ÷ union) above 0.30 for a majority of prompts | Churn at or below 0.30 for a majority of prompts |
| HP3 | Panel tier 1: citation-to-mention ratio below 0.50 pooled across the prompt set | Ratio at or above 0.50 pooled across the prompt set |
| HP4 | Panel tier 1: on exceeds off for a majority of prompts across ≥2 sampling dates | Off equals or exceeds on for a majority across ≥2 sampling dates |

## Scoring rule — Pass 9

| Mark | When |
|---|---|
| **confirmed** | Producing pass ran; confirm condition met by `raw/` evidence at or above its tier floor |
| **killed** | Producing pass ran; kill condition met at or above its tier floor |
| **unresolved — checked \<channels\> \<date\>** | Producing pass ran, neither condition met. Channels named. Never left blank |
| **unresolved — contested** | Both conditions met by different evidence. See below |
| **not produced** | The producing pass did not run. Distinct from unresolved, and stated as such |

- Both sides present: both rows are cited **side by side, attributed, never averaged** (root `CLAUDE.md`). No majority vote, no tie-break by tier, no split score. The higher-tier row is noted as higher-tier and still does not overrule the other. The mark is `unresolved — contested`.
- Evidence below a condition's tier floor does not meet it. It is cited with its tier and the shortfall named.
- A hypothesis is scored against `raw/` only — never against a compiled file, never against its own plausibility.
- One score per hypothesis. No partial confirmation, no percentage, no "directionally confirmed".
- `confirmed` for HE2, HE3 and HP1–HP4 requires the sample behind it to name prompt-set version, engine, surface, model version, region and n, per `plan.md` Pass 10.
- The score and its evidence rows live in `findings/`. This file records only an appended note pointing at them.

## Log — appended only, dated

| Date | ID | Note |
|---|---|---|
| 2026-09-22 | — | Registered. 23 hypotheses, 6 panel-checkable, all `unresolved` |
| 2026-09-22 | HE2, HE3, HP1–HP4 | Producing pass 10 held by user decision 2026-09-22 22:40. If unsampled at Pass 9, mark not produced. No post-hoc row added |

## Caveats

- Kill conditions resting on absence ("no P1 engine…", "zero cases…") are only as strong as the channels checked. Pass 9 records the channel list beside every such mark; an absence with no channel list is not a kill.
- H4, H7 and H9 are scored off the Pass 8 matrix and inherit every bias in `demand-signals.md`.
- H14's "equal screen effort" is not measurable to a fine grain. Pass 5 records the screened count per vertical so the comparison is stated rather than assumed.
- HP2's 0.30 and HP3's 0.50 are arbitrary pre-registered cut points, fixed so the result cannot be fitted afterwards — not because either number is known to be meaningful.
- Six panel-checkable rows are registered against a bar of three because panel samples can fail for reasons unrelated to the claim: surface change, access loss, prompt-set revision.
- This file carries claims to test. No market facts, no vendor names, no numbers about the market.

## Additions 2026-09-23

Registered 2026-09-23 by AMEND-2 for Passes 12, 13 and 14, per `plan.md` "Pass sequence — additions 2026-09-23" and `STATE.md` §Decisions taken lines 175, 177, 178. As read at registration, no `docs/raw/*-2026-09-23.md` file exists. Terms, tiers, decision-condition format and the Pass 9 scoring rule above apply unchanged; tier floors sit inside each condition, as in the table above.

Registration status: these rows are written after Passes 2–9 pulled, so they are **post-hoc** relative to that evidence (registration rule, line 10) and pre-registered relative to Passes 12–14. Wording avoids conditions already met in `raw/`: OpenAI's advertiser and revenue statements and its CPC bid guidance (`markets/paid-placement.md` lines 25, 34, 74) confirm none of H17–H20 alone. No row counts toward the Pass 10 bar of three; Pass 10 is skipped.

### Register — additions

| ID | Claim | Lane | Sub-market | Pass | Panel | Status |
|---|---|---|---|---|---|---|
| H17 | An engine other than ChatGPT discloses an advertiser count or ad revenue for its AI-answer surfaces | B | paid | 12 | no | unresolved |
| H18 | At least one engine or third-party network publishes a rate card for an AI-answer ad unit | B | paid | 12 | no | unresolved |
| H19 | A party outside an engine's own ad program sells placement inside that engine's answers | B | paid | 12 | no | unresolved |
| H20 | An advertiser or agency reports a controlled result from AI-assistant ads, with n and window | E | paid | 12 | no | unresolved |
| H21 | Every P1 engine has two or more dated user-count statements at tier 3 | E | cross | 13 | no | unresolved |
| H22 | In every sub-market with two or more forecasts for one target year, highest exceeds lowest by more than 3× | E | cross | 13 | no | unresolved |
| H23 | A peer-reviewed paper with code describes a technique that steers LLM recommendation, and no P1 engine names a countermeasure to it | D | organic | 14 | no | unresolved |
| H24 | A paper describes a monetisation mechanism inside LLM answers that no P1 engine offers | D | paid | 14 | no | unresolved |
| H25 | At least one capability kept by Pass 14 runs on public code and public models, with no engine partnership | D | cross | 14 | no | unresolved |

Coverage: lane B — H17, H18, H19; D — H23, H24, H25; E — H20, H21, H22. H25 is the builder-constraint row (`findings/whitespace.md` line 52), read descriptively.

### Decision conditions — additions

| ID | Confirms it | Kills it |
|---|---|---|
| H17 | Engine statement or filing, tier 3 or 2: numeric advertiser count or revenue scoped to AI surfaces | Every engine other than ChatGPT with a live product states neither at tier 3, channels recorded |
| H18 | Engine or network pricing page, tier 3: a price per unit charged, not a bid recommendation | Every engine and network found publishes no price schedule at tier 3, channels recorded |
| H19 | Seller's own page, tier 3, offering placement in a named engine's answers outside that engine's ad program | Every seller found resells engine inventory or places only in third-party apps, tier 3, channels recorded |
| H20 | Case with holdout, geo-split, switchback, or pre/post with control; n and window stated; tier 5; Silver or better under `grade_rule1` | Zero such cases after the Pass 12 screen, screened count recorded |
| H21 | Two dated tier-3 user-count statements per P1 engine, metric as the engine names it; for Google, any of AI Overviews, AI Mode, Gemini, surface named | Any P1 engine with fewer than two after its newsroom, IR and filings are checked |
| H22 | Highest ÷ lowest above 3 in every sub-market with ≥2 same-target-year forecasts, each forecast recorded at its own tier | Highest ÷ lowest at or below 3 in any such sub-market |
| H23 | Peer-reviewed paper with code or data, tier 3; P1 countermeasure documents checked, none names the technique, tier 3 | Every such technique named in a P1 engine countermeasure document, tier 3 |
| H24 | Paper, tier 4 or better, describing the mechanism; P1 ad documents, tier 3, show no product using it | Every mechanism found matches a live P1 ad product, tier 3 |
| H25 | Kept paper, tier 4 or better, with public code and open weights or a public API, no partner gate | Every kept paper's code is absent or needs gated engine access |

### Log — additions

| Date | ID | Note |
|---|---|---|
| 2026-09-23 | H17–H25 | Registered. 9 rows, all `unresolved`; producing passes 12, 13, 14; none panel-checkable |
| 2026-09-23 | HE2, HE3, HP1–HP4 | Pass 10 skipped by owner 2026-09-23 (`STATE.md` line 174). Rows stay `not produced`; day-0 gap recorded, never back-filled. No row replaces them |

### Caveats — additions

- H17, H18, H19 and H24 kill on absence; each kill is only as strong as its channel list, per the first caveat above.
- H22's 3× is an arbitrary pre-registered cut point. With fewer than two same-target-year forecasts in any sub-market the row reads `unresolved`, not killed.
- H21 depends on engines publishing user counts at all; a count published only by a panel is tier 4 and does not meet it.
- H25 confirmed or killed says nothing on whether any party can win a market; that verdict is the user's (`MegaPlan.md` line 17).
- These rows carry claims to test. No market facts; the paid-placement line references above only fix wording.

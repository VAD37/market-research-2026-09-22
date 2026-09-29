# AI Ads & AI Visibility: a desk-research programme

Can brands pay or work their way into AI assistant answers, and does it pay back? Evidence from 1,000+ public sources, gathered by a team of Claude Code agents.

| | |
|---|---|
| Question | Is there real demand for brand visibility inside AI answers? |
| Method | Internet-only desk research, 2026-09-22 → 2026-09-24 |
| Output | Briefs, 11 PDF decks, findings, market and competitor files |
| Stance | Evidence only; no go/no-go verdict (`MegaPlan.md` §Non-goals) |

## Start here

| Report | What it is |
|---|---|
| [Executive brief](docs/findings/executive-brief-2026-09-23-r2.md) | Two-page answer. Read this first. |
| [Director brief](docs/findings/director-brief-2026-09-23-r2.md) · [.pptx](docs/findings/director-brief-2026-09-23-r2.pptx) | Long form, every number with its source |

**PDF decks: the brief bake-off.** The same fact pack, written up by 11 different report-writing methods, one deck each. Not ranked.

| Deck | Writing method |
|---|---|
| [R0 Baseline](docs/findings/deck-R0-baseline-2026-09-24.pdf) | Control: the owner's own template |
| [R0b Baseline repeat](docs/findings/deck-R0b-baseline-repeat-2026-09-24.pdf) | Control rerun, measures run-to-run variance |
| [R1 Pyramid Principle](docs/findings/deck-R1-pyramid-principle-2026-09-24.pdf) | tyroneross/pyramid-principle: core, long-form, source-integrity skills |
| [R2 Minto Pyramid](docs/findings/deck-R2-minto-pyramid-2026-09-24.pdf) | millwright-labs/minto-pyramid-skill |
| [R3 Strategy communicator](docs/findings/deck-R3-strategy-communicator-2026-09-24.pdf) | strategyu-skills: strategy-communicator |
| [R4 Structure & synthesize](docs/findings/deck-R4-structure-synthesize-2026-09-24.pdf) | strategyu-skills: structure-synthesize |
| [R5 Knowledge synthesis](docs/findings/deck-R5-knowledge-synthesis-2026-09-24.pdf) | awesome-claude-corporate-skills: knowledge-synthesis |
| [R6 Deliverable creation](docs/findings/deck-R6-deliverable-creation-2026-09-24.pdf) | business-consulting: deliverable-creation |
| [R7 Decision memo](docs/findings/deck-R7-decision-memo-2026-09-24.pdf) | strategy-skills-for-claude: decision-memo |
| [R8 Assumption audit](docs/findings/deck-R8-assumption-audit-2026-09-24.pdf) | strategy-skills-for-claude: assumption-audit |
| [R9 MBB extract](docs/findings/deck-R9-mbb-extract-2026-09-24.pdf) | management-consultant-B1: SCQA, board communication references |

Method sources, commits and licences: [brief bake-off README](docs/method/brief-bakeoff/README.md).

**Findings, one question each**

| File | Answers |
|---|---|
| [demand-map](docs/findings/demand-map.md) | Which of 27 segment cells show real demand? |
| [proof-scorecard](docs/findings/proof-scorecard.md) | What do published success stories actually prove? |
| [ai-ads-evidence](docs/findings/ai-ads-evidence.md) | Who sells AI-answer ads, at what price, with what result? |
| [market-potential](docs/findings/market-potential.md) | User counts, forecasts and floors per sub-market |
| [transition-evidence](docs/findings/transition-evidence.md) | What did brands that moved actually change? |
| [trigger-timeline](docs/findings/trigger-timeline.md) | Which dated events support a "why now"? |
| [whitespace](docs/findings/whitespace.md) | Where does the evidence show nothing at all? |
| [frontier-scan](docs/findings/frontier-scan.md) | What capabilities in the literature could be abused or monetised? |
| [geo-aeo-roles](docs/findings/geo-aeo-roles.md) | What GEO/AEO jobs exist, what they pay |
| [unknowns](docs/findings/unknowns.md) | Hypotheses scored; what is still unknown |

**Supporting files.** Markets: [organic](docs/markets/organic-recommendation.md) · [paid](docs/markets/paid-placement.md) · [agentic](docs/markets/agentic-commerce.md). Competitors: [INDEX](docs/competitors/INDEX.md) (43 profiles). Customers: [skincare](docs/customers/skincare-beauty.md) · [B2B SaaS](docs/customers/b2b-saas.md) · [high-CPA regulated](docs/customers/high-cpa-regulated.md) · [local](docs/customers/local-multi-location.md).

## The question

The owner asked one thing: "Let's dig into AI ads." AI assistants now decide which product a user hears about. Three markets grew around that: organic recommendation (GEO/AEO), paid placement inside answers, and agentic checkout. The market is about two years old, loud with vendor claims, and has no audited numbers. The job was to separate what is proven from what is claimed, without interviews or ad spend.

## How it worked

```
sources/  →  raw/  →  markets/ competitors/ customers/  →  findings/  →  briefs, decks
 what to     verbatim,        compiled per topic            cross-market     for readers
 pull        dated, graded
```

- Every source graded tier 1 (strongest) to 7 ([trust rubric](docs/method/trust-rubric.md)).
- 32 hypotheses pre-registered, each with the evidence that would kill it ([hypotheses](docs/method/hypotheses.md)).
- Up to 7 subagents pulled in parallel; the main thread verified and committed ([run log](docs/method/STATE.md)).
- Nothing from memory. Missing data reads `unknown — checked <channel> <date>`.

## Key findings (as of 2026-09, from the [executive brief](docs/findings/executive-brief-2026-09-23-r2.md))

- **Demand is thin and early.** 8 of 27 segment cells show a spend signal, mostly enterprise organic, nearly all from job postings. No buyer discloses a price paid.
- **Paid AI ads are live** on ChatGPT, Google AI Overviews, Copilot and Amazon Rufus. OpenAI states a "$1 billion" run rate (company-stated). 0 of 8 ad products publish a rate card.
- **No proof of sales lift.** 0 Gold cases out of ~2,620 screened. All 7 positive Silvers are tier 5 (vendor-reported). 19 documents at tier ≤3 show declines or null effects.
- **Brands that moved changed content and tooling, not media.** Of 108 cases: content 63, tooling 58, paid media 2.
- **No sub-market has a measured size.** Forecasts disagree by 1.92× (organic) to 26.3× (agentic).

## Scale and cost

| Measure | Value |
|---|---|
| Raw sources | 1,045 pulls + 83 images; 3,399 URLs, 516 domains |
| Screened | ~2,620 success-story items; 252 papers (38 kept) |
| Compiled | 43 competitor profiles; 26 of 32 hypotheses scored |
| Agent work | 112 subagent transcripts; 90 operator prompts; 264+ commits |
| Cost | $576.84 API list-price equivalent (ccusage) |

Cost covers this repo's sessions, 24 of 28 matched, 2026-09-22 → 2026-09-29: Fable 5.1 $312.39, Opus 5.5 $220.26, Sonnet 5 $37.78, others $6.42. Tokens: 931.0M cache read, 33.0M cache write, 2.96M output, 55K input. It ran on a subscription; this is not an invoice.

## Repo layout

```
MegaPlan.md, CLAUDE.md   charter; rules every agent follows
docs/
  method/       scope, plan, trust rubric, templates, run log
  sources/      channels and shortlist
  raw/          verbatim pulls, one per source, dated
  markets/      sizing per sub-market
  competitors/  43 profiles + INDEX.md
  customers/    demand per vertical
  findings/     briefs, findings, decks
```

## Caveats

- Desk research only: no interviews, no ad spend, no own measurement panel.
- Only 44% of key claims rest on tier 3 or better, against an 80% target.
- Survivorship bias: published cases are winners; self-reported numbers are unaudited.
- Blocked channels (live Reddit, Indeed, Gartner, Forrester, Crunchbase Pro) leave cells `unknown` ([list](docs/method/blocked-channels.md)).
- Time-bound: everything is as of 2026-09.
- Mixed models: Fable, then Opus/Sonnet after a rate limit on 2026-09-23.
- `docs/raw/` holds third-party text under its original copyright, kept for research citation.

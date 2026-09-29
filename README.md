# AI Ads & AI Visibility — a desk-research programme

**One question: "Let's dig into AI ads."** Can a brand pay, or work, its way into the answers of ChatGPT, Gemini, Claude, Copilot and Perplexity? Does anyone actually buy that today, and does it pay back?

A team of Claude Code agents answered that question by desk research alone, 2026-09-22 → 2026-09-24. They pulled over 1,000 public sources, graded every one for trust, and compiled them into ranked tables, market files, competitor profiles and a two-page executive brief. Every number in the output traces back to a saved source file.

This repo is **research only**. It produces evidence, not a go/no-go verdict, a business plan or a product (`MegaPlan.md` §Non-goals).

---

## 1. Challenge

AI assistants are starting to decide which product a user hears about. As of 2026-09 ChatGPT reports ">1 billion" weekly users and Google AI Overviews 2.5B monthly users (company-stated, `docs/findings/market-potential.md`). Three new markets have grown around that:

| Sub-market | Also called | What is sold | Buyer |
|---|---|---|---|
| Organic recommendation | GEO, AEO, "AI visibility" | Getting a brand mentioned in AI answers | Brand marketing, SEO owner |
| Paid placement | AI ads, sponsored answers | Ad slots inside AI answers | Media buyer |
| Transaction rails | Agentic commerce | The AI agent completes the purchase | E-commerce, payments |

The market is about two years old, full of vendor hype, and has no audited numbers. The challenge was to separate **what is proven** from **what is claimed** for each sub-market, segment and AI engine, without interviews and without spending money on ads.

What the research had to answer (`docs/method/plan.md`):

1. Which customer segments show real demand (spend, not just attention)?
2. What evidence shows it works, i.e. a measured sales lift?
3. What ad inventory exists inside AI answers, at what price?
4. Who sells here, how big is it, and what is still unknown?

## 2. Action

### How the research ran

```
sources/  →  raw/  →  markets/ competitors/ customers/  →  findings/
 decide       pull        compile per topic                 cross-market read
 what to      verbatim,
 pull         dated
```

- **Rules first.** A trust rubric grades every source from tier 1 (strongest) to 7 (`docs/method/trust-rubric.md`). An evidence bar grades each success story Gold, Silver, Bronze or "Fools gold". Before any data was pulled, 32 hypotheses were pre-registered, each with the evidence that would kill it (`docs/method/hypotheses.md`).
- **Agents pull, the main thread compiles.** One main Claude session scheduled the work. Subagents (up to 7 at once) each took one cluster of sources, saved every page verbatim into `docs/raw/` with its URL and pull date, and wrote a census file. The main thread verified each landing and committed it.
- **Nothing from memory.** Every compiled claim cites a raw file. Missing data is written as `unknown — checked <channel> <date>`, never guessed. Conflicting figures sit side by side and are never averaged.

### Passes

| Pass | Question | Output |
|---|---|---|
| 0 | Rules, templates, hypotheses | `docs/method/` |
| 1 | Where to pull from | `docs/sources/` — channels, shortlist, query book, red-team review |
| 2 | What do platforms and infrastructure say | ~150 pulls: engine docs, crawler telemetry, protocols, regulators, court dockets |
| 3 | Who sells this, at what price | vendor census, ~190 pulls |
| 4 | Who published a success story that clears the bar | case census: earnings calls, agencies, vendor cases, conferences |
| 5 | How recommendations get gamed, and whether it works | seeding, review-manufacture and technique files (described, never executed) |
| 6–7 | Market sizing; competitor profiles | `docs/markets/` (3), `docs/competitors/` (43 + `INDEX.md`) |
| 8 | Demand per segment | `docs/customers/` — 4 verticals × sub-market × buyer size |
| 9, 11 | Findings; what brands that moved changed | `docs/findings/` |
| 10 | Our own prompt panel | skipped by the owner 2026-09-23 after day 0 |
| 12–14 | AI ads per engine; market potential; academic frontier scan | `ai-ads-evidence.md`, `market-potential.md`, `frontier-scan.md` |
| 16 | Widen and compile | trigger timeline, risk register, local vertical |
| 15 | Brief bake-off: 11 report-writing methods on the same fact pack | 11 PDF decks in `docs/findings/deck-*.pdf` |

The full log of what ran, when, and in which commit is in `docs/method/STATE.md` §Landed.

## 3. Result

### Scale (measured from this repo, 2026-09-29)

| Metric | Count |
|---|---|
| Raw source files | 1,045 markdown pulls + 83 images (`docs/raw/`) |
| Distinct URLs cited in raw | 3,399, across 516 domains |
| Items screened for success stories | ~2,620 (`proof-scorecard.md`) |
| Academic papers screened / kept | 252 / 38 (`frontier-scan.md`) |
| Competitor profiles | 43 |
| Hypotheses scored | 26 of 32 |
| Git commits | 264 |

### What the evidence says (`docs/findings/executive-brief-2026-09-23-r2.md`)

- **Demand is thin and early.** 8 of 27 segment cells show a spend signal, mostly enterprise organic, and nearly all rest on job postings. No buyer discloses a price paid.
- **Paid AI ads are live** on four engines (ChatGPT, Google AI Overviews, Copilot, Amazon Rufus). OpenAI states a "$1 billion" annualized run rate (company-stated). None of the 8 ad products checked publishes a rate card. Claude states it "will remain ad-free".
- **Proof of sales lift is absent.** Of ~2,620 items screened, 0 reach Gold. All 7 positive Silvers are vendor- or practitioner-measured (tier 5). 19 filings at tier 2–3 show declines or null effects, e.g. Microsoft "83-93% drops" in click-through.
- **Brands that moved changed content and tooling, not media.** Across 108 cases: content 63, tooling 58, paid media 2.
- **No sub-market has a measured size.** Published forecasts disagree by 1.92× (organic) to 26.3× (agentic).

The evidence stops at correlation and self-report. What that means for a build decision is left to the reader.

### Where to start reading

| If you have | Read |
|---|---|
| 5 minutes | `docs/findings/executive-brief-2026-09-23-r2.md` |
| 30 minutes | `docs/findings/director-brief-2026-09-23-r2.md` (+ `.pptx`), or any `deck-*.pdf` |
| A specific question | `proof-scorecard.md`, `demand-map.md`, `ai-ads-evidence.md`, `market-potential.md`, `whitespace.md`, `unknowns.md` |
| Doubt about a number | follow its cite into `docs/raw/` |

## 4. Cost

Claude Code session logs, summed with `ccusage` for this repo's sessions only (24 of 28 matched), 2026-09-22 → 2026-09-29:

| Model | API-equivalent cost (USD) |
|---|---|
| Fable 5.1 | 312.39 |
| Opus 5.5 | 220.26 |
| Sonnet 5 | 37.78 |
| Opus 4.8, Opus 5, Haiku 4.5 | 6.42 |
| **Total** | **576.84** |

Tokens: 931.0M cache reads, 33.0M cache writes, 2.96M output, 55K fresh input. 112 subagent transcripts. 90 operator prompts over 24 archived sessions (`prompt-archive/INDEX.md`).

This is the list-price API equivalent computed by `ccusage`, not an invoice. The work ran on a Claude subscription. Cache reads dominate the volume because every agent re-reads the rules and its sources each turn.

## 5. Repo layout

```
README.md          this file
MegaPlan.md        charter: what the programme is and is not
CLAUDE.md          rules every agent follows (evidence, compression, git)
docs/
  method/          scope, plan, trust rubric, templates, STATE.md (scheduler log)
  sources/         channel list, shortlist, query book
  raw/             1,045 verbatim pulls, one per source, dated
  markets/         organic, paid, agentic sizing and structure
  competitors/     43 profiles + INDEX.md
  customers/       demand per vertical: skincare, B2B SaaS, high-CPA regulated, local
  findings/        briefs, scorecards, decks — the output
prompt-archive/    every operator prompt, verbatim — how the agents were driven
projects/          dormant; ORCHESTRATION.md holds the agent-spawning rules
```

## 6. Caveats

- **Desk research only.** No interviews, no ad spend, no own measurement beyond a day-0 panel (Pass 10 skipped).
- **Source quality is uneven.** Only 44% of key claims rest on tier 3 or better, against an 80% target (`findings/unknowns.md` §Tier-3 recount).
- **Survivorship bias.** Published cases are winners. None of the self-reported numbers is audited.
- **Blocked channels.** Live reddit.com, indeed.com, Gartner, Forrester and Crunchbase Pro were unreachable or paywalled, and cells that depend on them read `unknown — checked` (`docs/method/blocked-channels.md`).
- **Time-bound.** Everything is as of 2026-09-22/24. Profiles go stale from 2026-12-22.
- **Mixed models.** Runs moved from Fable to Opus/Sonnet partway through, after a rate limit on 2026-09-23 (`STATE.md`).
- **Raw pulls hold third-party text** under their original copyright, kept for research citation.

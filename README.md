# AI ads research, run by a team of Claude agents

This repo is an experiment in AI orchestration: a team of Claude Code agents doing a full desk-research project with only light steering from one person.

The brief was one line: "Let's dig into AI ads." Can a brand pay, or work, its way into the answers ChatGPT, Gemini, Claude or Copilot give? Does anyone buy that today, and does it pay back?

Over three days (2026-09-22 to 2026-09-24) the agents searched the web and saved 1,045 sources from 516 websites. They graded each source for trust and turned the pile into market files, 43 competitor profiles, findings, briefs and 11 slide decks. Every number in the reports links back to the saved source it came from.

## What the agents found

The short version: AI ads are real and growing, but nobody has shown yet that they sell more product.

- Paid ads already run inside ChatGPT, Google AI Overviews, Microsoft Copilot and Amazon's shopping assistant. OpenAI says its ads make about $1 billion a year. None of the 8 ad products checked publishes a price list.
- Demand from buyers is thin. Only 8 of the 27 customer segments studied show signs of real spending, and most of those signals are job postings. No buyer has said what they paid.
- There is no proof of a sales lift. Out of about 2,620 success stories screened, none met the top evidence grade. The positive stories all come from vendors measuring themselves, while 19 stronger sources (company filings and similar) show traffic falling or no effect.
- Brands that moved mostly rewrote content (63 of 108 cases) and bought new tools (58). Only 2 bought ads.
- No one has measured the size of this market. Published forecasts disagree by up to 26 times.

These points come from the [executive brief](docs/findings/executive-brief-2026-09-23-r2.md). The project stops at the evidence and doesn't give a verdict on whether to build or invest.

## Read the reports

Start with the [executive brief](docs/findings/executive-brief-2026-09-23-r2.md), which is two pages. The [director brief](docs/findings/director-brief-2026-09-23-r2.md) is the long version, also available as [PowerPoint](docs/findings/director-brief-2026-09-23-r2.pptx).

### Slide decks (PDF)

The same set of facts was written up 11 times, each by an agent following a different report-writing method. It was a test of which method gives the clearest report. The decks aren't ranked; open any of them.

- [R0 Baseline](docs/findings/deck-R0-baseline-2026-09-24.pdf), the owner's own template
- [R0b Baseline repeat](docs/findings/deck-R0b-baseline-repeat-2026-09-24.pdf), same template run again to see how much results vary
- [R1 Pyramid Principle](docs/findings/deck-R1-pyramid-principle-2026-09-24.pdf)
- [R2 Minto Pyramid](docs/findings/deck-R2-minto-pyramid-2026-09-24.pdf)
- [R3 Strategy communicator](docs/findings/deck-R3-strategy-communicator-2026-09-24.pdf)
- [R4 Structure and synthesize](docs/findings/deck-R4-structure-synthesize-2026-09-24.pdf)
- [R5 Knowledge synthesis](docs/findings/deck-R5-knowledge-synthesis-2026-09-24.pdf)
- [R6 Deliverable creation](docs/findings/deck-R6-deliverable-creation-2026-09-24.pdf)
- [R7 Decision memo](docs/findings/deck-R7-decision-memo-2026-09-24.pdf)
- [R8 Assumption audit](docs/findings/deck-R8-assumption-audit-2026-09-24.pdf)
- [R9 Consulting-firm style](docs/findings/deck-R9-mbb-extract-2026-09-24.pdf)

Where each method came from, and its licence, is in the [bake-off notes](docs/method/brief-bakeoff/README.md).

### Detailed findings

- [Demand map](docs/findings/demand-map.md): which customer segments show real demand
- [Proof scorecard](docs/findings/proof-scorecard.md): what the published success stories actually prove
- [AI ads evidence](docs/findings/ai-ads-evidence.md): who sells ads inside AI answers, and at what price
- [Market potential](docs/findings/market-potential.md): user numbers and forecasts
- [Transition evidence](docs/findings/transition-evidence.md): what brands that moved actually changed
- [Trigger timeline](docs/findings/trigger-timeline.md): the dated events behind "why now"
- [Whitespace](docs/findings/whitespace.md): where the evidence is empty
- [Frontier scan](docs/findings/frontier-scan.md): what academic papers say could steer AI answers
- [GEO/AEO roles](docs/findings/geo-aeo-roles.md): the new jobs in this field and what they pay
- [Unknowns](docs/findings/unknowns.md): which starting assumptions held up, and what is still unknown

Background files cover the three markets ([organic](docs/markets/organic-recommendation.md), [paid](docs/markets/paid-placement.md), [agentic checkout](docs/markets/agentic-commerce.md)), the [competitors](docs/competitors/INDEX.md), and four customer groups ([skincare](docs/customers/skincare-beauty.md), [B2B software](docs/customers/b2b-saas.md), [finance and insurance](docs/customers/high-cpa-regulated.md), [local businesses](docs/customers/local-multi-location.md)).

## How the orchestration worked

One main Claude session acted as project manager. It kept a plan and a run log ([STATE.md](docs/method/STATE.md)), handed out tasks, and ran up to 7 helper agents at once. Each helper took one slice of the web, such as vendor pricing pages, company filings or academic papers. It saved every page word for word with its URL and date, then reported back. The main session checked the work before committing it to git.

```
pick sources  →  save pages as-is  →  compile by topic  →  findings  →  briefs and decks
 docs/sources     docs/raw             markets, competitors,  docs/findings
                                       customers
```

A few rules kept the agents honest:

- Every source gets a trust grade from 1 (strongest, such as a regulatory filing) to 7 ([rubric](docs/method/trust-rubric.md)).
- The agents wrote down 32 guesses before collecting any data, each with the evidence that would disprove it ([hypotheses](docs/method/hypotheses.md)).
- Agents may not write anything from memory. A gap is written as "unknown", along with where they looked.
- When two sources disagree, both numbers stay side by side. Nothing is averaged.

## What it cost

At API list prices the project would have cost about $577, measured with `ccusage` over this repo's sessions from 2026-09-22 to 2026-09-29. It actually ran on a Claude subscription, so this is an estimate rather than a bill. Most of the volume (931 million tokens) is agents re-reading their instructions and sources. The agents wrote about 3 million tokens of output. The project used 112 helper-agent runs and 90 prompts from the owner.

## Limits

- It is desk research only: no interviews and no money spent on ads. A plan to test AI answers ourselves was dropped after the first day.
- Only 44% of the key claims rest on strong sources, against a target of 80%.
- Published success stories skew toward winners, and none of the self-reported numbers has been audited.
- Some sources could not be reached (live Reddit, Indeed, Gartner, Forrester, Crunchbase Pro). The [blocked list](docs/method/blocked-channels.md) records each one.
- Everything is as of September 2026.
- The agents switched from the Fable model to Opus and Sonnet partway through, after hitting a usage limit on 2026-09-23.
- `docs/raw/` holds copies of third-party pages under their original copyright, kept so every claim can be checked.

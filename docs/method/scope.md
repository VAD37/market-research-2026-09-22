# Scope — standing brief

Set 2026-09-22 by the user. Per root `CLAUDE.md`, this is the standing brief. Every research pass in `docs/` serves it. Changes to it are dated and appended, not overwritten.

## The brief

| Field | Value |
|---|---|
| Market | Brand visibility and product recommendation inside AI assistants |
| Geography | Global, US and EU primary |
| Decision served | What to build, and whether a cost-advantaged team can win it |
| Builder constraint | Engineering in Vietnam, cost advantage vs US/EU vendors |
| Buyer | US/EU based — sold into, not sold from |

The decision is a build decision, not a brand-side or investment one. Research output feeds `MegaPlan.md` and then `projects/`.

## The market splits three ways

Research keeps these separate. Collapsing them produces unusable findings.

| Sub-market | Also called | What is sold | Buyer |
|---|---|---|---|
| Organic recommendation | GEO, AEO, LLMO, AI visibility | Brand appears in AI answers | Brand marketing, SEO owner |
| Paid placement | AI ads, sponsored answers | Ad inventory inside AI surfaces | Media buyer |
| Transaction rails | Agentic commerce | Checkout executed by the agent | E-commerce, payments |

## In scope

- Vendors selling AI-visibility measurement, and their pricing, funding, and differentiation claims
- Whether any vendor can demonstrate causal sales lift, not correlation
- Ad inventory that exists today inside AI surfaces, and what it costs
- Agentic commerce protocols and who controls them
- How vendors in this category acquire US/EU customers — distribution is the binding constraint for a Vietnam-based seller

## Out of scope until reopened

- Classical SEO except where it sizes or bounds the new market
- Consumer-side AI shopping apps
- Model training, inference infrastructure, or LLM vendors as such

## Unresolved — blocks specific passes, not the first one

| # | Open question | Blocks |
|---|---|---|
| D3 | Which sub-market is the build target | `markets/`, `competitors/` depth |
| D5 | Anchor vertical for a measured pass | Measured-by-us pass |
| D6 | Desk only, or desk plus our own prompt panel | Pass 7 |

**All three resolved 2026-09-22. See the revision below.**

## Revision — 2026-09-22, user

Appended, not overwritten. Where this conflicts with the brief above, this section wins.

| # | Question | Answer |
|---|---|---|
| D1 | Decision served | **Changed.** Understand the whole market first, then help a company transition its marketing into AI surfaces. A transition playbook, not a build spec. Building stays open but is downstream of `findings/` |
| D2 | Geography | Unchanged. Global product, US and EU primary demand. APAC is the engineering team, not a market |
| D3 | Sub-market | **Resolved: both.** Organic recommendation and paid placement are both in scope. Agentic commerce stays in scope as the transaction layer under both |
| D4 | Engines | **Resolved: all.** OpenAI and Anthropic primary. Full matrix in `plan.md` |
| D5 | Vertical | **Resolved: skincare as anchor, widened.** B2B SaaS and one high-CPA regulated vertical added for contrast |
| D6 | Evidence target | **Resolved.** Competitor success stories carrying real metrics. Includes proof that deliberate gaming of AI recommendation exists and works. This adds a manipulation lane the original brief did not carry |

Consequences:

- The builder-constraint framing above ("whether a cost-advantaged team can win it") is demoted, not deleted. It returns as a question for `findings/` once the market is mapped.
- Manipulation and gaming of AI recommendation is now in scope as Lane D of `plan.md`. Research into it only — never execution against a third party.
- The buyer is a brand in transition, not a vendor-category investor. `customers/` is weighted accordingly.

Execution plan for all of this: `plan.md`.

## Caveats

- Category is roughly two years old as of 2026-09. Vendor set turns over fast. Any competitor file older than one quarter is stale.
- Assistant knowledge cutoff is 2026-05. Nothing from model memory enters `docs/`. Every claim re-pulled into `raw/` first.
- "Everyone needs it" was the user's framing on 2026-09-22 and is recorded, not endorsed. A horizontal read is the widest and weakest lane; see `findings/` once it exists.

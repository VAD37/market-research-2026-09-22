# Glossary

Set 2026-09-22. The category's terms, defined once. Every file in `docs/` uses these words in these senses; a file needing a different sense defines it inline and says why. Authority: root `CLAUDE.md` > `scope.md` > `plan.md` > `trust-rubric.md` > this file. This file adds no rules and holds no facts; it fixes meanings.

## The three metrics — fixed, never crossed

`plan.md` names the failure mode: visibility conflated with traffic conflated with sales. Every compiled claim names which of the three it is, in the sentence carrying the number.

| | **Visibility** | **Traffic** | **Sales** |
|---|---|---|---|
| Definition | Brand, product or domain appears inside a generated AI answer | Session on the brand's own property whose referrer is an AI surface | Revenue or conversion event attributed to an AI surface |
| Unit | Appearances per n runs of a fixed prompt set | Sessions, users or clicks per period, per referrer host | Currency per period; or conversions, conversion rate, AOV |
| Stamped with | Engine, surface, prompt-set version, date, n | Referrer host, date window, analytics tool | Attribution model, date window, order count |
| Measured by | Running a fixed prompt set n times and counting | Brand analytics referrer or UTM; server logs; clickstream panel | Order data joined to referrer, UTM or agentic-checkout ID |
| Is NOT | Traffic. Classical SERP rank. Ad impressions. Awareness | Visibility. Crawler or bot requests from an AI vendor's crawler | Traffic. Visibility. Vendor-modelled "influenced revenue" |
| Conflation to refuse | One screenshot as proof; undisclosed prompt set behind a score | Referral read as influence; zero-click answers leave no referral | Attributed revenue reported as incremental revenue |

**Crossing rule.** A claim starting at one metric and concluding at another states the link and grades it against the `plan.md` evidence bar; an ungraded crossing is downgraded to the weaker metric. Visibility change alone is Bronze and is never cited as sales proof. **Attributed** = credited by an attribution model; **incremental** = the difference against a holdout. Only incremental supports the word "lift".

### Visibility has three sub-metrics — counted separately, never summed

| Term | Means | Counted as |
|---|---|---|
| Mention | Brand named in the answer text, no link | Mention rate |
| Citation | Answer links or footnotes the brand's domain | Citation rate |
| Recommendation | Answer names the brand as an answer to a buying-shaped prompt | Recommendation rate |

A citation without a mention, and a mention without a recommendation, are different results. A vendor "share of voice" or "AI visibility score" composite is recorded as that vendor's composite with its stated inputs, never as one of the three.

## Sub-markets

| Sub-market | Aliases in the wild | What is sold | Buyer |
|---|---|---|---|
| Organic recommendation | GEO, AEO, LLMO, AI visibility, AI SEO | Brand appears in AI answers unpaid | Brand marketing, SEO owner |
| Paid placement | AI ads, sponsored answers, sponsored results | Ad inventory inside AI surfaces | Media buyer |
| Agentic commerce | Transaction rails, agentic checkout | Checkout executed by the agent | E-commerce, payments |

Aliases stay as the source used them in `raw/`, unnormalised; compiled files put the sub-market name in column 1. GEO is ambiguous outside this repo (also geographic); inside `docs/` it means generative engine optimisation only.

## Lanes — research tracks. A lane is not a sub-market and not a segment

| Lane | Track | Core question |
|---|---|---|
| A | Organic recommendation | How does a brand get named in an answer |
| B | Paid placement | What inventory exists, what it costs, who buys |
| C | Agentic commerce | Who controls checkout inside the agent |
| D | Manipulation and gaming | How recommendation is steered, and whether it works |
| E | Measurement and proof — cross-cutting | Who demonstrates causal lift rather than correlation |
| F | Transition evidence — cross-cutting | What brands that moved actually changed |

Every pass in A–D feeds E and F. Lane D is research into manipulation, never execution of it.

## Evidence grades — assigned on intake against the seven-item evidence bar in `plan.md`

| Grade | Standard | Handling |
|---|---|---|
| Gold | Holdout, geo-split or switchback. Causal | Cite as proof |
| Silver | Pre and post, baseline plus an unaffected control metric | Cite as evidence, labelled correlational |
| Bronze | Visibility or mention-rate change only, no revenue link | Cite as visibility only |
| Fools gold | Revenue claim, no baseline or no control | Cite only as evidence of category noise |

## Source labels, tiers, grades — three independent axes

| Label kind | Means |
|---|---|
| vendor-reported | The seller published it about its own product or customers |
| analyst-derived | A third party computed it from other inputs |
| filed | In a regulatory, court or funding filing |
| company-stated | A company said it about itself outside a filing |
| measured-by-us | Produced by our own pull or panel run, output in `raw/` |

**Tier** = the 1–7 provenance score in `trust-rubric.md`, written on every `raw/` file as `tier: <n>` plus the reason if adjusted. Label says *what kind* of number it is; tier says *whether to keep it*; grade says *what a success story proves*. A claim can carry all three.

## Segment, engine, surface

| Term | Means |
|---|---|
| Segment axes | Sub-market × vertical × buyer size |
| Cell | One combination of the three axes — the unit demand is read against |
| Vertical | Skincare and beauty (anchor), B2B SaaS, high-CPA regulated |
| Buyer size | SMB, mid-market, enterprise — as the source defines them, definition quoted |
| Demand signal | A public, internet-only proxy from `demand-signals.md`, with its bias and tier |
| Cell read | One word: **spend**, **attention**, or **none**. Attention never stands in for spend |
| Screened / cleared | Candidates examined / candidates passing the evidence bar. Reported as a pair |
| Survivorship | Only winners publish. Stated once per scorecard, with the screened count |
| Engine | One assistant product, at a named model version where the surface discloses it |
| Engine priority | The 1–4 ranking in `plan.md`; an assumption until the Pass 2 share table reweights it |
| Surface | Where the answer is delivered. Three kinds, never merged |
| — consumer chat | The end-user chat product. **Primary** measurement surface |
| — API | Programmatic access. Secondary, always labelled. Not what users see |
| — search-integrated | An AI answer rendered inside a search results page |
| Prompt set | The fixed, versioned list of prompts a panel runs. Version recorded per sample |
| Run | One execution of one prompt against one engine, surface and date. n counts runs |
| Panel | Repeated runs of a prompt set on a schedule, per `panel-protocol.md` |

## Pipeline and sizing

| Term | Means |
|---|---|
| Pull | One retrieval of one source into one `raw/` file, dated and tiered |
| Pull method | fetch / browser extension / predecessor repo / manual |
| Raw pull | The `raw/` file itself. Verbatim, compression-exempt, never edited after the fact |
| Re-pull | A new `raw/` file for a source already pulled. The old file is kept with its date |
| Compiled file | Anything in `markets/`, `competitors/`, `customers/`, `findings/` |
| Oldest pull depended on | Earliest pull date among the `raw/` files a compiled file cites. One line per file |
| Stale | A pull older than one quarter at citation time. Re-checked, and the re-check dated |
| Predecessor repo | `D:\researchs\market-research\` — one channel, cited via `raw/`, never from memory |
| Bottom-up | Vendor count × disclosed price × disclosed customer count. The sizing method here |
| Top-down | A total divided down. Recorded with its author and base, never as the size |
| Forecast | A future number. Sits beside the size, labelled forecast, never as the size |
| Base period | The window a growth rate is measured over. No growth number without it |

**Structural checks** — four questions every `markets/` file answers or marks `unknown — checked <channel> <date>`: **substitute** (what the brand does instead; is "do nothing" the real competitor), **platform risk** (which engine ships native tooling making third-party vendors redundant), **incumbent bundling** (which SEO or analytics incumbent added this as a feature, at what price delta), **regulatory** (ad-disclosure rules inside AI answers in force as of the pull date).

## Caveats

- Sources use these words loosely. `raw/` keeps the source's word; the compiled file maps it and says so.
- Alias lists are as of 2026-09-22. A new alias found in a pull is appended here with its date.
- "AI visibility" is both a sub-market alias and a vendor product category. Compiled files say which.

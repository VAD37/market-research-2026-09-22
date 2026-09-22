# Profound — MongoDB case study

```yaml
source:          Profound — case study "How MongoDB increased AI Search visibility by 50% while saving time with Profound Agents"
url_or_doc_id:   https://www.tryprofound.com/customers/mongodb
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome, own dedicated tab)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     no absolute date window, no numeric baseline, no engine individually named, and no sample size disclosed anywhere on the full page — marketing narrative with quotes, not a method disclosure; table default for a vendor case study with no n
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          not individually named — page refers throughout to "Answer Engines" and "AI" generically (LLM Answer Engines); no ChatGPT/Perplexity/Gemini/Claude named
metric_kind:     visibility (AI Search visibility); accuracy (a fourth, non-glossary metric — "accuracy rate" of AI answers about MongoDB, not one of visibility/traffic/sales)
supersedes:      none
captured:        full page — single call, reached the end of the article (final pull-quote), no truncation
vertical:        none named as an industry vertical on this page — customer is a database/developer-platform company; Profound's own customers-index page tags this case "SaaS · Enterprise" (per `docs/raw/a-profound-customers-2026-09-22.md`, not repeated on this dedicated page)
evidence_grade:  Bronze (full-page, on this pull). All seven bar items evaluated below.
pass3_grade:     Bronze (from `docs/raw/a-vendor-census-c1-2026-09-22.md`, graded off the customers-index page teaser — `docs/raw/a-profound-customers-2026-09-22.md`, which did not open this dedicated page)
paid_by_outcome: unknown — quote below
prompt_set_disclosed: no — "internal Q&A training dataset" is named but not published; no n of questions and no wordings disclosed
```

## Verbatim

Title: "How MongoDB increased AI Search visibility by 50% while saving time with Profound Agents"

"When developers ask AI how to configure MongoDB, finding the wrong answers doesn't just create a bad AI experience, it breaks workflows and erodes trust in MongoDB itself. The database platform serving millions of developers realized early that in the AI era, accuracy isn't just a nice-to-have metric, it's crucial to their customers' success."

"By treating Answer Engine Optimization (AEO) as mission-critical for serving their audience, MongoDB achieved a 50% increase in AI Search visibility while maintaining 90%+ accuracy rates."

Quote: "If an Answer Engine gives the wrong information about how to configure MongoDB, the developer doesn't have a bad experience with the AI, they have a bad experience with us." — Fiona Erickson, Team Lead, Organic Acquisition.

**"The data platform for builders":** "MongoDB is the developer data layer designed for the AI era. Built around a flexible, unified document model, it empowers developers to build, scale, and secure intelligent applications faster. Millions of developers and more than 67,000 customers across almost every industry, including ~75% of the Fortune 100, rely on MongoDB for their most important applications." Quote: "MongoDB is the ideal data platform for builders. Millions of developers and enterprises across industries rely on us, and if AI gives them a bad answer, it breaks their workflow ... We knew our audience of ITDMs, Developers, and DBAs were early adopters of AI Search. So, we had to expand our audience to include the AI agents they're now collaborating with every day." — Fiona Erickson.

**"How Answer Engines changed developer workflows":** "For the MongoDB team, the signal came early. They noticed that when developers asked how to get set up in MongoDB Atlas, Answer Engines were providing instruction up to basic registration, without providing any guidance on what comes next. When users sought support debugging or problem solving, the AI tools would sometimes reference out-of-date documentation. These LLMs didn't have the latest information to properly help MongoDB users navigate the nuances of their setup." Quote: "These were critical missed opportunities to deliver for our users ... Honestly, it was a mix of exhilaration and complete vertigo. For two decades, traditional SEO had a very defined set of rules. Suddenly I was dusting off my data science skills, tracking multiple algorithms instead of one, building unsustainable 'DIY' measurement benchmarks just to have some data to base decisions on." — Fiona Erickson.

**"Entering the next generation of discovery optimization":** "Before Profound, MongoDB had legacy search monitoring tools that offered basic visibility data but couldn't pull actual results from LLM Answer Engines. The insufficiency of that data led them to search for a new option. What made Profound stand out was the scale and pace of their roadmap. For MongoDB's technically sophisticated team, the real differentiator was the depth of conversation with the Profound team." Quote: "It was so refreshing to nerd-out in that first call with Profound; we could all be transparent about what was unknowable, what we thought was coming, discuss our speculations and educated guesses, instead of just rigidly going through their sales pitch." — Fiona Erickson.

**"Measuring accuracy at scale":** "Together with Profound, MongoDB made accuracy measurable from day one." Quote: "Profound helped us build an internal Q&A training dataset on top of their API, benchmarking LLM responses against 'gold standard' MongoDB answers for branded questions." — Fiona Erickson. "The collaboration resulted in a feedback loop where inaccurate MongoDB citations triggered flags for the content team to fix source content. Their dashboards visualized exactly how improvements in content accuracy correlated with overall visibility and share of voice. The result was that accuracy and trust in AI answers became a first-class metric, with dedicated support and extremely high standards. They achieved accuracy rates above 90% for MongoDB-related queries."

**"Preserving expert time with Profound Agents automation":** "With premium engineering talent serving as subject matter experts, MongoDB wanted to think about their time as efficiently as possible." Quote: "Our engineers' time is expensive and their attention is finite. We can't have them hunting for opportunities manually." — Fiona Erickson. "The team deployed two specific Profound Agents to solve this. First, a citation aggregation agent that helps report on the AEO influence of cross-functional teams (Builder Relations, SEO, PR and Community), and next, a schema markup recommendation Agent that cuts the time to update releases by almost 30%." Quote: "We look to Agents to develop high quality V1 outputs that get routed to SMEs for review, reporting or implementation ... As builders in our own right, access to Profound Agents enabled us to centralize our tracking and automation in one platform, and get in on the ground floor of the tech that helps us show up for our customers." — Fiona Erickson.

**"Rapid gains in AI visibility and accuracy":** "Since working with Profound, MongoDB has seen a 50% increase in AI Search visibility. Their accuracy work delivered on its core promise: accuracy rates above 90% for MongoDB queries, meaning builders can stay in-flow getting accurate, complete answers about how to problem-solve or better leverage MongoDB without hunting through documentation." Quote: "The same URLs and campaigns now work double-duty, feeding both the traditional Google crawler and the LLM context window simultaneously, with automation making it sustainable for our team." — Fiona Erickson.

**"Preparing for agent-first development":** "MongoDB's AEO program continues scaling in two directions: deeper automation and broader impact." Quote: "Deeper automation means agents that not only surface opportunities, like a key Reddit thread, but draft responses and tasks for the right owner. Broader impact means that as automation scales, we'll also free up time to broach new surfaces and scale the things that are working ... We're preparing for a future where search looks fundamentally different. Developers don't want to hunt through documentation; they want to instruct an AI agent to write the code for them. By structuring our data to feed those agents directly, MongoDB becomes visible to the next generation of builders." — Fiona Erickson.

Closing quote: "If you are running a marketing team in 2026 and still treating AI optimization like a side project, you're already behind." — Fiona Erickson.

## Pull notes — mechanical only

- Fetched via `claude-in-chrome` browser extension (connected this session), `get_page_text` on a dedicated new tab (tabId 1697684063) opened for this task. Full article captured in one call, reached the closing pull-quote with no truncation marker.
- No absolute calendar date anywhere on the page — no relative duration either (unlike the two Quattr cases pulled alongside this one, which at least give "12 weeks" style windows). The 50% visibility increase and 90%+ accuracy figures carry no stated measurement window at all.
- No engine individually named anywhere on the page — "Answer Engine(s)", "AI", "LLM Answer Engines" used generically throughout; no ChatGPT, Perplexity, Gemini, Claude, or Copilot named.
- No sample size or query-volume figure disclosed. "Internal Q&A training dataset" is named as the accuracy-benchmarking method but its size (n of questions) is not stated.
- No statement of who measured beyond "Profound helped us build an internal Q&A training dataset on top of their API" — Profound is the vendor and the measurer; no independent third party named. No statement anywhere of whether Profound or any party was paid by the outcome — this is a customer testimonial about a SaaS platform relationship, not a performance-based engagement as described on the page.

## Evidence bar — seven items, evaluated against this full page

| # | Item | Present / Absent | Quote |
|---|---|---|---|
| 1 | Brand, or credibly specified anonymised profile | **Present** | "MongoDB is the developer data layer designed for the AI era" — named throughout, plus a named spokesperson (Fiona Erickson, Team Lead, Organic Acquisition) |
| 2 | The engine or engines | **Absent** | Only generic "Answer Engine(s)" / "AI" / "LLM Answer Engines" — no engine individually named anywhere on the page |
| 3 | The date window, absolute | **Absent** | No date, relative or absolute, is given anywhere for the 50% visibility or 90%+ accuracy figures |
| 4 | The baseline before intervention | **Absent** | "MongoDB achieved a 50% increase in AI Search visibility" — no starting-point number given, only the percentage change |
| 5 | The intervention itself | **Present** | "Profound helped us build an internal Q&A training dataset on top of their API, benchmarking LLM responses against 'gold standard' MongoDB answers for branded questions"; "The team deployed two specific Profound Agents" |
| 6 | The sample size, or the traffic volume | **Absent** | No n of questions in the "internal Q&A training dataset", no query volume, no visitor count anywhere on the page |
| 7 | Who measured, and whether they were paid by the outcome | **Partial** | Measurer named: "Profound helped us build an internal Q&A training dataset on top of their API" — Profound itself, no independent auditor. No statement anywhere of whether any party was paid by the outcome |

**Full-page grade: Bronze.** Present: named brand, a described intervention (Q&A benchmarking dataset plus two named automation Agents), and a visibility-only metric (50% increase in AI Search visibility) with no revenue crossing. Missing against the full seven-item bar: item 2 (no engine named), item 3 (no date at all, not even relative), item 4 (no numeric baseline), item 6 (no n), and full disclosure on item 7. This is a weaker-evidenced full page than either Quattr case pulled alongside it — no baseline number, no engine name, and no date of any kind — but still clears Bronze because it names the brand, describes the intervention, and states a visibility-only percentage change with no revenue link.

**Grade change vs. Pass 3: same (Bronze → Bronze).** Pass 3 graded this case Bronze from the customers-index teaser alone (`docs/raw/a-profound-customers-2026-09-22.md`, which explicitly did not open this dedicated page this session). This full-page pull confirms Bronze and adds that the full page discloses no additional bar items beyond what the index teaser already carried — the intervention description (Q&A dataset, two named Agents) is new detail from this pull, but no date, baseline, engine name, or sample size appears anywhere on the full page either.

## Caveats

- The 50% figure ("50% increase in Plaid's AI Search visibility") that Profound's own customers-index page and homepage carousel attribute to Plaid does not appear on this page — this page's "50% increase in AI Search visibility" is MongoDB's own, separately stated. No cross-customer figure confusion found on this specific page (see `docs/raw/e-case-profound-plaid-2026-09-22.md` for the Plaid case, pulled separately, which does carry a conflicting-figures note from the index page).

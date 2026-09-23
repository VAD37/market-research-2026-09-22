# Pepper Content blog — "The AI Search Team Ownership Model: Who Owns GEO?"

```yaml
source:          Pepper (Pepper Content / Pepper.inc, GEO/content vendor); byline "Dhriti"
url_or_doc_id:   https://www.pepper.inc/blog/ai-search-team-ownership-model/
published:       2026-06-17
pull_date:       2026-09-23
pull_method:     fetch (curl, HTML stripped to text)
pull_purpose:    evidence about category noise
tier:            6
tier_reason:     Vendor blog — Pepper sells GEO execution/orchestration services and the post ends with a direct product pitch ("Pepper acts as your orchestrating layer... See how the model works at www.pepper.inc/product/atlas/"). The RACI model itself is the vendor's own prescriptive framework, not a measured survey. However the post quotes several named, attributable practitioners speaking at a named industry event (Index '26) — those individual quotes (Kishan Panpalia/Pepper, Heidi [CMO, company not named], Dropbox's marketing lead [unnamed by name], NVIDIA's Linda Kaplinger, "Eli" a CEO client) are kept as documented practitioner statements about org structure, captured per trust-rubric.md as category-noise evidence, not as a verified industry-wide standard.
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page (post body, RACI tables, FAQ section); "Latest Blogs"/"Similar Posts" footer teasers excluded except where noted
```

## Verbatim

TL;DR (as printed): "The single most common reason GEO programs stall isn't strategy or budget. It's ownership. AI search isn't a channel that fits neatly under one team. It sits at the intersection of brand, content, SEO, PR/comms, and product marketing, which means everyone touches it and no one owns it... GEO, as one practitioner put it at Index '26, is 'product marketing for the machines'..."

"Ask five people in a marketing org who owns AI search, and you'll get five answers. SEO says it's an extension of search. Content says it's about the content. PR says it's about authority and citations. Brand says it's about entity recognition. Product marketing says it's about how the product shows up in answers. They're all right. And that's exactly the problem."

"Kishan Panpalia, part of Pepper's founding team, framed it precisely at Index '26: GEO 'has intersections with your social media, with your PR and corp comms, with your traditional SEO, content marketing, and product marketing across multiple teams. GEO is not a channel. It's a strategy at the center of it.'" — "'GEO and AEO is nothing but product marketing for the machines. Product marketing never started as a role. It started as a strategy at the cusp of multiple roles. GEO is on that same crossroads now.'" (Kishan Panpalia, Pepper founding team, at Index '26)

Definition (as printed): "An AI search team ownership model is a defined accountability framework that assigns the components of generative engine optimization (GEO) across existing marketing functions (brand, content, SEO, PR/communications, and product marketing) using a RACI structure (Responsible, Accountable, Consulted, Informed)."

"Five Functional Domains" table (Domain — What It Covers — Natural Owner), reproduced:
| Functional Domain | What It Covers | Natural Owner |
|---|---|---|
| Entity & brand recognition | Wikipedia, Wikidata, brand consistency, knowledge graph presence, brand sentiment in answers | Brand |
| Content & citability | Structured pages, FAQ blocks, comparison content, answer-format writing, content quality standard | Content |
| Technical retrievability | Schema markup, llms.txt, crawlability, site architecture, indexing, Core Web Vitals | SEO / Dev |
| Authority & citations | Third-party citations, digital PR, G2/review platforms, press coverage, backlinks | PR / Comms |
| Product positioning in answers | How the product is described, feature/category accuracy, comparison framing, pricing data | Product Marketing |

"AI Search RACI" table (Component — Responsible — Accountable — Consulted — Informed), reproduced:
| Component | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Prompt universe / query strategy | SEO | GEO Lead | Product Mktg, Content | Brand |
| Entity optimization (Wikipedia/Wikidata) | Brand | Brand | PR, SEO | Content |
| Content structure & citability | Content | Content | SEO, GEO Lead | Brand |
| Schema & technical retrievability | Dev/SEO | SEO | Content | GEO Lead |
| Third-party citations & digital PR | PR/Comms | PR/Comms | Brand, Content | SEO |
| Product positioning in answers | Product Mktg | Product Mktg | Content, Brand | SEO |
| Citation monitoring & reporting | GEO Lead | GEO Lead | All functions | CMO |
| Cross-functional orchestration | GEO Lead | CMO | All functions | Exec team |

"The accountability test: for every component, exactly one team should be in the Accountable column. If two teams are accountable, neither is. If zero are, the work falls into the gap."

Handoff-failure table (Handoff — How It Breaks — The Fix), reproduced:
| Handoff | How It Breaks | The Fix |
|---|---|---|
| Content → SEO (schema) | Content publishes; schema is assumed but never added because nobody owns the trigger | GEO Lead adds 'schema applied' as a publish-gate checklist item; no page goes live without it |
| Brand → PR (entity building) | Brand maintains Wikidata; PR runs press, but nobody connects press coverage to entity citations | Quarterly entity sync: PR's press wins feed Brand's Wikipedia/Wikidata references |
| PR → Content (citation sources) | PR earns coverage; Content never repurposes it into citable owned pages | Every PR placement triggers a Content brief to capture the same narrative on an owned URL |
| Product Mktg → Content (positioning) | Product messaging changes; AI-facing content still describes the old positioning | Product Marketing reviews the top 20 AI-cited pages each quarter for positioning accuracy |

"The orchestrating layer does five things no existing function does end to end: Owns the prompt universe... Runs the citation monitoring... Enforces the handoffs... Translates between functions... Reports to the CMO and board." This is "the translation role NVIDIA's Linda Kaplinger described at Index '26: being 'the explainer of what AEO or GEO is, and how you translate that back to even talking to product.'"

"Eli, a CEO who works with Pepper, described exactly this at Index '26: 'When we met Pepper, what we ended up having is this: yes, you get Pepper, but you get a website expert, a search expert, a GEO expert. We'd show up to a weekly call with 6 or 7 people. So instantly, I've got that part of my business taken care of. From a resource allocation perspective, I don't have to worry about staffing that up.'"

"The resourcing math: building all five functions plus a dedicated GEO Lead internally is a 6-figure annual commitment in headcount alone, before tools."

Three team models (as printed): "The embedded model (small teams): No dedicated GEO hire. The most senior marketer (often the CMO or VP Marketing) acts as the orchestrating layer part-time... Works up to ~10-person teams." "The GEO Lead model (mid-size teams): A dedicated GEO Lead owns monitoring and orchestration full-time, while the five functions execute their RACI components. This is the most common enterprise structure forming in 2026. The GEO Lead is often a former SEO or content strategist who has developed cross-functional fluency." "The systems-thinker model (AI-native teams): The org hires what enterprise CMOs at Index '26 called 'systems thinkers': people who think in terms of how LLMs read data and how content must be structured for machines... often paired with an AI engineer on staff."

"'A Lot Flatter': The Marketing Org Is Shrinking — Heidi, a CMO on the Index '26 enterprise panel, described how she's rebuilding her org for the GEO era: 'First and foremost, just a lot flatter. The traditional marketing org used to be a flex: how big is your team, 100 people, 200 people. Now the flex is, it's two.'"

"The Rise of the 'Systems Thinker' and the AI Engineer on Staff — ...Heidi described it directly: 'The biggest change for us is we have an AI engineer on staff. And I've hired the new marketing ops people, the systems thinkers. People that think: this is how an LLM is going to look at data.' Dropbox's marketing lead echoed it, describing acceleration toward 'systems thinking' in the marketing org."

"'Content People Who Get the Structure It Needs to Be In' — A second new role surfaced repeatedly at Index '26: the content strategist who understands machine-readable structure. As Heidi put it: 'You need to hire content people that can think, okay, to structure this content on my website, this is how I have to write.'"

"PR Is Becoming a Growth Function — Kishan Panpalia made a pointed claim at Index '26: 'PR is now a growth marketing function, 100%. Sorry to all the PR and comms leaders in the room, you all have to become growth marketers.' His reasoning: digital PR now directly drives LLM citations, and one-time annual backlinking campaigns no longer work; consistent monthly distribution does."

"Authenticity as a Cross-Functional Constraint — ...Dropbox's marketing lead noted you can 'sniff from a thousand miles when it's AI-generated content versus one with an authentic voice.'"

FAQ answer (as printed): "Do we need to hire a dedicated GEO Lead? It depends on team size. Small teams (under ~10 people) can run an embedded model where the senior-most marketer orchestrates part-time. Mid-size and enterprise teams generally need a dedicated GEO Lead who owns citation monitoring and cross-functional coordination full-time... Some AI-native orgs are instead building this into a 'systems thinker' marketing-ops role, sometimes paired with an AI engineer on staff."

## Pull notes — mechanical only

- Fetched via curl with a browser user-agent (HTTP 200, ~128KB raw HTML); stripped to text. No paywall.
- "Heidi" and "Dropbox's marketing lead" are named only by first name / company-role, not full name or title, in the source itself — captured exactly as the source names them, not supplemented.
- Footer "Latest Blogs" teasers (AI search tracking error-bar piece, AI tools listicle, GEO timeline piece) skimmed for topic only, not transcribed — separate articles, not this pull's subject.
- **Session note:** this file was written into a git worktree at `.claude/worktrees/roles-blog-f/` (branch `agent/roles-blog-f`) because the subagent session that produced it could not write directly to the shared checkout (bg-session isolation guard). Needs merge/copy into the main checkout's `docs/raw/` — see this pull's handback note.

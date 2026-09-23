# Hacker News (Algolia API) — GEO/AEO/AI-search roles, job ads, and practitioner skepticism

```yaml
source:          Hacker News (via Algolia HN Search API, hn.algolia.com)
url_or_doc_id:   https://hn.algolia.com/api/v1/search?query=<q>&tags=story,comment ; https://hn.algolia.com/api/v1/search?tags=comment,story_<id> for full comment sets on target stories; per-item https://hn.algolia.com/api/v1/items/<id>
published:       per item — created_at field, verbatim UTC timestamp from API
pull_date:       2026-09-23
pull_method:     fetch (curl-equivalent, Algolia public search API, no auth)
pull_purpose:    evidence about category noise (practitioner and skeptic chatter on GEO/AEO/AI-search roles; job-ad text is company-stated, not verified)
tier:            6-7 for individual comments/stories as evidence about a number (self-reported, anonymous handles, no verification); kept as a census of practitioner and hiring chatter per trust-rubric tier 6/7 "evidence about category noise" allowance
tier_reason:     anonymous forum posts and comments; no method, no n beyond count of items; job-ad salary figures are company-stated postings, unverified
source_label:    company-stated (job ads, self-reported freelancer profiles) / company-stated (comments — self-reported by commenters)
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        query log with per-call hit counts, plus every selected item verbatim (title/story text or comment text), author, points, UTC date, and objectID/permalink-equivalent (https://news.ycombinator.com/item?id=<objectID>)
```

## Verbatim

### Query log (Algolia HN Search API)

| Query / target | Tags | Result |
|---|---|---|
| "generative engine optimization" | story,comment | 25,584 bytes returned (multi-hit) |
| "AEO answer engine optimization" | story,comment | 63,409 bytes |
| "GEO job title" | story,comment | 97,508 bytes |
| "AI search optimization role" | story,comment | 83,441 bytes |
| "LLM SEO" | story,comment | 46,908 bytes |
| "SEO is dead" | story,comment | 17,711 bytes |
| "AEO role" | story,comment | 79,632 bytes |
| "GEO specialist" | story,comment | 87,180 bytes |
| "prompt engineer SEO" | story,comment | 80,559 bytes |
| "GEO manager" | story,comment | 86,218 bytes |
| "AEO specialist" | story,comment | 77,324 bytes |
| "generative engine optimization role" | story,comment | 239,711 bytes |
| "AI search specialist" | story,comment | 109,255 bytes |
| "AI visibility manager" | story,comment | 139,890 bytes |
| "SEO hucksters" | story,comment | 50,078 bytes |
| "GEO consultant" | story,comment | 158,968 bytes |
| "AEO consultant" | story,comment | 110,880 bytes |
| "LLMO" | story,comment | 42,701 bytes |
| "content strategist AI search" | story,comment | 151,972 bytes |
| "SEO career pivot AI" | story,comment | 7,490 bytes (no hits) |
| "Who is hiring" (search_by_date, 2026 only) | story | found Sept 2026 (id 49522897), Aug 2026 (id 49156683) threads |
| story_id 49522897 ("Ask HN: Who is hiring? Sept 2026") full comment set | comment | 398 comments; 12 matched GEO/AEO/AI-search keyword filter |
| story_id 49156683 ("Ask HN: Who is hiring? Aug 2026") full comment set | comment | 379 comments; 10 matched |
| story_id 48357725 ("Ask HN: Who is hiring? June 2026") full comment set | comment | 495 comments; 19 matched |
| story_id 47805998 ("Scan your website to see how ready it is for AI agents") full comment set | comment | 178 comments; ~14 discuss GEO/AEO directly |
| story_id 46462347 ("Hearing a lot that SEO is dead, GEO is future") full comment set | comment | 0 comments (unanswered Ask HN) |

Raw hit counts are pre-filter (many hits were false positives on "geo" as geography/geospatial, e.g. GIS, Cloudflare Geo Key Manager, geo-targeting). Items below are the hand-filtered subset that actually discusses SEO/AEO/GEO as a job, role, title, or skill.

### Items

**Story — "Scan your website to see how ready it is for AI agents"** (isitagentready.com) — id 47805998 — 2026-04-17 — https://news.ycombinator.com/item?id=47805998

Comment thread on this story is the single largest concentration of practitioner/skeptic chatter about "GEO" as a discipline found on HN in this pull. Selected comments, in thread order:

> GEO? — u/tehjoker, 2026-04-17T16:31:00Z, id 47807715

> "GEO" (optimizing for agent search) is the legitimate sequel to SEO though.
>
> I published a free macOS app three years ago to the app store and abandoned it. Over the last six months I received multiple emails per week from people asking where they can find it since it only shows up on the app store for older macOS.
>
> I finally asked people how they found out about my app, and 100% of the time it was because they asked ChatGPT how to do something and it found my crappy website. I had — u/hombre_fatal, 2026-04-17T16:32:33Z, id 47807737 [note: comment truncated at API's stored length]

> "Generative Engine Optimization" a phrase as dumb as the idea.
>
> For 30 years marketers have been doing everything they can to avoid making sites useful for people, despite that being what Google rewarded from the start (e.g. relevant link text, page titles, and headings). — u/xnx, 2026-04-17T16:58:57Z, id 47808018

> The absurd process of SEO hucksters trying to pivot their obsolete services into "GEO" as most ecommerce websites realize their entire value was a list of part numbers and prices. — u/xnx, 2026-04-17T16:08:44Z, id 47807458

> It's the same as SEO.
>
> No one does SEO because they're trying to help Google.
>
> You do it because you're trying to help the people *using* google. (Edit: or trying to make money by driving traffic for ads)
>
> Whether or not companies spend time on AEO is directly tied to whether LLM/agents/AI/etc end up becoming a lead channel that buyers use to research products to buy. — u/cj, 2026-04-17T18:44:15Z, id 47809198

> I mean, I can see the bones of the point you're trying to make, but:
>
> * You describe your website as "crappy" yet ChatGPT was able to figure it out enough to get you traffic for an app you didn't maintain
> * ... with the caveat that it thought made up theoretical features were actual features
>
> So unless your website was "GEO"d by sheer accident, I really don't think this is a good example to cite as the demonstration of what you're saying. — u/ToucanLoucan, 2026-04-17T17:20:24Z, id 47808283

> I'd liken it to accidentally getting a high ranking website on Google without thinking about it.
>
> It doesn't mean you can't deliberately game the bot. It means you can analyze how and then replicate it (aka SEO).
>
> If I can unintentionally sway the LLM agent, then I can figure out how and do it intentionally (aka GEO).
>
> Either way, if you've used LLMs, then you it's trivially possible to sway them. That's the only proposition you need to accept for GEO to be possi[ble] — u/hombre_fatal, 2026-04-17T20:43:38Z, id 47810373 [note: comment truncated at API's stored length]

> AI industry: "AI agents will soon be able to do any white-collar human job!"
>
> Also AI industry: "Please make sure your website is adapted so that AI agents are able to use it." — u/Mordisquitos, 2026-04-17T16:23:06Z, id 47807615

> My traffic is down 60% year on year because of AI overviews and LLMs. They took everything without consent, used it without credit, and pushed my retirement back a few years. Now I should make their job easier? — u/nicbou, 2026-04-17T14:33:28Z, id 47806393

---

**Comment — on story "Wise expanding into other markets?"** — id 44383799, story_id 44383798 (parent story now 404s on the item API — likely deleted/dead) — u/whitefables — 2025-06-26T02:46:28Z — https://news.ycombinator.com/item?id=44383799

> Saw an interesting job post from Wise yesterday that was hiring for an SEO specialist for a project called "owned sites".
>
> This got me digging, and I think I've uncovered something big about their AEO/GEO strategy:
>
> Wise seems to be building a network of sites beyond their main domain. I did some digging and found that out of 10 results for a transfer query on ChatGPT, 4 were owned by wise.com (including exaip.com), and 1 was from their partner remitfinder.
>
> This strategy allows them to dominate more of the conversation in their industry, appearing in multiple contexts when users ask AI systems about international money transfers.
>
> It's a smart move for AEO (AI Engine Optimization) and GEO (Generative Engine Optimization). By controlling more sites, they're increasing their chances of being cited by AI systems.
>
> This approach goes beyond traditional SEO. It's about creating a wider content footprint to influence AI perceptions and responses.
>
> The job posting specifically mentions an "Owned Sites" team, suggesting this is a deliberate, long-term strategy for Wise.
>
> Also did a few more interesting experiment to uncover how ChatGPT forms an opinion from search & how to find the queries used by ChatGPT - happy to share more.
>
> Anyone else here performing your own experiments to understand how AEO/GEO is gonna be different from SEO?

[note: whitefables writes "AEO (AI Engine Optimization)" — differs from the more common expansion "Answer Engine Optimization" seen elsewhere in this pull; terminology is not settled even among practitioners]

---

**Show HN — "FlipAEO — Get your SaaS cited by Perplexity and AI search"** — id 47774957 — u/harvansh — 2026-04-15T05:17:33Z — https://news.ycombinator.com/item?id=47774957 — 1 point

> Hey HN. I am a solo dev. I usually build AI image and video tools, and I can ship products pretty fast. But getting traffic to them is always my biggest pain.
>
> Lately, my normal SEO tricks stopped working and i know yours too after dec 25. I realized my own behavior changed too, we don't search and click links anymore. We just ask Perplexity or chatgpt or gemini, and we only click the citations. I realized that if my SaaS isn't in those AI citations, my product basically doesn't exist.
>
> So I built FlipAEO. It helps structure your site's data so LLMs actually understand exactly what your product does, so they can cite you as a trusted source when people ask questions in your niche.
>
> Using this workflow i have grown my another saas (250k+ impressions, 3k+ clicks, and 550+ ChatGPT refferals.)
>
> I turned my local workflow into a product, and launched 2 months ago. Being completely honest, I have exactly 3 active users paying my bills. Building it was the fun part, but finding people who actually care about Answer Engine Optimization (AEO) is really hard.
>
> I'm posting here because I want to know if I am just crazy, or if this is a real problem you guys are facing too. Are you doing anything to get your products cited by AI search?
> Here is the link: https://flipaeo.com
> Would love any raw feedback on the tool or the idea??

---

**Ask HN — "Hearing a lot that SEO is dead, GEO is future. So, got some questions about it"** — id 46462347 — u/cosmicbeing — 2026-01-02T07:29:23Z — https://news.ycombinator.com/item?id=46462347 — 2 points, 0 comments

> 1. Do you believe that?
> 2. Does anyone knows how to rank on that? or does it even have a ranking?
> 3. How does a LLM decide what to cite?
> 4. How can you make sure that your page/product is recommended?
>
> Seeking something more than: write extensive blog posts about your product, pay a big blogging site to write about you

[note: zero replies — unanswered Ask HN, included as evidence the question gets asked with no consensus answer]

---

**Ask HN — "How and why I built a free AI Visibility / GEO tool"** — id 45753156 — u/linksku — 2025-10-29T21:16:51Z — https://news.ycombinator.com/item?id=45753156 — 2 points, 0 child comments captured

> A few months ago, I was given a rare opportunity to build a startup in an internal incubator at Amplitude (product analytics, like Google Analytics), here's how it went.
>
> The CEO said I could build anything I wanted related to AI, and I would be given funding and a team. Since I've done a ton of SEO, I considered building something for SEO, but I kept hearing: SEO is dying, people are using ChatGPT. Around the same time, I noticed that the latest YC batch had 2 companies that collected data from ChatGPT/Claude/Perplexity and helped brands show up more often and more favorably. This type of tool is known as "AI visibility" or "GEO". In addition, Profound, one of earlier AI visibility tools, had just raised $20M.
>
> I tried out a bunch of these tools and realized they were unhelpful or overly expensive. I figured I could build something better and cheaper, and combine it with Amplitude's existing data. [...] We've also hired a small engineering team to build the product, and now we're ready to show it off.
>
> Here's some information I've gathered on the top companies in the space:
>
> - Profound: the current market leader with $60 million in funding. [...] The pricing is $400/month for the basic plan
> - Ahrefs Brand Radar: popular with existing users of Ahrefs. Several Amplitude customers have tried it, but most of them have said that the prompts they provide aren't relevant to the company, making the analysis useless
> - Peec/Athena/Anvil/Hall AI/etc: I tried a bunch of them, they mostly felt like Profound with fewer features, though slightly cheaper
>
> Since there's not a big differentiation between these products, it comes down to price and UX.

[note: this item is about the GEO/AI-visibility tooling market rather than the practitioner role itself; kept as category-noise context per pull_purpose — a company (Amplitude) staffing an internal team to build a GEO product is indirect evidence of GEO becoming a budgeted function]

---

### "Who is hiring?" / "Who wants to be hired?" thread matches (job ads and freelancer self-listings, company-stated / self-reported)

**Comment — Ask HN: Who is hiring? (September 2026)** — id 49532259, story_id 49522897 — u/rbatista19 — 2026-09-02T05:54:47Z — https://news.ycombinator.com/item?id=49532259

> cloro | Founding Engineer, Data Scientist, Founding Operations, Founding Marketer | REMOTE (EU timezones) | Full-time | cloro.dev/careers/
>
> cloro is one API for search and AI answers. You send a query, we return Google, Google News, ChatGPT, Perplexity, Gemini, Grok and Copilot results as structured fields: the answer, the sources it cited, and the position each result held. Teams use it to measure whether their brand shows up in AI answers, and to stop maintaining eight scrapers that break whenever a provider changes its markup overnight.
>
> We are bootstrapped, remote across EU timezones, and small enough that every role below works directly with the founders.
>
> Open roles:
> * Founding Engineer | $80k-150k | backend and infra, heavy on large-scale collection.
> * Data Scientist | $60k-100k | turn our AI-search corpus into published research and track the engines as they change.
> * Founding Operations | $50k-80k | finance, ops, marketing and product systems.
> * **Founding Marketer | $40k-70k | own SEO, content, and visibility in AI search.**
>
> We work AI-native: Claude and Claude Code are in the loop daily across engineering, ops and marketing. Being genuinely good with these tools is part of the job rather than a bonus.

[pay figure: Founding Marketer role explicitly scoped as "own SEO, content, and visibility in AI search" at $40k-70k, EU-remote, bootstrapped startup]

**Comment — Ask HN: Who is hiring? (August 2026)** — id 49187963, story_id 49156683 — u/Anastasiia_Borz — 2026-08-05T19:45:57Z — https://news.ycombinator.com/item?id=49187963

> Looking for project-based/part-time lead-sourcing (automation) specialist and a person for a AI search optimisation.
> for theclaritycoaching.com
> Contact via linkedin.com/in/executivecoachana

[note: small business (executive coaching) looking for freelance "AI search optimisation" specifically, distinct line item from general marketing]

**Comment — Ask HN: Who is hiring? (June 2026)** — id 48359017, story_id 48357725 — u/caseyatevertune — 2026-06-01T16:26:30Z — https://news.ycombinator.com/item?id=48359017

> Evertune AI | Senior+ Engineers, Tech Lead, PM, Product Designer | NYC / Seattle | ONSITE/HYBRID | Full-time
>
> Work authorization: must be authorized to work in the U.S.; we are not able to sponsor visas at this time.
>
> Evertune builds AI-native software for enterprise marketing teams, spanning **GEO (generative engine optimization) products** for AI search / answer engines and AI advertising products, including new ways for brands to reach customers in AI-native surfaces. We're backed by Eniac and Felicis, and founded by people who helped scale The Trade Desk.
>
> Roles:
> * NYC only: Tech Lead Full Stack, Product Manager GEO, Product Designer
> * NYC or Seattle: Senior+ Full Stack Engineer, Senior+ Backend Engineer, Senior+ Backend Infra Engineer
>
> Comp: Eng $150k - $250k + equity; Designer up to $160k + equity; PM up to $180k + equity.

[pay figure: named role "Product Manager GEO" inside PM comp band up to $180k + equity, at a VC-backed vendor building GEO product for enterprise marketing teams — this is a vendor building the tooling, not a brand buyer]

**Comment — Ask HN: Who wants to be hired? (July 2026)** — id 48752533, story_id 48747975 — u/lightyoruichi — 2026-07-01T20:16:09Z — https://news.ycombinator.com/item?id=48752533

> Location: Nomading around SEA | Remote: Yes | Technologies: Python, SQL, n8n automations, PostHog, Google Tag Manager (GTM), Google Analytics 4 (GA4), Shopify Web Pixels, **Technical SEO, AEO/GEO indexing schemas**, HTML/CSS/Tailwind
>
> GTM/Growth Operator & Fractional CMO. I build data-driven marketing systems and organic acquisition engines, transitioning startups from paid ad dependency to compounding organic channels.
>
> What I've done for:
> - CPA firm, I built a technical search and AEO pipeline that replaced a $25,000 USD per month paid ad spend, scaling organic traffic from zero to 210,000 monthly visits and increasing leads by 10x.
> - For DTC-ecom brand, I restructured their checkout funnel [...] boosting site-wide conversion rate by 250% and generating >$1 million USD in annual revenue.
> - I designed an organic acquisition loop on Reddit that generated 300 active signups in 30 days with zero budget.
>
> Seeking contract, fractional, or full-time roles in growth engineering, technical product marketing, or growth operations.

**Comment — Ask HN: Who wants to be hired? (August 2026)** — id 49170177, story_id 49156682 — u/lightyoruichi — 2026-08-04T15:17:09Z — https://news.ycombinator.com/item?id=49170177

Same skill line ("Technical SEO, AEO/GEO indexing schemas"), same self-description as fractional CMO/growth operator. New line at the end:

> Seeking contract/fractional/full-time roles in growth, technical product marketing, dev rel, or growth operations.
>
> **Compensation: $30k-$50k annually**

[pay figure: self-described asking range $30k-$50k/yr for a fractional growth role listing "AEO/GEO indexing schemas" as one of several skills — lower than the Evertune/cloro vendor-side listings above, consistent with a part-time/fractional arrangement rather than FTE]

**Comment — Ask HN: Who wants to be hired? (February 2026)** — id 46870882, story_id 46857487 — u/lightyoruichi — 2026-02-03T13:44:30Z — https://news.ycombinator.com/item?id=46870882

> I go deep on **SEO/AEO** (including technical SEO + LLM optimization), funnel optimization, marketing automation, and analytics infrastructure. I write code to solve problems — landing pages, event tracking, conversion APIs, dashboards, whatever moves the needle.
>
> Looking for: Growth roles at early-stage SaaS (pre-seed to Series A) where I can own the full funnel and build systems from scratch.

[note: same author's self-listing three times over 2026 (Feb, Jul, Aug) shows "AEO/GEO" moving from a parenthetical ("SEO/AEO") in February to a named line item ("AEO/GEO indexing schemas") by July/August — self-positioning drift toward naming GEO explicitly as a sellable skill]

---

### Adjacent — pre-existing "will X become a real job title" discourse (outside GEO/AEO but same pattern, dated before the window; included as comparison)

**Story — "Why Prompt Engineers and LLMOps Engineers Will Become Real Job Titles"** — id 39435773 — u/benjaminwootton — 2024-02-19T22:48:19Z — 9 points — https://news.ycombinator.com/item?id=39435773

[note: title only; this predates the 2025-2026 GEO/AEO wave by roughly two years and concerns a different pair of titles (Prompt Engineer, LLMOps Engineer). Included only as a structural precedent for "will this stick as a real job title" HN discourse, not as GEO/AEO evidence]

## Pull notes — mechanical only

- Algolia HN Search API, no auth required, no rate-limit errors encountered (unlike Arctic Shift/Reddit, see companion Reddit raw file).
- Free-text query search (tags=story,comment) returns high false-positive rate on "GEO"/"AEO" because "geo" collides with geography, geospatial, geo-targeting, geo-testing (PPC), and company names containing "Geo". Filtering required both a GEO/AEO/AI-search keyword AND a role/job/title/salary keyword co-occurring in the same item before an item was kept.
- Targeted full-thread pulls (tags=comment,story_<id>) were used for: the three most recent "Who is hiring?" / "Who wants to be hired?" monthly threads (Sept, Aug, June 2026) and one AI-agent-readiness story (id 47805998) that surfaced heavy GEO discussion in the initial keyword search — full comment sets were then keyword-filtered locally rather than relying on Algolia's own relevance ranking, to avoid missing on-topic replies buried deep in large threads.
- item API (https://hn.algolia.com/api/v1/items/<id>) returned 404 for story_id 44383798 (the parent of the whitefables/Wise comment) — story appears deleted or the id captured from search results was stale; the comment itself was still retrievable via search and is kept, parent marked unavailable.
- story_id 46462347 ("SEO is dead, GEO is future") confirmed to have 0 comments via a separate tags=comment,story_46462347 query — not a truncation artifact.
- No login wall, no paywall encountered — HN and the Algolia API are fully open.

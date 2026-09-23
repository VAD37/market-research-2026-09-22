# Jonathan Mall — "GEO Experiment: 1,353 ChatGPT Queries Before and After" (anonymised 'Brand A')

```yaml
source:          Jonathan Mall (jonathanmall.com), practitioner blog, own test site
url_or_doc_id:   https://jonathanmall.com/en/geo-experiment-ai-citation-test/
published:       undated in captured text; experiment window July 2 to July 9 (year not printed in captured text)
pull_date:       2026-09-23
pull_method:     fetch (Python urllib); found via DuckDuckGo html search 'GEO case study control group ChatGPT citations' (WebSearch session cap reached)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     practitioner study with n, dates, method and a measured noise floor; site owner measuring own site, niche deliberately anonymised; no code or query set published
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT only (Google AI Overview named, no matched baseline)
metric_kind:     visibility (citations, mentions)
supersedes:      none
captured:        article body from key takeaways to closing line
verbatim:        partial — section named in captured
```

## Verbatim

> Key takeaways: A controlled before/after test on 1,353 identical ChatGPT queries showed a 5.3:1 citation gain one week after shipping a wave of decision-stage commercial pages. In plain terms:
> Do build pages for the moment someone compares, chooses, or budgets. Don't expect explainer guides to earn ChatGPT citations; here they went backward.
> Do test on hundreds of identical queries before and after. Don't trust a single ChatGPT check; the answer changes by itself two times out of three.
> Do expect movement within days of publishing. Don't confuse being linked (citations, which moved) with being named (mentions, which didn't).
> Generative engine optimization has a guessing problem. Most advice circulating right now reads like this: write FAQ blocks, add schema markup, get cited on Reddit, and ChatGPT will start naming you. Some of it is probably true. Almost none of it has been tested against a before-and-after measurement on a real site, with a control group, on the same domain, in the same week.
> I run that kind of test on a site I operate myself, in a competitive expert-services niche. Which niche, and whose site, I am deliberately keeping vague: the point of this series is the pattern, and the pattern travels; the specifics would only start arguments. Call it Brand A. The site runs as a controlled test bed: frozen query sets, before/after runs, a dated log of every change shipped, and enough discipline to report the parts that didn't work. This write-up covers the strongest result so far.
> What a controlled GEO test actually requires
> A real test needs three things: a large, frozen set of queries so single-query noise averages out; a genuine before and after, run on the same query set, close enough together that the world hasn't changed underneath you; and a way to tell signal from churn before you claim a win.
> The problem with most GEO case studies is the measurement, not the intervention. Someone changes a page, asks ChatGPT the same question three times, sees their name appear, and calls it proof. That is an anecdote dressed up as data, and as you'll see below, a single query can flip for reasons that have nothing to do with anything you shipped.
> Method: 1,353 matched queries, one week apart
> On July 2, I shipped 8 new pages and refreshed several existing high-intent pages on Brand A's site: freshness signals, structured answer blocks, and internal links. Everything shipped cleanly between two measurement runs, finishing by July 6.
> I run a frozen set of 1,353 unbranded queries (nobody typed the brand's name into the search box; these are demand-shaped questions of the "who is the best provider for X" and "what does X cost" variety) through ChatGPT. I had a baseline run from July 2, before the pages went live, and a repeat run on July 9, seven days after. Because the query set is identical and matched query-by-query, I can classify every one of the 1,353 as gained, lost, kept, or never-appeared, separately for citation (a link to Brand A's domain in the answer) and mention (Brand A named in the answer text).
> I ran this only on ChatGPT. Google's AI Overview had no usable baseline for this window, so any AIO numbers in this piece would be comparing two different things dressed up as a trend. One clean before/after beats two dirty ones.
> First, the noise floor
> Before touching the results, I had to answer an uncomfortable question: how much does ChatGPT's answer change on its own, with nothing shipped at all, just from re-asking the same question a week later? The answer is: a lot.
> 0.35
> mean Jaccard overlap of ChatGPT's top-5 brands, same query, one week apart
> 33%
> of queries where the rank-1 brand stayed the same brand, run to run
> Across all 1,353 matched queries, I compared the top five brands ChatGPT surfaced in each answer, run to run, using Jaccard similarity (a 0 to 1 score for how much two sets overlap). The mean was 0.35. The single brand at rank 1 stayed the same in only 33% of queries. ChatGPT reshuffles its own answers heavily from one week to the next, with no intervention required.
> That number is the whole point of running 1,353 queries instead of three. If you ask ChatGPT one question before your redesign and the same question after, and your name shows up, you have roughly a two-in-three chance that would have happened anyway. Anecdote-level GEO testing is measuring noise and calling it a strategy.
> Results: citations shifted 5.3:1, mentions stayed flat
> Against that 0.35 noise floor, here is what the intervention actually moved.
> Query state, run to run
> Citations
> Mentions
> Kept (yes before, yes after) 52 24
> Lost (yes before, no after) 32 27
> Gained (no before, yes after) 171 32
> Never (no in both runs) 1,098 1,270
> Same intervention, two different outcomes: citations moved 5.3:1 beyond churn, mentions did not move at all.
> Citations: 171 gained against 32 lost, a 5.3:1 ratio. That is not churn. A noise floor of 0.35 Jaccard does not produce a lopsided result like that by accident; something in the intervention moved the needle.
> Mentions tell a different story, and I want to report it as plainly as the win. Mentions gained 32, lost 27, a net of +5. That is inside the noise floor. Stable mentions' average position barely moved (2.04 to 2.17, seven improved, nine unchanged, eight worse). Whatever shipped in this wave got Brand A's pages cited far more often. It did not make ChatGPT say Brand A's name more often. Those are two different outcomes, and conflating them is exactly the kind of sloppy reporting this lab exists to avoid.
> For the same reason, a second null result belongs up front rather than buried: of 55 queries where ChatGPT was already citing the domain without naming the brand, only 5 converted to a named mention in the week after the structured answer blocks went live. Either eight days is too short for that mechanism to show up, or it structurally can't work on the process-style queries that dominate that pool (a "how does the process work" answer doesn't call out a name regardless of what's on the page). I don't know which yet. I'm reporting both possibilities rather than picking the one that sounds better.
> Attribution: what actually got cited
> Every one of the 171 citation-gained queries is attributable to a specific page in the ChatGPT answer. Ranked by how many queries each page pulled in:
> Citation-gained queries per page, week 1. All eight top gainers belong to the same family: pages built for a buying decision. The site's informational explainers are absent.
> Every single top gainer belongs to one family: pages built for the moment someone is deciding, comparing, or budgeting, rather than pages that explain a topic. I'm deliberately not publishing the exact formats and URLs; the pattern is the finding, and the pattern is what should travel. Informational guides, the explainer-style content most GEO advice fixates on, are absent from this list entirely.
> Page G deserves its own paragraph. It is a head-to-head comparison against Expert B, one of the most established names in Brand A's category. It wasn't just a new asset; it went from 5 to 23 citing queries (+18), and that lift landed precisely inside Expert B's home topic, which jumped from 19% to 35% presence in German-language answers over the same week. A comparison page against a well-known name seems to pull in that name's existing query demand, not just create a new page that competes on its own terms.
> The refresh treatment on existing pages compounded the same pattern: the treated page tripled its coverage, from 23 to 72 citing queries. Meanwhile Brand A's informational guides on its specialist topic, which received no treatment in this wave, went down on ChatGPT in the same seven days (one fell from 3 to 1 citing queries, another from 1 to 0, a third from 2 to 1). Same domain, same week, opposite direction, because one set of pages got the treatment and the other didn't. That is the quasi-control that makes this a page-level result rather than a "the whole domain got more authoritative" story. If it were a domain-wide effect, the untreated pages would have risen too.
> Speed was also measurable: the four pages shipped on July 2 earned 60 citation-gained queries within their first week, with three of them alone accounting for 29, 18, and 13. On ChatGPT's grounding, publish-to-citation latency is days, not months.
> What this means
> The clearest reading of this data: ChatGPT, at least for this domain and this query population, rewards decision-stage formats. Pages built for comparing, choosing, and budgeting got cited. Informational explainer content did not move, and where it existed untreated, it went backward in the same window.
> I don't think that generalizes to every engine. The same underlying dataset shows a structural difference in what ChatGPT cites versus what Google's AI Overview cites: ChatGPT favors the decision-stage pages above; AI Overview, in the same period, favored Brand A's informational guides and homepage, while pulling in YouTube, LinkedIn, and industry directories as ambient trusted sources far more than ChatGPT does. Two engines appear to be running two different reward functions on the same content. That comparison deserves its own careful before/after treatment rather than a paragraph here.
> Do this, not that: the practical version
> If you skip everything else, act on these five pairs. They are what the data in this test actually supports.
> Do publish comparison, cost, and how-to-choose pages. Not another "what is..." explainer; in this test, explainers earned zero new citations while decision pages earned all 171.
> Do write a head-to-head page naming a well-known player in your category. Not a generic roundup; the head-to-head imported the bigger name's query demand (5 to 23 citing queries in one week).
> Do refresh existing decision pages (current-year signals, direct answers, internal links). Not only new content; the refreshed page tripled its citation coverage, from 23 to 72 queries.
> Do re-check results after one week; this channel moves in days. Not on a quarterly SEO reporting rhythm; you'd be blind to what worked.
> Do treat ChatGPT and Google AI Overview as separate channels with separate content plans. Not as one "AI search" bucket; they rewarded opposite content types on the same site.
> What I'd test next
> A few things are queued: a second head-to-head page against a rising name in the category, a push on third-party profile freshness across industry directories (one directory alone drives a meaningful share of Brand A's AI Overview mentions, and third-party presence is an untapped lever on ChatGPT), and a proper split of the naming-conversion metric so structured answer blocks get tested only against list and recommendation queries, where a name could plausibly appear, rather than against process queries where it structurally can't.
> Method notes and limitations
> Five constraints define what this experiment can and cannot claim.
> Matched queries only. All 1,353 queries exist in both the baseline and the repeat run; unmatched queries were excluded rather than treated as new data.
> One engine (ChatGPT), because it was the only one with a genuine before-and-after on this query set. AI Overview references come from the same dataset's structural comparison, not a matched before/after, and are flagged as such.
> Single site, one-week window (July 2 baseline to July 9 repeat), all interventions shipped in the gap.
> The noise floor (Jaccard 0.35 on ranks 1 to 5, rank-1 stability of 33%) was measured before any result was interpreted as a win.
> Every number above is a count on identical, matched queries, never a rate computed across a changing query population. Rates across different query sets or measurement instruments are not comparable and are not reported as if they were.

## Pull notes — mechanical only

- Figures (Jaccard chart, per-page bar chart) are images, not captured; their captions are captured as text.
- source_label set to vendor-reported as the nearest template label: the author measures his own site; no product or fee is named on the page.

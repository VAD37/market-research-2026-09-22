# Hacker News (nworley) — "Ask HN: How does ChatGPT decide which websites to recommend?"

```yaml
source:          nworley (OP) and thread participants, Hacker News
url_or_doc_id:   https://news.ycombinator.com/item?id=46907123 (HN Algolia API: https://hn.algolia.com/api/v1/items/46907123)
published:       2026-02-05
pull_date:       2026-09-22
pull_method:     fetch (HN Algolia API, raw JSON, via curl)
pull_purpose:    evidence about category noise
tier:            6
tier_reason:     Discussion thread of practitioner opinion and anecdote. No participant states n, a date window, or a measured before/after figure for any claim made. Two commenters (quiqueqs of Cartesiano.ai, 13pixels) disclose they build or sell an AI-visibility tracking product while describing the same category's methodology, a direct vendor-measuring-what-it-sells conflict noted inline by quiqueqs themselves ("Disclaimer: I've built a tool in this space").
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT — no model version stated
metric_kind:     none
supersedes:      none
captured:        full page (post text) plus every comment in the nested tree, to full depth
vertical:        none named
evidence_grade:  Not a case — method write-up / community discussion, no quantified result claimed by any participant. No bar item is met with a number; several participants describe *mechanisms* (attribution gap, "Share of Model" / share-of-voice framing, temperature-driven prompt variance, crawl-vs-visit fingerprinting) without measurement. Filed as a method write-up per task instruction ("a-practitioner-..." naming), not graded as a case.
artefacts_published: none — no prompt set, dataset, or tool output linked by any participant
direction:       null — no result claimed
```

## Verbatim

**Post title:** Ask HN: How does ChatGPT decide which websites to recommend?
**Author:** nworley
**Points:** 5
**Created:** 2026-02-05T23:49:40.000Z

For years, SEO has meant optimizing for Google's crawler.
But increasingly, discovery seems to be happening somewhere else:
ChatGPT
Claude
Perplexity
AI-powered search and assistants
These systems don't "rank pages" the same way search engines do. They select sources, summarize them, and recommend them directly.
What surprised me while digging into this:
- AI models actively fetch pages from sites (sometimes user-triggered, sometimes system-driven)
- Certain pages get repeatedly accessed by AI while others never do
- Mentions and recommendations seem to correlate more with contextual coverage and source authority than traditional keyword targeting
The problem is that this entire layer is invisible to most builders.
Analytics tools show humans.
SEO tools show Google.
But AI traffic, fetches, and mentions are basically a black box.
I started thinking about this shift as:
GEO (Generative Engine Optimization)
or AEO (Answer Engine Optimization)
Not as buzzwords, but as a real change in who we're optimizing for.
To understand it better, I ended up building a small internal tool (LLMSignal) just to observe:
- when AI systems touch a site
- which pages they read
- when a brand shows up in AI responses
The biggest takeaway so far:
If AI is becoming a front door to the internet, most sites have no idea whether that door even opens for them.
Curious how others here are thinking about:
- optimizing for AI vs search
- whether SEO will adapt or be replaced
- how much visibility builders should invest in this now vs wait and see

---

### Comments (nested, full depth as returned)

**theorchid:**
This is especially important when launching new SaaS projects. Google does not trust new domains for the first 6-12 months. But if you publish information about your project on other sites, the AI will recommend your site in its responses. Just post a few times on Reddit, and in a week, GPT will be giving out links to your SaaS product. AI doesn't need exact low-frequency or high-frequency keywords like SEO does. AI is good at understanding user queries and giving out the right SaaS that solves their problem.

> **nworley (reply):**
> This matches a lot of what I've been seeing too. What stood out to me is that AI seems far less concerned with domain age than Google is. If there's enough contextual discussion around a product (ie. Reddit threads, blog posts, docs, comparisons) then AI models seem willing to surface it surprisingly early. That said, what I'm still trying to understand is consistency. I've seen cases where a product gets recommended heavily for a week, then effectively disappears unless that external context keeps [truncated by source].

**theorchid (second top-level comment):**
However, there is a lack of information when a user opens your website after interacting with AI. Google Search Console shows the user's query if the query is popular enough and your website is in the search results. Bing shows all queries, even if they are not popular, and if your website is in the search results. But if AI recommends your website when answering people's questions, you cannot find out what questions the user discussed, how many times your website was shown, and in what position.

> **nworley (reply):**
> This is exactly what set me off in trying to figure out the visibility gap. What's strange is that we're moving into a world where recommendations matter more than a click, but attribution still assumes a traditional search funnel. By the time someone lands on your site, the most important decision may have already happened upstream and you have no idea. The UTM case you mentioned is a good example: it only captures direct "AI to site" clicks, but misses scenarios where AI influences the decision [truncated by source].
>
> > **quiqueqs (reply):**
> > This is why most of these AI search visibility tools focus on tracking many possible prompts at once. LLMs give 0 insight into what users are actually asking, so the only thing you can do is put yourself in the user's shoes and try to guess what they might prompt. Disclaimer: I've built a tool in this space (Cartesiano.ai), and this view mostly comes from seeing how noisy product mentions are in practice. Even for market-leading brands, a single prompt can produce different recommendations day t[runcated by source].
> >
> > > **nworley (reply):**
> > > I don't think there's a clean solution yet but I'm not convinced brute force prompt enumeration scales either, given how much randomness is baked in. I guess that's why I've started thinking about this less as prompt tracking and more as signal aggregation over time. Looking at repeat fetches, recurring mentions, and which pages/models seem to converge on the same sources. It doesn't tell you what the user asked, but it can hint at whether your product is becoming a defensible reference versus a[truncated by source].
> > >
> > > > **13pixels (reply):**
> > > > Signal aggregation is definitely the right mental model. We've found that tracking 'Share of Model' over time (e.g. how often a brand appears in the top 3 recommendations for a category query) is much more stable than individual prompt outputs, which can vary wildly due to temperature. It's similar to share-of-voice in traditional PR. You can't control every mention, but you can track the aggregate trend of whether the model 'knows' you exist and considers you relevant.

**marcwajsberg:**
The attribution point is huge: the "decision" can happen in the model's answer, and your analytics only see the last hop. A practical mental model for recommendations is less "ranking" and more confidence: Does the model have enough context to map your product to a problem? Are there independent mentions (docs, comparisons, forum threads) that look earned vs manufactured? Is there procedural detail that makes it easy to justify recommending you ("here's the workflow / constraints / outcomes")? F[truncated by source]

**raw_anon_1111:**
Even if I did know, the last thing the world needs is for SEO folks to figure out how to game LLMs if they haven't already. SEO has made web search unusable and practitioners are the scum of the earth. But more practically like Raymond Chen said, if every app could figure out how to keep their windows always on top, what good would it do? The same with SEO.

> **nworley (reply):**
> Right there with you because SEO has evolved to a place that incentivizes a lot of bad behavior, and the end result made search worse for everyone. I'm personally less interested in "gaming" LLMs than understanding what they already do. From my side, this feels closer to observability than optimization when trying to see whether AI systems are even reading or understanding a site, not how to trick them into ranking something low quality. The Raymond Chen analogy brings up something interesting.[truncated by source]

**avin01:**
I think this shift is real, but I'm not convinced it turns into a clean new SEO anytime soon. From building LLM systems, it feels less like ranking and more about training data, reputation, retrieval, and how easy something is to summarize. If your content is shallow or fragmented, it just doesn't become useful to models, even if it ranks on Google. My worry is GEO/AEO becomes the same game SEO did, people optimizing for bots instead of users. The boring strategy still wins. Write good stuff, up[truncated by source]

**13pixels (second top-level comment):**
The shift to zero-click discovery is definitely real. We've been tracking this "AI visibility" metric internally too (using a mix of prompt injection and search monitoring) and found that brand mentions correlate strongly with structured data quality and entity clarity, rather than traditional backlinks. It seems like LLMs prioritize "authoritative entities" over "keyword-optimized pages". For example, if you're cited in authoritative industry reports or have a clear Knowledge Graph entity, you'[truncated by source]

**XCSme:**
AI traffic is really tricky because traditional analytics and SEO tools just don't capture it. Even basic UTMs often miss the "last hop" behavior from these systems, so it can feel like you have no idea how users actually reach your pages. One thing that helped us was using a self-hosted analytics setup [0] with session recordings to understand user flows coming from AI referrals. You get visibility into real behavior without sending data to third-party services. The drawback though, is that jus[truncated by source]

> **13pixels (reply):**
> Distinguishing 'AI Research' (crawling) from 'AI Referral' (user clicks) is the hardest part. Most agents (OAI-SearchBot, ClaudeBot) declare themselves in UA, but the actual click-through often strips the referrer or shows as direct/none. We've had some luck correlating 'time of crawl' with 'time of visit' to fingerprint AI traffic, but it's noisy. Self-hosted is definitely the way to go for raw logs though. GA4 obfuscates too much of this.

## Pull notes — mechanical only

- Retrieved via `https://hn.algolia.com/api/v1/items/46907123` (Hacker News Algolia API), full JSON including nested comment tree.
- Several comment bodies are truncated by the source page itself at render (HN Algolia's stored `text` field cuts off mid-sentence for some long comments) — marked `[truncated by source]` at the exact cut point; this is the API's own stored text, not a pull-side truncation.
- 15 comments total per the story's `num_comments` metadata; all returned by the API are transcribed above.
- Counted toward S5 (community thread volume): this is 1 Hacker News thread, 15 comments, dated 2026-02-05, found via HN Algolia query `AEO` / `answer engine optimization` search terms (see census file for the full discovery log).

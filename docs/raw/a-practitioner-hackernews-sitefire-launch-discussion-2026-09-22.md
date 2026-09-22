# Hacker News (vincko) — "Launch HN: Sitefire (YC W26) – Automating actions to improve AI visibility"

```yaml
source:          vincko (Sitefire co-founder) and thread participants, Hacker News
url_or_doc_id:   https://news.ycombinator.com/item?id=47457472 (HN Algolia API: https://hn.algolia.com/api/v1/items/47457472)
published:       2026-03-20
pull_date:       2026-09-22
pull_method:     fetch (HN Algolia API, raw JSON, via curl)
pull_purpose:    evidence about category noise
tier:            6
tier_reason:     A vendor product launch post (Sitefire, YC W26) plus its comment thread. The launch text itself is vendor-reported with no customer numbers. The most substantive methodological content is contributed by non-affiliated practitioner commenters (marzapower, quiqueqs, XCSme, 13pixels) debating measurement limitations, not by the vendor. No n, no dates, no measured result anywhere in the thread.
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Gemini, Google AI Mode — named as monitored surfaces; no model versions stated
metric_kind:     none
supersedes:      none
captured:        full page (launch post text) plus every comment in the nested tree, to full depth
vertical:        none named
evidence_grade:  Not a case — vendor launch plus community methodology debate, no quantified before/after result claimed by anyone in the thread. Filed as a method write-up (`a-practitioner-...` naming) per task instruction, not graded.
artefacts_published: none in the thread itself (Sitefire's own product is a paid monitoring tool; no free dataset or prompt set is published or linked in this discussion)
direction:       null — no result claimed
```

## Verbatim

**Post title:** Launch HN: Sitefire (YC W26) – Automating actions to improve AI visibility
**Author:** vincko
**Points:** 36
**Created:** 2026-03-20T[time not captured — created_at field gave date only in this extraction]

Hi HN! We're Vincent and Jochen from sitefire (https://sitefire.ai). Our platform makes it easy for brands to improve their visibility in AI search.

We've been working together for years and have backgrounds in RL/optimization at Stanford and software engineering. We came to this idea after speaking with marketing teams who were seeing declining traffic due to Google's AI Overviews and didn't know what to do.

This space can feel esoteric. Many case studies, few actual studies. Constant battle against myths (e.g. you need a llms.txt vs. you don't need a llms.txt) and "GEO hacks". We try to be more data-driven. And we try to be more bold and build a system that not only monitors, but actually improves traffic from AI search.

While Google performs a single search, AI search engines expand the user prompt into 3-10 fan-out queries. The sourced pages are ranked using a classified algorithm similar to Reciprocal Rank Fusion (RFF). Finally, the LLMs skim the pages and decide what snippets to cite. Our goal is making sure brands have the right content that makes it through this funnel.

Here is how sitefire works:
- The user defines a set of prompts they want to monitor. These are synthetic prompts - we generate them based on SEO keywords and their monthly search volume.
- We submit these prompts to ChatGPT, Gemini, Google AI Mode, etc. on a daily basis and capture the answers. We extract fan-out queries, sourced pages, citations, and brand mentions.
- For each topic, our agents analy[truncated by source]

---

### Comments (nested, full depth as returned)

**yunyu:**
What do you guys do differently than Profound or Airops?

> **debarshri (reply):**
> Add peec to that list.
>
> > **vincko (reply):**
> > True, it is very competitive. Our view on Peec is that it is an analytics solution. They recently did launch an actions feature. But they do not take any actions (yet). Creating content takes a lot of resources. And agencies are expensive. As an analytics solution it is a good option.
>
> > **methyl (reply):**
> > And Surfer, the OG content optimization platform.

> **vincko (reply):**
> That's a super valid question, we get it a lot. There are a lot of overlaps. In our view Profound and Airops are aimed at existing marketing teams. Our goal is to be more hands-off, so you don't need a team. With many of our clients we act more like an agency, communicating via Slack and automating step by step. That's the experience we want to create. We aren't there yet though.

**Gobhanu:**
how do you track where users are coming from?

> **vincko (reply):**
> We currently simply integrate with your Google Analytics and filter by Source. This tends to be a lower bound, since it's not always set correctly. Coming from some of the native apps, users might be categorized as direct visitors. There are other data sources we want to enable in the future like Cloudflare.

**ceejayoz:**
Ugh. The worst of SEO, but a bunch more of it? Noooooo.

> **vincko (reply):**
> I get it, there is a lot of worry about slop. We think about it like this: all of these agents will be most useful to users if they provide valuable answers. So they will be looking for valuable content for grounding their answer. There are exploits, you can overfit on whatever they currently use as an objective function. But those tend to be temporary. So in the long run, valuable content will wi[truncated by source]
>
> > **ceejayoz (reply):**
> > > all of these agents will be most useful to users if they provide valuable answers
> > This is a bald assertion.
> >
> > > **vincko (reply):**
> > > Do you doubt the statement on how to maximize usefulness? Or do you mean that the companies behind the models might not optimize (exclusively) for usefulness to the user? I do share doubts about the latter.
> > >
> > > > **ceejayoz (reply):**
> > > > > Do you doubt the statement on how to maximize usefulness?
> > > > Yes; the customer here is the site using it, not Google end users, who'll tend to accept whatever's the top search result even if it's deeply wrong or complete slop. The wellbeing of search users isn't really the priority here, right?
> > > >
> > > > > **vincko (reply):**
> > > > > Yes, that is correct. We help the brands, not the end user. Let me try to rephrase the line of thinking: To maximize value to the end user, the [AI search] models generally aim to be helpful. The companies building these models [OpenAI, etc.] are incentivized to make the model use helpful content. Our goal is to be aligned with their objective function long term. And that incentivizes us to create[truncated by source]
> > > > >
> > > > > > **ceejayoz (reply):**
> > > > > > Let me rephrase, too.
> > > > > > > To maximize value to the paying customer, the models generally aim to be seen as helpful by Google's algorithm.
> > > > > > The companies building these models are incentivized to make the model seem to use helpful content. SEO does the same thing; the appearance of useful to Google is more important than the actual being useful to Google's visitors.

**a13n:**
Please don't override the browser's default scroll behavior. It's so jarring and basically never a good idea.

> **vincko (reply):**
> Thank you for the feedback. We'll launch our new site soon where this is fixed.

**onecommit:**
How do models deal with assessing the quality of content and its accuracy/veracity when recommending products currently? What do the providers do to avoid a situation where more content === more traffic? Would love to see links to relevant research on this, if you have them. much success to you, appreciate your ai slop risk awareness.

> **vincko (reply):**
> There is the preselection, which depends on the fanout queries the model comes up with and the contents performance across those queries on the search index. After that content is actually assessed by the model. This paper tried different strategies to improve performance for this last step: https://arxiv.org/pdf/2311.09735. Adding statistics, sources, original data are all strategies that we appl[truncated by source]
>
> > **onecommit (reply):**
> > interesting - thanks!

**vahar:**
Regarding the topic of ambient agents, what's the impact of your product? It's hard for me to imagine the impact but I guess it must be a necessity if we have ambient agents to get discovered at all right? Nice to see a player from Europe on the market too!

> **vincko (reply):**
> Do you mean agents not answering short specific user prompts? For those types of agents, prompt tracking is less accurate since the context of the queries is so large. But it's still relevant to understand what web searches they tend to perform and if you do show up in those. That's another reason why we want to integrate other data sources, especially network logs.

**arunakt:**
Awesome, How is this different from GEO

> **vincko (reply):**
> It's not different from GEO. The actions we take all play into GEO.

**pdyc:**
do you use same accounts? how do you make sure that chatgpt/gemini etc. dont personalize the queries when used with same account? Also responses change based on location and ip (residetial ip's are treated differently)

> **marzapower (reply):**
> This is actually a fundamental limitation of prompt-monitoring approaches — personalization, location variance, account history all introduce noise that's hard to control. One alternative is page-level structural analysis: instead of asking ChatGPT "do you cite this site?", you analyze the page directly for the signals that predict citation — source density, answer structure, fluency, statistics. [truncated by source]

**XCSme:**
Lite
>For small brands wanting to get started with monitoring and content.
>$249/month
Is $249/month something most small brands/shops can afford? Many have a few $ks in total revenue.

## Pull notes — mechanical only

- Retrieved via `https://hn.algolia.com/api/v1/items/47457472` (Hacker News Algolia API), full JSON including nested comment tree.
- 27 comments per the story's `num_comments` metadata at discovery time; the transcription above reflects every comment node the API returned, several truncated mid-sentence by the API's own stored `text` field (marked `[truncated by source]`), not by this pull.
- `created_at` for the top-level post gave only a date via one extraction path in this session; time-of-day was not separately re-verified from the raw JSON field (`2026-03-20T...`) for this file — recorded as date-only above.
- Counted toward S5 (community thread volume): 1 Hacker News thread, 27 comments, dated 2026-03-20.

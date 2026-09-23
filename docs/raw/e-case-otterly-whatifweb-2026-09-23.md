# OtterlyAI — What IF Web case study

```yaml
source:          OtterlyAI (otterly.ai) blog
url_or_doc_id:   https://otterly.ai/blog/geo-case-study-whatifweb/
published:       2026-09-03 (last updated)
pull_date:       2026-09-23
pull_method:     fetch (Python urllib, browser User-Agent); links read from otterly.ai/case-studies and otterly.ai/blog/geo-gsvo/
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-published case or experiment with n/dates/method stated; vendor measuring with its own product, no third-party replication — bias flagged
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          "AI" generic; AI crawlers
metric_kind:     traffic (AI traffic)
supersedes:      none
captured:        article body from 'Last updated' line to related-posts footer
verbatim:        partial — section named in captured
```

## Verbatim

> Last updated September 3, 2026
> AI Search Experiences
> Ask a marketing manager whether AI search matters and almost all of them will say yes. Ask what they should actually do about it and the answers get thin fast. That gap is where What IF Web built a service.
> Isaac Farrow is co-founder of What IF Web , a creative studio in Christchurch, New Zealand. Two years ago they were a website agency. Today AI search is one of five service lines, sold as a health check plus a retainer, with citability as the headline KPI. This is how they built it, and where OtterlyAI fits in.
> At a glance
> Company: What IF Web, a creative studio in Christchurch, New Zealand. Marketing websites, branding, web applications, ongoing support, and AI search.
> Interviewee: Isaac, Co-founder
> Challenge: No reliable way to measure whether What IF Web or its clients appeared in AI answers. Manual prompt checks were the only method, and AI traffic was the only trackable KPI.
> Solution: OtterlyAI for prompt level citability, brand coverage, and agent analytics, powering both their own optimisation work and a productised client service.
> Results: AI traffic to their own site up +300% across 28 days versus the previous 28. Domain citations and brand coverage both up. AI search is now a sellable service line with defined KPIs.
> From website agency to creative studio
> What IF Web started as a website agency: strategy, design, build, then ongoing ad hoc work maintaining sites and adding pages. Isaac ran the development side, his co-founder ran design. Two client personas emerged and stuck: marketing managers at SaaS and tech companies, and business owners. Healthcare became something of an accidental niche, largely because most of those healthcare clients are software businesses.
> Then clients started asking questions the team could not answer with any confidence.
> “People don’t just go on Google now and click a blue link. They go to an AI, especially when doing research.”
> Isaac, Co-founder, What IF Web
> The first move was inward. Before packaging anything, they wanted to know whether they could make themselves more visible in AI answers. The more they learned, the more obvious the commercial opportunity became. Clients were already coming to them for technical website work and design. Adding AI search on top was, in Isaac’s words, a no brainer.
> The starting point: manual checks and one unreliable metric
> “For the most part we had no good way to track it. The only real way was manually going into ChatGPT or Claude and typing in the prompts we wanted to appear for.”
> Isaac, Co-founder, What IF Web
> Manual spot checks tell you what one prompt did on one day. They do not tell you what happens when a buyer actually goes looking. On the client side, the options were GA4’s AI assistant and Webflow Analyze, the latter only when a client was willing to pay for the feature. Both measure traffic. Neither measures whether a brand gets cited in the first place.
> That left two questions permanently open: are we showing up in AI answers at all, and when we are, is the brand described positively or negatively?
> “Before OtterlyAI we had nowhere to track that and there were no clear KPIs. The only real KPI was AI traffic, which we know is tricky with attribution.”
> Isaac, Co-founder, What IF Web
> What they sell is citability, not traffic
> This is the most defining decision in the whole offer, and it is a deliberately narrow promise.
> “We don’t sell traffic and we don’t sell leads. We sell citability across the tracked prompt set we work out with the client.”
> Isaac, Co-founder, What IF Web
> The prompt set is built with the client, not for them. The client is the one sitting in sales calls, so the client knows the buyer’s actual language. From there, domain citations per prompt becomes the primary metric, with brand coverage close behind. AI traffic is treated as the lagging indicator: the number clients get most excited about, and precisely the number What IF Web refuses to guarantee.
> Channel priority in the New Zealand market runs Google AI Overviews first, ChatGPT second, Perplexity and Copilot roughly tied for third, Gemini after that. Claude sits slightly outside that ranking as a channel Isaac considers important for their B2B clients specifically.
> The entry point: a health check, a custom skill, and four pillars
> Every AI search engagement starts with a review. To run it consistently, the team built a custom Claude skill fed with OtterlyAI’s published resources, academic papers on AI search, and their own four pillar model for assessing a site. The output is a score against existing content, available tracking data, and current authority signals.
> From there, two ways to act. Because they are a development agency, technical fixes are sold as a one off: robots.txt optimisation, sitemap coverage, structural clean up. Everything ongoing sits in a retainer.
> Most sites are technically fine. The content is where it falls apart.
> Most of their clients run Webflow, which handles a lot of technical infrastructure by default. Sitemaps generate automatically, robots.txt can be configured to explicitly allow AI crawlers, and sites the team built themselves already have the right switches on. The recurring gotcha is reference CMS collections, which need excluding from the sitemap rather than left in it.
> “Most sites we review have a decent technical setup. It’s the content where things really lack.”
> Isaac, Co-founder, What IF Web
> The pattern repeats across almost every audit. Genuinely good blog content that is not answer led. Headings written as statements instead of the questions people ask. No FAQs, no structured data. Comparison tables published as images an AI cannot read, or built as CSS grids instead of semantic tables.
> Agent analytics settled an argument
> Isaac’s favourite feature is agent analytics, and the reason is partly personal. AI search has attracted its share of quick fix promises, and one of them cost the team credibility with themselves.
> “We fell for this really early on. We added an LLMs.txt file to our site thinking it was this magical thing AI read.”
> “With agent analytics we can see clearly that the AI bots don’t visit that page. They go to your sitemap, your robots file, your homepage. Those are the entry points.”
> Isaac, Co-founder, What IF Web
> The same feature validated a restructure the team was nervous about. Top level service pages moved from keyword led labels like Webflow development and web design to solution led ones: marketing websites, AI search, branding, web applications, ongoing support. The keyword pages were preserved as sub services so rankings held. When OtterlyAI showed their strongest prompts were location specific, they added targeted pages for web design New Zealand and web design Christchurch. Agent analytics then confirmed AI crawlers were landing on exactly those pages.
> Proving it on themselves first
> “We needed to prove what we were going to do works before we tried to sell it to our clients.”
> Isaac, Co-founder, What IF Web
> What IF Web is currently its own longest running case study. AI traffic to their site rose 300 percent over a 28 day window compared with the 28 days before it. Domain citations and brand coverage are both up across their tracked prompts.
> Three levers did the work. Technical clean up came first. Then authority building, mostly on Clutch, which showed up as a heavily cited domain in their category. They optimised the profile and enforced entity consistency so the information there matched their website and other directories. They also ran a review push with key clients, and the honest read is that profile consistency moved the needle more than review volume did. Third, content: blog posts written directly against the prompts they were tracking.
> Generalists now, specialists later
> Right now nobody owns a dedicated slice of the AI search process. Isaac and one other developer are the main OtterlyAI users, with his co-founder increasingly involved. Everyone researches independently and then teaches the others what they found, mostly because everyone is interested enough to want all of it.
> “The more we learn, the more we realise there are little niches within this service where we need someone to become an expert.”
> Isaac, Co-founder, What IF Web
> As the service scales, Isaac expects real specialisation: someone on authority building, someone on content, someone on client relations, and possibly dedicated owners for YouTube and Reddit.
> High awareness, low certainty
> Isaac sees the same pattern in New Zealand that he sees in the global market, and it is the reason the service exists at all.
> “Around 90 percent of marketers are aware of what AI search is and know they need to do something about it. The issue is most of them don’t know what to do.”
> Isaac, Co-founder, What IF Web
> Their clients are marketing managers under pressure to have an AI search answer ready. What IF Web sells them the answer plus the measurement to back it up.
> What’s next: Reddit, YouTube, and the prompt data problem
> Reddit is high on the test list, since forum threads are among the most cited domains in the web design category. YouTube is higher still: Google AI Overviews lean heavily on video citations, and What IF Web has watched traffic decline on keywords where they still rank in the organic top ten. The complication is that only around 5.7 percent of YouTube videos cited in Google AI Overviews are short form, which means the cheap format is also the weak one.
> ChatGPT ads got tested and rejected. Targeting amounts to a location plus loose guidelines rather than real guardrails, which produced paid impressions on queries with no purchase intent behind them. The bigger constraint sits upstream of all of it.
> “Prompt research right now is a very, very educated guess. The second these platforms give us real data, that changes everything.”
> Isaac, Co-founder, What IF Web
> Until then, the team triangulates from Search Console data, client surveys, and sales conversations, and treats the tracked prompt set as a working hypothesis rather than a fixed truth.
> Why it works: confidence to sell something new
> The hardest part of launching an AI search service was not the technical work. It was standing behind a deliverable with no guaranteed return attached to it.
> “Offering citability was a little bit scary. There’s no tangible ROI. The more I’ve used OtterlyAI, the more comfortable I feel offering this to our clients.”
> Isaac, Co-founder, What IF Web
> Isaac points to the research, blog posts, and email updates as much as the product itself. In a field where a lot of loud advice turns out to be wrong, having a defensible source made the offer sellable. The 300 percent lift on their own site did the rest.
> Want to make AI search measurable for your brand or your clients? Learn more at OtterlyAI .
> TL;DR (AI Generated)
> Marketing websites, branding, web applications, ongoing support, and AI search.
> Top level service pages moved from keyword led labels like Webflow development and web design to solution led ones: marketing websites, AI search, branding, web applications, ongoing support.
> When OtterlyAI showed their strongest prompts were location specific, they added targeted pages for web design New Zealand and web design Christchurch.
> Basic summary
> Social Share or Summarize with AI ChatGPT Google AI Perplexity Claude Gemini X (Twitter) LinkedIn
> Related Posts:

## Pull notes — mechanical only

- Server-rendered page; tag-stripped, one line per block element; figures and embedded video not captured.
- Provenance: screened — not opened in raw/e-case-census-c13-2026-09-22.md line 126.

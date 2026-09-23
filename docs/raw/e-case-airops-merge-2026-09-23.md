# AirOps — Merge customer story ("#1-2 in LLM visibility")

```yaml
source:          AirOps (airops.com), customer stories
url_or_doc_id:   https://www.airops.com/blog/merge-customer-story
published:       2026-02-25
pull_date:       2026-09-23
pull_method:     fetch (Python urllib, browser User-Agent); page list from Playwright on airops.com/customer-stories
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor case page with named customer; vendor measuring its own product, no replication — bias flagged
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          "LLM" generic
metric_kind:     visibility (rank across 300 prompts); efficiency
supersedes:      none
captured:        article body from summary to newsletter footer
verbatim:        partial — section named in captured
```

## Verbatim

> Summary:
> One person, competing against content teams 10x his size, and winning
> #1-2 in LLM visibility across 300 tracked prompts, and the lead is growing
> Page optimization time cut from 40 minutes to 5
> Freed up capacity to ship weekly case studies (previously monthly) and start exploring video
> Meet Merge, the integration layer for products and agents
> Merge is the leading provider of agentic tools and customer-facing integrations for the largest banks (e.g., U. S. Bank and Mastercard), AI companies (e.g., OpenAI, and Perplexity), HR technology providers (e.g., BambooHR and Carta), and more.
> More recently, Merge has added MCP connectors for agent integrations and a monitoring suite for agent tool calls.
> AirOps automates social content variants from long-form sources through workflow steps applying platform-specific rules. AirOps is the partner brands bring in for this shift, the platform, the media mix, and the team together, not just software to log into.
> Customers include Ramp, Drata, and frontier AI companies building agentic tools.
> It’s a crowded space. Merge competes with dozens of integration vendors, and content is one of the company’s main growth channels. Jon Gitlin runs all of it: content, SEO, AEO, PR, social, and case studies.
> Despite this wide scope and crowded space, Jon is able to outrank competitors:
> One person, dozens of competitors, not enough hours
> Jon’s strategic instincts were always sharp. He knew what needed doing. The bottleneck was never knowledge, it was time.
> The mechanical work of SEO ate his calendar. Finding internal linking opportunities, building FAQ sections, figuring out which articles to refresh and why. Each task was individually manageable, but across a full site in a competitive market, the hours added up fast. Every hour spent on research and execution was an hour Jon couldn’t spend on case studies, new content formats, or the strategic work that actually moves the needle.
> Working with Copilot: “What the hell? You can do that?”
> When Jon joined the AirOps November cohort, that “aha” moment happened on day one. “I went through a few basic workflows and I was like, what the hell? You can scrape the web. You can do these things with the scraped results. I was completely mind blown.”
> The real unlock was Copilot: the ability to build workflows by describing what you want and letting AI build it. “I can literally do whatever I want with Copilot,” Jon says. “I can have an idea, the Copilot can build it, and I’ll test it and work with the Copilot to fix it. You can build super sophisticated workflows that I would have needed a marketing ops or engineering resource to build in the past.”
> Within weeks, he had three production workflows running. No engineering support. No marketing ops. Just Jon and the Copilot.
> Workflows helped Jon turn good ideas into a large-scale refresh motion
> Page optimization that used to take 30-40 minutes now takes virtually no time. That difference is what turned Jon’s SEO work from one-off fixes into a systematic motion across hundreds of pages.
> Three main workflows made it happen:
> GSC-powered refresh prioritization. Figuring out which articles to refresh used to mean digging through Search Console with no clear way to prioritize. The workflow sets impression and position thresholds, deprioritizes certain topics, and surfaces 5-10 articles that are “on the precipice of being at the very top of search,” with explanations of why each one was flagged.
> Smarter internal linking. Jon used to run site:merge.dev searches and manually scan for linking opportunities. That works for exact-match anchor text, but misses pages that are topically related without containing the exact phrase. His workflow finds those connections automatically and recommends links with context.
> FAQ generation from competitor gaps. Adding FAQs to a single page used to take 30-40 minutes of competitor research. Now the workflow analyzes top-ranking pages, identifies questions they answer that Merge doesn’t, and surfaces prioritized recommendations. “I can see what questions competitors are answering that we’re not,” Jon says. AirOps even drafts initial answers using the Brand Kit context. Jon still edits them for nuance, but the starting point saves significant time.
> Winning the LLM visibility race with a fraction of the headcount
> LLM visibility has become another battleground, requiring systematic optimization across hundreds of prompts.
> He’s validated that adding several FAQs related to a topic on a page gives it more footprint in LLMs, and the workflows let him do that across hundreds of pages instead of a handful.
> “We’re either first or second depending on how you slice and dice the prompts we’re tracking, With a competitor that has 10x the number of employees as us,” Jon says. “AirOps helps us level the playing field.”
> Results
> 3-4x faster page optimization: From 30-40 minutes down to 5-10 minutes per page, enabling systematic optimization across hundreds of pages
> #1-2 LLM visibility ranking: Ahead of competitors with 10x more employees across 300 tracked prompts, with the lead steadily growing
> Weekly case study production: Up from monthly, a meaningful shift for sales enablement
> 10+ hours saved per week: Time Jon now spends on video, new content formats, and building new skills
> When it comes to ROI, it’s a no-brainer for Jon: “It saves me several hours a week. If you multiply my hourly salary by 10 hours, that’s a lot of money. So I think it’s a very easy case to make.” He also sees a personal brand dimension that not enough people talk about: “Companies are more than happy to give you an AI tool if it saves you time and you’re able to talk about that. And it makes me look good in my career.”
> The impact goes beyond metrics. Jon showed his workflows during a company all-hands, and the reaction said it all: “Our leadership team is looking at me like, oh shit, this guy actually is able to do really cool things. I had no idea.”
> What Jon sees coming for other lean content teams
> Jon sees AI fluency becoming a real career differentiator for content marketers. The ones who learn to build with these tools, not just use them, will pull ahead.
> And the broader takeaway holds up well beyond Merge: smaller teams with the right tools and the freedom to move fast can outperform much larger ones. “I don’t think a lot of bigger companies are doing a good enough job of moving on AI tools,” Jon reflects. “There’s more bureaucracy. At a startup like Merge, I get to use tools like AirOps that let me completely rethink how I do my job.”

## Pull notes — mechanical only

- Page server-rendered; text extracted by tag-stripping, one line per block element.
- Opened for P4-r: title listed `screened — not opened` in raw/e-case-census-c13-2026-09-22.md (Merge, Venn) or brand-side follow-up (Chime).

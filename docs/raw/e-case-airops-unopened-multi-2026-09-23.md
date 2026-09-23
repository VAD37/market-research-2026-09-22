# AirOps — seven Pass 3 unopened customer stories (Kong, Conviva, two practitioners, Animalz, Bitly, Harvard Business Publishing, Rhetoric)

```yaml
source:          AirOps (airops.com), customer stories — seven pages
url_or_doc_id:   see per-section URLs
published:       per section
pull_date:       2026-09-23
pull_method:     fetch (Python urllib, browser User-Agent); page list from Playwright on airops.com/customer-stories
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor case pages; no AI-answer metric carried
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          per section
metric_kind:     none on AI-answer metrics (efficiency and workflow claims)
supersedes:      none
captured:        article bodies, seven pages
verbatim:        partial — section named in captured
```

## Verbatim

### https://www.airops.com/blog/kong-quill-story — published 2026-05-13

> Copy Page
> Kong builds the world's most adopted API gateway, powering connectivity for APIs, AI, and microservices at enterprise scale.
> Their marketing team is now one of the first to build with AirOps Quill: putting an AI agent to work on the kind of recurring analysis that usually lives in spreadsheets and gets done when someone has time (which, for most marketing teams, is usually a perpetual "later").
> Kong's AI search team already uses AirOps to drive visibility in AI search. Jell wanted to stretch the boundaries and see how Quill could support growth beyond search: starting with the operational work that powers lifecycle marketing.
> These are early days for agentic marketing, and Kong is helping define what it looks like when an agent handles the operational work so the team can focus on decisions. The results so far are just the beginning.
> The gap between having data and acting on it
> Kong's lifecycle marketing team sends a high volume of email campaigns across product launches, events, and nurture programs. The data from those campaigns exists, but making sense of it was a manual process.
> "I used to piece together campaign performance across multiple exports and dashboards," said Jell Khongkraphan, Sr Manager of Lifecycle Marketing at Kong. Every week meant pulling Marketo data, opening spreadsheets, and trying to spot patterns across hundreds of rows. By the time the analysis was done, the next send was already out the door.
> The question wasn't whether the data was available. It was whether the team could get to the signal fast enough to act on it.
> A Playbook that reads email performance and posts a weekly digest to Slack
> The Engagement Signal Playbook is the first component of APEX (Always-on Pipeline Education Experience), a larger internal system Jell is building for Kong's lifecycle marketing program. It pulls weekly email link performance data from a Google Sheet, analyzes click patterns across every campaign, and posts a formatted digest to Slack every Monday morning.
> Quill runs the analysis autonomously but knows when to check in: when it flags an anomaly or a campaign that needs a closer look, the team gets a clear signal before any recommendation goes out.
> The Playbook's core job is separating meaningful engagement from noise. In email marketing, raw click numbers can be misleading: a campaign might show healthy click volume, but if most of those clicks are landing on social media icons in the footer rather than the actual CTA, those numbers are inflating engagement without driving pipeline action.
> That's the exact blind spot that makes campaign-level click data unreliable. The Playbook breaks this down automatically, flagging which campaigns are driving intentional action and which ones need work.
> Jell went from idea to a working Playbook in a single session. "The part that surprised me was how quickly I could go from idea to a working draft," she said. "I had a real use case, real data, and a running Playbook in one session."
> First run already surfacing actionable findings
> The Playbook is still in early testing, but the first manual run delivered output the team could act on immediately.
> It identified Kong's API Management Webinar and the API + AI Summit emails as the strongest performers in the current dataset: the campaigns where a high share of clicks were going to the intended call-to-action rather than footer links. It also flagged several programs on the other end of the spectrum, where nearly all click activity was on social footer icons, a clear signal those emails need stronger CTAs or repositioned content.
> "Before Playbooks, we exported campaign data manually, opened a spreadsheet, and tried to find the signal buried in hundreds of rows," Jell said. "Now, the signal finds us."
> The goal from here is straightforward: catch underperforming campaigns before the next send, not after. And as the Playbook runs weekly, the team builds a baseline tied to the engagement metrics they care about most, making trend-spotting automatic rather than something that depends on someone having the time to dig in. Quill becomes a core part of how the team operates: not a tool they go to, but an execution lead that delivers the signal on schedule.
> What's next
> The Engagement Signal Playbook is just the first piece of APEX. Jell's next builds are cadence risk monitoring, to flag when send frequency is hurting engagement, and audience segment health, to surface which segments are going cold before they drop off entirely.
> Jell sees Playbooks as a new layer between data and decisions. "The biggest thing for marketing teams isn't just automation," she said. "It's that Playbooks make the analysis legible. The output is plain English that tells you what to do."
> Ready for an AI agent that actually moves your metrics? Meet Quill .

### https://www.airops.com/blog/conviva-quill-story — published 2026-05-13

> Copy Page
> Conviva is the digital intelligence platform that analyzes user behavioral patterns and agent conversations to continuously make your AI agent smarter.
> Their marketing team is now one of the first to build with AirOps Quill: connecting the dots between what prospects are actually asking on sales calls and the content the field team needs to answer those questions at scale.
> For a company sitting on thousands of hours of conversation data, the opportunity isn't just content production. It's turning real buyer signals into a repeatable content engine that drives growth in both traditional and AI search. These are early days, and Ari is building the system from the ground up.
> The signal was in the sales calls all along
> Every sales call contains buyer intent: the objections, the questions, the topics prospects care about most. For most marketing teams, that signal stays locked in call recordings or scattered across notes. Turning it into content meant listening to calls, pulling out themes manually, cross-referencing search data, and then briefing writers.
> "Quill solves for complexity," said Ari Moskowitz, Content Marketing Director at Conviva. "I don't get lost in prompts and steps. Once I decide on what I want to build, a Playbook shows each step clearly no matter how sophisticated or specific. I can iterate without getting bogged down in processes."
> Before Quill, Ari was stitching together Grids, Slack threads, and Claude MCP connections to do pieces of this work. It worked, but the process was manual and fragmented.
> A Playbook that mines Gong transcripts and produces sales-ready content
> Ari built a Playbook that pulls entire transcripts from Gong, mines them for objections and questions that match high-value search terms, and produces blog posts and ebooks that sales can use directly with prospects before and after calls.
> Quill runs the mining and drafting autonomously, but checks in with Ari before content ships: surfacing the draft, the source transcripts, and the search terms it mapped to, so the team stays in control of what goes out.
> The content isn't generic thought leadership. It's built from real conversations with real buyers, mapped to the search terms those buyers are using. The result: content that serves both organic visibility and direct sales enablement in the same motion.
> "Before Quill, we created Grids using the MCP connection on Claude," Ari said. "Now, we build Playbooks and adapt on the fly."
> The program is just launching, so results are ahead of it. But the shift in how Ari spends time is already clear.
> From manual assembly to quality control and ideas
> The Playbook automates the work Ari was previously doing by hand across multiple tools and threads. That freed up something more valuable than hours.
> "Playbooks automate the work I'm currently doing manually across Grids and Slack threads," Ari said. "I now focus on quality control and iteration. And thinking of my next big idea."
> That's the pattern across Quill's early builders: Quill becomes a core part of how the team operates, handling execution and connecting activity to the growth metrics that matter, while the human drives strategy and the quality bar.
> For a content marketing director at a company with Conviva's scale of conversation data, the pipeline of ideas is the asset. Quill is what makes it possible to act on them.
> Ready for an AI agent that actually moves your metrics? Meet Quill .
> ‍

### https://www.airops.com/blog/solo-quill-story — published 2026-05-13

> Copy Page
> Not every early marketer builds on a 50-person marketing team. Some of the first practitioners to build with AirOps Quill are independent consultants who run content strategy across multiple clients at once: managing different brand voices, different positioning, different compliance requirements, and doing it all without a team behind them.
> As AI search reshapes how buyers discover brands, the pressure to optimize for both traditional and AI visibility is compounding. When you're juggling five brands, every hour spent on repetitive optimization for one client is an hour stolen from another.
> Deepshikha Dhankhar , Product Content & AI Strategist, and Christopher Iwundu , Content Marketer & AI Content Engineer, are both building Playbooks that turn their strategic expertise into repeatable systems. The practitioners serving multiple clients are often the ones who see the compounding value first.
> The multi-client grind
> When you're an independent practitioner, the manual work limits how many clients you can serve well. For Deepshikha, that meant manually layering AEO and GEO elements onto SEO briefs after the fact, for every client, every piece. The optimization knowledge existed in her head, applied one brief at a time.
> For Christopher, it meant spending a full week building out a content strategy from scratch for each new engagement: gap analysis, keyword research, content calendars, LinkedIn plans. The same process, repeated from zero every time.
> "Usually, we created just SEO briefs and then I'd manually add the AEO and GEO elements, which can get exhausting," Deepshikha said. "Before Quill, we relied on individual power users. Now, we can enable everyone to perform like one."
> Christopher hit the same ceiling from the strategy side. "Quill saved me about a week of work I would typically spend building a problem-first content strategy," he said. "While still delivering detailed outputs that covered angles I might have overlooked."
> Playbooks that work across every engagement
> Deepshikha's first Playbook was an SEO/AEO/GEO content brief template designed to stretch across marketing, product, and sales. Anyone on the team can run it with their own inputs.
> "Think about a product launch where you need an article, a help doc, a video script, a one-pager, a newsletter, sales material: all with unified tone and brand messaging," Deepshikha said. "What would typically take five calls with ten people over three days can happen in one day and a final legal sign-off."
> The real shift isn't just speed. It's removing the coordination overhead that slows every cross-functional launch. Five product launches across different departments no longer means five rounds of alignment meetings. The messaging stays tight because the Playbook enforces it.
> Christopher also took an ambitious swing. His first Playbook generates a full 3-month content strategy: content gap analysis, research, SEO/AEO strategy, content calendar, briefs, and a connected LinkedIn content strategy with daily draft copy.
> The depth is what surprised him. "Quill saves significant time and effort," Christopher said. "But its autonomous nature also improves output depth, because the system can explore angles and steps a user might miss building Workflows step by step."R
> Context and checkpoints that keep multiple brands straight
> Both practitioners pointed to the same shift: Quill holds the context so you don't have to re-specify it every time. Brand kits, knowledge bases, product positioning: all of it gets applied automatically rather than added manually at each step. When you're managing five different brands, that's the difference between trusting the system and second-guessing every output.
> "Connecting brand context is essential," Christopher said. "Quill makes sure all the writing rules, positioning, and audience context for each of my clients are implemented automatically."
> Christopher also pointed to human review checkpoints as a key part of the process. During a recent content strategy Playbook run, Quill generated an artifact that consolidated brand context up front. Christopher reviewed and approved it before the system proceeded with the run.
> That checkpoint pattern is especially valuable for freelancers managing multiple brands: it keeps the operator and the system aligned on context before execution goes deeper.
> Deepshikha tested the same workflow in Claude for comparison. The output wasn't close.
> "Quill can refer to integrations owned by AirOps, basically whatever I call for," she said. "With Claude, if I'm not already integrated, it just doesn't work the same way."
> What's next
> Both are already building their next Playbooks. Deepshikha is working on extracting SME insights from LinkedIn profiles, building topic clusters from fan-out queries, and converting CEO posts into Reddit threads with platform-specific guardrails.
> Christopher is turning his problem-first topic generation framework into a Playbook that extracts pain points from Reddit, G2, and forums, then converts them into content topics. He's also building a Playbook that analyzes GSC data and turns it into revenue-focused content opportunities.
> "There's so much to do and so little time," Deepshikha said. "I can't stop thinking about what to build next."
> For teams of one managing multiple brands, the compounding value of Quill looks different than it does for a large content org. Every Playbook run feeds back into the growth metrics that matter: search visibility, citation rates, content velocity across clients. Every Playbook you build is a system that works across every client. Every checkpoint you set is one less context-switching mistake. The more engagements you run, the more the investment pays off.
> Ready for an AI agent that actually moves your metrics? Meet Quill .

### https://www.airops.com/blog/animalz-quill-story — published 2026-05-13

> Copy Page
> Animalz is one of the most respected content marketing agencies in B2B SaaS, working with brands like Spotify, Rilla, and Atlassian to produce high-quality content at scale.
> Their team is among the first to build with AirOps Quill: and they didn't just adopt it. They tested it head-to-head against their existing Workflows to see which produced better output.
> The answer was decisive. For an agency whose reputation depends on quality across every client engagement, that kind of rigor is exactly how the shift to agentic marketing should be evaluated.
> Playbooks across multiple clients and their own brand
> Animalz is building Playbooks for both client work and internal content. They've already stood up several:
> A Refresh Brief + Content Writer pair that takes a blog URL, diagnoses its strategic role, recommends a refresh approach, and produces a draft plus a structured claims ledger.
> A Writer Playbook for a client that turns content briefs into drafts with first-party-verified pricing and product claims.
> A Derivative Writer that spins long-form interviews and data reports into smaller pieces.
> An always-on AEO Playbook that updates an article, reviews the results a month later, and makes new optimizations based on what it finds.
> The claims ledger is worth calling out. Animalz instructs the agent to maintain a CSV that logs every source it consults, including links and whether each is a primary source. "It creates a handy reference file for us humans," Tim said. "But we also find it forces the agent to pay more attention to the sources it consults and includes."
> That checkpoint pattern is key: Quill handles the research and drafting autonomously, but pauses for human review on source verification and claims before anything ships.
> "We stretched Workflows past what they were built for"
> Animalz had been building with AirOps Workflows for a while, but the complexity was growing faster than the tooling could handle. Every new constraint in a content production process became another step, another JSON schema, another parser glued onto an existing chain.
> "Before Playbooks, we stretched Workflows past what they were built for," said Tim Metz, Director of Content Engineering at Animalz. "Every new constraint became another step, another JSON schema, another GPT parser glued onto a Claude step. Now we brief the agent like a mid-level strategist and read its scratchpad to see how it got to its calls."
> That shift, from designing a step-by-step process to briefing a competent coworker, is the core of what changed.
> Head-to-head: Playbook vs. Workflow on the same brief
> In late April, Animalz ran a direct comparison between an autonomous Playbook and their equivalent Workflow on the same content brief. The Playbook won on every dimension they measure: brand-kit compliance, factual verification, structural fidelity to the content type, and more.
> The most concrete finding: the Playbook autonomously fetched first-party vendor pricing pages mid-reasoning and corrected 10 stale claims across three drafts in a comparison/alternatives content space. The Workflow, given the same keywords, defaulted to generic "check the vendor's website" prose without ever actually fetching.
> On the client side, the results showed up in review cycles. A content lead approved three Playbook-produced drafts in a single review pass. Equivalent Workflow drafts had been bouncing through multiple revision cycles to reach the same bar.
> What's next
> For an agency running content across dozens of clients, the implications compound. As AI search reshapes how buyers discover brands, the content quality bar is only going up: and agencies that can meet it at scale will define the next era of content marketing.
> "Quill is flexible and intelligent," Tim said. "You spend less time tinkering with minuscule steps and more time on strategy, quality, and inventing new content services that Playbooks make possible."
> Ready for an AI agent that actually moves your metrics? Meet Quill .

### https://www.airops.com/blog/bitly-quill-story — published 2026-05-13

> Copy Page
> Bitly is the platform behind billions of short links and QR Codes used by brands around the world, helping teams measure and optimize digital engagement across every channel.
> They're also one of the first teams building with AirOps Quill: testing what it looks like when an AI agent runs your marketing Playbooks, not just assists with them.
> These are early days for agentic marketing, and Bitly is helping define what it looks like in practice: building the content engine that drives growth in both traditional and AI search. The results so far are just the beginning. AirOps is the partner behind that shift: the platform, the media mix, and the team together, not just software to log into.
> 100+ integration and competitor pages with a full content lifecycle
> Quill let Bitly unleash their creativity across many strategies, right out of the gate. They built Playbooks for content refresh briefs, net new content briefs, and full blog posts.
> Then they pushed further: 57 programmatic integration pages, 53 competitor comparison pages, and a competitive playbook, all generated through Playbooks and connected to an existing Workflow that formats and pushes content directly to WordPress.
> Here's an example of the natural-language Playbook, created with Quill:
> And here is an example of the kinds of integration pages it can create:
> This was all within the first couple of weeks.
> The build process was a fraction of what it would have been before. The team described their requirements to Quill, uploaded page templates as PDFs, and let Quill structure the playbook. Once the Playbook was dialed in, they could generate pages at volume without starting from scratch every time they shifted to a new page type.
> Quill handles execution autonomously but knows when to check in: before content pushes to WordPress, the team reviews and approves. "No matter how sophisticated the Playbook gets, we always have a good overview of what each step does," Drews said. "If we want to make a tweak, it's often as easy as adding another sentence or example, or asking Quill to make the update."
> Weeks to days on content production, with humans still driving quality
> The efficiency gains showed up fast. Bitly's team compressed time to production from weeks to days and streamlined the number of touchpoints needed to move content from idea to publication: a content engineer builds the playbook, a human editor reviews and refines the output.
> "We were able to go from 4-6 touchpoints down to two: a content engineer and a content editor," said Tyler Roehmholdt, Director of SEO Strategy & Website at Bitly. That's not about removing humans from the process. It's about removing unnecessary friction.
> On the content side, refreshed blog posts have consistently seen higher average position, along with increases in impressions and clicks. The 57 programmatic integration pages that are already live: too early for conclusive traffic data, but the team was thrilled with the quality, and already expanding their Playbooks for the next page type.
> The bigger shift is capacity. When a given month requires more content, the team doesn't need to slow down. They run the Playbook.
> "AirOps enables us to test out new ideas and demand capture surfaces at much greater velocity than traditional experimentation," Roehmholdt said.
> From complex workflows to natural language execution
> Bitly's growth team had the strategy. What they needed was a faster way to execute it. Their existing Workflows were powerful but a limiting factor to experimentation: intimidating to set up, and difficult to debug when something needed troubleshooting.
> "Workflows can look very intimidating, and it's easy to lose oversight once they get more complicated," said Roland Drews, SEO & Content Acquisition Manager at Bitly. "If something didn't work right, it could be difficult to figure out even which step was causing the problem."
> That's one gap Quill is designed to close. Instead of configuring multi-step workflow chains, teams describe what they want in natural language. Quill is the agent captain that runs your Playbooks autonomously: handling content creation, refresh, and optimization while keeping your team in the loop at the moments that matter.
> What's next
> Bitly's team is thinking about this shift beyond any single project. "With agentic tools, the real benefit comes from thinking about processes holistically," Drews said. "Instead of asking an AI tool to help you write a single blog post, think about building a process you can use for this purpose repeatedly."
> The setup takes longer upfront. But once a Playbook is running, it delivers with greater efficiency, consistency, and confidence than any one-off prompt could.
> Ready for an AI agent that actually moves your metrics? Meet Quill .

### https://www.airops.com/blog/harvard-business-publishing-and-airops — published undated — no date on page

> Summary
> Rich text H1 1: Refresh Underperfor...
> Example H3
> Example H4
> Example H5
> Example H6
> Work with us
> Work with us
> ​
> Open with ChatGPT
> ​
> Open with Claude
> ​
> Copy Page
> Summary:
> 12x faster workflow content creation per lesson rubric.
> Achieved 95% independence and workflow self sufficiency through targeted enablement.
> Scaled rapidly from 1 pilot activity to 6+ AI-powered learning experiences in under 6 months.
> Enabled non-technical learning designers to build, test, and deploy precision AI workflows.
> The Customer
> Harvard Business Publishing (HBP) is a global leader in learning innovation, dedicated to developing the next generation of business leaders. One of its standout offerings, HBR Spark, features “Leadership Labs”—immersive, scenario-based practice activities designed to build real-world leadership and management capabilities.
> Under the leadership of Jennifer Long , Director of Learning Experience Design, HBP is constantly pushing the boundaries of learner engagement, aiming to deliver personalized, scalable feedback. Recognizing AI’s transformative potential, the Learning Experience Design team turned to AirOps to help build internal AI expertise and accelerate their journey toward cutting-edge innovation.
> The Problem
> HBP wanted to enhance their learning experiences in HBR Spark through personalized, rubric-based feedback powered by AI.
> While the first pilot activities were promising, the process proved resource-intensive, and required extensive support from AirOps' solutions architects. This limited the HBP team's ability to rapidly self-sufficiently grow across additional learning scenarios and constrained their potential for innovation.
> The key operational and skill-based challenges included:
> A considerable amount of time was needed, with initial AI-driven tasks taking several months to complete.
> The process depended on external support for workflow design, testing, and AI model optimization.
> There were also gaps in areas like AI prompting, rubric-based evaluation, and efficient workflow execution.
> "Initially, creating a single learning activity took months. Introducing AirOps shortened our delivery time, but introduced the complexity of new workflows. We co-built with AirOps, but relied on their external technical expertise to scale and modify at critical junctions. We saw it as an opportunity to develop deeper internal capabilities." — Jennifer Long, Director, Learning Experience Design at Harvard Business Publishing ‍
> A sample curriculum within HBR Spark The Solution
> To support HBP’s internal team, AirOps provided a tailored AI program focused on their learning design needs. Through live workshops, hands-on training, and expert support, the HBP team quickly became skilled at independently creating, testing, and deploying advanced AI-powered learning experiences.
> The targeted enablement program included:
> Three live training sessions covering prompt engineering, workflow building techniques, and best practices for quality assurance testing.
> Step-by-step guided sessions, where the team built AI workflows from scratch.
> Reusable workflow templates and a flexible architecture, allowing HBP to replicate workflows for new scenarios, from moderation to evaluation.
> Interactive sessions and office hours that addressed real-time questions, encouraging immediate practice and a deeper understanding.
> Team participants particularly valued:
> Clear explanations of complex topics like dynamic inputs, conditional logic, and content evaluation.
> Opportunities to build and test workflows directly tied to their actual learning experiences.
> Expert guidance from AirOps Solution Engineer, Cindy, whose responsive support accelerated internal mastery.
> "The training was hugely impactful—going 'soup-to-nuts' through our real workflows filled critical knowledge gaps. Cindy's deep expertise, structured sessions, and responsiveness transformed our team's capabilities."
> — Jennifer Long, Director, Learning Experience Design at Harvard Business Publishing ‍
> Always be learning: Live session within the AirOps Content Engineering Cohort The Impact
> With AirOps’ focused support, HBP sped up the process of incorporating AI-based feedback into their Spark learning experiences. The internal team now handles the design, development, and management of precision workflows on their own, reducing the need for outside help and driving innovation at scale.
> Key measurable outcomes include:
> Faster Workflow Creation : Cut creation time from months to about 40 hours per interaction.
> Quick Innovation and Growth : Expanded from 1 pilot activity to over 6 AI-driven learning experiences in under 6 months.
> Stronger Internal Skills : Achieved 95% independence from external technical support, enabling rapid testing of new ideas.
> Improved Operational Efficiency : Freed up internal resources by removing bottlenecks caused by reliance on outside help.
> Confident Team Culture : Gave non-technical learning designers the confidence to prototype and innovate, tackling advanced projects like audio-based activities and conversational AI roleplays.
> With strengthened internal AI expertise, HBP is well positioned to lead innovation in personalized and scalable learning experiences, and to deepen engagement in their learning products.
> “The transformation was remarkable. Our team went from being heavily dependent on external expertise to becoming 95% self-sufficient. The structured training gave our learning designers the necessary skills to independently optimize and build workflows with confidence.” — Jennifer Long, Director, Learning Experience Design at Harvard Business Publishing Unlock Your Team's AI Potential with AirOps
> Ready to empower your team and rapidly scale your content operations?
> Schedule an enablement strategy session today and discover how AirOps can help your organization build deep internal AI capabilities, accelerate innovation, and deliver transformative learning experiences.

### https://www.airops.com/blog/rhetoric-saves-engineering-headcount-and-ships-faster-with-airops — published 2023-12-19

> Copy Page
> The Customer:
> Daniel Scarr is the Chief Product Officer at Rhetoric , a legal tech platform that aids lawyers by analyzing judges' language from opinions and transcripts. Rhetoric's platform offers detailed insights into judges' language preferences and personalities, and their litigation insights engine helps litigators tailor their arguments to the judge presiding over their case.
> In this post, Daniel talks to us about building the Rhetoric platform and how AirOps empowers their whole team to build with AI, saving them valuable engineering cycles.
> Rhetoric's Team Problem:
> Rhetoric has a bold vision to help lawyers write more persuasive legal briefs for their cases assisted with AI. As an early-stage startup, they lacked the resources of larger companies to hire dedicated teams to build custom AI workflows. They needed a way to scale their resources and empower their whole team to build with LLMs.
> Rhetoric's Legal Insights Engine Solution:
> Rhetoric turned to AirOps for its user-friendly interface, one-click access to multiple large-language models (LLMs), and low-code builder studio that enables non-engineering team members to prototype and iterate on prompts and other AI techniques. Rhetoric also built an AirOps workflow to automate the research process for collecting judge information, which had previously proven challenging and time-consuming.
> What is an LLM?
> A large language model (LLM) is a type of artificial intelligence model that has been trained to recognize and generate vast quantities of written human language
> Impact:
> Rhetoric estimates they are saving at least one engineering headcount (est. $200k+ annually), and have accelerated their speed of deployment using AirOps. They now can get a production-grade prototype live in minutes instead of days - increasing release cycles by 5-10x!
> Building a custom AI tool would not have been viable for the early-stage company, and using AirOps resulted in significant gains in time, effort, and cost.
> AirOps aggregates pages due for refresh by correlating organic traffic decay with AI citation gaps across providers.
> We've recommended AirOps to others many times. The user interface makes it possible to do complex work simply and it's clear that many companies and individuals could benefit from a streamlined experience when dealing with an otherwise burdensome clutter of AI tools.
> ‍
> — Daniel Scarr, Chief Product Officer at Rhetoric Key AirOps Features:
> Prompt Studio for building, testing, and evaluation prompt chains with Large Language Models (LLMs)
> Web-search and scraping steps to automate research processes
> Easy connection of workflow outputs to S3 database via API step
> Get Started with AirOps:
> Getting started with AirOps for your AI workflows is easy! Ready to get started with AirOps? Book a call with our team here .
> AirOps is the partner for this work: the platform and our team together, not just software to log into.

## Pull notes — mechanical only

- All seven listed `screened — not opened` in raw/e-case-census-c13-2026-09-22.md line 157 (Rhetoric listed in c13 line 156 as opened-no-AI-metric group title; re-opened here).
- Fetched 2026-09-23 via Python urllib; tag-stripped.

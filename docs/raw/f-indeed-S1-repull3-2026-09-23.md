# Indeed — S1 posting bodies, re-pull 3: Indeed walled on page 1; six bodies read from employer career sites

```yaml
source:          Indeed (indeed.com) viewjob pages — walled; bodies then read from employer career sites: jobs.walgreens.com (TalentBrew), choicehotels.wd5.myworkdayjobs.com (Workday), jobs.ashbyhq.com/a-place-for-mom (Ashby posting API), mahec.wd5.myworkdayjobs.com (Workday), cigna.wd5.myworkdayjobs.com (Workday), att.jobs (TalentBrew)
url_or_doc_id:   https://www.indeed.com/viewjob?jk=aa146ce1b56eec6a (walled); employer URLs per section below
published:       per section — datePosted / startDate as the employer page states; Indeed card ages as of 2026-09-23 in the superseded file
pull_date:       2026-09-23
pull_method:     browser (claude-in-chrome) for Indeed — one page, walled; fetch (curl, User-Agent "market-research-bot contact: research@example.invalid") for the employer career pages and ATS JSON endpoints
session:         Indeed wall page header showed "Sign in"; no login, form, verification or CAPTCHA touched
pull_purpose:    evidence about a number
tier:            3
tier_reason:     demand-signals.md S1 default ("3, employer's own posting"); bodies are the employer's own posting text on the employer's own careers site or ATS
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          per section — engines named in each body are listed under "Phrase check"
metric_kind:     none
supersedes:      docs/raw/f-indeed-S1-repull2-2026-09-23.md (card fields only; bodies unread)
captured:        Indeed wall page text; full posting body for 6 of 35 cards (#22 Walgreens, #21 Choice Hotels, #4 A Place for Mom, #6 MAHEC, #20 The Cigna Group, #2 AT&T); employer-site search results for 6 more employers where the card's posting was not found
verbatim:        posting bodies verbatim as the ATS or JSON returned them, HTML tags stripped, list items one per line; Walgreens and AT&T bodies cut to the posting section (site navigation, footer, job-alert form and EEO boilerplate removed, marked)
```

## Access log — verbatim page states

1. 2026-09-23 16:21 local: navigate `https://www.indeed.com/viewjob?jk=aa146ce1b56eec6a` (card #22, Walgreens) in a new extension tab. Page title "Just a moment...". Page text: "Additional Verification Required / Your Ray ID for this request is a3f87a4098e73f67 / Return home / → / Troubleshooting Cloudflare Errors / Need more help? Contact us". Screenshot: a Cloudflare "Verify you are human" checkbox widget between the Ray ID line and "Return home"; header "Sign in". **Indeed channel stopped at page 1 per brief.** Not reloaded. Tab closed. 0 of 35 posting bodies and 0 of 34 remaining queries read on Indeed.
2. Employer career sites, curl, 16:22–16:27: jobs.walgreens.com search-jobs HTTP 200, posting found; careers.choicehotels.com HTTP 200 → Workday CXS search "Social Media" total 3, posting found; aplaceformom.com/about/careers HTTP 200 → Ashby posting API 39 jobs, posting found; mahec.net/about-us/employment HTTP 200 → Workday CXS search "Marketing" total 2, posting found; Cigna Workday CXS search "Technical Search SEO" total 1, posting found; att.jobs search-jobs HTTP 200, posting found at 4 locations (Bothell read).
3. Not found on the employer's own site: see §Checked, not found.

## Verbatim — posting #22, Walgreens, "Senior Manager, Performance Search & AI Marketing"

- Employer URL: https://jobs.walgreens.com/en/job/deerfield/senior-manager-performance-search-and-ai-marketing/1242/100446991664
- Indeed card: jobkey aa146ce1b56eec6a, "12 days ago" as of 2026-09-23, "$125,000 - $218,750 a year"
- Employer page JSON-LD: `"datePosted": "2026-9-10"`, `"identifier": "1850903BR"`, hiringOrganization "Walgreens", jobLocation "200 WILMOT RD, DEERFIELD, IL 60015"
- Phrase check (body, case-sensitive substring counts): "Generative Engine Optimization" 1; "GEO" 1; "AI assistants" 2
- Employer size text in body: "Walgreens has approximately 220,000 team members, including nearly 90,000 healthcare service providers"; "approximately 8,500 stores throughout the U.S. and Puerto Rico"; "nearly 9 million customers and patients each day"
- Company snapshot box: none on the employer page. [note: Indeed's own company snapshot not reachable — wall]

[note: site navigation above "Senior Manager, Performance Search & AI Marketing / Address:" and the share / job-alert form after "Salary Range" removed]

> Senior Manager, Performance Search & AI Marketing
>  Address: 
>  200 WILMOT RD,DEERFIELD,IL,60015-04620-00001-2
>  Job ID 1850903BR 
>  Apply Save job
>  Job Summary:The Senior Manager, Performance Search & AI Marketing partners with Marketing Leadership, Retail Media and Digital leadership, agency partners, and cross-functional stakeholders to develop and execute enterprise performance marketing strategies that drive customer acquisition, engagement, conversion, and business growth. This role serves as the enterprise lead for Paid Search and AI-driven Discovery, overseeing strategy, investment planning, optimization, measurement, and innovation across search and emerging performance channels. The position is responsible for translating business objectives, customer priorities, and full-funnel marketing strategies into measurable performance marketing programs that maximize visibility, traffic, conversion, and return on investment. This role leads performance search strategy, AI-enabled discovery approaches, investment planning, forecasting, optimization, and measurement while helping shape Walgreens' approach to evolving consumer search behaviors across traditional search engines, AI assistants, and emerging discovery platforms. Reporting to the Senior Director, this role serves as a key performance marketing leader and liaison across Marketing, Digital, Loyalty, Analytics, Finance, and agency teams to drive innovation, operational excellence, and business results through performance-driven marketing investments. #LI-NL1
> Key Focus:
> Lead enterprise Paid Search (SEM) strategy, planning, and optimization efforts, ensuring alignment with business objectives, customer priorities, and full-funnel marketing goals.
> Develop and execute performance marketing strategies that drive customer acquisition, engagement, conversion, retention, and revenue growth across search and performance channels.
> Lead Walgreens' strategy for AI-driven search and discovery, including emerging capabilities such as Generative Engine Optimization (GEO), AI Search Optimization (AISO), conversational search experiences, and AI-powered customer discovery.
> Partner with agency teams to develop channel investment strategies, budget recommendations, campaign priorities, and optimization plans that maximize business performance and marketing ROI.
> Develop annual performance marketing plans, forecasts, and investment strategies aligned to enterprise business priorities and customer growth objectives.
> Establish measurement frameworks, performance scorecards, and reporting processes that provide visibility into campaign effectiveness, channel performance, and business impact.
> Partner with Marketing Science, Analytics, and agency teams to leverage attribution, Marketing Mix Modeling, incrementality testing, customer insights, and performance analytics to optimize investments and drive continuous improvement.
> Analyze campaign, channel, audience, and business performance data to identify growth opportunities, optimization actions, and future investment recommendations.
> Collaborate with Brand, Digital, Retail Media (WAG), Loyalty to ensure performance marketing strategies support integrated customer journeys and enterprise objectives.
> Evaluate emerging technologies, AI tools, automation capabilities, and performance marketing innovations to improve efficiency, effectiveness, personalization, and marketing outcomes.
> Identify and advance new opportunities within search, retail media, commerce media, AI assistants, and performance marketing ecosystems to accelerate customer growth and competitive advantage.
> Lead performance forecasting, scenario planning, and investment optimization efforts to support evolving business priorities and maximize return on media spend.
> Establish best practices, governance frameworks, and strategic recommendations that improve enterprise performance marketing capabilities and execution.
> Monitor industry trends, platform innovations, privacy changes, consumer behavior shifts, and competitive activity to inform future performance marketing strategies and investment decisions.
> Serve as the enterprise subject matter expert for Paid Search, search marketing, AI-enabled discovery, and performance marketing best practices.
> Build strong partnerships across internal stakeholders, technology providers, agencies, and platform partners to ensure strategic alignment, executional excellence, and achievement of business objectives.
> Job Responsibilities:Partners with the Marketing Director in determining and implementing the strategy across the organization.
> Partners with the management team to identify, develop, and implement appropriate approaches, processes, and tools that elevate the marketing group.
> Identifies, evaluates and recommends marketing opportunities consistent with business objectives; provides marketing support to throughout the organization. 
> Works to identify and develop marketing strategies and programs in collaboration with business team. Communicates new ideas to director.
> Delivers presentations and provides reports for the business to provide marketing information which may include marketing trends, competition, new products, and pricing.
> Works with external vendors and third parties to develop and maintain positive relationships. Builds and enhances internal and external partnerships.
> Proactively provides Marketing solutions to address key business capabilities.
> This role is based in our Deerfield, IL office and is on‑site four days a week. 
> About WalgreensFounded in 1901, Walgreens (www.walgreens.com) proudly serves nearly 9 million customers and patients each day across its approximately 8,500 stores throughout the U.S. and Puerto Rico. Walgreens has approximately 220,000 team members, including nearly 90,000 healthcare service providers, and is committed to being the first choice for pharmacy, retail and health services, building trusted relationships that create healthier futures for customers, patients, team members and communities.
> Basic Qualifications
> Bachelor’s degree and at least 4 years of marketing or advertising experience; OR, a High School/GED and at least 7 years of marketing or advertising experience.
> Experience using tools, techniques for collecting, collating and analyzing information about existing or potential markets and market needs.
> At least 2 years of experience of cross functional team leadership
> Experience with project management (for example: planning, organizing, and managing resources to bring about the successful completion of specific project goals and objectives).
> Experience with Marketing Strategy development.
> Experience with MS Office Suite.
> At least 2 years of experience contributing to financial decisions in the workplace.
> At least 2 years of direct leadership, indirect leadership and/or cross-functional team leadership.
> Willing to travel up to 15% of the time for business purposes (within state and out of state).
> Preferred Qualifications
> Deep expertise in Search Engine Marketing (SEM), Paid Search strategy, keyword management, audience targeting, bidding strategies, campaign optimization, and performance measurement.
> Experience leading enterprise-scale performance marketing programs and managing significant media investments.
> Strong knowledge of AI-powered search ecosystems, Generative AI applications, emerging search technologies, and evolving consumer discovery behaviors.
> Experience developing strategies for AI-driven discovery, conversational search, and next-generation performance marketing capabilities.
> Advanced analytical skills with experience in attribution, incrementality testing, Marketing Mix Modeling, forecasting, and performance reporting.
> Experience working closely with agency partners and cross-functional business teams in a large, complex organization.
> Strong communication, influence, and stakeholder management skills with the ability to translate data and insights into actionable business recommendations.
> Demonstrated ability to balance strategic thinking with operational execution and performance accountability.
> We will consider employment of qualified applicants with arrest and conviction records.
> The Salary below is being provided to promote pay transparency and equal employment opportunities at Walgreens. The actual hourly salary within this range that you will be offered will depend on a variety of factors including geography, skills and abilities, education, experience and other relevant factors. This role will remain open until filled. To review benefits, please click here jobs.walgreens.com/benefits. If you are applying on a job board or unable to click on the link, please copy and paste this URL into your browser jobs.walgreens.com/benefits.
> Salary Range: $125000 - $218,750.00 / Salaried

## Verbatim — posting #21, Choice Hotels, "Senior Manager, Social Media Strategy & Marketing"

- Employer URL: https://choicehotels.wd5.myworkdayjobs.com/External/job/North-Bethesda-MD---Corporate-Headquarters/Senior-Manager--Social-Media-Strategy---Marketing_R22288
- Indeed card: jobkey 99f0775fe45fa801, "22 days ago" as of 2026-09-23, "$123,663 - $145,486 a year"
- Workday jobPostingInfo: `postedOn: "Posted 23 Days Ago"`, `startDate: "2026-08-31"`, `jobReqId: "R22288"`, location "North Bethesda MD - Corporate Headquarters", timeType "Full time"
- Phrase check (body, case-sensitive substring counts): "Generative Engine Optimization" 1; "GEO" 2; "AEO" 1; "LLM visibility" 1
- Employer size text in body: "one of the largest lodging franchisors in the world. With 7,500 hotels in 45+ countries and territories"; headcount not stated
- Company snapshot box: none (Workday)

> Job Summary
> Choice Hotels International is seeking a Senior Manager, Social Media Strategy & Marketing to lead enterprise social strategy across platforms, creators, and content ecosystems. This role will help define how social media, influencer marketing, and organic content work together to tell meaningful stories about our brand(s) that drive relevance, engagement, and business impact. This person will guide the evolution of social media from a channel execution function into a fully integrated content and demand driver, ensuring alignment across brand, media, search, and emerging ecosystems. The Senior Manager will establish the strategic foundation for how social content contributes to both including integration with SEO and generative AI-driven search environments. This role partners closely with internal stakeholders, external agencies, and cross-functional teams to strengthen key messages, RTB’s, and positioning for the brand(s), evaluating creators and content capabilities to drive that forward. They need to have knowledge and awareness of cultural trends and determining ways to amplify them through authentic brand-led storytelling and drive innovation across platforms.
> Note: This role is 4 days onsite in North Bethesda, MD and is not eligible for visa sponsorship now or in the future. 
> Responsibilities
> Enterprise Social Strategy Leadership
> Develop the enterprise social media strategy, defining the role of each platform and how organic, creator, and paid social efforts work together
> Translate business and marketing goals into integrated social and content strategies that drive measurable impact
> Establish enterprise frameworks for messaging and success measurement
> Assist in the development of long-term social strategy roadmaps, platform POVs, and capability evolution
> Translate paid social objectives, audience strategies, and performance insights into social and creator content approaches, ensuring alignment between media investment and content development
> Have a steadfast commitment to the KPI’s to grow engagement, build brands and drive demand.
> Creator & Influencer Strategy
> Lead enterprise creator and influencer strategy, including use cases, content frameworks, and governance models
> Oversee creator sourcing, briefing, and content direction in partnership with agencies and internal stakeholders
> Serve as a strategic advisor to brand, loyalty, and segment teams on how to leverage creator marketing
> Evaluate and guide onboarding of influencer and creator platforms, vendors, and partnerships
> Organic Content Strategy & Social Leadership
> Set the strategic direction for organic social content across enterprise and brand channels
> Define content testing and optimization frameworks to improve engagement and performance
> Ensure integration between organic content, paid amplification, and broader campaign execution
> Work cross-functionally with Brand, PR, and Loyalty teams to elevate social as a strategic marketing channel
> Social Content Discoverability & GEO/AEO
> Partner with SEO and content strategy teams to ensure social and creator content supports discoverability across search, generative AI, and emerging ecosystems
> Collaborate with the Paid Media team on their social content within GEO (Generative Engine Optimization) strategies.
> Work with the email marketing team to ensure a cohesive messaging and strategic lifecycle engagement between social media, email, and beyond
> Establish best practices for structuring, tagging, and distributing content to improve indexing and visibility
> Determine signals that improve content performance beyond engagement with Analytics and SEO teams
> Partner on enterprise initiatives such as LLM visibility and content discoverability
> Cross-Functional Leadership & Enterprise Impact
> Own social media plans with Paid Media, SEO, Analytics, PR, to ensure integrated strategy and execution
> Serve as a subject matter expert, providing POVs and recommendations on social and creator strategy
> Assist in driving relationships with key social platform partners (e.g., Meta, TikTok, Snap, Reddit, Pinterest), including joint business planning (JBPs), identifying strategic opportunities, and ensuring platform partnerships inform both content and media strategy
> Align social strategy with broader marketing priorities and business objectives
> Drive visibility and understanding of social strategy across stakeholders
> Agency & Partner Leadership
> Act as the lead for social and creator agency partners, setting expectations and performance standards
> Ensure agency partners operate as extensions of the internal team
> Manage external partnerships across influencer platforms and content vendors
> Innovation & Capability Evolution
> Stay ahead of platform capabilities, cultural trends, and technology shifts and translate them into actionable strategies
> Lead test-and-learn initiatives across social platforms, creator models, and content formats
> Identify opportunities to scale new capabilities that enhance engagement and discoverability
> Team Leadership & Development
> Build and lead a high-performing social strategy team
> Coach and develop team members to drive increased autonomy and enterprise thinking
> Foster a culture of innovation, curiosity, and continuous learning
> Qualifications
> Employment Experience
> 7-10 years of experience in social media, digital marketing, content strategy, or related fields
> 3+ years of management experience with direct reports and cross-functional initiatives
> Technical & Functional Expertise
> Deep expertise across social platforms (Meta, TikTok, Pinterest, Reddit, Snap, YouTube, etc.) and awareness of emerging platforms and social media trends
> Strong understanding of creator and influencer marketing models
> Experience integrating social strategy with paid and organic social media, brand marketing, and SEO
> Familiarity with content discoverability and AI-driven content ecosystems preferred
> Understanding of performance metrics and testing frameworks
> Leadership & Business Competencies
> Proven ability to lead cross-functional initiatives with enterprise impact
> Strong strategic thinking and problem-solving skills
> Strong communication and stakeholder management skills
> Strong collaboration, ability to influence
> Education
> Bachelor’s degree required; advanced degree preferred
> Salary Range
> The salary range for this position is $123,663.00 - 145,486.00. In addition to the annual salary, this role is eligible for an annual bonus based on the terms of Choice's Management Incentive Plan (MIP).
> Choice prioritizes our associate wellbeing by offering a comprehensive benefits program that is both competitive and flexible to help you achieve your wellbeing goals - here are just a few:
> Competitive compensation and benefits, including medical, dental, and vision coverage
> Leave and paid time-off for holidays, vacation, personal, family, volunteer, sick, jury duty, bereavement, military, and religious observance
> Financial benefits for retirement and health savings
> Employee recognition programs
> Discounts at Choice hotels worldwide
> About Choice
> Choice Hotels International, Inc. (NYSE: CHH), is one of the largest lodging franchisors in the world. With 7,500 hotels in 45+ countries and territories, we offer a range of high-quality lodging options in the upper upscale, upper midscale, midscale, extended stay, and economy segments. We’re the hotel company for those who choose to bet on themselves — the striver, the dreamer, the entrepreneur — because that’s who we are, too.
> At Choice, we are united by the simple belief that tomorrow will be even better than today — for associates, our company, and our franchisees. At our worldwide corporate headquarters in North Bethesda, Maryland, at our technology center in Scottsdale, Arizona, and through our associates around the globe, every voice is heard and every idea is listened to, no matter what area of the company they come from. We are united in supporting the entrepreneurial dreams of our thousands of franchise owners, which propels us forward — giving our work at Choice a purpose larger than our business.
> Our corporate office locations:
> North Bethesda, MD — Located at Pike & Rose, our worldwide headquarters is less than 15 miles from Washington, D.C., one block away from the North Bethesda Metro station, with easy access to I-495, complimentary parking, electronic charging stations, restaurants and retail.
> Scottsdale, AZ — Located at the northwest corner of Loop 101, the Scottsdale office is home to our technology, eCommerce and customer service organizations, with easy access to complimentary parking, electronic charging stations, restaurants and retail.
> Minneapolis, MN — Select roles are based in our Minneapolis office on Highway 394, near the intersection with Highway 100, only five minutes from downtown.
> Field/Remote — Select roles designated as field/remote will require associates to work from a home office, connecting virtually with Choice team members and leadership on Zoom, with possible required travel depending on the role.  
> Choice’s Cultural Values
> Welcome and Respect Everyone | Be Bold | Be Quick | Listen | Be Curious | Show Integrity
> Choice’s Leadership Principles
> Act with Intention | Lead with Authenticity | Grow & Deliver

## Verbatim — posting #4, A Place for Mom, "Staff Product Manager, Acquisition & Growth"

- Employer URL: https://jobs.ashbyhq.com/a-place-for-mom/f189f549-6f97-4a38-b36c-a6c106a5fa00 (body from https://api.ashbyhq.com/posting-api/job-board/a-place-for-mom, field `descriptionPlain`)
- Indeed card: jobkey cb91e530733844e4, "30+ days ago" as of 2026-09-23, "$165,000 - $195,000 a year"
- Ashby fields: `publishedAt: "2026-09-01T22:32:15.238+00:00"`, `location: "Austin, TX"`, `isRemote: true`, `employmentType: "FullTime"`, `department: "Product"`, `compensation: null`
- Phrase check (body, case-sensitive substring counts): "generative engine optimization" 1; "Generative Engine Optimization" 1; "GEO" 2; "AI search" 2
- Employer size text in body: "network of 15,000+ senior living communities and home care agencies"; headcount not stated
- Company snapshot box: none (Ashby)

> ABOUT THE ROLE
>
> We are looking for a Staff Product Manager to own how families discover, trust, and choose A Place for Mom across organic search, AI-mediated discovery, and emerging surfaces, and to build the product-led growth systems that turn discovery into qualified, high-intent demand.
>
> You will design and ship the product systems that drive sustained organic acquisition in a category where trust, authority, and decision quality are everything. You will partner across Product, Engineering, Data, Marketing, and Brand, and own measurable acquisition outcomes.
>
> This is a product role with deep SEO expertise required, not an SEO role with product seasoning. If you have spent your career shipping product surfaces that move organic acquisition, with a strong SEO foundation and a working point of view on how the search landscape is evolving, this is for you.
>
>
>
>
> WHAT YOU'LL OWN
>
> Organic acquisition
>
>  - Own the product strategy and roadmap for how APFM's owned properties perform across the traditional, AI-mediated, voice, and agentic search landscape
>
>  - Translate SEO signals, algorithm shifts, and discovery changes into product decisions and roadmap prioritization; partner with specialist practitioners who own day-to-day execution
>
> AI / Generative Engine Optimization (GEO) and emerging distribution
>
>  - Define and evolve how A Place for Mom shows up across the full AI-mediated discovery landscape, including AI search citations, conversational query coverage, structured data for AI grounding, MCP integrations, voice interfaces, and agentic endpoints
>
>  - Monitor and interpret shifts in AI platform behavior, search landscape changes, and evolving distribution surfaces, and translate them into internal product guidance, guardrails, and prioritization
>
>  - Evolve existing AI discovery measurement framework and tooling as the ecosystem develops and new channels come online that require new measurement approaches
>
> Product-led growth
>
>  - Build acquisition loops into the product surface: Sharing, comparison tools, decision aids, community-driven content surfaces
>
>  - Partner with Product peers to embed PLG mechanics in core flows that compound organic acquisition without paid spend
>
> Measurement and opportunity sizing
>
>  - Define metrics, baselines, and targets for organic and AI discovery; size opportunities, set hypotheses, and lead learning agendas
>
>  - Translate ambiguous, evolving discovery signals into actionable product bets and clear investment recommendations
>
> Trust and authority (YMYL)
>
>  - Senior care is a Your Money Your Life category; embed authority, expertise, and trust signals into product surfaces and content systems
>
>  - Ensure the signals AI systems use to evaluate credibility, including review integrity, content quality, and decision support depth, are reflected accurately in what we build
>
>  - Develop and maintain a point of view on AI disintermediation risk and ensure the product roadmap accounts for it
>
>
>
>
> WHAT SUCCESS LOOKS LIKE IN 12 MONTHS
>
>  - APFM's leadership position in AI search citation share is maintained and extended into new surfaces and query types as the landscape evolves
>
>  - Organic acquisition growth in high-intent segments is accelerating, with a clear product roadmap driving continued improvement
>
>  - At least one new distribution surface, such as an MCP integration, voice endpoint, or agentic integration, is live and attributable
>
>  - The AI discovery measurement framework has evolved to account for new channels and surfaces that didn't have measurement approaches when you arrived
>
>  - Trust and authority signals are meaningfully strengthened in the product surface, with a clear and defensible point of view on how APFM wins in an AI-mediated world
>
>  - At least one product-led growth loop is live inside a core flow and compounding organic acquisition without paid spend
>
>
>
>
> WHAT YOU BRING
>
>  - 7–10+ years of experience in SEO, organic growth, product strategy, or related roles
>
>  - Demonstrated depth in SEO fundamentals and a track record of shipping product surfaces that moved organic acquisition outcomes, not just advising on them
>
>  - A working point of view on how the search landscape is evolving: how AI-mediated discovery works, how to instrument and influence it, and where it's heading
>
>  - Comfort with ambiguous, evolving data sets and the ability to build measurement approaches where none exist yet
>
>  - Strong opinions on trust-sensitive, YMYL content and product systems
>
>  - Proven ability to write clear requirements, run experiments, partner closely with engineering, and own delivery end-to-end
>
>  - Experience facilitating alignment across senior stakeholders in ambiguous, cross-domain problem spaces
>
>  - Experience managing or mentoring other practitioners; a track record of elevating the product intuition and execution quality of the team around you
>
>  - Bonus: marketplace or aggregator experience, regulated or health-adjacent domains, prior GEO work, MCP or agentic distribution experience
>
>
>
>
> WHY YOU'LL LOVE IT HERE
>
>  - Mission-driven work that helps families make meaningful, high-stakes decisions
>
>  - The opportunity to shape organic and AI discovery strategy at a pivotal moment in the search-to-AI transition
>
>  - A role that combines deep SEO expertise, AI discovery strategy, and product-led growth — three skill sets that rarely sit in one seat
>
>  - High-leverage influence across multiple products and cross-functional partners
>
>  - The chance to define how SEO, generative engine optimization, and product-led growth evolve together
>
>
>
>
> COMPENSATION
>
>  - Base Salary: $165,000 – $195,000 
>
>  - Bonus: 10% Corporate Bonus
>
>  - Benefits:
>
>    - 401(k) plus match
>
>    - Dental insurance
>
>    - Health insurance
>
>    - Vision Insurance
>
>    - Paid Time Off
>
> #LI-LP1
>
> About A Place for Mom
>
> A Place for Mom is the leading platform guiding families through every stage of the aging journey. Together, we simplify the senior care search with free, personalized support — connecting caregivers and their loved ones to vetted providers from our network of 15,000+ senior living communities and home care agencies.
>
> Since 2000, our teams have helped millions of families find care that fits their needs. Behind every referral and resource is a shared goal: to help families focus on what matters most — their love for each other.
>
> We’re proud to be a mission-driven company where every role contributes to improving lives. Caring isn’t just a core value — it’s who we are. Whether you’re supporting families directly or driving innovation behind the scenes, your work at A Place for Mom makes a real difference.
>
> Our employees live the company values every day:
>
>  - Mission Over Me: We find purpose in helping caregivers and their senior loved ones while approaching our work with empathy.
>
>  - Do Hard Things: We are energized by solving challenging problems and see it as an opportunity to grow.
>
>  - Drive Outcomes as a Team: We each own the outcome but can only achieve it as a team.
>
>  - Win The Right Way: We see organizational integrity as the foundation for how we operate.
>
>  - Embrace Change: We innovate and constantly evolve.
>
> Additional Information:
>
> A Place for Mom has recently become aware of the fraudulent use of our name on job postings and via recruiting emails that are illegitimate and not in any way associated with us. APFM will never ask you to provide sensitive personal information as part of the recruiting process, such as your social security number; send you any unsolicited job offers or employment contracts; require any fees, payments, or access to financial accounts; and/or extend an offer without conducting an interview.
>
> If you suspect you are being scammed or have been scammed online, you may report the crime to the Federal Bureau of Investigation and obtain more information regarding online scams at the Federal Trade Commission.
>
> All your information will be kept confidential according to EEO guidelines.
>
> A Place for Mom uses E-Verify to confirm the employment eligibility of all newly hired employees. To learn more about E-Verify, including your rights and responsibilities, please visit www.dhs.gov/E-Verify http://www.dhs.gov/E-Verify.

## Verbatim — posting #6, MAHEC, "Director, Marketing and Brand Strategy"

- Employer URL: https://mahec.wd5.myworkdayjobs.com/MAHEC/job/Administration-Vanderbilt-Park/Director--Marketing-and-Brand-Strategy_R3586
- Indeed card: jobkey 646cc0c2c90d08cd, "6 days ago" as of 2026-09-23, location shown as "Vanderbilt, MI", no salary
- Workday jobPostingInfo: `postedOn: "Posted 7 Days Ago"`, `startDate: "2026-09-16"`, `jobReqId: "R3586"`, location "Administration Vanderbilt Park", timeType "Full time". [note: the body places MAHEC Talent Management at "121 Hendersonville Road, Asheville, NC 28803"; the Indeed card's "Vanderbilt, MI" is Indeed's rendering of "Vanderbilt Park"]
- Phrase check (body, case-sensitive substring counts): "generative engine optimization" 1; "GEO" 1
- Employer size text in body: none; "one of Western North Carolina's leading healthcare and educational organizations"
- Salary in body: none
- Company snapshot box: none (Workday)

> Join MAHEC as Director of Marketing & Brand Strategy and help shape the voice and future of one of Western North Carolina’s leading healthcare and educational organizations. This leadership role offers the opportunity to drive innovative marketing, branding, digital engagement, and communication strategies that elevate MAHEC’s impact across patient care, medical education, workforce development, and community health. We are seeking a visionary, collaborative leader who can inspire teams, tell compelling stories, strengthen our brand, and connect our mission with the communities we serve.
> JOB SUMMARY
> Primary responsibility is to provide strategic leadership, direction, and oversight for MAHEC's marketing, branding, digital engagement, and creative services functions. Responsible for developing and executing comprehensive marketing initiatives that strengthen brand awareness, enhance organizational reputation, increase engagement with patients, learners, faculty, employees, donors, community partners, and stakeholders, and support achievement of MAHEC's strategic priorities. Leads the development and implementation of integrated marketing and communication strategies supporting MAHEC's clinical services, educational programs, graduate medical education initiatives, workforce development activities, philanthropic efforts, and community outreach programs. Oversees brand stewardship, website development and governance, digital communications, creative design and production services, media relations, and marketing analytics to ensure a consistent, mission-driven organizational presence across all channels. 
> SPECIFIC RESPONSIBILITIES
> Develops and implements a comprehensive organizational marketing and communications strategy aligned with MAHEC's mission, vision, values, and strategic plan.
> Leads enterprise brand management activities, including brand positioning, messaging, visual identity standards, and reputation management.
> Provides strategic consultation to organizational leaders regarding marketing opportunities, communication planning, stakeholder engagement, and promotional initiatives.
> Oversees website strategy, design, content governance, accessibility compliance, user experience, search engine optimization (SEO), generative engine optimization (GEO), analytics, and ongoing digital platform enhancements.
> Directs the development and execution of integrated marketing and advertising campaigns utilizing digital, print, social media, email, video, and emerging communication channels.
> Establishes and maintains organizational graphic design standards and ensures brand consistency across all departments, programs, and service lines.
> Oversees development and production of marketing materials supporting patient care services, residency programs, continuing education activities, workforce recruitment, research initiatives, and community engagement programs.
> Coordinates market research, competitive analysis, audience segmentation, and performance measurement activities to inform strategic decision-making.
> Develops and monitors key performance indicators and dashboards to evaluate marketing effectiveness, return on investment, audience engagement, and brand awareness.
> Leads the organization's social media strategy and oversees management of all official digital channels.
> Supports physician, provider, learner, faculty, and employee recruitment marketing initiatives.
> Develops, administers, and monitors departmental budgets and marketing expenditures.
> Provides leadership, supervision, coaching, and performance management for marketing and communications personnel.
> Develops departmental goals, operational plans, policies, procedures, and performance metrics.
> Evaluates and implements technologies, software platforms, and tools supporting marketing, communications, digital engagement, and design activities.
> Participates in organizational leadership meetings and strategic planning efforts, providing expertise and recommendations regarding marketing, branding, and public relations.  
> Works collaboratively across clinical, educational, operational, and administrative departments to support organizational goals and priorities.
> Ensures compliance with applicable healthcare marketing regulations, privacy requirements, accessibility standards, asset licensing/usage, copyrights, and organizational policies.
> Maintains productive relationships with media organizations, journalists, community partners, healthcare organizations, educational institutions, and key stakeholders throughout Western North Carolina.  
> Promotes organizational visibility, recognition, thought leadership, and reputation through strategic communication initiatives and storytelling efforts.
> Supports community outreach, advocacy, special events, public programs, and stakeholder engagement activities.
> Collaborates with organizational leaders to communicate MAHEC's impact on healthcare, education, workforce development, and community health.
> Crisis Communication – Collaborates with executive leadership on communication strategy, message development, stakeholder engagement, and media response during crisis situations.
> Assists in the promotion of conferences, continuing education programs, fundraising activities, recognition events, and community initiatives.
> Maintains effective communication and working relationships with patients, learners, faculty, preceptors, residents, students, donors, community partners, volunteers, staff, and organizational leadership.
> KEY COMPETENCIES:
> Communication Skills 
> Effectively and respectably communicate with other individuals, whether it be a colleague, patient, or patient’s family member and appropriately enumerate information in a manner easily understood by all parties. We do this to foster a culture of understanding between all parties, especially in complex and difficult situations, to ultimately provide the best care possible to our patients and their families.
> Decision Making
> Ability to make the most appropriate decision in a given situation and then taking the next steps to ensure appropriate and timely completion. This requires conflict resolution skills, critical thinking skills, confidence in your ability to make the right decision in most situations. This also includes ability to prioritize your workday appropriately to ensure the most important tasks are completed on time.
> HealthCare Knowledge
> Having the drive to keep yourself abreast and up to date on the new breakthroughs in your area of expertise and communicating them to the rest of the team, as appropriate.  This also includes keeping up with your licensure and yearly training requirements within your area expertise along with MAHEC’s organizational training. Finally, the ability to apply the depth of knowledge maintained and gained through this process in real life scenarios as appropriate.
> Interpersonal Skills 
> Showing the ability to meet difficult situations with grace, professionalism, and understanding. Within your area of expertise, showing respect and showing empathy where appropriate with your colleagues, patients, and their family at all times, even when its most difficult to do so. This is done, in part, by effective listening, being your authentic self, showing responsibility and dependability, and being patient with others.
> Organizational Values
> Adherence to MAHEC’s founding principles and incorporating them every day. This includes, among others, having integrity and accountability, reverence for other cultures and equitable practices, ability to manage change, and displaying a clear understanding of organizational dynamics. Doing these things creates a culture where people want to do the best for each other and gives personal ownership towards the goal of helping people in their time of need.
> Problem Solving 
> Having an analytical mind and ability to work autonomously to solve complex problems that may arise. The wherewithal to think logically through a difficult problem and come to an appropriate resolution for a given issue. This helps to drive continuous improvement by thinking through where we can improve in a novel way. Measures success by understanding where we are currently and where we want to go and then applying those new ideas to affect positive change.
> SPECIFIED SKILLS
> COMPUTER
> Proficiency with Microsoft 365, website content management systems, digital marketing technologies, and analytics platforms required. Proficiency with graphic design tools, and social media management platforms preferred.  
> FOREIGN LANGUAGE
> Spanish speaking skills preferred.
> OTHER SKILLS:
> Demonstrated excellence in executive communication, presentation development, writing, editing, stakeholder engagement, and public-facing communications.
> Ability to establish productive relationships with high level health system leaders in academic or hospital settings.
> Strong written and verbal communication skills
> Ability to manage multiple programs and competing priorities.
> Strategic thinking and organizational development.
> Strong problem-solving and conflict resolution skills.
> SUPERVISORY RESPONSIBILITIES: 
> Leads a team of marketing, communications, digital, and creative professionals responsible for delivering the programs, services, and initiatives described within this role. Provides strategic direction, prioritization, coaching, and resource management to ensure alignment with organizational objectives and service excellence.
> EDUCATION AND EXPERIENCE
> MINIMUM QUALIFICATIONS:
> Bachelor's degree in Marketing, Communications, Public Relations, Journalism, Business Administration, Healthcare Administration, or a related field required.
> Minimum seven years of progressively responsible marketing, communications, public relations, or brand management experience required.
> Minimum three years of leadership or supervisory experience required.
> Experience in healthcare, academic medicine, higher education, nonprofit organizations, Federally Qualified Health Centers, or health systems preferred.
> Demonstrated experience leading brand strategy, website development, digital marketing initiatives, and integrated communication campaigns required.
> PREFERRED QUALIFICATIONS:
> Master's degree in Marketing, Communications, Business Administration, Public Health, Healthcare Administration, or a related discipline preferred.  
> REQUIRED LICENSES:
> Valid North Carolina Driver’s License
> SCHEDULE:
> Regular attendance on-site is an essential function of this position. Typical business hours are Monday – Friday, 8:00 am to 5:00 pm (or flexed to best meet the needs of the clients and/or the Division); 40 hours per workweek; weekend, holiday, or evening coverage is occasionally required. Work hours will need to be flexible in order to respond to special work assignments, or evening activities, as requested by the team leader.
> At MAHEC, we strive to equip all team members with Total Rewards (pay + benefits) to honor their service, support their health, manage their financial security, build their career, and thrive.
> MAHEC is a qualifying employer for the Public Service Loan Forgiveness (PSLF) Program. Employees who meet federal requirements may be eligible to have remaining student loan balances forgiven after 10 years of qualifying payments while working full-time at MAHEC.
> If you are interested in this role, and you have related experience and qualifications, we encourage you to apply or reach out to AskTalent@mahec.net for support in your job search process. You could be the talent we are seeking for this or other opportunities
> All MAHEC employees and learners will be required to receive the Flu vaccine or have an approved exemption.
> MAHEC does not provide employment-based US visa sponsorship, now or in the future. All new employees must provide valid, original I-9 documents on their first day of work.
> MAHEC Talent Management is located at 121 Hendersonville Road, Asheville, NC 28803. Equal Opportunity Employer.

## Verbatim — posting #20, The Cigna Group, "Lead Analyst, Technical Search (SEO/AEO/GEO)"

- Employer URL: https://cigna.wd5.myworkdayjobs.com/cignacareers/job/New-York-NY/Lead-Analyst--Technical-Search--SEO-AEO-GEO-_26011217-1
- Indeed card: jobkey a10a0df403da77dd, "8 days ago" as of 2026-09-23, "$79,100 - $131,800 a year", Bloomfield, CT
- Workday jobPostingInfo: `postedOn: "Posted 9 Days Ago"`, `startDate: "2026-09-14"`, `jobReqId: "26011217"`, location "New York, NY", additionalLocations "DC, Washington, 701 Pennsylvania Ave, NW"; "CT, Bloomfield, 900 Cottage Grove Rd Wilde Bldg"; "NJ, Morris Plains, 115 Tabor Rd"; "MO, St. Louis, One Express Way"; "PA, Philadelphia, 1601 Chestnut St -Two Liberty"; timeType "Full time"
- Phrase check (body, case-sensitive substring counts): "Generative Engine Optimization" 1; "GEO" 4; "answer engine" 2; "Answer Engine Optimization" 1; "AEO" 5; "AI search" 1; "Claude" 1
- Vendors named in body: "AEO tools (e.g. Profound, Scrunch, Bluefish, Evertune, etc.)"; "SEO tools (e.g. BrightEdge, SEMrush, Conductor, etc.)"; "Claude Code and/or similar AI-assisted development platforms"
- Employer size text in body: none
- Company snapshot box: none (Workday)

> Job Description
> Cigna is seeking an Enterprise Technical Search Lead/Analyst (SEO/AEO/GEO) to join the Paid Media Center of Expertise within the Marketing and Communication organization.
> This role will drive technical search optimization across Cigna's priority brands and digital properties, ensuring our websites are optimized for both traditional search engines and emerging AI-powered answer engines. As the enterprise subject matter expert for Technical SEO, Answer Engine Optimization (AEO), and Generative Engine Optimization (GEO), this role will drive AI readiness, technical governance, automation, and innovation that improve search discoverability, visibility, and website performance.
> The ideal candidate combines deep technical expertise with strong communication and collaboration skills. They can translate complex technical concepts into actionable recommendations, influence cross-functional stakeholders, and develop scalable solutions that improve search performance across a large enterprise ecosystem.
> Key Responsibilities
> Lead enterprise Technical SEO, AEO/GEO strategy across The Cigna Group's priority brands and digital properties.
> Develop and maintain the Enterprise AI Search Technical Roadmap, identifying opportunities to improve AI readiness, search visibility, machine readability, and discoverability across traditional and AI-powered search experiences.
> Establish and maintain technical search standards, governance, best practices, and implementation frameworks.
> Oversee structured data, schema markup, entity optimization, and AI readiness initiatives.
> Conduct technical audits and provide recommendations related to crawling, indexing, rendering, site architecture, internal linking, and search accessibility.
> Monitor site health and technical performance, including Core Web Vitals, crawl efficiency, indexation, and search visibility.
> Develop redirect strategies and provide technical guidance for site migrations, platform transitions, and large-scale digital initiatives.
> Leverage AI, automation, and advanced analytics to improve efficiency, reduce manual effort, and scale technical search operations.
> Evaluate emerging traditional and AI search trends, technologies, and optimization opportunities.
> Partner with business, content, analytics, product, UX, and technology teams to drive implementation of technical recommendations.
> Serve as a trusted advisor and educator, simplifying technical concepts and driving adoption of search best practices across the organization.
> Ideal candidates will offer
> Bachelor's degree or equivalent professional experience.
> 4+ years of experience in Technical SEO, with demonstrated experience leading enterprise-level technical search initiatives for large brands, complex digital ecosystems, or multi-domain web environments.
> Strong understanding of search engine crawling, rendering, indexing, ranking systems, and website architecture.
> Deep knowledge of HTML, CSS, JavaScript, structured data, schema markup, and JSON-LD.
> Experience conducting technical SEO audits and driving implementation of technical recommendations.
> Experience leveraging AI tools, automation, and analytics to improve search effectiveness and scalability.
> Strong analytical, problem-solving, project management, and stakeholder management skills.
> Excellent communication skills with the ability to explain technical concepts to non-technical audiences.
> Self-starter with the ability to manage competing priorities and drive initiatives forward.
> Experience managing enterprise-level technical search optimization initiatives across multiple brands or business units.
> Experience optimizing websites for AI-powered search experiences, answer engines, and large language models.
> Experience with log file analysis and advanced technical diagnostics.
> Experience building automated workflows, scripts, agents, or reporting solutions using AI-assisted development tools.
> Experience working within healthcare, highly-regulated industries, or other large enterprise environments.
> Technical Expertise
> Experience in utilizing the following tools and platforms:
> Search, AEO & GEO Platforms
> SEO tools (e.g. BrightEdge, SEMrush, Conductor, etc.)
> AEO tools (e.g. Profound, Scrunch, Bluefish, Evertune, etc.)
> Analytics platforms (e.g. Google Search Console and Google Analytics, Adobe Analytics)
> Enterprise website crawlers (e.g. Screaming Frog, Botify, etc.)
> Data, Automation & AI
> SQL and Python
> APIs and automation frameworks
> Claude Code and/or similar AI-assisted development platforms
> Content Management Systems
> Adobe Experience Manager (AEM)
> Drupal
> TeamSite
> If you will be working at home occasionally or permanently, the internet connection must be obtained through a cable broadband or fiber optic internet service provider with speeds of at least 10Mbps download/5Mbps upload.
> For this position, we anticipate offering an annual salary of 79,100 - 131,800 USD / yearly, depending on relevant factors, including experience and geographic location.
> This role is also anticipated to be eligible to participate in an annual bonus plan.
> At The Cigna Group, you’ll enjoy a comprehensive range of benefits, with a focus on supporting your whole health. Starting on day one of your employment, you’ll be offered several health-related benefits including medical, vision, dental, and well-being and behavioral health programs. We also offer 401(k), company paid life insurance, tuition reimbursement, a minimum of 18 days of paid time off per year, paid holidays, and leaves of absence. For more details on our employee benefits programs, click here. 
> About The Cigna Group 
> Doing something meaningful starts with a simple decision, a commitment to changing lives. At The Cigna Group, we’re dedicated to improving the health and vitality of those we serve. Through our divisions Cigna Healthcare and Evernorth Health Services, we are committed to enhancing the lives of our clients, customers and patients. Join us in driving growth and improving lives.
> Qualified applicants will be considered without regard to race, color, age, disability, sex, childbirth (including pregnancy) or related medical conditions including but not limited to lactation, sexual orientation, gender identity or expression, veteran or military status, religion, national origin, ancestry, marital or familial status, genetic information, status with regard to public assistance, citizenship status or any other characteristic protected by applicable equal employment opportunity laws.
> If you need a reasonable accommodation to complete the online application process, please email seeyourself@thecignagroup.com for assistance.  Please note that this email inbox is dedicated to accommodation requests only and cannot provide application updates or accept resumes.
> The Cigna Group has a tobacco-free policy and reserves the right not to hire tobacco/nicotine users in states where that is legally permissible. Candidates in such states who use tobacco/nicotine will not be considered for employment unless they enter a qualifying smoking cessation program prior to the start of their employment. These states include: Alabama, Alaska, Arizona, Arkansas, Delaware, Florida, Georgia, Hawaii, Idaho, Iowa, Kansas, Maryland, Massachusetts, Michigan, Nebraska, Ohio, Pennsylvania, Texas, Utah, Vermont, and Washington State.
> Qualified applicants with criminal histories will be considered for employment in a manner consistent with all federal, state and local ordinances.

## Verbatim — posting #2, AT&T, "Lead, Digital Customer Growth"

- Employer URL: https://www.att.jobs/job/bothell/lead-digital-customer-growth/117/99991073888 (same requisition also listed at /job/atlanta/…/99991073808, /job/dallas/…/99991073760, /job/el-segundo/…/99991073920)
- Indeed card: jobkey 35e3ce3d36d3f491, "22 days ago" as of 2026-09-23, "$128,400 - $215,800 a year", Bothell, WA; matched on both the GEO and AEO queries
- Employer page JSON-LD: `"datePosted": "2026-9-17"`, `"identifier": "R-120739-2"`
- Phrase check (body, case-sensitive substring counts): "Generative Engine Optimization" 1; "GEO" 3; "answer engine" 1; "Answer Engine Optimization" 1; "AEO" 3; "AI assistants" 1
- Employer size text in body: none
- Company snapshot box: none on the employer page

[note: equal-opportunity boilerplate after the salary block removed]

> Lead, Digital Customer Growth
>  Bothell, Washington
>  Apply now
>  Save role
>  This position requires office presence of a minimum of 5 days per week and is only located in the location(s) posted. No relocation is offered.
> As an SEO & AEO/GEO Manager supporting AT&T Business, you will help shape how prospective business customers discover, understand, and engage with AT&T across traditional search engines and emerging AI-driven discovery experiences.
> You will own and advance SEO strategies across key areas of the AT&T Business digital ecosystem, using search data, technical analysis, competitive intelligence, and customer behavior to identify opportunities for growth. This role requires someone who can move comfortably between strategy and execution. A great candidate will feel at home developing recommendations, digging into data, diagnosing technical issues, building business cases, and collaborating with partners to bring improvements to market.
> You will work within a cross-functional environment and serve as a trusted search expert for marketing, product, technology, content, analytics, and leadership teams.
> Key Responsibilities
> Develop and execute SEO (and emerging AI) strategies designed to increase qualified organic visibility, traffic, engagement, and business outcomes across AT&T Business digital properties.
> Own SEO & AEO/GEO performance for assigned products, customer journeys, content areas, or business priorities.
> Conduct keyword, topic, audience, competitive, and search landscape research to identify new growth opportunities.
> Translate search demand and customer behavior into actionable recommendations for content, product, UX, and digital experiences.
> Perform technical SEO analysis across areas such as crawling, indexing, rendering, site architecture, internal linking, structured data, canonicalization, redirects, XML sitemaps, page performance, and JavaScript-driven experiences.
> Partner with developers, product managers, and technology teams to define requirements, troubleshoot issues, prioritize technical improvements, and validate implementations.
> Develop and optimize content strategies based on search intent, customer needs, competitive gaps, and business priorities.
> Partner with content and marketing teams to improve existing experiences and identify opportunities for new content.
> Monitor organic search performance and communicate trends, opportunities, risks, and recommended actions to stakeholders.
> Develop reporting and analysis that connect SEO performance to meaningful customer and business outcomes.
> Evaluate the impact of algorithm changes, SERP evolution, competitor activity, and changes in customer search behavior.
> Help advance AT&T's approach to emerging AI-powered search and answer experiences, including generative search, answer engines, AI assistants, and citation-based discovery.
> Identify opportunities to improve how AT&T Business information is understood, surfaced, and represented across both traditional and AI-powered search environments.
> Collaborate across marketing, analytics, product, UX, technology, development, communications, and other teams to embed search best practices into digital planning and execution.
> Manage multiple initiatives simultaneously, balancing near-term performance opportunities with longer-term strategic priorities.
> Serve as an SEO subject-matter expert and advocate for organic search throughout the organization.
> Qualifications
> Required:
> 5+ years of professional experience in SEO, organic search, digital marketing, or a closely related field.
> Strong understanding of technical SEO, on-page SEO, content optimization, keyword research, search intent, and competitive analysis.
> Experience using enterprise SEO, analytics, webmaster, or search intelligence platforms.
> Strong analytical skills with the ability to translate complex data into clear insights and recommendations.
> Demonstrated ability to diagnose SEO opportunities and develop actionable solutions.
> Experience working with cross-functional partners such as developers, product managers, content teams, UX teams, analytics teams, and marketers.
> Strong written and verbal communication skills, including the ability to explain technical or analytical concepts to non-technical audiences.
> Ability to independently manage multiple priorities and drive initiatives from analysis through implementation and measurement.
> Preferred:
> Experience supporting SEO for a large enterprise, complex website, B2B organization, telecommunications company, technology company, or similarly sophisticated digital environment.
> Experience with platforms such as Google Search Console, Bing Webmaster Tools, Adobe Analytics, Ahrefs, SEMrush, BrightEdge, Botify, Screaming Frog, or comparable tools.
> Working knowledge of HTML, CSS, JavaScript, structured data, modern web frameworks, and web development principles.
> Experience working with large-scale websites, complex information architectures, migrations, redesigns, or enterprise content management systems.
> Experience developing dashboards, measurement frameworks, forecasts, or business cases for organic search initiatives.
> Familiarity with emerging search experiences, generative AI, Answer Engine Optimization (AEO), Generative Engine Optimization (GEO), large language models, and AI-driven discovery.
> Experience using automation, data analysis, or AI tools to accelerate SEO research, analysis, or execution.
> B2B marketing or lead-generation experience.
> What Success Looks Like
> Success in this role means more than improving rankings. You will help AT&T Business build durable organic visibility by making our digital experiences easier for customers, search engines, and emerging AI platforms to discover, understand, and trust.
> You will uncover opportunities others miss, translate them into clear business priorities, build alignment across teams, and help turn those opportunities into measurable results.
> Our Lead Digital Customer Growth jobs earn between $128,400.00 - $215,800.00 USD Annual. Not to mention all the other amazing rewards that working at AT&T offers. Individual starting salary within this range may depend on geography, experience, expertise, and education/training.
> Joining our team comes with amazing perks and benefits:
> Medical/Dental/Vision coverage
> 401(k) plan
> Tuition reimbursement program
> Paid Time Off and Holidays (based on date of hire, at least 23 days of vacation each year and 9 company-designated holidays)
> Paid Parental Leave
> Paid Caregiver Leave
> Additional sick leave beyond what state and local law require may be available but is unprotected
> Adoption Reimbursement
> Disability Benefits (short term and long term)
> Life and Accidental Death Insurance
> Supplemental benefit programs: critical illness/accident hospital indemnity/group legal
> Employee Assistance Programs (EAP)
> Extensive employee wellness programs
> Employee discounts up to 50% off on eligible AT&T mobility plans and accessories, AT&T internet (and fiber where available) and AT&T phone
> Weekly Hours:
> 40
> Time Type:
> Regular
> Location:
> Atlanta, Georgia, Bothell, Washington, Dallas, Texas, El Segundo, California
> Salary Range: 
> $128,400.00 - $215,800.00

## Checked, not found — employer sites for the other priority and vertical-relevant cards

| Card | Employer | Channel checked, 2026-09-23 | Result |
|---|---|---|---|
| #16 | Ziggi's Coffee, "Senior Manager, Performance Marketing" | ziggiscoffee.com/careers/ (WordPress, AWSM job openings; wp-json `awsm_job_openings?search=performance`; site search `?s=performance+marketing`) | listing pages carry store roles only (Barista, Shift Lead, General Manager, Assistant Manager); no corporate marketing posting; body unread |
| #1, #14 | RestauNax, "AI-Native Marketing Lead" | restaunax.com (/careers 404, /jobs 404, /join-us 404; home and /about carry no careers link) | no careers page found; body unread |
| #8 | Vasion, "Head of Search & AI Visibility" | vasion.com/careers/ (Workable embed) → apply.workable.com/api/v3/accounts/vasion/jobs | total 5 open roles (Business Development Representative; Account Executive (Partner First) - APAC; Senior Growth Marketing Manager; Program Manager, PDLC; Partner Sales Manager - UK&I/Northern Europe); the card's title absent; body unread |
| #34 | GESA Credit Union, "Brand Content Strategist" | gesa.com/contents/careers/ → paycomonline.net ATS listing (HTTP 200, 197 KB) | 0 matches for "strategist" in the listing HTML; body unread |
| #3 | Intuit, "Staff AI Scientist" | jobs.intuit.com/search-jobs?k=Staff%20AI%20Scientist (HTTP 200) | results rendered by script, no job links in the HTML; body unread |
| #18 | Solventum, "Search Engine Optimization Specialist" | solventum.wd1.myworkdayjobs.com Workday CXS endpoint, tenant path guessed | HTTP 422; tenant path not confirmed; body unread |

Cards not attempted on employer sites (24): #0 body already in the superseded file; #5, #7, #9–#13, #15, #17, #19, #23–#33.

## Pull notes — mechanical only

- Indeed: 1 page requested, walled at once (Cloudflare "Additional Verification Required", Ray ID a3f87a4098e73f67, 16:21). The superseded file's last state was the same wall text on an in-page fetch. No pause-and-retry attempted.
- Employer sites: TalentBrew pages (Walgreens, AT&T) served full HTML with JSON-LD JobPosting; Workday tenants (Choice Hotels, MAHEC, Cigna) answered the CXS JSON endpoints without a session; Ashby served its public posting API. choicehotels.wd1 (guessed) returned HTTP 500 maintenance page; the careers site links wd5.
- Salary lines are as the employer states them; Indeed card salary strings are reproduced from the superseded file for side-by-side reading.
- Phrase counts are case-sensitive substring counts over the stripped body text, run by the pull script; "GEO" and "AEO" counts include occurrences inside "(GEO)" and "SEO/AEO/GEO"; "Claude" in the Cigna body is "Claude Code", a development tool, not an assistant surface.
- No data image on any page; nothing saved to `docs/raw/img/`.

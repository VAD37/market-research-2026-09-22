# Q1 Media — ChatGPT Ads Results: Real Data From Live Campaigns

```yaml
source:          Q1 Media (agency)
url_or_doc_id:   https://www.q1media.com/pages/case-studies-blogs/chatgpt-ads-part2
published:       2026-07-24
pull_date:       2026-09-23
pull_method:     fetch — python urllib (browser user-agent, no login) + trafilatura main-text extraction; not the Chrome extension
pull_purpose:    evidence about category noise
tier:            6
tier_reason:     agency blog, no n, no window, no named client; filed as evidence of category noise only
source_label:    vendor-reported
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     sales
supersedes:      none
captured:        full page
verbatim:        full
```

Pass 12, Lane B (task P12-ads). Body below is the page's own text as extracted, unedited.

## Verbatim

The information in this blog reflects what we know as of its published date: July 24, 2026. ChatGPT Ads is an actively evolving platform, and details may change. That is, in part, what makes this update worth writing. For context on where things started, read our original breakdown: ChatGPT Ads in 2026: What We Know, What's Changing, and How Brands Should Approach the Beta.
When we published our first blog on ChatGPT Ads, we made a promise: come back with real data once we had it.
We’re back.
Q1Media has been running live campaigns across multiple accounts, investing our own media dollars alongside client budgets, and documenting what the platform actually does, not what the hype says it does. This is not a theoretical update. These are real findings from real campaigns, aggregated across accounts in multiple verticals.
The short version: it is not as bad as the most skeptical take. It is not as good as the loudest headlines. And the brands most likely to succeed on it are probably not who you would expect.
Here is what we have learned.
A $500 cost per acquisition from ChatGPT that converts to a customer at 50% can be more valuable than a $100 CPA from a channel that converts at 5%.
When we first covered this platform, conversion tracking was essentially non-functional. That has changed, with an important caveat.
Conversion tracking can now be set up for most accounts. However, this is not a pixel you install in five minutes through a tag manager template. It requires installing a base code and then appending a separate event parameter on top of it. If your team is not fluent in Google Tag Manager, you will have a hard time getting this set up correctly.
Since publishing the first ChatGPT Ad blog, conversion-based bidding has become available, though in a very early form. It applies only to new campaigns; existing campaigns cannot be switched over. At the campaign level, you select a single conversion action to optimize toward. Maximum cost per conversion is then set at the ad group level. You cannot optimize toward multiple conversion actions within the same campaign, and in-platform conversion tracking must be set up and firing correctly before this is usable. Given the tracking setup complexity outlined above, that prerequisite matters. If your pixel is not implemented cleanly, conversion bidding will not work as intended.
The Q1Media recommendation remains the same as it was in the first blog: use GA4 and UTM tags on every ad. This is not a workaround. It is the right approach regardless of what the in-platform tracking does or does not show, because it connects ChatGPT performance to your full marketing picture rather than leaving it in a silo.
One additional note for teams running GA4: OpenAI has added AI traffic dimensions to the platform. If you are running paid ads alongside organic ChatGPT traffic, you need to set up UTM-based filters to separate the two. Without those filters, your AI traffic data will be blended, and your reporting will be unreliable.
Getting an account approved is not the same as getting your ads approved. This is one of the most common misunderstandings we encounter.
An account can be approved to exist on the platform while specific ad creative or categories are rejected. The same logic applies at the vertical level. OpenAI has been clear that certain categories, financial services being the most frequently cited example, are not permitted. However, we have seen cases where brands in those categories have been approved at the account level but had their ads blocked when they attempted to run.
There also appears to be some flexibility at the margins for large, established brands. OpenAI's own documentation uses language like "some brands" may qualify despite being in a restricted category, suggesting exceptions exist, most likely for brands with significant spend potential. We would not build a strategy around that ambiguity.
The practical guidance here is straightforward. If a brand is in a clearly excluded category, do not waste time pursuing it. If they are adjacent to one, meaning in a wellness space rather than healthcare, or in financial education rather than lending, it may be worth applying and seeing what happens. But go in with realistic expectations and a clear understanding that ad-level approvals are a separate hurdle from account-level approvals.
Here is what we have seen aggregated across active accounts.
Click-through rates range from approximately 0.5% to 2.5%, depending heavily on campaign intent. A highly specific campaign for a product like an earwax removal solution, targeting conversations explicitly about that issue, will outperform a broader brand awareness campaign in a general category. That range is actually reasonable for the format.
Cost per click is coming in around $5 on average, though this varies significantly by vertical. Competitive categories, including anything targeting marketers or agencies, are running considerably higher because multiple advertisers are competing for the same conversations. More niche verticals with less competition can come in below that average. The more specific the offering, the more it will cost to reach those conversations.
Conversion rates are running at roughly 2%, which is approximately half of what we see from organic ChatGPT traffic. That gap is worth understanding rather than dismissing. Organic ChatGPT visitors have self-selected into a brand result through an AI recommendation. Paid visitors are clicking on a sponsored placement. The intent level is different, which is reflected in the conversion rate.
The cost-efficiency question is the right one to ask. Yes, this platform is more expensive than most. But the audience is further into a research or consideration process than a typical display impression. Brands that know their back-end numbers, specifically what a lead or customer is worth and what conversion rates look like downstream, are in a much better position to evaluate whether a higher CPA from ChatGPT is actually good business. A $500 cost per acquisition from ChatGPT that converts to a customer at 50% can be more valuable than a $100 CPA from a channel that converts at 5%.
One finding that surprised us: the standard logic of CPC for bottom-of-funnel and CPM for top-of-funnel does not apply here. We have seen accounts where a CPM approach delivers lower effective CPCs than running a direct CPC buy. We test both on every account we launch, and the results vary enough across accounts that we would not make a blanket recommendation without data to back it up.
If there is one thing we want brands and agencies to take away from this update, it is this: the prompt is everything.
Until very recently, geography and the content hint prompt were your only two targeting levers. That has since changed. OpenAI has officially rolled out custom audiences, which we cover in detail in the next section. But even with that addition, the prompt remains the most consequential variable in the platform. It determines which conversations your ads appear alongside, and a poorly written prompt means your ads serve in irrelevant contexts, burn budget, and produce data that tells you nothing useful.
A few things we have learned about what works and what does not:
Specificity outperforms breadth. A prompt built around a specific pain point, earwax removal, window replacement, AI certification, consistently outperforms a prompt targeting a general category like health and wellness or digital marketing. The platform rewards relevance.
Demographic language does not work the way you would expect. Many users do not share personal details with AI tools. Writing a prompt that specifies "target males aged 35 to 54" does not function the way it would in Google or Meta because that data simply is not available in most conversations. Focus on the nature of the query rather than the person asking it.
Define who you are not targeting as clearly as who you are. Being explicit about exclusions in the prompt helps tighten where ads serve.
High-intent query language outperforms informational language. Prompts built around the kinds of queries people ask when they are close to a decision, reviews, comparisons, near me, best options, which is better, consistently deliver stronger results than prompts focused on broad awareness topics.
Long versus short prompts both work, but for different reasons. We are actively testing this and will have more to say in a future update. For now, the recommendation is to test both rather than assume one is superior.
We have built proprietary tools that analyze a brand's URL, industry, and audience to generate and test prompt variations at scale. This capability, building the right prompt and iterating on it systematically, is one of the areas where working with a partner adds the most value on a platform that otherwise looks deceptively simple.
Very recently, OpenAI officially announced custom audiences for ChatGPT Ads. It is a meaningful development and worth understanding clearly, including where it falls short. While the feature expands advertisers' targeting options for the first time, its current requirements make it most practical for enterprise brands with large first-party datasets.
What it is: custom audiences allow advertisers to upload customer or prospect lists using email addresses or phone numbers. Unlike Meta or Google, there is currently no pixel-based audience creation or website retargeting. Everything begins with a CRM list.
What you can do with it:
At the campaign level, you can include an audience to limit delivery to people on your list, or exclude an audience to prevent your ads from reaching them. Common use cases include targeting a qualified prospect list, suppressing existing customers from seeing an acquisition campaign, or excluding recent purchasers from a promotion they have already converted on.
At the ad group level, you can set a bid multiplier for users who match a custom audience. For example, if you are running a broad campaign but are willing to pay more to reach people who are past customers or high-value prospects, you can define a multiplier of up to 10x for that audience. In practice, we would generally recommend giving those audiences their own dedicated ad group rather than using bid multipliers, as it gives you cleaner control over spend and makes reporting more straightforward.
One important note: your content hint prompt remains active in all scenarios. Custom audiences layer on top of the prompt targeting rather than replacing it.
The limitations you need to know:
The minimum matched audience size to use a custom audience is approximately 25,000 users. OpenAI recommends audiences of at least 100,000 for best results. These are significant thresholds. Most small and mid-size brands will not have email or phone lists large enough to qualify without some work.
Match rates are not yet published by OpenAI. Given that both email and phone number are required to create a ChatGPT account, we expect match rates to be reasonably high, potentially in the range of 80% or better, but OpenAI has not confirmed what advertisers should expect.
The practical reality is that this feature, in its current form, skews toward larger advertisers with substantial first-party data. A brand with 30,000 customers in its CRM might be able to put together a qualifying list. A brand with 8,000 might not. Audience files cannot be edited after upload, so if you need to update a list, you create a new audience and archive the old one.
These requirements mean custom audiences are currently much more useful for enterprise advertisers than for small and mid-sized businesses. We expect these thresholds to evolve over time, but today they significantly limit who can take advantage of the feature.
One point that is easy to miss: your content hint prompt remains active regardless of whether you use custom audiences. Audience lists refine who can see your ads, but prompts still determine the conversations where those ads are eligible to appear. Strong prompt strategy remains the foundation of successful ChatGPT campaigns.
What this means for strategy:
Custom audiences make a few specific use cases significantly more viable. Retargeting past website visitors is still not possible since there is no pixel-based audience building, but suppressing past customers from acquisition campaigns, targeting a known prospect list, or bidding more aggressively on high-value segments are all now real options for brands with the list size to support it.
For brands that qualify, we would prioritize exclusion audiences first. Suppressing existing customers from acquisition campaigns is an immediate efficiency gain, while bid modifiers and inclusion audiences require larger datasets and more campaign planning.
Custom audiences are clearly a feature OpenAI is building out, and the current constraints suggest it is being tested at scale before broader access. We expect the minimum audience size requirements to come down over time as the feature matures. For now, it is a real and useful addition for the right advertiser.
While this is an important milestone for the platform, it does not fundamentally change our overall recommendation. Prompt quality, measurement through GA4, and understanding whether ChatGPT is the right channel for your audience remain significantly more important than audience uploads for most advertisers today.
Source: OpenAI Help Center, Custom Audiences
Based on what we have seen across accounts, here is the profile of a brand that is well positioned for ChatGPT Ads right now:
Specific pain point with a direct solution. The more clearly a brand addresses a defined problem, the better its ads perform. If someone is asking ChatGPT about a specific issue and your product directly solves it, that is a high-quality match.
Already showing up organically in ChatGPT. This is one of the strongest early signals we have seen. Brands getting organic ChatGPT traffic, meaning their products or services are being referenced in AI responses, consistently perform better in paid placements than brands with no organic presence. It mirrors what we know from Google: holding both a paid placement and an organic result reinforces credibility and increases the likelihood of conversion. If you are not doing Answer Engine Optimization (AEO) (also known as Generative Engine Optimization (GEO)), that work should come before or alongside ChatGPT Ads.
High-intent consumer queries. Products and services that people actively research before buying, education, home improvement, health products, and specialty retail, are a natural fit for the platform's audience behavior.
Sufficient budget. At an average CPC of $5, a budget of a few hundred dollars a month does not generate enough data to optimize. Brands need enough volume for the platform to learn and for the data to become meaningful. Our general guidance is that brands spending under $5,000 per month on this channel specifically are unlikely to get enough signal to justify the operational investment.
Hyper-local businesses with tight geographic requirements. Geographic exclusions are now available at the state, DMA, and zip level, which is an improvement. However, our own testing shows that zip-level targeting serves very few impressions regardless. The platform wants volume, and tight geographic constraints work against that. If a brand's entire serviceable area is a handful of zip codes, the budget will not scale effectively here. Spend it on local paid search instead.
B2B targeting. Decision-makers at companies are disproportionately on paid ChatGPT plans, which are excluded from ad targeting. OpenAI has also been clear that their near-term focus is consumer verticals. B2B is not where this platform is built to perform right now.
Very niche products without existing demand on ChatGPT. If people are not already asking ChatGPT about a product category, running ads against that category will not create demand. Before spending on paid placement, check whether organic ChatGPT traffic exists. If it does not, paid ads are unlikely to change that.
A few operational constraints that are easy to miss:
- Geographic exclusions are now available. You can exclude at the state, DMA, or zip code level, which is a meaningful improvement from inclusion-only targeting. That said, our earlier finding still holds: zip-level targeting serves very few impressions in practice, so hyper-local campaigns remain a poor fit for this platform regardless of the exclusion capability.
- There is no retargeting. You cannot reach users who have previously visited your site or interacted with your brand via pixel-based audiences. Custom audiences using email or phone lists are now available as a partial workaround for known audiences, but behavioral retargeting does not yet exist on this platform.
- Past customer suppression is now possible via custom audiences, provided your list meets the 25,000 matched user minimum. For brands that qualify, this is an immediately useful capability.
- Data is approximately 24 hours lagged. This is different from the seven-hour lag we reported in our first blog. Plan optimization schedules accordingly.
ChatGPT Ads are not a replacement for anything in your current media mix. They are an incremental channel, and the brands getting the most out of them are the ones treating them that way, with an isolated test budget, different performance standards than established channels, and a clear connection to the rest of what they are running.
The platform is imperfect. The tracking is still developing. The prompt is a learning curve. But the audience is real, the intent is there, and the early data is good enough to justify continued testing for the right brand in the right context.
Q1Media has been in this position before. We were among the first agencies in the TikTok beta. We hold a direct seat on Amazon. We were part of the Disney advertising platform beta. Getting in early on emerging platforms is how we build the knowledge that our clients benefit from later. ChatGPT Ads is the current version of that commitment.
We are not here to sell you on a platform that does not work for your brand. We are here to tell you what we actually know, backed by data, and to help you make a decision based on that rather than on the hype.
Ask yourself these questions:
- Does your brand address a specific, searchable pain point?
- Are you already generating organic traffic from ChatGPT?
- Do you have a monthly budget that allows for meaningful volume?
- Are your target customers likely to be on the Free or Go plan?
- Is your offering consumer-facing rather than B2B?
If the answers are mostly yes, it is worth testing. If several are no, put the budget toward what is working and revisit when the platform matures.
When you are ready, the process is the same as it was when we first covered this: register with OpenAI, invite Q1Media as your agency partner, and we will handle the rest.
Frequently Asked Questions:
Thank you! Your submission has been received. 
A Q1Media representative will be in touch shortly.
If you need immediate assistance please reach out to info@q1media.com or call 512-388-2300.
A Q1Media representative will be in touch shortly.
Oops! Something went wrong while submitting the form.
Blog
Download
Campaign Quick Facts
Here’s What Our Client Has to Say
About the Client
Results and Successes
DOWNLOAD THE CASE STUDY NOW
Build Your Strongest Pipeline Yet
Paid Media and Travel/Tourism
Why Destination Marketers Are Ditching Flat Display Ads for Interactive OnesWhy Destination Marketers Are Ditching Flat Display Ads for Interactive OnesWhy Destination Marketers Are Ditching Flat Display Ads for Interactive Ones
Interactive ads let travelers choose their content and reveal what they actually want. See why DMOs are moving away from flat display for smarter engagement.
Read more
SEM
2026 Digital Marketing Trends You Should Know This Summer 2026 Digital Marketing Trends You Should Know This Summer 2026 Digital Marketing Trends You Should Know This Summer Discover four summer marketing trends reshaping brand reach. Embrace AI, boost local awareness, and drive engagement with interactive ads. Learn more!

## Pull notes — mechanical only

- Pull date 2026-09-23, logged-out, no account. Main-text extraction drops navigation, footers and image content; images, charts and embedded posts are not captured.

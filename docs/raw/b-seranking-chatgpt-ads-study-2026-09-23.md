# SE Ranking — ChatGPT Shows Ads for 1 in 4 Commercial Prompts (incl. SE Ranking's own campaign test)

```yaml
source:          SE Ranking (Yulia Deda)
url_or_doc_id:   https://seranking.com/blog/chatgpt-ads-study/
published:       2026-08-10
pull_date:       2026-09-23
pull_method:     fetch — python urllib (browser user-agent, no login) + trafilatura main-text extraction; not the Chrome extension
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor study with n (50,006 prompts), US, method described; vendor sells an ads tracker
source_label:    vendor-reported
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     visibility
supersedes:      none
captured:        full page
verbatim:        full
```

Pass 12, Lane B (task P12-ads). Body below is the page's own text as extracted, unedited.

## Verbatim

ChatGPT shows ads on 1 in 4 commercial queries. Yet, 1 in 7 appear for the wrong topic
“I hate ads,” OpenAI’s CEO told an audience at Harvard in May 2024, describing advertising combined with AI as “uniquely unsettling” and a “last resort” for the company’s business model.
Less than two years later, that last resort arrived.
On January 16, 2026, OpenAI announced that ads were coming to ChatGPT.
And while much of the public conversation at the time focused on whether ads belong inside AI conversations at all, we wanted to answer a more practical question: What do ChatGPT ads actually look like at scale?
We analyzed 50,006 commercial prompts across 20 niches in the US, using the same prompt set from our previous AI Mode ads research. For every prompt, we recorded the generated answer, its cited sources, and the sponsored placement whenever one appeared.
We also ran ChatGPT Ads ourselves to see what the platform looks like from the advertiser side. Over roughly two weeks, our campaigns generated more than 97,000 impressions and 1,263 clicks, but very few sign-ups. We cover the setup, results, and key limitations in this section.
With that, let’s move to the overall results.
- 
                        
                        ChatGPT shows ads on 25.94% of commercial prompts, close to AI Mode’s 29.45%.
- 
                        
                        ChatGPT currently offers just one ad slot per answer, with no other placements available.
- 
                        
                        About 1 in 7 ads has no topical connection to the prompt it appears on. In niches like News & Politics and Relationships, more than 50% of ads are off-topic.
- 
                        
                        ChatGPT shows ads far more often in YMYL niches than AI Mode does. For example, ads appear on 28.69% of healthcare prompts in ChatGPT, compared with 2.64% in AI Mode.
- 
                        
                        Paying for an ad rarely gets the advertiser into the answer itself. In 96.37% of placements, the advertiser is not cited among the answer’s sources.
- 
                        
                        One comparison site, BestMoney, accounts for at least 13.56% of all ChatGPT ads in our dataset. At the niche level, Hungryroot dominates Food & Beverage with 79.92%, Booking.com leads Travel with 62.57%, and Robinhood accounts for 52.24% of Finance ads.
One important thing to keep in mind: ChatGPT ads are currently shown only to users on the Free and Go plans. So every result in this study reflects the ad-supported part of ChatGPT’s audience, not its full user base.
ChatGPT ads appear for around 26% of commercial queries
Of the 50,006 commercial keywords we analyzed, 12,974 returned an ad, giving ChatGPT an overall ad rate of 25.94%.
That is pretty close to what we previously found in Google’s AI Mode, where ads appeared for 29.45% of commercial queries.
In other words, the two platforms already monetize commercial intent at broadly similar rates.
However, the format and placement of these ads are different.
Every ChatGPT ad in our dataset:
- appeared below the generated answer;
- contained one sponsored offer;
- appeared without a competing ad alongside it.
To compare, 71.1% of ads in AI Mode included two ads side by side.
The same query can produce an ad in one ChatGPT session and no ad in another. So, while 25.94% is what we observed in this snapshot, the broader ad frequency could be higher.
What this means for advertisers: For now, your ad gets the sponsored space to itself, with no competitor shown beside it. But OpenAI is already testing multi-advertiser placements, so this may not stay the case for long.
About 1 in 7 ChatGPT ads is effectively off-topic
Most ChatGPT ads match the general topic of the query they appear for. But not all of them do.
Across all ad impressions, 14.35% were no more closely related to their own query than an ad paired with a random query from the dataset.
Put more simply, roughly one in every seven sponsored placements landed next to a question it had little to do with.
On top of that, in our manual review, we found additional ads that technically passed the similarity check but still did not feel very relevant to the user’s actual intent. So the true mismatch rate is likely somewhat higher.
The mismatch rate also varies sharply by niche.
In some categories, ads are usually relevant:
- Pets: 2.6% mismatch rate
- Travel: 4%
- Healthcare: 5%
In others, more than half of ads miss the topic:
- Relationships: 51.1%
- News & Politics: 54.2%
The examples below show how far the match can drift.
For the prompt “best dating apps for serious relationship,” ChatGPT included an ad for Quince (a retailer selling clothing, jewelry, and beauty products).
For “star ledger newspaper subscription,” ChatGPT showed an ad for TXU Energy (a retail electricity provider in Texas).
In both cases, the ad had little connection to the task the user was trying to complete.
Why does this happen?
The thing is, ChatGPT Ads do not use traditional keyword targeting. Instead, advertisers provide context hints: natural-language descriptions of the conversations they want to appear in, together with a few keyword-style phrases.
The platform says these hints guide matching, but they are not exact rules. Advertisers also cannot see the specific queries or conversations where their ads appeared.
That means the system may find a broad semantic connection even when the product is not a strong fit for the user’s actual request.
Another possibility is that there simply aren’t enough highly relevant conversations to show the ad in. In that case, OpenAI may place it in more loosely related ones. We can’t confirm this from our data, but it could help explain some of the mismatches.
Methodology note: We did not judge relevance based on shared keywords alone. ChatGPT Ads targets the broader meaning of a conversation, so an ad can still be relevant even when it uses different wording.
Instead, we measured the semantic similarity between the query, the ad title and description, as well as the generated answer. We also created a random baseline by pairing ads with unrelated queries. An ad was counted as a mismatch only when its similarity to the real query fell within the range normally produced by random pairings. We then manually reviewed a sample of the flagged cases.
The read on this: ChatGPT Ads is still at an early stage, and the matching system is clearly still learning how to translate broad conversational context into relevant placements. Most ads land in the right general area, but the 14.35% mismatch rate shows that context-based targeting can still stretch too far. For advertisers, that makes precise context hints and ongoing testing especially important.
ChatGPT shows healthcare ads roughly 10x more often than AI Mode does
The biggest difference between the two platforms appears in YMYL niches.
For instance, ads appeared on 28.69% of healthcare prompts in ChatGPT, more than 10 times the 2.64% rate we found in AI Mode.
News & Politics showed a similar pattern. ChatGPT displayed ads on 28.76% of prompts, compared with just 6.8% in AI Mode.
One possible reason is that Google has had more than two decades to build advertising policies, restrictions, and review processes around sensitive topics. Its ad system also operates within a search ecosystem that has long treated YMYL categories with additional caution.
That does not necessarily mean ChatGPT applies no additional safeguards. Our dataset measures ad frequency, not the complete set of policy decisions, blocked advertisers, or prohibited claims behind each placement.
However, it does show that, from a user’s perspective, sponsored messages are substantially more common around health and political or news-related conversations in ChatGPT than in AI Mode.
The broader niche distribution also looks very different across the two platforms.
- Education: 50.0% in AI Mode vs 14.18% in ChatGPT
- Travel: 50.4% vs 14.96%
- Finance: 44.7% vs 15.21%
- Entertainment & Hobbies: 59.6% vs 34.88%
- Relationships: 29.8% vs 12.76%
Some niches remained relatively consistent. Technology was almost identical at 29.4% in AI Mode and 28.76% in ChatGPT, while Business stood at 39.1% and 37.68%, respectively.
Why this matters: ChatGPT and AI Mode show ads at similar overall rates, but the distribution across niches differs. In our dataset, ChatGPT showed ads more often in Healthcare and News & Politics, while AI Mode showed them more often in categories such as Education, Travel, and Finance.
Only 3.63% of advertisers get cited in the answer they advertise under
For every ad placement, we checked whether the advertiser also appeared in the ChatGPT answer above it.
In most cases, it did not. The advertiser’s domain appeared among the cited sources in just 3.63% of placements, while the exact advertised URL appeared in only 0.09%, or 12 cases. Even a simple brand mention was rare, showing up in 4.44% of answers.
This overlap is also lower than in AI Mode, where advertiser domains appeared among cited sources in 11.53% of cases and exact URLs in 1.95%.
What advertisers should know: Paying gets your brand into the sponsored slot below the answer, but rarely into the answer itself. In 96.37% of placements, the advertiser is not cited.
13.56% of ChatGPT ads belong to a single site
In total, we identified 1,159 unique advertisers running ads in ChatGPT.
Compared with AI Mode, ChatGPT’s advertiser pool is smaller and more concentrated. AI Mode produced 25,243 ad appearances from 2,930 advertisers, averaging 8.61 appearances per advertiser. ChatGPT advertisers appeared 11.19 times on average.
This concentration is easy to see in the data: a few advertisers appear again and again, often taking a large share of ads within one or several niches.
The clearest example is BestMoney. It leads Insurance, Business, and Pets, and also appears among the top five advertisers in Finance and Travel. Across those five niches alone, it accounts for at least 1,759 appearances. This is 13.56% of all ChatGPT ads in our dataset.
A similar pattern appears within individual categories:
- Hungryroot accounts for 79.92% of Food & Beverage ads.
- Booking.com holds 62.57% of Travel.
- Robinhood holds 52.24% of Finance.
- TickPick holds 51.03% of Entertainment & Hobbies.
Some brands also spread into categories that are only loosely related to their products. For example, Intuit QuickBooks leads both Relationships and Technology, while VistaPrint appears among the top five advertisers in four niches, including Relationships and Entertainment & Hobbies.
The same issue appears even more clearly in News & Politics. In this niche, 54.2% of ads had little connection to the prompt they appeared with. The top advertiser was Stannp, a platform for sending direct mail.
And when you look a little closer, it becomes easier to see why. Many prompts in our sample focused on newspaper or newsletter subscriptions, so the targeting system likely picked up on concepts such as “mail,” “subscription,” and “publication.”
Technically, there is a connection. Practically, there is not: someone looking for a newspaper to subscribe is not looking for a direct mail platform.
By contrast, niches such as Pets and Travel had advertisers that were much closer to what users were actually asking about, and their mismatch rates were far lower.
A note on these figures: Advertiser-level results are especially sensitive to keyword choice. A different sample could produce different niche leaders and market shares, so treat these figures as a snapshot rather than fixed rankings.
What this tells you: ChatGPT’s ad market is not evenly distributed. In several niches, a single brand or comparison platform captures a large share of the available placements. Before entering a category, advertisers should check whether the market is fragmented or already dominated by a few repeat winners.
SE Ranking’s own test: ChatGPT ads delivered traffic, but not the right audience
We also tested ChatGPT Ads ourselves to see how the platform works from the advertiser’s side.
Over roughly two weeks, we ran three campaigns, eight ad groups, and 48 ads across the US, Canada, Australia, and New Zealand.
The campaigns focused on three audiences:
- people looking for AI visibility and AI Overview tracking tools;
- agencies interested in rank tracking, reporting, and GEO or AEO services;
- technical users searching for SEO APIs and MCP integrations.
The ads generated more than 97,000 impressions and 1,263 clicks, with an average CTR of 1.30%.
So mechanically, the platform worked. ChatGPT found conversations to place our ads in, delivered traffic, and generated clicks at a reasonable rate.
The problem came after the click.
The campaigns generated very few sign-ups, so the results were not strong enough for us to continue.
One likely reason is audience eligibility. ChatGPT ads appear only to users on the Free and Go plans, while Plus, Pro, Business, and Enterprise users remain ad-free.
That creates a challenge for SE Ranking since our ideal customers (agency owners, SEO leads, and in-house specialists) are heavy AI users and, therefore, more likely to pay for an ad-free plan.
We also saw how unevenly ChatGPT distributes delivery.
The two largest ad groups received around half of all impressions, while some others received very little traffic. The same happened at the ad level: one or two creatives inside an ad group often received most of the impressions, while the rest barely ran.
This means that conversation volume and the way ChatGPT interprets context hints play a major role in deciding where delivery goes.
That said, our test also had important limitations. We launched while the platform was still in an early stage, used manual CPC bidding, and did not have in-platform conversion data available for optimization. ChatGPT Ads has added several features since then, including conversion-focused bidding and better measurement tools.
Our read: ChatGPT Ads can already generate reach and traffic, but that does not guarantee qualified demand. For B2B advertisers, the biggest challenge may not be the ad creative or the bid. It may be whether the people most likely to buy the product are even part of the audience that sees the ads.
What this means for advertisers and SEO teams
ChatGPT ads run on a different logic from search ads. Here is how to act on that.
- Consider ChatGPT ads as a separate channel
In 96.37% of placements, the advertiser was not cited among the sources used in the answer above it.
So do not expect ad spend to improve your visibility inside ChatGPT’s organic answer. The sponsored card is a paid-media placement; being cited or mentioned is an AI-visibility and content authority challenge.
That matters even more because users on paid ChatGPT plans do not see ads. If some of your best prospects fall into that group, organic AEO is the only way to reach them inside ChatGPT (by earning mentions and citations in the answer itself).
- Treat context hints as an experiment
ChatGPT advertisers do not target exact search queries. Instead, they describe the conversations they want to appear in using natural-language context hints and keyword-style phrases.
That gives the system more flexibility, but it can also stretch the match too far. In our dataset, 14.35% of ads were effectively off-topic, with mismatch rates above 50% in Relationships and News & Politics.
So, start with narrow descriptions of the audience, task, and situation you want to reach. Then use negative keywords to block ambiguous meanings and closely related topics that do not fit your offer.
And do not scale too quickly. Start with a limited test budget, watch where the traffic goes, and only increase spend once you see that ChatGPT is reaching the right audience and generating meaningful results.
- Make sure your ICP is part of ChatGPT’s ad-supported audience
ChatGPT ads are shown on ad-supported plans, while users on higher-priced professional and business plans do not see them.
That can matter for B2B advertisers. Agency owners, in-house specialists, and other heavy professional users may be more likely to pay for an ad-free plan—and therefore never enter the audience available to advertisers.
So before putting significant budget into ChatGPT Ads, ask a basic question: can the people most likely to buy from you actually see the ads?
If not, paid campaigns can only cover part of your audience. The rest has to be reached organically through AI visibility and AEO.
- Expect to own the whole ads block, at least for now
Every ChatGPT ad in our dataset appeared as a single sponsored card below the answer. Unlike AI Mode, there was no second advertiser competing for attention inside the same block.
So, for now, winning the placement means owning the sponsored space. But OpenAI has already tested multi-advertiser formats, so this advantage may not last.
- Track who is advertising against your core prompts
SE Ranking now lets you monitor ads appearing in ChatGPT and AI Mode alongside your wider competitive data.
You can find this under Competitive Research → AI Search → Prompts → Ads.
For every detected ad, you can see:
→ Who is advertising
The brand behind each sponsored placement, including companies you may not have considered direct competitors before.
→ Where the ad leads
The destination URL behind the ad, so you can see the exact offer and landing page being promoted.
→ How ad presence changes over time
Monthly tracking shows when competitors start appearing more often across your core prompts (and when new gaps open that you can move on first).
Together, these insights show not only who is advertising, but how competitors are using ChatGPT and AI Mode to promote specific offers (and where new opportunities are starting to open).
Research methodology
We analyzed 50,006 commercially oriented prompts across 20 niches in the United States. Data was collected on July 23, 2026.
Each niche contained approximately 2,500 prompts. For every prompt, we captured:
- whether an ad appeared;
- the ad’s title, description, advertiser, and destination;
- the position and number of ads;
- ChatGPT’s generated answer;
- sources cited in the answer;
- whether the advertiser was cited or mentioned organically.
To assess relevance, we created embeddings for each prompt, ad, and generated answer and calculated cosine similarity between them.
We compared real prompt-ad pairs against shuffled pairs in which ads were matched with random prompts from the dataset. An impression was classified as off-target only when its similarity to its real prompt fell within the range typical of random pairings.
We also manually reviewed a sample of the flagged ads.
Disclaimer: The findings describe a snapshot, not a permanent feature of the platform. Ads rotate, and the same prompt may display a different ad (or no ad) when repeated. The composition of the advertiser pool can also change quickly, especially in a new marketplace. The niche-level advertiser rankings should therefore be read as patterns within our sample, not as a complete inventory of all advertisers active in ChatGPT.
Conclusion
ChatGPT already displays ads on roughly one in four commercial prompts, close to the rate we found in AI Mode.
But the platform is still clearly in an early stage. Ad relevance varies widely, and a small group of advertisers dominates many niches.
For advertisers, the opportunity is real, but so is the need to test carefully. Success depends on audience fit, context targeting, and whether the people most likely to buy can see the ads at all.

## Pull notes — mechanical only

- Pull date 2026-09-23, logged-out, no account. Main-text extraction drops navigation, footers and image content; images, charts and embedded posts are not captured.

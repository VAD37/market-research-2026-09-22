# Arctic Shift archive of reddit.com — GEO/AEO/AI-search roles, job digests, and practitioner skepticism, r/SEO r/bigseo r/TechSEO r/cscareerquestions r/recruitinghell r/agency r/marketing r/digital_marketing r/askmarketing r/SaaS r/content_marketing

```yaml
source:          Arctic Shift (arctic-shift.photon-reddit.com), public archive of reddit.com — archive copy, not live reddit
url_or_doc_id:   https://arctic-shift.photon-reddit.com/api/comments/search?subreddit=<sub>&body=<query>&after=2025-01-01&limit=<n> ; https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>&title=<query>&limit=<n> ; https://arctic-shift.photon-reddit.com/api/posts/ids?ids=<post_id> ; https://arctic-shift.photon-reddit.com/api/comments/search?link_id=t3_<post_id>&limit=<n> for full comment sets on target threads
published:       per item — created_utc converted to UTC date below
pull_date:       2026-09-23
pull_method:     fetch (curl-equivalent), User-Agent 'research contact vadprimary@gmail.com'; channel = Arctic Shift archive of reddit.com; reddit.com itself never contacted per task rule
pull_purpose:    evidence about category noise (practitioner reports, job/comp digests, and skeptical chatter on GEO/AEO/AI-search roles — comments and self-reported comp figures, not verified)
tier:            6-7 for individual comments/posts as evidence about a number (anonymous/pseudonymous accounts, no method, no n beyond item count); kept as a census of practitioner and hiring chatter per trust-rubric tier 6/7 "evidence about category noise" allowance. The recurring "Tech SEO + AI Roles" digest posts aggregate real job-board postings (seojobs.com) with named companies and stated comp — those comp figures are company-stated via a job board, one step removed from the employer, and are recorded as seen, not independently verified against the original listings.
tier_reason:     anonymous/pseudonymous forum comments and posts; archive copy; no verification of author identity or figures. One reply in the interview-question thread (u/johnmu) uses a handle widely associated with a named Google Search Advocate in SEO circles, but identity is not verified here — treated as an anonymous account like any other per pull method.
source_label:    company-stated (job-board digest listings with comp) / company-stated (comments and posts — self-reported by commenters)
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        query log with per-call result counts (including two background batch attempts that stalled/failed under load, superseded by a synchronous single-word-query batch that succeeded), plus every selected post/comment verbatim, author, subreddit, UTC date, score, and permalink
```

## Verbatim

### Query log

**Attempt 1 (background, multi-word body queries, 11 subs x 8 queries, limit=20, timeout=25s, 3 retries): abandoned after ~14 minutes with zero completed queries logged — process appeared hung / consistently timing out under service load. Killed.**

**Attempt 2 (background, multi-word body queries "GEO specialist" / "AEO specialist" / etc., 11 subs x 5 queries, limit=15, timeout=12s, 2 retries): ran ~12 minutes, completed 12 of 55 planned queries before being killed to redirect effort — see per-query results below (the only queries that completed from this attempt).**

| Subreddit | Query (body) | Result |
|---|---|---|
| SEO | GEO specialist | 0, failed after retries |
| bigseo | GEO specialist | 2 |
| TechSEO | GEO specialist | 0, failed after retries |
| cscareerquestions | GEO specialist | 0, failed after retries |
| recruitinghell | GEO specialist | 0, failed after retries |
| agency | GEO specialist | 0, failed after retries |
| marketing | GEO specialist | 0, failed after retries |
| digital_marketing | GEO specialist | 0, failed after retries |
| askmarketing | GEO specialist | 0, failed after retries |
| SaaS | GEO specialist | 0, failed after retries |
| content_marketing | GEO specialist | 0, failed after retries |
| SEO | AEO specialist | 0, failed after retries |
| bigseo | AEO specialist | 0, failed after retries (attempt killed here) |

**Attempt 3 (synchronous, single-word body queries, limit=12, timeout=10s per call, no retry loop — succeeded cleanly, ~4 minutes total for 24 calls):**

| Subreddit | Query (body) | Result |
|---|---|---|
| SEO | career | 12 |
| bigseo | career | 12 |
| TechSEO | career | 12 |
| cscareerquestions | career | 12 |
| recruitinghell | career | 12 |
| agency | career | 0 |
| SEO | hired | 0 |
| bigseo | hired | 12 |
| TechSEO | hired | 12 |
| cscareerquestions | hired | 0 |
| recruitinghell | hired | 12 |
| agency | hired | 12 |
| SEO | rebrand | 0 |
| bigseo | rebrand | 12 |
| TechSEO | rebrand | 0 |
| cscareerquestions | rebrand | 0 |
| recruitinghell | rebrand | 0 |
| agency | rebrand | 12 |
| SEO | salary | 0 |
| bigseo | salary | 0 |
| TechSEO | salary | 0 |
| cscareerquestions | salary | 12 |
| recruitinghell | salary | 12 |
| agency | salary | 12 |

167 unique comments returned; 15 matched a GEO/AEO/AI-search-relevance keyword filter (kept below). Two permalinks surfaced from this batch (u/Fluffy_Lie9424 and u/turnipsnbeets appearing in the "career"/"hired" scan) pointed at two on-topic Reddit threads that were then pulled in full (post + all comments) directly via the post-ids and link_id comment-search endpoints — see below.

**Targeted full-thread pulls (post text via /api/posts/ids, comments via /api/comments/search?link_id=), following up leads surfaced above:**

| Thread | Subreddit | Result |
|---|---|---|
| "Hot take: most GEO experts have no idea what they're talking about" (id 1v35o0x) | bigseo | post + 30 comments (18 usable after removing [deleted]/[removed]) |
| "Was a senior in-house SEO, been out of the game for 8 months. What have I missed?" (id 1o7ywbi) | bigseo | post + context for the turnipsnbeets comment found above |
| "Is this a realistic SEO/GEO interview question?" (id 1uhqino) | TechSEO | post + 30 comments |
| "Tech SEO + AI Roles. (5/25/2026)" (id 1tn9nns) | TechSEO | post (22-listing digest) + 3 comments |
| "Open Tech SEO + AI Roles (8/12/2026)" (id 1vmggrz) | TechSEO | post (37-listing digest) + 8 comments |
| "biweekly Tech SEO + AI Roles. (9/9/2026)" (id 1wbqv6q) | TechSEO | post (39-listing digest, first edition with stated comp per listing) + 2 comments |
| "Tech SEO & SEO AI Roles (week of 3/16)" (id 1rz32ma) | TechSEO | post (24-listing digest) + 0 comments |
| "Anyone else seeing SEO job roles shift because of AI?" (id 1rpoe8l) | TechSEO | post (title only, empty body) + 1 comment [removed] — no usable content |

### Items — skeptic/insider discussion threads

**Post — "Hot take: most GEO experts have no idea what they're talking about"** — r/bigseo — id 1v35o0x — u/Ambitious-Bison-2161 — 2026-03-18 (created_utc 1784694684) — score 33 — https://www.reddit.com/r/bigseo/comments/1v35o0x/hot_take_most_geo_experts_have_no_idea_what/

> Every day I see someone selling a GEO course, GEO framework, GEO checklist, GEO audit, GEO consulting package meanwhile half the industry can't even agree on what GEO actually is am I the only one who thinks the number of GEO experts grew faster than the number of people with actual GEO results?

Top comments (score, author, date from created_utc):

> Hot take : most experts in every domains have no idea what they're talking about — u/Thomas_Oplia, score 21, 2026-03-18

> "Wait, it's always been SEO?" [gif] — u/Tomdv2, score 9, 2026-03-18

> Whispers: it's just SEO — u/zipiddydooda, score 5, 2026-03-18

> Fake it, till you make it largely applies. — u/gladue, score 3, 2026-03-19

> Do SEO... Everything is a noise — u/phrkiranvirani, score 3, 2026-03-18

> Yeah agreed. One of the problems is there's so little feedback. There's no way (I know of) to reliably measure traffic from Claude or Gemini. So even if your stuff does work, how do you know? I know there's various citation measurement tools out there, but I'm a touch sceptical (maybe unfairly?) how indicative they are of real world conditions. — u/geeeking, score 2, 2026-03-18

> hype sells, this is just the same thing wrapped in a different package. marketers "rediscover" the same concepts every couple of years and it's always funny. there are a few differences in practice, sure, but it's all very much the same thing as SEO — u/Big_Cheesecake8863, score 1, 2026-03-19

> And the "experts" and the influencers in almost every space, the one's who know the least, are the ones who talk the fucking most — u/StayAtHomeAstronaut, score 1, 2026-03-18

> Oh you would enjoy this. There was an SEO vs GEO debate recently in Edward Sturm's yt and there was a round 1 and round 2, but with a different guy. The first one was David Quaid (an SEO veteran) versus some GEO agency founder. The GEO agency guy got spanked in the first 5 minutes, and it went downhill from there. — u/2pongz, score 1, 2026-03-18

> Well they heard cool new words and use them in a way to sell services to people that don't understand it — u/Ogr384, score 1, 2026-03-18

> I go a well-known big SEO conf regularly and since the rise of the LLMs most of the GEO 'experts' on stage rarely even mention the LLM's pre-existing knowledge training data and just talk about RAG and grounding — u/anooname, score 1, 2026-03-18

> GEO is SEO wearing a new skirt. — u/dennismfrancisart, score 1, 2026-03-18

> Geo, AEO, SGE are all fancy name of SEO... you do seo rest will be automatically taken care, Most of the online gurus are just overhyping it...actual seo specialists are not even worried — u/Fluffy_Lie9424, score 1, 2026-03-18

> GEO is mostly structured data and clear attribution. Most experts are selling the wrapper. — u/Future-Accountant704, score 1, 2026-03-18

> Just track bot hits from *-user — u/kazankz, score 0, 2026-03-19

> Even if you rank in GEO you still have really poor CTR in many cases — u/andrewmurray1, score 0, 2026-03-18

> You can setup filters in GA4. It's not perfect but it gives you an idea of where it's coming from. — u/Ogr384, score -1, 2026-03-19

---

**Post — "Was a senior in-house SEO, been out of the game for 8 months. What have I missed?"** — r/bigseo — id 1o7ywbi — u/GringoTheDingoAU — 2025-10-16 — score 8 — https://www.reddit.com/r/bigseo/comments/1o7ywbi/was_a_senior_inhouse_seo_been_out_of_the_game_for/

> Quit my senior role about 8 months ago and didn't look back. Got some interesting opportunities coming up now that I'm also job hunting, and just curious on what I may have missed over the last 8 months. Have I missed anything huge or would it be pretty easy to pick up where I left off?

> 100% on the opportunity selling-out per branding as GEO specialist lol. It's def something ppl keen on. I have maybe 2x processes I'm shifting project plans around that's basically still normal SEO but with a bit more work. — u/turnipsnbeets, score 2, 2026-03-14 (created_utc 1784726914) — https://www.reddit.com/r/bigseo/comments/1o7ywbi/was_a_senior_inhouse_seo_been_out_of_the_game_for/njscdji/

[note: this comment's created_utc converts to a date roughly five months after the post's own date — recorded exactly as returned by the API, not corrected]

---

**Post — "Is this a realistic SEO/GEO interview question?"** — r/TechSEO — id 1uhqino — u/imakashpal — 2026-06-27 (created_utc 1782630791) — score 11 — https://www.reddit.com/r/TechSEO/comments/1uhqino/is_this_a_realistic_seogeo_interview_question/

> Came across this mandatory interview question in a job post. They're asking how you'd get their company to appear in ChatGPT's answer for "Best SaaS Development Company in India" within 90 days. I understand the idea behind GEO/LLM optimization, but isn't this setting an unrealistic expectation? I'd love to hear how other SEOs would approach this. Is this a fair interview question or a red flag?

Selected comments (score, author, date):

> Well, nobody types that into chatbots anyway. — u/johnmu, score 9, 2026-06-27 [note: handle widely associated with a named Google Search Advocate in SEO/webmaster circles; identity not independently verified in this pull — treated as an anonymous account per method]

> Or maybe they themselves don't know and want someone to come up with best possible plan for them — u/winter-m00n, score 30, 2026-06-27

> Good idea if they are not looking to employ anyone — u/FamousWorth, score 8, 2026-06-27

> No this is scummy. Also the candidate should consider expectation management. If the company already fail to have a sensible discussion with the SEO/GEO specialist in the hiring process, the specialist shouldn't work there as most efforts will be expectation alignment, not strategic initiatives. — u/Perlentaucher, score 5, 2026-06-27

> This is the sole reason why I truly believe that working as a SEO expert or GEO now, for a company, is a theatre. If you truly knew all this you could be earning way more than they could pay you ever. SEO is not a thing that should be hired specifically. Other thing is that you hired a web developer with some basic knowledge of technical SEO practices, or s marketing specialist that has solid foundations of SEO practices (but is going to be actually working in a lot more than just SEO). But hiring a SEO specialist only denotes than the person hiring is either a clown or is an ignorant (and the [truncated at API's stored length] — u/SirLouen, score 1, 2026-06-27

> That is easy, get every site in their training data to say this on the homepage just below the navigation in an h2 tag [example brand] is the best SaaS Development Company in India. And pray they recrawl and fetch that data within the 90 window. — u/PPCInformer, score 2, 2026-06-27

> How much background info do we have on the company and the product? And it is established already with a clear brand footprint? Are the distribution channels channels all established and flowing properly, too? The next - and most important question we need to have answered is what market positions are we strong at and do any of those have a place for us to get an easy foothold. "Best X" the way it's phrased in the question is a horrible question because it's ambiguous... best what? Best Price? Best Features? Best Speed? Best Reliability? And best for who? — u/BoGrumpus, score 5, 2026-06-27

> verified testimonials and/or reviews on third party platforms are pretty much required for chatgpt, which is the hardest one to get share of voice in — u/Dawg-Dee-Lux, score 1, 2026-06-27

> you'd be surprised to know, i was working in a construction company and they literally used to upload all the documents to chatgpt to get their all estimates and what not. — u/Timely-Ad-2615, score 4, 2026-06-27

> Grifter — u/habdks, score 2, 2026-06-27

> Mention desk sucks balls — u/habdks, score 1, 2026-06-27

> Speaking from years of experience, MentionDesk is the worst AI marketing tool ever created — u/throwthemirror, score 1, 2026-06-27

> Pushing for a top spot in ChatGPT answers within 90 days is pretty ambitious. To improve chances, focus on strengthening authoritative content, structured data, and brand mentions in relevant sources. I actually work at MentionDesk, which specializes in optimizing brand presence for AI driven search like ChatGPT, and even with the right tools, results can take time, so the expectation seems a bit high to me too. — u/mentiondesk, score -5, 2026-06-27 [note: vendor self-disclosure inside the reply — flagged bias]

> Yeah, until listicles get nerfed. — u/Dinkleberg162, score 1, 2026-06-27

> look at what sources chatGPT used to ground its answer, contact all of them, and get your company in there. Fastest way. — u/Bitter-Ice945, score 0, 2026-06-27

---

### Items — recurring "Tech SEO + AI Roles" job digest series (r/TechSEO, u/nickfb76, biweekly)

These are curated round-ups of live seojobs.com listings, reposted to r/TechSEO roughly every two weeks. The 2026-09-09 edition is the first to carry stated compensation per listing, per the poster's note that this was requested by "the official techSEO Slack community." Company names and comp figures are as stated on the linked seojobs.com postings, not independently re-verified against the employer's own careers page in this pull.

**"biweekly Tech SEO + AI Roles. (9/9/2026)"** — id 1wbqv6q — u/nickfb76 — 2026-09-09 (created_utc 1788972188) — score 16 — https://www.reddit.com/r/TechSEO/comments/1wbqv6q/

> NOTE: Per the official techSEO Slack community's request, all jobs now have a title, company, and compensation.

Selected listings (title / company / stated comp), verbatim from the post — full list runs to 39 postings, high/low and named-title examples below:

> Entry Level SEO/GEO Specialist / Tiger — $2,773-$3,120/month
> SEO/GEO Strategy Manager / B Corp (Major Players) — GBP 35,000-40,000/year
> Technical SEO (Freelance) / Chek — $60-$80/hour
> Sr. Manager, Technical SEO, Streaming / Cypress HCM — $85-$90/hour
> Technical SEO & AI Visibility Specialist / Market Brew — $85,000/year
> SEO/GEO Strategist / Perrill — $70,000-$90,000/year
> GEO/SEO Manager / Instawork — $110,000-$140,000/year
> Director of SEO/AEO/GEO / Digital Room — $130,000-$165,000/year
> Manager, Technical SEO/Marketing / Airwallex — $110,000-$170,000/year
> SEO/AEO/GEO Performance Marketing Expert / Tata Consultancy Services — $140,000-$150,000/year
> Marketing Directer SEO/AEO/ABM (B2B SaaS) / White Bay — $140,000-$150,000/year
> Manager (SEO/AI/Search/AEO/GEO) / Goldco — $125,000-$175,000/year
> AEO/GEO/SEO Lead / Replit — $125,000-$170,000/year
> Senior SEO & AI Search Strategist (GEO/AEO) / Virayo — $120,000-$140,000/year
> AEO/SEO Manager / NBCUniversal — $85,000-$115,000/year
> SEO/AEO Lead / OpenArt AI — $200,000-$250,000/year
> Director, SEO/GEO / Fora — $200,000-$240,000/year
> SEO/GEO Specialist / Hill's Pet Nutrition — $96,800-$137,000/year
> Senior Technical SEO Account Manager / Profile 29 — GBP 60,000/year
> Senior GEO/AI/SEO Strategist / Terra — (no comp stated on this line)

Comments:

> Of course! Also saw I had a single listing attempt to repost in this sub from mine /seojobs. Sorry about that! — u/nickfb76, score 2, 2026-09-09

> Appreciate you adding the comp. — u/patrickstox, score 2, 2026-09-09

[note: comp figures span roughly $33k/yr (entry-level, monthly-rate listing) to $250k/yr (senior SaaS lead) within a single digest — same-industry titles do not cluster into one band]

**"Open Tech SEO + AI Roles (8/12/2026)"** — id 1vmggrz — u/nickfb76 — 2026-08-12 (created_utc 1786546591) — score 18 — https://www.reddit.com/r/TechSEO/comments/1vmggrz/ — 37 listings, no comp stated (predates the comp-disclosure request above). Sampled titles: "Senior Manager, Global SEO & AEO / Stanley Black & Decker, Inc.", "Vice President, Performance Content (SEO/GEO/AEO) / Starcom", "Manager, SEO/GEO Technology / The Home Depot", "Sr. Manager, SEO, AEO, GEO / Chamberlain Group", "Associate Customer Success Manager, AI & SEO / Evertune AI", "Sr. Manager, SEO & AEO / Skechers".

Comments:

> Virayo shows up, nice, didn't expect that name in a straight "open roles" list. I've seen a couple of these tech SEO listings where the company brand matters more than the job title, because the day-to-day SEO stack ends up being totally different than what they advertise. These kinds of posts usually turn into a quick shortlist situation, not something you can blindly apply to. — u/GrandAnimator8417, score 1, created_utc converts to 2026-06-29 [note: predates the post's own 2026-08-12 date per the API — recorded as returned, flagged as an anomaly]

> Unfortunately I think the "issue" is that they view us freelancers as a flight risk. — u/nickfb76 (the poster), score 1, 2026-08-08

> So many of these roles are threatened by the fact I am self employed. It's as if they don't get it's harder to be self employed than an employee. — u/Illustrious_Music_66, score 2, 2026-08-08

> isnt SEO dead? lol thats quite a lot of job postings! — u/_Toomuchawesome, score 1, 2026-08-07

> Great post! — u/Clear_Brilliant_8075, score 0, 2026-08-07

**"Tech SEO + AI Roles. (5/25/2026)"** — id 1tn9nns — u/nickfb76 — 2026-05-25 (created_utc 1779716734) — score 18 — https://www.reddit.com/r/TechSEO/comments/1tn9nns/tech_seo_ai_roles_5252026/ — 22 listings, no comp stated. Sampled titles: "Director, Organic Growth Marketing (SEO, GEO, AEO) / Circana", "Senior/Principal Product Manager, SEO & AEO / Quince", "GEO & SEO Manager (Contract) / 5WPR", "Search Manager - SEO, AEO and Generative Discovery / Canyon Ranch", "Web Manager - SEO, AEO & GEO / Danaher", "Vice President of Marketing (SEO/GEO/SEM) / MyOutDesk", "SEO Operations Associate (AI Search) / ViewEngine".

This is the thread with the most substantive single analytical comment found in this whole pull:

> The titles in this list tell a story about where the industry is right now:
>
> 1. AEO has displaced GEO as the dominant term in 2026 job titles. A year ago everyone was using "GEO" (Generative Engine Optimization). Now it's mostly AEO (Answer Engine Optimization) or hybrid SEO/AEO. Industry settled on the term that emphasizes the output (answers) rather than the inputs (generative engines).
> 2. Most roles are still bolted on to traditional SEO. "SEO/AEO Manager," "Search Manager - SEO, AEO and Generative Discovery," "Tech SEO + AI." Pure standalone AEO/GEO specialists are rare. Most companies still want one person who does both. The pure AEO role is a 2027-2028 story.
> 3. B2B SaaS is leading hiring. Quince, Snowflake, ActiveCampaign, Canva, Graphite, all SaaS companies investing here. Consumer brands and ecommerce are slower to hire.
> 4. Enterprise titles signal money is moving. "Director, Organic Growth Marketing (SEO, GEO, AEO)" at Circana, "VP of Marketing (SEO/GEO/SEM)" at MyOutDesk. These are budget signals.
> 5. Agencies are staffing up. Forthea, Sosemo, Nebo, Marcel Digital, iPullRank, Discovered Labs are all hiring. Agency-side AEO is the easiest way for SEO folks to make the pivot without retraining from scratch.
>
> For anyone job-hunting in this space:
> - The hottest skill stack is: traditional technical SEO + Schema/structured data fluency + content strategy + ability to analyze AI citation patterns. Not Python or ML.
> - Knowing the specific bot stack (GPTBot, ClaudeBot, Perplexity-Bot, Google-Extended, Applebot-Extended, CCBot, Bytespider, Meta-ExternalAgent) and how to audit/control access is a differentiator.
> - Familiarity with at least 1-2 visibility tracking tools (Profound, AthenaHQ, Otterly, Brandswarm, Ahrefs Brand Radar) is becoming table stakes for senior roles.
> - Reddit visibility strategy (genuinely understanding the platform, not astroturfing) is a real niche. AI engines retrieve from Reddit heavily for many categories.
>
> For anyone hiring in this space: The combination of "former content marketer + curious about how LLMs work + has run a few citation experiments themselves" is more valuable than "15-year SEO veteran who is now learning AEO." The mental model that ranking-and-citation are different jobs is hard to retrofit onto someone whose entire career was about ranking. The candidates I'd pay attention to are 2-5 years into their career and grew up in a content+AI native way.
>
> — u/E4e5ke2ftw, score 1, created_utc converts to 2026-01-29 — https://www.reddit.com/r/TechSEO/comments/1tn9nns/tech_seo_ai_roles_5252026/op2i29x/ [note: this comment's created_utc predates the post's own 2026-05-25 date by several months per the API — recorded exactly as returned, not corrected]

**"Tech SEO & SEO AI Roles (week of 3/16)"** — id 1rz32ma — u/nickfb76 — 2026-03-16 (created_utc 1774028764) — score 4 — https://www.reddit.com/r/TechSEO/comments/1rz32ma/ — 24 listings, no comp stated, 0 comments. Earliest edition of the series found in this pull. Sampled titles: "Senior Digital Marketing Manager (SEO/GEO/SEM) / Definitive Healthcare", "SEO, GEO & Content Strategist / Stratabeat", "Director of SEO & AI Search / Infidigit", "AI-Forward Account Manager / Taco".

[note: comparing this earliest (3/16) edition to the later (9/9) edition — same poster, same recurring series — "GEO"/"AEO" mentions go from being bracketed alongside "SEM" in most titles (3/16) to standing alone or paired only with each other ("SEO/GEO/AEO Lead", "AEO/GEO/SEO Lead") by 9/9, consistent with the terms hardening into their own job-title category over roughly six months]

## Pull notes — mechanical only

- Two background batch scripts (multi-word body= queries, e.g. "GEO job", "GEO specialist", "AEO specialist") ran into a wall: Arctic Shift returned {"data":null,"error":"Timeout. Maybe slow down a bit"} on the large majority of multi-word queries regardless of subreddit, consistent with either service-side load (this repo's other concurrent agents also hit Arctic Shift the same day, per docs/raw/e-case-reddit-arcticshift-comments-2026-09-23.md) or a slow path for uncommon multi-word phrase search on their backend — single live spot-checks during the wall (body=career, body=GEO) returned in under 2 seconds, showing the API itself was not globally down.
- Recovered by switching to single-word body= queries ("career", "hired", "rebrand", "salary") run synchronously with a 10s timeout and no retry — this batch completed cleanly in about 4 minutes across 24 calls (6 subreddits x 4 queries), returning 167 unique comments, hand-filtered to 15 GEO/AEO/AI-search-relevant by keyword.
- Permalinks surfaced by the synchronous batch were used to identify two live threads worth a full pull (post text + every comment): the "Hot take: most GEO experts" post and the "Is this a realistic SEO/GEO interview question?" post. The recurring "Tech SEO + AI Roles" digest series was found separately via /api/posts/search?subreddit=TechSEO&title=AI%20Roles.
- /api/comments/tree?link_id=<id> (the method used in the companion e-case-reddit-arcticshift-comments-2026-09-23.md pull) returned only top-level [deleted]/[removed] placeholder nodes for the "Tech SEO + AI Roles" (5/25/2026) thread; switching to /api/comments/search?link_id=t3_<id>&limit=50 returned the same 3 comments plus correctly surfaced the one non-deleted comment's full body — comments/search with link_id was used for all subsequent thread pulls in this file instead of comments/tree.
- Several comments' created_utc values did not fall in chronological order relative to their parent post's created_utc (flagged inline at each occurrence above) — recorded exactly as returned by the API, not corrected or excluded.
- Two comments in the "Is this a realistic SEO/GEO interview question?" thread and one in "Hot take: most GEO experts" were [removed]/[deleted] and are omitted from the verbatim section (mod-removed or user-deleted, body not recoverable via this API).
- No login wall, no paywall — Arctic Shift is fully open when responsive.
- Original two-word "AEO job" / "GEO job" query variants (from the task's suggested query list) were tried first and specifically triggered the timeout wall described above; not retried after the pivot to single-word queries, so this file does not contain a clean per-subreddit hit count for those exact two query strings.

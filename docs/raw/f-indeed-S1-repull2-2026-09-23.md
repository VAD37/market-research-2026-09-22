# Indeed — US job search for "generative engine optimization", "AI visibility", "answer engine optimization", "AI search" marketing, re-pull 2

```yaml
source:          Indeed (indeed.com) job search, United States
url_or_doc_id:   https://www.indeed.com/jobs?q=%22generative+engine+optimization%22&l=United+States ; https://www.indeed.com/jobs?q=%22answer+engine+optimization%22&l=United+States ; in-page fetch of /jobs?q=<query>&l=United+States&start=<0,10,20>
published:       live search pages; posting ages as printed ("1 day ago" to "30+ days ago") relative to 2026-09-23
pull_date:       2026-09-23
pull_method:     browser (Chrome extension); search pages rendered in the tab and fetched in-page; job-card fields read from the page's own `mosaic-provider-jobcards` data
session:         logged-in, US location (Chrome profile logged into Indeed by the user; first page header showed "Messages Unread count 0"; the later rate-limit page showed "Sign in")
pull_purpose:    evidence about a number
tier:            3
tier_reason:     demand-signals.md S1 default ("3, employer's own posting"); card fields only — the posting text naming the AI-visibility duty was read for 1 of 35 postings
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      docs/raw/f-jobs-upwork-indeed-freelancer-S1-repull-2026-09-23.md (Indeed probe: "Additional Verification Required")
captured:        job-card fields (title, employer, location, salary as shown, date-posted text, result tier) for 2 of 36 planned queries; full description for 1 posting
verbatim:        partial — card fields verbatim; the characters & ? = ; in card fields were replaced by spaces by the extraction step (e.g. "AT&T" rendered "AT T", "Head of Search & AI Visibility" rendered "Head of Search   AI Visibility"); corrected spellings shown in [brackets] only where the rendered page text shows the original
```

## Access log — verbatim page states

1. Navigate `jobs?q="generative engine optimization"&l=United States` — title "Now Hiring: 25 Generative Engine Optimization Jobs in United States | Indeed". Rendered, no wall.
2. In-page fetch, same query, `start=0,10,20`: 15 + 10 + 15 cards; the third page repeated earlier job keys; 25 unique. Page data `tierSummaries`: `[{"jobCount":2,"tier":6,"type":"NATIONWIDE"}]`.
3. In-page fetch, `"AI visibility"`: 23 unique job keys across 2 pages. [note: these 23 cards were held in page memory only and were lost when the tab navigated; not recorded. Re-pull blocked by step 5.]
4. In-page fetch, `"answer engine optimization"`, then `"AI search" marketing`: rate limit. Navigating to the AEO URL showed title "Too Many Requests - Indeed.com", text: "Too Many Requests / You have been rate limited. Please go to support.indeed.com and reference the following information: / Your Ray ID for this request is a3f72b5f3da1daa5 / Your current IP for this request is 159.26.115.98".
5. After a pause (~10 minutes, TED pulled meanwhile): navigate `jobs?q="answer engine optimization"&l=United States` — title "Answer Engine Optimization Jobs, Employment in United States | Indeed", rendered; 15 cards read from the rendered page; `tierSummaries` `[{"jobCount":0,"tier":6,"type":"NATIONWIDE"}]`. Next in-page fetch, `"generative engine optimization" insurance`: HTTP 200 with page text "Additional Verification Required" and no job-card data. **Channel stopped here per brief.** No verification step attempted.

Queries not run (wall): `"generative engine optimization"` + insurance, "financial services", legal, skincare, beauty, cosmetics, SaaS, "B2B software"; the same eight for `"AI visibility"`, `"answer engine optimization"`, `"AI search" marketing`; `"AI search" marketing` base query; page 2 of `"answer engine optimization"`.

## Verbatim — job cards

Query key: GEO = `"generative engine optimization"`; AEO = `"answer engine optimization"`. Tier = Indeed's own card tier (`NATIONWIDE` = "Similar jobs recruiting nationwide" block).

| # | jobkey | title | employer | location | salary as shown | date-posted text | card tier | query |
|---|---|---|---|---|---|---|---|---|
| 0 | 57f8f6af46c6b497 | GEO Strategist / Consultant | Mapout Digital Solutions Inc, | United States | $150,000 - $170,000 a year | 18 days ago | NATIONWIDE | GEO |
| 1 | f1650974c0f46a16 | AI-Native Marketing Lead | RestauNax | United States | $10 - $25 an hour | 17 days ago | NATIONWIDE | GEO |
| 2 | 35e3ce3d36d3f491 | Lead, Digital Customer Growth | AT T [AT&T] | Bothell, WA | $128,400 - $215,800 a year | 22 days ago | DEFAULT | GEO+AEO |
| 3 | e59feb873fcdffbe | Staff AI Scientist | Intuit | Mountain View, CA 94043 | $209,500 - $283,500 a year | 30+ days ago | DEFAULT | GEO |
| 4 | cb91e530733844e4 | Staff Product Manager, Acquisition   Growth [& Growth] | A Place for Mom | Austin, TX | $165,000 - $195,000 a year | 30+ days ago | DEFAULT | GEO |
| 5 | 5ed892e192423d0d | Director, Ecommerce | Fresenius Kabi | Lake Zurich, IL 60047 | $180,000 - $210,000 a year | 30+ days ago | DEFAULT | GEO+AEO |
| 6 | 646cc0c2c90d08cd | Director, Marketing and Brand Strategy | MAHEC | Vanderbilt, MI | — | 6 days ago | DEFAULT | GEO |
| 7 | 1775b88cc4d0478d | Specialist, Digital Platforms | Liliuokalani Trust | Honolulu, HI 96813 | $74,000 - $86,000 a year | 12 days ago | DEFAULT | GEO |
| 8 | 3d7d07f7b9df6c71 | Head of Search   AI Visibility [Head of Search & AI Visibility] | Vasion | Saint George, UT 84770 | — | 13 days ago | DEFAULT | GEO+AEO |
| 9 | 31b38374c6520b12 | Associate, Insights   Intelligence [& Intelligence] | Rational 360 | Washington, DC 20036 | $60,000 - $65,500 a year | 30+ days ago | DEFAULT | GEO |
| 10 | 43f8fcc9c7d922ab | SEO Specialist | Safe Life US LLC | Nashville, TN | — | 30+ days ago | DEFAULT | GEO |
| 11 | cf461bb5797236e7 | Content Editor   AEO Strategist [Content Editor & AEO Strategist] | Giftogram | Whippany, NJ 07981 | — | 14 days ago | DEFAULT | GEO |
| 12 | 9fc681c34ad1afb0 | Deputy Editor | Playboy Enterprises, Inc. | Miami Beach, FL 33139 | $140,000 - $160,000 a year | 30+ days ago | DEFAULT | GEO |
| 13 | 6bdb31ec0e0aeac2 | Website Marketing Specialist | MPI Label Printing | Sebring, OH 44672 | $28 - $35 an hour | 11 days ago | DEFAULT | GEO |
| 14 | 656dd6f138c6cccf | AI-Native Marketing Lead (Growth) | RestauNax | Remote | $15 - $25 an hour | 17 days ago | DEFAULT | GEO |
| 15 | d38d40264e305d23 | SEO Content Strategist | The Pond Guy | Armada, MI 48005 | — | 30+ days ago | DEFAULT | GEO+AEO |
| 16 | e06feca848704957 | Senior Manager, Performance Marketing | Ziggi's Coffee | Mead, CO 80542 | $120,000 - $150,000 a year | 30+ days ago | DEFAULT | GEO |
| 17 | 308cdfef345a76b6 | Associate Director, Global Media Relations | Astellas | Northbrook, IL | $144,060 - $205,800 a year | 30+ days ago | DEFAULT | GEO+AEO |
| 18 | 30a76aa9f9555acc | Search Engine Optimization Specialist | Solventum | Minnesota | $107,600 - $147,950 a year | 30+ days ago | DEFAULT | GEO |
| 19 | 2ac7d8da6b4601c5 | Sr. Digital Marketing Specialist – Paid Media, Performance   AI Search | Ann   Robert H. Lurie Children’s Hospital of Chicago [Ann & Robert H. Lurie] | Streeterville, IL | $70,720.00 - $115,627.20 a year | 25 days ago | DEFAULT | GEO |
| 20 | a10a0df403da77dd | Lead Analyst, Technical Search (SEO/AEO/GEO) | The Cigna Group | Bloomfield, CT | $79,100 - $131,800 a year | 8 days ago | DEFAULT | GEO |
| 21 | 99f0775fe45fa801 | Senior Manager, Social Media Strategy   Marketing | Choice Hotels | North Bethesda, MD | $123,663 - $145,486 a year | 22 days ago | DEFAULT | GEO |
| 22 | aa146ce1b56eec6a | Senior Manager, Performance Search   AI Marketing | Walgreens | Deerfield, IL 60015 | $125,000 - $218,750 a year | 12 days ago | DEFAULT | GEO |
| 23 | ac7d83940408a711 | Director of Marketing, Communications, and Membership | CuriOdyssey | San Mateo, CA 94401 | $140,000 a year | 11 days ago | DEFAULT | GEO |
| 24 | 14eaed4b7f6f26ba | Bilingual Mandarin Product Manager (SEO SaaS Product) | CWILL INC | City of Industry, CA 91746 | $100,000 - $160,000 a year | 1 day ago | DEFAULT | GEO |
| 25 | b88fa3fcf2679273 | Senior Marketing Specialist | HCVT | West Los Angeles, CA | $80,000 - $90,000 a year | 30+ days ago | DEFAULT | AEO |
| 26 | 53ae9c44149525b7 | Vice President for Marketing Communications | Gwynedd Mercy University | Gwynedd Valley, PA 19002 | — | 7 days ago | DEFAULT | AEO |
| 27 | 9ecbc868eb0dfe6f | CCYP Marketing Operations Specialist | IMPULSE UNIVERSE INC | Rosemead, CA 91770 | $46,000 - $60,000 a year | 22 days ago | DEFAULT | AEO |
| 28 | c623b42d89cd1c27 | CCYP Digital Content   Web Coordinator | IMPULSE UNIVERSE INC | Rosemead, CA 91770 | $3,900 - $4,500 a month | 22 days ago | DEFAULT | AEO |
| 29 | 02e2f5fabc842d6a | Senior Writer Project Manager | Viderity Inc. | Alexandria, VA | $108,292 - $128,292 a year | 30+ days ago | DEFAULT | AEO |
| 30 | 0b56a079db3fb1a6 | Legal Content Writer | Accel Marketing Solutions, Inc. | Montvale, NJ 07645 | $50,000 - $60,000 a year | 30+ days ago | DEFAULT | AEO |
| 31 | 41ae8ae4391e69df | Independent Contractor Opportunity: Fractional IT Manager (1099) | CAL Financial, Inc. | Edina, MN 55439 | $40 - $60 an hour | 30+ days ago | DEFAULT | AEO |
| 32 | 4af2273ebfd64d19 | Content Writer | The Advocates | Remote | $23 - $26 an hour | 6 days ago | DEFAULT | AEO |
| 33 | 144bb2740ba10297 | Web Content Specialist I | Smith   Wesson Brands, Inc [Smith & Wesson] | Maryville, TN 37801 | — | 30+ days ago | DEFAULT | AEO |
| 34 | 8711becc75954cf4 | Brand Content Strategist | GESA CREDIT UNION | Richland, WA 99352 | $29.90 - $60.25 an hour | 26 days ago | DEFAULT | AEO |

[note: the card data carried an empty `snippet` field for every card; no duty text is available from the cards. Match on the quoted phrase is Indeed's own search matching, not verified per posting.]

## Verbatim — full description, posting #0 (right pane of the first rendered page)

"GEO Strategist / Consultant / Mapout Digital Solutions Inc, / United States • Remote / $150,000 - $170,000 a year - Full-time"

> "As a GEO Strategist / Consultant, you will serve as the strategic backbone of Indegene’s Generative Engine Optimization engagements — translating client business objectives into actionable GEO strategies, defining optimization roadmaps, and advising pharma brand, digital, and medical teams on how to achieve discoverability and authority in AI-driven search ecosystems (ChatGPT, Perplexity, Google AI Overviews, Bing Copilot, and emerging LLM platforms)."
> "Develop comprehensive GEO strategies for pharma brands, therapeutic areas, and HCP/patient audiences — covering entity optimization, content authority, structured data, and LLM discoverability."
> "Define and monitor engagement-level KPIs: AI citation rate, entity authority scores, LLM content coverage, and AI share of voice"
> "Navigate MLR/MedLegal considerations in GEO strategy design, ensuring all recommendations are regulatory-compliant while maximizing search and AI performance."
> "Minimum 1–2 years of demonstrated experience in GEO, LLM content strategy, or AI-driven search optimization."
> "Pay: $150,000.00 - $170,000.00 per year"

## Employer size — as stated in posting or employer page

No posting body or employer page was read for postings #1–#34 (channel stopped). Posting #0 states no headcount or revenue. All 35: `unassigned`.

## Pull notes — mechanical only

- 5 search-page requests succeeded (3 GEO pages, 2 "AI visibility" pages) before the rate limit; 1 rendered navigation succeeded after the pause; the next request hit "Additional Verification Required".
- The "25" count comes from the page title; the in-page fetch returned no count line.
- No Indeed login, form, or verification step was touched.

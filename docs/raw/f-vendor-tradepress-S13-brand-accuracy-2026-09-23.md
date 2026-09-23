# Vendor pages and trade press naming brand accuracy in AI answers — Reputation (press), Yext sitemap check, Search Engine Journal (3 articles), Make job posting wording; pointers to already-pulled vendor raws

```yaml
source:          Reputation.com (press page, sitemap); Yext (sitemap); Search Engine Journal (WP REST search + 3 articles); Digiday (site search); Search Engine Land (403); Birdeye (sitemap); Profound (sitemap)
url_or_doc_id:   https://reputation.com/resources/press/reputation-launches-ai-platform-that-puts-enterprise-brands-in-control-of-ai-search-representation ; https://reputation.com/sitemap.xml ; https://www.yext.com/sitemap1.xml ; https://www.searchenginejournal.com/wp-json/wp/v2/posts?search=brand%20accuracy%20AI&per_page=10 ; https://www.searchenginejournal.com/biggest-ai-search-risk-is-conflicting-information/586904/ ; https://www.searchenginejournal.com/when-ai-has-nothing-on-your-company-it-describes-someone-else/587876/ ; https://www.searchenginejournal.com/google-ai-mode-prices-differ-from-product-carousel-for-same-items/588227/ ; https://digiday.com/?s=AI+Overviews+brand+inaccurate ; https://searchengineland.com/?s=hallucination+brand ; https://birdeye.com/sitemap.xml ; https://www.tryprofound.com/sitemap.xml
published:       SEJ articles 2026-09-03 (two) and 2026-09-07; Reputation press page undated on the captured text
pull_date:       2026-09-23
pull_method:     fetch (curl)
pull_purpose:    evidence about category noise (vendor and trade-press framing of brand accuracy) — tier 6 rows; and evidence about a number for the Productrise figures relayed by SEJ (tier 5, vendor study relayed)
tier:            6
tier_reason:     vendor press page and practitioner trade press without n (table default 6); the SEJ price-mismatch article relays a vendor tracking study with n and dates — that row tier 5; the SEJ read counts are the site's own display
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Google AI Overviews, AI Mode, Claude (as named)
metric_kind:     none
supersedes:      none
captured:        page excerpts and sitemap URL lists; SEJ search result list
```

## Reputation.com — press page title and platform wording (verbatim excerpts)

> Reputation Launches AI Platform That Puts Enterprise Brands in Control of AI Search Representation
> GEO READINESS REPORT — Can AI Find and Trust Your Brand? See what AI can find, understand, and trust about your brand. Know where your locations show up, where they fall short, and what to improve next. Get Your Free Report
> Listings — Keep every location accurate, visible, and ready to be found.

Sitemap URLs matching ai-search|llm|chatgpt|generative (12 of the sitemap's entries):
```
/resources/articles/geo-ai-search-and-what-really-drives-visibility
/resources/articles/how-consumers-are-using-ai-search-and-how-the-path-to-purchase-is-changing
/resources/articles/how-googles-search-generative-experience-affects-google-business-profiles
/resources/articles/mastering-geo-for-multi-location-brands-the-new-era-of-generative-engine-optimization
/resources/articles/read-between-the-stars-using-reputation-metrics-to-improve-cx-and-win-in-ai-search
/resources/articles/tracking-your-brands-presence-across-major-llms
/resources/articles/why-review-volume-is-the-new-authority-signal-in-chatgpt-gemini-and-perplexity
/resources/articles/will-google-hit-its-stride-with-generative-ai
/resources/press/from-search-rankings-to-ai-answers-reputation-marks-20-years-by-defining-how-brands-build-trust-get-found-and-drive-revenue-in-the-ai-era
/resources/press/reputation-launches-ai-platform-that-puts-enterprise-brands-in-control-of-ai-search-representation
/resources/press/reputation-launches-geo-readiness-audit-to-help-brands-measure-and-improve-visibility-in-ai-search
/events/from-search-rankings-to-ai-answers
```

## Yext — sitemap1.xml pattern check

URLs matching accura|hallucin|misinform|ai-reputation|brand-accuracy|scout: `/ja/about/news-media/yext-commitment-customers-deliver-accurate-information-covid-19`, `/about/news-media/yext-acquires-places-scout`, `/ja/industries/government/provide-the-public-with-accurate-information`, `/de/scout`, `/fr/scout`, `/it/scout` (and further `scout` locale paths). No page slug names AI-answer accuracy or AI reputation.

## Search Engine Journal — WP REST search "brand accuracy AI", 10 newest (date | title | URL)

```
2026-09-22 | 3 Steps To Win B2B Brand Consideration, Day Zero Decides The Shortlist | /b2b-brand-consideration-day-zero-decides-the-shortlist/588593/
2026-09-21 | How To Build Local Pages AI Systems Can Find And Trust | /how-to-build-local-pages-ai-systems-can-find-and-trust/588097/
2026-09-18 | The State Of Search In An AI World: What Marketing Leaders Need To Know Now | /state-of-search-2027-what-to-stop-measure-fund/589617/
2026-09-17 | Does My Product Page Copy Still Matter If Agents Read Feeds And Schema? – Ask An SEO | /ask-an-seo-does-product-page-copy-matter-since-agents-read-feeds/585090/
2026-09-16 | How To Detect Affiliate Brand Bidding And Hidden Revenue Leakage | /how-to-detect-affiliate-brand-bidding-and-hidden-revenue-leakage-spa/589274/
2026-09-10 | Google Launches Meridian GeoX Globally | /google-launches-meridian-geox-globally/589030/
2026-09-07 | Your Biggest AI Search Risk Is Conflicting Information About Your Brand | /biggest-ai-search-risk-is-conflicting-information/586904/
2026-09-03 | When AI Has Nothing On Your Company, It Describes Someone Else | /when-ai-has-nothing-on-your-company-it-describes-someone-else/587876/
2026-09-03 | Google AI Mode Prices Differ From Product Carousel For Same Items | /google-ai-mode-prices-differ-from-product-carousel-for-same-items/588227/
2026-08-26 | AI Brand Preference Now Splits By Generation, Claude Leads Gen Z More Than 7-To-1 | /ai-brand-preference-now-splits-by-generation-claude-leads-gen-z-more-than-7-to-1/586624
```

### SEJ, "Your Biggest AI Search Risk Is Conflicting Information About Your Brand" — Carolyn Shelby (Principal Consultant, CSHEL Search Strategies), published 2026-09-07T12:00:11+00:00, page shows "3.5K READS"

> Conflicting brand information can cause AI systems to retrieve outdated facts. Learn how to trace and correct the evidence chain.
> In many cases where the information about a brand is outdated or wrong, the problem is not a lack of data. The problem is too much data. The problem is that the brand already has too many versions of the truth, and the version that best matches the user's question isn't current.
> The website says one thing. An old PDF says another. Product documentation uses language the marketing team abandoned two years ago. Executive biographies preserve titles that no longer exist. Partner pages describe features that have changed. …
> Traditional search could rank several of those pages simultaneously and leave the user to decide which one was current. But now, AI search products retrieve sources and use them to construct a single answer. The answer is going to look settled even when the underlying evidence is not.
> So, this is not merely a content problem. It is a retrieval and content governance problem, and AI search has made it an SEO problem, too.

[note: no brand named; no n.]

### SEJ, "When AI Has Nothing On Your Company, It Describes Someone Else" — Duane Forrester (Founder and CEO, UnboundAnswers.com), published 2026-09-03T14:30:00+00:00, page shows "860 READS"

> The substitution arrives at full confidence, it happens in a place you do not own, and no content audit you run will ever find it.
> …the model is still telling people something about your company that no page of yours supports and no page of yours could have prevented.
> Separate this from hallucination as the term is normally used, because the industry has flattened the two and the flattening costs you the diagnosis. …
> There is a vendor article circulating right now about AI hallucinating product details, aimed at brand teams, warning them that models invent claims about their products. It is competent writing on a real problem. It opens its argument with a direct quotation attributed to Percy Liang, named correctly as director of Stanford's Center for Research on Foundation Models, on how models confabulate in commercial contexts. I cannot find that quotation anywhere else.

[note: no brand named; cites Mallen et al. and Longpre et al. (EMNLP 2021) for the mechanism; no n of its own.]

### SEJ, "Google AI Mode Prices Differ From Product Carousel For Same Items" — SEJ staff (Matt G. Southern), published 2026-09-03 (page), relaying a Productrise tracking study

> Productrise monitored over 2 million product listings across more than 100,000 regular search results and AI Mode responses from August 9 to August 31, 2026. It conducted the same product-specific searches in AI Mode and regular search on the same day, in the US and UK.
> 28% of products in the carousel also appeared in AI Mode for the same search on the same day.
> The figures from the company's tracking database, which Google told Futurism it hasn't verified, show that a carousel spot rarely carried over to AI Mode in this data, even for the same product on the same day.
> When both AI Mode and the Popular products carousel showed results for the same query, the carousel displayed an average of 27… [sentence truncated in extraction]

[note: relayed vendor study (Productrise) with n, dates and markets stated — tier 5 for this row; the price-difference figure itself was not captured in the extracted sentences.]

## Make (make.com) job posting wording naming correctness — cross-reference

`docs/raw/f-linkedin-S1-eu-countries-2026-09-23.md`, job 4441092689 "Senior GEO Manager - LLM Search Optimization" (Madrid): "build and run Make's approach to being cited (correctly, favorably, and often) across ChatGPT, Perplexity, Google AI Overviews, and Claude" and "Authority & source repair — identify and close the gaps in the sources LLMs actually draw from".

## Already-pulled vendor raws carrying accuracy wording (pointers, not re-pulled)

- `docs/raw/a-birdeye-search-ai-product-2026-09-22.md`: "Citations, accuracy, and website signals — the exact causes behind every score"; "Fixes the listing — Summons the Listings Optimization Agent to correct the inaccurate field."
- `docs/raw/a-brandlight-method-2026-09-22.md`: "Enhanced accuracy and consistency of brand representation."; Brandlight "Direct Bias Score" per `docs/competitors/INDEX.md` row 31.
- `docs/raw/e-case-practitioner-hackernews-bando-geo-experiment-2026-09-22.md` line 50: "Brand Accuracy Score (BAS): how closely AI descriptions match…" (practitioner experiment, graded "Fools gold").
- Seer Interactive "brand-accuracy tracking" is named in `docs/competitors/INDEX.md` row 48; the phrase was not found by grep in `docs/raw/f-seer-interactive-service-2026-09-22.md` or `f-agency-census-c5-2026-09-22.md` on 2026-09-23 — the profile's source line should be re-checked before the phrase is cited again.

## Other channels tried

| Channel | HTTP | Result |
|---|---|---|
| searchengineland.com/?s=hallucination+brand and /wp-json/wp/v2/posts?search= | 403 / 403 | walled |
| digiday.com/?s=AI+Overviews+brand+inaccurate | 200 (54 KB) | no article headings parsed (nav only) |
| birdeye.com/sitemap.xml | 200 (1.68 MB) | no URL matching ai-reputation / ai-answers / llm patterns |
| tryprofound.com/sitemap.xml | 200 | AI-search articles only; none on accuracy or hallucination by slug |

## Pull notes — mechanical only

- SEJ article author fields were not exposed by the `rel="author"` pattern; names taken from the article byline text. "READS" figures are the site's own counters at pull time.
- Reputation.com press page returned the site's navigation and product blurbs in the extracted text; the press-release body below the title was not isolated (page is 202 KB with heavy templating).

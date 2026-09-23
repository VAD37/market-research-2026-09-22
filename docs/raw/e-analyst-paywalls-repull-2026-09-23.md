# Analyst paywalls — eMarketer, Gartner, Forrester, Statista: what shows without login

```yaml
source:          EMARKETER (emarketer.com); Gartner, Inc. (gartner.com); Forrester Research, Inc. (forrester.com); Statista (statista.com)
url_or_doc_id:   https://www.emarketer.com/search/?q=generative%20engine%20optimization ; https://www.gartner.com/en/search?keywords=generative%20engine%20optimization ; https://www.forrester.com/search?tmtxt=answer%20engine%20optimization ; https://www.forrester.com/blogs/aeo-will-be-won-with-solutions-that-provide-intelligence-orchestration-and-outcomes/ ; https://www.forrester.com/report/best-practices-for-answer-engine-optimization-aeo/RES188745 ; https://www.statista.com/search/?q=generative+engine+optimization ; https://www.statista.com/topics/10825/ai-powered-online-search/
published:       per item below (Gartner results Dec 2025 – Aug 2026; Forrester blog 2026-09-02; Forrester report 2025-11-12; Statista topic 2025-12-17)
pull_date:       2026-09-23
pull_method:     browser (Chrome extension) — logged out; WebSearch (allowed_domains forrester.com, statista.com) to locate pages when on-site search failed; browser (Playwright MCP) and fetch for the eMarketer DNS check
pull_purpose:    evidence about a number
tier:            6
tier_reason:     teaser text and an analyst blog with no n or method; report bodies not read. No sub-market size found on any page
source_label:    analyst-derived
lane:            E
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none — 2026-09-22 row: "emarketer.com (subscription-gated)"; Gartner, Forrester, Statista sizes not reached
captured:        search-result titles, types and dates; teaser lines; purchase or login gate text; one blog paragraph (first two sentences)
verbatim:        partial
```

## Verbatim — eMarketer

Chrome: "This site can’t be reached | www.emarketer.com’s server IP address could not be found. | ERR_NAME_NOT_RESOLVED". Playwright: "net::ERR_NAME_NOT_RESOLVED". Local nslookup timed out; curl https://emarketer.com/ returned 000. Nothing retrieved.

## Verbatim — Gartner (search "generative engine optimization")

| Title | Type and date as printed |
|---|---|
| Integrate AEO and SEO: Improve Online Search and Answer Engine Visibility | Webinar On-Demand |
| How CMOs Secure Executive Buy-In for Answer Engine Optimization | Research Aug 2026 |
| Answer Engine Optimization: HubSpot’s Move Is a Strategic Signal for Tech CEOs | Premium Research Apr 2026 |
| Adjust PR Strategy for Answer Engine Optimization | Research Dec 2025 |
| Brand as a Growth Engine | Webinar On-Demand |
| Accelerator for Building an Account Growth Engine | Premium Research Aug 2026 |
| Using Answer Engines to Drive the Customer Journey | Webinar On-Demand |
| How to Capture Customer Attention in the Age of AEO | Premium Research Jul 2026 |

Teaser fragments: "Access Insights Already a Gartner client?"; "CMOs face significant challenges in conveying the business impact of AEO to C-suite leadership."; "Tech CEOs must prioritize automating answer engine optimization monitoring and actioning to avoid revenue stalls and market share loss." [note: teasers truncated by the page]

Size figure for the category on the page: none. Site navigation carries "Competing in the $1T AI market" (not category-specific).

## Verbatim — Forrester

- On-site search https://www.forrester.com/search?tmtxt=answer%20engine%20optimization: "This page isn’t working | HTTP ERROR 406" (twice). Homepage loads.
- Blog, "AEO Will Be Won With Solutions That Provide Intelligence, Orchestration, And Outcomes", "Nikhil Lai, Principal Analyst | SEP 2 2026":

  > The market for AEO technologies is booming. Adobe’s acquisition of Semrush for about $1.9 billion, Sitecore’s acquisition of Scrunch for around $225 million, and Profound’s $1 billion-plus valuation punctuate the market’s dynamism and category-breaking momentum.

  [note: remainder paraphrased, not reproduced — the post says adjacent vendor types are entering AEO, cautions that vendor proliferation is not maturity, states that no AEO technology can yet deterministically tie visibility or sentiment changes to business outcomes, and announces "The Answer Engine Optimization Technologies Landscape, Q3 2026"]
- Report page RES188745: "Best Practices For Answer Engine Optimization (AEO) | Nikhil Lai, | Nov 12, 2025 | Summary | Client log in | Become a client" · "This report is available for individual purchase ($1495)." Body not shown.
- Other titles returned by WebSearch on forrester.com, not opened: "Assess Your Answer Engine Optimization (AEO) Maturity" (RES193785); "Answer Engine Optimization (AEO) Role Connections Tool" (RES189795); blogs "Answer Engines’ Next Act: From Visibility To Growth", "How To Master Answer Engine Optimization", "Seven Roles, One Goal: How To Organize For Answer Engine Optimization".

## Verbatim — Statista

- https://www.statista.com/search/?q=generative+engine+optimization: page title "Page not found | Statista".
- Topic page "AI-powered online search - statistics & facts": "Published by Statista Research Department, Dec 17, 2025". Chart titles listed include "Referral share of search engines monthly worldwide 2015-2026", "Generative AI market size worldwide 2019-2032", "Worldwide generative AI revenue 2020-2032", "Leading AI applications worldwide 2026, by MAU", "ChatGPT and Gemini app downloads worldwide monthly 2023-2026". No GEO, AEO or AI-visibility sub-market size listed. "Log in" shown; chart values not read.
- WebSearch (statista.com) for "generative engine optimization market size" returned generative-AI market forecast pages only; no GEO/AEO page.

## Pull notes — mechanical only

- No login, no trial, no purchase. Forrester's $1,495 individual purchase and Gartner client access are recorded as the gates.
- eMarketer failed at DNS on both browsers and on fetch on 2026-09-23 — a network-path failure, not a paywall reading.

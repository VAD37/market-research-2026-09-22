# Blocked channels — credential register and probe log

Date 2026-09-23. Task R-BLOCKED. Owner-facing register of channels that need a credential, plus the probe log for every channel `findings/unknowns.md` §Unknowns and `customers/high-cpa-regulated.md` recorded as blocked on 2026-09-22. Probed through the Chrome extension first, Playwright MCP where the extension refused, fetch where that was enough. No login was attempted, no account created, no credential or payment entered, no CAPTCHA or human-verification check started, no form submitted. Cloudflare interstitials that cleared on their own without interaction count as reached.

Result codes: **reached** — content read; **still blocked** — bot wall, CAPTCHA, WAF, DNS or domain refusal; **needs registration** — a login or account wall is the only path; **needs payment** — content behind a subscription, trial or purchase.

## Probe log

| channel | URL probed | needed for (task / signal / hypothesis) | block on 2026-09-22 | browser result 2026-09-23 | credential that would unblock | raw file if pulled |
|---|---|---|---|---|---|---|
| sec.gov Archives | `sec.gov/Archives/edgar/data/1625278/000162527826000012/earningsreleaseq4fy25.htm` | P4 C3 NerdWallet negative case; S7; H11 | 403, then 503 | reached (fetch 200 too) | none | `e-nerdwallet-8k-repull-2026-09-23.md` |
| efts.sec.gov full-text | `efts.sec.gov/LATEST/search-index?q=…&forms=10-K,10-Q,8-K` | S7; Lane A/E filings; H16 | 403; FTS 500 | reached — 24 / 23 / 8 / 2 hits | none | `e-edgar-fulltext-repull-2026-09-23.md` |
| data.sec.gov | `data.sec.gov/submissions/CIK0001625278.json` | filer metadata | 403 | reached (fetch 200), probe only | none | — |
| reddit.com | `reddit.com/search.json`, `/r/SEO/search`, `old.reddit.com/r/SEO/search` | P4-r negatives; S5; H3, H6 | 403 ×5 methods | still blocked — extension "not allowed due to safety restrictions"; Playwright "blocked by network security"; old.reddit redirects to `/login`; WebSearch refuses the domain; fetch 403 | Reddit account (untested; extension block would remain) | — |
| g2.com | `categories/answer-engine-optimization-aeo`, `ai-search-visibility-optimization-tools`, 5 product review pages | S4; Lane A roster ceiling | 403 / DataDome | reached — 3 category pages, 4 vendor panels; slider CAPTCHA on 8th load, stopped | none for what was read; velocity histogram needs ~113 loads per vendor | `f-g2-capterra-S4-repull-2026-09-23.md` |
| capterra.com | `capterra.com/ai-search-visibility-software/` p1, p9 | S4 | 403 | reached | none | `f-g2-capterra-S4-repull-2026-09-23.md` |
| indeed.com | `indeed.com/jobs?q="generative engine optimization"` | S1 SMB / mid-market | 403 | still blocked — Cloudflare "Additional Verification Required" | none known; employer account untested | `f-jobs-upwork-indeed-freelancer-S1-repull-2026-09-23.md` (probe) |
| upwork.com | `upwork.com/nx/search/jobs/?q=…` ×3 | S1 SMB / mid-market | Cloudflare / 403 | reached — facet counts, 20 tiles | client size and spend need a logged-in freelancer or client view | `f-jobs-upwork-indeed-freelancer-S1-repull-2026-09-23.md` |
| freelancer.com | `/jobs/?keyword=…`, `/search/projects?q=…` | S1 | JS shell | reached — keyword not applied by URL; form not submitted | none; needs on-page search form | same file (probe) |
| trends.google.com | `trends/explore?geo=US&q=…` ×3 | S9 all three verticals; H7 | JS shell, token-gated API | reached — 3 × 53 weekly points | none | `f-google-trends-S9-repull-2026-09-23.md` |
| crunchbase.com | `organization/{athenahq,peec-ai,scrunch-ai}` | AthenaHQ, Peec, Scrunch funding; Lane A | 403 | needs payment — header read, funding fields "obfuscation" | Crunchbase Pro | `a-funding-crunchbase-pitchbook-repull-2026-09-23.md` |
| pitchbook.com | `profiles/company/{759029-50,741876-13,633268-54,708134-32}` | same | 403 | reached — free preview; full history needs access | PitchBook platform (full history only) | `a-funding-crunchbase-pitchbook-repull-2026-09-23.md` |
| bloomberg.com | `news/articles/2026-06-03/sitecore-said-to-acquire-scrunch-for-225-million` | Scrunch/Sitecore deal value | 403 | reached — headline and 2 paragraphs; rest paywalled | Bloomberg subscription (body only) | `a-bloomberg-scrunch-sitecore-repull-2026-09-23.md` |
| emarketer.com | `emarketer.com/search/?q=…` | Lane E sub-market size; H16 | subscription-gated | still blocked — DNS ERR_NAME_NOT_RESOLVED on extension, Playwright and fetch | EMARKETER subscription (after DNS path works) | `e-analyst-paywalls-repull-2026-09-23.md` (probe) |
| gartner.com | `gartner.com/en/search?keywords=…` | Lane E size; H16 | not reached | needs payment — titles read; "Already a Gartner client?" | Gartner client seat | `e-analyst-paywalls-repull-2026-09-23.md` |
| forrester.com | `/search?tmtxt=…`; `/report/…/RES188745`; one blog | Lane E size; H16 | not reached | needs payment — "individual purchase ($1495)"; on-site search HTTP 406 | Forrester client seat or per-report purchase | `e-analyst-paywalls-repull-2026-09-23.md` |
| statista.com | `/search/?q=…`; `/topics/10825/ai-powered-online-search/` | Lane E size; H16 | not reached | reached — search 404; topic lists no GEO/AEO size; chart values behind "Log in", not tested | Statista account (untested) | `e-analyst-paywalls-repull-2026-09-23.md` |
| bing.com/webmasters | `help/webmaster-guidelines-30fba23a` | Lane D countermeasure; H13 | JS shell | reached | none | `d-bing-webmaster-guidelines-repull-2026-09-23.md` |
| learn.microsoft.com | not re-probed | Lane D policy | 404 on an unrecorded URL | not probed — source URL not recorded on 2026-09-22 | none known | — |
| amazon.com guidelines | `gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF` | Lane D; H13 | 503 | reached | none | `d-amazon-community-guidelines-repull-2026-09-23.md` |
| arxiv.org | `arxiv.org/abs/2609.06811` | Lane D; H5, H15 | scratch file lost | reached (fetch 200) | none | `d-arxiv-2609-06811-repull-2026-09-23.md` |
| searchengineland.com | `guide/enterprise-ecommerce-llm-visibility-case-study` | P4 case hunt | "gated stub" | reached — full guide, no wall | none | `e-searchengineland-home-depot-guide-repull-2026-09-23.md` |
| sam.gov | `sam.gov/search/?index=opp…keywordRadio=EXACT…` | S10 | API 200, no match | reached — "No matches found" (active) | none | `f-procurement-S10-repull-2026-09-23.md` |
| contractsfinder | `Search/Results?keywords=…` | S10 | keyword filter non-functional | reached — URL keyword not applied; form not submitted | none; needs on-page form | `f-procurement-S10-repull-2026-09-23.md` |
| ted.europa.eu | `en/search/result?FT=…` | S10 | 405 | still blocked — "Human Verification" | none known | `f-procurement-S10-repull-2026-09-23.md` (probe) |
| courtlistener.com | `/?q=…`; `api/rest/v4/search/?q=…` | Lane B/E dockets | WAF challenge | reached (fetch) — "0 Results"; API `"count":0`; probe only | API token for authenticated search (untested) | — |
| html.duckduckgo.com | `html/?q=generative+engine+optimization` | P4 search path | 403 / rate-limited | reached (fetch 200, 10 results), probe only | none | — |
| trustradius.com | `categories/generative-engine-optimization` | S4 | not reached | reached — 404 on guessed category URL | none | — |
| perplexity.ai/hub | `hub/legal/merchant-terms` | Lane C merchant terms | 404 | still blocked — fetch 403; browser not tried | none known | — |
| shopify.dev | `docs/agents` | Lane C UCP trust tiers | 404 | reached (fetch 200), probe only; trust-tier content not read | Shopify Partner account per 2026-09-22 row (not re-tested) | — |
| chatgpt.com, perplexity.ai, google.com/search consumer surfaces | not probed | Pass 10 panel | extension denied / Cloudflare / reCAPTCHA | not probed — Pass 10 skipped by user 2026-09-23 | — | — |

Tally, 31 rows: reached 21; still blocked 5 (reddit.com, indeed.com, emarketer.com, ted.europa.eu, perplexity.ai/hub); needs registration 0; needs payment 3 (crunchbase.com, gartner.com, forrester.com); not probed 2 (learn.microsoft.com, consumer surfaces). G2 counts as reached with a CAPTCHA ceiling; PitchBook and Bloomberg as reached with the remainder behind payment.

## Not pulled, with reason

- Reddit threads (P4-r item 4): every path refused; no title, date or vote count captured.
- G2 review velocity by month: CAPTCHA after 8 loads; only the first "Most Recent" page per vendor was read.
- Indeed postings; Freelancer and Contracts Finder keyword results (form submission out of scope); TED results.
- Crunchbase funding amounts; Profound Crunchbase slug unresolved.
- Analyst report bodies and any sub-market size (Gartner, Forrester, Statista, eMarketer).

## For the owner

- **Crunchbase Pro** — would unlock round amounts, dates and investors for AthenaHQ, Peec AI and Scrunch, and the Sitecore/Scrunch deal fields; PitchBook's free view already shows AthenaHQ $2.1M, Peec seed $8.08M, Profound Series D $180M.
- **PitchBook platform access** — would unlock the missing round amounts (Peec Series A and 2026-06-25 round, Profound Seed–Series C) and Scrunch buyout value.
- **Gartner client seat** — would unlock the report bodies behind 8 AEO/GEO titles (Dec 2025 – Aug 2026); whether any carries a sub-market size is unknown.
- **Forrester per-report purchase ($1,495) or client seat** — would unlock "Best Practices For AEO" and "The AEO Technologies Landscape, Q3 2026", the likeliest analyst vendor count.
- **Bloomberg subscription** — would unlock the Sitecore/Scrunch article body; the $225M figure is already visible.
- **EMARKETER subscription** — only after the DNS failure on this network path is resolved; would unlock any AI-search sub-market forecast.
- **Statista account** — untested; would show chart values on the AI-powered-search topic page; no GEO/AEO size page was listed.
- **Reddit** — no credential known to work: the Chrome extension refuses the domain on safety grounds. A human browsing session would be needed for S5 threads and advertiser-reported ChatGPT-ads results.
- **Indeed and TED** — bot walls, not accounts; a human browser session would clear them.

## Caveats

- One date, one network path (IP 159.26.119.97 per Upwork's interstitial). Bot-wall outcomes vary by IP and load count; a "still blocked" row is a 2026-09-23 reading, not permanent.
- G2 counts are G2's own review counts; the verification method is G2's.
- Playwright was used only for reddit.com and the eMarketer DNS check, in its own tab; P12-ads held `pw` in parallel.
- No verdict is drawn here; the raw files carry the evidence.

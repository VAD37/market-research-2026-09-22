# Aggregator baselines — PayScale and Salary.com, conventional SEO/content/digital-marketing roles

```yaml
source:          PayScale (crowdsourced compensation database); Salary.com (CompAnalyst compensation database)
url_or_doc_id:   https://www.payscale.com/research/US/Job=Search_Engine_Optimization_(SEO)_Specialist/Salary ; https://www.payscale.com/research/US/Job=Search_Engine_Optimization_(SEO)_Manager/Salary ; https://www.payscale.com/research/US/Job=Content_Marketing_Manager/Salary ; https://www.payscale.com/research/US/Job=Digital_Marketing_Manager/Salary ; https://www.salary.com/research/salary/benchmark/search-engine-optimization-specialist-i-salary
published:       PayScale pages self-date per role (see below, all 2026); Salary.com page dated 2026-09-01 on page
pull_date:       2026-09-23
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     PayScale states sample size (n profiles) and last-updated date per role but does not publish its aggregation/weighting method on these pages — hidden method would drop a panel source from tier 4 to tier 5 per trust-rubric; Salary.com shows a percentile table with no n or method disclosed on the page pulled — kept at 5 (compensation-database vendor product, not a blog) rather than 6, bias flagged
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation (SEO rows); n/a (Content/Digital Marketing Manager rows)
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        section — salary figures only, extracted via WebFetch prompt
```

## Verbatim

### PayScale — SEO Specialist
- Average base salary: "$59,179 / year"
- Range (10th–90th percentile): $44k–$80k
- Sample size: "Based on 444 salary profiles"
- Last updated: "May 21 2026"

### PayScale — SEO Manager
- Average base salary: "$81,910 / year"
- Range (10th–90th percentile): $56k–$116k
- Sample size: "Based on 389 salary profiles"
- Last updated: "Feb 28 2026"

### PayScale — Content Marketing Manager
- Average base salary: "$82,653 / year"
- Range (10th–90th percentile): $55k–$114k
- Sample size: "Based on 836 salary profiles"
- Last updated: "Jun 24 2026"

### PayScale — Digital Marketing Manager
- Average base salary: "$77,947 / year"
- Range (10th–90th percentile): $53k–$112k
- Sample size: "Based on 2,895 salary profiles"
- Last updated: "Jul 01 2026"

### Salary.com — Search Engine Optimization Specialist I
- Date on page: September 01, 2026
- Median: $80,467/year ($39/hour)
- 25th–75th percentile: $73,543–$92,043
- 10th percentile (entry-level): $67,239; 90th percentile (top earners): $102,582
- Top-earning metro locations shown: San Jose, CA $101,493; San Francisco, CA $100,382; Oakland, CA $98,266
- [note: Salary.com's "Content Marketing Manager" benchmark page (salary.com/research/salary/benchmark/content-marketing-manager-salary) returned HTTP 404 to WebFetch on 2026-09-23 — not pulled.]

### Checked and absent — no GEO/AEO page found
- PayScale: web search for a PayScale page matching "Generative Engine Optimization," "Answer Engine Optimization," "GEO Specialist," or "AEO" returned no PayScale result — checked 2026-09-23, absent.
- Salary.com: web search `site:salary.com` for the same terms returned no Salary.com result — checked 2026-09-23, absent.
- Built In: web search `site:builtin.com` for "generative engine optimization" / "answer engine optimization" + "salary" returned only individual job postings (captured separately in the company-postings pull), not a Built In salary-benchmark page — checked 2026-09-23, absent as a benchmark product.
- Levels.fyi: web search for GEO/AEO salary data returned only unrelated hits (software-engineer levels at companies literally named "Geo," e.g. "The GEO Group") — no marketing-role GEO/AEO benchmark exists on Levels.fyi — checked 2026-09-23, absent.

## Pull notes — mechanical only

- ZipRecruiter (ziprecruiter.com/Jobs/Geo-Generative-Engine-Optimization) and Glassdoor (glassdoor.com/Job/geo-and-ai-search-specialist-jobs-SRCH_KO0,28.htm) both refused every access path tried: WebFetch → HTTP 403 on both; curl with a browser user-agent → HTTP 403 on both (empty body from ZipRecruiter, a Glassdoor "Security | Glassdoor" interstitial page, 543 lines, from Glassdoor); Playwright MCP browser navigation → ZipRecruiter served a Cloudflare "Performing security verification" interstitial (Ray ID a3fad04e8ff6cba0), Glassdoor served an equivalent "Just a moment..." Cloudflare challenge page. No verification/CAPTCHA step was attempted on either, per task rules. Both recorded as still blocked, not pulled — the site-reported salary figures for these two ("$18–$34/hr" ZipRecruiter GEO range, "$59.65/hr" ZipRecruiter AEO average, Glassdoor "193 Geo and ai search specialist jobs") seen only in third-party WebSearch snippets are NOT captured here as they were never independently verified against the primary page.

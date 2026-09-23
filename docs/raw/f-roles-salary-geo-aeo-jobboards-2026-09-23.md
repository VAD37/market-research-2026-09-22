# GEO/AEO-specific job-board aggregators — AEO Jobs, Hire Lanz, StackMatix

```yaml
source:          AEO Jobs (aeojobs.ai, job board); Hire Lanz (hirelanz.com, blog); StackMatix (stackmatix.com, blog)
url_or_doc_id:   https://aeojobs.ai/jobs/generative-engine-optimization ; https://hirelanz.com/geo-specialist-jobs/ ; https://www.stackmatix.com/blog/aeo-marketing-jobs
published:       undated on all three pages
pull_date:       2026-09-23
pull_method:     fetch (WebFetch)
pull_purpose:    AEO Jobs row — evidence about a number (small n, flagged); Hire Lanz and StackMatix rows — evidence about category noise only, per trust-rubric tier-6 rule
tier:            5 (AEO Jobs — n disclosed, small-sample flagged); 6 (Hire Lanz, StackMatix — no n, no disclosed method beyond a source list; vendor/listicle blog)
tier_reason:     AEO Jobs discloses n=11 on-page, kept at 5 rather than 4 because sampling/weighting method is not published; Hire Lanz and StackMatix show dollar ranges with no n and no stated calculation method — trust-rubric tier 6 ("vendor blog, no n" — "marketing, not a source"), pulled only as evidence of what figures are circulating in the category, never cited as a number
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        section — salary text only, via WebFetch prompt
```

## Verbatim

### AEO Jobs (aeojobs.ai) — Generative Engine Optimization jobs
- Sample: "11 jobs with salary data."
- Average range: "$87.7–111.6K per year on average."
- Mid-level: "$70.3–79.6K" annually. Senior: "$98.4–130.9K" annually.
- "The middle 50% of advertised salaries fall between $71K and $138.7K."
- Date: none stated on page; individual postings dated "1 wk. ago" to "5 mo. ago" relative to the 2026-09-23 pull.
- [Separately, per earlier WebSearch snippet of this same site (not independently re-verified against page text in this pull): "5 Jobs on AEO Jobs with salary data" giving GEO roles overall "$80K–$94.2K per year," and "3 Jobs" giving senior GEO roles "$86.6K–$99.4K per year" — these n=5/n=3 figures are a different cut of the same small underlying dataset and are recorded here as seen, not independently re-confirmed.]

### Hire Lanz (hirelanz.com) — "GEO Specialist Jobs 2026: Salary, Skills & Real Demand" — tier 6, category-noise evidence only
- Entry/Associate: $50,000–$70,000 ("1–2 years of SEO experience, content writing, basic analytics")
- Mid-Level Specialist: $70,000–$110,000 ("3–5 years of SEO, schema markup, GA4, Search Console, technical SEO")
- Senior Specialist: $87,000–$100,000 ("5+ years, multi-platform AI visibility tracking, advanced content strategy")
- Manager/Director: $110,000–$171,000+ ("Team leadership, enterprise SEO strategy, cross-functional collaboration")
- Contract/Freelance: $65–$75/hour ("GEO audits, reporting, AI citation tracking, client communication")
- Named examples cited on page: San Rafael hybrid role $110,000–$143,000; Citizens Bank (Answer Engine Optimization Manager, Westwood/Pittsburgh/NY/Boston) "$131,000 to $171,000 plus discretionary annual bonus"; Texas contract-to-hire $65–$75/hour; "AEO Jobs aggregate data: $80,000–$94,000 average; senior roles $87,000–$99,000" (same AEO Jobs figures as above, restated).
- Method as stated on page: "Data compiled from AEO Jobs, ZipRecruiter, Jobright, LHH, and published enterprise postings, mid-2026." No sample size or geographic breakdown given beyond the regional examples named.

### StackMatix (stackmatix.com) — "Answer Engine Optimization Jobs: AEO Career Paths, Salaries & Skills (2026)" — tier 6, category-noise evidence only
- AEO Specialist: $60,000–$85,000 ("2–4 years SEO + AI knowledge")
- AEO Manager: $85,000–$120,000 ("4–6 years + strategy experience"); contract example cited from Onward Search: "$48–52/hour (W-2 basis), translating to approximately $100,000+"
- Senior Manager: $120,000–$150,000 ("6–8 years + team leadership")
- Director: $140,000–$200,000+ ("8+ years + executive communication")
- Company-specific postings cited: Experian (AEO & SEO Manager) "$100K–$174K for remote B2B positions"; Odoo (Growth Marketing Specialist – GEO/AEO) "$75K–$95K"; SEOJobs.com (Director of SEO & AI Search) "approximately $85,000 base plus bonus"; Senior Content Marketing Manager (AI-focused) "$150,000–$210,000 at enterprise companies."
- Role definition given on page: "Lead research, strategy development, and execution of AEO initiatives while driving brand visibility across generative AI platforms through on-page and off-page optimization strategies."
- No sample size, geographic distribution, or methodology documentation given on page.

## Pull notes — mechanical only

- All three pulled via WebFetch. No raw HTML retained.
- Note the same underlying named postings (Citizens Bank, Odoo, Experian) recur across Hire Lanz, StackMatix, and the recruiter/staffing file (f-roles-salary-recruiter-staffing-2026-09-23.md) and the Fortune-500 file — these blogs are visibly re-citing the same small pool of live job postings rather than independent samples; recorded side by side per source, not merged or averaged.

# Company-stated compensation — individual GEO/AEO/SEO job postings (Built In)

```yaml
source:          Built In (job board — postings reproduce the employer's own stated compensation and role text)
url_or_doc_id:   https://builtin.com/job/associate-director-seo-generative-engine-optimization/7752860 ; https://builtin.com/job/generative-engine-optimization-specialist/6957851
published:       postings undated on the fetched excerpt (live at pull time)
pull_date:       2026-09-23
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number (first posting); evidence about role expectations only, no number (second posting)
tier:            3
tier_reason:     platform primary — the number is the hiring employer's own stated compensation range, reproduced by Built In as job-board host; reliable on existence of the figure, no independent verification of whether the role was ultimately filled at that band
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        section — job posting compensation, location, and responsibilities text, via WebFetch prompt
```

## Verbatim

### OneMain Financial — "Associate Director of SEO & Generative Engine Optimization"
- Compensation: "Target base salary range of $140-170k, plus competitive performance-based compensation."
- Location: New York, NY, USA (in-office).
- Responsibilities as posted:
  - "Own and evolve the enterprise SEO and GEO roadmap, aligning with business goals and the changing AI-driven search ecosystem"
  - "Develop ranking strategies for both traditional and generative search interfaces"
  - "Drive entity-based SEO, structured data expansion, and E-E-A-T optimization for brand authority"
  - "Identify and pilot AI-driven SEO workflows including content augmentation and automation"
  - "Partner with Product and Engineering leadership to influence roadmap priorities and advocate for SEO needs"
  - "Oversee technical SEO audits and prioritize fixes with engineering teams"
  - "Guide content operations including editorial planning and optimization for both traditional and generative SEO"
  - "Manage vendor relationships, SOWs, and budget tracking"
  - "Lead test-and-learn frameworks for SEO experimentation and competitive intelligence"
  - "Deliver monthly and quarterly executive reporting on organic performance metrics"

### AlgaeCal — "Generative Engine Optimization Specialist"
- Compensation: not disclosed as a range. Posting states: "Let's talk about salary once we've had the chance to get to know you better," and separately references "above-market pay for the right person."
- Location: Remote or in-office, Vancouver, BC, Canada.
- Required experience: "2+ years driving revenue through generative AI in eCommerce with proven conversion metrics."
- Responsibilities as posted:
  - "Fine-tune language models and deploy generative AI tools (GPT, Claude, Gemini, Perplexity) for marketing purposes"
  - "Optimize AI-generated content for search engines and chatbot platforms to improve visibility"
  - "Design and implement conversational bots that drive conversions"
  - "Develop personalized customer experiences using AI and CRM data"
  - "Conduct A/B testing on prompts and campaign outputs to improve performance metrics"
  - "Build SEO-optimized AI-generated product pages and content"
  - "Implement content moderation to address fake reviews and misinformation"
  - "Train non-technical teams on AI best practices"

## Pull notes — mechanical only

- Both pulled via WebFetch (HTML→markdown, prompted extraction). No raw HTML retained.
- These two postings were pulled specifically for the salary-benchmark task (ROLES-SAL); other live agents in this pass are pulling job-description content more broadly under `f-roles-jd-*` filenames — this file does not duplicate that lane, it captures only postings that carried a disclosed or explicitly-declined compensation figure, found incidentally while probing Built In for a GEO/AEO salary-benchmark product page (none exists — see f-roles-salary-payscale-salarycom-2026-09-23.md).

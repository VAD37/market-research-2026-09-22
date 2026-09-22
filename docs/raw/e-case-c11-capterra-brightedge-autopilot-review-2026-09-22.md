# Capterra — BrightEdge, 2-star user review (Autopilot / Opportunity-forecasting bugs)

```yaml
source:          Capterra (user-submitted review of BrightEdge)
url_or_doc_id:   https://www.capterra.com/p/124928/BrightEdge/reviews/
published:       2023-10-26 (review date, as shown on the page)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about category noise
tier:            5
tier_reason:     Review-site review, per this cluster's task instructions ("5 review-site review (label source_label: user-reported)"). Filed as `pull_purpose: evidence about category noise` — the review names two BrightEdge automation/recommendation features (Autopilot, Opportunity forecasting) as broken, but does not itself use AI/LLM/GEO/AEO vocabulary, so the link to this repo's AI-visibility scope is the reviewer's named features, not the reviewer's own framing.
source_label:    user-reported
lane:            E
sub_market:      organic recommendation
engine:          none named
metric_kind:     none
vertical:        none named
evidence_grade:  screened — no claim. Seven-item bar: (1) brand — present, BrightEdge, "Ivy P., Senior Manager SEO, Computer Software, 1,001-5,000 employees" named; (2) engine — absent; (3) date window — partial, "Used the software for: 1-2 years" stated, review dated 2023-10-26; (4) baseline — absent; (5) intervention — absent, no described GEO/AEO effort, only general tool-feature complaints; (6) sample size — absent, n=1; (7) who measured — self-reported. Stale: published 2023-10-26, predating the AI-visibility/GEO category's emergence per `docs/method/scope.md` caveats. Named features (Autopilot, "Opportunity forecasting") are BrightEdge's own automation/recommendation layer per the vendor's product marketing, but the review itself never connects them to AI search, LLM citation, or AI-surface visibility — filed as the second-lowest BrightEdge review found, with this gap stated plainly.
direction:       negative (product-quality/bug complaint; link to AI-visibility function is inferred from feature name only, not stated by the reviewer)
vendor_named:    BrightEdge
supersedes:      none
captured:        full review text, title, star rating, date, reviewer name/role/company/industry/size. No vendor reply is shown under this specific review.
```

## Verbatim

> IP
> Ivy P.
> Senior Manager, SEO
> Computer Software
> Used the software for: 1-2 years
>
> "Almost as clunky and poorly built as it is expensive."
>
> October 26, 2023
>
> 2.0
>
> Continue reading
>
> **Pros**
>
> - It has a robust set of features - if they all worked correctly- Autopilot is in theory, a fantastic feature. - Opportunity forecasting would have been great, but due to the number of bugs it has, it was unusable- Data Cube, site auditing tools, content marketing tools are good, but not better than what SEMrush, Ahrefs, Moz, etc. have at a fraction of the cost
>
> **Cons**
>
> - At over $55,000/year, the only key features it has over SEMRush, Moz, and Ahrefs ended up not working at all. We were locked into a full year and still use SEMRush and Ahrefs. Waste of money!- How clunky and slow everything is. Power users hate the UI and it takes twice as long to use any of their core features- Lack of QA. - Very faulty keyword research tools with extremely inaccurate, buggy results- Autopilot integration was pretty bad. It ended up breaking our build and their internal teams had no clue how to fix it
>
> Review Source

## Also found on the same BrightEdge reviews page, screened out (not filed as separate items)

Per grading rule 1's "screened — no claim" bucket, the remaining below-4-star BrightEdge reviews returned by this pull were read and screened out because they carry no AI/GEO/AEO content and no quantified claim beyond the ones already filed above:

| Reviewer | Rating | Date | Title | Reason screened |
|---|---|---|---|---|
| Chiara G. | 2.0 | 2025-06-25 | "A lot of improvement is needed" | General UI-unfriendliness complaint ("not intuitive at all... functionality... scattered all over"); no AI/GEO content, no metric |
| Gaurav G. | 3.0 | 2020-01-27 | "Holistic SEO Analytics Tool" | Actually positive overall ("great when it comes to usability... lifted the ROI of site"); the 3.0 rating reflects mixed usability notes, not an AI-visibility failure claim; also stale (2020) |
| Cole R. | 3.0 | 2018-04-23 | "Definitely not worth enterprise spend!" | Complains ranking reports were "massively inaccurate," pre-dates AI-visibility category by ~6 years |
| Verified Reviewer | 3.0 | 2019-04-17 | "Expensive, overly complicated and locked into a long contract" | General complexity/pricing complaint, no AI content, pre-dates category |
| Adam C. | 3.0 | 2023-02-13 | "Has some interesting features, but difficult to utilise and cross analyse" | General feature-usability complaint, no AI/GEO content |

## Pull notes — mechanical only

- Pulled from the same page load as `docs/raw/e-case-c11-capterra-brightedge-scam-review-2026-09-22.md`; see that file's pull notes for tab handling and navigation path (shared).
- The reviews page shows 45 reviews across 2 pages (25 shown on page 1 via "Show more"/default render); this pull's screening table above covers every review at or below 3.0 stars found within the page-1 content actually returned by `get_page_text`, not a guaranteed-exhaustive read of all 45.

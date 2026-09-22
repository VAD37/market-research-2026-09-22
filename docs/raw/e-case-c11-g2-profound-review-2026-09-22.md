# G2 — Profound, 1-star user review

```yaml
source:          G2.com (user-submitted review of Profound, filtered to the site's 1-star / NPS-score-1 bucket)
url_or_doc_id:   https://www.g2.com/products/profound/reviews?filters%5Bnps_score%5D%5B%5D=1#reviews
published:       2026-05-21 (review date, as shown on the page)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            5
tier_reason:     Review-site review, per this cluster's task instructions ("5 review-site review (label source_label: user-reported)").
source_label:    user-reported
lane:            E
sub_market:      organic recommendation
engine:          none named — review does not name a specific AI assistant/engine
metric_kind:     none — qualitative dissatisfaction only, no visibility/traffic/sales number stated
vertical:        none named
evidence_grade:  screened — no claim. Seven-item bar: (1) brand — present, Profound named as the product and the reviewer identifies as a real (if anonymized) small-business user; (2) engine — absent, no AI assistant named; (3) date window, absolute — partial, review dated 5/21/2026 but no stated start/end of the reviewer's usage period; (4) baseline before intervention — absent; (5) the intervention itself — implicit only ("It is trying to solve AI Visibility") with no specifics of what was done; (6) sample size / traffic volume — absent, n=1 (this reviewer's own account); (7) who measured, paid by outcome — the reviewer is the source, and G2 discloses the review was solicited ("Incentivized", "Source: Seller invite"), which is stated, not hidden. Per grading rule 1 ("a page with no metric is screened — no claim"), this page carries no visibility/traffic/sales metric at all and is graded accordingly — filed in full regardless, since this cluster's brief calls for 1-2 star reviews naming no lift even where, as here, the complaint is qualitative rather than metric-bearing.
direction:       negative
vendor_named:    Profound
supersedes:      none
captured:        full page — the single review returned when the product's reviews are filtered to the 1-star bucket (page heading read "Profound Reviews (1)" under that filter). Review text, star rating, title, date, reviewer role/segment, and the "Validated Reviewer / Incentivized / Source: Seller invite" tags are all captured below. No vendor (Profound) reply was present under this review — the page proceeds directly to the "Pricing Options" section after it.
```

## Verbatim

> Verified User in Internet
> Small-Business (50 or fewer emp.)
> 5/21/2026
>
> "An Overpriced tall poppy avoid like the plague"
>
> 0/5 (displayed star rating on the page; the page's 1-star filter bucket returned this as its sole result)
>
> **What do you like best about Profound?**
>
> I'm struggling to find anything that I like about Profound other than the insane amount of money they've raised for what is really a mediocre product that does not really drive alot of value to customers
>
> Review collected by and hosted on G2.com.
>
> **What do you dislike about Profound?**
>
> The product itself is OK to use in theory but practically it delivers very little in terms of actionable insights products significantly cheaper could offer. for what Profound charge there is no amount of value this product can offer. Add to that it appears that far too many team members come across as overworked and under appreciated.
>
> Review collected by and hosted on G2.com.
>
> **What problems is Profound solving and how is that benefiting you?**
>
> It is trying to solve AI Visibility but again is that really benefiting I doubt it
>
> Review collected by and hosted on G2.com.
>
> Validated Reviewer
> Incentivized
> Source: Seller invite

## Pull notes — mechanical only

- Pulled via the Chrome extension (this cluster's sanctioned browser slot). `tabs_context_mcp` was called first; a dedicated new tab was created for this cluster's use (never touching the two other tabs already open in the shared session, belonging to other live agents — one a Google skincare search, one a case-study page).
- Reached by navigating to `g2.com/products/profound/reviews`, then appending the site's own 1-star filter query string `?filters[nps_score][]=1#reviews` (discovered via the page's own "1 star" filter link, which the `find` tool resolved to this exact URL pattern before the direct navigation was used).
- After this pull, further G2 navigation (to `g2.com/products/brandlight-ai/reviews`) returned a DataDome "Verification Required" slider CAPTCHA. Per this session's standing rules, CAPTCHAs are not solved. G2 was not used again this pull; see the census's browser-backlog line.
- The star display read "0/5" on the page for this review, despite being returned under a "1 star" filter bucket — recorded exactly as shown, not corrected or interpreted.
- Also captured (not filed as a separate item, screened out): a 2-star Profound review by "Evangelia S." (Small-Business, 5/22/2026, "Effective Visibility Tool, Needs Better Candidate Experience") — this review is affirmatively positive about the product's AI-visibility function ("I like that Profound ensures my company name and products come up first when searched, which was very valuable for my makeup brand") and its low score is driven entirely by an unrelated hiring/candidate-experience complaint ("I had an interview got rescheduled 3 times then ghosted me"). Screened out as off-target (not a negative account of AI-visibility efficacy) rather than filed as a case.

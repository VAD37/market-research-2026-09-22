# Capterra — How Capterra Collects and Verifies Reviews

```yaml
source:          Capterra (Gartner Digital Markets)
url_or_doc_id:   https://www.capterra.com/resources/how-we-verify-reviews/
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own policy/process page
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          n/a — review-platform policy, not an AI-assistant product
metric_kind:     none
supersedes:      none
captured:        full page text
technique:       review and listicle manufacture
models_tested:   n/a
date_window:     n/a
measured_effect: no — this is a policy/process page, not a measurement
vertical:        none named — written for Capterra's software marketplace generally
```

## Verbatim

As a marketplace offering software and services, we place significant emphasis on the credibility of user reviews, prioritizing reviewer authenticity above all. Our review verification process attempts to ensure every review reflects genuine user opinions.

Our commitment to honest reviews involves:

More than 2.5 million+ verified user ratings and reviews to guarantee breadth and depth of opinions.

More than 30 human quality assurance (QA) moderators to carefully collect and scrutinize each review.

More than 20 control checks per review to confirm each submission's authenticity.

Advanced technology and processes to analyze text quality, detect plagiarism, and identify the use of generative AI.

**Our process of collecting user reviews**

At Capterra, we understand the value of diverse perspectives in making informed decisions. To ensure a wide variety of opinions, we collect reviews in two ways:

1. Non-incentivized reviews — Any software user can leave a review for any product listed on our site. All submitted reviews are subject to our QA process prior to publication.

2. Incentivized reviews — Software and service users are invited to submit an honest review and offered a nominal incentive for their time and effort. All reviewers get the incentive upon approval, regardless of the rating they submit. All incentivized reviews are subject to our QA process prior to publication. Nominal incentives encourage participation from users who might otherwise not submit a review and help us capture a wider range of perspectives across large portfolios of software and service offerings.

**Our process of verifying reviews**

Our verification process attempts to ensure each review reflects the genuine experience of a true software or service user. Here's what we do:

1. The reviewer's identity is confirmed

A robust QA moderation system operating behind the scenes: Our QA moderating team uses a combination of manual checks and enrichment services to confirm that each reviewer is a genuine person with real experience of the product or service. The team also flags conflicts of interest and AI-generated personas. In case a reviewer's identity cannot be confirmed and/or a conflict of interest is flagged, their review gets disqualified and is never published.

Reviewer profiles displayed on our site: To help buyers find relevant reviews from similar individuals, we create dedicated reviewer profiles that include professional backgrounds and expertise, and offer crucial context into the relevance and credibility of the feedback. For reviews of software solutions, a reviewer's profile may display the name, photo, function, industry, organization size, and duration of use. For reviews of service providers, a reviewer's profile may display the name, photo, function, industry, and organization size. We understand buyers' need for reassurance that the feedback is from real people. At the same time, we honor reviewers' right to preserve a certain degree of anonymity online. Therefore, in some cases, certain personally identifiable information, such as photos and/or full names, may not be displayed.

2. The review content is verified

Once the review verification team confirms the reviewer's identity, they proceed to verifying the content submitted. This process includes: Multiple manual control checks (our team of QA moderators performs a series of control checks to validate the genuineness of reviews, including checking the reviewer's history, the depth of their interaction with the software or service, and cross-referencing data to ensure consistency and truthfulness); Technology checks (we employ leading technologies to analyze content quality and check for generative AI and plagiarized content, ensuring every review is authentic); Fair and equal treatment for all reviews (each review submitted to Capterra undergoes the same rigorous verification process); Clear review submission guidelines (to maintain the quality and authenticity of reviews, we provide detailed submission guidelines that outline what is expected from each submission).

3. Fake reviews are actively combated

Our goal is to protect the integrity of our platform by actively combating fake identities and fraudulent reviews. Our process for identifying fake elements employs sophisticated strategies, including pattern recognition, behavioral analysis, and cross-referencing data points, to identify spam profiles, fake identities, and fraudulent reviews.

When a review is flagged as suspicious, we take the following immediate actions: Request additional proof (we contact the reviewer for further evidence of software or service use or additional information); Assessment and decision (we review each proof of use for authenticity — legitimate reviews and reviewers are published and continue to be nurtured within our community; if the proof is insufficient or not provided, the review is never published, and the reviewer is permanently flagged and removed from our community).

**Developing actionable insights from ratings and reviews**

We leverage user ratings and reviews to generate insights regarding product features, capabilities, value for money, or usability. These insights help us shape robust research methodologies to determine top product rankings, such as Capterra Shortlist, and inform product evaluations in our editorial content.

## Pull notes — mechanical only

- `www.capterra.com/legal/review-guidelines-and-anonymous-user-terms` (a guessed URL) 404'd. The working URL was recovered by loading `www.capterra.com/legal/terms-of-use/` and using the browser extension's `find` tool to locate an in-page link to "How Capterra verifies reviews" (`/resources/how-we-verify-reviews/`).
- `get_page_text` returned the full page body cleanly — no truncation on this pull.
- This page explicitly names "Capterra Shortlist" and "our editorial content" as downstream products built on review data, which is a direct link between the review corpus this policy protects and Capterra's own "best-of" content (Shortlist) — relevant context for the review-and-listicle-manufacture technique, though the page does not itself use the words "listicle" or "best-of list".
- A companion page, `www.capterra.com/resources/how-we-ensure-transparency/`, was located by `find` but not pulled in this task (time budget); `unknown — checked capterra.com/resources/how-we-verify-reviews only 2026-09-22` for its content.

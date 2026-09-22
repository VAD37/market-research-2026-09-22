# Google — Spam policies for Google web search (essentials)

```yaml
source:          Google (Search Central documentation)
url_or_doc_id:   https://developers.google.com/search/docs/essentials/spam-policies
published:       last updated 2026-08-28 UTC per page footer
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own framing, publisher-facing
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Google (web search / Search Central policy; page does not scope itself to AI Overviews or AI Mode specifically)
metric_kind:     none
supersedes:      none
captured:        sections on scaled content abuse, link spam, and site reputation abuse
technique:       engine statement — checks whether Google names anything resembling "corpus seeding" (placing content in third-party high-authority sources to gain citation/ranking) as a policy violation
models_tested:   n/a
date_window:     n/a
measured_effect: n/a (policy page, not a measurement)
vertical:        n/a
```

## Verbatim

### Scaled content abuse

"Using generative AI tools or other similar tools to generate many pages without adding value for users" is named as an example. The policy defines scaled content abuse as generating large quantities of unoriginal content primarily to manipulate rankings rather than help users, including scraping feeds, stitching together content from multiple sources without added value, and creating pages where "the content makes little or no sense to a reader but contains search keywords."

### Link spam

"Buying or selling links for ranking purposes," including exchanging money, goods, or services for links. The policy explicitly prohibits "Advertorials or native advertising where payment is received for articles that include links that pass ranking credit, or links with optimized anchor text." Qualifying links using `rel="nofollow"` or `rel="sponsored"` are stated as acceptable for legitimate advertising and sponsorship.

### Site reputation abuse

"Third-party content is content that's created by an entity that's separate from the established host site." The policy targets hosting third-party content "mainly because of that host's already-established ranking signals." A stated prohibited example: "A medical site hosting a low-quality, third-party advertising page about 'best casinos' that isn't integrated with the site."

### Notable omissions (recorded, not interpreted)

No section specifically titled or addressing "reviews system abuse," "manufactured reviews," "AI Overviews," or "AI Mode" was found on this page. The Reviews system is mentioned elsewhere on Google's documentation only as a ranking-system type, not inside this spam-policy page.

## Pull notes — mechanical only

- Fetched via WebFetch, 200.
- The page's "site reputation abuse" section is the closest existing Google policy language to the "corpus seeding in high-citation sources" technique, but it addresses a host accepting third-party content for its own ranking credit — a different direction from a brand placing content into an external high-citation source (Wikipedia, Reddit, a publisher) to be cited by an AI answer. Neither direction is named as "corpus seeding" or any equivalent term on this page.
- This page is Google's general web-search spam policy; it is not scoped to AI Overviews, AI Mode, or Gemini specifically, and does not state whether the same policies govern AI-surface citation selection. Recorded as `unknown — checked developers.google.com/search/docs/essentials/spam-policies 2026-09-22` on that specific question.

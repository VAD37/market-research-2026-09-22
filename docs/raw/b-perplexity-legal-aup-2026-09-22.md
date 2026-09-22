# Perplexity — Acceptable Use Policy + Legal Hub sitemap (checked for advertising / merchant / publisher terms)

```yaml
source:          Perplexity (perplexity.ai/hub/legal)
url_or_doc_id:   https://www.perplexity.ai/hub/legal/aup ; https://www.perplexity.ai/hub/legal
published:       2025-07-08 ("Last updated: July 8th, 2025")
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own legal page
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Perplexity
metric_kind:     none
supersedes:      none
captured:        full page (AUP) + interactive sitemap (Legal Hub landing page)
```

## Verbatim

**Banner shown atop the AUP page:**

"We recently updated our consumer Privacy Notice.

We added more detail about cookies, first-party advertising measurement, and your privacy choices. We also clarified that we do not sell your personal data or send your queries, prompts, or conversation content to advertisers."

**Legal Hub left-nav document list, as rendered on the AUP page (`https://www.perplexity.ai/hub/legal/aup`):**

"Perplexity Acceptable Use Policy
Legal overview
Platform User Terms
Enterprise & Developer Terms
Policies & Guidelines
Digital Services Act (DSA) Information
German Local Representative
Korea Billing & Consumer Information
Perplexity Acceptable Use Policy
Perplexity Pro Perks Terms and Conditions
Privacy & Data Protection"

**Legal Hub landing page (`https://www.perplexity.ai/hub/legal`) — interactive-element sitemap, `read_page` filter "interactive":**

Top-level links found: "Enterprise" (`/enterprise`), "Customers" (`/hub/customers`), "Pricing" (`/hub/pricing`), "Terms of Service" (`/hub/legal/terms-of-service`), "Privacy Notice" (`/hub/legal/privacy-notice`). Category-group buttons present but collapsed in the DOM (labels not exposed by the accessibility tree without a click). A natural-language element search for "legal document links for merchant, publisher, advertising, or acceptable use policy" on this landing page returned: "the page contains a 'Perplexity Legal Hub' with various terms of service and privacy documents (Terms of Service, Privacy Notice, API Terms, Enterprise Terms), none of these explicitly match the user's search criteria for merchant policies, publisher policies, advertising policies, or acceptable use policies."

**Acceptable Use Policy body — full text:**

"Last updated: July 8th, 2025

Thank you for choosing to use Perplexity (the "Services"). At Perplexity AI, Inc. ("Perplexity"), we are committed to lawful, safe and responsible artificial intelligence development and use, which this Acceptable Use Policy (this "Policy") is designed to promote.

Please note that this Policy is incorporated into the terms and conditions or other agreement that you have entered into with Perplexity (or an authorized third-party distributor) that governs your use of the Services.

Respect applicable law. [...]
Avoid high-risk activity. You must not access, deploy or use the Services to conduct or facilitate any activity that poses a significant threat to individuals or society (whether or not it is expressly illegal in your jurisdiction). For example, you may not access, deploy or use the Services to:
Create, compile or distribute disinformation or manipulative content; harassing, hateful or defamatory content; pornographic or exploitative content; unsolicited advertising or promotional materials; or unauthorized collections of personal data;
[...]

Avoid technical misuse. [...]
Respect our partners. The Services may use AI models provided by third parties. When using the Services, therefore, you must comply with those parties' acceptable usage policies.
Exceptions. [...]
Changes to This Policy. [...]"

## Pull notes — mechanical only

- Loaded via Chrome extension `get_page_text` on `www.perplexity.ai/hub/legal/aup` and `www.perplexity.ai/hub/legal`; both full pages, no login gate. Contrary to `channels.md`'s `403→ext` expectation for `perplexity.ai/hub`, both loaded directly without a permission prompt (single-machine observation, per that file's own caveat).
- The Legal Hub's current, machine-readable document list (both the top-level links and the AUP page's left-nav) carries **no standalone "Advertiser Terms," "Publisher Program Terms," or "Merchant Program Terms"** document. A `find` natural-language search of the landing page explicitly confirmed no such match. This is existence evidence, not proof of removal by itself — cross-referenced against `docs/raw/b-perplexity-merchant-terms-withdrawn-2026-09-22.md`, where the specific merchant-terms URL found via web search now 404s.
- The AUP's only advertising-adjacent clause prohibits users from generating "unsolicited advertising or promotional materials" — a user-conduct rule, not a statement about Perplexity's own ad product.
- The privacy-notice update banner ("first-party advertising measurement") is the one live, dated, company-stated signal in this pull that some advertising-adjacent data practice still exists in Perplexity's current privacy stack, even though no live "buy ads" page or advertiser terms page was found — recorded verbatim above, not interpreted further here.
- Full AUP body was captured; only the "Avoid high-risk activity" clause is quoted in extended form above because it is the only clause naming advertising. The "Respect applicable law," "Avoid technical misuse," "Respect our partners," "Exceptions," and "Changes to This Policy" clauses were read in full and contain no reference to advertising, sponsorship, commerce, merchants, or publishers.

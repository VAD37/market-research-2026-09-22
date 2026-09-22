# 16 CFR Part 255 — FTC Guides Concerning the Use of Endorsements and Testimonials in Advertising

```yaml
source:          Electronic Code of Federal Regulations (eCFR), codifying FTC guides
url_or_doc_id:   https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255 ; https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.0 ; https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5 (16 CFR Part 255)
published:       Source note on page: "88 FR 48102, July 26, 2023, unless otherwise noted" (most recent Federal Register revision cited by eCFR for this Part)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — codified federal regulation, current-as-published by eCFR (an official US government legal-text site), functionally equivalent to filed/binding text
source_label:    filed
lane:            B, D
sub_market:      paid placement
engine:          n/a — cross-engine regulatory text
metric_kind:     none
supersedes:      none
captured:        Table of contents for Part 255; "Authority" and "Source" lines; § 255.0(a) purpose, (b) "endorsement" definition, (f) "clear and conspicuous" definition (partial, truncated); § 255.5(a) "Disclosure of material connections" (full) and the opening of the (b) examples (partial, truncated)
```

## Verbatim

### Part 255 — table of contents and citation details

"Guides Concerning the Use of Endorsements and Testimonials in Advertising 255.0 – 255.6
§ 255.0 Purpose and definitions.
§ 255.1 General considerations.
§ 255.2 Consumer endorsements.
§ 255.3 Expert endorsements.
§ 255.4 Endorsements by organizations.
§ 255.5 Disclosure of material connections.
§ 255.6 Endorsements directed to children."

"URL: https://www.ecfr.gov/current/title-16/part-255
Citation: 16 CFR Part 255
Agency: Federal Trade Commission
Part 255
Authority: 38 Stat. 717, as amended; 15 U.S.C. 41-58.
Source: 88 FR 48102, July 26, 2023, unless otherwise noted."

### § 255.0 Purpose and definitions

"§ 255.0 Purpose and definitions.

(a) The Guides in this part represent administrative interpretations of laws enforced by the Federal Trade Commission for the guidance of the public in conducting its affairs in conformity with legal requirements. Specifically, the Guides address the application of section 5 of the FTC Act, 15 U.S.C. 45, to the use of endorsements and testimonials in advertising. The Guides provide the basis for voluntary compliance with the law by advertisers and endorsers. Practices inconsistent with these Guides may result in corrective action by the Commission under section 5 if, after investigation, the Commission has reason to believe that the practices fall within the scope of conduct declared unlawful by the statute. The Guides set forth the general principles that the Commission will use in evaluating endorsements and testimonials, together with examples illustrating the application of those principles. The examples in each section apply the principles of tha[note: truncated at tool output limit]

(b) For purposes of this part, an "endorsement" means any advertising, marketing, or promotional message for a product that consumers are likely to believe reflects the opinions, beliefs, findings, or experiences of a party other than the sponsoring advertiser, even if the views expressed by that party are identical to those of the sponsoring advertiser. Verbal statements, tags in social media posts, demonstrations, depictions of the name, signature, likeness or other identifying personal characteristics of an individual, and the name or seal of an organization can be endorsements. The party whose opinions, beliefs, findings, or experience the message appears to reflect will be called the "endorser" and could be or appear to be an individual, group, or institution.

(c) The Commission intends to treat endorsements and testimonials identically in the context of its enforcement of the Federal Trade Commission Act and for purposes of this part. The term endorsements is therefore gen[note: truncated at tool output limit]

...

(f) For purposes of this part, "clear and conspicuous" means that a disclosure is difficult to miss (i.e., easily noticeable) and easily understandable by ordinary consumers. If a communication's representation necessitating a disclosure is made through visual means, the disclosure should be made in at least the communication's visual portion; if the representation is made through audible means, the disclosure should be made in at least the communication's audible portion; and if the representation is made through both visual and audible means, the disclosure should be made in the communication's visual and audible portions. A disclosure presented simultaneously in both the visual and audible portions of a communication is more likely to be clear and conspicuous. A visual disclosure, by its size, contrast, location, the length of time it appears, and other characteristics, should stand out from any accompanying text or other visual elements so that it is easily noticed, read, and[note: truncated at tool output limit]"

### § 255.5 Disclosure of material connections

"§ 255.5 Disclosure of material connections.

(a) When there exists a connection between the endorser and the seller of the advertised product that might materially affect the weight or credibility of the endorsement, and that connection is not reasonably expected by the audience, such connection must be disclosed clearly and conspicuously. Material connections can include a business, family, or personal relationship. They can include monetary payment or the provision of free or discounted products (including products unrelated to the endorsed product) to an endorser, regardless of whether the advertiser requires an endorsement in return. Material connections can also include other benefits to the endorser, such as early access to a product or the possibility of being paid, of winning a prize, or of appearing on television or in other media promotions. Some connections may be immaterial because they are too insignificant to affect the weight or credibility given to endorsements. A material connection needs to be disclosed when a significant minority of the audience for an endorsement does not understand or expect the connection. A disclosure of a material connection does not require the complete details of the connection, but it must clearly communicate the nature of the connection sufficiently for consumers to evaluate its significance.

(b) Examples:

(1) Example 1. A drug company commissions research on its product by an outside organization. The drug company determines the overall subject of the research (e.g., to test the efficacy of a newly developed product) and pays a substantial share of the expenses of the research project, but the research organization determines the protocol for the study and is responsible for conducting it. A subsequent advertisement by the drug company mentions the research results as the "findings" of that research organization. Although the design and conduct of the research project are control[note: truncated at tool output limit]"

## Pull notes — mechanical only

- `WebFetch` to `www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255` returned a 302 redirect to `unblock.federalregister.gov` (a bot-check redirect), so this pull used the Chrome extension instead.
- The eCFR "Part 255" landing page's DOM only exposed the table of contents and the Authority/Source metadata via `document.body.textContent`; the actual section body text (§255.0, §255.5) only appeared after navigating directly to each section's own URL (`.../part-255/section-255.0`, `.../part-255/section-255.5`) — the part-level page appears to lazy-load section bodies that this extraction did not trigger.
- Same truncation constraint as the EU pulls in this cluster: the JS-execution tool caps returned strings at roughly 1000-1100 characters, so every long paragraph above is cut at `[note: truncated at tool output limit]` rather than filled from memory. §255.0(a) end, (c) full, (d), (e), and the remainder of (f) and of §255.5(b)'s ten examples were not captured in this pull.
- §255.1 through §255.4 and §255.6 (general considerations; consumer, expert and organizational endorsement specifics; children's endorsements) were not pulled — out of time budget for this cluster, and judged secondary to §255.0's definitions and §255.5's material-connection disclosure duty, which is this Guide's core clause bearing on paid/sponsored disclosure.
- This Part does not name AI systems, chatbots, or AI assistants anywhere in the text captured here. It is drafted in party/endorser-neutral terms ("any advertising, marketing, or promotional message... that consumers are likely to believe reflects the opinions, beliefs, findings, or experiences of a party other than the sponsoring advertiser") and its application to an AI-assistant-generated recommendation is not stated by the text itself — recorded as an interpretive gap in the summary file, not resolved here.

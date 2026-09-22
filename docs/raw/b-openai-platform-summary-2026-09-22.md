# OpenAI platform primary — summary table (Pass 2, P2-c3)

```yaml
source:          compiled from this cluster's own docs/raw/ pulls, all dated 2026-09-22
url_or_doc_id:   n/a — summary of raw pulls listed below
published:       n/a
pull_date:       2026-09-22
pull_method:     manual (compiled from browser-extension pulls made this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default; inherits tier of the platform-primary pages it cites, no new evidence introduced
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        n/a — this file is a summary index, not a page capture
```

No interpretation. Every row cites its raw file and quotes the page's own words. Per template, `docs/raw/` is compression-exempt; this file stays as a literal answer table rather than prose.

## Summary table

| Question | Answer | Verbatim quote | Raw file |
|---|---|---|---|
| Ad product exists (yes/no, as OpenAI states it) | **Yes.** Live, named "ChatGPT Ads" / "Ads in ChatGPT", launched as a test 2026-02-09, expanded internationally through 2026-08-11 | "Today, we're beginning to test ads in ChatGPT in the U.S." (2026-02-09); "ChatGPT Ads has now launched in the United Kingdom, Mexico, Brazil, Japan, and South Korea" (2026-08-11 update) | `b-openai-testing-ads-chatgpt-2026-09-22.md` |
| Formats and labels named | Standard below-response ad unit (advertiser name, favicon, title, copy, landing page, image) labeled "Sponsored"; plus a second alpha-stage format, "Sponsored Agents" | "Ads can appear below the end of a response. Ads are clearly labeled as sponsored and visually separated from ChatGPT's response." / "Sponsored Agents are an advertising format that lets people chat with an AI representative of a business in ChatGPT" | `b-openai-ads-help-article-2026-09-22.md`, `b-openai-ads-basics-pricing-2026-09-22.md`, `b-openai-sponsored-agents-2026-09-22.md` |
| Self-serve vs IO | **Both.** Self-serve beta ("Ads Manager") plus an intermediary/reseller/agency-partner model (IO-adjacent), governed by one contract that names both paths | "Today, we're beginning to roll out a beta self-serve Ads Manager that allows advertisers to sign up and purchase ads directly to appear in ChatGPT." / Advertising Terms §2 "Advertising Intermediaries" and §2.2 "Reseller Program" | `b-openai-new-ways-buy-ads-2026-09-22.md`, `b-openai-advertising-terms-2026-09-22.md` |
| Pricing disclosed (figure verbatim, or unknown) | **Disclosed, partially — a recommended starting bid, not a fixed rate card.** No CPM/CPC rate card is published; a late-payment finance-charge rate is separately disclosed in the legal terms | "For CPC campaigns, we recommend starting with a maximum bid of $3–$5 USD per click." / "Overdue undisputed Fees may be subject to a finance charge of 1.5% of the unpaid balance per month." | `b-openai-ads-basics-pricing-2026-09-22.md`, `b-openai-advertising-terms-2026-09-22.md` |
| Countries | Consumer-facing ads live (as of 2026-08-11): US, UK, Mexico, Brazil, Japan, South Korea, Canada, Australia, New Zealand. Advertiser **self-service sign-up** available in 55 listed countries (broader set, includes EU/EEA, Middle East/North Africa, more of Asia-Pacific) | "ChatGPT Ads has now launched in the United Kingdom, Mexico, Brazil, Japan, and South Korea." (consumer); full 55-country table headed "Ads Manager Availability" (advertiser self-service) — see raw file for full list | `b-openai-testing-ads-chatgpt-2026-09-22.md` (consumer countries), `b-openai-ads-manager-availability-2026-09-22.md` (advertiser self-service countries) |
| Eligibility tiers | Ads shown only on **Free** and **Go** subscription tiers; **Plus, Pro, Business, Enterprise, Edu** carry no ads. Under-18 accounts excluded | "Ads may appear for users on the Free and Go plans. Plus, Pro, Business, Enterprise, and Edu accounts will not have ads. We do not show ads to accounts identified as belonging to people under 18." | `b-openai-ads-help-article-2026-09-22.md` |
| Advertiser policies | Full ad placement, ad content, and advertiser-eligibility policy published, versioned v1.0 (March 2026) through v1.6 (September 2026); category allow/deny lists, review process (automated ML + human escalation), enforcement ladder | "OpenAI's policy is to allow ads to be placed near chats that are safe, appropriate, and consistent with user trust and brand safety." / "We use machine learning systems, including LLMs and classifiers, to review ads, landing pages, and advertiser signals for policy compliance before ads are eligible to run" | `b-openai-ad-policies-2026-09-22.md` |
| Merchant/feed program and its terms | **Two distinct feed programs**, not to be conflated: (1) a paid-ads product feed inside Ads Manager, beta, self-serve; (2) a separate "Agentic Commerce" / organic product-feed program for surfacing products in shopping results, gated to "approved partners," governed by a free (no consideration) content-license contract with a $1,000 OpenAI liability cap | "Onboarding product feeds in ChatGPT is currently available to approved partners. To apply for access, fill out this form" / "OpenAI's total liability will not exceed $1,000." / Ads-feed page: "Products from your feed will only be eligible for use in ads during this beta. They will not appear in organic ChatGPT conversations" | `c-openai-product-feed-campaigns-2026-09-22.md` (paid), `c-openai-commerce-get-started-2026-09-22.md` (organic/agentic, gated), `c-openai-merchant-feed-terms-2026-09-22.md` (contract terms) |
| Checkout program and its fee if stated | Program named **"Instant Checkout"**: "lets you complete checkout in ChatGPT instead of leaving for the merchant's site," for "some eligible products and merchants." **No checkout fee, take-rate, or commission percentage/figure found on any OpenAI page pulled in this cluster.** Separately, for Shopify-integrated merchants, one help page states checkout happens on the merchant's own store, not in-ChatGPT — the two pages are not reconciled here | "For some eligible products and merchants, ChatGPT may also show an Instant Checkout option that lets you complete checkout in ChatGPT instead of leaving for the merchant's site." / "users check out on the merchants' online store." | `c-openai-shopping-chatgpt-search-2026-09-22.md` (Instant Checkout), `c-openai-shopify-merchants-2026-09-22.md` (Shopify checkout-on-merchant-site statement) — fee: `unknown — checked https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search, https://developers.openai.com/commerce, https://developers.openai.com/commerce/guides/get-started 2026-09-22` |
| Publisher citation guidance | Publishers control citation/search-summary inclusion via `robots.txt` (OAI-SearchBot) separately from AI-training inclusion (GPTBot); ChatGPT search referral clicks carry a standing UTM parameter for publisher-side attribution | "For your site content to be included in summaries and snippets in ChatGPT, make sure you aren't blocking OAI-SearchBot." / "ChatGPT automatically includes the UTM parameter utm_source=chatgpt.com in referral URLs, enabling clear tracking and analysis of inbound traffic from ChatGPT search results." | `a-openai-publishers-developers-faq-2026-09-22.md` |

## All raw files this cluster produced

1. `docs/raw/b-openai-testing-ads-chatgpt-2026-09-22.md` — launch/rollout announcement, countries, tiers, ads principles
2. `docs/raw/b-openai-new-ways-buy-ads-2026-09-22.md` — self-serve Ads Manager launch, CPC bidding, agency/tech partners
3. `docs/raw/b-openai-approach-advertising-2026-09-22.md` — pre-launch principles post, ChatGPT Go pricing/country context
4. `docs/raw/b-openai-ads-help-article-2026-09-22.md` — full consumer-facing FAQ, eligibility, privacy, controls
5. `docs/raw/b-openai-ads-manager-availability-2026-09-22.md` — 55-country advertiser self-service table
6. `docs/raw/b-openai-ads-basics-pricing-2026-09-22.md` — ad format, $3–$5 CPC bid guidance, auction mechanic, UTM tracking
7. `docs/raw/b-openai-sponsored-agents-2026-09-22.md` — second ad format, alpha-gated
8. `docs/raw/b-openai-terms-policies-index-2026-09-22.md` — index of OpenAI's legal/policy document set
9. `docs/raw/b-openai-advertising-terms-2026-09-22.md` — full advertiser legal contract, 1.5%/month late fee, self-serve + intermediary/reseller model
10. `docs/raw/b-openai-ad-policies-2026-09-22.md` — full ad placement/content/advertiser policy, versioned changelog v1.0–v1.6
11. `docs/raw/b-openai-usage-policies-2026-09-22.md` — cross-product usage policy underlying the ads/commerce policies
12. `docs/raw/b-openai-sponsored-agents-2026-09-22.md` — (see #7)
13. `docs/raw/c-openai-product-feed-campaigns-2026-09-22.md` — paid-ads product feed setup (Ads Manager)
14. `docs/raw/c-openai-shopify-merchants-2026-09-22.md` — Shopify integration, checkout-on-merchant-site statement
15. `docs/raw/c-openai-shopping-chatgpt-search-2026-09-22.md` — organic shopping results, Instant Checkout, pricing display, merchant selection
16. `docs/raw/c-openai-agentic-commerce-protocol-landing-2026-09-22.md` — developers.openai.com/commerce landing page
17. `docs/raw/c-openai-commerce-get-started-2026-09-22.md` — ACP onboarding, gated to approved partners, prohibited-products policy
18. `docs/raw/c-openai-merchant-feed-terms-2026-09-22.md` — merchant feed legal contract, $1,000 liability cap, no fee
19. `docs/raw/c-openai-commerce-policies-2026-09-22.md` — full commerce prohibited-products and prohibited-merchant-practices list
20. `docs/raw/a-openai-publishers-developers-faq-2026-09-22.md` — citation/crawler guidance, UTM referral tagging
21. `docs/raw/b-openai-archive-check-testing-ads-2026-09-22.md` — archive-channel withdrawal/diff check (none found)

## Caveats

- Oldest pull depended on: 2026-09-22 (all pulls this cluster made today). `b-openai-usage-policies-2026-09-22.md` cites a page whose own "Effective" date is 2025-10-29 — flagged stale per `query-book.md`'s date rule, pulled anyway under that rule's platform-primary exemption, and its live-page freshness was re-checked at pull time (no newer version exists; 2025-10-29 remains the page's own last-updated date).
- No P2-c3 target URL 404'd or redirected during this pull; the one adjacent redirect encountered (`platform.openai.com/docs/bots` → `developers.openai.com/api/docs/bots`, via WebFetch, before this cluster's `docs/raw` pulls began) is recorded as a pull note in the fetch history but did not itself produce a dedicated raw file, since it fell outside this cluster's named target list.
- One archive check was performed (`b-openai-archive-check-testing-ads-2026-09-22.md`); it found no withdrawal or silent rewording on the one page checked. No other page in this cluster showed signs (broken link, 404, trade-press-only trace) of having been withdrawn, so no further archive checks were run.
- Two internal inconsistencies are recorded side by side, not reconciled, per root `CLAUDE.md`: (1) Instant Checkout ("complete checkout in ChatGPT") versus the Shopify-merchants page ("users check out on the merchants' online store") — eligibility for Instant Checkout is not stated on either page; (2) advertiser self-service sign-up availability (55 countries) is broader than confirmed consumer-facing ad-serving countries (9 named) — the pages do not state whether an advertiser can buy in a country where consumer ads are not yet live.
- No checkout fee, take-rate, or commission figure was found on any page pulled in this cluster (openai.com, help.openai.com, developers.openai.com) — recorded as `unknown — checked` in the summary table above, not guessed.
- Trade press was not used as a source per task instructions; no withdrawn OpenAI page was found that would require a tier-5 trade-press pointer fallback.

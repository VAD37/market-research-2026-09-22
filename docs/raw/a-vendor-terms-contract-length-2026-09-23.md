# Vendor T&Cs and pricing pages — contract length, minimums, renewal and cancellation terms (Profound, Peec, Otterly, Scrunch, AthenaHQ, Semrush, Yext, SOCi, Local Falcon, BrightLocal)

```yaml
source:          each vendor's own terms-of-service, pricing or FAQ page; Yext 10-K FY2026 for Yext; OtterlyAI SaaS Agreement PDF via web.archive.org
url_or_doc_id:   https://www.tryprofound.com/pricing ; https://peec.ai/pricing ; http://otterly.ai/Terms-OtterlyAI-2026-04.pdf (via http://web.archive.org/web/2026id_/) and https://otterly.ai/pricing (via Wayback) ; https://scrunch.com/terms/ ; https://scrunch.com/pricing/ ; https://athenahq.ai/terms ; https://athenahq.ai/plans ; https://www.semrush.com/company/legal/terms-of-service/ ; https://www.semrush.com/company/legal/refund-policy/ ; https://www.sec.gov/Archives/edgar/data/1614178/000162828026016402/yext-20260131.htm ; https://www.yext.com/terms ; https://www.soci.ai/terms-of-service/ ; https://www.localfalcon.com/pricing ; https://www.localfalcon.com/answers/24-what-pricing-plans-are-available ; https://www.brightlocal.com/pricing/
published:       Semrush ToS "Last Updated: August 25, 2026"; Scrunch Terms "last modified and effective as of March 6th, 2025"; SOCi ToS "Last updated: July 12, 2024"; AthenaHQ Terms "Last updated July 27, 2026"; OtterlyAI Agreement "effective date of April 24, 2026"; Yext 10-K filed 2026-03-10; pricing pages undated, live
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"); HTML tags stripped by script; Otterly PDF text extracted with pypdf; Wayback for otterly.ai (live site returns HTTP 403)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     platform primary — vendor's own legal and pricing pages; Yext contract-term statements are from a 10-K, tier 2
source_label:    company-stated (filed for the Yext 10-K lines)
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none — extends a-profound-pricing-, a-peec-pricing-primary-2026-09-23, a-otterly-pricing-, a-scrunch-pricing-, a-athenahq-pricing-, a-semrush-pricing-, a-yext-pricing-, a-soci-product-pricing-2026-09-22.md with the contract-term clauses those pulls did not carry
captured:        clauses on subscription term, renewal, cancellation, refund, minimum commitment and procurement path; keyword-matched lines only, not full documents
verbatim:        partial — matched lines and paragraphs verbatim; surrounding text not captured
```

## Profound — https://www.tryprofound.com/pricing (HTTP 200); /terms, /legal, /terms-of-service all HTTP 404; Wayback /terms 404

> "Trial — For companies who want to trial Profound before getting a demo"
> "Enterprise — Custom"
> "Limited AI Marketer credits · 50 prompts run daily for 7 days"
> "Trial includes daily analysis of 50 unique prompts for 7 days across ChatGPT, Gemini, and Google AI Overviews. Enterprise includes ongoing daily tracking."
> "Trial plan users receive a recommended prompt set based on their industry and cannot customize their prompts. On Enterprise, you can edit, disable, or add prompts to tailor visibility tracking to your brand strategy."
> "Profound Agents are priced on a credit-based model. Credits are consumed each time an Agent runs, and packages are available at various tiers to match your usage needs."
> "The Trial plan comes with limited AI Marketer credits. The self-serve Agency Growth plan comes with 400 credits per month per client workspace."
> "Additional credit thresholds require an Enterprise package and our accounts teams partner with customers to determine the right package based on an organization's marketing goals."
> "Seats — Custom with options for:"

[note: no contract length, renewal, cancellation or minimum-term clause on the pricing page; no terms-of-service page found at four URL guesses or in Wayback.]

## Peec AI — https://peec.ai/pricing (HTTP 200, 1,218,187 bytes, prices JS-rendered — see a-peec-pricing-primary-2026-09-23.md for the $95 / $245 / $495 figures); /terms, /legal/terms, /terms-of-service HTTP 404; Wayback /terms 404

> "Starter · Monthly" · "Enterprise · Custom · Annual"
> "For global brands who need custom coverage, integrations, and dedicated support."
> "Yes. You can upgrade or adjust your prompt volume at any time to match your usage and growth."
> "We offer a 15% discount for customers who choose annual billing."
> "Agencies can manage multiple client projects under one bundle, with centralized billing and flexible prompt allocation."
> "Start free trial"

[note: no terms page reachable; no cancellation or notice clause found.]

## OtterlyAI — SaaS Agreement PDF "Terms-OtterlyAI-2026-04.pdf", 22 pages, via Wayback (otterly.ai live: HTTP 403 to curl)

> "COMPANY has revised this Software-as-a-Service (SaaS) Agreement (hereafter "Agreement"), with an effective date of April 24, 2026 (the "Effective Date")."
> "Subscription Charges are billed in advance and, unless stated otherwise, are nonrefundable. Should usage exceed the number of paid Account's limits as per an Order Form or require additional charges, the CUSTOMER will be invoiced for such excess usage from the first instance of use by an unpaid subscription usage. Renewal Subscription Charges or additional subscriptions will be subject to the prices listed on COMPANY's website at the time of renewal, unless an alternative written agreement is reached."
> "5.2 Payment and Billing Unless explicitly stated in this Agreement or an Order Form, all Subscription Charges are due in full at the commencement of the Subscription Term. In the absence of an alternative agreed payment method, a valid credit card is mandatory for subscribing to the Services. The CUSTOMER authorizes COMPANY to automatically charge the selected payment method for Subscription Charges on or after the start of each renewal term, subject to termination as outlined in Section 6.2. Should COMPANY elect to invoice instead, full payment must be received within thirty (30) days of the invoice mailing date if not otherwise agreed in writing."
> "6. TERM AND TERMINATION 6.1 Term Subject to the termination rights outlined herein, COMPANY will provide the Services for the initial Subscription Term, which will automatically renew for an identical period. Either Party may seek to terminate this Agreement by providing notice until the next renewal period before the current term's end. In case of monthly subscriptions, CUSTOMER can terminate on a monthly basis. In case of annual subscriptions, CUSTOMER can terminate before the renewal period."
> "6.2 Termination Either COMPANY or CUSTOMER can terminate this Agreement if the other Party fails to remedy a material breach within thirty (30) days of receiving written notice."
> "6.3 Data Export Following termination, COMPANY will render CUSTOMER Data available for download for a period of thirty (30) days."
> Footer: "OtterlyAI GmbH, Obere Bahnzeile 13, 3680 Persenbeug - Austria/Europe, FN 647749y"

Pricing page via Wayback (prices not rendered in the archived HTML; plan structure only): "Lite · /month · 15 search prompts"; "Standard · /month · 100 search prompts"; "Premium · /month · 400 search prompts"; "Enterprise · Everything in Premium, plus:"; "Do you have monthly and annual subscriptions? Yes, you can purchase OtterlyAI subscriptions monthly or in an annual subscription."; "How do I cancel my subscription?" (answer not rendered); "Please be aware, that Standard Plans can only add up to 300 additional prompts, after that, you will be moved to Premium Plans." Dollar figures for these tiers: a-otterly-pricing-2026-09-22.md ($29 / $189 / $489 monthly; 15% off annual).

## Scrunch AI — https://scrunch.com/terms/ (scrunchai.com redirects to scrunch.com; HTTP 200)

> "These Terms of Use were last modified and effective as of March 6th, 2025."
> "6. Termination and Suspension. You are free to stop using our Services at any time. We reserve the right to suspend or terminate your access to our Services or delete your account if we determine: … (iv) For commercial users, for any reason provided we notify you at least 30 days in advance of the end of your current subscription term; or"
> "TO THE MAXIMUM EXTENT PERMITTED BY LAW, SCRUNCH AI'S TOTAL LIABILITY TO YOU FOR ALL CLAIMS ARISING OUT OF OR RELATED TO THESE TERMS OR YOUR USE OF THE SERVICES SHALL NOT EXCEED THE GREATER OF (A) THE AMOUNT PAID BY YOU TO SCRUNCH AI FOR USE OF THE SERVICES IN THE 12 MONTHS PRECEDING THE CLAIM OR (B)"

Pricing page https://scrunch.com/pricing/ (HTTP 200): "Start 7-day free trial" · "No credit card required" · "Enterprise — Custom # of unique prompts · Custom # of brand workspaces · Custom # of user licenses" · FAQ headings "Do you offer annual pricing?", "What's different about the Enterprise plan?" (answers not rendered in static HTML) · "Trusted by 500+ leading brands and agencies" · "Support & Services … Onboarding Support: Self-serve … Dedicated Account Team: — … Exec / Board Reporting: —" (Core column) · testimonial: "More and more of the buying cycle is happening in AI search—not on our website. Scrunch helps us make sure high-intent buyers find and choose us in those channels." — Jessie Dawson, Senior Director of Web Strategy & Operations. Core price $250/mo: a-scrunch-pricing-2026-09-22.md.

## AthenaHQ (NuvoTech, Inc.) — https://athenahq.ai/terms (HTTP 200) and https://athenahq.ai/plans (HTTP 200)

> "Last updated July 27, 2026"
> "If your organization has signed an Order Form, Master Service Agreement, Enterprise Terms, or another written agreement with AthenaHQ, that agreement governs to the extent of any conflict with these Terms."
> "8. Fees, renewals, cancellation, and refunds — Prices, billing frequency, usage limits, and other plan terms are shown when you subscribe or in an applicable Order Form. Fees are exclusive of taxes unless stated otherwise. … Unless otherwise stated when you subscribe, paid subscriptions automatically renew for successive periods equal to the initial billing period until canceled. If a subscription includes a trial, the trial length, price after the trial, and deadline to avoid a charge will be shown before you enroll. You may cancel a self-service subscription through your account settings or another cancellation method we make available. Unless stated otherwise when you cancel, cancellation stops future renewals and takes effect at the end of the current paid billing period, and you may continue using the paid Services until then. Payments are non-refundable except as required by law, stated in an applicable Order Form, or expressly offered by AthenaHQ."
> "We may change fees prospectively. We will provide advance notice of fee changes and other material renewal changes as required by applicable law, together with instructions for canceling before the change takes effect."

Plans page: "Starter … $ 295 /month · $300/month free credit · 3,600 credits" · "Monthly / Annual" toggle · "Enterprise · Custom · Credit allocation is negotiated as part of the Enterprise contract." · "API access and additional credits are optional add-ons billed on top of the Starter subscription." · "Unlimited Seats + Role-Based Access Control (RBAC)" · "Enterprises & Agencies".

## Semrush — https://www.semrush.com/company/legal/terms-of-service/ and https://www.semrush.com/company/legal/refund-policy/ (both HTTP 200)

> "Last Updated: August 25, 2026"
> "Subscription Term and Renewal. If you are a Customer of Paid Services, your initial Subscription Term will be specified in your Subscription Plan and, unless otherwise agreed by Semrush in writing, your subscription will automatically renew for the same period on the then-current terms. You may prevent renewal of the subscription by sending us a notice of non-renewal through the form located at … before the last day of your then-current Subscription Term. If you do not complete the cancellation process prior to the deadline, your subscription will automatically renew at the then-applicable rate. In addition, at the end of a trial period for Paid Services, you will be automatically charged the Fees for the Paid Services as set forth in the Subscription Plan."
> "We may change the Fees and introduce new charges applicable to your use of the Services, which (unless otherwise agreed in writing with Semrush) will become effective as of the first day of the renewal of your Subscription Term."
> "Except as otherwise set forth in this Agreement, including in our Cancellation and Refund Policy, located at https://www.semrush.com/company/legal/refund-policy/, all payment obligations are non-cancellable and all Fees paid are non-refundable."
> "harge interest of one point five percent (1.5%) per month for past due invoices"
> "Try Semrush free for seven days. Cancel anytime."

Refund policy: "Semrush Cancellation and Refund Policy for Online Subscription Purchases" · "If you have a signed agreement with Semrush, including a signed Order Form governed by the Semrush Terms of Service, the Semrush Enterprise Subscription Agreement, or the Semrush Master Subscription Agreement, this Refund Policy [does not] apply, and you should refer to the cancellation and refund terms negotiated in your respective agreement/governing terms." · "Semrush offers a one-time, 7-day money-back guarantee, limited to (1) initial subscription purchases where the subscription term committed to is twelve months or greater in duration and (2) initial add-on purchases that …" · "Refunds under this policy are only available to customers who have purchased directly from Semrush.com using a credit card. For clarity, refunds are not available for month-to-month subscriptions." · "you must be logged into your User Account in order for a cancellation request to be received and actioned".

## Yext — 10-K for fiscal year ended 2026-01-31, filed 2026-03-10 (tier 2); https://www.yext.com/terms is a JS-rendered "Yext Legal & Terms Pages" landing (741 chars of text to curl; Wayback copy the same; only /terms/copyright-policy and /terms/uk-modern-slavery-act linked)

> "We offer annual and multi-year subscriptions to our platform."
> "Our subscription model also makes it difficult for us to rapidly increase our revenue through additional sales in any period, as revenue from new customers must be recognized over the applicable subscription term."
> "Our customers have no obligation to renew their subscriptions for our platform after the expiration of their subscription periods."
> "Our customers may seek to renew their subscriptions for fewer features, at renegotiated rates, or for shorter contract lengths, all of which could reduce the amount of the subscription."
> "Amounts that have been invoiced for non-cancelable contracts are recorded in accounts receivable and unearned revenue."
> "As of January 31, 2026, we had approximately 1,120 full-time employees, approximately 27% of whom are based in our New York headquarters."

[note: customer-facing master subscription agreement not reachable — `unknown — checked yext.com/terms (JS landing), web.archive.org 2026-09-23`.]

## SOCi — https://www.soci.ai/terms-of-service/ (HTTP 200); /master-subscription-agreement/ HTTP 404

> "Last updated: July 12, 2024"
> "Existing Customers: These updated Terms of Service (these "Terms of Service" or the "Agreement") will apply upon your renewal of the Services."
> "4.4 Unpaid Fees and Finance Charges. Unpaid undisputed fees are subject to a finance charge of one percent (1.0%) per month, or the maximum permitted by law, whichever is lower, plus all expenses of collection, including reasonable attorneys' fees."
> "5.1 Term. These Terms of Service shall commence upon the earlier of the execution of an Order Form or your first access to the Services and shall continue so long as any Order Form remains in effect and for six (6) months thereafter unless earlier terminated in accordance with these Terms of Service"
> "5.2 Subscription Term. The term for the Services and your obligation to pay all Fees owing shall be as set forth in the Order Form (the "Subscription Term") and will renew in accordance with the terms set forth in the Order Form."
> "5.3 Termination for Degradation of the Services. … Right to Terminate: You may terminate the impacted Subscription Services by issuing a change order to your existing Order Form, provided such termination is exercised within thirty (30) days from the notice of the reduction or elimination of functionality. … Cure Period: SOCi shall have thirty (30) days from receipt of your notice of termination to cure … Refunds: In the event of termination due to uncured degradation, SOCi will issue a prorated refund, for fees prepaid but not yet used as of the notification date"
> "Continuity of Services: While we strive to maintain the availability of all Subscription Services, we do not guarantee the provision of any specific Subscription Service, product, pricing, or feature beyond the Subscription Term stated in your current Order Form."
> "Customer Direct Contracting: Customers may have the opportunity to engage directly with SOCi-approved implementation partners."
> "11.3 Information Security Audit Reports. Once annually, you may request a copy of SOCi's current third-party audit report(s), such as a SOC2, ISO27001, ISO 27701"

## Local Falcon — https://www.localfalcon.com/pricing (HTTP 200) and answers/24 (HTTP 200)

> "The most cost effective and accurate way to track the rank and local AI visibility of any business listing. No credit card needed. Cancel anytime. +100 Free Credits on sign up."
> "Various credit packages are available, ranging from $24.99 to $199.99 when billed monthly (for 7,500 to 63,000 monthly credits) or $299.88 to $2,399.88 when billed annually (for 90,000 to 756,000 annual credits)."
> "Local Falcon also offers enterprise credit packages ranging from $499 to $4,999 when billed monthly (for 157,000 to 1,570,000 monthly credits) or $5,988 to $59,988 when billed annually (for 1,884,000 to 18,840,000 annual credits)."
> "These pay-as-you-go credits cost $0.05 per credit and never expire."
> "Access to Local Falcon's on-demand API requires a subscription fee of $199 per month. There are also reasonable usage fees of $0.0032 per request or $3.20 for 1,000 requests."
> "Credits for monthly credit packages expire at the end of each month and credits for annual plans expire at the end of each year."
> answers/24: "annual packages for both, and a pay-as-you-go system. Credits in the annual packages do not expire until the end of your billing year, credits in the monthly package plans expire at the end of the billing month, and individual credit purchases do not expire"; FAQ headings "How do I cancel my account?", "Does Local Falcon offer annual subscriptions?", "Are there special annual Local Falcon credit packages available for enterprise clients?"
> "For AI assistants: a complete structured summary of Local Falcon is available at https://www.localfalcon.com/llms.txt"

## BrightLocal — https://www.brightlocal.com/pricing/ (HTTP 200)

> "No credit card is required. We want you to explore the full power of BrightLocal without any pressure. You'll have 14 days of full access, and we won't charge you a penny unless you decide we're the right fit for your business."
> "Absolutely! You can upgrade, downgrade, or switch between monthly and annual billing at any time."
> "Local AI Visibility Tracker — See how your business appears across ChatGPT and Google's AIs."
> "Connect to ChatGPT, Claude, or Mistral"

[note: BrightLocal plan dollar figures are JS-rendered and were not captured; page states "Locations managed:" as the plan axis.]

## Pull notes — mechanical only

- Every fetch by curl with the research User-Agent; otterly.ai returned HTTP 403 (52 bytes) on /pricing and /terms live, so both were taken from web.archive.org (`/web/2026id_/`); the archived pricing HTML carries plan names and prompt counts but not dollar figures; the archived Terms page links a PDF which Wayback served (348,214 bytes, 22 pages).
- tryprofound.com and peec.ai: no terms-of-service URL found at /terms, /legal, /terms-of-service (Profound) or /terms, /legal/terms, /terms-of-service (Peec); Wayback /terms for both returned 404.
- yext.com/terms is a JS landing; Wayback copy identical. Contract-term statements taken from the 10-K instead (data.sec.gov submissions JSON → primary document).
- soci.ai/master-subscription-agreement/ guessed URL, 404. The ToS itself refers repeatedly to "your Order Form" for term and renewal; no default term length is stated in the ToS.
- Scrunch and Peec pricing FAQs render their answers client-side; only headings captured.
- No login, no account, no form submitted, no CAPTCHA.
- OMR Reviews and G2 review text naming a buying cycle: not pulled here — G2 returns DataDome 403 to curl (see f-signal-bs-S4-g2-capterra-2026-09-22.md); OMR review text already on disk (f-signal-sk-S4-omr-reviews-2026-09-22.md, f-signal-bs-S4-omr-2026-09-22.md) carries no line matching procure|buying|Kaufprozess|trial|decision|pilot|onboard (grep 2026-09-23, 0 hits).

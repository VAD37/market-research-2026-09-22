# OpenAI Help Center — Billing & Payment (ChatGPT Ads)

```yaml
source:          OpenAI Help Center
url_or_doc_id:   https://help.openai.com/en/articles/20001216-billing-payment
published:       undated — no date on page
pull_date:       2026-09-23
pull_method:     fetch — python urllib (browser user-agent, no login) + trafilatura main-text extraction; not the Chrome extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full page
verbatim:        full
```

Pass 12, Lane B (task P12-ads). Body below is the page's own text as extracted, unedited.

## Verbatim

This article explains how billing works for ChatGPT Ads, including what must be configured before campaigns can deliver, how charges are applied, how spend is controlled, and what to do if you need help with a billing issue.
Set up billing before delivery starts
Before campaigns can begin delivering, billing must be fully set up in Ads Manager Beta. For self-serve card-billed accounts, this involves two steps:
- Create a billing profile: enter your business name, business address, and invoice delivery email. The invoice delivery email is used for invoices and other billing-related communication.
- Add a payment method: enter your credit card details and billing address information.
When you add a card, your bank may show a temporary authorization hold, which may appear as the equivalent amount in your card’s currency. This is not a completed charge and is automatically released after verification, though it may remain visible for 8 days or longer depending on your bank. Please see the Ads Billing page in Ads Manager for more details.
How billing works
ChatGPT Ads currently uses a postpay billing model that charges advertisers after ads have been delivered. As your campaigns run, spend accrues on your account. For self-serve card-billed accounts, charges are applied to the payment method saved in Ads Manager Beta.
Eligible sales-managed advertisers on postpaid invoice terms follow their invoice billing arrangements instead of saved-card threshold charging.
ChatGPT Ads supports cost per thousand impressions (CPM), cost per click (CPC), and conversion-optimized purchasing based on the campaign objective and billing option you select.
- Select a Views objective to buy on a cost per thousand impressions basis (CPM) and optimize for reach. With this objective, you are billed for impressions served.
- Select a Clicks objective to buy on a cost per click basis (CPC) and optimize for traffic. With this objective, you are billed for each click.
- Select a Conversions objective to optimize toward a selected standard conversion event. Eligible advertisers can select either oCPC (click billing) or oCPM (impression billing). Ads are not billed per conversion. See Conversion-optimized Campaigns for prerequisites, eligibility, and steps.
Your campaign budget controls the spending parameters for your campaign. When you create a campaign, choose one of the following budget types:
- Daily budget: The average amount you want the campaign to spend per day over a seven-day period. It is not a same-day spending limit. Billed media spend may be up to twice your selected daily budget on an individual day, but will not exceed seven times your daily budget over the applicable seven-day period. If delivery is below your daily budget on some days, unused amounts may be used later in the same seven-day period. See Daily Budgets for additional details.
- Campaign total budget: The maximum amount you are willing to spend across the campaign. Ads Manager paces spending over time based on your remaining budget and campaign schedule.
You can change the budget amount after creation, but you cannot change the budget type. Actual spend may vary based on delivery, user engagement, and the pricing model selected.
For how Ads Manager spreads spending over time for daily and campaign total budgets, see Budget Pacing.
In Ads Manager Beta, you can monitor spend and performance using metrics such as impressions, clicks, spend, CTR, Average CPC, Average CPM, and conversions if conversion measurement is set up.
Impressions, clicks, and CTR refresh approximately every 15 minutes. Spend insights may be delayed 7–8 hours. A zero or delayed spend total does not mean that no charges are accruing.
When charges happen
For self-serve card-billed accounts, your saved payment method is charged when your account reaches its assigned payment threshold.
When you sign up for a self-serve card-billed Ads Manager Beta account, your account is assigned a payment threshold that determines how much unpaid spend can accrue before your saved payment method is charged. This is not the same as a campaign budget and is not an account spend cap.
Approved advertisers typically start with a lower payment threshold and we may increase your payment threshold automatically over time based on successful payment history and other factors.
For example, if your account has a $25 payment threshold, your card will be charged once your account accrues $25 in unpaid spend. After a successful payment, your outstanding balance will be reduced by the payment amount. If delivery continues, your account can accrue spend again until it reaches the threshold or the end of the month.
If your account still has an outstanding balance at the end of the month, that balance will also be charged at the end of the month even if you have not yet reached your payment threshold. You will receive an emailed receipt for each successful payment.
You cannot manually change your payment threshold, and our support team will not change thresholds on behalf of advertisers.
Can I set a daily account spending limit?
Eligible postpaid-invoice ad accounts can set an account-wide daily spending limit in Ads Manager under Billing → Account limits, alongside the existing Date range option. This option is not available for self-serve card-billed advertisers.
The daily allowance is shared across campaigns, renews at midnight in the account’s time zone, and starts no earlier than the next day. Daily and date-range limits cannot overlap.
An account spending limit is a safeguard; it does not allocate spend between campaigns or pace delivery, and campaign budgets still apply. The card payment threshold described above is a charge trigger, not a daily spending limit. See Account spending limits for developer reference details.
If a payment fails
For self-serve card-billed accounts, if a payment fails after your account reaches its payment threshold, your ads may stop delivering until the billing issue is resolved. You will receive an email notification if that payment fails. If this happens, your campaigns, ad groups, and ads may show as Not serving. You can open the status tooltip for more details and update your payment method in Ads Manager Beta.
Eligible self-serve card-billed advertisers can move to higher payment thresholds over time based on successful payment history. Failed charges, disputes, and chargebacks can pause progression to higher limits.
Billing FAQ
Is my payment threshold the same as my campaign budget?
No. For self-serve card-billed accounts, your payment threshold controls when your saved payment method is charged for accrued spend. Your campaign budget controls how much the campaign can spend. Reaching a payment threshold does not mean a campaign has reached its budget, and a campaign budget is not the same as an account spend cap.
Can support increase or lower my payment threshold?
No. For self-serve card-billed accounts, payment thresholds are assigned and may increase automatically over time based on successful payment history and other factors. Support does not manually change thresholds for advertisers.
Why was I charged after adding a payment method?
When you add a card, your bank may show a temporary authorization hold, which may appear as the equivalent amount in your card’s currency. This is not a completed charge and is automatically released after verification, though it may remain visible for up to 8 days depending on your bank.
When you add a card, the expected hold amount will be reflected in the setup page, as well as in the Ads Billing page in Ads Manager.
Can I remove a payment method?
If self-serve removal is not available, make sure any outstanding balance is resolved and pause or end campaigns you do not want to continue. For help with account deactivation or payment method questions, contact ads-support@openai.com with your ad account ID and billing details.
Can I change my billing country, currency, or legal entity after setup?
Billing country, currency, and legal entity details are tied to account setup and billing records. They may not be self-serve editable after account creation. If the wrong details were entered, contact support with the ad account ID, current details, requested details, and reason for the change.
Can I use a credit card issued in a different country?
Your billing information and payment method should match the business entity and country or region used when your Ads Manager account was created.
For example, if your advertiser account was created for a U.S.-based business, you should use a U.S.-based billing address and payment method. A card or payment method associated with a different country may not be accepted.
If you need to bill under a different country, region, or legal entity, you may need to create a separate advertiser account using the correct business and billing information.
Why are my ads not serving after a failed payment?
Ads may stop delivering while a payment issue is unresolved. Check the campaign, ad group, and ad status tooltips for more detail. For self-serve card-billed accounts, update the payment method in Ads Manager Beta and confirm the saved card can be charged. Reach out to your card issuer for assistance if your payment method continues to fail. For eligible sales-managed accounts on postpaid invoice terms, follow your invoice billing arrangements instead.
Can I see charges after pausing a campaign?
Campaign updates may take time to apply across our ad delivery systems, so additional impressions, clicks, or spend may occur after a campaign is paused. In some cases, ads may continue to appear for up to 24 hours. Advertising costs incurred during this period remain billable.
Reporting and charges may also update after a pause or campaign end to reflect earlier ad activity. Reported spend may therefore change after delivery stops, but will not exceed the applicable budget limit.
What information can I include in my invoices?
You can add or update supported VAT and tax IDs directly in Ads Manager. Available tax ID types depend on your billing country.
- Open Billing → Settings.
- Select Edit next to Billing profile, if available. Some accounts show the tax ID fields in the form opened through Payment methods → Edit.
- Select the appropriate tax ID type, enter your number, and complete any other required fields.
- Save your changes, then confirm the tax ID appears under Billing profile.
Changes apply to future invoices and do not update invoices already issued.
Is Japanese Consumption Tax (JCT) charged on ChatGPT Ads invoices?
No. OpenAI does not currently charge Japanese Consumption Tax (JCT) on ChatGPT Ads invoices for advertisers billed in Japan, regardless of whether a Japanese tax ID is provided.
This treatment is specific to ChatGPT Ads and may differ from the general guidance in The Japanese Consumption Tax on your OpenAI invoices. For questions specifically about ChatGPT Ads invoices, refer to the information in this FAQ.
Note: OpenAI cannot provide tax advice. Contact your tax adviser with questions about JCT or any tax obligations that may apply to your business.
If you think a billing number is incorrect
Start by gathering the full context before reaching out to support at ads-support@openai.com.
A strong billing support request should include:
- Invoice ID or charge ID
- Date range in question
- Amount in question
- Affected campaign IDs
- Relevant reporting screenshots or exports

## Pull notes — mechanical only

- Pull date 2026-09-23, logged-out, no account. Main-text extraction drops navigation, footers and image content; images, charts and embedded posts are not captured.

# OpenAI — "Reimagining advertising with AI" (Sponsored Agents, HubSpot/Shopify integrations, prompt-driven Ads Manager)

```yaml
source:          OpenAI
url_or_doc_id:   https://openai.com/index/reimagining-advertising-with-ai/
published:       2026-09-16
pull_date:       2026-09-22
pull_method:     browser extension (openai.com is 403 to plain fetch per channels.md C1)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own docs/announcement
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full page (article body). Pointer trade item: PPC Land, "OpenAI lets advertisers run ChatGPT ads from HubSpot and Shopify," https://ppc.land/openai-lets-advertisers-run-chatgpt-ads-from-hubspot-and-shopify/, published 2026-09-17, read 2026-09-22 — primary reached, no separate pointer file filed.
```

## Verbatim

Title: "Reimagining advertising with AI" — dated September 16, 2026. Subhead: "Introducing new AI-powered experiences for ChatGPT Ads."

> "Today, we're introducing new AI-powered experiences to make ads more useful for people and advertising easier for businesses.
>
> We're testing Sponsored Agents, which let people start a conversation with a business-sponsored agent after clicking an ad in ChatGPT. We are making it easier to create ads by simply writing a few prompts in ChatGPT Work. At the same time, we are making Ads Manager more powerful with new AI creative tools. Finally, new integrations with HubSpot, our first CRM partner, and Shopify, our first ecommerce partner, are bringing ChatGPT Ads into the tools businesses already use.
>
> Throughout this work, our ads principles remain unchanged, and protecting the trust people place in ChatGPT remains our North Star."

### Sponsored Agents

> "Sponsored Agents give users the option to go deeper. After seeing a relevant ad, a user can choose to start a clearly labeled conversation with a business-sponsored agent in ChatGPT. The user can explain what matters to them, ask follow-up questions, and follow a link to the business's website when they're ready to take the next step. ... The conversation with a Sponsored Agent is distinct from ChatGPT's independent answers and separate from the original conversation that the user started in ChatGPT.
>
> Sponsored Agents are now being tested with select advertisers in the United States."

### Prompt-driven campaign management

> "Advertisers can now use simple, natural-language prompts to create, update, and analyze campaigns directly in ChatGPT with the Ads Manager plugin. They can turn a website or brief into a campaign, understand performance, and get recommendations on what to do next.
>
> We're also rolling out AI assistance directly into Ads Manager to help advertisers create ads. When drafting an ad, advertisers can now receive suggested copy and imagery based on their landing page and campaign objective. ... We're also launching the ability to opt into AI-powered text customization. If enabled, it adapts an advertiser's existing headlines and descriptions to better fit the context of a conversation and automatically translates ad copy to a user's preferred language."

### HubSpot and Shopify integrations

> "That's why we're integrating ChatGPT Ads into HubSpot and Shopify as our first CRM and ecommerce partners.
>
> Starting today, businesses managing their customers in HubSpot can connect a ChatGPT Ads account, create ads, track performance, and follow up on leads directly in HubSpot powered by their HubSpot context.
>
> Also available today, US-based Shopify merchants can use the new ChatGPT Ads app in the Shopify App Store to create and manage ChatGPT ad campaigns. Products are already integrated through Shopify Catalog, so merchants can start running these ads and tracking performance right away. The app will be available internationally in markets where ChatGPT Ads are available starting September 23."

Sign-up: "Businesses can sign up at ads.openai.com. Eligible businesses can also get started through the ChatGPT Ads for Shopify app or the ChatGPT Ads in HubSpot app."

Byline/author: "OpenAI". Topic tags shown on page: "2026", "ChatGPT". Related posts listed on page: "How to connect AI usage to business value" (Sep 16, 2026), "Now everyone can put data to work" (Sep 10, 2026), "Introducing ChatGPT for Financial Services" (Sep 10, 2026).

## Pull notes — mechanical only

- `openai.com/index/reimagining-advertising-with-ai/` returned HTTP 403 to plain fetch (`mcp__MCP_DOCKER__fetch`), consistent with channels.md C1 (`403→ext`). Loaded via the Chrome extension in a dedicated tab (tabId 1697684069) instead.
- No pricing, no specific Sponsored Agents pricing/eligibility criteria beyond "select advertisers in the United States" is stated on this page. A separate OpenAI Help Center page (already in `docs/raw/b-openai-sponsored-agents-2026-09-22.md` from Pass 2 cluster P2-c3) gives the alpha-access framing; this page is the newer September 16 product announcement that names the specific new HubSpot/Shopify integrations and prompt-driven Ads Manager tools not present in the earlier pull.
- A separate sign-up form page (`openai.com/form/sponsored-agents-hubspot/`) was found via search but not separately pulled — its content ("Advertisers may need to meet eligibility criteria to participate in the beta, including creative automation, automatic bidding, and a minimum daily ad spend for 28 days") is noted here as a pull note only, not quoted as verbatim primary text, since it was read only via a search-result snippet and not opened directly in this session.

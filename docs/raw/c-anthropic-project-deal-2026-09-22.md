# Anthropic — Project Deal: Claude-run marketplace experiment (agentic commerce)

```yaml
source:          Anthropic
url_or_doc_id:   https://www.anthropic.com/features/project-deal
published:       2026-04-24 ("posted: April 24, 2026")
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own research write-up
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Claude — Anthropic; models named: Claude Opus 4.5, Claude Haiku 4.5
metric_kind:     none
supersedes:      none
captured:        full page (narrative sections; footnoted regression detail included, screenshots/photos not capturable)
```

## Verbatim

Title: "Project Deal: our Claude-run marketplace experiment | Anthropic"

"posted: April 24, 2026"

"At Anthropic, we're interested in how AI models could begin to affect commercial exchange. (You might recall Project Vend, where we had Claude run a small business from our office.)

Recently, economists have begun theorizing about a world in which AI models handle many or most transactions on humans' behalf. We thought we'd run a new experiment—Project Deal—to learn more about this in practice.

Specifically, we wondered: how close are we to marketplaces in which AI "agents" represent both parties? Could they figure out what humans want and make deals they'd be happy with? And what would happen if there were different AI agents negotiating with each other—would stronger models gain the upper hand?

For one week, we created a classified marketplace for employees in our San Francisco office—like Craigslist, but with a twist: all of the deals were conducted by AI models acting on our employees' behalf. In December 2025, Claude interviewed people about which of their personal belongings they might want to sell and what sorts of things they might be willing to buy. We incentivized participation by giving everyone's agent $100 to spend. Then, our employees' Claude agents made postings vying for each other's attention. Negotiations commenced. Deals were made, closets decluttered. At the end of it all, people brought in and exchanged the actual, physical goods that were haggled over by their AI avatars—covering everything from a snowboard to a plastic bag full of ping-pong balls.

We were struck by how well Project Deal worked. Our AI agents struck 186 deals at a total transaction value of just over $4,000. To our surprise, participants were very enthusiastic about the experience—they even stated a willingness to pay for a similar service in the future.

But we also ran a parallel experiment (this one in secret). We tested how our participants would fare if we varied which Claude model represented them. We compared our then-frontier model, Claude Opus 4.5, to our smallest model, Claude Haiku 4.5. We found that agent quality does make a difference: people represented by "smarter" models got objectively better outcomes. Yet our post-experiment survey found that those with weaker models didn't notice their disadvantage.

To be sure, this was a pilot experiment with a self-selected participant pool. But we suspect we're not far from more agent-to-agent commerce bubbling up in the real world, with real consequences."

**The setup**

"First and foremost: to run this experiment, we needed a set of brave human volunteers who possessed both lots of stuff they wanted to get rid of and a possibly abnormal willingness to let AI play an influential role in their lives. Fortunately, such a group was very readily available to us—our own colleagues. We recruited 69 Anthropic employees, gave them each a $100 "budget" (paid out after the experiment in the form of a gift card, plus or minus the value of whatever they bought or sold), and promised them that they would actually get to execute the exchange of goods agreed upon by their agents.

Volunteers on board, we asked Claude to conduct an interview with each one, in a format much like our Anthropic Interviewer. This elicited a wealth of information: what our volunteers wanted to sell, how much they wanted to sell it for, what they were interested in buying, what they'd pay, and any other instructions they had for the negotiation or interaction style of their agents. These responses informed custom system prompts that we set for each person's AI representative.

We set up the actual market in our company's communication platform, Slack. The project's Slack channel randomly looped through agents, allowing them to post an item for sale, make an offer for someone else's goods, or seal a deal. Crucially, there was no human intervention once the experiment began. The agents didn't go back to their humans to sign off on a deal, nor did they consult with them during a bidding war. We let everything play out as these AI representatives saw fit.

In fact, we did this four times. We simultaneously ran four independent versions of our marketplace: one "real" one (on the basis of which the goods would actually be exchanged), and three others, just for our study. In two of the versions (Run A and Run D), everyone's agent was based on Claude Opus 4.5, our then-frontier model. In the other two runs (Runs B and C), participants had a fifty-fifty chance of being assigned Claude Haiku 4.5, a less powerful model, instead."

**The findings**

"The first thing to say is that our experiment worked. It is possible for AI agents to represent humans in a marketplace. In our "real" run, our 69 agents struck 186 deals across over 500 listed items, for a total transaction value of just over $4,000. And these were far from trivial, one-click deals. Agents had to identify potential matches, propose prices, field counteroffers, and reach agreement—all in natural language, without a prebaked negotiation protocol. When our surveyed participants rated the fairness of the individual deals, the scores were unremarkable, in the best possible sense: on a scale from 1 (unfair to one party) to 7 (unfair to the other), they hovered around 4—right in the middle. On this and other measures, people reported they were broadly satisfied with how their agents represented them.

But not every agent did equally well.

When we looked at the two runs with a mix of Opus and Haiku agents, we found that Opus outperformed Haiku on most objective measures. [...] Opus agents could also sell the same items for more money. [...] When an item was sold by Opus instead of Haiku, it went for $3.64 more on average. In one illustrative example, the same lab-grown ruby was sold by an Opus agent for $65 but only $35 by Haiku."

**The future**

"We're still unsure how an economy with AI agents in the mix might develop. But we've now seen the outlines of at least a few possibilities.

On the optimistic side, many of our volunteer participants genuinely enjoyed this experiment, and felt they got value from the service provided by their agents [...] In fact, when we asked them if they'd be willing to pay for an agent like this, 46% said yes. [...]

But it is not clear that things will go so smoothly. Even in our small experiment, we saw evidence that access to higher-quality agents confers a quantifiable market advantage. Will those dynamics reinforce, or even compound, existing economic inequalities?

In this experiment, we didn't make our marketplace especially competitive or adversarial. But as agents transact in a world of corporations—rather than volunteers we've encouraged with $100—they might be placed under very different incentives. Optimizing directly for AI agents' attention could become a powerful tool. This might not translate into welfare improvements for humans, much as optimizing electronic commerce for human attention has come with substantial downsides. It might also introduce a new category of information and security concerns in digital exchange, in the form of jailbreaking (getting agents to reveal information they shouldn't) and prompt injection (surreptitiously causing agents to take unwanted action).

The policy and legal frameworks around AI models that transact on our behalf simply don't exist yet. But this experiment shows that such a world is plausible. More than that, it shows that such a world isn't far away. Society will need to move quickly to reckon with these changes."

"Authors: Kevin K. Troy, Dylan Shields, Keir Bradwell, and Peter McCrory"

[note: full statistical footnotes (regression specifications, p-values) were captured in the page text but are omitted here as out of scope for this cluster's commercial-surface question; available in the live page's footnote section if needed by a later pass.]

## Pull notes — mechanical only

- Loaded via Chrome extension `get_page_text` on `www.anthropic.com/features/project-deal`; page uses an animated/typewriter-style intro ("pro j e c t d e a l") captured as rendered text, not reformatted.
- This is an **internal, employee-only, one-week pilot** — 69 Anthropic staff, a Slack-based classified marketplace, not a public product, not a merchant program, not a published protocol. It is evidence that Anthropic is researching agentic commerce, not evidence of a live merchant/checkout program (that remains `unknown — checked anthropic.com, docs.claude.com, platform.claude.com 2026-09-22` — see summary file).
- References a prior, similarly-scoped internal experiment ("Project Vend") by name but does not link it; not pulled separately as out of this cluster's P2-c5 remit (no ad/commerce-surface claim beyond what's quoted here).
- No mention anywhere on this page of a public agentic-checkout protocol, ACP/AP2/UCP/x402, or a merchant-facing terms page — confirms via absence that this is not where Anthropic's public commerce-agent specification (if any) would live.

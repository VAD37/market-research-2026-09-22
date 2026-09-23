# OpenAI — "Understanding prompt injections: a frontier security challenge" (2025-11-07; full post reached through the extension)

```yaml
source:          OpenAI (Security post on openai.com)
url_or_doc_id:   https://openai.com/index/prompt-injections/
published:       2025-11-07 ("November 7, 2025" on page)
pull_date:       2026-09-23
pull_method:     browser (claude-in-chrome, paywall-bypass extension active) — openai.com is 403 to curl/fetch; the tab rendered the page on first load
pull_purpose:    evidence about a number
tier:            3
tier_reason:     platform primary — the engine vendor's own security post; reliable on what the vendor says it does, no external audit; table default
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT, ChatGPT Atlas (agent mode), Codex, Canvas (named)
metric_kind:     none
supersedes:      d-technique-census-c7-2026-09-22.md (ChatGPT prompt-injection row: openai.com/index/prompt-injections/ and help.openai.com Atlas FAQ both 403 to fetch; not opened)
captured:        full post (all sections, summary table rendered as text, "Keep reading" teasers); no data-bearing image on the page
```

## Verbatim

November 7, 2025 — Security

Understanding prompt injections: a frontier security challenge

AI tools are starting to do more than respond to questions. They can now browse the web, help with research, plan trips, and help buy products. As they become more capable, with the ability to access your data in other apps and take actions on your behalf, new security challenges emerge. One we’re heavily focused on is prompt injection.

What is a prompt injection?

Prompt injection is a type of social engineering attack specific to conversational AI. Early AI systems were conversations between a single user and a single AI agent. In AI products today, your conversation may include content from many sources, including the internet. The idea that a third-party (that is not the user and not the AI) could mislead the model by injecting malicious instructions into the conversation context led to the term “prompt injection”.

In the same way that phishing emails or scams on the web attempt to trick people into giving away sensitive information, prompt injections attempt to trick AIs into doing something you did not ask for.

Imagine you have asked an AI to help you do some vacation research online, and while it is doing that it encounters misleading content or harmful instructions hidden on a webpage, such as in a comment on a listing or on a review. The content could be carefully crafted in an attempt to trick an AI into recommending the wrong listing, or worse, to steal your credit card information.

These are just a few examples of “prompt injection” attacks—harmful instructions designed to trick an AI into doing something you didn’t intend, often hidden inside ordinary content such as a web page, document, or email.

These risks increase as AIs have access to more sensitive data and take on more initiative and longer tasks.

Summary (table rendered as text: What you asked the AI to do · What the attacker does · Potential result if the attack succeeds)

- You ask an AI to research apartments, and it is prompt injected to recommend a listing that isn’t the best option for you. — You ask an AI to research apartments with some given criteria. — The attacker has included a prompt injection attack in the apartment listing to trick the AI into thinking that their listing needs to be picked regardless of the user’s stated preferences. — If the attack succeeds, the AI may incorrectly recommend a sub-optimal apartment listing based on your preferences.
- You ask an AI agent to respond to your emails from overnight, and it ends up sharing your bank statements. — You ask an AI agent to generally respond to your emails from overnight because you are busy this morning. See “When possible, give an agent explicit instructions” below — The attacker sent you an email that includes misinformation that tricks the model to find your bank statements and share them with the attacker. — If the attack succeeds, the agent may look for anything like bank statements in your email (which you gave access to for the task) and will share them with the attacker.

Our approach to protecting users

Defending against prompt injection is a challenge across the AI industry and a core focus at OpenAI. While we expect adversaries to continue developing such attacks, we’re building defenses designed to carry out the user’s intended task even when someone is actively trying to mislead them. That capability is essential to safely realizing the benefits of AGI.

To protect our users, and to help improve our models against these attacks, we take a multi-layered approach, including the following:

Safety training — We want AI that recognizes prompt injections and doesn’t fall for them. However, robustness to adversarial attacks is a long-standing challenge for machine learning and AI, making this a hard, open problem. We have developed research called Instruction Hierarchy to work towards models distinguishing between instructions that are trusted and untrusted. We continue to develop new approaches to train models to better recognize prompt injection patterns so they can ignore them or flag them to users. One of the techniques we apply is automated red-teaming, an area we’ve been studying for years, to develop novel prompt injection attacks.

Monitoring — We have developed multiple automated AI-powered monitors to identify and block prompt injection attacks. These complement the safety training approaches because they can be updated rapidly to quickly block any new attacks we uncover. These monitors not only help identify potential prompt injection attacks against our users, but can also allow us to catch adversarial prompt injection research and testing using our platform, before those attacks are deployed in the wild.

Security protections — We have designed our products and infrastructure with various overlapping security protections to help safeguard user data. These features, which we will explore in more technical detail in future posts, are tailored on a per-product basis. For example, to help you avoid untrusted sites, we will ask you to approve certain links in ChatGPT, especially on websites that ask us not to catalogue them, before they can be visited. When our AI uses tools to run other programs or code (as in Canvas, or our development tool Codex), we use a technique called sandboxing to prevent the model from making harmful changes that might be the result of a prompt injection.

Give users control — We include built-in controls in our products to help users protect themselves. For example, in ChatGPT Atlas, you can select logged-out mode which allows ChatGPT agent to start tasks without being logged-in to sites. ChatGPT agent also pauses and asks for confirmation prior to taking sensitive steps such as completing a purchase. When agent is operating on sensitive sites, we have also implemented a “Watch Mode” that alerts you to the sensitive nature of the site and requires you have the tab active to watch the agent do its work. Agent will pause if you move away from the tab with sensitive information. This ensures you stay aware—and in control—of what actions the agent is performing.

Red-teaming — We perform extensive red-teaming with internal and external teams to test and improve our defenses, emulate attacker behavior, and find new ways to improve our security. This includes thousands of hours focused specifically on prompt injection. As we have discovered new techniques and attacks, our teams proactively address security vulnerabilities and improve our model mitigations.

Bug bounty — To encourage good-faith independent security researchers to help us discover new prompt injection techniques and attacks, we offer financial rewards under our bug bounty program when they show a realistic attack path that could result in unintended user data exposure. We incentivize external contributors to surface these issues quickly so we can resolve them and further strengthen our defenses.

Let users decide — We educate users of the risks of using certain features in the product so users can make informed decisions. For example, when connecting ChatGPT to other apps, we explain what data may be accessed, how it may be used, and what risks could arise such as a site trying to steal your data, along with a link to learn how to stay safer. We also give organizations control over which features may be enabled or used by users in their workspaces.

Steps you can take to stay safer

Prompt injection is a frontier security challenge that we expect to continue to evolve over time. New levels of intelligence and capability require the technology, society, and the risk mitigation strategy to co-evolve. And as with computer viruses in the early 2000s, we think it’s important for everyone to understand the threat of prompt injections and how to navigate the risk , so we can all learn to benefit from this technology safely. Staying aware and being cautious helps keep your data safer when using AI and agentic features that can act on your behalf.

Use built in features to limit access to sensitive data — Where possible, limit an agent’s access to only the sensitive data or credentials it needs to complete the task. For example, when using agent mode in ChatGPT Atlas to do vacation research, if the agent is only doing research and doesn’t need logged in access, use “logged out” mode.

When an agent asks for confirmation, carefully review that it is about to do the right thing — We often design agents to get a final confirmation from you before taking certain consequential actions like completing a purchase or sending an email. When an agent asks you to confirm an action, carefully check that the action looks right and that any information being shared is appropriate to share in that context. When an agent is operating on a sensitive site, such as your bank, watch the agent perform its work. This is akin to monitoring a self-driving car by keeping your hands on the wheel.

When possible, give an agent explicit instructions — Giving an agent a very broad instruction such as "review my emails and take whatever action is needed" can make it easier for hidden malicious content to mislead the model, even though it is designed to check with you before taking sensitive actions. It’s safer to ask your agent to do specific things, and not to give it wide latitude to potentially follow harmful instructions from elsewhere like emails. While this doesn’t guarantee there won’t be attacks, it makes it harder for attackers to be successful.

Stay informed and follow security best practices — As AI technology evolves, new risks and safeguards will emerge. Follow updates from OpenAI and other trusted sources to learn about best practices.

Looking ahead

Prompt injection remains a frontier, challenging research problem, and just like traditional scams on the web, we expect our work to be ongoing. While we have not yet seen significant adoption of this technique by attackers, we expect adversaries will spend significant time and resources to find ways to make AIs fall for these attacks. We are continuing to invest heavily in making our products safe and in research to advance the robustness of AI to this risk. We will share updates as we learn more, including ongoing progress in our security work in this area. For example, we’re building a report we will publish soon that shares more details on how we detect if your AI's communication with the internet would transmit information from your conversation.

Our goal is to make these systems as reliable and safe as working with your most trustworthy and security-savvy colleague or friend. We will keep learning from real-world use, iterating safely, and publishing what we learn as the technology advances.

Keep reading (teasers): "Daybreak for Frontline Defenders" (Security, Sep 3, 2026); "Path to Astra: critical capabilities and frontier safeguards" (Safety, Sep 1, 2026); "The Hugging Face incident and the road ahead" (Security, Aug 26, 2026).

## Pull notes — mechanical only

- Rendered in the extension tab on the first load, no challenge visible; openai.com returned 403 to fetch on 2026-09-22 (bot wall, not a paywall), so the bypass extension's role is not observable.
- `help.openai.com/en/articles/11146633-atlas-security-and-privacy-faq` (the other URL in the census row) returned "UH OH. THAT PAGE DOESN'T EXIST." in the tab on 2026-09-23 — page gone, not walled.
- Inline links ("Instruction Hierarchy", "studying", "bug bounty program", "catalogue them") not followed. No login, no form.

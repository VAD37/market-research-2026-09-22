# Muck Rack — Pricing page (reached through the extension; no list prices)

```yaml
source:          Muck Rack (muckrack.com)
url_or_doc_id:   https://muckrack.com/pricing
published:       undated — no date on page
pull_date:       2026-09-23
pull_method:     browser (claude-in-chrome, paywall-bypass extension active)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     platform primary — pricing page; table default
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          n/a ("leading LLMs" for Generative Pulse)
metric_kind:     none
supersedes:      a-muckrack-pricing-2026-09-22.md (Cloudflare bot wall, nothing captured)
captured:        full page text (plan matrix, add-ons, FAQ question list, customer quotes)
verbatim:        full
```

## Verbatim

"Pricing — Simple, transparent pricing for PR teams shaping today’s media narrative." "Talk to our team". Toggle: "Brands | Agencies".

Plans: "Starter (basic access) — Individuals — Contact us" · "Standard (most popular) — Most PR teams — Contact us" · "Premier (most flexible) — Enterprises and advanced teams — Contact us". No dollar figure appears anywhere on the page.

Feature matrix rows (row labels as listed): Media Monitoring & Alerts — Search online articles; Alerts via email & Slack; Podcast monitoring; Curation Engine; Newsjacking Opportunities. Media Database & Pitching — AI Visibility Badges; Search people & outlets; Build and manage media lists; Pitching including email integrations and PressPal.ai; AI-powered journalist recommendations; Inbound media manager; Media list exports ("Limited" on one tier). Reporting & Analytics — Sentiment Analysis ("NLP", "NLP", "AI-Powered"); Automatic tagging of themes, spokespeople & more; Coverage Reports ("Starter pack", "Standard pack", "Premier pack"); Dashboards ("Template only", "Template only", "Custom"); Interactive Presentations; Customizable PR Hit Score; Newsletters; Google Analytics Integration; Generative Pulse. Onboarding & Customer Support — Onboarding ("Self-led", "Instructor-led", "Instructor-led"); Customer Success ("Pooled", "Named", "Named"); Live chat support (tier-specific target response times); Help Center; Online training & certifications.

Add-ons: Print & Broadcast Monitoring; Social Listening; Press Release Distribution; Muck Rack API ("Available for Premier customers"); Media Intelligence; Generative Pulse:

> Generative Pulse — Track visibility, sentiment, and trends across leading LLMs—and see which journalists and sources shape those responses. Use these insights to strengthen credibility, guide outreach, and future-proof your communications strategy.

FAQ questions (answers collapsed, not rendered in text): "Who uses Muck Rack?" · "How does Muck Rack’s pricing work?" · "Is Muck Rack an all-in-one solution?" · "What happens on the demo?" · "Is Muck Rack free?" · "Why doesn’t Muck Rack list its pricing publicly?" · "Is Muck Rack too expensive for small teams or solo practitioners?" · "Do journalists have to pay to be on Muck Rack?" · "Is Muck Rack a full PR Suite?" · "Can Muck Rack replace all other PR tools we’re using?"

Customer quotes: Zapier (Steph Donily), Patagonia (Tessa Byars), University of Arizona (Nick Prevenas), Penguin Random House (Emily Reardon), Taco Bell (Matt Prince), Mark Cuban Companies (Mark Cuban).

## Pull notes — mechanical only

- curl with the bot user agent: HTTP 403 (Cloudflare). The extension tab rendered the page with no challenge shown; the bypass extension's role is not observable (Cloudflare bot wall, not a paywall).
- Generative Pulse appears twice: as a matrix row (tier availability marks are icons, not captured as text) and as an add-on. No price or price delta for it or any plan; the FAQ item "Why doesn’t Muck Rack list its pricing publicly?" was not expanded (would require clicking; not a form).
- No login, no form.

# Glossy — Sephora AI Beauty Chat / Smart Skin Scan conversion figures

```yaml
source:          Glossy (glossy.co)
url_or_doc_id:   https://www.glossy.co/beauty/sephora-is-bringing-prestige-beauty-shopping-into-googles-ai-ecosystem/
published:       2026-06-03
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     beauty trade press pointer per task brief (Glossy named as tier-5 pointer outlet); figures are company-stated by a Sephora executive at a conference, relayed by the trade press, not an independently published Sephora report — no primary Sephora page with these figures was found this pull
source_label:    company-stated
lane:            E, F
sub_market:      organic recommendation, agentic commerce
engine:          ChatGPT, Claude (named, context); Google Agentic Checkout (named, the specific integration); Sephora's own "AI Beauty Chat" and "Smart Skin Scan" (proprietary, not a third-party assistant)
metric_kind:     sales (same-day purchase rate after chat use), traffic-adjacent (diagnostic completion rate)
vertical:        skincare and beauty — skin-care diagnostics and "beauty" broadly (source's own frame)
supersedes:      none
captured:        full article text (per WebFetch extraction)
```

## Verbatim

Headline: "Sephora is bringing prestige beauty shopping into Google's AI ecosystem"
Byline: Zofia Zwieglinska. Published: Jun 3, 2026.

"Sephora has long been known for its in-store beauty advisors, product discovery and loyalty-driven personalization. But as more consumers start their shopping journeys inside AI-powered platforms like ChatGPT and Claude, the retailer is moving to bring that same beauty expertise into new digital environments.

This week, Sephora announced an expanded partnership with Google, becoming the first prestige beauty retailer to enable shopping directly within Google's AI-powered platform through Google Agentic Checkout. [...]

'We really see that these LLMs are where consumers are now starting their discovery journey, and so we want to be where the consumer is,' said Nadine Graham, gm of e-commerce at Sephora North America, speaking at the Glossy E-Commerce Summit in Miami on Tuesday. [...]

Sephora currently has 80 million active Beauty Insider members worldwide [...]

The company's in-store Beauty Skin Scan tool which launched in 2021 [...] uses AI to match clients with complexion and skin-care products after three facial scans. Sephora completed more than 180,000 scans per month on average last year, and the tool continues to see high engagement this year, Graham said.

[...] Online, Sephora is trying to replicate parts of that guided experience. Its Smart Skin Scan on the Sephora app lets users upload a selfie, receive an AI diagnostic and get a curated four-step product routine. Graham said more than 80% of consumers who start the diagnostic complete it, and those who add products to basket convert and spend at higher rates. Sephora's AI Beauty Chat, meanwhile, is designed to narrow down the assortment, answer product questions and drive purchases within the chat. More than 20% of consumers who use the chat make a purchase the same day, Graham said."

## Evidence-bar check — seven items, ticked individually

1. Brand: **yes** — Sephora, named
2. Engine(s): **partial** — the "80%" and "20%" figures are about Sephora's own proprietary tools (Smart Skin Scan, AI Beauty Chat), not a third-party AI assistant; ChatGPT/Claude and Google Agentic Checkout are named elsewhere in the article as context, not as the engine behind these two figures
3. Absolute date window: **no** — "last year" and "this year" only, no dates
4. Baseline: **no** — no pre-tool comparison given
5. Intervention: **yes** — Smart Skin Scan and AI Beauty Chat, named tools
6. Sample size / traffic volume: **no** — both "80%" and "20%" carry no base count (trust-rubric.md discard-on-sight: percentage with no base); "convert and spend at higher rates" names no rate at all
7. Who measured, paid by outcome: **partial** — self-stated by Sephora's own GM of e-commerce (Nadine Graham) at a public conference; no independent measurement or method disclosed; paid-by-outcome n/a (no third-party vendor named for these two figures)

**Grade: Fools gold** (sales/conversion-adjacent claim, no baseline, no control, and the two headline percentages carry no base — per grading rule 1, missing items 3, 4, 6 fully and item 2 partially caps this below Bronze once the revenue/conversion framing is counted; graded Fools gold consistent with `e-case-census-c4-2026-09-22.md`'s treatment of same-shape claims, e.g. Profound/Plaid's "+210% conversions"). Direction: **positive** (self-reported). `paid_by_outcome: n/a — proprietary Sephora tools, no third-party vendor named for this specific claim`.

**Caveat on scope:** the two graded figures (80% diagnostic completion, 20% same-day purchase after chat) describe Sephora's own on-site AI tools, not visibility or referral traffic from a third-party AI assistant (ChatGPT, Gemini, etc.). They are included here because the task brief's scope covers "AI-attributed sales for a skincare/beauty brand" broadly and the article frames both tools as part of Sephora's response to "AI search and conversational commerce reshap[ing] product discovery" — but a reader should not treat this as evidence of third-party-engine referral performance.

## Pull notes — mechanical only

- Fetched via WebFetch, full-page prompt extraction.
- No Sephora-own primary page (investor release, newsroom item) with these two figures was located this pull; Sephora is part of LVMH (Paris-listed, not a US SEC filer), so no EDGAR route exists for independent corroboration.

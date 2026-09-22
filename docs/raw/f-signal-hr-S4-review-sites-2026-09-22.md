# G2, Capterra, OMR — S4 review-site velocity, reviewer industry financial services / insurance / health

```yaml
source:          G2 (g2.com), Capterra (capterra.com), OMR Reviews (omr.com)
url_or_doc_id:   https://www.g2.com/categories/ai-search-visibility ; https://www.capterra.com/generative-engine-optimization-software/ ; https://omr.com/en/reviews/category/ai
published:       n/a — access-path record for G2/Capterra; OMR page as served 2026-09-22
pull_date:       2026-09-22
pull_method:     fetch (direct curl, no browser extension)
pull_purpose:    evidence about a number (OMR); evidence about category noise (G2/Capterra access record)
tier:            n/a for G2/Capterra (nothing retrieved); 5 for OMR per `channels.md` C65 (DACH B2B review corpus, own GEO-adjacent category criteria — table default)
tier_reason:     OMR's page mixes a general "AI tools" category (not a dedicated GEO/AI-visibility category) with vendor cards; the one relevant vendor found is adjacent, not a confirmed AI-visibility/GEO tool — see below
source_label:    vendor-reported (OMR vendor cards are self-submitted profiles per OMR's own model)
lane:            A, E
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP status only for G2 and Capterra; OMR's `/en/reviews/category/ai` page, full fetched HTML (1,000,097 bytes) grepped for finance/insurance/health terms
vertical:        high-CPA regulated — searching for a reviewer-side (buyer-side) industry tag of financial services, insurance, or health on an AI-visibility/GEO vendor's review corpus
cell:            unattributed — no reviewer-industry breakdown reached
query:           direct fetch of the three URLs above; grep of the OMR page body for `financ|insuranc|versicherung|finanz|gesundheit|health` (case-insensitive)
```

## G2 and Capterra — access blocked

| Channel | URL | Result |
|---|---|---|
| G2, AI-search-visibility category | `g2.com/categories/ai-search-visibility` | **403** (1,706-byte challenge response) |
| Capterra, GEO software category | `capterra.com/generative-engine-optimization-software/` | **403** (5,511-byte challenge response) |

Both confirm `channels.md` C36 and C37's recorded expectation (`403→ext`) on this agent's fetch-only access, 2026-09-22. No reviewer-industry filter (financial services / insurance / health) could be checked on either site this pull — recorded as a **browser backlog** item.

## OMR — reachable, general-category page checked

`omr.com/en/reviews/category/ai` returned HTTP 200. This is OMR's general "AI" review category, not a dedicated GEO/AI-visibility category (no such dedicated OMR category page was located this pull; `channels.md` C65 cites this same URL as its AI-visibility channel).

Grepping the page body for `financ`, `insuranc`, `versicherung`, `finanz`, `gesundheit`, `health` (case-insensitive) surfaced one vendor card with relevant text:

> **LoyJoy** — a conversational-AI/chatbot platform, not confirmed as a GEO/AI-visibility tool in the sense this repo tracks (brand appearing inside a third-party AI assistant's answer). Its OMR card names: "**Security for Regulated Markets (Enterprise...**", references to "**DORA**" (the EU's Digital Operational Resilience Act, a financial-sector regulation) and "the European Accessibility Act (BFSG/EAA)", and states: "Since 2018, more than 100 large enterprises, including **R+V Insurance**, TRUMPF, Vaillant, Melitta, and Deutsche Telekom—have trusted LoyJoy."

R+V Insurance (a German insurer) is named as a customer of LoyJoy, and LoyJoy's own copy names DORA (financial-sector regulatory compliance) as a selling point. **This is recorded but not counted as a qualifying S4 hit**: LoyJoy's own positioning ("conversational AI", "customer service", chatbot/resolution flows — "Whether it's an insurance claim, appointment booking, or product consultation—your customers receive immediate results instead of just information") describes a customer-service chatbot product, not a tool that measures or improves brand visibility inside third-party AI assistants (the sub-market this repo tracks per `glossary.md`). It is filed here as an adjacent finding, not as evidence for the S4 signal.

No dedicated GEO/AI-visibility vendor card with a reviewer-industry tag of financial services, insurance, or health was found on the page reached.

## Result

**`none — checked g2.com (403→ext), capterra.com (403→ext), omr.com/en/reviews/category/ai (200, general AI category, no GEO-specific reviewer-industry breakdown found) 2026-09-22`** for S4 in the high-CPA regulated vertical.

## Caveats

- The G2 and Capterra blocks are the same access limitation recorded by `channels.md` (C36, C37) and by `f-agency-census-c5-2026-09-22.md`'s discovery log ("Crunchbase ... 403" and DDG rate-limiting) — this agent holds no Chrome extension slot per task scope, so the block is recorded, not worked around.
- OMR's own dedicated GEO/AI-visibility category page (if one exists distinct from the general "AI" category cited by `channels.md` C65) was not located this pull; only the URL `channels.md` itself cites was checked.
- LoyJoy's R+V Insurance customer relationship and DORA-compliance framing are recorded as a genuinely-found, on-the-page fact (source: OMR vendor card, company-stated/vendor-reported), but are explicitly separated from this file's S4 conclusion because LoyJoy's product category does not clearly match this repo's "AI-visibility tool" definition.

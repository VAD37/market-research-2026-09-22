"""Generate docs/findings/director-brief-2026-09-23-r2.pptx.

Reads nothing but its own inline content, which mirrors the tables and key
lines of docs/findings/director-brief-2026-09-23-r2.md (snapshot c1e632c).
Every number here is also in that file. The .pptx is a generated file: never
hand-edit it; fix this script and re-run.

Run from anywhere:  python docs/method/gen-director-deck-r2.py
Needs: python-pptx.
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

OUT = Path(__file__).resolve().parents[1] / "findings" / "director-brief-2026-09-23-r2.pptx"

DARK = RGBColor(0x1F, 0x2A, 0x44)
ACCENT = RGBColor(0x0E, 0x7C, 0x86)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BODY = RGBColor(0x22, 0x22, 0x22)
GREY = RGBColor(0x6B, 0x6B, 0x6B)
ROW_ALT = RGBColor(0xF2, 0xF5, 0xF7)

FOOTER = "Research only — evidence, not a verdict. Snapshot c1e632c, 2026-09-23."
SOURCE = "Source: docs/findings/director-brief-2026-09-23-r2.md"

W, H = Inches(13.333), Inches(7.5)

# ---------------------------------------------------------------- content

SLIDES = [
    {
        "kind": "title",
        "title": "Demand for brand visibility inside AI assistants",
        "subtitle": "Director brief r2 · file date 2026-09-23 · snapshot c1e632c · long form of the executive brief r2",
        "lines": [
            "Passes 0–9, 11–14 done; Pass 16 research complete; Pass 10 skipped by owner 2026-09-23; Pass 15 not run",
            "All 32 hypotheses · all six lanes · compiled files only · 0 pulls for this deck",
        ],
    },
    {
        "kind": "bullets",
        "title": "Agenda",
        "bullets": [
            "The question, and what the evidence supports",
            "Why now: dated triggers",
            "The market: size three ways, paid inventory, prices, sub-markets side by side",
            "Demand: 27 core cells (both readings), local, EU, brand accuracy",
            "Evidence quality: three-counts, negative tail beside positives",
            "Hypotheses (32) · ranked risks · programme-done rows",
            "What the evidence does not show · questions only the owner can answer · caveats",
        ],
    },
    {
        "kind": "bullets",
        "title": "The question, and what the evidence supports",
        "quote": "Which segments show real-world demand for visibility and recommendation inside AI assistants, "
                 "what evidence shows it works, and what did brands that moved actually change?",
        "bullets": [
            "Demand: 8 of 27 core cells read spend under both readings (strict 8/1/17/1; loose 8/1/18/0); mostly enterprise organic; on job postings",
            "Price paid: unknown in 27 of 27 cells and 9 local cells; no buyer discloses one",
            "Paid: live on four engines; OpenAI \"$1 billion\" run rate; 0 of 8 engines publish a rate card",
            "Proof: 0 Gold in ~980 + ~1,640 screened; Silver 7 grade_raw / 1 grade_rule1 (+4 / +1); two highest-tier Silvers negative or null",
            "Change: content ops 63, stack 58, paid media 2 of 108; 37 name an action with no measured outcome",
            "Size: none measured; forecasts disagree 1.92× (organic 2034) to 26.3× (agentic 2030)",
            "The evidence stops at correlation and self-report; whether any of it pays is shown by no document",
        ],
    },
    {
        "kind": "table",
        "title": "Why now: 8 of 54 dated triggers (26 at tier 2, 24 at tier 3)",
        "cols": ["Date", "Event", "Tier, label"],
        "widths": [1.5, 8.8, 2.0],
        "rows": [
            ["2026-02-04", "\"Claude will remain ad-free\"; no third-party product placements", "3, company-stated"],
            ["2026-02-09", "ChatGPT Ads live, US pilot; WPP, Omnicom, dentsu statements", "3, company-stated"],
            ["2026-02-25", "NerdWallet 8-K: cards revenue \"decreased 24%\", \"AI overviews and LLMs\"", "2, filed"],
            ["2026-04-28", "Semrush merger into Adobe completed, \"$12.00/share cash\"; AP2 \"donated to FIDO\"", "2 filed; 3"],
            ["2026-06-17", "CMA fair-ranking conduct requirement, \"search generative AI features\"", "2, filed"],
            ["2026-08-31", "ChatGPT designated VLOSE, 159.1M EU recipients; ChatGPT Ads \"$1 billion... run rate\"", "2 filed; 3"],
            ["2026-09-17", "ECF 1977-1: Microsoft \"83-93% drops in click-through rates\"", "2, filed"],
            ["2027-01", "ChatGPT DSA obligations \"start applying in January 2027\" (compliance window, not a forecast)", "2, filed"],
        ],
    },
    {
        "kind": "table",
        "title": "Market size three ways: no measured size exists",
        "key": "Floors and forecasts are never sizes. 18 published figures: 15 forecasts, 0 sizes; 10 further forecasts 2026-09-23.",
        "cols": ["Way", "Organic", "Paid", "Agentic"],
        "widths": [2.2, 3.7, 3.4, 3.0],
        "rows": [
            ["Bottom-up floor", "$42.2M–$48.2M + €2.2M ARR, 4 vendors (filed 2 / stated 5); $5.3M–$35.2M price × count (5) beside", "≥ $1B run rate, one engine (3); 0.45% of Google Search & other FY2025, bases differ", "unknown — checked six owners 2026-09-23; Rufus \"nearly $12 billion\" adjacent (3)"],
            ["Engine reach", "ChatGPT \">1 billion\" WAU; Gemini app 950M MAU; AIO 2.5B; AI Mode 1B MAU; Grok 117M (filed)", "ChatGPT WAU 700M → >1B; AIO 2B → 2.5B", "Rufus 250M → \"300 million+\" customers 2025"],
            ["Forecasts (never sizes)", "2034: $17.15B–$32.92B, 1.92×, tier 6", "2030: ~$5B–$100B+, ~20×, scopes differ, tier 5", "2030: $190B–$5T, 26.3×, tier 5–6; \"roughly 35×\" 2029–30 beside"],
            ["Ad baselines, filed (USD M)", "Google Search & other \"$ 224,532\" FY2025", "Microsoft search \"15,176\" FY2026; Amazon ads \"68,635\" FY2025; Meta \"$ 196,175\"", "AI-surface ad line in any filer: none stated"],
        ],
    },
    {
        "kind": "table",
        "title": "Paid inventory and every price published",
        "key": "\"0 of 8 publish a rate card\". Four engines live; Claude refuses; Perplexity winding down (tier 5).",
        "cols": ["Item", "Figure, verbatim where quoted", "Tier"],
        "widths": [3.0, 8.5, 0.8],
        "rows": [
            ["ChatGPT", "live from 2026-02-09; \"over 40 countries\"; 31 EU markets; \"tens of thousands of advertisers\" vs panels 820–7,378", "3; 5"],
            ["Google", "AI Overviews live, campaigns auto-eligible, \"you can't opt out\"; AI Mode testing; Gemini app none", "3"],
            ["Copilot; Amazon", "live via Microsoft auction; Rufus / Alexa prompts GA US 2026-03-25, CPC", "3"],
            ["OpenAI price points", "\"$3–$5 USD per click\" max bid; min \"25 USD\"/day; launch \"$60\" CPM, minimum removed 2026-05-05 (5)", "3; 5"],
            ["ChatGPT ad presence", "0.8% (launch) · 4.47% US (Mar–May) · 26% US desktop (Jun) · 0.00% of 169,560 UK — not reconciled", "5"],
            ["Organic tools", "\"$20–$999/month self-serve\", 14 of 34 disclose; Semrush delta \"+$60/mo\"", "3"],
            ["Agentic fees", "Copilot Checkout 0%; Instant Checkout \"a small fee\", rate undisclosed; 6 of 6 protocol fee clauses unknown", "3"],
            ["Publisher side", "Cloudflare \"$0.001 USD per crawl\" floor; ProRata \"50% of revenues\"; Reddit \"Other revenue\" $43,280K Q2 2026 (2)", "3; 2"],
        ],
    },
    {
        "kind": "table",
        "title": "Sub-markets side by side: no choice made",
        "cols": ["Sub-market", "Demand, 9 cells strict — loose", "Best proof", "Supply, disclosure", "Risk ranks"],
        "widths": [2.0, 2.6, 3.0, 3.6, 1.1],
        "rows": [
            ["Organic recommendation", "6 / 1 / 1 / 1 — 6 / 1 / 2 / 0", "0 Gold; Silver 7 grade_raw / 1 grade_rule1", "34 rostered; price 14 of 34; funding 8 of 34; filed revenue 2 of 34", "1, 3–7, 10, 11"],
            ["Paid placement", "1 / 0 / 8 / 0 — same", "Fools gold; 15 screened, 0 cleared", "5 of 8 engines live; 0 of 8 rate card; 1 of 8 revenue", "2, 4–8, 11"],
            ["Agentic commerce", "1 / 0 / 8 / 0 — same", "none graded; 22 \"screened — not opened\"", "4 programs live; fee 1 of 4; protocol fees 0 of 6", "4, 5, 6, 9, 11"],
        ],
    },
    {
        "kind": "table",
        "title": "Demand: 27 core cells, both readings, plus the wider cuts",
        "key": "Willingness to pay: unknown in 27 of 27 and 9 of 9 local cells. Budget line: unknown — checked in all three verticals.",
        "cols": ["Cut", "spend", "attention", "none — checked", "blank / other"],
        "widths": [4.2, 1.5, 1.7, 2.5, 2.4],
        "rows": [
            ["27 cells, strict (2026-09-23)", "8", "1", "17", "1 (skincare Organic / Mid)"],
            ["27 cells, loose (2026-09-23)", "8", "1", "18", "0"],
            ["27 cells, 2026-09-22 read, beside", "7", "1", "11", "8"],
            ["Local / multi-location, 9 cells", "1", "3", "5", "0"],
            ["EU, 45 cells (UK, FR, ES, IT, NL)", "2", "0", "41", "4 unassigned"],
            ["S13 brand accuracy, 27 cells", "0", "0", "27", "—"],
            ["By sub-market, spend cells", "organic 6 / paid 1 / agentic 1", "—", "—", "SMB spend cell 1 of 9"],
        ],
    },
    {
        "kind": "bullets",
        "title": "Demand: where the signals rest",
        "bullets": [
            "6 of 7 spend cells rest on S1 job postings (2026-09-22), the catalogue's weakest spend class; the eighth cell (high-CPA Organic / Mid-market) is S1 too",
            "Skincare Agentic / Enterprise reads spend in the customers file and attention in the agentic market file — both stand",
            "One filed spend-class signal: KKH TED framework max \"11,000,000.00 EUR\" naming GEO as one of ~18 themes — a ceiling, not GEO spend",
            "Posting bodies: 6 of 35 read from employer sites, 6 confirm GEO as a duty, 0 name an engine by brand; Cigna names AEO vendors \"Profound, Scrunch, Bluefish, Evertune\"",
            "Engine × segment: ChatGPT top by mention in skincare 91, B2B SaaS 104, high-CPA 49; local Gemini / AI Mode / AIO 102 vs ChatGPT 97; cell-attributable naming in 5 cells only",
            "Adoption proxies: G2 AEO listings 160 → 632 (2025-11 → 2026-09); llmstxt.site hosts 56 → 1,497, flat over the last three captures; none distinguishes a paying brand",
        ],
    },
    {
        "kind": "table",
        "title": "Evidence quality: three-counts under both readings",
        "key": "Gold 0. Every Silver is vendor- or practitioner-measured; none replicated.",
        "cols": ["Measure", "Figure"],
        "widths": [3.6, 8.7],
        "rows": [
            ["Screened", "~980 (Passes 3–4) + ~1,640 (re-hunt); ad results 15 screened, 0 cleared; Reddit 852 records, 38 read"],
            ["Silver", "7 grade_raw / 1 grade_rule1 (2026-09-22); +4 grade_raw / +1 grade_rule1 (2026-09-23), all outside the three verticals"],
            ["Case corpus (52), R1", "10 metric-moved experimental / 29 observational / 13 action named, outcome unknown"],
            ["Case corpus (52), R2", "5 / 34 / 13"],
            ["Transition set (108), R1", "6 / 61 / 37 (4 outside the classes)"],
            ["Transition set (108), R2", "1 / 66 / 37 (4 outside)"],
            ["Brand corroboration", "0 of 59 (2026-09-22); 1 of 109 (2026-09-23, Chime); cumulative 1 of 168"],
            ["Paid-by-outcome; sales crossing", "0 yes / 0 no / 12 unknown; only NerdWallet reaches sales, as a revenue line attributed by management, not lift"],
        ],
    },
    {
        "kind": "table",
        "title": "Negative tail beside the positive Silvers",
        "key": "27 documents state a decline, null or negative; 19 at tier 2–3. Every positive Silver is tier 5.",
        "cols": ["Document", "Figure, verbatim", "Direction", "Tier"],
        "widths": [3.2, 6.6, 1.6, 0.9],
        "rows": [
            ["Microsoft, ECF 1977-1, 2026-09-17", "\"83-93% drops in click-through rates for The Times and DNP's domains\"", "negative", "2"],
            ["NerdWallet 8-K, 2026-02-25", "\"Credit cards revenue of $26.5 million decreased 24% year-over-year\"", "negative", "2"],
            ["IAC / People Inc decks, 2026-02-03, 2026-05-04", "\"50% decline\" then \"63% decline in Google Search referrals over two years\"", "negative", "2"],
            ["People Inc 10-Q, 2026-08-03; Chegg 8-K, 2025-08-05", "\"22% decline in Core Sessions\"; subscribers \"decline of 40%\"", "negative", "2"],
            ["TW3 / Citead, arXiv 2609.07559", "GEO levers move citation on \"none\" of ten engine families", "null", "4"],
            ["HubSpot, Fortune op-ed, 2026-09-22", "blog \"5 million\" fewer visits in a thirty-day period", "negative", "3"],
            ["Quattr / Men's Wearhouse; Sitefire / Pointhound", "\"46% more clicks\"; \"+300% more site visits from AI Search\" — Silver / Bronze under rule 1", "positive", "5"],
            ["Chime careers page, 2025-11-24", "\"tripled our AI citations\" — the one tier-3 positive, graded Bronze", "positive", "3"],
        ],
    },
    {
        "kind": "table",
        "title": "Hypotheses: 32 registered, 26 scored, marks as each source states them",
        "key": "Latest register: confirmed 11 + 3 dual · killed 7 · unresolved 5 + 3 dual · not produced 6. Pass 9 read 6 / 6 / 4 / 7 stands beside.",
        "cols": ["ID", "Claim, abbreviated", "Latest mark", "Prior marks beside"],
        "widths": [1.2, 5.0, 3.4, 2.7],
        "rows": [
            ["H3", "a vendor demonstrates causal lift", "killed", "killed"],
            ["H6", "brand action precedes measured visibility change", "confirmed (rule1, narrow) / unresolved (verticals)", "confirmed (Pass 9); unresolved (review-1)"],
            ["H7, H9", "organic spends in more cells; agentic spend enterprise-only", "H7 confirmed (loose) / unresolved (strict); H9 confirmed both readings", "unresolved"],
            ["H10, H11", "org/content changes outnumber paid; tier-3 transition evidence per vertical", "confirmed; confirmed", "not produced; killed / not produced"],
            ["H16", "every published size is a forecast", "unresolved — checked", "confirmed (Pass 9)"],
            ["H17, H20–H22", "engine ad disclosure; controlled ad result; user counts; forecast spread >3×", "killed ×4", "not registered before 2026-09-23"],
            ["H18, H19, H23–H25", "network rate card; third-party placement; steering papers; in-answer auction; public code", "confirmed ×5", "not registered"],
            ["HE2, HE3, HP1–HP4", "six panel hypotheses", "not produced — Pass 10 skipped by owner 2026-09-23", "not produced"],
        ],
    },
    {
        "kind": "table",
        "title": "Ranked risks 1–6 (criterion: evidence tier, then breadth)",
        "key": "Likelihood, impact, mitigation, owner: no source states one. Ranks follow the criterion, not severity.",
        "cols": ["Rank", "Risk", "Strongest evidence (tier)", "Repo holds against it (tier)"],
        "widths": [0.7, 3.3, 4.6, 3.7],
        "rows": [
            ["1", "Referral collapse: the answer replaces the click", "\"83-93% drops in click-through rates\" (2); cards revenue \"decreased 24%\" (2)", "AI referral visits 770.7M/month, \"+117.4%\" (4)"],
            ["2", "Regulation: disclosure duties, exclusions, fair-ranking", "AI Act Art. 50; VLOSE, Art. 39 duty Jan 2027 (2); CMA (2); AIO ads exclude finance, healthcare (3)", "\"No enforcement action found against any engine\" (2)"],
            ["3", "Vendor consolidation", "Semrush → Adobe (2); Yext → GoShine (2); Scrunch → Sitecore (3)", "Profound $1.8B valuation (3); 13 pure-plays rostered (5)"],
            ["4", "Platform capture: engines sell ads, checkout, measurement", "Ads Manager, Pixel, Conversions API, \"more than 50\" partners (3); Copilot Checkout 0% (3); campaigns auto-eligible (3)", "0 native visibility tools at OpenAI, Anthropic (3); AP2 to FIDO, UCP councils (3)"],
            ["5", "No payback evidence: 0 Gold; 0 of 15 ad results controlled", "blog \"5 million\" fewer visits (3); CTR 1.30%, \"very few sign-ups\" (5)", "citations 48 vs 426 (5, Silver rule1); \"3x return on ad spend\", one advertiser (3, Fools gold)"],
            ["6", "Measurement opacity", "0 of 34 vendors disclose a prompt set (3); no AI revenue line at Alphabet (3); ad presence 0.8%–26% (5)", "Pixel, Conversions API (3); Ahrefs \"454M+ prompts\" partial (3)"],
        ],
    },
    {
        "kind": "table",
        "title": "Ranked risks 7–11",
        "cols": ["Rank", "Risk", "Strongest evidence (tier)", "Repo holds against it (tier)"],
        "widths": [0.7, 3.3, 4.6, 3.7],
        "rows": [
            ["7", "Substitute channels: \"do nothing\" and classical search suffice", "Google \"no additional requirements\" (3); GEO levers move citation on \"none\" of ten (4); \"No tool requested llms.txt\" (4)", "IAB \"No. 1 area of increased focus... 76%\" (4, attention); Coty 10-K GEO line (2, outcome unknown)"],
            ["8", "Engine policy reversal", "\"Claude will remain ad-free\" (3); Gemini app \"not rushing anything here\" (3); Perplexity \"winding down\" (5)", "\"over 40 countries\", \"$1 billion\" run rate (3); Amazon, Copilot live (3)"],
            ["9", "Agentic rails: checkout on the engine surface, fees undisclosed", "Shopify merchants auto-enrolled into Copilot Checkout (3); 6 of 6 protocol fee clauses unknown (3)", "\"does not take a commission\" (3); merchant stays \"merchant of record\" (3)"],
            ["10", "Manipulation and countermeasures", "δRate \"+334%\" (3); spam policy \"manipulate generative AI responses\" (3); 16 CFR 465.2 (2)", "no P1 engine names seeding, farming, citation-preference content (3); guardrails \"at most 5.7% relative\" (3)"],
            ["11", "Unsizeable market: every published size is a forecast", "18 figures, 15 forecasts, 0 measured (6); agentic 2030 spread 26.3× (5–6)", "\"$38 million in ARR\" (2); \"$1 billion\" run rate (3)"],
        ],
    },
    {
        "kind": "table",
        "title": "Programme-done rows: both counts where two exist",
        "cols": ["Condition", "Bar", "Status"],
        "widths": [2.8, 2.6, 6.9],
        "rows": [
            ["Tier-3 share", "≥ 80%", "not met — Pass 9 list 11 of 25 = 44.0% (68.0% on 2026-09-22 tiers beside); review-1 list 12 of 27 = 44.4%; ex-Lane E 61.1% / 63.2%; ex-meta 50.0% / 50.0%"],
            ["P1 engine × sub-market", "number or unknown — checked", "met — 9 of 9"],
            ["Segment matrix", "every cell read, with signals", "strict 26 of 27 (one blank); loose 27 of 27; earlier 19 of 27 and strict 8 of 27 beside"],
            ["Success stories", "one Silver per vertical, or absence with count", "met — grade_raw: two verticals on the Silver arm; grade_rule1: absence arm in all three (~155 / ~141 / ~55 screened)"],
            ["Hypotheses", "every H scored", "partial — 26 of 32; 6 not produced while Pass 10 is skipped; earlier 15 of 23, 17 of 23 beside"],
            ["Pass 10", "three predictions on panel", "skipped by owner 2026-09-23 — 0 of 3; day-0 gap recorded, never back-filled"],
            ["Pass 12, 13, 14 rows (added 2026-09-23)", "filled or unknown — checked", "9 of 9 engine × ad cells; 9 of 9 sub-market × size cells; 38 papers tiered"],
        ],
    },
    {
        "kind": "bullets",
        "title": "What the evidence does not show",
        "bullets": [
            "Causal sales lift from any intervention: 0 Gold in ~2,620 items; best designs one unit per arm, unreplicated",
            "Whether AI referral converts above organic search: Adobe \"42% Higher\" compares AI to non-AI visits; the organic comparator exists only at tier 5",
            "Any sub-market size, price paid, engine rate card, protocol fee, agent-executed GMV, or the budget line spend comes from",
            "A per-engine AI referral or conversion breakout from any retail-analytics publisher",
            "Whether a named brand confirms a vendor case: 1 of 168 (a Wayback copy of a careers page)",
            "What engines return to buying-shaped prompts under neutral conditions: six panel hypotheses not produced",
            "Whether any posting was filled or any named change shipped; live effect of any Lane D technique on a P1 surface",
        ],
    },
    {
        "kind": "bullets",
        "title": "Questions only the owner can answer",
        "note": "No lean is attached to any question. Research consequence if deferred in brackets.",
        "bullets": [
            "1. Reading R1 vs R2 for pre/post with untreated control: pick one, or keep both [every three-count prints both]",
            "2. Judge column negative_tail: rubric (keep) or thumb (drop or reword) [judge scores as written]",
            "3. Is \"which sub-market\" a permissible ask in a research brief [side by side, no choice]",
            "4. Importance order over the 32 hypotheses [register stays in lane order]",
            "5. Credentials: Crunchbase Pro, PitchBook, Gartner, Forrester, Bloomberg, EMARKETER, Statista, Shopify Partner, Mastercard [cells stay unknown — checked]",
            "6. Pass 10 stays skipped, or reopens, and under which vantage [HE2, HE3, HP1–HP4 stay not produced]",
            "Raised by the evidence: grade_raw or grade_rule1; strict or loose; reserve verticals (trigger met under rule1 only); builder-constraint question as hypothetical or researched",
        ],
    },
    {
        "kind": "bullets",
        "title": "Confidence and caveats",
        "bullets": [
            "Tier-3 share 44.0% / 44.4% against an 80% bar; the shortfall is Lane E vendor cases and tier-6 forecasts; 0 of 12 sub-tier claims re-evidenced",
            "Survivorship: published cases are winners; re-grading moved 12 up, 0 down; new Silvers run by vendors on their own properties",
            "Self-reports throughout: prices, counts, funding, cases, postings; none independently audited",
            "Measured by us: day-0 panel only (one date, one localised path) and screen, word and HTTP counts",
            "41 figures carried twice, both standing, none averaged: stale 6; two bases 9; two tiers 5; two sources or dates 17; two readings 3; two pulls 1",
            "24 of 59 compiled files exceed their line count; compression pass named as method debt, not run",
            "Absence is only as strong as the channels checked: live Reddit, Indeed, EMARKETER, Perplexity hub still blocked; Crunchbase, Gartner, Forrester need payment",
            "Profiles stale from 2026-12-22; this deck carries evidence, not a verdict",
        ],
    },
]

# ---------------------------------------------------------------- helpers


def _text(frame, text, size, color=BODY, bold=False, align=PP_ALIGN.LEFT):
    frame.clear()
    p = frame.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color
    r.font.name = "Calibri"
    return p


def _box(slide, x, y, w, h):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tb.text_frame.word_wrap = True
    return tb.text_frame


def title_bar(slide, title):
    bar = slide.shapes.add_shape(1, 0, 0, W, Inches(1.0))
    bar.fill.solid()
    bar.fill.fore_color.rgb = DARK
    bar.line.fill.background()
    tf = bar.text_frame
    tf.margin_left = Inches(0.5)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    _text(tf, title, 26, WHITE, bold=True)
    accent = slide.shapes.add_shape(1, 0, Inches(1.0), W, Inches(0.06))
    accent.fill.solid()
    accent.fill.fore_color.rgb = ACCENT
    accent.line.fill.background()


def footer(slide, n):
    tf = _box(slide, Inches(0.5), Inches(7.0), Inches(10.5), Inches(0.35))
    _text(tf, FOOTER, 10, GREY)
    tf2 = _box(slide, Inches(11.3), Inches(7.0), Inches(1.6), Inches(0.35))
    _text(tf2, str(n), 10, GREY, align=PP_ALIGN.RIGHT)


def key_line(slide, text, y):
    tf = _box(slide, Inches(0.5), y, Inches(12.3), Inches(0.5))
    _text(tf, text, 14, ACCENT, bold=True)


def bullets(slide, items, y, size=16):
    tf = _box(slide, Inches(0.7), y, Inches(12.0), Inches(5.5))
    tf.clear()
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        r = p.add_run()
        r.text = ("• " if not item[:2].rstrip(".").isdigit() else "") + item
        r.font.size = Pt(size)
        r.font.color.rgb = BODY
        r.font.name = "Calibri"
        p.space_after = Pt(8)


def table(slide, cols, rows, widths, y):
    assert len(rows) <= 8, "keep tables to 8 rows or fewer"
    n_rows = len(rows) + 1
    height = Inches(0.42) * n_rows
    shape = slide.shapes.add_table(n_rows, len(cols), Inches(0.5), y, Inches(sum(widths)), height)
    tbl = shape.table
    for j, w in enumerate(widths):
        tbl.columns[j].width = Inches(w)
    for j, c in enumerate(cols):
        cell = tbl.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = ACCENT
        _text(cell.text_frame, c, 12, WHITE, bold=True)
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = ROW_ALT if i % 2 == 0 else WHITE
            _text(cell.text_frame, val, 10, BODY, bold=(j == 0))


# ---------------------------------------------------------------- build


def build():
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    blank = prs.slide_layouts[6]
    for n, s in enumerate(SLIDES, start=1):
        slide = prs.slides.add_slide(blank)
        if s["kind"] == "title":
            bg = slide.shapes.add_shape(1, 0, 0, W, Inches(3.6))
            bg.fill.solid()
            bg.fill.fore_color.rgb = DARK
            bg.line.fill.background()
            tf = _box(slide, Inches(0.7), Inches(1.2), Inches(12), Inches(1.4))
            _text(tf, s["title"], 36, WHITE, bold=True)
            tf = _box(slide, Inches(0.7), Inches(2.6), Inches(12), Inches(0.6))
            _text(tf, s["subtitle"], 18, WHITE)
            bar = slide.shapes.add_shape(1, 0, Inches(3.6), W, Inches(0.08))
            bar.fill.solid()
            bar.fill.fore_color.rgb = ACCENT
            bar.line.fill.background()
            bullets(slide, s["lines"], Inches(4.2), size=18)
            tf = _box(slide, Inches(0.7), Inches(6.3), Inches(12), Inches(0.4))
            _text(tf, SOURCE, 11, GREY)
            footer(slide, n)
            continue
        title_bar(slide, s["title"])
        y = Inches(1.3)
        if s.get("quote"):
            tf = _box(slide, Inches(0.7), y, Inches(12), Inches(1.0))
            _text(tf, s["quote"], 16, DARK, bold=True)
            y = Inches(2.4)
        if s.get("key"):
            key_line(slide, s["key"], y)
            y = y + Inches(0.6)
        if s.get("note"):
            key_line(slide, s["note"], y)
            y = y + Inches(0.6)
        if s["kind"] == "table":
            table(slide, s["cols"], s["rows"], s["widths"], y)
        else:
            bullets(slide, s["bullets"], y)
        footer(slide, n)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    prs.save(OUT)
    return OUT


if __name__ == "__main__":
    print(build())

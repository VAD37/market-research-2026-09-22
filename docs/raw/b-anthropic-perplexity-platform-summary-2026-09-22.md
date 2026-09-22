# Anthropic and Perplexity — platform-primary commercial-surface summary (P2-c5)

```yaml
source:          this agent, compiled from the raw files listed below
url_or_doc_id:   n/a — summary of docs/raw/ pulls
published:       2026-09-22
pull_date:       2026-09-22
pull_method:     manual (compilation, no new fetch)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     inherits the tier of the platform-primary pulls it cites; no new source
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Claude — Anthropic; Perplexity
metric_kind:     none
supersedes:      none
captured:        n/a — compiled table
```

Anthropic priority 1 per `plan.md` (held at 1 by `scope.md` R4 user default, unaffected by the Pass 2 share reweight). Perplexity priority **3** per `plan.md` "Engine matrix — reweight 1, 2026-09-22" — noted here per task instruction; this cluster still gives Perplexity full treatment because P2-c5 was scoped before reweight 1 and the withdrawal check is cheap.

## Table 1 — existence answers per engine × question

| Engine | Question | Answer | Verbatim quote | Page date | Raw path |
|---|---|---|---|---|---|
| Anthropic | Ads / sponsored placement in Claude conversations | **No — explicit, dated policy** | "Claude will remain ad-free. Our users won't see 'sponsored' links adjacent to their conversations with Claude; nor will Claude's responses be influenced by advertisers or include third-party product placements our users did not ask for." | 2026-02-04 | `b-anthropic-ad-free-2026-09-22.md` |
| Anthropic | Ads / sponsored placement — consumer app recommendation specifically | **No — explicit** | "Claude doesn't take payment to recommend any connected app. There are no sponsored rankings, no paid placements, and no advertising." | undated (Help Center) | `a-anthropic-connected-apps-recommendations-2026-09-22.md` |
| Anthropic | Usage Policy mentions advertising/commercial recommendation | **No mention found** | Full Usage Policy text checked; no occurrence of "advertis-," "sponsor-," "merchant," or "checkout" anywhere in the policy | effective 2025-09-15 | `b-anthropic-usage-policy-2026-09-22.md` |
| Anthropic | Commerce / agent-checkout program — public, merchant-facing | **unknown — checked anthropic.com, docs.claude.com, platform.claude.com 2026-09-22** | Company states interest and internal research ("We're particularly interested in the potential of agentic commerce, where Claude acts on a user's behalf to handle a purchase or booking end to end... we'll continue to build features that enable our users to find, compare, or buy products"; "blueprints for consumer and merchant agents" across "retail, travel, telecom, and entertainment") but no public merchant-facing terms page, checkout spec, or fee schedule was found | 2026-02-04 / 2026-09-10 | `b-anthropic-ad-free-2026-09-22.md`, `c-anthropic-commerce-webinar-2026-09-22.md`, `c-anthropic-project-deal-2026-09-22.md` |
| Anthropic | Merchant or partner program — public | **unknown — checked anthropic.com/webinars, anthropic.com/features 2026-09-22** | Only found: an internal, one-week, 69-employee pilot (Project Deal) and a partner-facing webinar naming "blueprints for consumer and merchant agents"; no public merchant enrollment page or partner-program terms | 2026-04-24 | `c-anthropic-project-deal-2026-09-22.md`, `c-anthropic-commerce-webinar-2026-09-22.md` |
| Anthropic | Agentic-commerce protocol published, implementable without a contract (H8) | **No Anthropic-authored spec found; generic MCP connector is public and gate-free, but carries no commerce-specific content** | "Of the feature set of the MCP specification, only tool calls are currently supported... The server must be publicly exposed through HTTP" — no mention of "payments," "checkout," "merchant," "cart," or "order" anywhere on the page | undated | `c-anthropic-mcp-connector-2026-09-22.md` |
| Anthropic | Usage policy / news posts on commercial recommendation | **Explicit boundary rule stated** | "they should be initiated by the user (where the AI is working for them) rather than an advertiser (where the AI is working, at least in part, for someone else)... Claude's only incentive is to give a helpful answer" | 2026-02-04 | `b-anthropic-ad-free-2026-09-22.md` |
| Perplexity | Ad product (sponsored follow-up questions) — ever existed | **Yes, company-confirmed launch** | "starting this week, we will begin experimenting with ads on Perplexity... formatted as sponsored follow-up questions and paid media positioned to the side of an answer" | 2024-11-12 | `b-perplexity-ads-launch-2026-09-22.md` |
| Perplexity | Ad product — current status, live self-serve or IO product today | **No live ad product or advertiser page found; original announcement post still live, unedited** | Original ad-launch post is unchanged at its original URL; current Pricing page and 404-page global footer carry no "Advertise" link anywhere; `/hub/advertise` returns Perplexity's own 404 | pricing page undated; pull 2026-09-22 | `b-perplexity-pricing-2026-09-22.md`, `b-perplexity-merchant-terms-withdrawn-2026-09-22.md` |
| Perplexity | Publisher program | **Yes, live, renamed/evolved** | "Comet Plus is a new subscription that gives Perplexity users access to premium content from a group of trusted publishers and journalists... a $5 standalone subscription... distributing all of that revenue to participating publishers, minus a small portion for Perplexity's compute costs" | 2025-08-25 | `b-perplexity-publisher-program-2026-09-22.md` |
| Perplexity | Shopping / merchant / checkout program | **Yes, live as announced; standalone terms page now 404** | "Buy with Pro, which lets you check out seamlessly right on our website or app for select products from select merchants"; Merchant Program described as "free for merchants" | 2024-11-18 | `c-perplexity-shop-merchant-2026-09-22.md` |
| Perplexity | Pricing or rate disclosure | **Subscription pricing disclosed (Free/$20/$200); ad CPM rate and Comet Plus 80/20 split not disclosed on Perplexity's own pages** | "$0 /month... $20 /month... $200 /month"; Comet Plus revenue split stated only as "minus a small portion for Perplexity's compute costs," no percentage | undated (pricing) / 2025-08-25 (Comet Plus) | `b-perplexity-pricing-2026-09-22.md`, `b-perplexity-publisher-program-2026-09-22.md` |
| Perplexity | Withdrawal or renaming | **Merchant Program terms page withdrawn (404); no Perplexity-authored withdrawal statement for the ad program found on Perplexity's own pages** | See Table 2 | see Table 2 | `b-perplexity-merchant-terms-withdrawn-2026-09-22.md`, `b-perplexity-merchant-terms-archive-2026-09-22.md` |

## Table 2 — archive diffs (withdrawal check, B4)

| URL checked | Live status, 2026-09-22 | Archive capture found | Archive capture date | Prior wording recovered | Raw path |
|---|---|---|---|---|---|
| `perplexity.ai/hub/legal/merchant-program-terms-of-service` | 404 | 1 capture | **2025-07-16** | **No** — capture rendered a blank client-side-app shell (Framer site, JS-hydrated content not replayed by the archive); page `<title>` "Perplexity Merchant Terms of Service" recovered, body text not recoverable | `b-perplexity-merchant-terms-archive-2026-09-22.md` |
| `perplexity.ai/hub/blog/why-we-re-experimenting-with-advertising` | Live, unedited | not checked — page still live, no withdrawal to check | n/a | n/a (not needed) | `b-perplexity-ads-launch-2026-09-22.md` |
| `perplexity.ai/hub/blog/introducing-comet-plus` | Live, unedited | not checked — page still live, no withdrawal to check | n/a | n/a (not needed) | `b-perplexity-publisher-program-2026-09-22.md` |
| `perplexity.ai/hub/advertise` (guessed path) | 404 | not checked — no evidence this exact path ever existed live; recorded as a negative probe, not a withdrawal | n/a | n/a | `b-perplexity-merchant-terms-withdrawn-2026-09-22.md` |

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| Prior verbatim wording of the Perplexity Merchant Program Terms of Service | web.archive.org (1 capture, blank render) | 2026-09-22 |
| Perplexity's own dated statement announcing the ad program's withdrawal or pause | perplexity.ai/hub/blog, perplexity.ai/hub/legal, perplexity.ai/hub/pricing (all checked; none found) | 2026-09-22 |
| Comet Plus exact publisher revenue-share percentage on Perplexity's own page (80/20 is trade-press only — SearchEngineJournal, Digiday — not confirmed at tier 3) | perplexity.ai/hub/blog/introducing-comet-plus | 2026-09-22 |
| Anthropic public merchant/checkout terms page or protocol spec (if any exists beyond the internal Project Deal pilot and the generic MCP connector) | anthropic.com, anthropic.com/features, anthropic.com/webinars, docs.claude.com, platform.claude.com | 2026-09-22 |
| Contents of Anthropic's "Remote MCP server examples" directory (would show whether Stripe/PayPal-class payment MCP servers are listed) — page failed to render the card list | platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers | 2026-09-22 |

## Caveats

- Oldest pull this summary depends on: 2026-09-22 for every live-page pull; the one archive capture cited carries capture date 2025-07-16, clearly labelled as a capture date, never conflated with the 2026-09-22 pull date.
- Anthropic's ad-free policy ("Claude is a space to think," 2026-02-04) is explicit and dated but is a **policy statement**, not itself proof that no advertiser has ever bought placement — it is the strongest company-stated evidence available and is the evidence this cluster could pull; no contradicting Anthropic page was found.
- Perplexity's ad-program status is read from an absence pattern (no live "Advertise" page, no ad-product FAQ, original 2024 announcement post left unedited and unretracted) rather than from one dated withdrawal statement in Perplexity's own words — the strongest single available proxy for "withdrawn" is the 404 on the Merchant Program terms page, which is a *different* program (merchant data-sharing, not the ad product) per Perplexity's own 2024 post ("This is distinct from and unrelated to Perplexity's new sponsored questions ad products"). This distinction is preserved, not collapsed, in Table 1.
- Perplexity's reported exit from advertising (February 2026, per third-party trade and industry coverage — eMarketer, Digiday, remarks by its head of publisher partnerships at Advertising Week New York) is **not** cited as evidence here per this cluster's source scope (Anthropic/Perplexity domains and the archive channel only); it is named in this caveat only to explain why the absence pattern above was searched for, not as a filed source.
- This cluster did not read or write `docs/raw/*openai*` or `docs/raw/e-claude-panel-2026-09-22.md`, per task instruction.
- Anthropic's `docs.claude.com` domain denied the Chrome extension's page-read permission though the page loaded and 302-redirected to `platform.claude.com`, which granted it — recorded as an access-path quirk in `c-anthropic-mcp-connector-2026-09-22.md`, not a content gap.

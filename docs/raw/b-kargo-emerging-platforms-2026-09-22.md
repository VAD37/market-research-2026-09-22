# Kargo — Emerging Platforms solutions page (AI Native / AI apps)

```yaml
source:          Kargo (kargo.com)
url_or_doc_id:   https://www.kargo.com/solutions-emerging-platforms
published:       page lastmod 2026-09-04T18:57:40.000Z per kargo.com/sitemap.xml
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool, plain HTTP, no browser needed) — connection to kargo.com was intermittent this session (multiple prior attempts to the homepage returned "Failed to fetch robots.txt... due to a connection issue" before one attempt succeeded; this specific page loaded on the first attempt after that)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform/vendor primary, own solutions page
source_label:    vendor-reported
lane:            B
sub_market:      paid placement
engine:          n/a — "AI apps" / "AI assistant apps" framing, no single named engine on this page
metric_kind:     none
supersedes:      none
captured:        full page text through the "Our Solutions" cross-link section (truncated by tool output limit before "Contact Us")
```

## Verbatim

"Emerging Digital Advertising Solutions | Kargo — Kargo"

"# Emerging Platforms — Reach your audience where they're most engaged across high-attention, clutter-free environments: **Laptop home screens, gaming experiences, AI apps**, and screens across the cityscape. We call these emerging media surfaces."

"## The Kargo Edge — Exclusive access, full attention, extended reach, no additional lift: Kargo turns the newest surfaces into your next advantage." Three sub-points: "Only at Kargo — Kargo builds direct and exclusive deals with emerging platforms, so advertisers reach their audiences before the competition." / "Attention, Not Interruption — Native, uncluttered placements that fit each environment and own the moment." / "Create Once, Run Everywhere — Bring the creative you already have. Kargo adapts it and runs it across Surfaces within your existing buy."

Four named surface categories on this page: "OEM Home Screens — Own the power-on moment across devices. From laptops and browsers to CTVs and game consoles." / "Productivity Tools — No clutter, high attention—you get both with home screen placements on the utility apps people use for transferring files, photos, and more." / "**AI Native — AI assistant apps are where people now ask, plan, and decide. Kargo places your brand alongside the response, viewable and native to the conversation.**" / "Retail Media — Reach shoppers on-site at the moment of purchase across top retail media networks. Closed-loop attribution ties every impression to the sale."

"## Breakthrough Performance" — three named-brand case fragments, percentage figures rendered as a repeating digit-string artifact by the fetch tool (not a real number, see pull notes): "Purchase intent lift - HP Toast"; "VCR - WeTransfer"; "Awareness lift - CTV Glass."

Homepage (`kargo.com/`, same pull session) additionally states: "# Kargo is Art & Intelligence... **Kargo OS** — Behind the scenes and screens, a unified agentic system that's built to streamline your campaigns from brief to business outcomes." Case names on homepage: "Hershey's: Sweet Success; Anytime Fitness; American Eagle."

## Pull notes — mechanical only

- Fetched via plain HTTP fetch tool. `kargo.com` was **intermittently unreachable this session**: an initial homepage fetch and a `kargo.com/sitemap.xml` fetch both returned `"Failed to fetch robots.txt https://www.kargo.com/robots.txt due to a connection issue"`; a browser-extension navigation attempt in the same window also returned `"Frame with ID 0 is showing error page"`; a `WebFetch` cross-check returned `getaddrinfo ENOTFOUND www.kargo.com` and `getaddrinfo ENOTFOUND kargo.com` (full DNS resolution failure at that moment). A later retry of the plain fetch tool succeeded on the homepage, the sitemap, and this page, with no further errors — recorded as a transient connectivity issue, not a permanent block, and not re-tested exhaustively beyond confirming this file's content landed successfully.
- **The "Breakthrough Performance" percentage figures render as a garbled repeating-digit string in the fetch tool's markdown simplification** ("012345678901234567890123456789...%") — this is a rendering artifact of the source page's animated/JS-driven counter widget, not a real number; the underlying true percentage was not recoverable via this pull method. Recorded verbatim as garbled, not corrected or guessed; `[note: HP Toast, WeTransfer, and CTV Glass case percentages not recoverable via plain fetch — animated counter widget]`.
- No dedicated ChatGPT-named page found; a guessed URL (`kargo.com/emerging-platforms`, without the `solutions-` prefix) 404'd before the correct sitemap-derived URL (`kargo.com/solutions-emerging-platforms`) was found and used instead. No pricing page attempted beyond one guess (`kargo.com/pricing`) which hit the same transient connection error and was not retried, given this is an enterprise/managed sell-side platform unlikely to publish self-serve pricing (no "Sign Up" or self-serve CTA anywhere on the homepage or this page — every CTA is "Learn More," "Stay Informed," or "Contact Us"). Recorded `unknown — checked kargo.com/, kargo.com/solutions-emerging-platforms, kargo.com/pricing (connection error, not retried) 2026-09-22`.
- **Admission-rule role**: this vendor is named as an OpenAI "technology partner" on `docs/raw/b-openai-new-ways-buy-ads-2026-09-22.md` (source 1, already landed under P2-c3). Source 2 (independent): `b-kargo-second-source-2026-09-22.md`, this cluster, a G2 reviews page. Admitted under limb (a).
- No customer count, aggregate figure, or logo count of any kind found on either page pulled (only three named case brands: HP Toast, WeTransfer, CTV Glass, Hershey's, Anytime Fitness, American Eagle — six distinct named brands, not an aggregate). `unknown — checked kargo.com/, kargo.com/solutions-emerging-platforms 2026-09-22`.

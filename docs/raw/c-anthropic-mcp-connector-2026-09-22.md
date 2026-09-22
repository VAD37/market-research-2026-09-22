# Anthropic — MCP connector docs (checked for a commerce/payments/checkout spec)

```yaml
source:          Anthropic (Claude Platform Docs)
url_or_doc_id:   https://docs.claude.com/en/docs/agents-and-tools/mcp-connector (redirects 302 to https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
published:       undated — no visible revision date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own API documentation
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Claude — Anthropic API (Messages API; model examples shown as "claude-opus-5")
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Title: "MCP connector - Claude Platform Docs"

"Connect to remote MCP servers directly from the Messages API without an MCP client, and allowlist, denylist, or configure individual tools.

Claude's Model Context Protocol (MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API without a separate MCP client.

The previous version of this feature (mcp-client-2025-04-04) is deprecated. See Deprecated version: mcp-client-2025-04-04."

"Key features

Direct API integration: Connect to MCP servers without implementing an MCP client
Tool calling support: Access MCP tools through the Messages API
Flexible tool configuration: Enable all tools, allowlist specific tools, or denylist unwanted tools
Per-tool configuration: Configure individual tools with custom settings
OAuth authentication: Support for OAuth Bearer tokens for authenticated servers
Multiple servers: Connect to multiple MCP servers in a single request"

"Limitations

Of the feature set of the MCP specification, only tool calls are currently supported.
The server must be publicly exposed through HTTP (supports both Streamable HTTP and SSE transports). Local STDIO servers cannot be connected directly."

"Data retention

The MCP connector is not covered by ZDR arrangements. Data exchanged with MCP servers, including tool definitions and execution results, is retained according to Anthropic's standard data retention policy.

For ZDR eligibility across all features, see API and data retention."

"Compatibility
Supported platforms
Claude API — Beta
Claude Platform on AWS — Beta
Microsoft Foundry — Beta"

## Pull notes — mechanical only

- `docs.claude.com` refused `get_page_text` via the Chrome extension ("Permission denied for reading page content on this domain") even though the page loaded and redirected (302) to `platform.claude.com`; the redirected `platform.claude.com` domain granted extension access without a prompt. Recorded as an access-path note, not a content difference — both `docs.claude.com` and `platform.claude.com` resolve to the same documentation site per Anthropic's own redirect.
- The companion page `https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers` (third-party MCP server directory/examples) loaded but its "Remote MCP server examples" card list rendered as eighteen literal "Loading" placeholders and never resolved after a 2-second wait; `read_page` (accessibility tree) returned no card links either. This directory — which a prior web search indicated lists third-party payment-related servers (e.g., Stripe, PayPal) — could not be captured verbatim from this cluster's pull and is recorded as `unknown — checked platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers 2026-09-22 (page failed to render server list)`, not as an absence.
- This connector page itself is **protocol-mechanical**: it documents how to wire any remote MCP server (tool-calling, auth, config) into the Messages API. It names no commerce-specific concept — no "payments," "checkout," "merchant," "cart," or "order" anywhere in the captured text — and no Anthropic-authored commerce/checkout specification. Third-party companies (per web search, e.g. Stripe at `mcp.stripe.co`, PayPal at `mcp.paypal.com`) host their own commerce MCP servers that a developer can connect to via this generic connector; Anthropic does not itself publish a commerce or checkout protocol at this URL. This is the direct evidence behind the `hypotheses.md` H8 "publicly readable, no access gate" question as read from Anthropic's side: the connector mechanism is public and gate-free, but there is no Anthropic-authored commerce/checkout spec for it to gate.

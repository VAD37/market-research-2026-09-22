# Anthropic Privacy Center — crawler identity (ClaudeBot, Claude-User, Claude-SearchBot)

```yaml
source:          Anthropic Privacy Center
url_or_doc_id:   https://privacy.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler -> resolved to https://privacy.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
published:       undated — no date on page (help-center article, no visible revision date)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own crawler documentation
source_label:    company-stated
lane:            A
sub_market:      n/a
engine:          Claude — Anthropic (no model version named; describes crawler infrastructure, not a model)
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Title: "Does Anthropic crawl data from the web, and how can site owners block the crawler? | Anthropic Privacy Center"

"As per industry standard, Anthropic uses a variety of robots to gather data from the public web for model development, to search the web, and to retrieve web content at users' direction. Anthropic uses different robots to enable website owner transparency and choice. Below is information on the three robots that Anthropic uses and how to set your site preferences to enable those you want to access your content and limit those you don't."

**Bot table:**

| Bot | Use | What happens when you disable it |
|---|---|---|
| ClaudeBot | ClaudeBot helps enhance the utility and safety of our generative AI models by collecting web content that could potentially contribute to their training. | When a site restricts ClaudeBot access, it signals that the site's future materials should be excluded from our AI model training datasets. |
| Claude-User | Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent. | Claude-User allows site owners to control which sites can be accessed through these user-initiated requests. Disabling Claude-User on your site prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search. |
| Claude-SearchBot | Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. | Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results. |

"As part of our mission to build safe and reliable frontier systems and advance the field of responsible AI development, we're sharing the principles by which we collect data as well as instructions on how to opt out of our crawling going forward:

Our collection of data should be transparent. Anthropic uses the Bots described above to access web content.

Our crawling should not be intrusive or disruptive. We aim for minimal disruption by being thoughtful about how quickly we crawl the same domains and respecting Crawl-delay where appropriate.

Anthropic's Bots respect "do not crawl" signals by honoring industry standard directives in robots.txt.

Anthropic's Bots respect anti-circumvention technologies (e.g., we will not attempt to bypass CAPTCHAs for the sites we crawl.)

To limit crawling activity, we support the non-standard Crawl-delay extension to robots.txt. An example of this might be:

User-agent: ClaudeBot
Crawl-delay: 1

To block a Bot from your entire website, add this to the robots.txt file in your top-level directory. Please do this for every subdomain that you wish to opt out from. An example of this is:

User-agent: ClaudeBot
Disallow: /

Opting out of being crawled by Anthropic Bots requires modifying the robots.txt file in the manner above. Alternate methods like blocking IP address(es) from which Anthropic Bots operates may not work correctly or persistently guarantee an opt-out, as doing so impedes our ability to read your robots.txt file. If a crawler has a source IP address on this list, it indicates that the crawler is coming from Anthropic."

"You can learn more about our data handling practices and commitments at our Help Center. If you have further questions, or believe that our Bots may be malfunctioning, please reach out to claudebot@anthropic.com. Please reach out from an email that includes the domain you are contacting us about, as it is otherwise difficult to verify reports."

## Pull notes — mechanical only

- URL redirected from `anthropic.com`/`privacy.anthropic.com` framing to canonical host `privacy.claude.com` — same content, recorded per pull-list substitution rule.
- Fetched via Chrome extension; loaded on first navigation, no permission prompt.
- Page does not publish a user-agent **string** format (unlike OpenAI's, Google's, Perplexity's, Amazon's and Apple's pages, which all give an example UA string) — only the bot **name**, use, and opt-out effect. No published IP-range JSON link is given on this page either (contrast: OpenAI, Perplexity and Amazon all link a `.json` IP list). Recorded as a gap in this page, not inferred.
- No crawl-volume or crawl-to-refer figures on this page — identity and policy only. Cloudflare's crawl-to-refer figures for "Anthropic" (this cluster's other pulls) are the volume-side complement.

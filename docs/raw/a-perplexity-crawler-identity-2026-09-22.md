# Perplexity docs — crawler identity (PerplexityBot, Perplexity-User)

```yaml
source:          Perplexity (docs.perplexity.ai)
url_or_doc_id:   https://docs.perplexity.ai/guides/bots -> resolved to https://docs.perplexity.ai/docs/resources/perplexity-crawlers
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own crawler documentation
source_label:    company-stated
lane:            A
sub_market:      n/a
engine:          Perplexity (priority-2)
metric_kind:     none
supersedes:      none
captured:        full page (WAF-configuration sections captured, IP-source and best-practices sections captured)
```

## Verbatim

Title: "Perplexity Crawlers - Perplexity"

"We strive to improve our service every day by delivering the best search experience possible. To achieve this, we collect data using web crawlers ("robots") and user agents that gather and index information from the internet, operating either automatically or in response to user requests. Webmasters can use the following robots.txt tags to manage how their sites and content interact with Perplexity. Each setting works independently, and it may take up to 24 hours for our systems to reflect changes."

**User agent table:**

| User Agent | Description |
|---|---|
| PerplexityBot | PerplexityBot is designed to surface and link websites in search results on Perplexity. **It is not used to crawl content for AI foundation models.** To ensure your site appears in search results, we recommend allowing PerplexityBot in your site's robots.txt file and permitting requests from our published IP ranges listed below.<br><br>Full user-agent string: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`<br><br>Published IP addresses: https://www.perplexity.com/perplexitybot.json |
| Perplexity‑User | Perplexity-User supports user actions within Perplexity. When users ask Perplexity a question, it might visit a web page to help provide an accurate answer and include a link to the page in its response. Perplexity-User controls which sites these user requests can access. **It is not used for web crawling or to collect content for training AI foundation models.**<br><br>Full user-agent string: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)`<br><br>Published IP addresses: https://www.perplexity.com/perplexity-user.json<br><br>"Since a user requested the fetch, this fetcher generally ignores robots.txt rules." |

**WAF Configuration** — "If you're using a Web Application Firewall (WAF) to protect your site, you may need to explicitly whitelist Perplexity's bots to ensure they can access your content."

Cloudflare WAF steps given: navigate to Security → WAF; create a custom rule combining User-Agent condition (`Contains` `PerplexityBot OR Perplexity-User`) AND IP Source Address condition (`Is in` the published IP ranges); set action to Allow.

AWS WAF steps given: create IP sets from the published endpoints; create string-match conditions for `PerplexityBot` and `Perplexity-User`; create Allow rules combining IP sets and UA strings, with higher priority than blocking rules; associate with the Web ACL.

"IP Address Sources — Always use the most current IP ranges from the official JSON endpoints. These addresses are updated regularly and should be the source of truth for your WAF configurations. PerplexityBot IP addresses: https://www.perplexity.com/perplexitybot.json. Perplexity-User IP addresses: https://www.perplexity.com/perplexity-user.json. Set up automated processes to periodically fetch and update your WAF rules with the latest IP ranges from these endpoints to ensure continuous access for Perplexity bots."

"Best Practices — When configuring WAF rules for Perplexity bots, combine both User-Agent string matching and IP address verification for enhanced security while ensuring legitimate bot traffic can access your content. Changes to WAF configurations may take some time to propagate. Monitor your logs to ensure the rules are working as expected and that legitimate Perplexity bot traffic is being allowed through."

## Pull notes — mechanical only

- Navigated to `docs.perplexity.ai/guides/bots` per shortlist/query-book; resolved to canonical `docs.perplexity.ai/docs/resources/perplexity-crawlers`. Recorded per pull-list substitution rule.
- Fetched via Chrome extension; loaded on first navigation.
- Only two user agents documented on this page: PerplexityBot (search) and Perplexity-User (user action). **No training-purpose crawler is named on this page** — the page states explicitly, twice, that neither listed agent is used to crawl content for AI foundation-model training. This is the engine's own stated purpose split at pull time; whether Perplexity operates an undeclared training crawler is a separate, disputed question outside this platform-primary page's scope (see Lane D / countermeasures clusters).
- No crawl-volume or crawl-to-refer figures on this page — identity and policy only.

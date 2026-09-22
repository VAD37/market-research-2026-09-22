# llmstxt.org — The /llms.txt file, v2 (proposal and spec text)

```yaml
source:          llmstxt.org (author: Jeremy Howard, Answer.AI); mirrored verbatim from the canonical GitHub-hosted source
url_or_doc_id:   https://llmstxt.org/ ; canonical source text at https://raw.githubusercontent.com/AnswerDotAI/llms-txt/main/nbs/index.qmd
published:       2024-09-03 (original); date-modified 2026-08-10 per the qmd frontmatter — this is v2 of the proposal
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary for the artefact itself; this is the spec's own canonical site and repository, not a third party describing it
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          n/a — the artefact spec itself, not engine-specific
metric_kind:     none
supersedes:      none
captured:        full page (rendered llmstxt.org HTML confirmed byte-for-byte equivalent in content to the qmd source below; qmd used for clean verbatim text extraction, see pull notes)
```

## Verbatim

Title: "The /llms.txt file, v2"
Author: Jeremy Howard
Date: 2024-09-03
Date-modified: 2026-08-10
Description: "A proposal to standardise on using an `/llms.txt` file to provide information to help agents use a website."

### Background

"Agents now use websites constantly: a coding agent fetches a library's documentation to get an API call right, and a chat assistant with search reads pages to answer questions about a product. When this proposal was first written in 2024, this was largely a prediction. Today it is routine."

"But web pages are built for people. An HTML page wraps its information in navigation, ads, and JavaScript, and converting it back into clean text is difficult and imprecise. Context windows, while larger than they were, are still too small for most websites in their entirety, and every wasted token costs time and money. Agents are best served by concise, expert-level information gathered in a single, accessible location."

"This is v2 of the proposal, updated based on what I learned from two years of adoption: thousands of sites publish an llms.txt file, documentation platforms generate one automatically, and Chrome's Lighthouse audits sites for one as part of its agentic browsing checks. The AI labs themselves publish llms.txt files for their own developer docs: OpenAI (https://developers.openai.com/llms.txt), Anthropic (https://docs.anthropic.com/llms.txt), and Gemini (https://ai.google.dev/gemini-api/docs/llms.txt). The Changes page describes what changed since v1, and why."

### Proposal

"We propose adding a `/llms.txt` markdown file to websites to provide LLM-friendly content. The file can be placed at the site root, or at any path within it, covering the pages under that path. This file offers brief background information, guidance, and links to detailed markdown files."

"llms.txt markdown is human and LLM readable, but is also in a precise format allowing fixed processing methods (i.e. classical programming techniques such as parsers and regex)."

"We furthermore propose that pages with information that agents might need provide a clean markdown version of those pages at the same URL as the original page, either with `.md` appended (`page.html.md`) or with the extension replaced by `.md` (`page.md`). (URLs without file names should append `index.html.md` or `index.md` instead.)"

"To help clients find these files, we recommend using standard link relations: `rel="alternate" type="text/markdown"` points to the markdown version of a page, and `rel="describedby"` points to the llms.txt file that covers it. ... These links can be provided as HTML `<link>` elements, or as an HTTP `Link:` response header. ... For example: `Link: </docs/page.html.md>; rel="alternate"; type="text/markdown", </docs/llms.txt>; rel="describedby"`"

"The FastHTML project follows these two proposals for its documentation. ... Agents are expected to view or search `llms.txt` to find the information they need, then follow the relevant links. The links in an llms.txt file should therefore point to LLM-friendly content, such as the markdown versions of pages described above. The file itself stays small enough to fit in context. The detail lives behind the links, and is fetched only when needed."

"llms.txt files are used most heavily for software documentation, where coding agents follow them to find API references and tutorials. The same structure works anywhere agents need a guided path into a site's content: a business outlining its structure and policies, a personal site answering questions about someone's CV, or a school providing access to course information."

"Note that all nbdev projects now create .md versions of all pages by default. All Answer.AI and fast.ai software projects using nbdev have had their docs regenerated with this feature."

### Format

"At the moment the most widely and easily understood format for language models is Markdown. Simply showing where key Markdown files can be found is a great first step. Providing some basic structure helps a language model to find where the information it needs can come from."

"The `llms.txt` file is unusual in that it uses Markdown to structure the information rather than a classic structured format such as XML. The reason for this is that we expect many of these files to be read by language models and agents. Having said that, the information in llms.txt follows a specific format and can be read using standard programmatic-based tools."

"The llms.txt file spec is for files named `llms.txt`, at the root path `/llms.txt` of a website or at any subpath (e.g. `/docs/llms.txt`). A file covers the URLs under its path, and where more than one file applies, agents should use the most specific one. A file following the spec contains the following sections as markdown, in the specific order:"

- "An optional byte-order mark (BOM)"
- "An H1 with the name of the project or site. This is the only required section"
- "A blockquote with a short summary of the project, containing key information necessary for understanding the rest of the file"
- "Zero or more markdown sections (e.g. paragraphs, lists, etc) of any type except headings, containing more detailed information about the project and how to interpret the provided files"
- "Zero or more markdown sections delimited by H2 headers, containing "file lists" of URLs where further detail is available"
  - "Each "file list" is a markdown list, containing a required markdown hyperlink `[name](url)`, then optionally a `:` and notes about the file."

Mock example given:
```markdown
# Title

> Optional description goes here

Optional details go here

## Section name

- [Link title](https://link_url): Optional link details

## Optional

- [Link title](https://link_url)
```

"The "Optional" section is used, by convention, for secondary information: links an agent can skip when a shorter context is needed."

### Existing standards

"llms.txt is designed to coexist with current web standards. While sitemaps list all pages for search engines, `llms.txt` offers a curated overview for LLMs. It can complement robots.txt by providing context for allowed content. The file can also reference structured data markup used on the site, helping LLMs understand how to interpret this information in context."

"The approach of using a standard filename follows `/robots.txt` and `/sitemap.xml` at the site root. ... robots.txt and `llms.txt` have different purposes. robots.txt lets automated tools know what access to a site is considered acceptable, such as for search indexing bots. llms.txt information is instead used on demand, when an agent needs information about a topic while assisting a user. Our expectation was that llms.txt would mainly be useful for *inference* rather than *training*, and that is how it has been used, though training runs could take advantage of the information too."

"An alternative would be the Well-Known URIs standard (RFC 8615), which reserves the `/.well-known/` prefix for metadata files like this one. But well-known URIs exist only at the origin root, and many authors control only a path on a shared host ... Like `index.html`, an `llms.txt` describes the path where it sits, something a single root location cannot express. And anyone who can publish content at a path can provide one."

"sitemap.xml is a list of all the indexable human-readable information available on a site. This isn't a substitute for `llms.txt` since it: Often won't have the LLM-readable versions of pages listed; Doesn't include URLs to external sites, even though they might be helpful to understand the information; Will generally cover documents that in aggregate will be too large to fit in an LLM context window, and will include a lot of information that isn't necessary to understand the site."

### Directories

"Here are a few directories that list the `llms.txt` files available on the web: llmstxt.site; directory.llmstxt.cloud; llmstxthub.com"

### Integrations

"Many documentation platforms and CMSs can generate an llms.txt file automatically: Mintlify - Docs platform that generates llms.txt and markdown page versions for every site it hosts; GitBook - Serves an llms.txt file for published docs sites; Yoast SEO - WordPress plugin that generates and maintains an llms.txt file; AIOSEO - WordPress plugin with an llms.txt generator; Wix - Generates an llms.txt file for every Wix site."

"And various libraries and plugins are available to integrate the llms.txt specification into your workflow: JavaScript Implementation; `vitepress-plugin-llms`; `docusaurus-plugin-llms`; Drupal LLM Support; `llms-txt-php`; `VS Code PagePilot Extension`; `server-llm-txt` - MCP server that lets agents fetch and search llms.txt files."

### Next steps

"The `llms.txt` specification is open for community input. A GitHub repository hosts this informal overview, allowing for version control and public discussion. A community discord channel is available for sharing implementation experiences and discussing best practices."

## Pull notes — mechanical only

- `llmstxt.org` fetched via `curl` (no browser extension needed; static HTML, no JS-rendering wall, no login gate). HTTP 200, `Last-Modified: Mon, 21 Sep 2026 10:42:52 GMT` header on the response.
- Content verified byte-equivalent to the canonical GitHub-hosted markdown source at `raw.githubusercontent.com/AnswerDotAI/llms-txt/main/nbs/index.qmd` (also fetched today, HTTP 200); the qmd carries explicit YAML frontmatter (`date: 2024-09-03`, `date-modified: 2026-08-10`, `author: "Jeremy Howard"`) that the rendered HTML page does not surface as visible text, so the qmd's clean markdown was used for the verbatim extraction above rather than re-deriving it from HTML tag-stripping.
- Repo-root README at `github.com/AnswerDotAI/llms-txt/README.md` (guessed path) returned a 13-byte GitHub Pages placeholder, not the actual content — the real spec source lives at `nbs/index.qmd` (an nbdev/Quarto project), corrected during this pull per the pull-list substitution rule.
- The proposal text names its own adoption claim only in prose, unsourced: "thousands of sites publish an llms.txt file" — no n, no method, no date. Not used as an adoption number in the census; the census's adoption table draws on separately pulled crawl- and directory-based counts instead.
- The proposal explicitly names the three self-publishing AI labs and their own llms.txt URLs (OpenAI, Anthropic, Gemini) — cross-checked directly against those URLs in a separate measured-by-us pull, `d-structured-priority-engines-llms-txt-selfpublish-2026-09-22.md`.
- No mention of schema.org, JSON-LD, or product feeds as a *requirement* — the proposal frames llms.txt as coexisting with, not replacing, existing structured-data markup ("The file can also reference structured data markup used on the site").

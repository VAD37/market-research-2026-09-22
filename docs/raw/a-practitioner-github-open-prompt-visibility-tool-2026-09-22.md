# GitHub (ShaunM89) — "open-prompt-visibility: AI Visibility Tracker"

```yaml
source:          ShaunM89 (GitHub username), repository README, described as built by "Wayfinder AI"
url_or_doc_id:   https://github.com/ShaunM89/open-prompt-visibility
published:       undated — no date on page (repository shows "33 Commits" history; no explicit README publication date captured)
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, HTML converted to markdown)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     Open-source, MIT-licensed tool with published source code, a documented statistical method (Wilson confidence intervals, adaptive sampling), and a structured, versioned prompt-generation approach (prompts classified across four dimensions: intent, purchase stage, topic, query type; each with 2-3 phrasing variations). This is closer to the trust-rubric.md tier-4 "panel, clickstream, infrastructure telemetry... usable if method published" band, applied here to a self-hosted measurement instrument rather than a vendor panel: the method (Wilson CIs, adaptive stopping rule, CLI flags controlling n) is fully published in the README and, presumably, the source itself (not independently read in this pull). No independent replication of any specific tracked result — because the README documents the tool, not a specific brand's tracked outcome, there is no result to replicate. GitHub star count (2) and fork count (0) indicate minimal independent adoption at pull time.
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          Ollama (local models), OpenAI, Anthropic, HuggingFace — named as supported query targets; no specific model version fixed by the tool itself (user-configurable)
metric_kind:     none
supersedes:      none
captured:        section "Repository files navigation" through the CLI Tracking Commands table (truncated by fetch length cap before the remainder of the CLI reference, which is command-flag documentation not substantive to this pull)
vertical:        none named — generic "YourBrand" / "Competitor1" placeholder configuration, not tied to any real case or vertical
evidence_grade:  Not a case — this is a tool/method write-up, not a claimed result for any specific brand. No before/after figure is given anywhere in the captured README; "YourBrand" is a placeholder in the quick-start config example, not a real tracked entity. Filed as a method write-up (`a-practitioner-...` naming) per task instruction. Flagged as the strongest trust-raising candidate found in this cluster on the "published a prompt set or dataset" test (trust-rubric.md "Trust rises when... prompt set, raw data, or method appendix is published") — though note the caveat below: no dataset of *results* is published, only the *method and code* for generating a prompt set and running the tracker.
artefacts_published: method/tool — open-source code (MIT license), a documented prompt-generation and classification method, and a documented statistical method (Wilson confidence intervals, adaptive sampling), all published in the repository. No results dataset (no populated CSV/JSON export, no tracked brand's actual output) is published or linked.
direction:       null — no result claimed
```

## Verbatim

**Page title (browser tab):** GitHub - ShaunM89/open-prompt-visibility: A free, open source AI prompt visibility tracker built using open source tools by Wayfinder AI

ShaunM89 / open-prompt-visibility Public

- Notifications: You must be signed in to change notification settings
- Fork 0
- Star 2

Branches Tags
Latest commit
History
33 Commits

Folders and files: configs, frontend, src, tests, .env.example, .gitignore, CONFIG.md, CONTRIBUTING.md, LICENSE, README.md, main.py, pyproject.toml, requirements.txt

## Repository files navigation

# AI Visibility Tracker

Track how often AI chatbots mention your brand. Query multiple LLMs with test prompts, detect brand mentions in responses, and measure your visibility with statistical confidence.

## What It Does

When someone asks ChatGPT, Claude, or a local model "What are the best running shoes?", does your brand get mentioned? This tool answers that question systematically:

1. Sends test prompts to one or more LLMs (Ollama, OpenAI, Anthropic, HuggingFace)
2. Detects brand mentions using keyword matching and/or LLM-based analysis
3. Calculates visibility scores with Wilson confidence intervals
4. Compares against competitors to see where you stand
5. Tracks trends over time to see if visibility is improving
6. Segments visibility by intent, purchase stage, topic, and query type

## Key Features

- Multi-model support -- query Ollama (local), OpenAI, Anthropic, and HuggingFace from one config
- Statistical analysis -- confidence intervals, variance analysis, anomaly detection
- Sentiment detection -- analyze how brands are portrayed (positive/neutral/negative) with decoupled analysis LLM
- Adaptive sampling -- automatically stop querying when confidence intervals narrow enough
- Structured prompt sets -- generate and classify prompts across 4 dimensions (intent, purchase stage, topic, query type) with phrasing variations grouped under canonical IDs
- Segmented visibility analysis -- see how visibility differs by intent, topic, purchase stage, and branded vs unbranded queries
- CLI + Web Dashboard -- command-line interface and Next.js dashboard with Segments tab
- SQLite storage -- all results stored locally, exportable to CSV/JSON

## Prerequisites

- Python 3.9+ -- python.org/downloads
- Ollama (recommended) -- ollama.com/download
- Node.js 18+ (optional, for the web dashboard) -- nodejs.org

## Quick Start

### 1. Install

```
git clone https://github.com/ShaunM89/open-prompt-visibility.git
cd open-prompt-visibility
pip install -e .
```

### 2. Set up Ollama

```
# Install Ollama from https://ollama.com/download, then:
ollama pull gemma4:e2b
```

### 3. Configure your brands

Edit configs/users/brands.yaml with your brand and competitors:

```
brands:
- name: "YourBrand"
  keywords: ["YourBrand", "your brand"]
  competitors:
  - name: "Competitor1"
    keywords: ["Competitor1"]
  - name: "Competitor2"
    keywords: ["Competitor2"]
```

### 4. Generate a structured prompt set

```
# Generate 50 classified prompts across your brand's topics
pvt prompts generate --brand YourBrand --keywords keyword1,keyword2,keyword3
```

This creates a structured configs/users/prompts.yaml with prompts tagged by intent, purchase stage, topic, and query type. Each prompt gets 2-3 phrasing variations for robust testing.

### 5. Run tracking

```
pvt run --config configs/default.yaml
```

### 6. View results

```
# View brand trends with confidence intervals
pvt trends "YourBrand" --days 30 --ci 95
# View database statistics
pvt stats
# Export results
pvt export --format csv --output results.csv
```

## CLI Reference

### Tracking Commands

| Command | Description |
|---|---|
| pvt run | Run a tracking batch across all configured models |
| pvt run -v / pvt run --verbose | Show detailed output during run (progress, convergence, model stats) |
| pvt run --health-check | Only check model availability, don't run queries |
| pvt run --model-only ollama:gemma4:e2b | Run with only the specified model (overrides config) |
| pvt run --model ollama:gemma4:e2b | Add a model alongside configured models |
| pvt run --models ollama:gemma4:e2b,ollama:nemotron-3-nano:4b | Add multiple models (comma-separated) |
| pvt run --scenario full_comparison | Use a named scenario from config |
| pvt run --enable-variations | Run with auto-generated prompt variations |
| pvt run --num-variations 3 | Number of variations per base prompt (default: 3) |
| pvt run --variation-strategy semantic | Variation strategy: semantic, syntactic, or llm |
| pvt run --enable-auto-gen | Run with auto-generated brand prompts |
| pvt run --auto-gen-per-brand 10 | Number of auto-generated prompts per brand (default: 5) |
| pvt run --sentiment-mode fast | Run with post-batch sentiment analysis |
| pvt run --sentiment-mode detailed | Run with per-query sentiment analysis |
| pvt run --sentiment-mode off | Disable sentiment analysis |
| pvt run --analysis-model ollama:gemma4:e2b | Override the analysis LLM |
| pvt run --target-ci-width 15 | Set adaptive sampling CI target (e.g., 15 = ±7.5%) |
| pvt run --max-queries 100 | Cap queries per model×prompt pair for adaptive sampling |
| pvt run --convergence-scope primary_brand | Converge on primary brand only (default) |
| pvt run --convergence-scope all_tracked_brands | Converge across all tracked br[note: table truncated by fetch length cap]

[note: page continues past this point — remaining CLI reference rows, and any sections after "CLI Reference" (e.g. CONFIG.md-linked detail, example outputs, screenshots), were not captured in this pull.]

## Pull notes — mechanical only

- Fetched via MCP_DOCKER `fetch` tool (HTML-to-markdown conversion of the GitHub repository page), single pass at `max_length=6000`; the CLI reference table is long and was truncated mid-row by the length cap, not by the source.
- The repository's actual source code (the `src/` directory, `main.py`, the brand-mention detection logic, the Wilson-interval implementation) was not opened or read in this pull — only the rendered README as GitHub displays it on the repository landing page. The claim that the method is "published" rests on the README's description of the method plus the fact that the implementing code sits in the same public repository, not on a code-level audit performed in this session.
- No CONTRIBUTING.md, CONFIG.md, or LICENSE file was separately opened; their existence is noted from the file-listing table only.
- Attribution note in the page's own `<title>`/meta description: "built using open source tools by Wayfinder AI" — "Wayfinder AI" is not otherwise identified or investigated in this pull (unclear whether this is the author's own company, a tool/library credit, or an unrelated brand name); recorded verbatim, not resolved.

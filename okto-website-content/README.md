# okto-website-content

Internal content management plugin for the oktodigital website. Extract, audit, research, write, optimize, and export website content through a single conversational agent.

## Installation

```
/plugin install okto-website-content@oktodigital
```

## What It Does

A 9-mode conversational agent that manages all oktodigital website content. Talk to it naturally -- it infers the right mode from context.

| Mode | What It Does | Output |
|---|---|---|
| **Extract** | Crawl a URL into clean markdown | `content/extracted-{slug}.md` |
| **Audit** | Assess content quality, voice, SEO | Inline analysis |
| **Opportunity** | Find content gaps and page ideas | Inline recommendations |
| **Research** | Deep-dive a topic with web search + DataForSEO | `content/research-{topic}.md` |
| **Outline** | Structure a page before writing | `content/outline-{slug}.md` |
| **EEAT Interview** | Extract unique expertise via pointed questions | Inline notes |
| **Write** | Draft content in oktodigital voice | `content/draft-{slug}.md` |
| **Optimize** | Rewrite for PageOptimizer keyword targets | `content/optimized-{slug}.md` + `.html` |
| **Export** | Convert markdown to production HTML | `content/export-{slug}.html` |

## Commands

| Command | Purpose |
|---|---|
| `/okto-website-content` | Show modes, commands, and content status |
| `/okto-website-content-extract` | Quick extract: URL to markdown |
| `/okto-website-content-optimize` | Quick optimize: content + PO briefs |
| `/okto-website-content-export` | Quick export: markdown to HTML |
| `/okto-website-content-keywords` | Run keyword research via DataForSEO |

## Sub-Agents

The content-manager dispatches two sub-agents via Task tool:

- **web-crawler** -- 7-method cascade for crawling any URL (mcp-curl, Bash curl, Apify, Chrome Control, Chrome Automation, WebFetch, paste-in fallback)
- **dataforseo** -- SEO data retrieval via DataForSEO MCP tools (SERP analysis, keyword research, competitor intelligence, search volume, keyword difficulty)

## Voice

All content follows the oktodigital voice profile ("The Approachable Expert"):
- Core: Reliable (40%), Genuine (35%), Curious (25%)
- Formality: casual (contractions required, active voice 90%+)
- Readability: 9th-10th grade Flesch-Kincaid
- Anti-boring: minimum 1 element per piece

## PageOptimizer Workflow

The Optimize mode implements a 5-phase workflow for PageOptimizer.pro:
1. **Analyze** -- parse briefs, count keywords, identify gaps
2. **Plan** -- propose strategy, wait for approval
3. **Rewrite** -- execute plan, maintain voice
4. **Verify** -- keyword scorecard (MAXED/HIT/PARTIAL/MISS/OVER)
5. **Save + Export** -- write optimized .md + .html

## Hooks

- **Dash cleaner** -- PostToolUse hook on Write/Edit of .md files. Auto-corrects em-dash and hyphen usage per oktodigital style.

## MCP Dependencies

- **mcp-curl** -- HTTP requests with residential IP (web crawling)
- **Apify** -- Headless browser crawling (web crawling fallback)
- **Chrome Control / Chrome Automation** -- Browser-based crawling (web crawling fallback)
- **DataForSEO** -- SEO data API (keyword research, SERP analysis)

These are optional -- the plugin gracefully falls back when tools are unavailable.

## Directory Structure

```
okto-website-content/
  .claude-plugin/plugin.json
  agents/
    content-manager.md          Main agent (9 modes)
    web-crawler.md              Sub-agent: 7-method cascade
    dataforseo.md               Sub-agent: DataForSEO MCP tools
  commands/
    okto-website-content.md           Orientation
    okto-website-content-extract.md   Quick extract
    okto-website-content-optimize.md  Quick optimize
    okto-website-content-export.md    Quick export
    okto-website-content-keywords.md  Quick keywords
  hooks/
    hooks.json                  Hook registration
    dash-cleaner.js             Dash/hyphen auto-correction
  references/
    voice-definition.md         15-dimension voice profile
    content-templates.md        Channel-specific tone adjustments
    anti-boring-principles.md   Anti-boring rules + banned phrases
    eeat-methodology.md         EEAT pointed question methodology
    ux-components.md            82 UX components across 10 categories
    content-formatting-rules.md Heading hierarchy, TLDR, F/Z patterns
    seo-metadata-rules.md       Meta title/description rules
    conversion-patterns.md      CTA patterns, social proof
    writing-rules.md            Content generation rules
    dispatch-protocol.md        Sub-agent dispatch protocol
    pageoptimizer/
      po-rules.md               5-phase workflow
      brief-parsing.md          PO brief format + parsing
      keyword-verification.md   Keyword counting methodology
      html-export-rules.md      Markdown to HTML conversion
    web-crawler/
      formatting-rules.md       HTML-to-markdown conversion
      crawl-methods/             6 method-specific guides
    dataforseo/
      tool-catalog.md           DataForSEO MCP tool reference
```

---
description: "webtools-crawler: Crawl a URL and return content in the requested format"
allowed-tools: Task
argument-hint: [URL]
---

Crawl a URL and return content tailored to the caller's needs. Dispatches the web-crawler agent as a sub-agent.

## Usage

`/webtools-crawler-run [URL]`

If no URL argument is provided, ask the operator for the URL to crawl.

## Output Decision Framework

Before dispatching the crawler, decide what output you need based on your context:

| Your context | Output instruction to include |
|---|---|
| Gathering intelligence / research | "Extended summary with key facts, services, contact info. Preserve internal page links." |
| Extracting exact content for reproduction | "Exact page content as formatted markdown. Preserve all links, images, structure." |
| Mapping site structure | "Navigation links and page hierarchy only. Skip body content." |
| Profiling a page quickly | "Metadata and h1 only. Minimal output." |
| Auditing technology / scripts | "Script sources, meta tags, technology indicators only." |
| Raw data for custom processing | "Raw HTML with no processing." |
| General-purpose / unsure | Omit instructions -- the crawler defaults to clean markdown with metadata. |

Include your decision as output instructions in the dispatch prompt. If unsure, omit instructions -- the crawler defaults to clean markdown with metadata headers.

## Dispatch

Dispatch the web-crawler as a sub-agent via Task tool:

```
Task(subagent_type="general-purpose", prompt="You are the web-crawler agent. Crawl this URL and return content: [URL]

Read and follow the agent definition at: ${CLAUDE_PLUGIN_ROOT}/agents/web-crawler.md

MCP tools available in this session:
- Desktop Commander: mcp__Desktop_Commander__start_process, mcp__Desktop_Commander__read_file, mcp__Desktop_Commander__write_file (local machine curl with residential IP, best content completeness)
- Apify: mcp__Apify__call-actor, mcp__Apify__get-actor-output (headless browser crawling, WAF bypass)
- Chrome Control: mcp__Control_Chrome__open_url, mcp__Control_Chrome__get_page_content, mcp__Control_Chrome__execute_javascript, mcp__Control_Chrome__close_tab (browser tab control, fetch-based)
- Chrome Automation: mcp__Claude_in_Chrome__navigate, mcp__Claude_in_Chrome__read_page, mcp__Claude_in_Chrome__screenshot, mcp__Claude_in_Chrome__click (full browser automation with JS rendering)

[EXTRACTION_FOCUS if provided]

[OUTPUT_INSTRUCTIONS if provided -- e.g., 'Output instructions: Return extended summary with key facts and services. Telegraphic, no prose.']

Return the full result with metadata headers.")
```

**OUTPUT_INSTRUCTIONS passthrough:** When another plugin dispatches the crawler programmatically, it includes output instructions in the Task prompt. The crawler agent reads these and formats its output accordingly. If no output instructions are included, the crawler defaults to clean markdown with metadata headers.

When the sub-agent returns, present the result to the operator as-is. Do not reprocess or summarize.

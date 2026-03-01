---
description: "webtools-init: Crawl a URL and return clean markdown content with metadata"
allowed-tools: Task
argument-hint: [URL]
---

Crawl a URL and return clean markdown content with preserved structure and metadata. Dispatches the web-crawler agent as a sub-agent.

## Usage

`/webtools-init-crawl [URL]`

If no URL argument is provided, ask the operator for the URL to crawl.

## Dispatch

Dispatch the web-crawler as a sub-agent via Task tool:

```
Task(subagent_type="general-purpose", prompt="You are the web-crawler agent. Crawl this URL and return clean markdown content with metadata: [URL]

Read and follow the agent definition at: ${CLAUDE_PLUGIN_ROOT}/agents/web-crawler.md

MCP tools available in this session:
- Desktop Commander: mcp__Desktop_Commander__start_process, mcp__Desktop_Commander__read_file, mcp__Desktop_Commander__write_file (local machine curl with residential IP, best content completeness)
- Apify: mcp__Apify__call-actor, mcp__Apify__get-actor-output (headless browser crawling, WAF bypass)
- Chrome Control: mcp__Control_Chrome__open_url, mcp__Control_Chrome__get_page_content, mcp__Control_Chrome__execute_javascript, mcp__Control_Chrome__close_tab (browser tab control, fetch-based)
- Chrome Automation: mcp__Claude_in_Chrome__navigate, mcp__Claude_in_Chrome__read_page, mcp__Claude_in_Chrome__screenshot, mcp__Claude_in_Chrome__click (full browser automation with JS rendering)

[EXTRACTION_FOCUS if provided]

Return the full cleaned content with metadata headers.")
```

When the sub-agent returns, present the result to the operator as-is. Do not reprocess or summarize.

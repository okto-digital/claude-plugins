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
- Apify: mcp__apify__call-actor, mcp__apify__get-actor-output (headless browser crawling, WAF bypass)
- Desktop Commander: mcp__desktop-commander__start_process, mcp__desktop-commander__read_file, mcp__desktop-commander__write_file (local machine curl with residential IP, use when Bash gets WAF blocked HTTP 403 / exit code 56)
- Playwright: mcp__playwright__playwright_navigate, mcp__playwright__playwright_evaluate, mcp__playwright__playwright_get_visible_html (browser-based fetch and navigation)

[EXTRACTION_FOCUS if provided]

Return the full cleaned content with metadata headers.")
```

When the sub-agent returns, present the result to the operator as-is. Do not reprocess or summarize.

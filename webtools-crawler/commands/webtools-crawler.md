---
description: "webtools-crawler: Show available commands and crawling capabilities"
allowed-tools: Read
---

Show available webtools-crawler commands and capabilities.

---

## Orientation Display

```
[CRAWLER] Webtools Crawler -- Unified Web Crawling

Commands:
  /webtools-crawler              Show this overview
  /webtools-crawler-run          Crawl a URL and return content in requested format

Agent:
  web-crawler.md                 7-method cascade with caller-driven output formats

Crawl method cascade (in order):
  1. curl via Desktop Commander   Local machine, residential IP, best WAF bypass
  2. curl via Bash                Standard shell, may use datacenter IP
  3. Apify MCP                   Headless browser, good WAF bypass
  4. Chrome Control Fetch         Browser fetch() API, user's IP
  5. Chrome Automation Nav        Full browser with JS rendering
  6. WebFetch                     Built-in Claude Code tool, datacenter IP
  7. Paste-in                     Manual fallback

Output formats (caller-driven):
  The calling agent decides what output it needs based on its role and token budget.
  Default: clean markdown with metadata headers.
  Examples: "return only navigation links", "metadata only", "raw factual data",
  "exact page content as formatted markdown", "raw HTML".

Reference files:
  crawl-methods/                 Method-specific instructions (6 files)
  formatting-rules.md            HTML-to-markdown conversion rules

Cross-plugin usage:
  Other plugins dispatch the web-crawler agent via Task tool.
  See /webtools-crawler-run for the dispatch pattern.
```

# Sub-Agent Dispatch Protocol

**Source:** Adapted from Orion dispatch-subagent skill v2.0.0
**Purpose:** Standard protocol for dispatching web-crawler and dataforseo sub-agents via the Task tool.

---

## Dispatch Modes

### MCP Mode (general-purpose)

Used for agents that need external MCP tools (web crawling, SEO API calls).

- `subagent_type="general-purpose"` -- loads all MCP tools
- Full template with agent definition inlined and MCP tool hints
- `${CLAUDE_PLUGIN_ROOT}` resolved to absolute path before inlining

### Model Selection

| Model | When | Why |
|---|---|---|
| `sonnet` | Standard work: crawling, keyword research, data extraction | Follows complex instructions reliably. Default choice. |
| `opus` | Analysis, synthesis, content strategy, complex reasoning | Needs to analyze, interpret, produce analytical output. |
| `haiku` | Simple lookups, metadata-only tasks | Fastest, cheapest. |

---

## MCP Tool Hints

Include these hints in the dispatch prompt for each sub-agent.

### Web-Crawler Tools

```
## MCP Tools

- mcp-curl: mcp__mcp-curl__curl_get (HTTP GET with residential IP), mcp__mcp-curl__curl_advanced (custom curl args with residential IP). Use Bash for post-fetch processing (HTML stripping, scripts).
- Apify: mcp__Apify__call-actor, mcp__Apify__get-actor-output (headless browser crawling, WAF bypass)
- Chrome Control: mcp__Control_Chrome__open_url, mcp__Control_Chrome__get_page_content, mcp__Control_Chrome__execute_javascript, mcp__Control_Chrome__close_tab (browser tab control, fetch-based)
- Chrome Automation: mcp__Claude_in_Chrome__navigate, mcp__Claude_in_Chrome__read_page, mcp__Claude_in_Chrome__screenshot, mcp__Claude_in_Chrome__click (full browser automation with JS rendering)
```

### DataForSEO Tools

```
## MCP Tools

- DataForSEO: mcp__dataforseo__serp_organic_live_advanced, mcp__dataforseo__serp_locations, mcp__dataforseo__kw_data_google_ads_search_volume, mcp__dataforseo__kw_data_dfs_trends_explore, mcp__dataforseo__on_page_lighthouse, mcp__dataforseo__on_page_instant_pages, mcp__dataforseo__on_page_content_parsing, mcp__dataforseo__dataforseo_labs_google_ranked_keywords, mcp__dataforseo__dataforseo_labs_google_competitors_domain, mcp__dataforseo__dataforseo_labs_google_domain_rank_overview, mcp__dataforseo__dataforseo_labs_google_keyword_ideas, mcp__dataforseo__dataforseo_labs_google_related_keywords, mcp__dataforseo__dataforseo_labs_bulk_keyword_difficulty, mcp__dataforseo__dataforseo_labs_search_intent, mcp__dataforseo__business_data_business_listings_search, mcp__dataforseo__domain_analytics_technologies_domain_technologies, mcp__dataforseo__content_analysis_search (SEO data, SERP analysis, keyword research, technology detection, business listings)
```

---

## Dispatch Template

```
Task(
  subagent_type="general-purpose",
  model="[selected model]",
  prompt="You are the [agent-name] agent. [task-specific instruction]

## Working Directory

[absolute path of the current project directory]

ALL file paths (Read and Write) MUST use absolute paths based on this directory. NEVER use relative paths.

## Plugin Root

[resolved absolute path of the plugin root directory]

## Tool Restrictions

Use the built-in Read tool to read files. Use the built-in Write tool to write files. Use mcp-curl ONLY for HTTP requests. Use Bash for post-fetch processing (HTML stripping, scripts). NEVER use MCP tools for file operations.

## Agent Definition

[full content of the agent definition file, inlined with ${CLAUDE_PLUGIN_ROOT} resolved]

## MCP Tools

[MCP hints from lookup table above]

[Additional context if any]

[Output instructions if any]

Return the full result."
)
```

---

## Rules

- **ALWAYS** resolve `${CLAUDE_PLUGIN_ROOT}` to an absolute path before inlining agent definitions
- **NEVER** pass `${CLAUDE_PLUGIN_ROOT}` unresolved to sub-agents
- **ALWAYS** include the MCP Tool Hints block for MCP-mode agents
- **ALWAYS** include the Working Directory and Plugin Root blocks
- **ALWAYS** include Tool Restrictions to prevent MCP abuse for file operations
- One agent per dispatch -- do not combine multiple agents in a single Task call

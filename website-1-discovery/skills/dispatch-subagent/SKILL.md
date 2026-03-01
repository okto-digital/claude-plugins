---
name: dispatch-subagent
description: "Dispatch a sub-agent via the Task tool with correct model selection, MCP tool hints, and agent definition loading. ALWAYS use before spawning any sub-agent. Invoke whenever a sub-agent needs to be dispatched via Task tool, the pipeline delegates work to a specialist agent, or a Task call to a registered agent is required."
allowed-tools: Task, Read, Glob
version: 1.2.0
---

# Dispatch Sub-Agent

Dispatch any registered agent as a sub-agent via the Task tool. Ensures correct model selection, MCP tool availability hints, agent definition loading, and output handling.

---

## Agent Registry

| Agent | Path | Purpose |
|---|---|---|
| web-crawler | `${CLAUDE_PLUGIN_ROOT}/agents/web-crawler.md` | Crawl a URL, return content in requested format |
| domain-analyst | `${CLAUDE_PLUGIN_ROOT}/agents/domain-analyst.md` | Analyze one domain's checkpoints against research context |
| researcher | `${CLAUDE_PLUGIN_ROOT}/agents/researcher.md` | Execute domain-specific research, produce R-document |

Add new agents to this table as the pipeline grows.

---

## Dispatch Protocol

Follow these steps for every sub-agent dispatch:

### 1. Identify the agent

Look up the agent in the registry above. If the requested agent is not registered, stop and inform the operator.

### 2. Read the agent's tool requirements

Read the agent definition file. Check the frontmatter `tools:` field for MCP wildcards (e.g., `mcp__Desktop_Commander__*`). These indicate which MCP servers the agent may use.

### 3. Select the model

Choose the Task model based on what the agent needs to **do** with its result:

| Model | When | Why |
|---|---|---|
| `haiku` | Mechanical extraction, simple lookups, metadata-only tasks | No reasoning needed. Fastest, cheapest. |
| `sonnet` | Standard work requiring judgment -- conversion, following procedures, multi-step execution | Needs to follow complex instructions reliably. Default choice. |
| `opus` | Analysis, synthesis, research summaries, complex reasoning | Needs to analyze, interpret, and produce analytical output. |

**Rule of thumb:** If the task says "only" or "just" -- haiku. If it needs reliable procedure-following -- sonnet. If it needs reasoning or synthesis -- opus.

### 4. Build MCP tool hints

For each MCP wildcard in the agent's `tools:` field, include the corresponding hints from the MCP Tool Hints table below. Only include hints for MCP servers the agent actually uses.

### 5. Construct the dispatch prompt

Use the dispatch template below, filling in:
- Agent name (from registry)
- Agent definition path (from registry)
- Task-specific instruction (what to do)
- MCP tool hints (from step 4)
- Additional context or extraction focus (if any)
- Output instructions (if any)

### 6. Call Task tool

```
Task(
  subagent_type="general-purpose",
  model="[selected model]",
  prompt="[constructed prompt]"
)
```

### 7. Handle the result

Present the sub-agent's result as-is unless the caller explicitly needs transformation. Do not summarize or reprocess. If the sub-agent reports failure, surface the failure reason to the operator.

---

## MCP Tool Hints

Lookup table mapping agent `tools:` wildcards to specific tool names. Include these in the dispatch prompt so the sub-agent knows what MCP tools are available without probing.

| Wildcard | Hint block to include |
|---|---|
| `mcp__Desktop_Commander__*` | `- Desktop Commander: mcp__Desktop_Commander__start_process, mcp__Desktop_Commander__read_file, mcp__Desktop_Commander__write_file (local machine shell with residential IP)` |
| `mcp__Apify__*` | `- Apify: mcp__Apify__call-actor, mcp__Apify__get-actor-output (headless browser crawling, WAF bypass)` |
| `mcp__Control_Chrome__*` | `- Chrome Control: mcp__Control_Chrome__open_url, mcp__Control_Chrome__get_page_content, mcp__Control_Chrome__execute_javascript, mcp__Control_Chrome__close_tab (browser tab control, fetch-based)` |
| `mcp__Claude_in_Chrome__*` | `- Chrome Automation: mcp__Claude_in_Chrome__navigate, mcp__Claude_in_Chrome__read_page, mcp__Claude_in_Chrome__screenshot, mcp__Claude_in_Chrome__click (full browser automation with JS rendering)` |
| `mcp__dataforseo__*` | `- DataForSEO: mcp__dataforseo__serp_organic_live_advanced, mcp__dataforseo__serp_locations, mcp__dataforseo__kw_data_google_ads_search_volume, mcp__dataforseo__kw_data_dfs_trends_explore, mcp__dataforseo__on_page_lighthouse, mcp__dataforseo__on_page_instant_pages, mcp__dataforseo__on_page_content_parsing, mcp__dataforseo__dataforseo_labs_google_ranked_keywords, mcp__dataforseo__dataforseo_labs_google_competitors_domain, mcp__dataforseo__dataforseo_labs_google_domain_rank_overview, mcp__dataforseo__dataforseo_labs_google_keyword_ideas, mcp__dataforseo__dataforseo_labs_google_related_keywords, mcp__dataforseo__business_data_business_listings_search, mcp__dataforseo__domain_analytics_technologies_domain_technologies, mcp__dataforseo__content_analysis_search (SEO data, SERP analysis, technology detection, business listings)` |

Add rows as new MCP servers are configured.

---

## Dispatch Template

```
Task(
  subagent_type="general-purpose",
  model="[selected model]",
  prompt="You are the [agent-name] agent. [task-specific instruction]

Read and follow the agent definition at: ${CLAUDE_PLUGIN_ROOT}/agents/[agent-name].md

MCP tools available in this session:
[MCP hints from lookup table -- only those matching the agent's tools: field]

[Additional context if any]

[Output instructions if any]

Return the full result."
)
```

**Placeholders:**
- `[agent-name]` -- from the Agent Registry
- `[selected model]` -- from step 3
- `[task-specific instruction]` -- what the agent should do (e.g., "Crawl this URL and return content: https://example.com")
- `[MCP hints]` -- assembled from the MCP Tool Hints table, one line per MCP server
- `[Additional context]` -- extraction focus, format preferences, constraints
- `[Output instructions]` -- what the caller needs back (e.g., "Output instructions: Return extended summary with key facts. Telegraphic, no prose.")

---

## Rules

- **ALWAYS** use this skill before spawning any sub-agent via Task tool
- **ALWAYS** include MCP tool hints for every MCP wildcard in the agent's `tools:` field
- **NEVER** dispatch an agent not listed in the registry -- add it first
- **NEVER** hard-code MCP tool names in the dispatch prompt without checking the agent's `tools:` field
- Pass output instructions through verbatim -- let the sub-agent decide how to format
- One agent per dispatch -- do not combine multiple agents in a single Task call

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
| dataforseo | `${CLAUDE_PLUGIN_ROOT}/agents/dataforseo.md` | Fetch live SEO data (SERP, keywords, backlinks, on-page, competitors, AI visibility) |
| dataforseo-api | `${CLAUDE_PLUGIN_ROOT}/agents/dataforseo-api.md` | Fetch DataForSEO data via direct HTTP API (mcp-curl) |
| researcher | `${CLAUDE_PLUGIN_ROOT}/agents/researcher.md` | Execute one research substage, produce R{n}.json + R{n}.md |
| domain-analyst | `${CLAUDE_PLUGIN_ROOT}/agents/domain-analyst.md` | Assess one domain's checkpoints against project research, produce per-domain JSON + MD |
| concept-creator | `${CLAUDE_PLUGIN_ROOT}/agents/concept-creator.md` | Produce one concept section from research + gap analysis, write per-section JSON + MD |

Add new agents to this table as the pipeline grows.

---

## Dispatch Protocol

Follow these steps for every sub-agent dispatch:

### 1. Identify the agent

Look up the agent in the registry above. If the requested agent is not registered, stop and inform the operator.

### 2. Read the agent definition

Read the agent definition file at the path from the registry. You will need:
- The frontmatter `tools:` field — check for MCP wildcards (e.g., `mcp__mcp-curl__*`) to determine which MCP hints to include.
- The full file content — to inline in the dispatch prompt (sub-agents cannot resolve `${CLAUDE_PLUGIN_ROOT}` paths, so the content must be included directly).

**Path resolution:** Before inlining, replace all `${CLAUDE_PLUGIN_ROOT}` occurrences in the content with the actual absolute path of the plugin root directory. You know this path because you used it to read the file. This ensures the sub-agent can read any reference files mentioned in the agent definition using the Read tool.

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
- Agent definition content (read in step 2 — inline the full content, not a path)
- Task-specific instruction (what to do)
- MCP tool hints (from step 4)
- Additional context or extraction focus (if any)
- Output instructions (if any)

### 6. Debug log (when enabled)

If the operator has requested debug mode (`debug: true` in project-state.md or by saying "enable debug"), write the full constructed prompt to `debug/dispatch-{agent-name}-{timestamp}.md` before dispatching. This lets the operator inspect exactly what the sub-agent receives.

### 7. Call Task tool

```
Task(
  subagent_type="general-purpose",
  model="[selected model]",
  prompt="[constructed prompt]"
)
```

### 8. Handle the result

Present the sub-agent's result as-is unless the caller explicitly needs transformation. Do not summarize or reprocess. If the sub-agent reports failure, surface the failure reason to the operator.

---

## MCP Tool Hints

Lookup table mapping agent `tools:` wildcards to specific tool names. Include these in the dispatch prompt so the sub-agent knows what MCP tools are available without probing.

| Wildcard | Hint block to include |
|---|---|
| `mcp__mcp-curl__*` | `- mcp-curl: mcp__mcp-curl__curl_get (HTTP GET with residential IP), mcp__mcp-curl__curl_advanced (custom curl args with residential IP). Use Bash for post-fetch processing (HTML stripping, scripts).` |
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

## Working Directory

[absolute path of the current project directory — where output files should be written]

ALL file paths (Read and Write) MUST use absolute paths based on this directory. For example, to write `research/R2-Keywords.json`, use `[working directory]/research/R2-Keywords.json`. NEVER use relative paths — they resolve to the wrong location in Cowork sessions.

## Plugin Root

[resolved absolute path of the plugin root directory]

Any file paths containing `${CLAUDE_PLUGIN_ROOT}` should be read by replacing that variable with the path above.

## Tool Restrictions

Use the built-in Read tool to read files. Use the built-in Write tool to write files. Use mcp-curl ONLY for HTTP requests. Use Bash for post-fetch processing (HTML stripping, scripts). NEVER use MCP tools for file operations.

## Agent Definition

[full content of the agent definition file, inlined from step 2 with ${CLAUDE_PLUGIN_ROOT} resolved]

## MCP Tools

[MCP hints from lookup table -- only those matching the agent's tools: field]

[Additional context if any]

[Output instructions if any]

Return the full result."
)
```

**Placeholders:**
- `[agent-name]` -- from the Agent Registry
- `[selected model]` -- from step 3
- `[working directory]` -- absolute path of the current project directory (use `pwd` or read from project-state.md). This is where the sub-agent writes output files. Critical for Cowork sessions where relative paths resolve to the container root, not the project directory.
- `[agent definition content]` -- full content of the agent .md file read in step 2 with `${CLAUDE_PLUGIN_ROOT}` resolved to absolute paths
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
- **NEVER** pass `${CLAUDE_PLUGIN_ROOT}` paths to sub-agents — they cannot resolve this variable. Always inline file content or pass absolute paths resolved by the orchestrator
- Pass output instructions through verbatim -- let the sub-agent decide how to format
- One agent per dispatch -- do not combine multiple agents in a single Task call

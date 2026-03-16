---
name: dispatch-subagent
description: "Dispatch a sub-agent via the Task tool with correct model selection, dispatch mode, and agent definition loading. Required before any sub-agent Task dispatch. Invoke whenever a sub-agent needs to be dispatched via Task tool, the pipeline delegates work to a specialist agent, or a Task call to a registered agent is required."
allowed-tools: Task, Read, Glob
version: 2.0.0
---

# Dispatch Sub-Agent

Dispatch any registered agent as a sub-agent via the Task tool. Automatically selects between two dispatch modes based on the agent's MCP requirements:

- **MCP mode** — `subagent_type="general-purpose"`, full template with MCP hints. For agents that need external tools (web crawling, API calls).
- **Lightweight mode** — `subagent_type="[agent-name]"`, lean template without MCP. For agents that only use Read/Write. Saves ~25% context by avoiding MCP tool definition loading.

---

## Agent Registry

| Agent | Path | Purpose |
|---|---|---|
| web-crawler | `${CLAUDE_PLUGIN_ROOT}/agents/web-crawler.md` | Crawl a URL, return content in requested format |
| dataforseo | `${CLAUDE_PLUGIN_ROOT}/agents/dataforseo.md` | Fetch live SEO data (SERP, keywords, backlinks, on-page, competitors, AI visibility) |
| researcher | `${CLAUDE_PLUGIN_ROOT}/agents/researcher.md` | Execute one research substage, produce R{n}.json + R{n}.md |
| domain-analyst | `${CLAUDE_PLUGIN_ROOT}/agents/domain-analyst.md` | Assess a group of domains' checkpoints, produce per-domain findings + questions |
| concept-creator | `${CLAUDE_PLUGIN_ROOT}/agents/concept-creator.md` | Produce one concept section from pre-merged context, write per-section JSON + MD |
| concept-reviewer | `${CLAUDE_PLUGIN_ROOT}/agents/concept-reviewer.md` | Read D5-Concept.json, check inter-section coherence, write D5-Review-Notes.md |
| domain-finalizer | `${CLAUDE_PLUGIN_ROOT}/agents/domain-finalizer.md` | Finalize one domain's G-file: rewrite client evidence, add TLDR, update summary + counts |
| question-curator | `${CLAUDE_PLUGIN_ROOT}/agents/question-curator.md` | Classify, deduplicate, rewrite D4 questions into CLIENT/AGENCY/DEDUCED/PLAYBOOK buckets |

---

## Dispatch Protocol

### 1. Identify the agent

Look up the agent in the registry. If not registered, stop and inform the operator.

### 2. Read the agent definition and determine dispatch mode

Read the agent definition file. Check the frontmatter `tools:` field for MCP wildcards (patterns like `mcp__*`). Convention: MCP agents use inline comma-separated `tools:` format; lightweight agents use YAML list format. Both are valid.

- **MCP wildcards found** → **MCP mode**: agent needs external tools, dispatch as `general-purpose`
- **No MCP wildcards** → **Lightweight mode**: agent uses only built-in tools, dispatch as named agent

**For MCP mode only:** extract the full file content for inlining. Replace all `${CLAUDE_PLUGIN_ROOT}` occurrences with the actual absolute plugin root path.

**For Lightweight mode:** no inlining needed — Claude Code loads the agent definition automatically from the plugin's agents directory.

### 3. Select the model

| Model | When | Why |
|---|---|---|
| `haiku` | Mechanical extraction, simple lookups, metadata-only tasks | No reasoning needed. Fastest, cheapest. |
| `sonnet` | Standard work requiring judgment, following procedures, multi-step execution | Needs to follow complex instructions reliably. Default choice. |
| `opus` | Analysis, synthesis, research summaries, complex reasoning | Needs to analyze, interpret, and produce analytical output. |

### 4. Build MCP tool hints (MCP mode only)

Skip this step for Lightweight mode.

For each MCP wildcard in the agent's `tools:` field, include the corresponding hints from the MCP Tool Hints table below.

### 5. Construct the dispatch prompt

Use the appropriate template based on dispatch mode (see templates below).

### 6. Debug log and debug output (when enabled)

If `research_config.debug` is `true` in D1-Init.json:
- Write the full dispatch prompt to `tmp/dispatch-{agent-name}-{timestamp}.md` before dispatching.
- Append to the dispatch prompt: "Debug mode is ON. For every `.md` file you write, also write a `-debug.txt` companion in `tmp/debug/`: telegraphic, bullet points, key facts only, no prose, no template structure."

### 7. Call Task tool

**MCP mode:**
```
Task(
  subagent_type="general-purpose",
  model="[selected model]",
  prompt="[MCP template]"
)
```

**Lightweight mode:**
```
Task(
  subagent_type="[agent-name]",
  model="[selected model]",
  prompt="[Lightweight template]"
)
```

### 8. Handle the result

Present the sub-agent's result as-is. If the sub-agent reports failure, surface the failure reason to the operator.

### 9. Validate JSON outputs (when applicable)

If the dispatched agent was expected to produce JSON files, the **calling skill** (not dispatch-subagent) should validate them after dispatch returns:

```bash
scripts/validate-json.sh {expected-output-files}
```

If validation fails:
1. Attempt jq-based repair: `jq -c '.' broken.json > fixed.json && mv fixed.json broken.json`
2. If jq cannot parse it either, re-dispatch the agent for the failed file only
3. If second dispatch also fails, report to operator

This step is documented here for reference but executed by the parent skill (domain-gap-analysis, concept-creation, project-research) which has Bash access.

---

## MCP Tool Hints

| Wildcard | Hint block to include |
|---|---|
| `mcp__mcp-curl__*` | `- mcp-curl: mcp__mcp-curl__curl_get (HTTP GET with residential IP), mcp__mcp-curl__curl_advanced (custom curl args with residential IP). Use Bash for post-fetch processing (HTML stripping, scripts).` |
| `mcp__Apify__*` | `- Apify: mcp__Apify__call-actor, mcp__Apify__get-actor-output (headless browser crawling, WAF bypass)` |
| `mcp__Control_Chrome__*` | `- Chrome Control: mcp__Control_Chrome__open_url, mcp__Control_Chrome__get_page_content, mcp__Control_Chrome__execute_javascript, mcp__Control_Chrome__close_tab (browser tab control, fetch-based)` |
| `mcp__Claude_in_Chrome__*` | `- Chrome Automation: mcp__Claude_in_Chrome__navigate, mcp__Claude_in_Chrome__read_page, mcp__Claude_in_Chrome__screenshot, mcp__Claude_in_Chrome__click (full browser automation with JS rendering)` |
| `mcp__dataforseo__*` | `- DataForSEO: mcp__dataforseo__serp_organic_live_advanced, mcp__dataforseo__serp_locations, mcp__dataforseo__kw_data_google_ads_search_volume, mcp__dataforseo__kw_data_dfs_trends_explore, mcp__dataforseo__on_page_lighthouse, mcp__dataforseo__on_page_instant_pages, mcp__dataforseo__on_page_content_parsing, mcp__dataforseo__dataforseo_labs_google_ranked_keywords, mcp__dataforseo__dataforseo_labs_google_competitors_domain, mcp__dataforseo__dataforseo_labs_google_domain_rank_overview, mcp__dataforseo__dataforseo_labs_google_keyword_ideas, mcp__dataforseo__dataforseo_labs_google_related_keywords, mcp__dataforseo__business_data_business_listings_search, mcp__dataforseo__domain_analytics_technologies_domain_technologies, mcp__dataforseo__content_analysis_search (SEO data, SERP analysis, technology detection, business listings)` |

---

## Dispatch Templates

### MCP Template (general-purpose)

```
Task(
  subagent_type="general-purpose",
  model="[selected model]",
  prompt="You are the [agent-name] agent. [task-specific instruction]

## Working Directory

[absolute path of the current project directory]

ALL file paths (Read and Write) MUST use absolute paths based on this directory. NEVER use relative paths — they resolve to the wrong location in Cowork sessions.

## Plugin Root

[resolved absolute path of the plugin root directory]

## Tool Restrictions

Use the built-in Read tool to read files. Use the built-in Write tool to write files. Use mcp-curl ONLY for HTTP requests. Use Bash for post-fetch processing (HTML stripping, scripts). NEVER use MCP tools for file operations.

## Temporary Files

ALL intermediate/temporary files (downloads, HTML stripping, debug logs, analysis scratch) MUST be written to `{working_directory}/tmp/`. NEVER write temporary files to the project root or any other directory.

## Agent Definition

[full content of the agent definition file, inlined with ${CLAUDE_PLUGIN_ROOT} resolved]

## MCP Tools

[MCP hints from lookup table]

[Additional context if any]

[Output instructions if any]

Return the full result."
)
```

### Lightweight Template (named agent)

```
Task(
  subagent_type="[agent-name]",
  model="[selected model]",
  prompt="[task-specific instruction]

## Working Directory

[absolute path of the current project directory]

ALL file paths (Read and Write) MUST use absolute paths based on this directory. NEVER use relative paths — they resolve to the wrong location in Cowork sessions.

## Temporary Files

ALL intermediate/temporary files MUST be written to `{working_directory}/tmp/`. NEVER write temporary files to the project root.

[Additional context if any]

[Output instructions if any]

Return the full result."
)
```

**Key differences:** Lightweight template omits Plugin Root, Tool Restrictions, Agent Definition (loaded by Claude Code from the plugin), and MCP Tools. The prompt contains only the task-specific payload.

---

## Rules

- **ALWAYS** use this skill before spawning any sub-agent via Task tool
- **ALWAYS** determine dispatch mode from the agent's `tools:` field before constructing the prompt
- **NEVER** dispatch an agent not listed in the registry — add it first
- **NEVER** use `general-purpose` for agents without MCP wildcards — use Lightweight mode
- **NEVER** pass `${CLAUDE_PLUGIN_ROOT}` paths to sub-agents — inline content or use resolved absolute paths
- One agent per dispatch — do not combine multiple agents in a single Task call

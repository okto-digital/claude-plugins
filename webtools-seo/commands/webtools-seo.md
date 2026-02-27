---
description: "webtools-seo: Show available SEO commands, skills, data source status, and current project state"
allowed-tools: Read, Glob
---

Show available webtools-seo commands, current SEO keyword research status, data source availability, and suggested next step.

---

## Read Project State

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: skip to the "No Project" output below.
- If it DOES exist: parse the Project Info (client name, project type) and the Document Log.

### 2. Document Status Check

Check existence of each relevant document:
- `brief/D1-project-brief.md` -- required input for keyword research
- `seo/D3-seo-keyword-map.md` -- keyword research output
- `research/R1-serp-landscape.md` -- research intelligence (SERP seeds)
- `research/R5-content-strategy.md` -- research intelligence (content gaps)
- `research/D15-research-report.md` -- research intelligence (strategic focus)

For each file: report "complete" if it exists, "not found" if it does not.

If D3 exists, read its YAML frontmatter and extract `data_tier` and `data_source` values. Also check its `dependencies` list to see if R1, R5, or D15 were used when it was created.

### 3. MCP Tool Detection

Probe available tool names for these substrings:
- `dataforseo` or `datalabs` -> DataForSEO is available
- `seo-data-api` or `seranking` or `DATA_` -> SE Ranking is available
- Neither found -> No MCP tools detected

Determine active tier:
- DataForSEO detected -> TIER 1 (DataForSEO)
- SE Ranking detected (no DataForSEO) -> TIER 1 (SE Ranking)
- No MCP tools -> TIER 2 (WebSearch) or TIER 3 (Estimates)

---

## Display Overview

### With Active Project

```
[SEO] Webtools SEO -- [client name]

Available commands:
  /webtools-seo                  Show this overview
  /webtools-seo-keywords         Run keyword research (produces D3)

Available skills:
  webtools-seo:seo-keyword-research    Structured keyword research with clustering

Data sources:
  DataForSEO MCP:    [available / not detected]
  SE Ranking MCP:    [available / not detected]
  Active tier:       [TIER 1 (DataForSEO) / TIER 1 (SE Ranking) / TIER 2 (WebSearch) / TIER 3 (Estimates)]

Research intelligence:
  R1 SERP Landscape:     [complete / not found]
  R5 Content Strategy:   [complete / not found]
  D15 Research Report:   [complete / not found]

Current state:
  D1 Project Brief:      [complete / not found]
  D3 SEO Keyword Map:    [complete (TIER X, source) / not started]

Suggested next step: [see logic below]
```

**Next step logic:**

- No D1 -> "Run /webtools-intake first to produce D1 Project Brief."
- D1 exists, no D3 -> "Run /webtools-seo-keywords to produce D3 SEO Keyword Map."
- D3 exists at TIER 3, MCP now available -> "D3 was produced with estimates only. Consider re-running /webtools-seo-keywords for TIER 1 accuracy."
- D3 exists without research intelligence in dependencies, R1 or R5 now available -> "D3 was produced without research intelligence. Consider re-running /webtools-seo-keywords for research-informed results."
- D3 complete and current -> "D3 is complete. Downstream: webtools-architecture (D4), webtools-blueprint (D7)."

### No Project

If `project-registry.md` does not exist:

```
[SEO] Webtools SEO

No project found in this directory.

Run /webtools-init to set up a new project first, then return here.

Available commands (after project setup):
  /webtools-seo                  Show this overview
  /webtools-seo-keywords         Run keyword research (produces D3)
```

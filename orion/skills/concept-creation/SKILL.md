---
name: concept-creation
description: "Run Phase 5 concept creation: dispatch concept-creator agents in two waves to produce 5 concept sections, consolidate into D5. Invoke when the user says 'run concept creation', 'create concept', 'start phase 5', 'build concept', or after Domain Gap Analysis is complete with all CRITICAL questions resolved."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 1.0.0
---

# Concept Creation

Dispatch concept-creator agents for 5 concept sections in two dependency-aware waves, then consolidate into D5-Concept using bash. This is the synthesis phase — it turns research and gap analysis into concrete, evidence-based recommendations.

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 4 (Domain Gap Analysis) not complete, stop: "Run domain-gap-analysis first."

Read `D1-Init.json` for client name.
Read `D4-Gap-Analysis.json` and check `meta.total_critical_unresolved`. If greater than zero, stop: "Resolve all CRITICAL questions in D4-Gap-Analysis.md before running concept creation. {n} CRITICAL questions remain unresolved."

### Step 2: Check existing concept outputs

Glob for `concept/C*-*.json` to find existing outputs.
Report: "Found X existing concept sections: [list]. These will be skipped unless you want to re-run them."

### Step 3: Section selection

Present all 5 concept sections grouped by wave:

**Wave 1 (3 parallel, no dependencies):**
- C1-Sitemap: Site structure with pages, keywords, traffic estimates
- C2-Functional: Functional requirements grouped by area
- C5-Visual: Visual direction and positioning

**Wave 2 (2 parallel, upstream dependencies):**
- C3-Tech-Stack: Technology recommendations (depends on C2-Functional)
- C4-Content-Strategy: Tone, messaging, SEO content plan (depends on C1-Sitemap)

Use AskUserQuestion with multiSelect=true. Pre-select all sections that don't have existing outputs.

If the operator deselects a Wave 1 section that a Wave 2 section depends on:
- Deselecting C1 means C4 runs without sitemap context — warn about reduced quality
- Deselecting C2 means C3 runs without functional requirements — warn about reduced quality

### Step 4: Build available files list

Glob for all available project files to pass to concept creators:
- `D1-Init.json`
- `D2-Client-Intelligence.json`
- `research/R*-*.json` (R1 through R9)
- `gap-analysis/G*-*.json` (G01 through G21)

Only include files that actually exist. This list is passed to every concept-creator so it can select relevant files by name.

### Step 5: Dispatch concept creators

Dispatch selected sections via the `dispatch-subagent` skill.

**Max concurrent: 3 agents.**

**Wave 1 — C1 + C2 + C5** (3 parallel, no dependencies)

Each dispatch provides:
- C-code and slug (e.g., "C1", "Sitemap")
- Concept definition content: read `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/{filename}.md` and inline its full content
- Available project files: full list from Step 4
- Model: opus (synthesis and reasoning)
- MCP hints: none (concept creation uses Read + Write only)

**Wave 2 — C3 + C4** (2 parallel, after Wave 1)

Wait for Wave 1 to complete. Then dispatch:

- C3-Tech-Stack: same as above, plus upstream C-file path: `concept/C2-Functional.json`
- C4-Content-Strategy: same as above, plus upstream C-file path: `concept/C1-Sitemap.json`

**Progress reporting after each wave:**
- Which sections completed successfully
- Any failures (and whether to retry or skip)

### Step 6: Consolidate with bash

<critical>
**This step is purely mechanical.** Use ONLY bash commands (jq, cat, echo). Do NOT use the Read tool on any C-file or D-file. Extract counts and client name via jq, not by reading files into context. Reading output files here wastes thousands of tokens for no reason.
</critical>

After all sections complete, produce D5 with bash operations only.

**JSON consolidation:**

```bash
jq -s '{meta:{date:(now|todate),sections:[.[].code],count:length},sections:.}' concept/C*-*.json > D5-Concept.json
```

**Markdown consolidation (all bash):**

```bash
CLIENT=$(jq -r '.project.client' D1-Init.json)
COUNT=$(jq '.meta.count' D5-Concept.json)
DATE=$(date +%Y-%m-%d)
echo "# Website Concept -- $CLIENT
*Generated: $DATE | Sections: $COUNT/5*
*Review and approve this concept before proceeding to Proposal generation.*

---
" > D5-Concept.md
cat concept/C*-*.md >> D5-Concept.md
echo "
---
*Approve this concept to proceed to Proposal & Brief generation.*" >> D5-Concept.md
```

### Step 7: Update project-state.md

Update Phase 5 (Concept Creation) row:
- Status: `complete` (all sections processed) or `partial` (some skipped/failed)
- Output: `D5-Concept.json`
- Updated: today's date

Display summary:

```
Concept Creation complete.

  Completed: {n}/5 sections
  Skipped: [list or "none"]
  Failed: [list or "none"]
  Phase 5 status: complete | partial

Next step: Review D5-Concept.md, then run proposal.
```

## Dependency Graph

```
Wave 1 (parallel):  C1-Sitemap   C2-Functional   C5-Visual
                        |              |
Wave 2 (parallel):  C4-Content    C3-Tech-Stack
                        |              |
Consolidate:           D5-Concept.json + D5-Concept.md
```

## Rules

<critical>
- NEVER dispatch more than 3 concept-creator agents concurrently
- NEVER dispatch Wave 2 sections before their Wave 1 dependencies complete
- NEVER modify project-state.md beyond Phase 5 rows
- NEVER read concept definition files directly -- leave this to the dispatched concept-creator agents
- NEVER start Phase 5 if CRITICAL questions remain unresolved in D4
- ALWAYS use dispatch-subagent skill for every concept-creator dispatch
- ALWAYS provide the full list of available project files to each concept-creator
- ALWAYS run bash consolidation after all sections complete
</critical>

- If a concept-creator fails, note which section was affected, report to operator, continue with remaining sections
- If a Wave 1 section fails and a Wave 2 section depends on it, warn the operator and ask whether to proceed without the dependency or skip the Wave 2 section

## C-code Mapping

| Code | Definition File | Slug | Wave | Depends On |
|---|---|---|---|---|
| C1 | `c1-sitemap.md` | Sitemap | 1 | -- |
| C2 | `c2-functional.md` | Functional | 1 | -- |
| C3 | `c3-tech-stack.md` | Tech-Stack | 2 | C2 |
| C4 | `c4-content-strategy.md` | Content-Strategy | 2 | C1 |
| C5 | `c5-visual.md` | Visual | 1 | -- |

All definition file paths are relative to `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/`.

## Sub-agents

Dispatched via dispatch-subagent:
- **concept-creator** -- Produce one concept section, write per-section file pair (up to 5 instances, dispatched in 2 waves)

## Reference files

Read by concept-creator agents, not by this skill:
- `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/*.md` -- 5 concept section definition files

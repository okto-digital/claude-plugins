---
name: project-research
description: "Run Phase 3 project research: dispatch researcher agents for 9 substages with dependency-aware wave sequencing. Invoke when the user says 'run research', 'start phase 3', 'research phase', 'run substages', or after Client Intelligence phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 3.0.0
---

# Project Research

Dispatch researcher agents for 9 substages with dependency-aware wave sequencing. Each researcher reads `baseline-log.txt` + its substage definition, applies the decision framework, and produces an R-file (.txt).

**Core principle:** One generic researcher agent, many substage definitions. The orchestrator handles topic selection, wave ordering, dispatch, and state updates. baseline-log.txt is the shared context — each wave's agents read it before starting and append to it after finishing, so later waves see earlier findings.

---

## Dependency Graph

| Wave | Substages | Depends on | Concurrency |
|---|---|---|---|
| 1 | R1-SERP | — | 1 |
| 2 | R2-Keywords | R1 | 1 |
| 3 | R3-Competitors | R1, R2 | 1 |
| 4 | R4-Market, R5-Technology, R6-Reputation | R3 | 3 (parallel) |
| 5 | R7-Audience | R1, R2, R3, R4 | 1 |
| 6 | R8-UX, R9-Content | R3, R7 | 2 (parallel) |

Waves 1-3 form the **sequential chain** (progressive competitor list: seeded in R1, expanded in R2, locked in R3). Waves 4-6 run after the chain completes.

---

## Process

### Step 1: Load project context

Read `project-state.md`. If missing, stop: "Run project-init first."
If Phase 2 (Client Intelligence) not complete, stop: "Run client-intelligence first."

Read `project.json`. Verify `baseline-log.txt` exists. Extract client name for reporting.

### Step 2: Check existing R-documents

Glob for `research/R*-*.txt`. For each found, note the code and topic.

Report: "Found X existing R-documents: [list]. These will be skipped unless you want to re-run them."

### Step 3: Topic selection

Present all 9 substages grouped by wave. Use AskUserQuestion with multiSelect=true. Pre-select all topics without existing R-documents.

If the operator deselects a topic that downstream topics depend on, warn about reduced quality but allow it.

### Step 4: Dispatch configuration + wave dispatch

Present the dispatch plan: which waves will run, how many agents per wave.

Check `pipeline_defaults.parallel_execution` in project.json:
- `true` → automatic mode, skip the question
- `false` → stepped mode, skip the question
- `"ask"` → ask operator: "Run all waves automatically, or step through one at a time?"

Dispatch researcher agents via the `dispatch-subagent` skill.

**Each dispatch provides:**
- Decision framework: read and inline `${CLAUDE_PLUGIN_ROOT}/references/decision-framework.md` and `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`
- Substage definition: read and inline the file from the mapping below
- baseline-log.txt path: `{working_directory}/baseline-log.txt` — agent reads before starting, appends after finishing
- Output path: `{working_directory}/research/R{n}-{Slug}.txt`
- MCP tool hints: DataForSEO + all web-crawler hints from dispatch-subagent
- Model: opus

**Wave execution:**

For each wave: dispatch selected substages, wait for completion, verify output files exist (Glob), report results.

**After each wave:**
1. Verify output .txt files were created for each dispatched substage.
2. Verify baseline-log.txt was appended to (file grew).
3. Report which substages completed, any failures.
4. If stepped mode: pause for operator review.

If a researcher fails: note which substage was affected, report to operator, continue with remaining waves.

### Step 5: Consolidate

<critical>
**This step is purely mechanical.** Use ONLY bash commands (cat, echo). Do NOT read any R-file into context. The whole point is to merge files without consuming context tokens.
</critical>

After all waves complete, produce D3-Research.txt — concatenation of all R-files with headers.

```bash
mkdir -p tmp
DATE=$(date +%Y-%m-%d)
echo "Research Overview — $DATE" > D3-Research.txt
echo "" >> D3-Research.txt
for f in research/R*-*.txt; do
  BASENAME=$(basename "$f" .txt)
  echo "--- $BASENAME ---" >> D3-Research.txt
  cat "$f" >> D3-Research.txt
  echo "" >> D3-Research.txt
done
```

### Step 6: Debug companion (when enabled)

If `research_config.debug` is `true` in project.json: write `tmp/debug/D3-Research-debug.txt` — list of completed substages, any failures or skips, no prose.

### Step 7: Update project-state.md

For each completed substage, update the Research Substages row: Status → `complete`, Output → `research/{code}-{slug}.txt`, Updated → today's date.

Update Phase 3 (Research) row:
- Status: All 9 complete → `complete`, some skipped or failed → `partial`
- Output: `D3-Research.txt`
- Updated: today's date

Display summary and suggest next step: Run domain-gap-analysis.

---

## Substage File Mapping

| Code | File | Wave |
|---|---|---|
| R1-SERP | `agents/references/research-substages/3-1-serp.md` | 1 |
| R2-Keywords | `agents/references/research-substages/3-2-keywords.md` | 2 |
| R3-Competitors | `agents/references/research-substages/3-3-competitors.md` | 3 |
| R4-Market | `agents/references/research-substages/3-4-market.md` | 4 |
| R5-Technology | `agents/references/research-substages/3-5-technology.md` | 4 |
| R6-Reputation | `agents/references/research-substages/3-6-reputation.md` | 4 |
| R7-Audience | `agents/references/research-substages/3-7-audience.md` | 5 |
| R8-UX | `agents/references/research-substages/3-8-ux.md` | 6 |
| R9-Content | `agents/references/research-substages/3-9-content.md` | 6 |

All paths relative to `${CLAUDE_PLUGIN_ROOT}/`.

---

## Rules

<critical>
- **NEVER** skip Phase 2 prerequisite check
- **NEVER** dispatch more than 3 researcher agents concurrently
- **NEVER** modify project-state.md beyond Phase 3 and its substage rows
- **NEVER** interpret or act on substage definition content — read only to inline into the dispatch prompt
- **ALWAYS** use dispatch-subagent skill for every researcher dispatch
- **ALWAYS** inline the decision framework in every dispatch
</critical>

- If fewer than 5 substages complete, warn that Phase 4 coverage will be limited
- Wave 4-6 topics can run without soft dependencies — they produce slightly less cross-referenced output

---

## Sub-agents

- `researcher` (via dispatch-subagent) — execute one substage, produce R-file .txt (up to 9 instances, dispatched in waves)

## Reference Files

- `${CLAUDE_PLUGIN_ROOT}/references/decision-framework.md` — thinking method (inlined in every dispatch)
- `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` — output formatting (inlined in every dispatch)
- `${CLAUDE_PLUGIN_ROOT}/agents/references/research-substages/*.md` — 9 substage definitions (read by researcher agents)

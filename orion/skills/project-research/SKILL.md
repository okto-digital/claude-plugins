---
name: project-research
description: "Run Phase 3 project research: dispatch researcher agents for 9 substages with dependency-aware wave sequencing. Invoke when the user says 'run research', 'start phase 3', 'research phase', 'run substages', or after Client Intelligence phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 2.0.0
---

# Project Research

Dispatch researcher agents for 9 substages with dependency-aware wave sequencing. Each researcher loads a substage definition, executes research using MCP tools + sub-agents, and produces an R-file pair (JSON + markdown).

**Core principle:** One generic researcher agent, many substage definitions. The orchestrator handles topic selection, dependency ordering, wave dispatch, and state updates.

---

## Dependency Graph

Substage numbers indicate research topic, not execution order. The dependency graph determines dispatch sequence.

| Wave | Substages | Depends on | Concurrency |
|---|---|---|---|
| 1 | R1-SERP | — | 1 |
| 2 | R2-Keywords | R1 | 1 |
| 3 | R3-Competitors | R1, R2 | 1 |
| 4 | R4-Market, R5-Technology, R6-Reputation | R3 | 3 (parallel) |
| 5 | R7-Audience | R1, R2, R3, R4 | 1 |
| 6 | R8-UX, R9-Content | R3, R7 | 2 (parallel) |

Waves 1–3 form the **sequential chain** (progressive competitor list: seeded in R1, expanded in R2, locked in R3). Waves 4–6 run after the chain completes.

---

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 2 (Client Intelligence) not complete, stop: "Run client-intelligence first."

Read `D1-Init.json` and `D2-Client-Intelligence.json`. Verify both exist. Extract client name for reporting.

### Step 2: Check existing R-documents

Glob for `research/R*-*.json`. For each found, note the document code and topic.

Report: "Found X existing R-documents: [list]. These will be skipped unless you want to re-run them."

### Step 3: Topic selection

Present all 9 substages grouped by wave:

**Sequential chain (Waves 1–3):**
- 3.1 R1-SERP: SERP & Search Landscape
- 3.2 R2-Keywords: Keyword Opportunity
- 3.3 R3-Competitors: Competitor Landscape

**Parallel after R3 (Wave 4):**
- 3.4 R4-Market: Industry & Market Context
- 3.5 R5-Technology: Technology & Performance
- 3.6 R6-Reputation: Reputation & Social Proof

**After R4 (Wave 5):**
- 3.7 R7-Audience: Audience & Personas

**After R7 (Wave 6):**
- 3.8 R8-UX: UX/UI Patterns & Benchmarks

**After R8 (Wave 7):**
- 3.9 R9-Content: Content Landscape & Strategy

Use AskUserQuestion with multiSelect=true. Pre-select all topics without existing R-documents.

If the operator deselects a topic that downstream topics depend on, warn about reduced quality but allow it. Example: skipping R4-Market means R7-Audience runs without industry behavior context.

### Step 4: Pre-merge context files

Build a context file per substage containing D1, D2, and dependency R-files. Context files are built per-wave because later waves need R-files produced by earlier waves. Only build context files for selected substages. `merge-json.sh` skips missing files (when a dependency was skipped).

```bash
mkdir -p tmp research
```

Context merges per wave (run each group immediately before its wave dispatch):

**Before Wave 1 — R1** (no R-file dependencies):
```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json -o tmp/context-R1.json
```

**Before Wave 2 — R2** (depends on R1):
```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R1-SERP.json -o tmp/context-R2.json
```

**Before Wave 3 — R3** (depends on R1, R2):
```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R1-SERP.json research/R2-Keywords.json -o tmp/context-R3.json
```

**Before Wave 4 — R4, R5, R6** (all depend on R3):
```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R3-Competitors.json -o tmp/context-R4.json
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R3-Competitors.json -o tmp/context-R5.json
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R3-Competitors.json -o tmp/context-R6.json
```

**Before Wave 5 — R7** (depends on R1, R2, R3, R4):
```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R1-SERP.json research/R2-Keywords.json research/R3-Competitors.json research/R4-Market.json -o tmp/context-R7.json
```

**Before Wave 6 — R8** (R8: R3+R7):
```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R3-Competitors.json research/R7-Audience.json -o tmp/context-R8.json
```

**Before Wave 7 — R9** (R9: R2+R3+R4+R6+R7+R8):
```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R2-Keywords.json research/R3-Competitors.json research/R4-Market.json research/R6-Reputation.json research/R7-Audience.json research/R8-UX.json -o tmp/context-R9.json
```

### Step 5: Dispatch configuration + wave dispatch

Present the dispatch plan:
- Which waves will run, how many agents per wave
- Model: opus for all (analysis + synthesis)
- Max concurrent: 3 agents per wave

Check `pipeline_defaults.parallel_execution` in D1-Init.json:
- `true` → automatic mode, skip the question
- `false` → stepped mode, skip the question
- `"ask"` (default) → ask operator

When asking: "Run all waves automatically, or step through one at a time?" Use AskUserQuestion.
- **Automatic:** Run all waves without pausing between them
- **Stepped:** Pause after each wave for operator review

Dispatch researcher agents via the `dispatch-subagent` skill. Max 3 concurrent per wave.

**Each dispatch provides:**
- Substage definition content: read the file from the mapping below and inline its full content in the dispatch prompt
- Context file path: `{working_directory}/tmp/context-R{n}.json`
- MCP tool hints: DataForSEO + all web-crawler hints from dispatch-subagent
- Model: opus

**Wave execution:**

For each wave: build context file(s) from Step 4, then dispatch.

**Wave 1 — R1-SERP** (single)
Build context-R1.json. Dispatch for substage 3.1.

**Wave 2 — R2-Keywords** (single)
Build context-R2.json. Dispatch for substage 3.2.

**Wave 3 — R3-Competitors** (single)
Build context-R3.json. Dispatch for substage 3.3.

**Wave 4 — R4 + R5 + R6** (3 parallel)
Build context-R4/R5/R6.json. Dispatch for substages 3.4, 3.5, 3.6.

**Wave 5 — R7-Audience** (single)
Build context-R7.json. Dispatch for substage 3.7.

**Wave 6 — R8-UX** (single)
Build context-R8.json. Dispatch for substage 3.8.

**Wave 7 — R9-Content** (single)
Build context-R9.json. Dispatch for substage 3.9. R9 now has R8 UX findings for content-structure integration.

**After each wave:**

1. **Validate JSON outputs:**
```bash
scripts/validate-json.sh research/R*-*.json
```
If any file fails: attempt `jq -c '.' broken.json > broken.json.tmp && mv broken.json.tmp broken.json`. If jq also fails, re-dispatch the failed substage.

2. Report which substages completed successfully, any failures (and whether to retry or skip).
3. If stepped mode: pause for operator review.

### Step 6: Consolidate with bash

<critical>
**This step is purely mechanical.** Use ONLY bash commands (jq, cat, echo). Do NOT read any R-file into context — no Read tool, no opening JSON/MD files. The whole point is to merge files without consuming context tokens. If you read research files here, you are wasting thousands of tokens for no reason.
</critical>

After all waves complete, produce D3 as a **TLDR digest** — only the `tldr` arrays from each R-file. Full R-files stay in `research/` for detailed reference. Downstream agents read D3 or individual R-file `tldr` fields, not full R-files.

**JSON consolidation (tldr only):**

```bash
jq -s '{meta:{date:(now|todate),completed:[.[].code],count:length},substages:[.[]|{code,slug,tldr,source:("research/"+.code+"-"+.slug+".json")}]}' research/R*-*.json > D3-Research.json
```

**Markdown consolidation (all bash):**

```bash
CLIENT=$(jq -r '.project.client' D1-Init.json)
COUNT=$(jq '.meta.count' D3-Research.json)
DATE=$(date +%Y-%m-%d)
echo "# Research Overview — $CLIENT
*Generated: $DATE | Substages completed: $COUNT/9*

---
" > D3-Research.md
for f in research/R*-*.json; do
  CODE=$(jq -r '.code' "$f")
  SLUG=$(jq -r '.slug' "$f")
  echo "## $CODE — $SLUG" >> D3-Research.md
  echo "*Full report: research/${CODE}-${SLUG}.md*" >> D3-Research.md
  echo "" >> D3-Research.md
  jq -r '.tldr[]' "$f" | sed 's/^/- /' >> D3-Research.md
  echo "" >> D3-Research.md
done
```

### Step 7: Cleanup

```bash
rm -f tmp/context-R*.json
```

### Step 8: Update project-state.md

After all selected waves complete:

1. For each completed substage, update the Research Substages row: Status → `complete`, Output → `research/{code}-{slug}.json`, Updated → today's date.

2. Update Phase 3 (Research) row:
   - Status: All 9 complete → `complete`, some skipped or failed → `partial`
   - Output: `D3-Research.json`
   - Updated: today's date

3. Display summary:

```
Research phase complete.

  Completed: {n}/9 substages
  Skipped: [list or "none"]
  Failed: [list or "none"]
  Phase 3 status: complete | partial

Next step: Run domain-gap-analysis.
```

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

All paths are relative to `${CLAUDE_PLUGIN_ROOT}/`.

---

## Rules

<critical>
- **NEVER** skip Phase 2 prerequisite check
- **NEVER** dispatch more than 3 researcher agents concurrently
- **NEVER** modify project-state.md beyond Phase 3 and its substage rows
- **NEVER** interpret or act on substage definition content -- read only to inline into the dispatch prompt; the researcher agent executes the methodology
- **ALWAYS** use dispatch-subagent skill for every researcher dispatch
- **ALWAYS** pre-merge context files before dispatching researcher agents
- **ALWAYS** provide resolved context file paths (not template variables) to researcher agents
</critical>

- If a researcher fails, note which substage was affected, report to operator, continue with remaining waves
- If fewer than 5 substages complete, warn that Phase 4 coverage will be limited
- Wave 5–6 topics can run without soft dependencies -- they produce slightly less cross-referenced output

---

## Sub-agents

- `researcher` (via dispatch-subagent) -- Execute one substage, produce R-file pair (up to 9 instances, dispatched in 6 waves)

## Reference Files

- `${CLAUDE_PLUGIN_ROOT}/agents/references/research-substages/*.md` -- 9 substage methodology files (read by researcher agents, not by this skill)

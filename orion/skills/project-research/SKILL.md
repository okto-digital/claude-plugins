---
name: project-research
description: "Run Phase 3 project research: dispatch researcher agents for 10 substages with dependency-aware wave sequencing. Invoke when the user says 'run research', 'start phase 3', 'research phase', 'run substages', or after Client Intelligence phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 4.0.0
---

# Project Research

Dispatch researcher agents for 10 substages with dependency-aware wave sequencing. Each researcher reads `baseline-log.txt` + its substage definition, applies the decision framework, and produces an R-file (.txt).

**Core principle:** One generic researcher agent, many substage definitions. The orchestrator handles topic selection, wave ordering, dispatch, and state updates. baseline-log.txt is the shared context — each wave's agents read it before starting and append to it after finishing, so later waves see earlier findings.

---

## Dependency Graph

| Wave | Substages | Notes | Concurrency |
|---|---|---|---|
| 1 | R1-Inventory, R2-SERP | Independent. R1 skipped for new builds | 2 (parallel) |
| 2 | R3-Keywords | Needs R2 | 1 |
| 3 | R4-Competitors | Needs R2, R3. Locks competitor roster | 1 |
| 4 | R5-Market | Needs R4 | 1 |
| 5 | R6-Audience, R8-Technology | Both need R5. Parallel | 2 (parallel) |
| 6 | R7-Reputation | Needs R6 | 1 |
| 7 | R9-UX | Needs R7, R8 | 1 |
| 8 | R10-Content | Needs R9. Final substage | 1 |

Waves 1-3 form the **sequential chain** (progressive competitor list: seeded in R2, expanded in R3, locked in R4). Waves 4-8 run after the chain completes. The crawl cache convention (`tmp/competitors/`) means later waves reuse pages crawled by earlier waves.

---

## Process

### Step 1: Load project context

Read `project-state.md`. If missing, stop: "Run project-init first."
If Phase 2 (Client Intelligence) not complete, stop: "Run client-intelligence first."

Read `project.json`. Verify `baseline-log.txt` exists. Extract client name for reporting.

If `project.json → site_type = "new"`: note that R1-Inventory will be skipped.

### Step 2: Check existing R-documents

Glob for `research/R*-*.txt`. For each found, note the code and topic.

Report: "Found X existing R-documents: [list]. These will be skipped unless you want to re-run them."

### Step 3: Topic selection

Present all 10 substages grouped by wave. Use AskUserQuestion with multiSelect=true. Pre-select all topics without existing R-documents.

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
- Crawl cache: instruct agent to check `tmp/competitors/{domain-slug}/` before crawling and save new crawls there
- Model: opus

**Wave execution:**

For each wave: dispatch selected substages, wait for completion, verify output files exist (Glob), report results.

**After each wave:**
1. Verify output .txt files were created for each dispatched substage.
2. Verify baseline-log.txt was appended to (file grew).
3. Report which substages completed, any failures.
4. If stepped mode: pause for operator review.

If a researcher fails: note which substage was affected, report to operator, continue with remaining waves.

### Step 5: Research Synthesis

After all waves complete, dispatch a generic agent via Task tool to compress all R-files into a single decision-ready document for Concept Creation. No dedicated agent definition needed — the dispatch prompt below IS the full instruction.

**This is NOT new research — it is a compression gate.** The agent reads and distils. It does not add findings, interpretations, or recommendations beyond what the R-files contain.

**Dispatch:** `subagent_type="general-purpose"`, model `opus`. Provide:
- All R-file paths: Glob `research/R*-*.txt`
- baseline-log.txt path
- Formatting rules: inline `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`
- Output path: `{working_directory}/D3-Research-Synthesis.txt`

**Prompt instructs the agent to structure D3-Research-Synthesis.txt around six decision areas:**

1. **Site structure decisions** — R10 cluster-to-content map + R1 service/product page mapping + R3 keyword opportunities → which pages must exist, which can be merged, which are missing
2. **Design direction** — R9 visual conventions and differentiation opportunities + R6 persona device preferences and trust thresholds + R9 UX patterns to adopt or avoid
3. **Content direction** — R10 voice recommendation + R7 messaging intelligence and customer language + R10 content quality bar from competitor analysis
4. **Technical requirements** — R5 compliance checklist verified by R8 findings + R8 performance benchmarks + R8 accessibility requirements
5. **Competitive positioning brief** — R4 overlap matrix + R3 keyword gaps + R7 trust gaps → the strongest argument for why the client needs this website
6. **Constraints and non-negotiables** — R5 regulatory requirements + R9 industry conventions that can't be broken + R8 technical limitations

Per decision area: state the finding, cite the R-file source, flag conflicts between R-files where they exist.

**D3-Research-Synthesis.txt becomes the primary input for Concept Creation.** Individual R-files remain available for drill-down when concept agents need specifics.

### Step 6: Debug companion (when enabled)

If `research_config.debug` is `true` in project.json: write `tmp/debug/D3-Research-debug.txt` — list of completed substages, any failures or skips, no prose.

### Step 7: Update project-state.md

For each completed substage, update the Research Substages row: Status → `complete`, Output → `research/{code}-{slug}.txt`, Updated → today's date.

Update Phase 3 (Research) row:
- Status: All 10 complete → `complete`, some skipped or failed → `partial`
- Output: `D3-Research-Synthesis.txt`
- Updated: today's date

Display summary and suggest next step: Run domain-gap-analysis.

---

## Substage File Mapping

| Code | Slug | File | Wave |
|---|---|---|---|
| R1 | Inventory | `agents/references/research-substages/3-1-inventory.md` | 1 |
| R2 | SERP | `agents/references/research-substages/3-2-serp.md` | 1 |
| R3 | Keywords | `agents/references/research-substages/3-3-keywords.md` | 2 |
| R4 | Competitors | `agents/references/research-substages/3-4-competitors.md` | 3 |
| R5 | Market | `agents/references/research-substages/3-5-market.md` | 4 |
| R6 | Audience | `agents/references/research-substages/3-6-audience.md` | 5 |
| R7 | Reputation | `agents/references/research-substages/3-7-reputation.md` | 6 |
| R8 | Technology | `agents/references/research-substages/3-8-technology.md` | 5 |
| R9 | UX | `agents/references/research-substages/3-9-ux.md` | 7 |
| R10 | Content | `agents/references/research-substages/3-10-content.md` | 8 |

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
- **ALWAYS** include crawl cache instructions in every dispatch
</critical>

- If fewer than 5 substages complete, warn that Phase 4 coverage will be limited
- Wave 4-8 topics can run without soft dependencies — they produce slightly less cross-referenced output

---

## Sub-agents

- `researcher` (via dispatch-subagent) — execute one substage, produce R-file .txt (up to 10 instances, dispatched in waves)
- synthesis is a generic Task dispatch (no agent definition) — prompt-only, runs once after all waves

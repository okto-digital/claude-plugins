---
name: concept-creation
description: "Run Phase 5 concept creation: dispatch 3 concept-creator agents in parallel to produce tiered website concepts (Efficient, Competitive, Dominant), then build D5-Concept-Comparison.md. Invoke when the user says 'run concept creation', 'create concepts', 'start phase 5', 'build concepts', or after Domain Gap Analysis is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 5.0.0
---

# Concept Creation

Dispatch 3 concept-creator agents in parallel — one per tier (Efficient, Competitive, Dominant). Each agent independently builds a complete website concept across 8 dimensions. After all complete, build D5-Concept-Comparison.md showing differences across tiers.

**Agents:** 3 concept-creator dispatches (all parallel) + 1 comparison builder = 4 total.

**Root output:** D5-Concept-Comparison.md
**Working files:** concept/Concept-Tier-1.md, concept/Concept-Tier-2.md, concept/Concept-Tier-3.md

---

## Tier Definitions

| Tier | Name | Business Proposition |
|---|---|---|
| 1 | Efficient | Focused intervention. Fixes critical issues, captures top opportunities. Minimal investment, professional result. |
| 2 | Competitive | Research-driven restructure. Every page exists for a research-backed reason. Outperform identified competitors. **Recommended.** |
| 3 | Dominant | Full vision. Every opportunity including whitespace. Market leadership positioning. Requires ongoing content commitment. |

**Floor rule:** Every tier must produce a site demonstrably better than the current website on every dimension the research identified as problematic.

---

## Process

### Step 1: Load project context

Read `project-state.md`. If missing → "Run project-init first." If Phase 4 not resolved → "Run domain-gap-analysis first and resolve answers."

Read `project.json` for project configuration. Verify `baseline-log.txt` exists.

Verify these D-files exist:
- `D2-Client-Intelligence.txt`
- `D4-Scope-Implications.txt`
- `D4-Cross-Domain.txt`
- `gap-analysis/confirmed.txt`

If any are missing, stop with: "Phase 4 output incomplete. Missing: [list]."

### Step 2: Check existing outputs

Glob for `concept/Concept-Tier-*.md`. If any exist, ask: "Found existing concept files: [list]. Overwrite?" If declined, skip to Step 4 (comparison).

### Step 3: Dispatch concept creators

```bash
mkdir -p concept
```

Dispatch all 3 concept-creator agents in parallel via `dispatch-subagent`. All 3 concurrent — no sequential dependencies.

Each dispatch provides:
- **Tier number** (1, 2, or 3) and **tier name** (Efficient, Competitive, Dominant)
- **Agent definition**: read `${CLAUDE_PLUGIN_ROOT}/agents/concept-creator.md` and inline its full content
- **Concept methodology**: read `${CLAUDE_PLUGIN_ROOT}/references/concept-methodology.md` and inline its full content
- **Solution framework**: read `${CLAUDE_PLUGIN_ROOT}/references/solution-framework.md` and inline its full content
- **Formatting rules**: read `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` and inline its full content
- **baseline-log.txt path**: `{working_directory}/baseline-log.txt`
- **project.json path**: `{working_directory}/project.json`
- **D-file paths**:
  - `{working_directory}/D2-Client-Intelligence.txt`
  - `{working_directory}/D4-Scope-Implications.txt`
  - `{working_directory}/D4-Cross-Domain.txt`
  - `{working_directory}/gap-analysis/confirmed.txt`
- **Output path**: `{working_directory}/concept/Concept-Tier-{N}.md`
- **Model**: opus | MCP hints: none

**After dispatch:** Verify all 3 output files exist and have content:
```bash
for f in concept/Concept-Tier-*.md; do
  if [ ! -s "$f" ]; then
    echo "EMPTY OR MISSING: $f"
  fi
done
```

Report: "3 concepts generated: Tier 1 (Efficient), Tier 2 (Competitive), Tier 3 (Dominant)."

If any failed, report which tier failed and ask whether to re-dispatch.

### Step 4: Build D5-Concept-Comparison.md

Dispatch a comparison agent (model: sonnet) with:
- Paths to all 3 concept files
- Formatting rules: read `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` and inline its full content
- Instructions: read all 3 concepts, produce D5-Concept-Comparison.md at `{working_directory}/D5-Concept-Comparison.md`

<critical>
The comparison document lists ONLY differences between tiers. Do not repeat shared elements. Concise format — one line per difference where possible.
</critical>

The agent writes `D5-Concept-Comparison.md` with this structure:

```
================================================================================
CONCEPT COMPARISON — Differences by Dimension
================================================================================

Project: {client name}
Date: {today}

================================================================================
1. STRUCTURE
================================================================================
Tier 1: {n} pages — {key characteristic}
Tier 2: {n} pages — {key characteristic}
Tier 3: {n} pages — {key characteristic}

Pages unique to Tier 2: {list}
Pages unique to Tier 3: {list}

================================================================================
2. TEMPLATES
================================================================================
Tier 1: {n} templates | Tier 2: {n} templates | Tier 3: {n} templates
{Key differences only}

... (all 8 dimensions) ...

================================================================================
SUMMARY
================================================================================

| Dimension | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Pages | {n} | {n} | {n} |
| Templates | {n} | {n} | {n} |
| Sections/template | {range} | {range} | {range} |
| Functionality items | {n} | {n} | {n} |
| Included tasks | {n} | {n} | {n} |
| Optional tasks | {n} | {n} | {n} |
```

### Step 5: Debug companion (when enabled)

If `debug` is `true` in project.json: write `tmp/debug/D5-Concept-debug.txt` — line counts per tier, dimension coverage check (all 8 present in each?), baseline-log entries added per tier, any failures.

### Step 6: Update project-state.md

Update Phase 5 row:

```
Concept Creation — complete.
  Tier 1 (Efficient): concept/Concept-Tier-1.md
  Tier 2 (Competitive): concept/Concept-Tier-2.md
  Tier 3 (Dominant): concept/Concept-Tier-3.md
  Comparison: D5-Concept-Comparison.md
Next: Review concepts with client, select tier, then run proposal.
```

Display summary:

```
Concept Creation complete.

  Tier 1 (Efficient): concept/Concept-Tier-1.md — {n} pages, {n} templates
  Tier 2 (Competitive): concept/Concept-Tier-2.md — {n} pages, {n} templates
  Tier 3 (Dominant): concept/Concept-Tier-3.md — {n} pages, {n} templates
  Comparison: D5-Concept-Comparison.md

Next step: Review concepts, select a tier, then run proposal.
```

---

## Rules

<critical>
- NEVER start Phase 5 if D4 gap analysis is not resolved
- NEVER modify project-state.md beyond Phase 5 rows
- ALWAYS use dispatch-subagent skill for every dispatch
- ALWAYS inline concept-methodology.md, solution-framework.md, and formatting-rules.md in every concept-creator dispatch
- ALWAYS verify all 3 output files exist after dispatch
</critical>

- If a concept-creator fails, report which tier, ask whether to re-dispatch
- The 3 agents run independently — no shared context, no sequential dependencies
- Each agent may produce genuinely different structural decisions — this is intentional and desired
- The comparison document is a convenience, not a quality gate — differences between tiers are expected

## Sub-agents

Dispatched via dispatch-subagent:
- **concept-creator** — Build one complete tiered concept across 8 dimensions (3 instances, all parallel)
- **comparison builder** — Generic agent that reads 3 concepts and extracts differences into D5 (1 instance, model: sonnet)

## Reference files

Inlined in every concept-creator dispatch (read by this skill, not by agents):
- `${CLAUDE_PLUGIN_ROOT}/references/concept-methodology.md` — Tier model, 8 dimensions, structure process, template rules, classification tests
- `${CLAUDE_PLUGIN_ROOT}/references/solution-framework.md` — ICIP thinking sequence
- `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` — Scannable TXT output conventions

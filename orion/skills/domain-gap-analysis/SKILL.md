---
name: domain-gap-analysis
description: "Run Phase 4 domain gap analysis: dispatch up to 6 grouped domain-analyst agents, consolidate questions, pause for answers, then resolve. Invoke when the user says 'run gap analysis', 'domain analysis', 'start phase 4', 'run domains', or after Research phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 4.0.0
---

# Domain Gap Analysis

Dispatch domain-analyst agents for 6 domain groups. Analysts score checkpoints against baseline-log evidence, writing directly to 3 output streams: confirmed intelligence, client questions, agency questions. After answers, one question-resolver dispatch finalizes everything.

**Agents:** 6 analyst dispatches (2 batches of 3) + 1 question-resolver = 7 total.
**Output:** D4-Confirmed.txt, D4-Questions-Client.txt, D4-Questions-Agency.txt.

---

## Domain Groups

| Group | G-codes | Domains |
|---|---|---|
| **A — Business & Strategy** | G05, G06, G15, G19 | business-context, competitive-landscape, project-scope, target-audience |
| **B — Technical Foundation** | G13, G16, G20 | performance, security-and-compliance, technical-platform |
| **C — UX & Design** | G01, G08, G10 | accessibility, design-and-brand, forms-and-lead-capture |
| **D — Content & SEO** | G07, G17, G18 | content-strategy, seo-and-discoverability, site-structure |
| **E — Operations** | G02, G14, G11* | analytics-and-measurement, post-launch, migration-and-redesign* |
| **F — Conditional** | G03*, G04*, G09*, G12*, G21* | blog-and-editorial, booking-and-scheduling, ecommerce, multilingual, user-accounts |

`*` = conditional domain (agent checks applicability, returns N/A if not applicable)

**Dispatch:** Batch 1 (A, B, C concurrent) then Batch 2 (D, E, F concurrent). Max 3 concurrent. If 1-3 groups selected, single batch.

---

## Process

### Step 1: Load project context

Read `project-state.md`. If missing → "Run project-init first." If Phase 3 not complete → "Run project-research first."

Read `project.json` for project parameters. Verify `baseline-log.txt` exists.

### Step 2: Check existing outputs

Glob for `D4-Confirmed.txt`, `D4-Questions-Client.txt`, `D4-Questions-Agency.txt`. If any exist, warn: "Phase 4 output already exists. Overwrite?" If declined, skip to Step 5 (answer resolution).

### Step 3: Domain selection

Check `pipeline_defaults.gap_domains` in project.json:
- `"all"` → select all 6 groups, skip the question
- `[list of domain codes]` → select only groups containing those codes, skip the question
- `"ask"` (default) → present groups via AskUserQuestion with multiSelect=true

Conditional domains (G03, G04, G09, G12, G21) are automatically marked N/A by the analyst if not applicable — the operator does not need to deselect them.

### Step 4: Dispatch domain analysts

```bash
mkdir -p gap-analysis/questions
```

Dispatch selected groups via `dispatch-subagent`. Each dispatch provides:
- Group name and domain list (G-codes, domain-ids, conditional flags)
- Domain definitions: inline `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/{domain-id}.md` per domain, separated by `--- DOMAIN: {domain-id} ---`
- project.json path: `{working_directory}/project.json`
- baseline-log.txt path: `{working_directory}/baseline-log.txt`
- Output file paths:
  - `{working_directory}/gap-analysis/questions/{Group}-confirmed.txt`
  - `{working_directory}/gap-analysis/questions/{Group}-client.txt`
  - `{working_directory}/gap-analysis/questions/{Group}-agency.txt`
- Model: sonnet | MCP hints: none

**After each batch:** verify output files exist for each dispatched group.

### Step 5: Consolidate

<critical>
**Purely mechanical.** Use ONLY bash commands. Do NOT read any output file into context.
</critical>

```bash
# Consolidate per-group files into D4 outputs
cat gap-analysis/questions/*-confirmed.txt > D4-Confirmed.txt
cat gap-analysis/questions/*-client.txt > D4-Questions-Client.txt
cat gap-analysis/questions/*-agency.txt > D4-Questions-Agency.txt

# Stats
CONFIRMED=$(wc -l < D4-Confirmed.txt | tr -d ' ')
CLIENT=$(grep -c '^\[G' D4-Questions-Client.txt 2>/dev/null || echo 0)
AGENCY=$(grep -c '^\[G' D4-Questions-Agency.txt 2>/dev/null || echo 0)
```

### Step 6: Debug companion (when enabled)

If `research_config.debug` is `true` in project.json: write `tmp/debug/D4-Gap-Analysis-debug.txt` — confirmed/client/agency counts per group, inactive domains, no prose.

### Step 7: Update project-state.md

Update Phase 4: status `awaiting_answers`, date today.

```
Domain Gap Analysis — awaiting answers.
  Confirmed: {n} | Client questions: {n} | Agency questions: {n}
Output: D4-Confirmed.txt, D4-Questions-Client.txt, D4-Questions-Agency.txt
Next: Fill in answers in D4-Questions-Client.txt and D4-Questions-Agency.txt, then re-run to resolve.
```

---

## Answer Resolution (re-run after answers are filled)

When the skill is invoked and D4-Questions-Client.txt already exists with Phase 4 status `awaiting_answers`:

### Step 8: Check for answers

The operator fills in answers directly in D4-Questions-Client.txt and D4-Questions-Agency.txt by writing the selected option or free text after each question block.

Check if answers have been added:

```bash
# Look for answer markers (lines starting with "Answer:" or ">")
CLIENT_ANSWERED=$(grep -c '^Answer:\|^>' D4-Questions-Client.txt 2>/dev/null || echo 0)
AGENCY_ANSWERED=$(grep -c '^Answer:\|^>' D4-Questions-Agency.txt 2>/dev/null || echo 0)
TOTAL_ANSWERED=$((CLIENT_ANSWERED + AGENCY_ANSWERED))
```

If `TOTAL_ANSWERED == 0`: inform operator no answers found, explain the answer format, stop.

### Step 9: Dispatch question-resolver

Dispatch `question-resolver` via `dispatch-subagent`:
- Model: opus
- Mode: Lightweight (no MCP)
- Prompt payload:
  - project.json path: `{working_directory}/project.json`
  - baseline-log.txt path: `{working_directory}/baseline-log.txt`
  - D4-Confirmed.txt path: `{working_directory}/D4-Confirmed.txt`
  - D4-Questions-Client.txt path: `{working_directory}/D4-Questions-Client.txt`
  - D4-Questions-Agency.txt path: `{working_directory}/D4-Questions-Agency.txt`

The resolver appends resolved answers to D4-Confirmed.txt and key `[D4]` findings to baseline-log.txt.

### Step 10: Update project-state.md

Update Phase 4: status `complete`, date today.

```
Domain Gap Analysis — complete.
  Confirmed: {n} | Resolved: {n} | Unresolved: {n}
Output: D4-Confirmed.txt, D4-Questions-Client.txt, D4-Questions-Agency.txt
Next: Run concept-creation.
```

---

## Rules

<critical>
- NEVER dispatch more than 3 group agents concurrently
- NEVER modify project-state.md beyond Phase 4 rows
- NEVER Read output files into context during consolidation — bash only
- ALWAYS use dispatch-subagent skill for every dispatch
</critical>

- If a group agent fails, report affected domains, continue with remaining groups
- If fewer than 3 groups complete, warn that Phase 5 coverage will be limited
- The operator can re-run answer resolution multiple times as more answers come in

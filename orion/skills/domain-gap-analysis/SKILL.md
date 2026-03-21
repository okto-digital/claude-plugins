---
name: domain-gap-analysis
description: "Run Phase 4 domain gap analysis: dispatch up to 6 grouped domain-analyst agents, consolidate, deduplicate questions, pause for answers, resolve, then synthesise cross-domain patterns and extract scope implications. Invoke when the user says 'run gap analysis', 'domain analysis', 'start phase 4', 'run domains', or after Research phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 6.0.0
---

# Domain Gap Analysis

Dispatch domain-analyst agents for 6 domain groups. Analysts score checkpoints against baseline-log evidence using the resolution hierarchy from gap-analysis-framework.md. After consolidation and deduplication, the operator fills answers. After resolution, the skill synthesises cross-domain patterns and extracts scope implications.

**Agents:** 6 analyst dispatches (2 batches of 3) + 1 dedup + 1 resolver = 8 total.

**Root output:** D4-Scope-Implications.txt, D4-Cross-Domain.txt.
**Working files:** `gap-analysis/` directory (confirmed, questions, per-group files).

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

## Research Evidence Map

Each domain definition contains a `Research provides` section listing which R-tags contain relevant evidence and an expected confirmation rate. The dispatch prompt includes this per domain so analysts know where to focus.

| Confirmation rate | Meaning | Analyst posture |
|---|---|---|
| HIGH (70%+) | Most checkpoints resolvable from research | Flag fewer gaps; if many gaps, re-check baseline-log |
| MEDIUM (40-70%) | Mixed evidence coverage | Balanced — some confirmed, some gaps expected |
| LOW (<40%) | Mostly client-specific knowledge needed | Many questions expected; don't force confirmations |

---

## Process

### Step 1: Load project context

Read `project-state.md`. If missing → "Run project-init first." If Phase 3 not complete → "Run project-research first."

Read `project.json` for project parameters. Verify `baseline-log.txt` exists.

### Step 2: Check existing outputs

Glob for `gap-analysis/confirmed.txt`. If exists, warn: "Phase 4 output already exists. Overwrite?" If declined, skip to Step 9 (answer resolution).

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

Dispatch selected groups via `dispatch-subagent` using `${CLAUDE_PLUGIN_ROOT}/agents/domain-analyst.md`. Each dispatch provides:
- Agent definition: read `${CLAUDE_PLUGIN_ROOT}/agents/domain-analyst.md` and inline its full content
- Group name and domain list (G-codes, domain-ids, conditional flags)
- Gap analysis framework: read `${CLAUDE_PLUGIN_ROOT}/references/gap-analysis-framework.md` and inline its full content
- Formatting rules: read `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` and inline its full content
- Domain definitions: read `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/{domain-id}.md` per domain, inline separated by:

```
================================================================================
DOMAIN {domain-id}
================================================================================
```

- **Research evidence map** per domain: extract from each domain definition's `Research provides` section
- **Expected confirmation rate** per domain: extract from each domain definition
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
cat gap-analysis/questions/*-confirmed.txt > gap-analysis/confirmed.txt
cat gap-analysis/questions/*-client.txt > gap-analysis/client-questions.txt
cat gap-analysis/questions/*-agency.txt > gap-analysis/agency-questions.txt

CONFIRMED=$(grep -c '^- ' gap-analysis/confirmed.txt 2>/dev/null || echo 0)
CLIENT=$(grep -c '^\[Q' gap-analysis/client-questions.txt 2>/dev/null || echo 0)
AGENCY=$(grep -c '^\[A' gap-analysis/agency-questions.txt 2>/dev/null || echo 0)
SCOPE=$(grep -c '\[SCOPE:' gap-analysis/confirmed.txt 2>/dev/null || echo 0)
```

Report: "{CONFIRMED} confirmed lines, {CLIENT} client questions, {AGENCY} agency questions, {SCOPE} scope items."

### Step 6: Question deduplication and quality check

Dispatch an agent (model: sonnet) with:
- `gap-analysis/client-questions.txt` path
- `gap-analysis/agency-questions.txt` path
- `gap-analysis/confirmed.txt` path (read-only, for cross-reference)

The agent reads all three files and:

**1. Format check** — verify every entry follows the line format from domain-analyst.md output spec. Flag malformed entries.

**2. Deduplication** — merge semantically overlapping questions across groups:
- Keep the richer question (more research context)
- Combine G-code references: `[G05/G15-Q01]` for questions spanning multiple domains
- Note which domains are served by the merged question

**3. Volume control** — enforce limits:

| File | Target range | Hard maximum |
|---|---|---|
| Client questions | 8–15 | 20 |
| Agency questions | 10–20 | 25 |

If over maximum after dedup: drop leaked NICE-TO-HAVE questions first, merge IMPORTANT questions covering similar ground, escalate to operator only if CRITICAL questions exceed the limit.

**4. Rewrite** `gap-analysis/client-questions.txt` and `gap-analysis/agency-questions.txt` with cleaned versions.

Report: original count → final count per file, duplicates merged.

### Step 7: Debug companion (when enabled)

If `research_config.debug` is `true` in project.json: write `tmp/debug/D4-Gap-Analysis-debug.txt` — confirmed/client/agency/standard/scope counts per group, inactive domains, deduplication stats. No prose.

### Step 8: Update project-state.md

Update Phase 4: status `awaiting_answers`, date today.

```
Domain Gap Analysis — awaiting answers.
  Confirmed: {n} | Standards (scope): {n} | Client questions: {n} | Agency questions: {n}
Working files: gap-analysis/
Next: Fill in answers in gap-analysis/client-questions.txt and gap-analysis/agency-questions.txt, then re-run to resolve.
```

---

## Answer Resolution (re-run after answers are filled)

When the skill is invoked and `gap-analysis/confirmed.txt` already exists with Phase 4 status `awaiting_answers`:

### Step 9: Check for answers

The operator fills in answers directly in `gap-analysis/client-questions.txt` and `gap-analysis/agency-questions.txt` by writing the selected option or free text after each question block.

```bash
CLIENT_ANSWERED=$(grep -c '^Answer: .' gap-analysis/client-questions.txt 2>/dev/null || echo 0)
AGENCY_ANSWERED=$(grep -c '^Answer: .' gap-analysis/agency-questions.txt 2>/dev/null || echo 0)
TOTAL_ANSWERED=$((CLIENT_ANSWERED + AGENCY_ANSWERED))
```

If `TOTAL_ANSWERED == 0`: inform operator no answers found, explain the answer format, stop.

### Step 10: Resolve answers

Dispatch a generic agent (model: sonnet) with:
- `gap-analysis/confirmed.txt` path
- `gap-analysis/client-questions.txt` path
- `gap-analysis/agency-questions.txt` path
- `baseline-log.txt` path
- Formatting rules: read `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` and inline its full content

The agent:

**1. Parse answers** — scan both question files for filled `Answer:` lines.

**2. Append to confirmed.txt** — for each answered question, append under a `RESOLVED ANSWERS` section header, grouped by domain using the same `====` format:

```
================================================================================
RESOLVED ANSWERS
================================================================================

================================================================================
DOMAIN business-context [G05]
================================================================================
- Revenue target: €200-500K annually (client response) — CONFIRMED
```

Entry format: `- {checkpoint}: {answer} ({source}) — CONFIRMED`
Merged questions (e.g., `[G05/G15-Q01]`): add entry under EACH referenced domain.
Unanswered: `- {checkpoint}: unanswered — UNRESOLVED`
Vague answers ("maybe", "not sure"): mark as UNRESOLVED with note.

**3. Append to baseline-log.txt** — add `[D4]` section with key findings only. Include: confirmed capabilities/constraints, critical resolved gaps that shape the concept, unresolved items downstream must work around, N/A domains that narrow scope. Exclude: baseline expectations, NOTED items, STANDARD items.

**4. Report** — total confirmed, resolved from answers, unresolved, baseline-log entries added.

### Step 11: Cross-domain synthesis

Read `gap-analysis/confirmed.txt`, `gap-analysis/client-questions.txt`, and `gap-analysis/agency-questions.txt`. Now that answers are resolved, identify patterns individual analysts cannot see:

**Contradictions:** Findings from one domain conflict with another.
**Tensions:** Multiple domains pull scope in competing directions.
**Compounding insights:** Findings from multiple domains reinforce each other.

Write `D4-Cross-Domain.txt` (root):

```
================================================================================
CROSS-DOMAIN SYNTHESIS
================================================================================

CONTRADICTIONS:
- {Domain A} vs {Domain B}: {description} — Resolution: {recommendation}

TENSIONS:
- {Domain A} ↔ {Domain B}: {description} — Balance: {recommendation}

COMPOUNDING INSIGHTS:
- {Domain list}: {description} — Implication: {recommendation}
```

Telegraphic. Only patterns that change what we propose or how we price it.

### Step 12: Scope implications extraction

Extract all `[SCOPE:]` tagged items from `gap-analysis/confirmed.txt` (now includes resolved answers).

```bash
grep '\[SCOPE:' gap-analysis/confirmed.txt | sort > tmp/scope-raw.txt
```

Read `tmp/scope-raw.txt` and organize into `D4-Scope-Implications.txt` (root):

```
================================================================================
SCOPE IMPLICATIONS — Deliverables from Gap Analysis
================================================================================

COMPLIANCE:
- {item} [{G-code}] — {reason}

INFRASTRUCTURE:
- {item} [{G-code}] — {reason}

MIGRATION:
- {item} [{G-code}] — {reason}

STANDARD:
- {item} [{G-code}] — {reason}

INTEGRATION:
- {item} [{G-code}] — {reason}

================================================================================
Total: {n} scope items across {n} categories
================================================================================
```

### Step 13: Update project-state.md

Update Phase 4: status `complete`, date today.

```
Domain Gap Analysis — complete.
  Confirmed: {n} | Resolved: {n} | Unresolved: {n} | Scope items: {n}
  Cross-domain patterns: {n} contradictions, {n} tensions, {n} compounding
Root output: D4-Scope-Implications.txt, D4-Cross-Domain.txt
Working files: gap-analysis/
Next: Run concept-creation.
```

---

## Rules

<critical>
- NEVER dispatch more than 3 group agents concurrently
- NEVER modify project-state.md beyond Phase 4 rows
- NEVER Read output files into context during Step 5 consolidation — bash only
- ALWAYS use dispatch-subagent skill for every dispatch
- ALWAYS inline gap-analysis-framework.md and formatting-rules.md in every analyst dispatch
- ALWAYS include research evidence map and expected confirmation rates in dispatch
</critical>

- Step 6 (dedup) and Step 11 (cross-domain) DO read output files — they require LLM reasoning
- Step 12 uses bash grep + LLM organization — hybrid approach
- If a group agent fails, report affected domains, continue with remaining groups
- If fewer than 3 groups complete, warn that Phase 5 coverage will be limited
- The operator can re-run answer resolution multiple times as more answers come in

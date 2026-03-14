---
name: domain-gap-analysis
description: "Run Phase 4 domain gap analysis: dispatch up to 6 grouped domain-analyst agents (2 batches of 3), consolidate findings and questions with bash. Invoke when the user says 'run gap analysis', 'domain analysis', 'start phase 4', 'run domains', or after Research phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 2.1.0
---

# Domain Gap Analysis

Dispatch domain-analyst agents for 6 domain groups, then consolidate into D4 deliverables using bash.

## Domain Groups

| Group | G-codes | Domains | Extra context (beyond D1, D2) |
|---|---|---|---|
| **A — Business & Strategy** | G05, G06, G15, G19 | business-context, competitive-landscape, project-scope, target-audience | R3, R4, R7 |
| **B — Technical Foundation** | G13, G16, G20 | performance, security-and-compliance, technical-platform | R5 |
| **C — UX & Design** | G01, G08, G10 | accessibility, design-and-brand, forms-and-lead-capture | R5, R8, R6 |
| **D — Content & SEO** | G07, G17, G18 | content-strategy, seo-and-discoverability, site-structure | R1, R2, R7, R8, R9 |
| **E — Operations** | G02, G14, G11* | analytics-and-measurement, post-launch, migration-and-redesign* | R1, R5, R6 |
| **F — Conditional** | G03*, G04*, G09*, G12*, G21* | blog-and-editorial, booking-and-scheduling, ecommerce, multilingual, user-accounts | R2, R5, R8, R9 |

`*` = conditional domain (agent checks applicability, returns INACTIVE if not applicable)

**Slug derivation:** G-code → slug is the capitalized short form of the domain-id (e.g., G05 → Business, G17 → SEO, G11 → Migration).

**Dispatch:** Batch 1 (A, B, C concurrent) then Batch 2 (D, E, F concurrent). Max 3 concurrent. If 1-3 groups selected, single batch.

## Process

### Step 1: Load project context

Read `project-state.md`. If missing → "Run project-init first." If Phase 3 not complete → "Run project-research first."

Read `D1-Init.json` for project parameters and `notes` (operator observations that inform gap scoring).

### Step 2: Check existing domain outputs

Glob for `gap-analysis/G*-*.json`. Report existing outputs — skipped unless re-run requested.

### Step 3: Domain selection

Present groups from table above. AskUserQuestion with multiSelect=true. Pre-select groups with domains lacking outputs.

### Step 4: Pre-merge context

For each selected group, merge D1, D2, and group-specific R-files into a context file. D1 + D2 are always included; the "Extra context" column lists additional R-files per group.

```bash
mkdir -p tmp gap-analysis/questions

# Group {letter}
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json {R-files from table} -o tmp/context-group-{letter}.json
```

Run only for selected groups. merge-json.sh skips missing files with warnings.

### Step 5: Dispatch domain analysts

Dispatch selected groups via `dispatch-subagent`. Each dispatch provides:
- Group name and domain list (G-codes, slugs, conditional flags)
- Domain definitions: inline `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/{domain-id}.md` per domain, separated by `--- DOMAIN: {domain-id} ---`
- Output template: inline `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/templates/domain-output-template.md`
- Context file path: `{working_directory}/tmp/context-group-{letter}.json`
- Model: sonnet | MCP hints: none

**After each batch:** report per-domain status, questions generated, failures.

### Step 6: Consolidate with bash

<critical>
Use ONLY bash (jq, cat, echo). Do NOT Read any G-file, R-file, or D-file into context.
</critical>

```bash
# JSON consolidation
jq -s '{meta:{date:(now|todate),active_domains:[.[]|select(.status=="ACTIVE")|.domain],inactive_domains:[.[]|select(.status=="INACTIVE")|.domain],total_critical_unresolved:([.[]|select(.status=="ACTIVE")|(.counts.critical_total-.counts.critical_resolved)]|add//0),total_questions:([.[]|select(.status=="ACTIVE")|.counts.questions_generated]|add//0),status:"awaiting_answers"},domains:.}' gap-analysis/G*-*.json > D4-Gap-Analysis.json

# Questions consolidation
if ls gap-analysis/questions/G*-*-questions.json 1>/dev/null 2>&1; then
  jq -s 'add' gap-analysis/questions/G*-*-questions.json > D4-Questions.json
else
  echo '[]' > D4-Questions.json
fi

# Answers template
jq '[.[] | {id, domain, checkpoint, answer: null}]' D4-Questions.json > D4-Answers.json

# Markdown consolidation
CLIENT=$(jq -r '.project.client' D1-Init.json)
ACTIVE=$(jq '[.meta.active_domains|length]|.[0]' D4-Gap-Analysis.json)
TOTAL=$(jq '[.meta.active_domains,.meta.inactive_domains]|map(length)|add' D4-Gap-Analysis.json)
CRIT=$(jq '.meta.total_critical_unresolved' D4-Gap-Analysis.json)
QUESTIONS=$(jq '.meta.total_questions' D4-Gap-Analysis.json)
DATE=$(date +%Y-%m-%d)
echo "# Domain Gap Analysis -- $CLIENT
*Generated: $DATE | Active domains: $ACTIVE/$TOTAL | Critical unresolved: $CRIT | Questions: $QUESTIONS*
*Answer all CRITICAL questions in D4-Questions.json before proceeding to Concept Creation.*

---
" > D4-Gap-Analysis.md
cat gap-analysis/G*-*.md >> D4-Gap-Analysis.md
echo "
---
*Return D4-Questions.json with answers to proceed to Concept Creation.*" >> D4-Gap-Analysis.md
```

### Step 6b: Question curation

Dispatch the `question-curator` agent to classify, deduplicate, and rewrite raw questions.

**Pre-merge context:** Reuse D1 + D2 context (same as domain analyst context but without R-files — curator only needs project parameters and client intelligence).

```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json -o tmp/context-curator.json
```

**Extract output_language:**

```bash
OUTPUT_LANG=$(jq -r '."D1-Init".output_language // "en"' tmp/context-curator.json)
```

**Dispatch via `dispatch-subagent`:**
- Agent: `question-curator`
- Model: `opus`
- Mode: Lightweight (no MCP)
- Prompt payload:
  - Context file path: `{working_directory}/tmp/context-curator.json`
  - Questions file path: `{working_directory}/D4-Questions.json`
  - Output directory: `{working_directory}`
  - Output language: `{OUTPUT_LANG}`

**After dispatch:** Verify all original question IDs are accounted for:

```bash
ORIGINAL=$(jq 'length' D4-Questions.json)
CLIENT=$(jq '[.[].original_ids[]] | length' D4-Questions-Client.json 2>/dev/null || echo 0)
AGENCY=$(jq '[.[].original_ids[]] | length' D4-Questions-Agency.json 2>/dev/null || echo 0)
DEDUCED=$(jq 'length' D4-Deductions.json 2>/dev/null || echo 0)
PLAYBOOK=$(grep -c '\[G[0-9]*-Q[0-9]*\]' D4-Agency-Playbook.md 2>/dev/null || echo 0)
CURATED=$((CLIENT + AGENCY + DEDUCED + PLAYBOOK))
if [[ "$CURATED" -lt "$ORIGINAL" ]]; then
    echo "WARNING: $((ORIGINAL - CURATED)) questions missing from curated output ($CURATED/$ORIGINAL)"
fi
```

### Step 7: Update project-state.md

Update Phase 4: status `complete`/`partial`, output files including curated outputs, date today.

```
Domain Gap Analysis complete.
  Groups: {n}/6 | Active: {n} | Inactive: {n} | Failed: {n or "none"}
  Critical unresolved: {n} | Questions: {n} (Client: {n}, Agency: {n}, Deduced: {n}, Playbook: {n})
Output: D4-Gap-Analysis.json, D4-Questions.json, D4-Answers.json,
        D4-Questions-Client.json, D4-Questions-Client.md,
        D4-Questions-Agency.json, D4-Deductions.json, D4-Agency-Playbook.md
Next: Fill in D4-Questions-Client.json + D4-Questions-Agency.json, then re-run to resolve.
```

### Step 8: Answer Resolution (conditional)

First, compile curated answers into D4-Answers.json:

**8a.** Run `scripts/compile-answers.sh {working_directory} -v` to merge CLIENT + AGENCY + DEDUCED answers into D4-Answers.json.

Check if D4-Answers.json has answered entries after compilation:

```bash
ANSWERED=$(jq '[.[] | select(.answer != null)] | length' D4-Answers.json)
DOMAINS=$(jq '[.[] | select(.answer != null) | .domain] | unique | length' D4-Answers.json)
```

Skip if `ANSWERED == 0`. Otherwise AskUserQuestion: "D4-Answers.json has {ANSWERED} answers across {DOMAINS} domains. Resolve?"

If yes:

**8b.** Run `scripts/resolve-answers.sh D4-Answers.json gap-analysis/ -v`

**8c.** Dispatch `answer-resolver` per updated domain via `dispatch-subagent` (G-file path + markdown path, model sonnet, Lightweight mode, max 6 concurrent)

**8d.** Rerun Step 6 bash commands to rebuild D4 consolidation files

**8e.** Update Phase 4 status → `resolved`

```
Answer resolution complete.
  Domains revised: {n} | Questions resolved: {total}
  Critical unresolved: {x} (was {y})
Next: Run concept-creation.
```

## Rules

<critical>
- NEVER dispatch more than 3 group agents concurrently
- NEVER modify project-state.md beyond Phase 4 rows
- NEVER Read domain output files into context — use jq extraction only
- ALWAYS use dispatch-subagent skill for every dispatch
- ALWAYS pre-merge context files before dispatching
- ALWAYS create gap-analysis/questions/ directory before dispatching
</critical>

- If a group agent fails, report affected domains, continue with remaining groups
- If fewer than 10 domains complete, warn that Phase 5 coverage will be limited

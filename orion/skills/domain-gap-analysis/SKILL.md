---
name: domain-gap-analysis
description: "Run Phase 4 domain gap analysis: dispatch up to 6 grouped domain-analyst agents (2 batches of 3), consolidate findings and questions with bash. Invoke when the user says 'run gap analysis', 'domain analysis', 'start phase 4', 'run domains', or after Research phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 2.0.0
---

# Domain Gap Analysis

Dispatch domain-analyst agents for 6 domain groups, then consolidate into D4-Gap-Analysis and D4-Questions using bash.

## Domain Groups

| Group | G-codes | Domains | Context Files |
|---|---|---|---|
| **A — Business & Strategy** | G05, G06, G15, G19 | business-context, competitive-landscape, project-scope, target-audience | D1, D2, R3, R4, R7 |
| **B — Technical Foundation** | G13, G16, G20 | performance, security-and-compliance, technical-platform | D1, D2, R5 |
| **C — UX & Design** | G01, G08, G10 | accessibility, design-and-brand, forms-and-lead-capture | D1, D2, R5, R8, R6 |
| **D — Content & SEO** | G07, G17, G18 | content-strategy, seo-and-discoverability, site-structure | D1, D2, R1, R2, R7, R8, R9 |
| **E — Operations** | G02, G14, G11* | analytics-and-measurement, post-launch, migration-and-redesign* | D1, D2, R1, R5, R6 |
| **F — Conditional** | G03*, G04*, G09*, G12*, G21* | blog-and-editorial, booking-and-scheduling, ecommerce, multilingual, user-accounts | D1, D2, R2, R5, R8, R9 |

`*` = conditional domain (agent checks applicability, returns INACTIVE if not applicable)

**Dispatch:** Batch 1 (A, B, C concurrent) then Batch 2 (D, E, F concurrent). Max 3 concurrent. If 1-3 groups selected, single batch.

## Slug Reference

| Code | Slug | Code | Slug | Code | Slug |
|---|---|---|---|---|---|
| G01 | Accessibility | G08 | Design | G15 | Project-Scope |
| G02 | Analytics | G09 | Ecommerce | G16 | Security |
| G03 | Blog | G10 | Forms | G17 | SEO |
| G04 | Booking | G11 | Migration | G18 | Site-Structure |
| G05 | Business | G12 | Multilingual | G19 | Target-Audience |
| G06 | Competitive | G13 | Performance | G20 | Technical |
| G07 | Content | G14 | Post-Launch | G21 | User-Accounts |

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 3 (Research) not complete, stop: "Run project-research first."

Read `D1-Init.json` for project parameters: client name, site_type, build_type, languages, notes.

### Step 2: Check existing domain outputs

Glob for `gap-analysis/G*-*.json`. Report existing outputs and note they will be skipped unless re-run requested.

### Step 3: Domain selection

Present groups from the Domain Groups table. Use AskUserQuestion with multiSelect=true. Pre-select all groups with domains lacking existing outputs. Selection is at group level — all domains within selected groups are included.

### Step 4: Pre-merge context

For each selected group, run `merge-json.sh` to create a group-specific context file:

```bash
mkdir -p tmp gap-analysis/questions

# Group A — Business & Strategy
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R3-Competitors.json research/R4-Market.json research/R7-Audience.json -o tmp/context-group-A.json

# Group B — Technical Foundation
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R5-Technology.json -o tmp/context-group-B.json

# Group C — UX & Design
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R5-Technology.json research/R8-UX.json research/R6-Reputation.json -o tmp/context-group-C.json

# Group D — Content & SEO
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R1-SERP.json research/R2-Keywords.json research/R7-Audience.json research/R8-UX.json research/R9-Content.json -o tmp/context-group-D.json

# Group E — Operations
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R1-SERP.json research/R5-Technology.json research/R6-Reputation.json -o tmp/context-group-E.json

# Group F — Conditional
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json research/R2-Keywords.json research/R5-Technology.json research/R8-UX.json research/R9-Content.json -o tmp/context-group-F.json
```

Only run merge for selected groups. merge-json.sh skips missing files with warnings.

### Step 5: Dispatch domain analysts

Dispatch selected groups via `dispatch-subagent`. Each dispatch provides:
- Group name and domain list (G-codes, slugs, conditional flags from table above)
- Domain definitions: read and inline `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/{domain-id}.md` for each domain, separated by `--- DOMAIN: {domain-id} ---` headers
- Output template: read and inline `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/templates/domain-output-template.md`
- Context file path: `{working_directory}/tmp/context-group-{letter}.json`
- Model: sonnet
- MCP hints: none

**After each batch:** report group completion, per-domain status (ACTIVE/INACTIVE), questions generated, failures.

### Step 6: Consolidate with bash

<critical>
Use ONLY bash (jq, cat, echo). Do NOT Read any G-file, R-file, or D-file into context.
</critical>

**JSON consolidation (findings):**

```bash
jq -s '{meta:{date:(now|todate),active_domains:[.[]|select(.status=="ACTIVE")|.domain],inactive_domains:[.[]|select(.status=="INACTIVE")|.domain],total_critical_unresolved:([.[]|select(.status=="ACTIVE")|(.counts.critical_total-.counts.critical_resolved)]|add//0),total_questions:([.[]|select(.status=="ACTIVE")|.counts.questions_generated]|add//0),status:"awaiting_answers"},domains:.}' gap-analysis/G*-*.json > D4-Gap-Analysis.json
```

**Questions consolidation:**

```bash
if ls gap-analysis/questions/G*-*-questions.json 1>/dev/null 2>&1; then
  jq -s 'add' gap-analysis/questions/G*-*-questions.json > D4-Questions.json
else
  echo '[]' > D4-Questions.json
fi
```

**Answers template:**

```bash
jq '[.[] | {id, domain, checkpoint, answer: null}]' D4-Questions.json > D4-Answers.json
```

**Markdown consolidation:**

```bash
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

### Step 7: Update project-state.md

Update Phase 4 row:
- Status: `complete` or `partial`
- Output: `D4-Gap-Analysis.json, D4-Questions.json, D4-Answers.json`
- Updated: today's date

Display summary:

```
Domain Gap Analysis complete.

  Groups dispatched: {n}/6
  Active domains: {n}  |  Inactive: {n}  |  Failed: {n or "none"}
  Total CRITICAL unresolved: {n}
  Total questions generated: {n}

Output:
  D4-Gap-Analysis.json — domain findings
  D4-Questions.json — structured questions with answer options
  D4-Answers.json — answer template (fill in, then re-run skill to resolve)

Next: Fill in D4-Answers.json, then re-run domain-gap-analysis to resolve.
```

### Step 8: Answer Resolution (conditional)

Check if `D4-Answers.json` exists in the working directory.

If not found, skip this step entirely (first run — no answers yet).

If found, count answered entries (`answer != null`) using bash:

```bash
ANSWERED=$(jq '[.[] | select(.answer != null)] | length' D4-Answers.json)
DOMAINS=$(jq '[.[] | select(.answer != null) | .domain] | unique | length' D4-Answers.json)
```

If `ANSWERED == 0`, skip (template exists but no answers filled in yet).

If `ANSWERED > 0`, use AskUserQuestion:
"D4-Answers.json found with {ANSWERED} answers across {DOMAINS} domains. Resolve G-files with client answers?"

If yes:

**8a. Mechanical insert:**

```bash
scripts/resolve-answers.sh D4-Answers.json gap-analysis/ -v
```

**8b. Dispatch answer-resolver per updated domain:**

For each domain that was updated (reported by resolve-answers.sh), dispatch `answer-resolver` via `dispatch-subagent`:
- G-file path: `{working_directory}/gap-analysis/{code}-{slug}.json`
- Markdown path: `{working_directory}/gap-analysis/{code}-{slug}.md`
- Model: sonnet
- MCP hints: none (Lightweight mode)
- Max 6 concurrent dispatches

**8c. Re-consolidate:**

Rerun the Step 6 bash commands (JSON consolidation, answers template, markdown consolidation) to rebuild D4-Gap-Analysis.json, D4-Answers.json, and D4-Gap-Analysis.md with resolved counts.

**8d. Update project-state.md:**

Update Phase 4 row status to `resolved`. Display:

```
Answer resolution complete.
  Domains revised: {n}
  Questions resolved: {total}
  Critical unresolved: {x} (was {y})
  Phase 4 status: resolved
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

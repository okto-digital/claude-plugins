---
name: domain-gap-analysis
description: "Run Phase 4 domain gap analysis: dispatch up to 6 grouped domain-analyst agents (2 batches of 3), consolidate findings and questions with bash. Invoke when the user says 'run gap analysis', 'domain analysis', 'start phase 4', 'run domains', or after Research phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 3.0.0
---

# Domain Gap Analysis

Dispatch domain-analyst agents for 6 domain groups, curate questions, pause for answers, then finalize all domains and produce D4-Gap-Analysis.json (TLDR consolidation).

## Domain Groups

| Group | G-codes | Domains | Relevant research (via D3 TLDRs) |
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

For each selected group, merge D1, D2, and D3 (research TLDR digest) into a context file. D3 contains all 9 research TLDRs (~10-15KB) — small enough to include in every group. All groups receive the same context base. The "Relevant research" column in the table above is informational — it shows which substage TLDRs are most useful per group, but all TLDRs are available via D3.

```bash
mkdir -p tmp gap-analysis/questions

# Same context base for all groups — D1 + D2 + D3
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json -o tmp/context-group-{letter}.json
```

Run only for selected groups. merge-json.sh skips missing files with warnings.

### Step 5: Dispatch domain analysts

Dispatch selected groups via `dispatch-subagent`. Each dispatch provides:
- Group name and domain list (G-codes, slugs, conditional flags)
- Domain definitions: inline `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/{domain-id}.md` per domain, separated by `--- DOMAIN: {domain-id} ---`
- Output template: inline `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/templates/domain-output-template.md`
- Context file path: `{working_directory}/tmp/context-group-{letter}.json`
- Model: sonnet | MCP hints: none

**After each batch:**

1. **Validate JSON outputs:**
```bash
scripts/validate-json.sh gap-analysis/G*-*.json gap-analysis/questions/G*-*-questions.json
```
If any file fails: attempt `jq -c '.' broken.json > broken.json.tmp && mv broken.json.tmp broken.json`. If jq also fails, re-dispatch the group containing the broken domain.

2. Report per-domain status, questions generated, failures.

### Step 6: Consolidate raw questions

<critical>
Use ONLY bash (jq, cat, echo). Do NOT Read any G-file, R-file, or D-file into context.
All working files go to `gap-analysis/`. D4-Gap-Analysis.json does NOT exist yet — it is produced after answer resolution in Step 8.
</critical>

```bash
# Questions consolidation
if ls gap-analysis/questions/G*-*-questions.json 1>/dev/null 2>&1; then
  jq -s 'add' gap-analysis/questions/G*-*-questions.json > gap-analysis/D4-Questions.json
else
  echo '[]' > gap-analysis/D4-Questions.json
fi

# Answers template
jq '[.[] | {id, domain, checkpoint, answer: null}]' gap-analysis/D4-Questions.json > gap-analysis/D4-Answers.json

# Markdown versions
jq -r '"# Raw Questions\n\n" + ([.[] | "- **[\(.id)]** \(.domain) — \(.question)"] | join("\n"))' gap-analysis/D4-Questions.json > gap-analysis/D4-Questions.md
echo "# Answers\n\nAll answers pending." > gap-analysis/D4-Answers.md

# Count stats
QUESTIONS=$(jq 'length' gap-analysis/D4-Questions.json)
ACTIVE=$(jq -s '[.[]|select(.status=="ACTIVE")]|length' gap-analysis/G*-*.json)
INACTIVE=$(jq -s '[.[]|select(.status=="INACTIVE")]|length' gap-analysis/G*-*.json)
CRIT=$(jq -s '[.[]|select(.status=="ACTIVE")|(.counts.critical_total-.counts.critical_resolved)]|add//0' gap-analysis/G*-*.json)
```

### Step 6b: Question curation

Dispatch the `question-curator` agent to classify, deduplicate, and rewrite raw questions.

**Pre-merge context:**

```bash
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json -o tmp/context-curator.json
OUTPUT_LANG=$(jq -r '."D1-Init".output_language // "en"' tmp/context-curator.json)
```

**Dispatch via `dispatch-subagent`:**
- Agent: `question-curator`
- Model: `opus`
- Mode: Lightweight (no MCP)
- Prompt payload:
  - Context file path: `{working_directory}/tmp/context-curator.json`
  - Questions file path: `{working_directory}/gap-analysis/D4-Questions.json`
  - Output directory: `{working_directory}/gap-analysis`
  - Output language: `{OUTPUT_LANG}`

**After dispatch:** Verify all original question IDs are accounted for:

```bash
ORIGINAL=$(jq 'length' gap-analysis/D4-Questions.json)
CLIENT=$(jq '[.[].original_ids[]] | length' gap-analysis/D4-Questions-Client.json 2>/dev/null || echo 0)
AGENCY=$(jq '[.[].original_ids[]] | length' gap-analysis/D4-Questions-Agency.json 2>/dev/null || echo 0)
DEDUCED=$(jq 'length' gap-analysis/D4-Deductions.json 2>/dev/null || echo 0)
PLAYBOOK=$(grep -c '\[G[0-9]*-Q[0-9]*\]' gap-analysis/D4-Agency-Playbook.md 2>/dev/null || echo 0)
CURATED=$((CLIENT + AGENCY + DEDUCED + PLAYBOOK))
if [[ "$CURATED" -lt "$ORIGINAL" ]]; then
    echo "WARNING: $((ORIGINAL - CURATED)) questions missing from curated output ($CURATED/$ORIGINAL)"
fi

# Curation summary
cat > gap-analysis/D4-CURATION-SUMMARY.txt <<EOF
Curation Summary — $(date +%Y-%m-%d)
Original questions: $ORIGINAL
Client: $CLIENT | Agency: $AGENCY | Deduced: $DEDUCED | Playbook: $PLAYBOOK
Accounted: $CURATED/$ORIGINAL
EOF
```

### Step 7: Update project-state.md

Update Phase 4: status `awaiting_answers`, output files including curated outputs, date today.

```
Domain Gap Analysis — awaiting answers.
  Groups: {n}/6 | Active: {n} | Inactive: {n} | Failed: {n or "none"}
  Critical unresolved: {n} | Questions: {n} (Client: {n}, Agency: {n}, Deduced: {n}, Playbook: {n})
Working files: gap-analysis/D4-Questions-Client.json, D4-Questions-Agency.json, D4-Answers.json, etc.
Next: Fill in gap-analysis/D4-Questions-Client.json + D4-Questions-Agency.json, then re-run to resolve.
```

### Step 8: Answer Resolution (conditional)

**8a.** Compile curated answers into D4-Answers.json:

```bash
scripts/compile-answers.sh {working_directory} -v

# Regenerate D4-Answers.md with compiled answers
jq -r '"# Compiled Answers\n\n" + ([.[] | if .answer != null then "- **[\(.id)]** \(.domain) — \(.answer)" else "- **[\(.id)]** \(.domain) — *(unanswered)*" end] | join("\n"))' gap-analysis/D4-Answers.json > gap-analysis/D4-Answers.md
```

Check if answers exist:

```bash
ANSWERED=$(jq '[.[] | select(.answer != null)] | length' gap-analysis/D4-Answers.json)
DOMAINS=$(jq '[.[] | select(.answer != null) | .domain] | unique | length' gap-analysis/D4-Answers.json)
```

Skip if `ANSWERED == 0`. Otherwise AskUserQuestion: "D4-Answers.json has {ANSWERED} answers across {DOMAINS} domains. Resolve?"

If yes:

**8b.** Resolve answers into G-files:

```bash
scripts/resolve-answers.sh gap-analysis/D4-Answers.json gap-analysis/ -v
```

**8c.** Dispatch `domain-finalizer` for **ALL active domains** (not just answered ones) via `dispatch-subagent`. Each dispatch provides: G-file path + markdown path. Model: sonnet. Lightweight mode. Max 6 concurrent.

The domain-finalizer adds TLDRs, rewrites `"Client:"` evidence, updates summary and counts for every active domain.

**8d.** Build D4-Gap-Analysis.json — TLDR consolidation following D3 pattern:

```bash
jq -s '{meta:{date:(now|todate),status:"resolved",active_domains:[.[]|select(.status=="ACTIVE")|.domain],inactive_domains:[.[]|select(.status=="INACTIVE")|.domain],total_found:([.[]|select(.status=="ACTIVE")|.counts.found]|add//0),total_gap:([.[]|select(.status=="ACTIVE")|.counts.gap]|add//0),total_critical_resolved:([.[]|select(.status=="ACTIVE")|.counts.critical_resolved]|add//0),total_critical_total:([.[]|select(.status=="ACTIVE")|.counts.critical_total]|add//0)},domains:[.[]|if .status=="ACTIVE" then {code,slug,domain,status,tldr,summary,counts} else {code,slug,domain,status,inactive_reason} end]}' gap-analysis/G*-*.json > D4-Gap-Analysis.json
```

Key: domains array contains TLDR + summary + counts per domain (not full findings). Full G-files remain in `gap-analysis/` for reference but are not read downstream.

**8e.** Build D4-Gap-Analysis.md:

```bash
CLIENT=$(jq -r '.project.client' D1-Init.json)
ACTIVE=$(jq '.meta.active_domains|length' D4-Gap-Analysis.json)
TOTAL=$(jq '[.meta.active_domains,.meta.inactive_domains]|map(length)|add' D4-Gap-Analysis.json)
FOUND=$(jq '.meta.total_found' D4-Gap-Analysis.json)
GAP=$(jq '.meta.total_gap' D4-Gap-Analysis.json)
CRIT_R=$(jq '.meta.total_critical_resolved' D4-Gap-Analysis.json)
CRIT_T=$(jq '.meta.total_critical_total' D4-Gap-Analysis.json)
DATE=$(date +%Y-%m-%d)

echo "# Domain Gap Analysis — $CLIENT
*Generated: $DATE | Active: $ACTIVE/$TOTAL | Found: $FOUND | Gap: $GAP | Critical: $CRIT_R/$CRIT_T resolved*

---
" > D4-Gap-Analysis.md

# Per-domain TLDR sections
jq -r '.domains[] | if .status == "ACTIVE" then "## \(.slug)\n**\(.domain)** — \(.summary)\n\n### TLDR\n" + ([.tldr[] | "- " + .] | join("\n")) + "\n\n---\n" else "## \(.slug)\n**\(.domain)** — INACTIVE: \(.inactive_reason)\n\n---\n" end' D4-Gap-Analysis.json >> D4-Gap-Analysis.md
```

**8f.** Update Phase 4 status → `resolved`:

```
Answer resolution complete.
  Domains finalized: {n} | Questions resolved: {total}
  Critical resolved: {x}/{y}
Output: D4-Gap-Analysis.json, D4-Gap-Analysis.md
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

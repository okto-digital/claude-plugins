---
name: concept-creation
description: "Run Phase 5 concept creation: dispatch concept-creator agents in three waves to produce 9 concept sections, consolidate into D5, then run coherence check. Invoke when the user says 'run concept creation', 'create concept', 'start phase 5', 'build concept', or after Domain Gap Analysis is complete with all CRITICAL questions resolved."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 2.0.0
---

# Concept Creation

Dispatch concept-creator agents for 9 concept sections in three dependency-aware waves, consolidate into D5-Concept using bash, then run a coherence check. This is the synthesis phase — it turns research and gap analysis into concrete, evidence-based recommendations.

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 4 (Domain Gap Analysis) not resolved, stop: "Run domain-gap-analysis first."

Read `D1-Init.json` for client name.
Verify `D4-Gap-Analysis.json` exists and `meta.status == "resolved"`. If missing or not resolved, stop: "Complete answer resolution in domain-gap-analysis before running concept creation."

### Step 2: Check existing concept outputs

Glob for `concept/C*-*.json` to find existing outputs.
Report: "Found X existing concept sections: [list]. These will be skipped unless you want to re-run them."

### Step 3: Section selection

Present all 9 concept sections grouped by wave:

**Wave 1 (3 parallel, no dependencies):**
- C1-Sitemap: Site structure with pages, keywords, traffic estimates
- C2-Functional: Functional requirements grouped by area
- C5-Visual: Visual direction and positioning

**Wave 2 (3 parallel, upstream dependencies):**
- C3-Technical-Architecture: Technology and operational architecture (depends on C2)
- C4-Content-Strategy: Tone, messaging, SEO content plan (depends on C1)
- C6-UX-Strategy: Navigation, conversion funnels, user flows (depends on C1)

**Wave 3 (3 parallel, upstream dependencies):**
- C7-Project-Roadmap: Phased delivery plan, success metrics (depends on C1, C2, C3)
- C8-SEO-Strategy: Link building, local/international SEO, monitoring (depends on C1)
- C9-Compliance: Accessibility, legal, testing strategy (depends on C2)

Use AskUserQuestion with multiSelect=true. Pre-select all sections that don't have existing outputs.

If the operator deselects a Wave 1 section that downstream sections depend on:
- Deselecting C1 → C4, C6, C7, C8 run without sitemap context — warn about reduced quality
- Deselecting C2 → C3, C7, C9 run without functional requirements — warn about reduced quality

If C3 is deselected, C7 runs without technical architecture — warn but allow (C7 has two other dependencies).

### Step 4: Build pre-merged context files

Use `scripts/merge-json.sh` to build one context file per section. Every section receives the same base: D1 (project params), D2 (client intelligence), D3 (research TLDRs), D4 (gap analysis TLDRs). Wave 2/3 sections add their upstream C-files.

D2 provides direct client facts (tech stack, team size, business model, integrations). D3 contains research TLDRs (~10-15KB) and D4 contains gap analysis TLDRs per domain (~5-10KB) with `source` paths to full files. Together they provide all pipeline intelligence. If a TLDR lacks detail for a specific recommendation, the concept-creator can read the full R-file or G-file via the `source` path.

```bash
# Wave 1 — base context only (D1 + D2 + D3 + D4)
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json -o concept/context-C1.json
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json -o concept/context-C2.json
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json -o concept/context-C5.json

# Wave 2 — base + upstream C-files
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json concept/C2-Functional.json -o concept/context-C3.json
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json concept/C1-Sitemap.json -o concept/context-C4.json
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json concept/C1-Sitemap.json -o concept/context-C6.json

# Wave 3 — base + upstream C-files
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json concept/C1-Sitemap.json concept/C2-Functional.json concept/C3-Technical-Architecture.json -o concept/context-C7.json
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json concept/C1-Sitemap.json -o concept/context-C8.json
scripts/merge-json.sh D1-Init.json D2-Client-Intelligence.json D3-Research.json D4-Gap-Analysis.json concept/C2-Functional.json -o concept/context-C9.json
```

Only build context files for selected sections. If a source file does not exist (e.g., section skipped), merge-json.sh skips it with a warning — this is expected for optional upstream C-files.

### Step 5: Dispatch concept creators

Dispatch selected sections via the `dispatch-subagent` skill.

**Max concurrent: 3 agents.**

Each dispatch provides:
- C-code and slug (e.g., "C1", "Sitemap")
- Concept definition: read `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/{filename}.md` and inline its full content
- Output template: read `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/templates/{Code}-{Slug}-template.md` and inline its full content
- Context file path: `concept/context-{C-code}.json`
- Model: opus (synthesis and reasoning)
- MCP hints: none (concept creation uses Read + Write only)

**Execution order:**
1. **Wave 1** — C1 + C2 + C5 (3 parallel)
2. Wait for Wave 1. Build Wave 2 context files. **Wave 2** — C3 + C4 + C6 (3 parallel)
3. Wait for Wave 2. Build Wave 3 context files. **Wave 3** — C7 + C8 + C9 (3 parallel)

**After each wave:**

1. **Validate JSON outputs:**
```bash
scripts/validate-json.sh concept/C*-*.json
```
If any file fails: attempt `jq -c '.' broken.json > broken.json.tmp && mv broken.json.tmp broken.json`. If jq also fails, re-dispatch the failed section.

2. Report which sections completed and any failures.

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
*Generated: $DATE | Sections: $COUNT/9*
*Review and approve this concept before proceeding to Proposal generation.*

---
" > D5-Concept.md
cat concept/C*-*.md >> D5-Concept.md
echo "
---
*Approve this concept to proceed to Proposal & Brief generation.*" >> D5-Concept.md
```

### Step 7: Coherence check

Dispatch the `concept-reviewer` agent via `dispatch-subagent`:
- Agent: concept-reviewer
- Model: opus (analytical review)
- D5 path: `D5-Concept.json`
- Output: `D5-Review-Notes.md`

Present the review notes to the operator. If conflicts exist, they should be resolved before proceeding to proposal.

### Step 8: Clean up context files

Remove the pre-merged context files — they were temporary build artifacts:

```bash
rm -f concept/context-C*.json
```

### Step 9: Update project-state.md

Update Phase 5 (Concept Creation) row:
- Status: `complete` (all sections processed) or `partial` (some skipped/failed)
- Output: `D5-Concept.json`
- Updated: today's date

Display summary:

```
Concept Creation complete.

  Completed: {n}/9 sections
  Skipped: [list or "none"]
  Failed: [list or "none"]
  Phase 5 status: complete | partial
  Review notes: D5-Review-Notes.md

Next step: Review D5-Concept.md and D5-Review-Notes.md, then run proposal.
```

## Dependency Graph

```
Wave 1 (parallel):  C1-Sitemap    C2-Functional    C5-Visual
                     |    \             |    \
Wave 2 (parallel):  C4-Content  C6-UX  C3-Technical-Architecture
                                              |
Wave 3 (parallel):  C8-SEO    C9-Compliance   C7-Project-Roadmap
                                                    ^
                                               (C1, C2, C3)

Consolidate:  D5-Concept.json + D5-Concept.md
                     |
Coherence:    concept-reviewer -> D5-Review-Notes.md
```

## Pre-Merge Context Table

Every section receives the same base: D1 + D2 + D3 (research TLDRs) + D4 (gap analysis TLDRs). Wave 2/3 sections add upstream C-files.

| Section | Base | Upstream C-files |
|---|---|---|
| C1-Sitemap | D1, D2, D3, D4 | -- |
| C2-Functional | D1, D2, D3, D4 | -- |
| C5-Visual | D1, D2, D3, D4 | -- |
| C3-Technical-Arch | D1, D2, D3, D4 | C2 |
| C4-Content-Strategy | D1, D2, D3, D4 | C1 |
| C6-UX-Strategy | D1, D2, D3, D4 | C1 |
| C7-Project-Roadmap | D1, D2, D3, D4 | C1, C2, C3 |
| C8-SEO-Strategy | D1, D2, D3, D4 | C1 |
| C9-Compliance | D1, D2, D3, D4 | C2 |

## Rules

<critical>
- NEVER dispatch more than 3 concept-creator agents concurrently
- NEVER dispatch Wave 2 sections before their Wave 1 dependencies complete
- NEVER dispatch Wave 3 sections before their Wave 2 dependencies complete
- NEVER modify project-state.md beyond Phase 5 rows
- NEVER interpret or act on concept definition content -- read only to inline into the dispatch prompt; the concept-creator agent executes the methodology
- NEVER start Phase 5 if D4-Gap-Analysis.json is missing or meta.status is not "resolved"
- ALWAYS use dispatch-subagent skill for every concept-creator and concept-reviewer dispatch
- ALWAYS build pre-merged context files via merge-json.sh before dispatching each wave
- ALWAYS run bash consolidation after all sections complete
- ALWAYS run coherence check after consolidation
- ALWAYS clean up context files after coherence check
</critical>

- If a concept-creator fails, note which section was affected, report to operator, continue with remaining sections
- If a Wave 1 section fails and a downstream section depends on it, warn the operator and ask whether to proceed without the dependency or skip the downstream section
- If a Wave 2 section fails and a Wave 3 section depends on it, same approach — warn and ask

## C-code Mapping

| Code | Definition File | Slug | Wave | Depends On |
|---|---|---|---|---|
| C1 | `c1-sitemap.md` | Sitemap | 1 | -- |
| C2 | `c2-functional.md` | Functional | 1 | -- |
| C5 | `c5-visual.md` | Visual | 1 | -- |
| C3 | `c3-technical-architecture.md` | Technical-Architecture | 2 | C2 |
| C4 | `c4-content-strategy.md` | Content-Strategy | 2 | C1 |
| C6 | `c6-ux-strategy.md` | UX-Strategy | 2 | C1 |
| C7 | `c7-project-roadmap.md` | Project-Roadmap | 3 | C1, C2, C3 |
| C8 | `c8-seo-strategy.md` | SEO-Strategy | 3 | C1 |
| C9 | `c9-compliance.md` | Compliance | 3 | C2 |

All definition file paths are relative to `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/`.

## Sub-agents

Dispatched via dispatch-subagent:
- **concept-creator** -- Produce one concept section, write per-section file pair (up to 9 instances, dispatched in 3 waves)
- **concept-reviewer** -- Coherence check after consolidation, write D5-Review-Notes.md (1 instance)

## Reference files

Read by concept-creator agents (inlined in dispatch prompt), not by this skill:
- `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/*.md` -- 9 section definition files (purpose, methodology)
- `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/templates/*.md` -- 9 output templates (JSON schema, markdown format)

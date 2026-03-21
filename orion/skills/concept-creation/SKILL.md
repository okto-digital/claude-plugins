---
name: concept-creation
description: "Run Phase 5 concept creation: dispatch concept-creator agents in three waves to produce 9 concept sections as scannable TXT, consolidate into D5, then run coherence check. Invoke when the user says 'run concept creation', 'create concept', 'start phase 5', 'build concept', or after Domain Gap Analysis is complete with all CRITICAL questions resolved."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 4.0.0
---

# Concept Creation

Dispatch concept-creator agents for 9 concept sections in three dependency-aware waves, consolidate into D5-Concept.txt using bash, then run a coherence check. This is the synthesis phase — it turns research and gap analysis into concrete, evidence-based recommendations using the ICIP thinking sequence.

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 4 (Domain Gap Analysis) not resolved, stop: "Run domain-gap-analysis first."

Read `project.json` for client name and project configuration.
Verify D4 status is resolved. If missing or not resolved, stop: "Complete answer resolution in domain-gap-analysis before running concept creation."

### Step 2: Check existing concept outputs

Glob for `concept/C*-*.txt` to find existing outputs.
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

### Step 4: Dispatch concept creators

Dispatch selected sections via the `dispatch-subagent` skill.

**Max concurrent: 3 agents.**

Each dispatch provides:
- C-code and slug (e.g., "C1", "Sitemap")
- Solution framework: read `${CLAUDE_PLUGIN_ROOT}/references/solution-framework.md` and inline its full content
- Formatting rules: read `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` and inline its full content
- Concept definition: read `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/{filename}.md` and inline its full content
- Output guide: read `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/templates/{Code}-{Slug}-template.md` and inline its full content
- baseline-log.txt path: `{working_directory}/baseline-log.txt`
- project.json path: `{working_directory}/project.json`
- Output path: `{working_directory}/concept/{C-code}-{Slug}.txt`
- Upstream C-files: list of paths from the Source Table below (wave 2/3 only, empty for wave 1)
- Plugin root path: `${CLAUDE_PLUGIN_ROOT}`
- Model: opus (synthesis and reasoning)
- MCP hints: none (concept creation uses Read + Write + Edit + Bash only, no MCP tools)

**Execution order:**
1. **Wave 1** — C1 + C2 + C5 (3 parallel)
2. Wait for Wave 1. **Wave 2** — C3 + C4 + C6 (3 parallel)
3. Wait for Wave 2. **Wave 3** — C7 + C8 + C9 (3 parallel)

**After each wave:**

1. Check that output files exist and have content:
```bash
for f in concept/C*-*.txt; do
  if [ ! -s "$f" ]; then
    echo "EMPTY OR MISSING: $f"
  fi
done
```
If any file is empty or missing, re-dispatch the failed section.

2. Report which sections completed and any failures.

### Step 5: Coherence check

Dispatch the `concept-reviewer` agent via `dispatch-subagent`:
- Agent: concept-reviewer
- Model: opus (analytical review)
- C-file paths: list of all concept TXT files (Glob `concept/C*-*.txt`)
- Formatting rules: read `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` and inline its full content
- Output: `D5-Review-Notes.md`

Present the review notes to the operator. If conflicts exist, they should be resolved before proceeding to proposal.

### Step 6: Build D5 digest

<critical>
**This step is purely mechanical.** Use ONLY bash commands (cat, echo, date). Do NOT use the Read tool on any C-file or D-file. Do NOT read output files into context. This is a simple concatenation.
</critical>

After coherence check, produce D5-Concept.txt with bash operations only:

```bash
DATE=$(date +%Y-%m-%d)
echo "Concept Overview — $DATE" > D5-Concept.txt
echo "" >> D5-Concept.txt
for f in concept/C*-*.txt; do
  BASENAME=$(basename "$f" .txt)
  echo "--- $BASENAME ---" >> D5-Concept.txt
  cat "$f" >> D5-Concept.txt
  echo "" >> D5-Concept.txt
done
```

Same pattern as D3-Research.txt consolidation. Purely mechanical cat.

### Step 7: Debug companion (when enabled)

If `debug` is `true` in project.json: write `tmp/debug/D5-Concept-debug.txt` — completed sections, line counts per section, review notes summary, any failures, no prose.

### Step 8: Update project-state.md

Update Phase 5 (Concept Creation) row:
- Status: `complete` (all sections processed) or `partial` (some skipped/failed)
- Output: `D5-Concept.txt`
- Updated: today's date

Display summary:

```
Concept Creation complete.

  Completed: {n}/9 sections
  Skipped: [list or "none"]
  Failed: [list or "none"]
  Phase 5 status: complete | partial
  Review notes: D5-Review-Notes.md

Next step: Review D5-Concept.txt and D5-Review-Notes.md, then run proposal.
```

## Pre-Read Table

Every section reads `baseline-log.txt` and `project.json` from the working directory root. Wave 2/3 sections also read their upstream C-files:

| Section | Wave | Upstream C-files |
|---|---|---|
| C1-Sitemap | 1 | -- |
| C2-Functional | 1 | -- |
| C5-Visual | 1 | -- |
| C3-Technical-Architecture | 2 | `concept/C2-Functional.txt` |
| C4-Content-Strategy | 2 | `concept/C1-Sitemap.txt` |
| C6-UX-Strategy | 2 | `concept/C1-Sitemap.txt` |
| C7-Project-Roadmap | 3 | `concept/C1-Sitemap.txt`, `concept/C2-Functional.txt`, `concept/C3-Technical-Architecture.txt` |
| C8-SEO-Strategy | 3 | `concept/C1-Sitemap.txt` |
| C9-Compliance | 3 | `concept/C2-Functional.txt` |

Prefix all paths with `{working_directory}/` for absolute paths when passing to dispatch.

**No R-files, no D-files.** baseline-log.txt by Phase 5 contains confirmed findings from phases 1-4 plus [C1]-[C9] entries as waves complete. This IS the shared context. If a baseline-log entry doesn't have enough detail for a specific recommendation, the agent flags the recommendation as INFERRED in its output — it does not read source files.

## Dependency Graph

```
Wave 1 (parallel):  C1-Sitemap    C2-Functional    C5-Visual
                     |    \             |    \
Wave 2 (parallel):  C4-Content  C6-UX  C3-Technical-Architecture
                                              |
Wave 3 (parallel):  C8-SEO    C9-Compliance   C7-Project-Roadmap
                                                    ^
                                               (C1, C2, C3)

Coherence:    concept-reviewer -> D5-Review-Notes.md
                     |
D5 Digest:    D5-Concept.txt (concatenation of 9 C-files)
```

## Rules

<critical>
- NEVER dispatch more than 3 concept-creator agents concurrently
- NEVER dispatch Wave 2 sections before their Wave 1 dependencies complete
- NEVER dispatch Wave 3 sections before their Wave 2 dependencies complete
- NEVER modify project-state.md beyond Phase 5 rows
- NEVER interpret or act on concept definition content — read only to inline into the dispatch prompt; the concept-creator agent executes the methodology
- NEVER start Phase 5 if D4 gap analysis is not resolved
- ALWAYS use dispatch-subagent skill for every concept-creator and concept-reviewer dispatch
- ALWAYS inline solution-framework.md and formatting-rules.md in every concept-creator dispatch
- ALWAYS run coherence check after all waves complete
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
- **concept-creator** — Produce one concept section as scannable TXT, update baseline-log (up to 9 instances, dispatched in 3 waves)
- **concept-reviewer** — Coherence check reading C-file TXTs directly, write D5-Review-Notes.md (1 instance)

## Reference files

Inlined in every concept-creator dispatch prompt (read by this skill, not by agents):
- `${CLAUDE_PLUGIN_ROOT}/references/solution-framework.md` — ICIP thinking sequence for solution agents
- `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` — Scannable TXT output conventions
- `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/*.md` — 9 section definition files (purpose, methodology)
- `${CLAUDE_PLUGIN_ROOT}/agents/references/concept-sections/templates/*.md` — 9 output guides (TXT structure)

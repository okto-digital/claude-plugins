---
name: project-init
description: "Initialize a new website discovery project, show pipeline status, or update phase state. Invoke when the user says 'initialize project', 'start new project', 'new client', 'project status', 'show pipeline', 'update phase status', or begins work on a new client website."
allowed-tools: Read, Write, Glob, AskUserQuestion
version: 2.0.0
---

# Project Init

## Step 1: Detect Mode

Check whether `project-state.md` exists in the current working directory.

- Not found → **Initialize Mode**
- Found + operator requested state update → **Update Mode**
- Found, no update request → **Status Mode**

---

## Initialize Mode

### 1. Gather Project Info

Collect all mandatory fields before proceeding. Optional fields use defaults if not provided.

| Field | Required | Default |
|---|---|---|
| Client name | Yes | -- |
| Project name | Yes | -- |
| URL (existing site, if any) | Yes | -- |
| Build type (`new` / `redesign`) | Yes | -- |
| Site type (`ecommerce`, `portfolio`, `corporate`, `portal`) | Yes | -- |
| Goal (one sentence) | Yes | -- |
| Languages (primary + additional) | Yes | -- |
| Output language (language for deliverables) | Yes | -- |
| Location (primary market + additional) | Yes | -- |
| Notes (free-form from client meeting) | No | empty |
| Research depth (`basic` / `deep`) | No | `basic` |
| Output format (`verbose` / `concise`) | No | `concise` |
| Gap domains (`ask` / `all` / `[list]`) | No | `ask` |
| Parallel execution (`ask` / `true` / `false`) | No | `ask` |
| Proposal style (`ask` / `full` / `summary_only`) | No | `ask` |
| Debug output (`ask` / `true` / `false`) | No | `ask` |

### 2. Configure Pipeline

After mandatory fields are collected, use AskUserQuestion: "Before I finalize, would you like to configure pipeline options (debug output, gap domains, parallel execution, proposal style)?"

- **"No, use defaults"** → skip to Step 3. All `ask` variables stay as `ask` (downstream skills prompt at runtime).
- **"Yes, let me configure"** → present each `ask`-type variable via AskUserQuestion:

| Variable | Options |
|---|---|
| Debug output | `true` (generate telegraphic debug companions) / `false` (skip) |
| Gap domains | `all` (21 domains) / `ask` (decide at Phase 4) / custom list |
| Parallel execution | `true` / `false` / `ask` (decide per phase) |
| Proposal style | `full` / `summary_only` / `ask` (decide at Phase 6) |

Skip any variable the operator already set explicitly in Step 1.

### 3. Process Notes

Structure raw notes into clean, discrete statements. Remove noise, preserve strategic signals. No notes = empty array.

### 4. Write project.json

Write as **a single line** — no newlines, no indentation, no spaces after colons or commas.

Schema and template: `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` § JSON Schema.

**research_config defaults:** `research_depth`: `basic`, `output_format`: `concise`, `serp_max_keywords`: 50, `search_landscape_max_keywords`: 100, `competitors_max`: 5. When `basic`: caps enforced. When `deep`: caps are guidelines. `output_format` affects Phase 3 research markdown length only (`concise`: ~1,800 chars, `verbose`: ~5,000 chars).

**pipeline_defaults:** `ask` = downstream skill prompts at runtime. Any other value = skip the question.

### 5. Write D1-Init.txt

The mission document. Free-form TXT — no template, no mandatory sections, you decide the structure. Use telegraphic style.

Read `${CLAUDE_PLUGIN_ROOT}/references/decision-framework.md` and `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`. Apply both:

1. **Start with the mission statement.** One sentence that frames the entire pipeline — why this project exists and what every finding downstream should serve.
2. **Then capture project facts from project.json.** Apply the four filters — only include what would change a downstream agent's output. Telegraphic. Self-contained lines. Notes from the operator often contain the anomalies worth capturing.

The agent decides what structure serves this project best. No prescribed sections.

### 6. Write baseline-log.txt

Create `baseline-log.txt`. This is the cumulative knowledge file — every downstream agent reads it before starting, appends after finishing.

**First line: the mission statement** from D1-Init.txt, inside a `--- MISSION ---` block.

**Then: INIT entries.** Apply the four filters from `${CLAUDE_PLUGIN_ROOT}/references/decision-framework.md` to decide what makes the cut. Tag with `[INIT]`. Telegraphic. Follow baseline-log rules from `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`.
**Rules:** Append-only. Downstream agents add to this file but never edit existing lines.


### 7. Create Directories and Settings

- Create subdirectories (skip existing): `research/`, `gap-analysis/`, `concept/`, `tmp/`
- If debug is `true`: also create `tmp/debug/`
- Add `tmp/` to `.gitignore` (create or append)
- Create `.claude/settings.json` if absent (merge if exists, don't overwrite):
  ```json
  {"env":{"ENABLE_TOOL_SEARCH":"auto:5"}}
  ```

### 8. Create project-state.md

Use template from `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` § Project State Template. Mark Phase 1 (INIT) as `complete` with today's date. All others start as `--`.

### 9. Confirm

Summarize what was created (project.json, D1-Init.txt, baseline-log.txt, project-state.md, directories). Suggest next step (client-intelligence). Stop.

---

## Status Mode

1. Read `project-state.md`. Parse pipeline + research substage rows.
2. For each row with Output not `--`, verify file exists (Glob). Flag missing as `[!!]`.
3. Display dashboard with status and flags.
4. Suggest next step:

| Condition | Suggestion |
|---|---|
| Phase 2 incomplete | Run client-intelligence |
| Phase 3 incomplete | Run research (next substage: {first incomplete}) |
| Phase 4 incomplete | Run domain-gap-analysis |
| Phase 5 incomplete | Run concept-creation |
| Phase 6 incomplete | Run proposal |
| All complete | Pipeline complete |

---

## Update Mode

1. Read `project-state.md`. Identify target phase/substage and status.
2. Validate transition is allowed. If not, warn and stop.
3. Update row (Status + Updated date). Confirm with next step suggestion.

---

## State Update Convention

Each downstream skill updates `project-state.md` after producing output:
1. Read → 2. Find matching row → 3. Set Status=`complete`, Output=path, Updated=date → 4. Write

---

## Critical Rules

- **NEVER** proceed without all mandatory fields.
- **NEVER** skip notes processing — empty notes = empty array in JSON.
- **ALWAYS** write project.json as a single line.
- **ALWAYS** generate D1-Init.txt applying the decision framework, not from a template.
- **ALWAYS** write baseline-log.txt with INIT entries before creating project-state.md.
- **ALWAYS** mark Phase 1 complete in project-state.md after initialize.
- **ALWAYS** run Step 2 (Configure Pipeline) — never silently default `ask` variables.

## Reference Files

- `${CLAUDE_PLUGIN_ROOT}/references/decision-framework.md` — thinking method (four filters, hypothesis, escalation)
- `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` — output formatting (source binding, confidence, scannable style, baseline-log rules)
- `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` — JSON schema, project-state template

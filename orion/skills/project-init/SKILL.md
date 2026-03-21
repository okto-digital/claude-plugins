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
- **"Yes, let me configure"** → present each `ask`-type variable via AskUserQuestion. Skip any the operator already set explicitly in Step 1.

### 3. Write project.json

Process raw notes into clean, discrete statements first. Remove noise, preserve strategic signals. No notes = empty array.

Write as **a single line** — no newlines, no indentation, no spaces after colons or commas.

Schema and template: `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` § JSON Schema.

**research_config defaults:** `research_depth`: `basic`, `output_format`: `concise`, `serp_max_keywords`: 50, `search_landscape_max_keywords`: 100, `competitors_max`: 5. When `basic`: caps enforced. When `deep`: caps are guidelines. `output_format` affects Phase 3 research markdown length only (`concise`: ~1,800 chars, `verbose`: ~5,000 chars).

**pipeline_defaults:** `ask` = downstream skill prompts at runtime. Any other value = skip the question.

### 4. Write D1-Init.txt and baseline-log.txt

Read `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`. Apply throughout.

**D1-Init.txt** — The mission document. Free-form TXT, telegraphic style, no template. You decide the structure.

1. **Start with the mission statement.** One sentence framing the entire pipeline — why this project exists and what every finding downstream should serve.
2. **Then capture project facts from project.json.** Only include what would change a downstream agent's output. Notes from the operator often contain the anomalies worth capturing.

**baseline-log.txt** — Cumulative knowledge file. Every downstream agent reads it before starting, appends after finishing. Append-only — downstream agents add but never edit existing lines.

1. **First line: the mission statement** (same as D1-Init.txt).
2. **Then: `[INIT]` entries.** Telegraphic. Follow baseline-log rules from formatting-rules.md.

### 5. Create Directories and Settings

- Create subdirectories (skip existing): `research/`, `gap-analysis/`, `concept/`, `tmp/`
- If debug is `true`: also create `tmp/debug/`
- Add `tmp/` to `.gitignore` (create or append)
- Create `.claude/settings.json` if absent (merge if exists, don't overwrite):
  ```json
  {"env":{"ENABLE_TOOL_SEARCH":"auto:5"}}
  ```

### 6. Create project-state.md

Use template from `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` § Project State Template. Mark Phase 1 (INIT) as `complete` with today's date. All others start as `--`.

### 7. Confirm

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

## Critical Rules

- **NEVER** proceed without all mandatory fields.
- **NEVER** skip notes processing — empty notes = empty array in JSON.
- **ALWAYS** write project.json as a single line.
- **ALWAYS** generate D1-Init.txt as free-form TXT, not from a template.
- **ALWAYS** write baseline-log.txt before creating project-state.md.
- **ALWAYS** mark Phase 1 complete in project-state.md after initialize.
- **ALWAYS** run Step 2 (Configure Pipeline) — never silently default `ask` variables.


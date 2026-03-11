---
name: project-init
description: "Initialize a new website discovery project, show pipeline status, or update phase state. Invoke when the user says 'initialize project', 'start new project', 'new client', 'project status', 'show pipeline', 'update phase status', or begins work on a new client website."
allowed-tools: Read, Write, Glob, AskUserQuestion
version: 1.0.0
---

# Project Init

Initialize a new project, display pipeline status, or update phase state. Mode is determined automatically.

## Step 1: Detect Mode

Check whether `project-state.md` exists in the current working directory.

- File does not exist: **Initialize Mode**.
- File exists AND operator requested a state update: **Update Mode**.
- File exists (no update request): **Status Mode**.

---

## Initialize Mode

### 1. Gather Project Info

Ask the operator for these fields. Do not proceed until all 7 mandatory fields are provided.

| Field | Required | Default |
|---|---|---|
| Client name | Yes | -- |
| Project name | Yes | -- |
| Build type (`new` / `redesign`) | Yes | -- |
| Site type (`ecommerce`, `portfolio`, `corporate`, `portal`) | Yes | -- |
| Goal (one sentence) | Yes | -- |
| Languages (primary + additional) | Yes | -- |
| Location (primary market + additional) | Yes | -- |
| Notes (free-form from client meeting) | No | empty |
| Research depth (`basic` / `deep`) | No | `basic` |
| Output format (`verbose` / `concise`) | No | `concise` |

### 2. Process Notes

Parse the operator's raw notes (any language, format, or shorthand):

1. Structure into a clean list of discrete, meaningful statements.
2. Remove noise (phone numbers, irrelevant fragments) while preserving strategic signals.
3. Flag notes that represent requirements, constraints, or action items for downstream phases.
4. If no notes provided, produce an empty array.

### 3. Write D1-Init.json

Write `D1-Init.json` to the project root as **minified JSON** (no whitespace, no indentation).

Use the schema and example from `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` § JSON Schema.

**research_config defaults:**
- `research_depth`: `basic`, `output_format`: `concise`
- `serp_max_keywords`: 50, `search_landscape_max_keywords`: 100, `competitors_max`: 5
- When `basic`: numeric caps are enforced. When `deep`: caps are guidelines only.
- Operator can adjust before any phase begins.

### 4. Write D1-Init.md

Generate `D1-Init.md` from `D1-Init.json` using the markdown template in `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` § Markdown Template.

This file is a disposable human-review view. The JSON is always the source of truth.

### 5. Create Directories

Create these subdirectories in the current working directory (skip any that already exist):

- `research/`
- `gap-analysis/`
- `concept/`

### 6. Create project-state.md

Write `project-state.md` using the template in `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` § Project State Template.

Mark Phase 1 (INIT) as `complete` with output `D1-Init.json` and today's date. All other phases start as `--`.

### 7. Confirm

Display:

```
Project initialized.

  Client: {client name}
  Project: {project name}
  Type: {build_type} | {site_type}
  Language: {primary} | Market: {primary market}
  Research: {depth} | Output: {format}
  Notes: {count} structured notes
  State: project-state.md
  Output: D1-Init.json, D1-Init.md

Next step: Run client-intelligence to produce Phase 2 output.
```

Stop here.

---

## Status Mode

### 1. Load State

Read `project-state.md`. Parse:
- Project info from the header
- Pipeline table rows (Phase, Name, Status, Output, Updated)
- Research substage rows (Sub, Name, Status, Output, Updated)

### 2. Cross-Check Files

For each row where Output is not `--`, verify the file exists on disk using Glob. If listed but missing, flag as `[!!]`.

### 3. Display Dashboard

```
[INIT] Project: {name} ({build_type} | {site_type})
Language: {primary} | Market: {primary market}
Research: {depth} | Output: {format}

PIPELINE
  1  INIT                  [{status}]
  2  Client Intelligence   [{status}]
  3  Research              [{status}]
  4  Domain Gap Analysis   [{status}]
  5  Concept Creation      [{status}]
  6  Proposal & Brief      [{status}]

RESEARCH SUBSTAGES
  3.1  R1-SERP          SERP & Search Landscape    [{status}]
  3.2  R2-Keywords       Keyword Opportunity        [{status}]
  3.3  R3-Competitors    Competitor Landscape       [{status}]
  3.4  R4-Market         Industry & Market Context  [{status}]
  3.5  R5-Technology     Technology & Performance   [{status}]
  3.6  R6-Reputation     Reputation & Social Proof  [{status}]
  3.7  R7-Audience       Audience & Personas        [{status}]
  3.8  R8-UX             UX/UI Patterns             [{status}]
  3.9  R9-Content        Content Landscape          [{status}]

Progress: {n}/6 phases complete | {m}/9 substages complete

Next step: {suggestion}
```

Status markers: `[--]` not started, `[OK]` complete, `[IP]` in progress, `[!!]` file missing.

### 4. Determine Next Step

| Condition | Suggestion |
|---|---|
| Phase 2 not complete | "Run client-intelligence to produce Phase 2 output." |
| Phase 2 complete, Phase 3 not complete | "Run research. Next substage: {first incomplete}." |
| Phase 3 complete, Phase 4 not complete | "Run domain-gap-analysis." |
| Phase 4 complete, Phase 5 not complete | "Run concept-creation." |
| Phase 5 complete, Phase 6 not complete | "Run proposal." |
| All complete | "Pipeline complete." |

---

## Update Mode

### 1. Parse Request

Read `project-state.md`. Identify which phase or substage and target status the operator wants to set.

### 2. Validate

Check the current status allows the transition. If not, warn and stop.

### 3. Update and Confirm

Update the row in `project-state.md` (Status + Updated date). Display confirmation with the next step suggestion.

---

## State Update Convention

Each downstream skill updates `project-state.md` after producing its output:

1. Read `project-state.md`
2. Find the row matching the phase or substage just completed
3. Update: Status → `complete`, Output → relative path, Updated → `YYYY-MM-DD`
4. Write `project-state.md`

---

## Critical Rules

- **NEVER** proceed without all 7 mandatory fields.
- **NEVER** skip notes processing -- even empty notes produce an empty array in D1-Init.json.
- **ALWAYS** write D1-Init.json as minified JSON (no whitespace).
- **ALWAYS** generate D1-Init.md from D1-Init.json, not independently.
- **ALWAYS** mark Phase 1 as complete in project-state.md after initialize.

## Reference Files

- `${CLAUDE_PLUGIN_ROOT}/skills/project-init/references/templates.md` — JSON schema, markdown template, project-state template, example

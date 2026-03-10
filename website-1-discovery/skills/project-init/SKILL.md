---
name: project-init
description: "Initialize a new website project, show pipeline status, or update document state. Invoke when the user says 'initialize project', 'start new project', 'project status', 'what documents are done', 'mark D1 interview complete', 'update D1 status', or begins work on a new client website."
allowed-tools: Read, Write, Glob, Bash
version: 1.0.0
---

# Project Init

Initialize a new project or display pipeline status. Mode is determined automatically.

---

## Step 1: Detect Mode

Check whether `project-state.md` exists in the current working directory.

- File does not exist: go to **Initialize Mode**.
- File exists AND operator requested a state update (e.g., "mark D1 interview complete"): go to **Update Mode**.
- File exists (no update request): go to **Status Mode**.

---

## Initialize Mode

### 1. Gather Project Info

Ask the operator for:

1. **Client name** (required) -- the name of the client or project
2. **Client website URL** (optional) -- used later by client-intake
3. **Project type** (required) -- one of: `new-build`, `redesign`, `landing-page`, `ecommerce`
4. **Primary language** (required) -- the main language of the website and its target audience (e.g., "Slovak", "German", "English"). Default suggestion: detect from URL TLD if provided (.sk → Slovak, .de → German, .nl → Dutch), otherwise ask.
5. **Primary market** (required) -- the geographic market the website targets (e.g., "Slovakia", "DACH region", "US").
6. **Secondary languages** (optional) -- other languages relevant to the project. Ask: "Are there other languages that matter? For example, if targeting Slovakia, Czech or English might be relevant for research." Record as comma-separated list, or "none".

Do not proceed until client name, project type, primary language, and primary market are provided.

### 2. Create Directory Structure

Create these subdirectories in the current working directory (skip any that already exist):

- `intake/`
- `research/`

### 3. Create Project State

Write `project-state.md` in the current working directory using this template. Replace placeholders with values from step 1.

```markdown
# Project: {Client Name}

**Client:** {Client Name}
**URL:** {URL or "not provided"}
**Type:** {project type}
**Created:** {YYYY-MM-DD}

## Language Configuration

**Primary language:** {language}
**Primary market:** {market}
**Secondary languages:** {comma-separated list or "none"}

## Pipeline

| Doc | Name | Status | File | Updated |
|---|---|---|---|---|
| D1 | Client Intake | -- | -- | -- |
| D2 | Project Research | -- | -- | -- |
| D3 | Project Brief | -- | -- | -- |
```

### 4. Confirm

Display:

```
Project initialized.

  Client: {name}
  Type: {type}
  Language: {primary language} | Market: {primary market}
  Secondary: {secondary languages or "none"}
  State: project-state.md
  Directories: intake/, research/

Next step: Run client-intake to produce D1.
```

Stop here.

---

## Status Mode

### 1. Load State

Read `project-state.md`. Parse:
- Project info (Client, URL, Type) from the header
- Pipeline table rows (Doc, Name, Status, File, Updated)

### 2. Cross-Check Files

For each pipeline row where File is not `--`, verify the file exists on disk using Glob. If a file is listed but missing, flag it as `[!!]` (stale reference).

### 3. Display Dashboard

```
[INIT] Project: {name} ({type})
Language: {primary language} | Market: {primary market}
Secondary: {secondary languages or "none"}

PIPELINE STATUS
  D1 Client Intake       [{status}]
  D2 Project Research    [{status}]
  D3 Project Brief       [{status}]

Progress: {n}/3 complete

Next step: {suggestion}
```

Status markers:
- `[--]` not started
- `[OK]` complete
- `[!!]` file missing (stale state -- warn operator)

### 4. Determine Next Step

Apply this logic in order:

| Condition | Suggestion |
|---|---|
| D1 not complete | "Run client-intake to produce D1." |
| D1 research-complete | "Interview the client and fill answers into D1. Then run project-research to produce D2." |
| D1 interview-complete, D2 not complete | "Run project-research to produce D2." |
| D2 complete, D3 not complete | "Run project-brief to produce D3." |
| All complete | "Pipeline complete." |

---

## Update Mode

For manual state transitions that no downstream skill handles automatically.

### 1. Parse Request

Read `project-state.md`. Identify which document and target status the operator wants to set.

Currently supported:

| Request | Action |
|---|---|
| "mark D1 interview complete" | Set D1 status from `research-complete` to `interview-complete` |

If the request does not match a supported transition, inform the operator and stop.

### 2. Validate

Check that the current status allows the transition. D1 must be `research-complete` before it can become `interview-complete`. If the precondition is not met, warn the operator and stop.

### 3. Update and Confirm

Update the pipeline row in `project-state.md` (status + updated date). Display: "D1 status updated to interview-complete. Next step: Run project-research to produce D2."

---

## State Update Convention

Each downstream skill updates `project-state.md` directly after producing its document:

1. Read `project-state.md`
2. Find the pipeline row matching the document just produced
3. Update the row: Status → `complete`, File → relative path to output, Updated → `YYYY-MM-DD`
4. Write `project-state.md`

Manual transitions (e.g., D1 `research-complete` → `interview-complete`) use this skill's Update Mode.

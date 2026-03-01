---
name: project-init
description: "Initialize a new website project or show current pipeline status. Creates project directory structure and state file. Invoke when the user says 'initialize project', 'start new project', 'project status', 'what documents are done', or begins work on a new client website."
allowed-tools: Read, Write, Glob, Bash
version: 1.0.0
---

# Project Init

Initialize a new project or display pipeline status. Mode is determined automatically.

---

## Step 1: Detect Mode

Check whether `project-state.md` exists in the current working directory.

- File exists: go to **Status Mode**.
- File does not exist: go to **Initialize Mode**.

---

## Initialize Mode

### 1. Gather Project Info

Ask the operator for:

1. **Client name** (required) -- the name of the client or project
2. **Client website URL** (optional) -- used later by client-intake
3. **Project type** (required) -- one of: `new-build`, `redesign`, `landing-page`, `ecommerce`

Do not proceed until client name and project type are provided.

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

## Pipeline

| Doc | Name | Status | File | Updated |
|---|---|---|---|---|
| D1 | Client Intake | -- | -- | -- |
| D2 | Client Interview | -- | -- | -- |
| D3 | Project Research | -- | -- | -- |
| D4 | Project Brief | -- | -- | -- |
```

### 4. Confirm

Display:

```
Project initialized.

  Client: {name}
  Type: {type}
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

PIPELINE STATUS
  D1 Client Intake       [{status}]
  D2 Client Interview    [{status}]
  D3 Project Research    [{status}]
  D4 Project Brief       [{status}]

Progress: {n}/4 complete

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
| D1 complete, D2 not complete | "Run intake-interview to produce D2." |
| D2 complete, D3 not complete | "Run research to produce D3." |
| D3 complete, D4 not complete | "Run brief-writer to produce D4." |
| All complete | "Pipeline complete." |

---

## State Update Convention

This skill does NOT include a state update mode. Each downstream skill updates `project-state.md` directly after producing its document.

**Pattern for downstream skills:**

1. Read `project-state.md`
2. Find the pipeline row matching the document just produced
3. Update the row: Status → `complete`, File → relative path to output, Updated → `YYYY-MM-DD`
4. Write `project-state.md`

This keeps state maintenance distributed -- each skill owns its own row update.

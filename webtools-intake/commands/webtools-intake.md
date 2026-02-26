---
description: "webtools-intake: Show available intake workflows and current project state"
allowed-tools: Read, Glob
---

Show available webtools-intake commands, current project state, and suggested next step.

---

## Read Project State

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: skip to the "No Project" output below.
- If it DOES exist: parse the Project Info (client name, project type) and the Document Log (D11 and D1 statuses).

### 2. Session State Check

Check if `brief/intake-session.md` exists.

- If yes: read it and extract `current_phase`, `phases_completed`, `critical_coverage`, `total_data_points`, and `last_updated`.
- If no: session state is empty (no phases started).

### 3. Document Status Check

Determine the status of key documents:
- **D11 Questionnaire:** check if `brief/D11-client-questionnaire.md` exists. If yes, report its status from the registry. If no, report "not started".
- **D1 Brief:** check if `brief/D1-project-brief.md` exists. If yes, report its status from the registry. If no, report "not started".

---

## Display Overview

### With Active Project

```
[INTAKE] Webtools Intake -- [client name]

Available commands:
  /webtools-intake                  Show this overview
  /webtools-intake-questionnaire    Generate client intake questionnaire (D11)
  /webtools-intake-prep             Analyze pre-existing data, produce interview guide
  /webtools-intake-meeting          Live meeting companion (submarine mode)
  /webtools-intake-review           Post-meeting gap analysis and inference review
  /webtools-intake-brief            Generate D1: Project Brief

Current state:
  Project: [client name] ([project type])
  D11 Questionnaire: [complete / not started]
  Intake session: [phase info from intake-session.md, e.g. "PREP completed, MEETING not started"]
  D1 Brief: [complete / not started]
  CRITICAL coverage: [X/Y] ([Z]%)
  Data points: [count]

Suggested next step: /webtools-intake-[phase]
```

**Next step logic:**
- No intake-session.md and no D11 -> suggest `/webtools-intake-questionnaire` or `/webtools-intake-prep`
- D11 complete but no session -> suggest `/webtools-intake-prep`
- PREP completed -> suggest `/webtools-intake-meeting`
- MEETING completed -> suggest `/webtools-intake-review`
- REVIEW completed -> suggest `/webtools-intake-brief`
- D1 complete -> report "Intake complete. D1 is ready for downstream tools."

### No Project

If `project-registry.md` does not exist:

```
[INTAKE] Webtools Intake

No project found in this directory.

Run /webtools-init to set up a new project first, then return here.

Available commands (after project setup):
  /webtools-intake                  Show this overview
  /webtools-intake-questionnaire    Generate client intake questionnaire (D11)
  /webtools-intake-prep             Analyze pre-existing data, produce interview guide
  /webtools-intake-meeting          Live meeting companion (submarine mode)
  /webtools-intake-review           Post-meeting gap analysis and inference review
  /webtools-intake-brief            Generate D1: Project Brief
```

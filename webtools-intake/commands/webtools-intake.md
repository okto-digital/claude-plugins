---
description: "webtools-intake: Show available intake workflows and current project state"
allowed-tools: Read, Glob
---

Show available webtools-intake commands and skills, current project state, and suggested next step.

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
- **D14 Client Research Profile:**
  - Check if `brief/D14-client-research-profile.md` exists (compressed version).
  - Check if `brief/D14-client-research-profile.raw.md` exists (raw version).
  - Report: "complete (compressed)" if .md exists, "complete (raw only)" if only .raw.md exists, "not started" if neither exists.
- **D11 Questionnaire:** check if `brief/D11-client-questionnaire.md` exists. If yes, report its status from the registry. If no, report "not started".
- **D1 Brief:**
  - Check if `brief/D1-project-brief.md` exists (compressed version).
  - Check if `brief/D1-project-brief.raw.md` exists (raw version).
  - Report: "complete (compressed)" if .md exists, "complete (raw only)" if only .raw.md exists, "not started" if neither exists.

---

## Display Overview

### With Active Project

```
[INTAKE] Webtools Intake -- [client name]

Available skills:
  webtools-intake:client-researcher  Research client company, produce D14 intelligence profile

Available commands:
  /webtools-intake                  Show this overview
  /webtools-intake-prep             Research client + produce interview guide (auto-researches if no D14)
  /webtools-intake-questionnaire    Generate client intake questionnaire (D11)
  /webtools-intake-meeting          Live meeting companion (submarine mode)
  /webtools-intake-review           Post-meeting gap analysis and inference review
  /webtools-intake-brief            Generate D1: Project Brief

Current state:
  Project: [client name] ([project type])
  D14 Client Research: [complete (compressed) / complete (raw only) / not started]
  D11 Questionnaire: [complete / not started]
  Intake session: [phase info from intake-session.md, e.g. "PREP completed, MEETING not started"]
  D1 Brief: [complete (compressed) / complete (raw only) / not started]
  CRITICAL coverage: [X/Y] ([Z]%)
  Data points: [count]

Suggested next step: /webtools-intake-[command]
```

**Next step logic:**
- No D14 and no D11 and no intake-session.md -> suggest `/webtools-intake-prep [url]` as primary starting point ("Research the client and prepare for the meeting")
- D14 complete but no intake-session.md and no D11 -> suggest `/webtools-intake-prep` or `/webtools-intake-questionnaire`
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

Available skills:
  webtools-intake:client-researcher  Research client company, produce D14 intelligence profile

Available commands (after project setup):
  /webtools-intake                  Show this overview
  /webtools-intake-prep             Research client + produce interview guide (auto-researches if no D14)
  /webtools-intake-questionnaire    Generate client intake questionnaire (D11)
  /webtools-intake-meeting          Live meeting companion (submarine mode)
  /webtools-intake-review           Post-meeting gap analysis and inference review
  /webtools-intake-brief            Generate D1: Project Brief
```

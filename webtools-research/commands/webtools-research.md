---
description: "webtools-research: Show available research topics, commands, and current project state"
allowed-tools: Read, Glob
---

Show available webtools-research commands, current research status, and suggested next step.

---

## Read Project State

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: skip to the "No Project" output below.
- If it DOES exist: parse the Project Info (client name, project type) and the Document Log.

### 2. Research Directory Check

Check if `research/` directory exists using Glob for `research/*.md`.

### 3. R-Document Status

Check existence of each research document:
- `research/R1-serp-landscape.md`
- `research/R2-competitor-landscape.md`
- `research/R3-audience-personas.md`
- `research/R4-ux-benchmarks.md`
- `research/R5-content-strategy.md`
- `research/R6-reputation-social-proof.md`
- `research/R7-tech-performance.md`
- `research/R8-market-context.md`
- `research/D15-research-report.md`

For each file: report "complete" if it exists, "not started" if it does not.

### 4. Prerequisite Check

Check existence of prerequisite documents:
- `brief/D1-project-brief.md` -- required for research
- `brief/D14-client-research-profile.md` -- recommended but not required

---

## Display Overview

### With Active Project

```
[RESEARCH] Webtools Research -- [client name]

Research Topics:
  R1  SERP & Search Landscape        [complete / not started]
  R2  Competitor Landscape            [complete / not started]
  R3  Audience & User Personas        [complete / not started]
  R4  UX/UI Patterns & Benchmarks     [complete / not started]
  R5  Content Landscape & Strategy    [complete / not started]
  R6  Reputation & Social Proof       [complete / not started]
  R7  Technology & Performance        [complete / not started]
  R8  Industry & Market Context       [complete / not started]
  D15 Research Report (consolidated)  [complete / not started]

Available commands:
  /webtools-research                  Show this overview
  /webtools-research-run              Select topics and run research (parallel)
  /webtools-research-serp             Run R1 only
  /webtools-research-competitors      Run R2 only
  /webtools-research-audience         Run R3 only
  /webtools-research-ux               Run R4 only
  /webtools-research-content          Run R5 only
  /webtools-research-reputation       Run R6 only
  /webtools-research-tech             Run R7 only
  /webtools-research-market           Run R8 only
  /webtools-research-consolidate      Merge R-docs into D15

Prerequisites:
  D1 Project Brief:          [complete / not found]
  D14 Client Research:       [complete / not found]

Suggested next step: [see logic below]
```

**Next step logic:**

- No D1 -> "Run /webtools-intake first to produce D1 Project Brief."
- D1 exists, no R-documents started -> "Run /webtools-research-run to select topics and start research."
- Some R-documents complete, others not started -> "Continue with /webtools-research-run or run individual topic commands."
- All R-documents complete (at least one exists), no D15 -> "Run /webtools-research-consolidate to produce D15."
- D15 complete -> "Research phase complete. D15 is ready for proposal writing and production deep-dives."

### No Project

If `project-registry.md` does not exist:

```
[RESEARCH] Webtools Research

No project found in this directory.

Run /webtools-init to set up a new project first, then return here.

Available commands (after project setup):
  /webtools-research                  Show this overview
  /webtools-research-run              Select topics and run research (parallel)
  /webtools-research-serp             Run R1 only
  /webtools-research-competitors      Run R2 only
  /webtools-research-audience         Run R3 only
  /webtools-research-ux               Run R4 only
  /webtools-research-content          Run R5 only
  /webtools-research-reputation       Run R6 only
  /webtools-research-tech             Run R7 only
  /webtools-research-market           Run R8 only
  /webtools-research-consolidate      Merge R-docs into D15
```

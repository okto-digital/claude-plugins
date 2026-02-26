---
description: "webtools-intake: Generate D1: Project Brief from all accumulated intake data (BRIEF mode)"
allowed-tools: Read, Write, Glob, Bash(mkdir:*)
---

Enter the brief-generator agent in **BRIEF mode**. Compile all accumulated data from PREP, MEETING, and REVIEW into D1: Project Brief. Check prerequisites, draft section-by-section with confidence tags, and iterate until approved.

**You are now the brief-generator agent in BRIEF mode.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/brief-generator.md

---

## Phase Entry Instructions

After completing the Lifecycle Startup from the agent definition above (including step 3b Session State), enter **BRIEF mode** explicitly.

1. If session state was loaded from `brief/intake-session.md`:
   - Report accumulated data: phases completed, CRITICAL coverage, total data points, confirmed inferences, remaining gaps, flags.
   - If D1 already exists (detected during Output Preparation), follow the agent definition's existing-D1 options (Overwrite / Revise / Cancel).

2. **Prerequisites check.** Before drafting, verify:
   - All CRITICAL gaps are resolved (covered, inferred HIGH, or operator-approved "[To be provided]")
   - Inferences from REVIEW have been confirmed

   If prerequisites are NOT met, warn the operator:

```
[BRIEF] Prerequisites warning:

Unresolved CRITICALs: [count]
Unconfirmed inferences: [count]

Options:
(a) Proceed anyway -- gaps marked "[To be provided]" in the brief
(b) Return to review -- run /webtools-intake-review to address gaps
(c) Provide answers now -- I will ask the remaining questions
```

3. If prerequisites are met (or operator chose to proceed), announce BRIEF mode:

```
[BRIEF] Generating D1: Project Brief

Data sources:
  PREP data: [count] data points
  MEETING data: [count] data points
  Confirmed inferences: [count]
  Flags to address: [count]

Drafting section by section...
```

4. Follow the BRIEF Mode rules in the agent definition: present each section with confidence tags (Solid / Thin / Assumed / Missing), iterate until the operator explicitly approves.

5. After approval, execute the Lifecycle Completion from the agent definition:
   - Write D1 to `brief/D1-project-brief.md`
   - Update `project-registry.md`
   - Show downstream notification

6. Write final session state to `brief/intake-session.md` as described in the agent definition's Session State Write section.

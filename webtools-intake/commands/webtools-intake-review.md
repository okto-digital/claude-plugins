---
description: "webtools-intake: Post-meeting gap analysis, inference review, and D13 generation (REVIEW mode)"
allowed-tools: Read, Write, Glob, Bash(mkdir:*)
---

Enter the brief-generator agent in **REVIEW mode**. Conduct a 3-part post-meeting review: Meeting Summary, Inference Confirmation, and Gap Report. Optionally generate D13: Client Follow-Up Questionnaire.

**You are now the brief-generator agent in REVIEW mode.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/brief-generator.md

---

## Phase Entry Instructions

After completing the Lifecycle Startup from the agent definition above (including step 3b Session State), enter **REVIEW mode** explicitly.

1. If session state was loaded from `brief/intake-session.md`:
   - Report what was carried forward (data points, coverage, conditional domains, inferences, flags).
   - If REVIEW was already completed, inform the operator and offer options:
     - (a) Re-run REVIEW with additional data or corrections
     - (b) Skip to the next uncompleted phase (suggest `/webtools-intake-brief`)

2. If no MEETING data exists in session state (operator skipped directly to REVIEW):
   - Warn that no meeting data was found.
   - Offer to proceed anyway if the operator has notes to paste, or suggest running `/webtools-intake-meeting` first.

3. Announce REVIEW mode entry and begin the 3-part review sequence:

```
[REVIEW] Starting post-meeting review.

Part 1 of 3: Meeting Summary
```

4. Present the three sections **one at a time** as defined in the agent definition's REVIEW Mode:
   - **Section 1: Meeting Summary** -- topics covered, key decisions, data points captured
   - **Section 2: Inference Confirmation** -- HIGH/MEDIUM/LOW inferences grouped for batch Y/N/correction
   - **Section 3: Gap Report** -- remaining CRITICAL and IMPORTANT items with resolution options

5. If the operator chooses to generate D13, follow the D13 Generation rules in the agent definition. Write to `brief/D13-client-followup.md`.

6. When REVIEW is complete, write session state to `brief/intake-session.md` as described in the agent definition's Session State Write section.

7. Suggest next step:

```
[REVIEW] Review complete. When ready to generate the brief, run:
  /webtools-intake-brief
```

---
description: "webtools-intake: Analyze pre-existing client data and produce interview guide (PREP mode)"
allowed-tools: Read, Write, Glob, Bash(mkdir:*)
---

Enter the brief-generator agent in **PREP mode**. Analyze pre-existing client data, score against domain checkpoints, run inference engine, and produce a PREP Report with an interview guide for the upcoming meeting.

**You are now the brief-generator agent in PREP mode.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/brief-generator.md

---

## Phase Entry Instructions

After completing the Lifecycle Startup from the agent definition above (including step 3b Session State), enter **PREP mode** explicitly.

1. If session state was loaded from `brief/intake-session.md` and PREP was already completed, inform the operator and offer options:
   - (a) Re-run PREP with new/additional data
   - (b) Skip to the next uncompleted phase (suggest the appropriate `/webtools-intake-*` command)

2. If no prior state exists or PREP was not yet completed, announce PREP mode entry:

```
[PREP] Ready for pre-meeting analysis.

Share any client data you have:
- Inquiry form answers
- D11 questionnaire responses
- Meeting prep notes, emails, URLs
- Any format works

I will score it against all domain checkpoints and produce an interview guide.
```

3. Process all input following the PREP Mode rules in the agent definition.

4. When PREP is complete (PREP Report delivered), write session state to `brief/intake-session.md` as described in the agent definition's Session State Write section.

5. Suggest next step:

```
PREP complete. When the client arrives, run:
  /webtools-intake-meeting
```

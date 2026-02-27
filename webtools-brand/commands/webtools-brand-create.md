---
description: "webtools-brand: Interactive brand voice creation from scratch (Generate mode)"
allowed-tools: Read, Write, Bash(mkdir:*), WebFetch
---

Enter the brand-voice-creator agent in **Generate mode**. Co-create a new brand voice through archetype identification, dimension-by-dimension exploration, and iterative sample content generation.

**You are now the brand-voice-creator.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/brand-voice-creator.md

---

## Mode Entry Instructions

After completing the Lifecycle Startup from the agent definition above, enter **Generate mode** explicitly. Skip mode detection -- the operator chose this mode.

1. If D2 already exists (detected during Output Preparation), present the Overwrite/Revise/Cancel options from the agent's Output Preparation step.

2. Announce Generate mode entry:

```
[BRAND] Generate Mode -- [client name]

Creating brand voice from scratch through interactive exploration.

D1 Project Brief: [loaded / not found]
Output: brand/D2-brand-voice-profile.md [new / overwrite / revise]

Starting archetype identification...
```

3. Proceed directly to Generate Mode Step 1 (Identify Brand Archetypes) in the agent definition. Follow all Generate mode steps through completion, then execute Lifecycle Completion.

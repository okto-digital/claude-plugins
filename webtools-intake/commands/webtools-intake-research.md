---
description: "webtools-intake: Research client and prepare interview guide (RESEARCH+PREP)"
allowed-tools: Read, Write, Glob, Bash(mkdir:*), WebSearch, Task
argument-hint: [client-url]
---

Research a client company and auto-enter PREP mode. This command combines client research (D14) and meeting preparation into one unified flow: web search for external intelligence, website crawl via web-crawler agent, business registry lookup, D14 generation with compression, then automatic transition to PREP mode for interview guide production.

**You are now running a unified RESEARCH+PREP workflow.** Load and follow the skill definition and agent definition below.

---

## Skill Definition (Research Phase)

@skills/client-researcher/SKILL.md

---

## Agent Definition (PREP Phase)

@agents/brief-generator.md

---

## Phase Entry Instructions

### Research Phase

1. **Lifecycle Startup** -- Complete the Lifecycle Startup from the client-researcher skill definition above:
   - Registry check
   - Directory validation (ensure `brief/` exists)
   - Status report

2. **URL intake** -- Ask the operator for the client website URL (required). Accept optional context about what to look for. If a URL was passed as an argument, use it directly.

3. **Execute research** -- Follow all steps in the client-researcher skill:
   - Step 2: Web search for external intelligence
   - Step 3: Website crawl via web-crawler agent (homepage discovery, page selection, parallel crawl)
   - Step 4: Business registry lookup
   - Step 5: Synthesis into D14 report
   - Step 6: Save to `brief/D14-client-research-profile.raw.md` and compress to `brief/D14-client-research-profile.md`

4. **Registry update** -- Update project-registry.md with D14 status (as described in the skill).

### Automatic PREP Transition

After D14 is produced and saved, automatically transition to PREP mode:

```
[RESEARCH] D14: Client Research Profile complete.

Sources: [web search findings count] external findings, [pages count] pages analyzed, registry: [status]
Output: brief/D14-client-research-profile.md (compressed)

Transitioning to PREP mode to produce interview guide...
```

5. **PREP Lifecycle Startup** -- Complete the brief-generator Lifecycle Startup:
   - Registry check (already done, reuse)
   - Directory validation: verify 8 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`, `research/`. Create any missing ones silently.
   - Reference loading: load all domain files, topic-mapping.md, inference-rules.md, d13-template.md, questioning-strategy.md
   - Session state: check for existing `brief/intake-session.md`
   - Input validation: load the just-produced D14 (compressed version at `brief/D14-client-research-profile.md`). Also load D11 if present.

6. **Enter PREP mode** -- Score D14 intelligence against every checkpoint in every applicable domain:
   - Mark checkpoints as EXPLICIT, PARTIAL, MISSING, or N/A
   - Run inference engine against MISSING and PARTIAL checkpoints
   - Determine conditional domain applicability (ask operator if ambiguous)
   - Produce the PREP Report with interview guide

7. **Write session state** to `brief/intake-session.md` with: project name, `current_phase: PREP`, `phases_completed: [RESEARCH, PREP]`, conditional domain statuses, CRITICAL coverage count, total data points, key facts, inferences, and flags.

8. **Suggest next step:**

```
RESEARCH+PREP complete. When the client arrives, run:
  /webtools-intake-meeting

Or generate a questionnaire first:
  /webtools-intake-questionnaire
```

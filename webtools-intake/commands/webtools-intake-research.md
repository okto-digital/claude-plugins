---
description: "webtools-intake: Research client and prepare interview guide (RESEARCH+PREP)"
allowed-tools: Read, Write, Glob, Bash(mkdir:*), WebSearch, Task
argument-hint: [client-url]
---

Research a client company and auto-enter PREP mode. This command combines client research (D14) and meeting preparation into one unified flow: web search for external intelligence, website crawl via web-crawler agent, business registry lookup, D14 generation with compression, then automatic transition to lightweight PREP for interview guide production.

**You are now running a unified RESEARCH+PREP workflow.** Load and follow the skill definition below for the Research phase, then run PREP analysis using the topic mapping.

---

## Skill Definition (Research Phase)

@skills/client-researcher/SKILL.md

---

## Topic Reference (PREP Phase)

@references/topic-mapping.md

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

After D14 is produced and saved, automatically transition to PREP:

```
[RESEARCH] D14: Client Research Profile complete.

Sources: [web search findings count] external findings, [pages count] pages analyzed, registry: [status]
Output: brief/D14-client-research-profile.md (compressed)

Transitioning to PREP to produce interview guide...
```

5. **Directory validation** -- Verify 8 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`, `research/`. Create any missing ones silently.

6. **Load available data** -- Load the just-produced D14 (compressed version at `brief/D14-client-research-profile.md`). Also load D11 if present at `brief/D11-client-questionnaire.md`.

7. **Analyze findings by topic** -- Using the topic reference above, organize all D14 and D11 findings into the 9 conversation topics:
   - For each topic, identify strong findings, partial findings, and gaps
   - Determine conditional domain applicability from the 6 extensions in the topic mapping
   - Include without asking when data clearly indicates applicability
   - Exclude without asking when data clearly indicates non-applicability
   - Ask the operator only when ambiguous

8. **Produce PREP Report:**

```
[PREP] PREP REPORT: [Client Name]

DATA LOADED
  Sources: [D14 / D11 -- list what was found]
  Key findings: [count of distinct data points extracted]

WHAT WE KNOW WELL
  [Topic]: [brief summary of strong findings]
  ...

GAPS AND OPEN QUESTIONS
  [Topic]: [what's missing or unclear, specific questions to ask]
  ...

CONDITIONAL DOMAINS
  Active: [list with evidence]
  Inactive: [list with evidence]
  Unknown -- ask early in meeting: [list]

INTERVIEW GUIDE
  Recommended conversation flow:
  1. [Topic] -- [reason to discuss, key questions to ask] (~[X] min)
  2. [Topic] -- [reason to discuss, key questions to ask] (~[X] min)
  ...

Ready for the meeting. Run: /webtools-intake-meeting
```

9. **Write session state** to `brief/intake-session.md`:
   - Set `current_phase: PREP`
   - Set `phases_completed: [RESEARCH, PREP]`
   - Record conditional domain statuses (active, inactive, unknown)
   - Record key facts extracted from data
   - Record topic gap summary (which topics have gaps, which are well covered)
   - Record data sources loaded
   - Set `last_updated` to today

10. **Suggest next step:**

```
RESEARCH+PREP complete. When the client arrives, run:
  /webtools-intake-meeting

Or generate a questionnaire first:
  /webtools-intake-questionnaire
```

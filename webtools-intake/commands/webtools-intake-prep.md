---
description: "webtools-intake: Research client and prepare interview guide (PREP mode)"
allowed-tools: Read, Write, Glob, Bash(mkdir:*), WebSearch, Task
argument-hint: [client-url]
---

Prepare for a client meeting. If D14 exists, analyze it and produce an interview guide. If D14 does not exist, run client research first (via sub-agent), then produce the interview guide. Accepts a URL argument for direct research, or manual data input when no URL is available.

---

## Lifecycle Startup

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log with all single-instance documents set to status `--`, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log. Extract the client name and project type for use throughout this session.

### 2. Directory Validation

Verify these 8 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`, `research/`. Create any missing ones silently.

### 3. Session State Check

Check if `brief/intake-session.md` exists.

- If yes: read it and extract current phase, phases completed, key facts, conditional domain statuses. Report what was loaded:

```
Session state loaded from brief/intake-session.md
  Project: [project name]
  Last phase: [phase name]
  Phases completed: [list]
```

- If no: proceed with empty state. The file will be created when PREP completes.

### 4. Load Available Data

Check for existing client data:

- **D14 Client Research Profile:** prefer `brief/D14-client-research-profile.md` (compressed). If only `brief/D14-client-research-profile.raw.md` exists, load the raw version.
- **D11 Questionnaire:** `brief/D11-client-questionnaire.md` -- load if present.
- **D13 Answers:** `brief/D13-client-followup.md` -- if it exists with status `complete`, load answered questions.

**If D14 exists:** load it and proceed to Topic Reference below.

**If D14 does NOT exist:** branch to the Research Dispatch section below.

**If no D14, D11, or D13 is found AND no URL was provided as argument:** prompt the operator:

```
[PREP] No pre-existing data found (D14, D11, or D13).

Do you have a client website URL to research?
  -> Provide URL and I will run client research first

Or share any client data you have:
  -> Inquiry form answers, meeting prep notes, emails
  -> Any format works
```

- If operator provides a URL: branch to Research Dispatch.
- If operator provides manual data: accept it and proceed to Topic Reference.

---

## Research Dispatch

When D14 does not exist and a URL is available (either from argument or operator input), dispatch client research as a sub-agent:

```
[PREP] No D14 found. Running client research on [URL]...
```

Dispatch the client-researcher skill via Task tool:

```
Task(subagent_type="general-purpose", prompt="You are running the client-researcher skill. Follow the skill definition exactly.

Read and follow: ${CLAUDE_PLUGIN_ROOT}/skills/client-researcher/SKILL.md

Client URL: [URL]
[Optional context from operator if provided]

Complete all steps: web search, website crawl (via web-crawler agent), business registry lookup, D14 synthesis, save and compress. Write output to brief/D14-client-research-profile.raw.md and compress to brief/D14-client-research-profile.md.

IMPORTANT: Present the page selection to the operator for confirmation before crawling. For all other progress updates, proceed without waiting for confirmation.")
```

Wait for the Task to complete. Then load the compressed D14 from `brief/D14-client-research-profile.md` and continue:

```
[PREP] D14: Client Research Profile complete.

Sources: [web search findings count] external findings, [pages count] pages analyzed, registry: [status]
Output: brief/D14-client-research-profile.md (compressed)

Analyzing findings for interview guide...
```

Proceed to Topic Reference below.

---

## Topic Reference

The 9 conversation topics and 6 conditional extensions define how findings are organized. Read the full mapping at session start:

@references/topic-mapping.md

---

## Analysis Process

Using the topic structure above, analyze all loaded data.

### 1. Organize Findings by Topic

For each of the 9 conversation topics, extract what the available data tells us:
- **Strong findings** -- clearly stated, specific information
- **Partial findings** -- mentioned but unclear or shallow
- **Gaps** -- no information found

### 2. Determine Conditional Domain Applicability

Evaluate the 6 conditional extensions:

| Extension | Question |
|---|---|
| Online Store | Products or services sold directly online? |
| Content Publishing | Regular content publishing planned (blog, news)? |
| Multiple Languages | Site needs more than one language? |
| Member Access | Login, membership, or gated content? |
| Moving From Current Site | Existing site to migrate or replace? |
| Bookings and Appointments | Online appointments or reservations? |

- **Include without asking** when data clearly indicates applicability.
- **Exclude without asking** when data clearly indicates non-applicability.
- **Ask the operator** only when ambiguous:

```
[PREP] Based on the available data, I want to confirm:
- [Extension]: [evidence that makes it ambiguous] [yes / no]
```

### 3. Build Interview Guide

Prioritize topics by gap density:
- Topics with the most missing information come first (they need the most meeting time)
- Topics with strong findings can be covered briefly to confirm
- Conditional extensions attach to their parent topics per the mapping

For each topic in the recommended order, identify:
- Why this topic needs discussion (what is missing or unclear)
- Specific questions to ask (business language, not technical jargon)
- What we already know (so the operator can confirm quickly and move on)

---

## Output: PREP Report

```
[PREP] PREP REPORT: [Client Name]

DATA LOADED
  Sources: [D14 / D11 / inquiry form / notes -- list what was found]
  Key findings: [count of distinct data points extracted]

WHAT WE KNOW WELL
  [Topic]: [brief summary of strong findings]
  [Topic]: [brief summary of strong findings]
  ...

GAPS AND OPEN QUESTIONS
  [Topic]: [what's missing or unclear, specific questions to ask]
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

---

## Session State Write

After producing the PREP Report, write or update `brief/intake-session.md`.

If the file already exists (e.g., from a prior RESEARCH phase), preserve existing data and merge:

- Set `current_phase: PREP`
- Add `PREP` to `phases_completed`. If research was dispatched in this session, also add `RESEARCH`.
- Record conditional domain statuses (active, inactive, unknown)
- Record key facts extracted from available data
- Record topic gap summary (which topics have gaps, which are well covered)
- Record data sources loaded
- Set `last_updated` to today

---

## Suggest Next Step

```
PREP complete. When the client arrives, run:
  /webtools-intake-meeting
```

---

## Behavioral Rules

- Accept input in ANY format.
- Do NOT load domain checklist files from `references/domains/`. Analyze at the topic level using topic-mapping.md.
- Do NOT generate fictional content. If information is missing, identify it as a gap.
- Use conversation topic names (from topic-mapping.md), not technical domain names.
- Write questions in business language, not technical language.
- Do not use emojis in any output.
- Every response starts with `[PREP]`.

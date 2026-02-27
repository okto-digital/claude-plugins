---
description: "webtools-research: Run R2 Competitor Landscape (broad) research"
allowed-tools: Read, Write, Glob, Bash, WebSearch, WebFetch
---

Run the competitor-mapper agent to map the competitive landscape broadly -- discover 8-15 competitors, assess positioning, digital maturity, and reputation.

**You are now the competitor-mapper.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/competitor-mapper.md

---

## Lifecycle Startup

1. Read `project-registry.md` in the current working directory.
   - If not found: inform operator and suggest `/webtools-init`. Stop.

2. Ensure `research/` directory exists. Create it if needed: `mkdir -p research/`

3. Load D1 Project Brief:
   - Read `brief/D1-project-brief.md`
   - If not found: inform operator that D1 is required and suggest `/webtools-intake`. Stop.
   - Extract: client name, industry, core services, target location, named competitors.

4. Load D14 Client Research Profile:
   - Read `brief/D14-client-research-profile.md`
   - If not found: warn but continue. D14 is recommended, not required.
   - Extract: competitive context, industry signals.

5. Detect available crawling methods (per Tool Detection in agent definition).

6. Report status and begin:
   ```
   [R2] Competitor Landscape -- [client name]

   Prerequisites: D1 [loaded], D14 [loaded/not found]
   Crawl methods: [list available methods]

   Starting competitor landscape research...
   ```

---

## Execute

Follow the Methodology section of the agent definition above. Execute all steps in order:

1. Discover competitors (beyond client-named ones)
2. Surface scan each competitor homepage
3. Build market positioning map
4. Assess digital maturity
5. Synthesize findings

---

## Lifecycle Completion

1. Write R2 document to `research/R2-competitor-landscape.md` following the R-document template.

2. Check which other R-documents exist in `research/`. Report:
   ```
   R2 Competitor Landscape complete: research/R2-competitor-landscape.md

   Key findings:
     1. [finding]
     2. [finding]
     3. [finding]

   Competitors discovered: [count]
   Research progress: [X/8 topics complete]
   ```

3. Suggest next step:
   - If all R-documents complete: "Run /webtools-research-consolidate to produce D15."
   - Otherwise: "Run additional topics or /webtools-research-run for parallel execution."

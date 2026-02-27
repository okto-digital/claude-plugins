---
description: "webtools-research: Run R7 Technology & Performance research"
allowed-tools: Read, Write, Glob, Bash, WebSearch, WebFetch
---

Run the tech-auditor agent to assess the client's technology stack, page performance (Core Web Vitals), mobile usability, and accessibility baseline. Includes competitor performance comparison.

**You are now the tech-auditor.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/tech-auditor.md

---

## Lifecycle Startup

1. Read `project-registry.md` in the current working directory.
   - If not found: inform operator and suggest `/webtools-init`. Stop.

2. Ensure `research/` directory exists. Create it if needed: `mkdir -p research/`

3. Load D1 Project Brief:
   - Read `brief/D1-project-brief.md`
   - If not found: inform operator that D1 is required and suggest `/webtools-intake`. Stop.
   - Extract: client name, URL, project goals (redesign vs new build).

4. Load D14 Client Research Profile:
   - Read `brief/D14-client-research-profile.md`
   - If not found: warn but continue. D14 is recommended, not required.
   - Extract: existing tech detection (CMS, SSL, responsiveness), competitor URLs.

5. Detect available crawling methods (per Tool Detection in agent definition).

6. Report status and begin:
   ```
   [R7] Technology & Performance -- [client name]

   Prerequisites: D1 [loaded], D14 [loaded/not found]
   Crawl methods: [list available methods]
   PageSpeed API: available (via WebFetch)

   Starting technology audit...
   ```

---

## Execute

Follow the Methodology section of the agent definition above. Execute all steps in order:

1. PageSpeed Insights (client, mobile + desktop)
2. Competitor performance comparison (2-3 competitors)
3. Technology detection (CMS, frameworks, integrations)
4. Mobile usability assessment
5. Accessibility baseline check
6. Synthesize findings

---

## Lifecycle Completion

1. Write R7 document to `research/R7-tech-performance.md` following the R-document template.

2. Check which other R-documents exist in `research/`. Report:
   ```
   R7 Technology & Performance complete: research/R7-tech-performance.md

   Key findings:
     1. [finding]
     2. [finding]
     3. [finding]

   Performance: Mobile [score]/100, Desktop [score]/100
   Research progress: [X/8 topics complete]
   ```

3. Suggest next step:
   - If all R-documents complete: "Run /webtools-research-consolidate to produce D15."
   - Otherwise: "Run additional topics or /webtools-research-run for parallel execution."

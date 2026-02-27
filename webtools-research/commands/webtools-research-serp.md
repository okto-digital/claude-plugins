---
description: "webtools-research: Run R1 SERP & Search Landscape research"
allowed-tools: Read, Write, Glob, Bash, WebSearch, WebFetch
---

Run the serp-researcher agent to map the search engine results landscape for the client's core service keywords.

**You are now the serp-researcher.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/serp-researcher.md

---

## Lifecycle Startup

1. Read `project-registry.md` in the current working directory.
   - If not found: inform operator and suggest `/webtools-init`. Stop.

2. Ensure `research/` directory exists. Create it if needed: `mkdir -p research/`

3. Load D1 Project Brief:
   - Read `brief/D1-project-brief.md`
   - If not found: inform operator that D1 is required and suggest `/webtools-intake`. Stop.
   - Extract: client name, industry, core services, target location, business type.

4. Load D14 Client Research Profile:
   - Read `brief/D14-client-research-profile.md`
   - If not found: warn but continue. D14 is recommended, not required.
   - Extract: detected services, audience signals, competitive context.

5. Detect available crawling methods (per Tool Detection in agent definition).

6. Report status and begin:
   ```
   [R1] SERP & Search Landscape -- [client name]

   Prerequisites: D1 [loaded], D14 [loaded/not found]
   Crawl methods: [list available methods]

   Starting SERP landscape research...
   ```

---

## Execute

Follow the Methodology section of the agent definition above. Execute all steps in order:

1. Derive search queries from D1 + D14
2. Run SERP analysis via WebSearch
3. Content format sampling (optional, via crawl cascade)
4. Local SEO assessment (conditional on business type)
5. Synthesize findings

---

## Lifecycle Completion

1. Write R1 document to `research/R1-serp-landscape.md` following the R-document template.

2. Check which other R-documents exist in `research/`. Report:
   ```
   R1 SERP & Search Landscape complete: research/R1-serp-landscape.md

   Key findings:
     1. [finding]
     2. [finding]
     3. [finding]

   Research progress: [X/8 topics complete]
   ```

3. Suggest next step:
   - If all R-documents complete: "Run /webtools-research-consolidate to produce D15."
   - Otherwise: "Run additional topics or /webtools-research-run for parallel execution."

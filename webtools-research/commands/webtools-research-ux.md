---
description: "webtools-research: Run R4 UX/UI Patterns & Benchmarks research"
allowed-tools: Read, Write, Glob, Bash, WebSearch, WebFetch
---

Run the ux-benchmarker agent to identify industry-standard UX/UI patterns, design trends, and conversion flow benchmarks.

**You are now the ux-benchmarker.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/ux-benchmarker.md

---

## Lifecycle Startup

1. Read `project-registry.md` in the current working directory.
   - If not found: inform operator and suggest `/webtools-init`. Stop.

2. Ensure `research/` directory exists. Create it if needed: `mkdir -p research/`

3. Load D1 Project Brief:
   - Read `brief/D1-project-brief.md`
   - If not found: inform operator that D1 is required and suggest `/webtools-intake`. Stop.
   - Extract: client name, industry, core services, project goals.

4. Load D14 Client Research Profile:
   - Read `brief/D14-client-research-profile.md`
   - If not found: warn but continue. D14 is recommended, not required.
   - Extract: current site visual style and structure signals.

5. **Check for R2 cross-topic data:**
   - Read `research/R2-competitor-landscape.md` if it exists.
   - If found: extract competitor URLs for benchmark site selection. This gives R4 a head start on identifying benchmark sites.
   - If not found: R4 will discover benchmark sites independently via WebSearch.

6. Detect available crawling methods (per Tool Detection in agent definition).

7. Report status and begin:
   ```
   [R4] UX/UI Patterns & Benchmarks -- [client name]

   Prerequisites: D1 [loaded], D14 [loaded/not found]
   Cross-topic: R2 [loaded/not available]
   Crawl methods: [list available methods]
   Screenshots: [available/not available] (browser tools)

   Starting UX benchmark research...
   ```

---

## Execute

Follow the Methodology section of the agent definition above. Execute all steps in order:

1. Identify benchmark sites (using R2 data if available, otherwise WebSearch)
2. Page type inventory
3. Navigation and structure patterns
4. Conversion flow analysis
5. Design trend indicators
6. Synthesize findings

---

## Lifecycle Completion

1. Write R4 document to `research/R4-ux-benchmarks.md` following the R-document template.

2. Check which other R-documents exist in `research/`. Report:
   ```
   R4 UX/UI Patterns & Benchmarks complete: research/R4-ux-benchmarks.md

   Key findings:
     1. [finding]
     2. [finding]
     3. [finding]

   Benchmark sites audited: [count]
   Research progress: [X/8 topics complete]
   ```

3. Suggest next step:
   - If all R-documents complete: "Run /webtools-research-consolidate to produce D15."
   - Otherwise: "Run additional topics or /webtools-research-run for parallel execution."

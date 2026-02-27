---
description: "webtools-research: Run R5 Content Landscape & Strategy research"
allowed-tools: Read, Write, Glob, Bash, WebSearch, WebFetch
---

Run the content-strategist agent to map the content ecosystem -- what content types perform, frequency expectations, depth benchmarks, and content gaps.

**You are now the content-strategist.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/content-strategist.md

---

## Lifecycle Startup

1. Read `project-registry.md` in the current working directory.
   - If not found: inform operator and suggest `/webtools-init`. Stop.

2. Ensure `research/` directory exists. Create it if needed: `mkdir -p research/`

3. Load D1 Project Brief:
   - Read `brief/D1-project-brief.md`
   - If not found: inform operator that D1 is required and suggest `/webtools-intake`. Stop.
   - Extract: client name, industry, core services, content-related goals.

4. Load D14 Client Research Profile:
   - Read `brief/D14-client-research-profile.md`
   - If not found: warn but continue. D14 is recommended, not required.
   - Extract: current content assessment from client website.

5. **Check for R1 cross-topic data:**
   - Read `research/R1-serp-landscape.md` if it exists.
   - If found: extract SERP feature data and content type observations. This gives R5 pre-built SERP intelligence to cross-reference.
   - If not found: R5 will conduct independent SERP content analysis.

6. Detect available crawling methods (per Tool Detection in agent definition).

7. Report status and begin:
   ```
   [R5] Content Landscape & Strategy -- [client name]

   Prerequisites: D1 [loaded], D14 [loaded/not found]
   Cross-topic: R1 [loaded/not available]
   Crawl methods: [list available methods]

   Starting content landscape research...
   ```

---

## Execute

Follow the Methodology section of the agent definition above. Execute all steps in order:

1. Content type analysis (using R1 SERP data if available)
2. Content depth expectations
3. Content frequency assessment
4. Content gap identification
5. Linkable asset opportunities
6. Synthesize findings

---

## Lifecycle Completion

1. Write R5 document to `research/R5-content-strategy.md` following the R-document template.

2. Check which other R-documents exist in `research/`. Report:
   ```
   R5 Content Landscape & Strategy complete: research/R5-content-strategy.md

   Key findings:
     1. [finding]
     2. [finding]
     3. [finding]

   Content gaps identified: [count]
   Research progress: [X/8 topics complete]
   ```

3. Suggest next step:
   - If all R-documents complete: "Run /webtools-research-consolidate to produce D15."
   - Otherwise: "Run additional topics or /webtools-research-run for parallel execution."

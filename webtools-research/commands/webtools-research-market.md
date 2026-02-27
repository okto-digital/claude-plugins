---
description: "webtools-research: Run R8 Industry & Market Context research"
allowed-tools: Read, Write, Glob, Bash, WebSearch, WebFetch
---

Run the market-analyst agent to gather industry growth indicators, regulatory factors, seasonal patterns, market trends, and professional associations.

**You are now the market-analyst.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/market-analyst.md

---

## Lifecycle Startup

1. Read `project-registry.md` in the current working directory.
   - If not found: inform operator and suggest `/webtools-init`. Stop.

2. Ensure `research/` directory exists. Create it if needed: `mkdir -p research/`

3. Load D1 Project Brief:
   - Read `brief/D1-project-brief.md`
   - If not found: inform operator that D1 is required and suggest `/webtools-intake`. Stop.
   - Extract: client name, industry, geographic scope, market statements.

4. Load D14 Client Research Profile:
   - Read `brief/D14-client-research-profile.md`
   - If not found: warn but continue. D14 is recommended, not required.
   - Extract: industry signals from client website.

5. Detect available crawling methods (per Tool Detection in agent definition).

6. Report status and begin:
   ```
   [R8] Industry & Market Context -- [client name]

   Prerequisites: D1 [loaded], D14 [loaded/not found]
   Crawl methods: [list available methods]

   Starting market context research...
   ```

---

## Execute

Follow the Methodology section of the agent definition above. Execute all steps in order:

1. Industry growth and trends
2. Regulatory and compliance factors
3. Seasonal patterns
4. Market trends affecting digital presence
5. Professional associations
6. Validate D1 market statements
7. Synthesize findings

---

## Lifecycle Completion

1. Write R8 document to `research/R8-market-context.md` following the R-document template.

2. Check which other R-documents exist in `research/`. Report:
   ```
   R8 Industry & Market Context complete: research/R8-market-context.md

   Key findings:
     1. [finding]
     2. [finding]
     3. [finding]

   Research progress: [X/8 topics complete]
   ```

3. Suggest next step:
   - If all R-documents complete: "Run /webtools-research-consolidate to produce D15."
   - Otherwise: "Run additional topics or /webtools-research-run for parallel execution."

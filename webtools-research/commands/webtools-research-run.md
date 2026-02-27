---
description: "webtools-research: Select research topics and run them in parallel, then consolidate into D15"
allowed-tools: Read, Write, Glob, Bash(mkdir:*), WebSearch, WebFetch, Task, AskUserQuestion
---

Select research topics, dispatch them in parallel via Task tool, and consolidate results into D15 Research Report.

---

## Lifecycle Startup

### 1. Registry Check

Read `project-registry.md` in the current working directory.
- If not found: inform operator and stop. Suggest `/webtools-init`.

### 2. Directory Setup

Ensure `research/` directory exists:
```bash
mkdir -p research/
```

### 3. Load D1 Project Brief

Read `brief/D1-project-brief.md`.
- If not found: inform operator that D1 is required. Suggest `/webtools-intake`. Stop.
- If found: extract a summary (client name, industry, core services, target location, business type, key goals). This summary will be passed to each topic agent.

### 4. Load D14 Client Research Profile

Read `brief/D14-client-research-profile.md`.
- If not found: warn the operator that D14 is recommended but not required. Continue.
- If found: extract a summary (detected services, audience signals, competitive context, tech stack, digital presence). This summary will be passed to each topic agent.

### 5. Check Existing R-Documents

Check which R-documents already exist in `research/`:
- R1-serp-landscape.md
- R2-competitor-landscape.md
- R3-audience-personas.md
- R4-ux-benchmarks.md
- R5-content-strategy.md
- R6-reputation-social-proof.md
- R7-tech-performance.md
- R8-market-context.md

Report which are already complete. These will be pre-checked as "skip" in the topic selection (but operator can override to re-run).

---

## Topic Selection

Present all 8 topics to the operator using AskUserQuestion with multiSelect: true.

Include descriptions and note which are already complete:

```
Select research topics to run:

Wave 1 (independent -- run in parallel):
  [ ] R1  SERP & Search Landscape       -- Map who ranks, SERP features, search intent  [complete/not started]
  [ ] R2  Competitor Landscape (Broad)   -- Discover 8-15 competitors, positioning map   [complete/not started]
  [ ] R3  Audience & User Personas       -- Demographics, psychographics, buyer journey  [complete/not started]
  [ ] R6  Reputation & Social Proof      -- Reviews, brand mentions, social presence     [complete/not started]
  [ ] R7  Technology & Performance       -- PageSpeed, tech stack, accessibility         [complete/not started]
  [ ] R8  Industry & Market Context      -- Growth trends, regulations, seasonality      [complete/not started]

Wave 2 (benefit from Wave 1 outputs):
  [ ] R4  UX/UI Patterns & Benchmarks   -- Page types, navigation, conversion flows     [complete/not started]
       Benefits from R2 competitor URLs
  [ ] R5  Content Landscape & Strategy   -- Content types, depth, gaps, linkable assets  [complete/not started]
       Benefits from R1 SERP findings
```

After operator selects topics, confirm the selection and proceed.

---

## Parallel Dispatch

### Wave 1

For each selected Wave 1 topic (R1, R2, R3, R6, R7, R8):

1. Read the agent definition file using the Read tool:
   - R1: `${CLAUDE_PLUGIN_ROOT}/agents/serp-researcher.md`
   - R2: `${CLAUDE_PLUGIN_ROOT}/agents/competitor-mapper.md`
   - R3: `${CLAUDE_PLUGIN_ROOT}/agents/audience-researcher.md`
   - R6: `${CLAUDE_PLUGIN_ROOT}/agents/reputation-scanner.md`
   - R7: `${CLAUDE_PLUGIN_ROOT}/agents/tech-auditor.md`
   - R8: `${CLAUDE_PLUGIN_ROOT}/agents/market-analyst.md`

2. For each agent, create a Task with subagent_type "general-purpose". The prompt for each Task must include:
   - The full agent definition content (embedded, not referenced)
   - The D1 summary
   - The D14 summary (if available)
   - Instruction to write the R-document to the research/ directory using the working directory path
   - Instruction to follow the agent's Methodology section step by step
   - The R-document template from `${CLAUDE_PLUGIN_ROOT}/references/r-document-template.md`

<critical>
Dispatch ALL Wave 1 Task calls in a SINGLE message. This enables parallel execution. Do NOT dispatch them one at a time.
</critical>

3. Wait for all Wave 1 Tasks to complete. As each returns, report progress:
   ```
   [2/6 topics complete] R1 SERP & Search Landscape -- done
   ```

### Wave 2

After Wave 1 completes, if R4 or R5 were selected:

1. Read any newly completed Wave 1 documents that Wave 2 agents benefit from:
   - For R4: read `research/R2-competitor-landscape.md` (if R2 was completed) -- extract competitor URLs
   - For R5: read `research/R1-serp-landscape.md` (if R1 was completed) -- extract SERP findings

2. Read the agent definition files:
   - R4: `${CLAUDE_PLUGIN_ROOT}/agents/ux-benchmarker.md`
   - R5: `${CLAUDE_PLUGIN_ROOT}/agents/content-strategist.md`

3. Dispatch Wave 2 Tasks (in a single message if both selected). Each Task prompt includes:
   - The full agent definition content
   - D1 summary, D14 summary
   - Cross-topic data from Wave 1 (R2 competitor URLs for R4, R1 SERP findings for R5)
   - Same R-document template and write instructions

4. Wait for Wave 2 to complete. Report progress.

**If operator selected R4 or R5 but NOT their Wave 1 dependency:** dispatch them anyway. The agents work without cross-topic data, just with less context.

### Failure Handling

If a Task fails or returns an error:
- Report the failure: "[FAILED] R[N] [Topic Name] -- [error summary]"
- Continue with remaining topics
- After all topics complete, suggest re-running failed topics individually:
  ```
  Failed topics can be re-run individually:
    /webtools-research-[topic]
  ```

---

## Consolidation

After all selected topics complete successfully:

### 1. Load All R-Documents

Read every R-document that exists in `research/` (not just the ones dispatched in this run -- include previously completed topics too).

### 2. Load D15 Template

Read `${CLAUDE_PLUGIN_ROOT}/references/d15-template.md`.

### 3. Synthesize D15

Follow the D15 template structure:

- **Executive Summary:** 5-8 most important findings across ALL completed topics. Write for a reader who will not read individual R-documents.
- **Strategic Opportunities:** Cross-cutting opportunities synthesized from MULTIPLE topics. Reference which R-documents contributed. Do not repeat single-topic findings.
- **Risk Factors:** Cross-cutting risks with mitigation suggestions.
- **Topic Summaries:** Key Findings section from each completed R-document.
- **Proposal Inputs:** Concrete suggestions organized by proposal section (problem statement, solution highlights, differentiation, risk mitigation, scope justification).
- **Recommended Deep-Dives:** Which existing webtools tools to run next with specific focus areas informed by research findings.
- **Appendix: Sources:** Consolidated and de-duplicated source list from all R-documents.

### 4. Write D15

Write to `research/D15-research-report.md` with YAML frontmatter:
```yaml
---
document_type: research-report
document_id: D15
title: "Research Report -- [Company Name]"
project: "[client name]"
topics_completed: [list of R-IDs completed]
topics_skipped: [list of R-IDs not completed]
created: [today's date]
created_by: webtools-research
status: complete
---
```

---

## Lifecycle Completion

### 1. Update Registry

Update `project-registry.md`:
- Add Research phase to the Phase Log (if not already present)
- Add D15 entry to the Document Log with status "complete"
- Add R-document entries for each completed topic

### 2. Report Completion

```
Research phase complete.

Topics completed: [list with R-IDs]
Topics skipped: [list with R-IDs]

D15 Research Report: research/D15-research-report.md

Key insights:
  1. [Top finding from executive summary]
  2. [Second finding]
  3. [Third finding]

Suggested next steps:
  - Use D15 to write the project proposal
  - Run production deep-dives informed by research:
    /webtools-seo (D3) -- [specific focus from R1/R5]
    /webtools-competitors (D5) -- [specific competitors from R2]
```

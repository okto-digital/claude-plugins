---
name: project-research
description: "Run D3 project research: dispatch researcher agents for 8 domains in waves of 2, consolidate into D3 summary. Invoke when the user asks to run project research, generate D3, research the project, or start the research phase."
allowed-tools: Read, Write, Glob, Bash, WebSearch, Task, AskUserQuestion
version: 1.0.0
---

# Project Research

Dispatch researcher agents for up to 8 research domains in waves of 2, then consolidate all R-documents into D3: Project Research summary. Each researcher agent loads a domain-specific methodology file, executes research using WebSearch + web-crawler + optionally DataForSEO, and produces an R-document.

**Core principle:** One generic researcher agent, many domain reference files. The orchestrator handles topic selection, wave dispatch, progress reporting, and final consolidation.

---

## Process

### Step 1: Load project context

Read `project-state.md` from the project working directory. Extract client name, URL, project type, and document status.

If project-state.md does not exist, stop and tell the operator: "Run project-init first to set up the project."

If D1 is not complete, stop and tell the operator: "D1 (Client Intake) must be complete before running D3 research. Run client-intake first."

### Step 2: Load D1 + D2

Read the D1 document (path from project-state.md). Extract a summary for research context:
- Client name, company name, URL
- Industry, location, business type (local/regional/national)
- Core services offered
- Key findings from research
- Competitors identified
- Domain analysis highlights (top gaps, critical findings)

If D2 exists (path from project-state.md), also read it and extract:
- Client priorities and constraints
- Decisions from interview
- Additional context not in D1

Combine into a **project context block** -- a text summary that will be passed to each researcher agent in the dispatch prompt. Keep it under 2000 words.

### Step 3: Check existing R-documents

Scan `research/` directory for existing R-documents (R1-R8):
- Glob for `research/R*.md`
- For each found, note the document ID and topic

Report to operator: "Found X existing R-documents: [list]. These will be skipped unless you want to re-run them."

### Step 4: Topic selection

Present all 8 research topics to the operator with wave labels:

**Wave 1 (independent -- no cross-topic inputs):**
- R1: SERP & Search Landscape
- R2: Competitor Landscape
- R3: Audience & User Personas
- R6: Reputation & Social Proof
- R7: Technology & Performance
- R8: Industry & Market Context

**Wave 2 (benefit from Wave 1 outputs):**
- R4: UX/UI Patterns & Benchmarks (benefits from R2 competitor URLs)
- R5: Content Landscape & Strategy (benefits from R1 SERP data)

Use AskUserQuestion with multiSelect=true. Pre-select all topics that do not have existing R-documents. Let the operator deselect topics they want to skip or select already-completed topics for re-run.

### Step 5: Wave dispatch

Dispatch selected researcher agents via the `dispatch-subagent` skill. All researcher agents use **opus** model (analysis + synthesis needed).

**Concurrency limit: maximum 2 sub-agents at a time.** Dispatch in batches of 2, wait for the batch to complete, then dispatch the next batch.

**Dispatch order:**

1. All selected Wave 1 topics, in batches of 2:
   - Batch 1: first 2 selected Wave 1 topics
   - Batch 2: next 2 selected Wave 1 topics
   - Batch 3: remaining Wave 1 topics (1-2)
2. All selected Wave 2 topics, in batches of 2:
   - For R4: include R2 output path as cross-topic input (if R2 was run or exists)
   - For R5: include R1 output path as cross-topic input (if R1 was run or exists)

**Each dispatch provides:**
- Domain name (e.g., "serp-landscape")
- Domain file path: `${CLAUDE_PLUGIN_ROOT}/agents/references/research-domains/[domain].md`
- R-document template path: `${CLAUDE_PLUGIN_ROOT}/references/r-document-template.md`
- Project context block (from Step 2)
- Cross-topic R-document paths (Wave 2 only, if available)
- Output directory: `research/`
- MCP tool hints: include both DataForSEO and web-crawler tool hints from dispatch-subagent
- Model: opus

**Progress reporting:** After each batch completes, report to operator:
- Which topics completed successfully
- Key Findings from each (the 3-5 bullet summary returned by each agent)
- Any failures (and whether to retry or skip)

### Step 6: Consolidate into D3

After all dispatched researchers complete, read all R-documents in `research/`.

Synthesize D3: Project Research with this structure:

```markdown
---
document_type: project-research
document_id: D3
title: "D3 Project Research -- [Company Name]"
project: "[client name]"
topics_completed: [N of 8]
created: [YYYY-MM-DD]
created_by: website-1-discovery
status: complete
---

# D3 Project Research -- [Company Name]

## Executive Summary

5-8 cross-topic findings that emerge from looking across all R-documents together. These are patterns visible only when combining multiple research angles -- not just restating individual R-document findings.

## Strategic Opportunities

Multi-topic patterns that suggest specific actions:
- [Opportunity] -- supported by [R-documents that contribute to this finding]

## Risk Factors

Challenges and threats that the proposal must address:
- [Risk] -- identified in [R-documents]

## Topic Summaries

### R1: SERP & Search Landscape
**Key Findings:** [from R1]
**Recommendations:** [from R1]

### R2: Competitor Landscape
**Key Findings:** [from R2]
**Recommendations:** [from R2]

[...repeat for each completed R-document...]

## Proposal Inputs

Concrete elements ready to include in D4 (Project Brief):

### Problem Statement
[Synthesized from research findings -- what is the core problem the project solves?]

### Solution Highlights
[Key solution elements supported by research evidence]

### Differentiation
[What sets the proposed solution apart, based on competitive gaps and market analysis]

### Risk Mitigation
[How the proposal addresses identified risks]

## Research Coverage

| Topic | Status | Confidence | Sources |
|---|---|---|---|
| R1 SERP & Search Landscape | complete/skipped | high/medium/low | N |
| R2 Competitor Landscape | complete/skipped | ... | N |
| R3 Audience & User Personas | complete/skipped | ... | N |
| R4 UX/UI Patterns & Benchmarks | complete/skipped | ... | N |
| R5 Content Landscape & Strategy | complete/skipped | ... | N |
| R6 Reputation & Social Proof | complete/skipped | ... | N |
| R7 Technology & Performance | complete/skipped | ... | N |
| R8 Industry & Market Context | complete/skipped | ... | N |
```

Write to `research/D3-project-research.md`.

### Step 7: Update state

Read project-state.md. Update the D3 row:
- status: complete
- file: research/D3-project-research.md
- updated: today's date

Write the updated project-state.md. Do not modify any other rows.

---

## Rules

<critical>
- **NEVER** skip D1 prerequisite check -- D1 must be complete before D3
- **NEVER** dispatch more than 2 researcher agents concurrently
- **NEVER** fabricate or embellish D3 findings beyond what R-documents contain
- **NEVER** modify project-state.md beyond the D3 row
- **NEVER** run without project-state.md -- require project-init first
- **NEVER** read the domain reference files directly -- leave this to the dispatched researcher agents
</critical>

- If a researcher agent fails, note which topic was affected, report to operator, and continue with remaining topics
- If fewer than 4 topics complete successfully, warn the operator that D3 coverage will be limited
- If D2 does not exist, proceed with D1 only -- D2 enriches context but is not required
- Wave 2 topics can run without their cross-topic inputs -- they just produce slightly less cross-referenced output

---

## Reference Files

All shared references are at the plugin root:

- `${CLAUDE_PLUGIN_ROOT}/references/r-document-template.md` -- R-document output template
- `${CLAUDE_PLUGIN_ROOT}/agents/references/research-domains/*.md` -- 8 domain methodology files (read by researcher agents, not by this skill directly)

Sub-agents dispatched by this skill (via dispatch-subagent):

- `researcher` -- Execute domain-specific research, produce R-document (up to 8 instances, dispatched in waves of 2)

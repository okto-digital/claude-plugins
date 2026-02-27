---
description: "webtools-research: Consolidate completed R-documents into D15 Research Report"
allowed-tools: Read, Write, Glob
---

Read all completed research topic documents (R1-R8) and synthesize them into D15: Research Report -- a consolidated deliverable with executive summary, cross-cutting insights, and proposal inputs.

---

## Lifecycle Startup

### 1. Registry Check

Read `project-registry.md` in the current working directory.
- If not found: inform operator and suggest `/webtools-init`. Stop.
- Extract: client name, project type.

### 2. Inventory R-Documents

List all files in `research/` directory. Check for each R-document:

| File | Topic | Status |
|---|---|---|
| `research/R1-serp-landscape.md` | SERP & Search Landscape | [found/missing] |
| `research/R2-competitor-landscape.md` | Competitor Landscape | [found/missing] |
| `research/R3-audience-personas.md` | Audience & User Personas | [found/missing] |
| `research/R4-ux-benchmarks.md` | UX/UI Patterns & Benchmarks | [found/missing] |
| `research/R5-content-strategy.md` | Content Landscape & Strategy | [found/missing] |
| `research/R6-reputation-social-proof.md` | Reputation & Social Proof | [found/missing] |
| `research/R7-tech-performance.md` | Technology & Performance | [found/missing] |
| `research/R8-market-context.md` | Industry & Market Context | [found/missing] |

If no R-documents are found: inform operator and suggest `/webtools-research-run`. Stop.

If some are found: report which topics will be included and which will be listed as skipped.

### 3. Check for Existing D15

If `research/D15-research-report.md` already exists:
- Inform operator that D15 exists
- Ask whether to overwrite or cancel

---

## Load R-Documents

Read each existing R-document in full. For each document, extract:
- **Key Findings** section (3-5 bullets)
- **Opportunities & Risks** section
- **Confidence** level from frontmatter
- **Sources** section

---

## Load D15 Template

Read `${CLAUDE_PLUGIN_ROOT}/references/d15-template.md` for the consolidation structure.

---

## Synthesize D15

Follow the D15 template structure precisely:

### 1. Executive Summary

Write 5-8 most important findings across ALL completed topics. Each finding should be 2-3 sentences with a specific data point and implication.

**IMPORTANT:** Write for a reader who will NOT read the individual R-documents. This section must stand alone as a complete briefing. Synthesize across topics -- do not just list one finding per topic.

### 2. Strategic Opportunities

Identify cross-cutting opportunities that synthesize findings from MULTIPLE topics. Each opportunity must reference which R-documents contributed:

- Look for reinforcing patterns (e.g., competitors weak on mobile + audience is mobile-heavy = differentiation opportunity)
- Look for converging signals (e.g., content gaps + underserved audience segments = content strategy opening)
- Prioritize opportunities that appear across 3+ topics

Do NOT repeat single-topic findings. The value of D15 is the cross-topic synthesis.

### 3. Risk Factors

Identify cross-cutting risks with the same multi-topic synthesis approach:

- Competitive threats that affect multiple areas
- Market or regulatory challenges
- Technical debt or performance issues that constrain other goals

Include mitigation suggestions for each risk.

### 4. Topic Summaries

One sub-section per completed R-document. Pull the Key Findings from each and present under a heading. Lightly edit for flow but preserve the substance.

Skip sub-sections for missing topics (they appear in the `topics_skipped` frontmatter).

### 5. Proposal Inputs

Organize concrete suggestions by proposal section:

- **Problem statement / pain points** -- what to emphasize based on research
- **Proposed solution highlights** -- features justified by research findings
- **Differentiation arguments** -- what competitors do NOT do that this project will
- **Risk mitigation / trust building** -- concerns to address proactively
- **Pricing / scope justification** -- market benchmarks that justify the scope

### 6. Recommended Deep-Dives

Specify which existing webtools tools should run next with focus areas informed by research:

- **D3 -- SEO Keyword Map** (webtools-seo): which keyword clusters from R1/R5, priority intent types
- **D5 -- Competitor Analysis** (webtools-competitors): which specific competitors from R2, why these matter
- **D6 -- Content Inventory** (webtools-inventory): recommended if redesign, focus areas from R5/R7

Each recommendation should be specific, not generic.

### 7. Appendix: Sources

Consolidate source lists from all R-documents. De-duplicate URLs that appear in multiple topics. Group by topic.

---

## Write D15

Write to `research/D15-research-report.md` with YAML frontmatter:

```yaml
---
document_type: research-report
document_id: D15
title: "Research Report -- [Company Name]"
project: "[client name]"
topics_completed: [R1, R3, R5, R7]
topics_skipped: [R2, R4, R6, R8]
created: [today's date]
created_by: webtools-research
status: complete
---
```

Replace the example lists with actual completed/skipped topic IDs.

---

## Lifecycle Completion

### 1. Update Registry

Update `project-registry.md`:
- Add D15 entry to the Document Log with status "complete" and today's date
- Add a Research phase entry to the Phase Log if not already present

### 2. Report Completion

```
D15 Research Report complete: research/D15-research-report.md

Topics included: [list with names]
Topics skipped: [list with names]

Executive summary highlights:
  1. [top finding]
  2. [second finding]
  3. [third finding]

Suggested next steps:
  - Use D15 to write the project proposal
  - Run production deep-dives informed by research:
    /webtools-seo (D3) -- [specific focus from R1/R5]
    /webtools-competitors (D5) -- [specific competitors from R2]
    /webtools-inventory (D6) -- [if applicable]
```

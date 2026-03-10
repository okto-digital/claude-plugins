---
name: project-brief
description: "Generate D3: Project Brief & Proposal from D1 + D2. Client-facing document with current state assessment, key findings, proposed solution, scope, timeline, and success metrics. Invoke when the user asks to generate the brief, write the proposal, produce D3, or finalize discovery."
allowed-tools: Read, Write, Glob, AskUserQuestion
version: 1.0.0
---

# Project Brief

Read D1 (Client Intake) and D2 (Project Research), synthesize into D3: a client-facing Project Brief & Proposal. Single pass -- no sub-agents needed.

**Core principle:** Every recommendation traces to evidence. Every section tells the client something actionable. No internal jargon, no raw research dumps.

---

## Process

### Step 1: Load project context

Read `project-state.md` from the project working directory. Extract client name, URL, project type, and document status.

If project-state.md does not exist, stop and tell the operator: "Run project-init first to set up the project."

If D1 is not complete, stop: "Run client-intake first."

If D1 is `research-complete` (not `interview-complete`), warn: "D1 has research findings but no client answers. Proposal will lack client priorities. Proceed?" Use AskUserQuestion.

If D2 is not complete, warn: "D2 not complete. D3 from D1 alone will lack research evidence. Proceed?" Use AskUserQuestion. If declined, stop.

### Step 2: Load D1

Read the full D1 document (path from project-state.md). Extract:

- Company identity (name, industry, location, services, positioning)
- Website assessment, digital presence, competitive context, external intelligence (Sections 1.3-1.6)
- Client priorities from interview answers (Section 2 domains)
- Active domains (determines applicable phases)
- Unresolved CRITICAL gaps
- Complexity signals: page count, integration count, content volume, conditional domains active

### Step 3: Load D2

Read the full D2 document (path from project-state.md). Extract:

- **Executive summary:** Cross-topic findings and overall assessment
- **Strategic opportunities:** Market gaps, differentiation angles, quick wins
- **Risk factors:** Competitive threats, market challenges, technical risks
- **Per-topic summaries:** Key findings and recommendations from each research domain
- **Proposal inputs:** Problem statement, solution highlights, differentiation points, risk mitigation strategies

### Step 4: Load R-documents (selective)

Scan `research/` for R-document files. Read individual R-documents only where D2 summaries lack sufficient detail for specific recommendations. Focus on:

- **Recommendations sections** -- these contain the specific, actionable items that feed into Section 4
- **Key findings** -- for evidence to cite in Sections 2 and 3

Do not read all R-documents by default. D2 consolidates the essentials. Only go deeper when writing a section and the D2 summary is too thin for specifics.

### Step 5: Determine applicable phases

Based on project type and D1 domain analysis, determine which phases appear in Sections 4 and 5:

| Phase | Condition |
|---|---|
| Strategy & Architecture | Always |
| Design & Brand | Always |
| Content | Always |
| SEO & Discoverability | Always |
| Development & Technical | Always |
| Migration | Project type = `redesign`, OR migration-and-redesign domain ACTIVE in D1 |
| E-commerce | ecommerce domain ACTIVE in D1 |
| Integrations | booking-and-scheduling domain ACTIVE, OR D1 technical-platform domain identifies CRM/payment/other integrations |
| Launch & Post-Launch | Always |

Record the list of applicable phases for use in Steps 7 and 8.

### Step 6: Estimate hours

Assess complexity as simple/medium/complex from D1 signals, then apply baseline hour ranges:

| Signal | Simple | Medium | Complex |
|---|---|---|---|
| Page count | 1-7 | 8-15 | 16+ |
| Integrations | 0 | 1-2 | 3+ |
| Content volume | Light (few pages, short copy) | Moderate | Heavy (blog, case studies, multilingual) |
| Conditional domains active | 0-1 | 2-3 | 4+ |
| E-commerce | No | Simple catalog | Full store with payments |

Use the median complexity level across signals. When signals conflict, weight page count and integrations higher (they drive development time most directly).

**Baseline hour ranges per phase:**

| Phase | Simple | Medium | Complex |
|---|---|---|---|
| Strategy & Architecture | 8-12h | 12-18h | 18-24h |
| Design & Brand | 16-24h | 24-36h | 36-48h |
| Content | 12-16h | 16-28h | 28-40h |
| SEO & Discoverability | 6-10h | 10-16h | 16-24h |
| Development & Technical | 24-32h | 32-48h | 48-72h |
| Migration | -- | 6-12h | 12-20h |
| E-commerce | -- | 16-24h | 24-40h |
| Integrations | -- | 4-8h | 8-16h |
| Testing & Launch | 6-10h | 10-14h | 14-20h |
| Post-Launch | 4-6h | 6-8h | 8-12h |

Notes:
- Migration, E-commerce, and Integrations are 0h when the phase does not apply
- Testing & Launch and Post-Launch are sub-phases of "Launch & Post-Launch" -- show them as separate rows in the scope table
- These are starting estimates for the proposal, not fixed quotes

### Step 7: Read D3 template

Read `references/d3-template.md` (relative to the plugin root -- use `${CLAUDE_PLUGIN_ROOT}/references/d3-template.md` or locate via Glob). This provides the output structure, formatting rules, and section guidelines.

### Step 8: Write D3

Create the `brief/` directory in the project working directory if it does not exist.

If `brief/D3-project-brief.md` already exists, warn: "D3 already exists at brief/D3-project-brief.md. Overwrite?" Use AskUserQuestion. If declined, stop.

Synthesize all extracted data into the D3 template structure. Write to `brief/D3-project-brief.md`.

**Section-by-section synthesis:**

1. **Executive Summary:** D1 identity + project type + D2 strategic summary. One page. Who, what, why, expected outcome.
2. **Current State Assessment:** D1 Sections 1.3-1.6 enriched with D2 topics. Five areas: Online Presence, Search Visibility, Competitive Position, Technical Health, Reputation & Trust. Narrative prose, specific evidence, end each with "Bottom line:" statement.
3. **Key Findings:** 5-8 cross-topic insights from D2 executive summary + strategic opportunities. Each needs evidence + business impact.
4. **Proposed Solution:** 3-6 actions per applicable phase (from Step 5). Each traces to Section 3 finding or Section 2 observation with "why" and "expected outcome". Use R-documents (Step 4) when D2 summaries lack specificity.
5. **Scope & Timeline:** Table with applicable phases, hour estimates (Step 6), project-specific deliverables. Add total row.
6. **Total Hours Summary:** Sum from Section 5. If >120h, split MVP vs full scope.
7. **Success Metrics:** 3-5 measurable KPIs from D1 priorities + D2 baselines with 6-month targets.
8. **Next Steps:** 2-3 actions: review brief, schedule kickoff, provide access to needed assets.

### Writing rules

Apply throughout:

- **Second person** where natural ("your website", "your competitors")
- **No internal codes** -- never write R1, R2, D1, D2 in the output
- **No internal language** -- no intake questions, confidence scores, "FOUND"/"PARTIAL"/"GAP" labels
- **Evidence over assertion** -- every recommendation links to an observed fact
- **Specific over generic** -- name competitors, cite numbers, reference actual pages
- **Prose** in Sections 2-3, **bullets** for actions in Section 4

### Step 9: Present to operator

After writing D3, display a summary to the operator:

```
D3: Project Brief & Proposal -- [Client Name]

Sections written:
  1. Executive Summary
  2. Current State Assessment ([N] areas covered)
  3. Key Findings ([N] findings)
  4. Proposed Solution ([N] phases, [N] total actions)
  5. Scope & Timeline ([low]-[high]h estimated)
  6. Total Hours Summary
  7. Success Metrics ([N] KPIs)
  8. Next Steps

Output: brief/D3-project-brief.md

Review the document and let me know if any sections need adjustment.
```

Wait for operator feedback. If they request changes, edit D3 in place.

### Step 10: Update state

After operator approves (or does not request changes), update `project-state.md`:

1. Read `project-state.md`
2. Find the D3 pipeline row
3. Update: Status to `complete`, File to `brief/D3-project-brief.md`, Updated to today's date
4. Write `project-state.md`

Display: "D3 complete. Pipeline status: 3/3 documents done."

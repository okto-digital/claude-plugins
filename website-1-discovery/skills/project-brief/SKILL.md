---
name: project-brief
description: "Generate D4: Project Brief & Proposal from D1 + D3. Client-facing document with current state assessment, key findings, proposed solution, scope, timeline, and success metrics. Invoke when the user asks to generate the brief, write the proposal, produce D4, or finalize discovery."
allowed-tools: Read, Write, Glob, AskUserQuestion
version: 1.0.0
---

# Project Brief

Read D1 (Client Intake) and D3 (Project Research), synthesize into D4: a client-facing Project Brief & Proposal. Single pass -- no sub-agents needed.

**Core principle:** Every recommendation traces to evidence. Every section tells the client something actionable. No internal jargon, no raw research dumps.

---

## Process

### Step 1: Load project context

Read `project-state.md` from the project working directory. Extract client name, URL, project type, and document status.

If project-state.md does not exist, stop and tell the operator: "Run project-init first to set up the project."

If D1 is not complete, stop and tell the operator: "D1 (Client Intake) must be complete before generating D4. Run client-intake first."

If D3 is not complete, warn the operator: "D3 (Project Research) is not complete. D4 can be generated from D1 alone, but the proposal will lack research-backed evidence and will be significantly weaker. Proceed anyway?" Use AskUserQuestion to confirm. If operator declines, stop.

### Step 2: Load D1

Read the full D1 document (path from project-state.md). Extract:

- **Company identity:** Name, industry, location, services, business model, positioning
- **Current website assessment:** Structure, content, tech stack, issues (Section 1.3)
- **Digital presence:** Social, SEO, conversion elements, analytics (Section 1.4)
- **Competitive context:** Competitors identified, client positioning (Section 1.5)
- **External intelligence:** News, reviews, social presence (Section 1.6)
- **Client priorities:** From interview answers throughout Section 2 domains
- **Active domains:** Which of the 21 domains had STATUS: ACTIVE (determines applicable phases)
- **Key gaps:** CRITICAL gaps that were not resolved in the interview
- **Complexity signals:** Page count (from site-structure domain), integration count (from technical-platform), content volume (from content-strategy), conditional domains active (migration, ecommerce, booking, multilingual)

### Step 3: Load D3

Read the full D3 document (path from project-state.md). Extract:

- **Executive summary:** Cross-topic findings and overall assessment
- **Strategic opportunities:** Market gaps, differentiation angles, quick wins
- **Risk factors:** Competitive threats, market challenges, technical risks
- **Per-topic summaries:** Key findings and recommendations from each research domain
- **Proposal inputs:** Problem statement, solution highlights, differentiation points, risk mitigation strategies

### Step 4: Load R-documents (selective)

Scan `research/` for R-document files. Read individual R-documents only where D3 summaries lack sufficient detail for specific recommendations. Focus on:

- **Recommendations sections** -- these contain the specific, actionable items that feed into Section 4
- **Key findings** -- for evidence to cite in Sections 2 and 3

Do not read all R-documents by default. D3 consolidates the essentials. Only go deeper when writing a section and the D3 summary is too thin for specifics.

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

Apply baseline ranges per phase, adjusted by complexity signals from D1.

**Complexity determination:**

Assess overall project complexity as simple, medium, or complex based on these signals:

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

### Step 7: Read D4 template

Read `references/d4-template.md` (relative to the plugin root -- use `${CLAUDE_PLUGIN_ROOT}/references/d4-template.md` or locate via Glob). This provides the output structure, formatting rules, and section guidelines.

### Step 8: Write D4

Create the `brief/` directory in the project working directory if it does not exist.

Synthesize all extracted data into the D4 template structure. Write to `brief/D4-project-brief.md`.

**Section-by-section synthesis:**

**Section 1 (Executive Summary):** Combine D1 company identity + project type + D3 strategic summary into a one-page overview. Lead with who the client is, what we propose, and the expected business outcome.

**Section 2 (Current State Assessment):** Build from D1 Sections 1.3-1.6 (website assessment, digital presence, competitive context, external intelligence) enriched with D3 topic summaries. Organize by the five client-facing areas (Online Presence, Search Visibility, Competitive Position, Technical Health, Reputation & Trust). Write narrative prose with specific evidence. End each area with a "Bottom line:" statement.

**Section 3 (Key Findings):** Synthesize from D3 executive summary and strategic opportunities. Select 5-8 findings that directly drive the proposal. Each finding must have a specific evidence statement and a business impact explanation. These are cross-topic insights, not per-topic summaries.

**Section 4 (Proposed Solution):** For each applicable phase (from Step 5), write 3-6 specific actions. Each action traces to a finding from Section 3 or an observation from Section 2. Include the "why" and "expected outcome" for each. Use R-document recommendations as the source for specific action items -- go back to individual R-documents (Step 4) if D3 summaries lack the specificity needed.

**Section 5 (Scope & Timeline):** Build the table using applicable phases, hour estimates from Step 6, and project-specific deliverables. Timeline assumes sequential phases with natural overlap. Add a total row.

**Section 6 (Total Hours Summary):** Sum the ranges from Section 5. If total exceeds 120h, present MVP vs full scope split.

**Section 7 (Success Metrics):** Select 3-5 KPIs from D1 client priorities and D3 research baselines. Each needs a current baseline (from research data) and a realistic 6-month target.

**Section 8 (Next Steps):** 2-3 concrete actions. Always include: review brief, schedule kickoff. Add project-specific items (provide access to hosting, CMS, brand materials, etc.) based on what D1 identified as needed.

### Writing rules

Apply these rules throughout the document:

- **Second person** where natural ("your website", "your competitors")
- **No internal codes** -- never write R1, R2, D1, D3 in the output document
- **No intake questions** -- D4 contains answers and recommendations, never questions
- **No confidence scores** -- internal quality tracking stays internal
- **No gap/checkpoint language** -- no "FOUND", "PARTIAL", "GAP", "CRITICAL gap"
- **Evidence over assertion** -- every recommendation links to an observed fact
- **Business language** -- "this will help you capture more leads" not "this improves conversion rate optimization"
- **Specific over generic** -- name competitors, cite numbers, reference actual pages
- **Prose over bullets** in Sections 2 and 3 -- use narrative paragraphs, not bullet dumps
- **Bullets for actions** in Section 4 -- each action is a distinct line item

### Step 9: Present to operator

After writing D4, display a summary to the operator:

```
D4: Project Brief & Proposal -- [Client Name]

Sections written:
  1. Executive Summary
  2. Current State Assessment ([N] areas covered)
  3. Key Findings ([N] findings)
  4. Proposed Solution ([N] phases, [N] total actions)
  5. Scope & Timeline ([low]-[high]h estimated)
  6. Total Hours Summary
  7. Success Metrics ([N] KPIs)
  8. Next Steps

Output: brief/D4-project-brief.md

Review the document and let me know if any sections need adjustment.
```

Wait for operator feedback. If they request changes, edit D4 in place.

### Step 10: Update state

After operator approves (or does not request changes), update `project-state.md`:

1. Read `project-state.md`
2. Find the D4 pipeline row
3. Update: Status to `complete`, File to `brief/D4-project-brief.md`, Updated to today's date
4. Write `project-state.md`

Display: "D4 complete. Pipeline status: 3/3 documents done."

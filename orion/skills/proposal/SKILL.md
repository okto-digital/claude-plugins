---
name: proposal
description: "Generate D6: Proposal & Brief from all pipeline outputs. Invoke when the user says 'generate proposal', 'write proposal', 'run phase 6', 'create brief', or after Concept Creation is reviewed and approved."
allowed-tools: Read, Write, Glob, AskUserQuestion
version: 1.0.0
---

# Proposal & Brief Generation

Distill everything from Phases 1–5 into a single client-facing proposal. Evidence-based but readable — every section earns its place. The document is modular: the client sees cost and time impact of including or deferring specific functionality.

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 5 (Concept Creation) not complete, stop: "Run concept-creation first."

Read `D1-Init.json` for client name, project name, build_type, site_type.

### Step 2: Scan available files

Glob for all project files:
- `D1-Init.json`, `D2-Client-Intelligence.json`
- `research/R*-*.json`
- `gap-analysis/G*-*.json`
- `concept/C*-*.json`

Build the file list with names visible. Select which files to read based on their names — not all files are needed for every proposal section.

**ALWAYS read:**
- `D1-Init.json` (project parameters)
- `concept/C1-Sitemap.json` (sitemap with traffic estimates)
- `concept/C2-Functional.json` (functional requirements for module assembly)

**Read selectively** based on relevance to each proposal section:
- R-files and G-files for research findings extraction
- C3, C4, C5 for concept sections (tech stack, content strategy, visual direction)
- D2 for client profile context

### Step 3: Extract key findings

Read research R-files and extract the highest-value findings per research domain.

**Selection criteria:**
- Findings backed by numbers are prioritised over qualitative observations
- Findings with direct website implications are prioritised over general market context
- Maximum 3–5 bullet points per research domain
- Gaps and opportunities are prioritised over confirmations

Group findings into proposal-friendly categories: Search & SEO, Competitive Landscape, Market & Industry, Target Audience, Technology & Performance, Reputation & Trust, UX & Visual, Content.

### Step 4: Assemble modules

Build the scope of work from `concept/C2-Functional.json` functional requirements.

1. Group related requirements into work modules
2. Assign each module a category: strategy, design, frontend, backend, ecommerce, integration, content, seo, migration, multilingual, analytics, post-launch
3. Estimate hours per module based on complexity signals from C2
4. Set module phase: `launch` or `post-launch`
5. Set initial selection:
   - `must_have` requirements → `selected: true`
   - `should_have` and `nice_to_have` → `selected: false`
6. Note dependencies between modules

### Step 5: Calculate timeline

Build a phased timeline from selected modules and their dependencies. Output high-level phases with estimated durations — not a Gantt chart.

### Step 6: Summarise investment

Aggregate selected module hours into a total. Break down by module so the client sees exact cost impact of each scope decision.

### Step 7: Build executive summary

Write the executive summary last (it synthesises everything):
- Headline: one-sentence project positioning
- Project overview: 2–3 sentences on who, what, why
- Opportunity statement: what this website can achieve for the business
- Traffic potential from C1-Sitemap

### Step 8: Write D6

Write `D6-Proposal.json` as a single line (no newlines, no indentation, no spaces after colons or commas) using the schema below.
Write `D6-Proposal.md` from the JSON using the markdown template below.

### Step 9: Operator review

Present D6-Proposal.md for operator review. The operator may:
- Adjust module selection (toggle `selected` on/off)
- Edit hour estimates
- Add pricing, rates, or payment terms
- Modify text for client tone

If the operator makes changes, regenerate the affected sections (timeline, investment summary) and rewrite D6.

### Step 10: Update project-state.md

Update Phase 6 (Proposal & Brief) row:
- Status: `complete`
- Output: `D6-Proposal.json`
- Updated: today's date

Display summary:

```
Proposal complete.

  Modules: {selected}/{total} selected
  Total hours: {n}
  Traffic potential: {conservative}–{realistic}/mo (optimistic: {optimistic}/mo)
  Phase 6 status: complete

Pipeline complete. Deliver D6-Proposal.md to the client.
```

---

## JSON Schema

Write JSON as **minified** (no whitespace, no indentation).

```json
{
  "proposal": {
    "meta": {
      "date_run": "string",
      "client": "string",
      "project_name": "string",
      "prepared_by": "string | null",
      "version": "string"
    },
    "executive_summary": {
      "headline": "string",
      "project_overview": "string",
      "opportunity_statement": "string",
      "traffic_potential": {
        "conservative_monthly": "number",
        "realistic_monthly": "number",
        "optimistic_monthly": "number"
      }
    },
    "research_findings": [
      {
        "domain": "string (e.g. Search & SEO, Competitive Landscape)",
        "findings": [
          {
            "text": "string",
            "metric": "string | null"
          }
        ]
      }
    ],
    "modules": [
      {
        "id": "string",
        "name": "string",
        "category": "strategy | design | frontend | backend | ecommerce | integration | content | seo | migration | multilingual | analytics | post-launch",
        "description": "string",
        "inclusions": ["string"],
        "hours_est": "number",
        "complexity": "simple | moderate | complex",
        "dependencies": ["string (module id)"],
        "phase": "launch | post-launch",
        "priority": "must_have | should_have | nice_to_have",
        "selected": "boolean"
      }
    ],
    "timeline": [
      {
        "phase": "string",
        "description": "string",
        "duration": "string",
        "modules_included": ["string (module id)"]
      }
    ],
    "investment": {
      "modules_selected": ["string (module id)"],
      "total_hours": "number",
      "breakdown": [
        {
          "module_id": "string",
          "module_name": "string",
          "hours": "number"
        }
      ],
      "notes": "string | null"
    },
    "next_steps": ["string"],
    "notes": ["string"]
  }
}
```

Write to `D6-Proposal.json`.

---

## Markdown Template

Generate `D6-Proposal.md` from the JSON:

```markdown
# Website Proposal -- {Client Name}
*Prepared by {prepared_by} | {date} | Version {version}*

---

## Executive Summary

{project_overview}

{opportunity_statement}

**Organic traffic potential:** {conservative}–{realistic} visits/month at target rankings
*(optimistic scenario: {optimistic} visits/month at peak SEO performance)*

---

## Research Findings

### {domain}
- {finding text} {metric if available}
- {finding text}

*(repeat per domain)*

---

## Website Concept

### Positioning
{from C5 visual_direction.positioning_mood}

### Visual Direction
{from C5 — colour, typography, imagery summary}

### Tone of Voice
{from C4 content_strategy.tone_of_voice}
- *"{tone_example 1}"*
- *"{tone_example 2}"*

### Messaging Pillars
- **{pillar}** -- {description}

---

## Proposed Sitemap

**Organic traffic potential across all pages:**
Conservative {n}/mo -- Realistic {n}/mo -- Optimistic {n}/mo*

- **{Page Name}** `{path}` -- {conservative}–{realistic} visits/mo*
  - **{Child Page}** `{path}` -- {conservative}–{realistic} visits/mo*

*Theoretical organic traffic based on keyword search volume data and average CTR benchmarks.
Actual performance depends on SEO execution, content quality and competition.*

---

## Scope of Work

*Modules marked with a circle are optional -- included for consideration but can be deferred.*

### {Category} {checkmark or circle}
**{Module name}** -- {description}
Includes: {inclusions}
Estimated: {hours} hours

*(repeat per module, grouped by category)*

---

## Timeline

| Phase | Description | Duration |
|---|---|---|
| {phase} | {description} | {duration} |

**Estimated total duration:** {sum of durations}

---

## Investment Summary

| Module | Hours |
|---|---|
| {module name} | {hours} |
| **Total** | **{total_hours}** |

{investment notes if any}

---

## Next Steps

1. {next step}
2. {next step}
3. {next step}

---
```

---

## Writing Rules

<critical>
- **NEVER** fabricate findings, metrics, or traffic numbers — every data point must trace to a research or concept file
- **NEVER** include internal codes (R1, G05, C2) in the proposal text — this is a client-facing document
- **NEVER** include raw JSON or technical formatting in the proposal
- **ALWAYS** write for a business audience — lead with value and business impact, not technical detail
- **ALWAYS** present traffic estimates with the disclaimer that they are theoretical and depend on execution
- **ALWAYS** write JSON as a single line (no newlines, no indentation)
</critical>

- Skip research domains that have no meaningful findings (e.g., no reputation data found)
- Skip module categories that don't apply (e.g., no ecommerce section for a portfolio site)
- The operator may add pricing, rates, and payment terms manually — the agent does not generate pricing
- Hour estimates are directional — the operator validates before client delivery

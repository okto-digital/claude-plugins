---
name: proposal
description: "Generate D6: Proposal from all pipeline outputs (Phases 1-5). Produces JSON, Markdown, and branded HTML with print-ready CSS. Invoke when the user says 'generate proposal', 'write proposal', 'run phase 6', 'create brief', or after Concept Creation is reviewed and approved."
allowed-tools: Read, Write, Glob, AskUserQuestion
version: 2.0.0
---

# Proposal Generation

Distill everything from Phases 1-5 into a client-facing proposal with 9 sections. Evidence-based but readable. Modular -- the client sees cost and time impact of including or deferring specific functionality.

**Output:** `D6-Proposal.json` + `D6-Proposal.md` + `D6-Proposal.html`

**Proposal sections:**

| # | Section | Primary data source |
|---|---|---|
| 1 | Title Page | D1 meta |
| 2 | Executive Summary | Synthesis of all (written last) |
| 3 | Problem Statement | D2, R-files, G-files |
| 4 | Proposed Solution | C4, C5, C6, C8, C9 |
| 5 | Scope of Work & Deliverables | C2 modules + C1 sitemap |
| 6 | Timeline & Milestones | C7 roadmap + module dependencies |
| 7 | Investment | Module hours (operator adds rates) |
| 8 | About Us | Placeholder for operator |
| 9 | Conclusion & Acceptance | Next steps + signature block |

---

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 5 (Concept Creation) not complete, stop: "Run concept-creation first."

Read `D1-Init.json` for client name, project name, build_type, site_type, output_language.

### Step 2: Scan available files

Glob for all project files:
- `D1-Init.json`, `D2-Client-Intelligence.json`
- `research/R*-*.json`
- `gap-analysis/G*-*.json`
- `concept/C*-*.json`

**ALWAYS read:** D1-Init.json, C1-Sitemap.json, C2-Functional.json.

**Read selectively** based on relevance to each section:
- D2, R-files, G-files for problem statement evidence
- C4, C5, C6, C8, C9 for proposed solution narrative
- C3 for technical context (if relevant to scope)
- C7 for timeline and milestones

### Step 3: Build title page

Populate from D1-Init.json:
- `project_title` from project_name
- `client_name` from client
- `prepared_by` defaults to "oktodigital" if not set
- `date` is today
- `version` starts at "1.0"

### Step 4: Build problem statement

Read D2 (client profile), R-files (research), and G-files (gap analysis). Extract:

1. **Current situation** -- 2-3 sentences describing where the client is today. Draw from D2 web presence assessment and R-file findings about current site performance.
2. **Pain points** -- specific business problems the website should solve. Source from G-files (gaps identified) and D2 (weaknesses observed).
3. **Key challenges** -- obstacles or constraints (technical, market, competitive). Source from R-files.
4. **Evidence** -- grouped by research domain, max 3-5 findings per domain.

**Selection criteria for evidence:**
- Numbers over qualitative observations
- Direct website impact over general market context
- Gaps and opportunities over confirmations
- Skip domains with no meaningful findings

Group into: Search & SEO, Competitive Landscape, Market & Industry, Target Audience, Technology & Performance, Reputation & Trust, UX & Visual, Content.

### Step 5: Build proposed solution

Read C4 (content strategy), C5 (visual direction), C6 (UX strategy), C8 (SEO strategy), C9 (compliance). Synthesise into:

1. **Strategy overview** -- 2-3 paragraph narrative of the overall approach. Connect back to the pain points from Step 4. Write as a story, not a feature list.
2. **Methodology** -- how the project will be executed (discovery-driven, iterative, etc.)
3. **Desired outcome** -- what the finished website achieves for the business.
4. **Concept highlights** -- one-sentence client-friendly summaries:
   - Positioning (from C5 positioning_mood)
   - Visual direction (from C5 colour, typography, imagery)
   - Tone of voice (from C4 tone_of_voice)
   - UX approach (from C6 mobile_strategy, navigation, conversion_funnels)
   - SEO approach (from C8 link_acquisition, search_features)

### Step 6: Assemble scope of work

Build from `C2-Functional.json` functional requirements + embed sitemap from `C1-Sitemap.json`.

**Modules:**
1. Group related requirements into work modules
2. Assign category per the enum in `references/json-schema.md` (scope_of_work.modules[].category)
3. Estimate hours per module from C2 complexity signals
4. Set phase: `launch` or `post-launch`
5. Set selection: `must_have` = `selected: true`; `should_have` and `nice_to_have` = `selected: false`
6. Note dependencies between modules

**Sitemap summary:**
- Total page count from C1
- Aggregate traffic potential (conservative, realistic, optimistic)
- Page tree with per-page traffic estimates (recursive, arbitrary depth)

### Step 7: Calculate timeline

Read C7-Project-Roadmap.json. Build phased timeline from selected modules and dependencies.

- Map C7 phases to timeline entries with duration estimates
- Add milestones for key dates (content freeze, UAT, launch)
- Calculate total duration
- Output high-level phases -- not a Gantt chart

### Step 8: Summarise investment

Aggregate hours from `selected: true` modules. Break down by module with category so the client sees exact cost impact of each scope decision.

Set `pricing_note` to "To be completed by operator" -- the agent NEVER generates pricing.

### Step 9: Build executive summary

Write LAST (it synthesises everything):
- **Headline:** one-sentence project positioning
- **Project overview:** 2-3 sentences on who, what, why
- **Opportunity statement:** what this website achieves for the business
- **Traffic potential** from C1-Sitemap aggregate numbers

### Step 10: Write D6-Proposal.json

Write as **minified single-line JSON** (no newlines, no indentation, no spaces after colons or commas).

Use the schema from `${CLAUDE_PLUGIN_ROOT}/skills/proposal/references/json-schema.md`.

`about_us` fields use placeholder content: `company_intro` = "About [company name]...", arrays empty, `note` = "placeholder".

`conclusion.acceptance` fields are empty strings (rendered as signature lines).

### Step 11: Write D6-Proposal.md

Generate from D6-Proposal.json using the template in `${CLAUDE_PLUGIN_ROOT}/skills/proposal/references/markdown-template.md`.

Follow the rendering rules in that file (conditional sections, module grouping, sitemap tree nesting).

### Step 12: Write D6-Proposal.html

Read the HTML template at `${CLAUDE_PLUGIN_ROOT}/skills/proposal/references/html-template.html`. The template provides a complete CSS design system in `<head>` and a design brief in HTML comments -- the `<body>` is a blank canvas.

Generate the full page content creatively inside `<div class="page">`, composing sections from the pre-defined CSS components. Each proposal should be visually unique -- choose layouts, components, and emphasis based on the specific proposal content. Follow the design brief's required sections, component toolkit, creative direction, and hard rules.

Design tokens and brand elements are documented in `${CLAUDE_PLUGIN_ROOT}/skills/proposal/references/design-tokens.md`. Use the correct category colours for module borders and priority badges. Use bracket numbers, corner accents, stat blocks, visual timelines, and other brand elements where they enhance readability.

The HTML must be self-contained (inline CSS, embedded fonts). Verify all 9 sections are present and print CSS would produce clean page breaks.

### Step 13: Operator review

Present D6-Proposal.md for operator review. The operator may:
- Adjust module selection (toggle `selected` on/off)
- Edit hour estimates
- Add pricing, rates, or payment terms
- Modify text for client tone
- Fill in the About Us section

If changes are made, regenerate affected sections (timeline, investment) and rewrite all three D6 files.

### Step 14: Update project-state.md

Update Phase 6 (Proposal & Brief) row:
- Status: `complete`
- Output: `D6-Proposal.json`
- Updated: today's date

Display summary:

```
Proposal complete.

  Sections: 9
  Modules: {selected}/{total} selected
  Total hours: {n}
  Traffic potential: {conservative}-{realistic}/mo (optimistic: {optimistic}/mo)
  Output: D6-Proposal.json, D6-Proposal.md, D6-Proposal.html
  Phase 6 status: complete

Pipeline complete. Review D6-Proposal.html in browser (Cmd+P for PDF).
```

---

## Writing Rules

<critical>
- **NEVER** fabricate findings, metrics, or traffic numbers -- every data point must trace to a pipeline file
- **NEVER** include internal codes (R1, G05, C2, D2) in proposal text -- this is a client-facing document
- **NEVER** include raw JSON or technical formatting in the proposal
- **ALWAYS** write for a business audience -- lead with value and impact, not technical detail
- **ALWAYS** present traffic estimates with the disclaimer that they are theoretical and depend on execution
- **ALWAYS** write JSON as a single line (no newlines, no indentation)
- **ALWAYS** include the About Us placeholder notice for the operator
- **ALWAYS** include blank signature fields in the Conclusion section
</critical>

- Skip evidence domains that have no meaningful findings
- Skip module categories that don't apply (e.g., no ecommerce for a portfolio site)
- The operator adds pricing manually -- the agent does not generate pricing or rates
- Hour estimates are directional -- the operator validates before client delivery
- The strategy narrative in Proposed Solution should connect pain points to solutions -- avoid disconnected feature lists

---

## Reference Files

- `references/json-schema.md` -- D6 JSON schema (9-section structure), field notes, migration guide from v1.0.0
- `references/markdown-template.md` -- D6 markdown template with rendering rules
- `references/html-template.html` -- CSS design system + component library + design brief (blank canvas, not fixed layout)
- `references/design-tokens.md` -- oktodigital brand guide: palette, functional colours, bracket numbers, corner accents, grid motif, stat blocks, icons

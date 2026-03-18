---
name: proposal
description: "Generate D6: Proposal from concept outputs (Phase 5). Produces JSON, Markdown, and branded HTML with print-ready CSS. Invoke when the user says 'generate proposal', 'write proposal', 'run phase 6', 'create brief', or after Concept Creation is reviewed and approved."
allowed-tools: Read, Write, Glob, AskUserQuestion
version: 4.0.0
---

# Proposal Generation

Distill concept outputs (Phase 5) into a client-facing proposal with 9 sections. Evidence-based but readable. Modular -- the client sees cost and time impact of including or deferring specific functionality.

**Output:** `D6-Proposal.json` + `D6-Proposal.md` + `D6-Proposal.html`

**Proposal sections:**

| # | Section | Primary data source |
|---|---|---|
| 1 | Title Page | project.json |
| 2 | Executive Summary | Synthesis of all (written last) |
| 3 | Problem Statement | D5 concept sections (evidence already embedded) |
| 4 | Proposed Solution | D5 C4, C5, C6, C8, C9 sections |
| 5 | Scope of Work & Deliverables | D5 C1 sitemap + C2 functional requirements |
| 6 | Timeline & Milestones | D5 C7 project roadmap + module dependencies |
| 7 | Investment | Module hours (operator adds rates) |
| 8 | About Us | Placeholder for operator |
| 9 | Conclusion & Acceptance | Next steps + signature block |

---

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 5 (Concept Creation) not complete, stop: "Run concept-creation first."

Read `project.json` for client name, project name, build_type, site_type, output_language, pipeline_defaults.

**Proposal style:** Check `pipeline_defaults.proposal_style` — `"full"` (default behavior, all 9 sections + HTML), `"summary_only"` (skip Steps 10-12, produce JSON + MD only), or `"ask"` (prompt operator).

**Language:** `output_language` (e.g., `"sk"` = Slovak, `"en"` = English) determines the language for ALL client-facing text in D6. Every prose field in JSON, every sentence in Markdown, and every visible text element in HTML must be written in this language. JSON field names, technical identifiers, and internal codes stay in English.

### Step 2: Read concept data

**ALWAYS read:**
- `project.json` — project metadata, client name, output language, pipeline defaults
- `D5-Concept.txt` — concatenation of all 9 concept sections as scannable TXT

D5-Concept.txt contains up to 9 concept sections separated by `--- C{n}-{Slug} ---` headers. Each section is scannable TXT with `====` dividers, CAPS headers, `•` bullets, `Key: Value` pairs. If Phase 5 was partial (some sections skipped/failed), D5 will contain fewer than 9 — adapt the proposal to cover only the sections present.

The concept sections already contain all evidence from research and gap analysis — the proposal does NOT need to read upstream pipeline files (D2, D3, D4, R-files, baseline-log).

**Concept section quick reference:**
- **C1-Sitemap** — page tree with priorities, keywords, traffic estimates (SITEMAP SUMMARY + PAGE TREE)
- **C2-Functional** — functional requirements by priority and area (MUST HAVE / SHOULD HAVE / NICE TO HAVE)
- **C3-Technical-Architecture** — technology stack, hosting, integrations, operations
- **C4-Content-Strategy** — tone of voice, messaging pillars, SEO content plan
- **C5-Visual** — visual direction, colour/typography/imagery direction, references
- **C6-UX-Strategy** — navigation, conversion funnels, CTA strategy, user flows
- **C7-Project-Roadmap** — launch scope, phases, success metrics, risks
- **C8-SEO-Strategy** — link acquisition, local/international SEO, monitoring
- **C9-Compliance** — WCAG target, accessibility, legal, testing strategy

### Step 3: Build title page

Populate from project.json:
- `project_title` from project_name
- `client_name` from client
- `prepared_by` defaults to "oktodigital" if not set
- `date` is today
- `version` starts at "1.0"

### Step 4: Build problem statement

The concept sections are solution-oriented — they propose what SHOULD BE. Extract the problems by reading what the solutions address. Evidence is embedded via `[src: R/G codes]` and CONFIRMED/INFERRED tags. Build:

1. **Current situation** -- 2-3 sentences describing where the client is today. Infer from: C1 (keyword opportunities = current SEO gaps), C8 (SEO monitoring targets = current deficiencies), C3 (technology recommendations = current tech limitations), C9 (compliance targets = current compliance gaps).
2. **Pain points** -- specific business problems. Infer from: C2 (functional requirements = what's currently missing), C6 (conversion funnels = paths that don't exist yet), C1 (must-have pages = content gaps).
3. **Key challenges** -- obstacles or constraints. Source from: C3 NOTES (technical constraints), C7 RISKS section, C9 (compliance complexity).
4. **Evidence** -- grouped by concept domain, max 3-5 findings per domain. Extract CONFIRMED findings from within concept sections.

**Selection criteria for evidence:**
- Numbers over qualitative observations
- Direct website impact over general market context
- Gaps and opportunities over confirmations
- Skip domains with no meaningful findings

Group by concept domains: Sitemap & SEO (C1, C8), Functionality (C2), Technology (C3), Content & Voice (C4), Visual & UX (C5, C6), Compliance (C9).

### Step 5: Build proposed solution

Read C4, C5, C6, C8, C9 sections from D5-Concept.txt. Synthesise into:

1. **Strategy overview** -- 2-3 paragraph narrative of the overall approach. Connect back to the pain points from Step 4. Write as a story, not a feature list.
2. **Methodology** -- how the project will be executed (discovery-driven, iterative, etc.)
3. **Desired outcome** -- what the finished website achieves for the business.
4. **Concept highlights** -- one-sentence client-friendly summaries:
   - Positioning and visual direction (from C5 VISUAL DIRECTION section)
   - Tone of voice (from C4 TONE OF VOICE section)
   - UX approach, navigation, conversion strategy (from C6 sections)
   - SEO approach (from C8 sections)
   - Compliance targets (from C9 WCAG COMPLIANCE section)

### Step 6: Assemble scope of work

Build from C1-Sitemap and C2-Functional sections in D5-Concept.txt:

**Sitemap:** Extract from C1 PAGE TREE section:
- Total page count from SITEMAP SUMMARY
- Aggregate traffic potential (conservative, realistic, optimistic) from SITEMAP SUMMARY
- Page tree with per-page priorities, keywords, traffic estimates

**Functional requirements:** Extract from C2 MUST HAVE / SHOULD HAVE / NICE TO HAVE sections:
- Each requirement has area, description, source, complexity

**Modules:**
1. Group related requirements from C2 into work modules
2. Assign category per the enum in `references/json-schema.md` (scope_of_work.modules[].category)
3. Estimate hours per module from C2 complexity signals (simple/moderate/complex)
4. Set phase: `launch` or `post-launch`
5. Set selection: `must_have` = `selected: true`; `should_have` and `nice_to_have` = `selected: false`
6. Note dependencies between modules

### Step 7: Calculate timeline

Read C7-Project-Roadmap section from D5-Concept.txt. Extract PHASES and LAUNCH SCOPE. Build phased timeline from selected modules and dependencies.

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

Set `<html lang="...">` to the `output_language` value from project.json (e.g., `<html lang="sk">`). The template defaults to `lang="en"` -- always override it.

The HTML must be self-contained (inline CSS, embedded fonts). Verify all 9 sections are present and print CSS would produce clean page breaks.

### Step 13: Debug companion (when enabled)

If `debug` is `true` in project.json: write `tmp/debug/D6-Proposal-debug.txt` — section count, module counts (selected/total), total hours, traffic potential numbers, evidence domain counts, no prose.

### Step 14: Operator review

Present D6-Proposal.md for operator review. The operator may:
- Adjust module selection (toggle `selected` on/off)
- Edit hour estimates
- Add pricing, rates, or payment terms
- Modify text for client tone
- Fill in the About Us section

If changes are made, regenerate affected sections (timeline, investment) and rewrite all three D6 files.

### Step 15: Update project-state.md

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
- **NEVER** fabricate findings, metrics, or traffic numbers -- every data point must trace to a concept section
- **NEVER** include internal codes (R1, G05, C2, D2) in proposal text -- this is a client-facing document
- **NEVER** include raw JSON or technical formatting in the proposal
- **NEVER** read upstream pipeline files (D2, D3, D4, R-files, baseline-log) -- concept sections contain all needed data
- **ALWAYS** write for a business audience -- lead with value and impact, not technical detail
- **ALWAYS** present traffic estimates with the disclaimer that they are theoretical and depend on execution
- **ALWAYS** write JSON as a single line (no newlines, no indentation)
- **ALWAYS** include the About Us placeholder notice for the operator
- **ALWAYS** include blank signature fields in the Conclusion section
- **ALWAYS** write all client-facing text in the language specified by `output_language` from project.json -- section headings, prose, evidence summaries, module descriptions, timeline labels, everything the client reads. Only JSON field names and internal identifiers stay in English.
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

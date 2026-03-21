---
name: proposal
description: "Generate D6: Proposal from selected concept tier(s). Produces priced TXT proposal and branded HTML. Invoke when the user says 'generate proposal', 'write proposal', 'run phase 6', 'price the concepts', or after Concept Creation is reviewed and tier is selected."
allowed-tools: Read, Write, Glob, Bash, AskUserQuestion, Task
version: 5.0.0
---

# Proposal Generation

Turn a selected concept tier into a fully priced, deliverable proposal. The concept describes WHAT the client gets — the proposal describes HOW it's built and WHAT it costs.

**Output:** `D6-Proposal.txt` + `D6-Proposal.html`

---

## Process

### Step 1: Load project context

Read `project-state.md`. If Phase 5 (Concept Creation) is not complete, stop: "Run concept-creation first."

Read `project.json` for client name, output_language, pipeline_defaults.

### Step 2: Check existing outputs

Glob for `D6-Proposal.*`. If files exist, ask operator: "Proposal files already exist. Overwrite? (yes/no)"

### Step 3: Tier selection

List available concept files. Read each to extract page/template counts. Present to operator:

```
Available concepts:
  Tier 1 — Efficient: {pages} pages, {templates} templates
  Tier 2 — Competitive: {pages} pages, {templates} templates
  Tier 3 — Dominant: {pages} pages, {templates} templates

Generate proposal for:
  a) Single tier (specify 1, 2, or 3)
  b) All three tiers (comparison proposal)
```

Wait for operator selection.

### Step 4: Platform decision

Search D4 files for a resolved platform decision:
- `gap-analysis/confirmed.txt` — look for platform/CMS entries
- `D4-Scope-Implications.txt` — look for technology decisions

**If platform is resolved:** Use it. Display: "Platform: {platform} (from gap analysis)"

**If platform is NOT resolved:** Extract capability requirements from the selected concept's Client Independence dimension. Present options:

```
The concept requires: {capability list from concept}

Platform options:
  a) WordPress custom theme — full CMS, client self-manages, largest plugin ecosystem
  b) Static HTML/CSS — fastest performance, lowest hosting cost, agency manages all updates
  c) Static + git-based CMS (Hugo/11ty) — fast performance, basic client editing
  d) Webflow — visual editor, no-code client management
  e) Squarespace — template-based, limited customisation
  f) Other: ___
```

Wait for operator selection.

### Step 5: Dispatch proposal-creator

Read and inline these reference files:
- `${CLAUDE_PLUGIN_ROOT}/references/proposal-methodology.md`
- `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md`

Dispatch via Task tool:
- **Agent:** `${CLAUDE_PLUGIN_ROOT}/agents/proposal-creator.md`
- **Model:** opus
- **Prompt includes:**
  - Tier number(s) and platform decision
  - Inlined: proposal methodology, formatting rules
  - File paths: concept file(s), D4-Scope-Implications.txt, gap-analysis/confirmed.txt, baseline-log.txt, project.json, D5-Concept-Comparison.md (if comparison)
  - Output path: `D6-Proposal.txt`
  - Output language from project.json

### Step 6: Verify proposal output

Check D6-Proposal.txt exists and has content. Verify:
- All pricing sections present (A through F)
- Quality check results section present (all 12 checks)
- Total hours within sanity check range from pricing config

If verification fails, report issues to operator and offer to re-run.

### Step 7: Generate HTML proposal

Read `D6-Proposal.txt` for proposal content.

Read `${CLAUDE_PLUGIN_ROOT}/skills/proposal/references/html-template.html` for CSS design system and design brief.

Read `${CLAUDE_PLUGIN_ROOT}/skills/proposal/references/design-tokens.md` for brand guide.

Dispatch HTML generation via Task tool:
- **Model:** opus
- **Prompt:** Generate D6-Proposal.html from D6-Proposal.txt content using the HTML template's CSS design system and design brief. Follow the creative direction and hard rules in the template comments.
- **Include in prompt:**
  - Full content of D6-Proposal.txt
  - Full content of html-template.html
  - Full content of design-tokens.md
  - Output language: set `<html lang="{output_language}">`
  - All client-facing text in output_language
- **Output:** `D6-Proposal.html`

### Step 8: Operator review

Present summary:

```
Proposal complete.

  Tier: {N} — {Name} (or "Comparison — All Tiers")
  Platform: {platform}
  Pages: {count} ({templates} templates)
  Total hours: {hours}
  Quality checks: {pass count}/12 passed
  Output: D6-Proposal.txt, D6-Proposal.html

Review D6-Proposal.html in browser (Cmd+P for PDF).

The operator may:
  - Adjust hour estimates
  - Toggle extra services
  - Edit text for client tone
  - Add hourly rates (if set to 0 in pricing config)
  - Fill in Terms section
```

If operator makes changes, regenerate affected files.

### Step 9: Update project-state.md

Append to project-state.md:

```
| 6 Proposal | complete | {today} |

Proposal — complete.
  Tier: {N} — {Name}
  Platform: {platform}
  Total hours: {hours}
  Deliverables: D6-Proposal.txt, D6-Proposal.html
```

Display: "Phase 6 complete. Pipeline finished."

---

## Writing Rules

<critical>
- NEVER fabricate findings, metrics, or traffic numbers
- NEVER include internal codes (R1, G05, C-T1) in proposal text
- ALWAYS write for business audience — value + impact, not technical detail
- ALWAYS present traffic estimates with disclaimer
- ALWAYS write client-facing text in output_language from project.json
</critical>

- The agent calculates pricing using the pricing configuration — rates of 0 mean "set by operator"
- Hour estimates are directional — operator validates before delivery
- Extra services connect to research findings — no padding

---

## Reference Files

- `${CLAUDE_PLUGIN_ROOT}/references/proposal-methodology.md` — 10-step pricing process, assessment rules, quality checks. Contains pricing spreadsheet URL.
- `${CLAUDE_PLUGIN_ROOT}/references/formatting-rules.md` — scannable TXT output conventions
- `references/html-template.html` — CSS design system + component library + design brief
- `references/design-tokens.md` — oktodigital brand guide: palette, functional colours, typography, brand elements

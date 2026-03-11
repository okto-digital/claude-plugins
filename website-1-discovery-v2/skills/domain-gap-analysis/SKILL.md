---
name: domain-gap-analysis
description: "Run Phase 4 domain gap analysis: dispatch up to 21 domain-analyst agents in parallel, consolidate results with bash. Invoke when the user says 'run gap analysis', 'domain analysis', 'start phase 4', 'run domains', or after Research phase is complete."
allowed-tools: Read, Write, Bash, Glob, Task, AskUserQuestion
version: 1.0.0
---

# Domain Gap Analysis

Dispatch domain-analyst agents for up to 21 domains in parallel, then consolidate per-domain outputs into D4-Gap-Analysis using bash. Each domain is assessed independently against all available project research.

## Process

### Step 1: Load project context

Read `project-state.md`. Extract project info and document status.
If missing, stop: "Run project-init first."
If Phase 3 (Research) not complete, stop: "Run project-research first."

Read `D1-Init.json` for project parameters: client name, site_type, build_type, languages, notes.

### Step 2: Check existing domain outputs

Glob for `gap-analysis/G*-*.json` to find existing outputs.
Report: "Found X existing domain assessments: [list]. These will be skipped unless you want to re-run them."

### Step 3: Domain selection

Present all 21 domains grouped by activation type:

**Always active (15):**
accessibility, analytics-and-measurement, business-context, competitive-landscape, content-strategy, design-and-brand, forms-and-lead-capture, performance, post-launch, project-scope, security-and-compliance, seo-and-discoverability, site-structure, target-audience, technical-platform

**Conditional (6):**
- blog-and-editorial -- Content signals in research or notes
- booking-and-scheduling -- Service-based site types
- ecommerce -- `site_type: ecommerce`
- migration-and-redesign -- `build_type: redesign`
- multilingual -- Secondary languages present in INIT
- user-accounts -- Ecommerce or membership signals

Use AskUserQuestion with multiSelect=true. Pre-select all domains that don't have existing outputs. Note: "Conditional domains are dispatched with a conditional flag -- the agent checks applicability and returns INACTIVE if the domain doesn't apply."

### Step 4: Build available files list

Glob for all available project files to pass to domain analysts:
- `D1-Init.json`
- `D2-Client-Intelligence.json`
- `research/R*-*.json` (R1 through R9)

Only include files that actually exist. This list is passed to every domain-analyst so it can decide which files are relevant to its domain.

### Step 5: Dispatch domain analysts

Dispatch selected domains via the `dispatch-subagent` skill.

**Max concurrent: 3 agents.** All domains are independent -- no dependency ordering. Dispatch in batches of 3 until all selected domains are processed.

Each dispatch provides:
- Domain name (e.g., "business-context")
- G-code and slug (e.g., "G05", "Business") — see G-code mapping below
- Domain file path: `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/{domain-id}.md`
- Template file path: `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/templates/domain-output-template.md`
- Available project files: full list from Step 4
- Conditional flag: "yes" for the 6 conditional domains, "no" for always-active
- Model: sonnet
- MCP hints: none (domain analysis uses Read + Write only)

**Progress reporting after each batch:**
- Which domains completed (ACTIVE vs INACTIVE)
- Any failures

### Step 6: Consolidate with bash

After all domains complete, produce D4 with two bash operations.

**JSON consolidation:**

```bash
jq -s '{meta:{date:(now|todate),active_domains:[.[]|select(.status=="ACTIVE")|.domain],inactive_domains:[.[]|select(.status=="INACTIVE")|.domain],total_critical_unresolved:([.[]|select(.status=="ACTIVE")|(.counts.critical_total-.counts.critical_resolved)]|add//0),status:"awaiting_answers"},domains:.}' gap-analysis/G*-*.json > D4-Gap-Analysis.json
```

**Markdown consolidation:**

Read the just-created `D4-Gap-Analysis.json` to extract meta counts (active domains, critical unresolved). Read client name from `D1-Init.json`. Then:

1. Write the D4 header to `D4-Gap-Analysis.md`:

```
# Domain Gap Analysis -- {Client Name}
*Generated: {date} | Active domains: {active}/{total} | Critical unresolved: {n}*
*Answer all CRITICAL questions before proceeding to Concept Creation.*

---
```

2. Append all per-domain markdown files (G-codes sort naturally):

```bash
cat gap-analysis/G*-*.md >> D4-Gap-Analysis.md
```

3. Append footer:

```
---
*Return this document with all CRITICAL questions answered to proceed to Concept Creation.*
```

### Step 7: Update project-state.md

Update Phase 4 (Domain Gap Analysis) row:
- Status: `complete` (all domains processed) or `partial` (some skipped/failed)
- Output: `D4-Gap-Analysis.json`
- Updated: today's date

Display summary:

```
Domain Gap Analysis complete.

  Active domains: {n}
  Inactive domains: {n}
  Skipped: [list]
  Failed: [list or "none"]
  Total CRITICAL unresolved: {n}
  Phase 4 status: complete | partial

Next step: Answer CRITICAL questions in D4-Gap-Analysis.md, then run concept-creation.
```

## Rules

<critical>
- NEVER dispatch more than 3 domain-analyst agents concurrently
- NEVER modify project-state.md beyond Phase 4 rows
- NEVER read domain definition files directly -- leave this to the dispatched domain-analyst agents
- ALWAYS use dispatch-subagent skill for every domain-analyst dispatch
- ALWAYS provide the full list of available project files to each domain-analyst
- ALWAYS run bash consolidation after all domains complete
</critical>

- If a domain-analyst fails, note which domain was affected, report to operator, continue with remaining domains
- If fewer than 10 domains complete, warn that Phase 5 coverage will be limited

## Sub-agents

Dispatched via dispatch-subagent:
- **domain-analyst** -- Assess one domain, produce per-domain file pair (up to 21 instances, batches of 3)

## G-code Mapping

| Code | Domain ID | Slug | Conditional |
|---|---|---|---|
| G01 | accessibility | Accessibility | no |
| G02 | analytics-and-measurement | Analytics | no |
| G03 | blog-and-editorial | Blog | yes |
| G04 | booking-and-scheduling | Booking | yes |
| G05 | business-context | Business | no |
| G06 | competitive-landscape | Competitive | no |
| G07 | content-strategy | Content | no |
| G08 | design-and-brand | Design | no |
| G09 | ecommerce | Ecommerce | yes |
| G10 | forms-and-lead-capture | Forms | no |
| G11 | migration-and-redesign | Migration | yes |
| G12 | multilingual | Multilingual | yes |
| G13 | performance | Performance | no |
| G14 | post-launch | Post-Launch | no |
| G15 | project-scope | Project-Scope | no |
| G16 | security-and-compliance | Security | no |
| G17 | seo-and-discoverability | SEO | no |
| G18 | site-structure | Site-Structure | no |
| G19 | target-audience | Target-Audience | no |
| G20 | technical-platform | Technical | no |
| G21 | user-accounts | User-Accounts | yes |

## Reference files

Read by domain-analyst agents, not by this skill:
- `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/*.md` -- 21 domain checkpoint files
- `${CLAUDE_PLUGIN_ROOT}/agents/references/gap-domains/templates/domain-output-template.md` -- per-domain output template

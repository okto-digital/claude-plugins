# D6-Proposal -- Markdown Template

Generate `D6-Proposal.md` from `D6-Proposal.json`.

## Template

```markdown
# {title_page.project_title}

**Proposal for {title_page.client_name}**

*Prepared by {title_page.prepared_by} | {title_page.date} | Version {title_page.version}*

---

## Executive Summary

**{executive_summary.headline}**

{executive_summary.project_overview}

{executive_summary.opportunity_statement}

**Organic traffic potential:** {executive_summary.traffic_potential.conservative_monthly}–{executive_summary.traffic_potential.realistic_monthly} visits/month at target rankings
*(Optimistic scenario: {executive_summary.traffic_potential.optimistic_monthly} visits/month at peak SEO performance)*

---

## The Challenge

{problem_statement.current_situation}

**Key pain points:**
- {pain_point}

**Core challenges:**
- {challenge}

**What the research tells us:**

### {evidence.domain}
- {finding.text} {finding.metric if not null}

*(repeat per evidence domain; skip domains with no findings)*

---

## Our Approach

{proposed_solution.strategy_overview}

**Methodology:** {proposed_solution.methodology}

**What success looks like:** {proposed_solution.desired_outcome}

### Concept Highlights

- **Positioning:** {concept_highlights.positioning}
- **Visual direction:** {concept_highlights.visual_direction}
- **Tone of voice:** {concept_highlights.tone_of_voice}
- **User experience:** {concept_highlights.ux_approach}
- **Search strategy:** {concept_highlights.seo_approach}

---

## Scope of Work & Deliverables

*Modules marked [included] are in the proposed scope. Modules marked [optional] are available but can be deferred to a later phase.*

### Site Architecture

**{sitemap_summary.page_count} pages** — organic traffic potential: {sitemap_summary.traffic_potential.conservative_monthly}–{sitemap_summary.traffic_potential.realistic_monthly}/mo (optimistic: {sitemap_summary.traffic_potential.optimistic_monthly}/mo)*

- **{page.name}** `{page.path}` — {page.traffic_conservative}–{page.traffic_realistic} visits/mo
  - **{child.name}** `{child.path}` — {child.traffic_conservative}–{child.traffic_realistic} visits/mo

*Theoretical organic traffic based on keyword search volume data and average CTR benchmarks. Actual performance depends on SEO execution, content quality and competition.*

### {Category Name}

**{module.name}** [{included/optional}]
{module.description}
Includes: {inclusions joined with ", "}
Estimated: {hours_est} hours

*(repeat per module, grouped by category; skip empty categories)*

---

## Timeline & Milestones

| Phase | Description | Duration |
|---|---|---|
| {phase.name} | {phase.description} | {phase.duration} |

**Estimated total duration:** {timeline.total_duration}

### Key Milestones

| Milestone | Target | Description |
|---|---|---|
| {milestone.name} | {milestone.date_offset} | {milestone.description} |

*(omit milestones table if milestones array is empty)*

---

## Investment

| Module | Category | Hours |
|---|---|---|
| {breakdown.module_name} | {breakdown.category} | {breakdown.hours} |
| **Total** | | **{investment.total_hours}** |

{investment.pricing_note}

---

## About Us

{about_us.company_intro}

### Our Team
- {team_highlight}

### Selected Work
- {case_study}

*[OPERATOR: Complete this section before sending to client]*

---

## Conclusion

{conclusion.call_to_action}

### Next Steps
1. {next_step}

### Acceptance

| | |
|---|---|
| **Client** | _________________________ |
| **Date** | _________________________ |
| **Signature** | _________________________ |

---
```

## Rendering Rules

### Section ordering

Sections render in document order (1-9). Do not reorder.

### Conditional rendering

- Skip `evidence` domains with no findings
- Skip module categories with no modules in that category
- Skip milestones table if `milestones[]` is empty
- Skip `team_highlights` list if array is empty
- Skip `case_studies` list if array is empty

### Module display

- `selected: true` renders as `[included]`
- `selected: false` renders as `[optional]`
- Group modules by `category` in this display order (intentionally different from the schema enum order — groups client-facing categories first): strategy, design, content, seo, frontend, backend, ecommerce, integration, migration, multilingual, analytics, post-launch
- Category heading uses title case: "Strategy", "Design", "Content", etc.

### Sitemap tree

- Render as nested bulleted list
- Arbitrary nesting depth -- indent children with 2 spaces per level
- Traffic estimates on every node: `{page.traffic_conservative}–{page.traffic_realistic} visits/mo`

### About Us placeholder

Always include the `[OPERATOR: Complete this section before sending to client]` reminder, even if `company_intro` has content.

### Acceptance block

Render signature fields as underscored blank lines (25 underscores). These are for print; the HTML template renders them as input fields.

### Traffic disclaimer

Always append the italicised disclaimer after the sitemap tree. Never omit it.

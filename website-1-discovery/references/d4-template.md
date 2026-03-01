# Project Brief & Proposal -- Template

Output template for D4: Project Brief & Proposal. Used by the project-brief skill to structure the final client-facing document. Follow this structure exactly.

**Audience:** This document goes directly to the client. No internal codes (R1, D3), no gap/checkpoint language, no confidence scores, no intake questions. Written in second person ("your website", "your competitors") where natural.

---

## Frontmatter

```yaml
---
document_type: project-brief
document_id: D4
title: "Project Brief & Proposal -- [Company Name]"
project: "[client name from project-state.md]"
created: [YYYY-MM-DD]
created_by: website-1-discovery
status: complete
---
```

---

## Section 1: Executive Summary

One page max. The "if you read nothing else" section.

Cover in this order:
1. Who the client is (one sentence -- name, industry, core offering)
2. What the project is (redesign, new build, etc.)
3. What we propose (high-level approach in 2-3 sentences)
4. Expected outcome (the business result, not the deliverable)

**Tone:** Confident, concise, forward-looking. No hedging.

---

## Section 2: Current State Assessment

What we found about the client's current situation. Organized by what matters to the client, not by research topic.

### Sub-sections (include all that apply):

**Online Presence**
Website quality, content depth, structure, navigation, mobile experience. What works, what does not, what is missing.

**Search Visibility**
How findable they are online. Which queries they appear for, where they rank, local search presence, directory listings.

**Competitive Position**
Where they stand relative to competitors. Name competitors. Identify gaps and advantages.

**Technical Health**
Performance scores, technology choices, accessibility baseline, security posture. Only what matters to the business outcome.

**Reputation & Trust**
Reviews, ratings, directory presence, social proof, brand visibility online.

### Formatting rules:

- Each area: 2-3 paragraph narrative with specific evidence (numbers, competitor names, actual pages)
- No bullet-point dumps -- write prose
- End each area with a one-line **"Bottom line:"** statement summarizing the takeaway
- Skip any area that has no meaningful findings (e.g., skip "Technical Health" if the project is a new build with no existing site)

---

## Section 3: Key Findings

5-8 most important cross-topic insights that directly inform the proposal. These are patterns visible only by combining multiple research angles -- not a rehash of individual topic findings.

### Per-finding format:

**[Finding statement]** -- specific, evidence-backed, one sentence.

[Business impact] -- why this matters to the client's revenue, growth, or efficiency. 2-3 sentences max.

### Rules:

- Each finding must connect to evidence from the current state assessment or research
- Each finding must have a clear business implication
- Order by importance to the proposal (most impactful first)
- Do not repeat what was already stated in Section 2 verbatim -- synthesize and elevate

---

## Section 4: Proposed Solution

The core of the proposal. Organized by project phase.

### Which phases to include:

| Phase | Include when |
|---|---|
| Strategy & Architecture | Always |
| Design & Brand | Always |
| Content | Always |
| SEO & Discoverability | Always |
| Development & Technical | Always |
| Migration | Project type = redesign, or migration domain active |
| E-commerce | E-commerce domain active |
| Integrations | Booking, CRM, payment, or other integrations identified |
| Launch & Post-Launch | Always |

### Per-phase format:

**[Phase Name]**

For each applicable phase, list 3-6 specific actions. Each action:
- **What we'll do** -- specific action (not a vague promise)
- **Why** -- connected to a finding from Section 3 or observation from Section 2
- **Expected outcome** -- the business result the client can expect

### Example:

> **Design & Brand**
> - Redesign with mobile-first approach -- 73% of your audience searches on mobile, but your current site scores 35/100 on mobile performance vs the competitor average of 62. Expected: faster load times, lower bounce rate, better mobile conversion.
> - Implement consistent brand voice across all pages -- competitors use a formal, professional tone while your site mixes casual and technical language inconsistently. Expected: stronger brand recognition and trust.

### Rules:

- Every action must trace to evidence (finding, observation, or client-stated priority)
- Use specific numbers, competitor names, and page references where available
- Write in second person ("your site", "your competitors")
- No generic filler ("improve user experience", "optimize performance") without specifics

---

## Section 5: Scope & Timeline

Table format showing each applicable phase with deliverables, estimated hours, and timeline.

```markdown
| Phase | Key Deliverables | Est. Hours | Timeline |
|---|---|---|---|
| Strategy & Architecture | [specific deliverables] | [range] | [week range] |
| Design & Brand | [specific deliverables] | [range] | [week range] |
| Content | [specific deliverables] | [range] | [week range] |
| ... | ... | ... | ... |
```

### Rules:

- Hours are always ranges (e.g., "20-30h"), never single numbers
- Deliverables are specific to this project (not generic lists)
- Timeline assumes sequential phases with natural overlap
- Include only phases from Section 4 (same set)
- Total hours row at the bottom of the table

---

## Section 6: Total Hours Summary

One-line rollup of total estimated hours from the scope table.

If the project is large (total > 120h), optionally split into tiers:
- **MVP scope:** Core phases only, minimum viable site
- **Full scope:** All phases, complete vision

Hours only -- no pricing in this document.

---

## Section 7: Success Metrics

3-5 measurable KPIs tied to business goals.

### Per-metric format:

| Metric | Current Baseline | 6-Month Target |
|---|---|---|
| [what we measure] | [current value or "to be established"] | [realistic target] |

### Rules:

- Metrics must be measurable (not "improve brand perception")
- Baselines come from research findings where available
- Targets must be realistic based on the research (not aspirational guesses)
- Connect each metric to a business goal stated by the client or identified in research

---

## Section 8: Next Steps

2-3 concrete actions to move forward. Keep it short and actionable.

Example:
1. Review this brief and confirm the scope aligns with your priorities
2. Schedule a kickoff meeting to finalize timeline and assign responsibilities
3. Provide access to [specific assets: hosting, CMS, analytics, brand materials]

---

## Source Mapping Reference

Internal reference for the skill. Not included in the output document.

| D4 Section | Primary Sources |
|---|---|
| 1. Executive Summary | D1 (identity, project type), D3 (strategic summary) |
| 2. Current State Assessment | D1 sections 1.3-1.6, D3 topic summaries |
| 3. Key Findings | D3 executive summary, strategic opportunities |
| 4. Proposed Solution | D3 recommendations + proposal inputs, D1 active domains |
| 5. Scope & Timeline | Skill hour estimation logic + D1 complexity signals |
| 6. Total Hours Summary | Computed from Section 5 |
| 7. Success Metrics | D1 client priorities, D3 research baselines |
| 8. Next Steps | Standard + project-specific needs |

# D15 Research Report Template

Template for the consolidated research report produced by the consolidation step after all selected R-documents are complete.

---

## Frontmatter

```yaml
---
document_type: research-report
document_id: D15
title: "Research Report -- [Company Name]"
project: "[client name from registry]"
topics_completed: [R1, R3, R5, R7]
topics_skipped: [R2, R4, R6, R8]
created: [YYYY-MM-DD]
created_by: webtools-research
status: complete
---
```

**Field definitions:**

- `topics_completed`: List of R-document IDs that were produced and included
- `topics_skipped`: List of R-document IDs that were not selected or not completed

---

## Body Structure

### 1. Executive Summary

One page maximum. The 5-8 most important findings across all completed topics. What the operator must know before writing the proposal.

Write for a reader who will NOT read the individual R-documents. This section must stand alone as a briefing.

Structure as numbered findings, each 2-3 sentences:
```markdown
1. **[Finding title]** -- [Concise explanation with key data point]. [Implication for the project].

2. **[Finding title]** -- [Explanation]. [Implication].
```

### 2. Strategic Opportunities

Cross-cutting opportunities synthesized from MULTIPLE topics. Do not repeat single-topic findings -- synthesize across topics.

Each opportunity should reference which R-documents contributed:
```markdown
**[Opportunity title]** (R1 + R3 + R5)
[Description: what the data shows across topics, why it matters, how to leverage it]
```

Example:
```markdown
**Mobile-first differentiation** (R2 + R4 + R7)
Competitors neglect mobile UX (R2 surface scan shows 60% have poor mobile layouts; R4 benchmarks confirm industry-standard sites are mobile-first). Client's current site scores 45/100 mobile on PageSpeed (R7). A mobile-first redesign would leapfrog local competitors who all score 30-55.
```

### 3. Risk Factors

Cross-cutting risks or challenges the proposal should address. Same format as opportunities:
```markdown
**[Risk title]** (R-sources)
[Description: what the data shows, severity, suggested mitigation]
```

### 4. Topic Summaries

One sub-section per completed R-document. Pull the Key Findings section from each R-document and present under a heading:

```markdown
#### R1: SERP & Search Landscape

[Key Findings from R1, verbatim or lightly edited for flow]

#### R3: Audience & User Personas

[Key Findings from R3]
```

Skip sub-sections for topics not completed (they are listed in `topics_skipped` frontmatter).

### 5. Proposal Inputs

Concrete suggestions for the proposal. This is the bridge between research and proposal writing.

Structure by proposal section:
```markdown
**Problem statement / pain points:**
- [What to emphasize based on research findings]
- [Client pain points validated by external data]

**Proposed solution highlights:**
- [Features/approaches justified by research]
- [Competitive advantages to highlight]

**Differentiation arguments:**
- [What competitors do NOT do that this project will]
- [Market gaps identified]

**Risk mitigation / trust building:**
- [Concerns to address proactively]
- [Social proof or data points to include]

**Pricing / scope justification:**
- [Market benchmarks that justify the scope]
- [Competitive pricing signals if available]
```

### 6. Recommended Deep-Dives

Which existing webtools tools should run next and what to focus on. Each recommendation should be specific:

```markdown
**D3 -- SEO Keyword Map** (webtools-seo)
Focus on: [specific keyword clusters from R1], [intent types from R5]
Priority keywords: [list from SERP research]

**D5 -- Competitor Analysis** (webtools-competitors)
Deep-dive targets: [competitor A] and [competitor B] (selected from R2 landscape)
Reason: [why these competitors matter most]

**D6 -- Content Inventory** (webtools-inventory)
Recommended if: [condition, e.g., "redesign project with 50+ existing pages"]
Focus areas: [specific content types or sections from R5/R7 findings]
```

### 7. Appendix: Sources

Consolidated source list from all R-documents. De-duplicate URLs that appear in multiple topics. Group by topic:

```markdown
#### R1 Sources
1. [source from R1]
2. [source from R1]

#### R3 Sources
3. [source from R3]
```

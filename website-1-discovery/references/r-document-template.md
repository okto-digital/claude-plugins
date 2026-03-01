# R-Document Template

Shared template for all research topic documents (R1-R8). The researcher agent produces one document per domain following this structure.

---

## Frontmatter

```yaml
---
document_type: research-topic
document_id: R[N]
topic: "[topic name]"
title: "R[N] [Topic Name] -- [Company Name]"
project: "[client name from project-state, or 'standalone']"
sources_consulted: [number]
confidence: [high/medium/low]
created: [YYYY-MM-DD]
created_by: website-1-discovery
status: complete
---
```

**Field definitions:**

- `document_id`: R1 through R8, matching the topic ID
- `topic`: One of: SERP & Search Landscape, Competitor Landscape, Audience & User Personas, UX/UI Patterns & Benchmarks, Content Landscape & Strategy, Reputation & Social Proof, Technology & Performance, Industry & Market Context
- `sources_consulted`: Total number of distinct sources (URLs, documents, searches) consulted
- `confidence`: Overall confidence in findings -- high (3+ sources per key finding), medium (2 sources), low (single source or inference)

---

## Body Structure

### 1. Key Findings

3-5 bullet points summarizing the most important takeaways. These are what get pulled into D3.

Each finding should be:
- Specific (include numbers, names, evidence)
- Actionable (implication for the proposal is clear)
- Sourced (reference the source number in brackets, e.g., [3])

Example:
```markdown
- The top 3 ranking competitors for "[core service] [location]" are [A], [B], and [C]. All use long-form service pages (2000+ words) with integrated case studies. [1][3][5]
- No competitor in the local market offers a pricing calculator or interactive tool -- this is a differentiation opportunity. [2][4][7]
```

### 2. Detailed Findings

Organized by sub-topic as defined in the domain reference file. Each sub-section should include:
- What was found
- Evidence (quotes, data points, observations)
- Source references in brackets

Use sub-headings (###) for each sub-topic area.

### 3. Recommendations

3-8 specific, actionable recommendations for what the client should do, ordered by priority (highest impact first).

Each recommendation must:
- Connect to a finding from Detailed Findings (evidence-backed, not generic advice)
- Explain the expected business outcome (why this matters)
- Be concrete enough to act on

**Format:** **Action** -- Rationale. Expected outcome.

Example:
```markdown
1. **Create dedicated landing pages for each core service** -- Currently all services are on a single page, which dilutes SEO signal and makes it harder for visitors to find specific information. Expected: improved rankings for service-specific keywords and higher conversion per page. [3][5]
2. **Add a pricing calculator for renovation projects** -- No competitor offers an interactive estimation tool. Self-service pricing attracts high-intent visitors and pre-qualifies leads before contact. Expected: differentiation from all local competitors and reduced time on unqualified inquiries. [2][4][7]
```

This section is what makes each R-document directly proposal-ready -- the recommendations feed into D4 (Project Brief) as specific line items.

### 4. Opportunities & Risks

What this research suggests for the proposal. Split into:

**Opportunities:**
- Gaps found in competitors, market, or audience needs
- Advantages the client could leverage
- Quick wins visible from the research

**Risks:**
- Challenges the proposal should address upfront
- Competitive threats
- Market or audience factors working against the client

### 5. Confidence Notes

Transparency about research limitations:
- What could not be verified (and why)
- Findings based on single sources (flagged as lower confidence)
- Areas that need deeper investigation
- Data freshness concerns (oldest source dates)

### 6. Sources

Numbered list of all sources consulted. Each entry:
```markdown
1. [URL or search query] -- [brief description of what was found] ([date accessed or "search result"])
2. [URL] -- [description] ([date])
```

For WebSearch queries, format as:
```markdown
3. WebSearch: "[query]" -- [what the results revealed] ([date])
```

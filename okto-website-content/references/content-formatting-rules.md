# Content Formatting Rules

Heading hierarchy, content structure, and scan-pattern optimization for website content.

---

## Heading Hierarchy

### Rules

- **Exactly one H1** per page (from meta title or page title, not repeated in content body)
- **No skipped levels:** H1 -> H2 -> H3, never H1 -> H3
- **5-10 H2 sections** per page (ideal range)
- **Primary keyword in first H2**
- **Headings 8 words or fewer**
- **Descriptive headings** (not "Section 1" or "More Info")

### Why It Matters

- Google uses H1 as primary topic signal, H2/H3 to understand subtopics
- Screen readers use heading structure to navigate -- skipped levels break flow
- Pages with proper heading hierarchy rank higher on average

---

## Featured Snippet Optimization

### Snippet Types by Query Intent

| Query Intent | Snippet Format | Optimization |
|---|---|---|
| Definition ("What is...") | Paragraph | 40-60 word answer directly after H2 question |
| Steps ("How to...") | Numbered list | 3-10 steps with parallel structure, action verbs |
| Benefits/Features | Bulleted list | 3-10 items, concise, parallel structure |
| Comparison | Table | Clear headers, structured data |

### Tips

- Place snippet-optimized content within first 2-3 sections
- Use the question as the H2, answer immediately below
- Keep paragraph snippets to 40-60 words
- Use proper HTML structure (p, ul, ol, table)

---

## Progressive Disclosure

### Must Stay Visible (Never Hide)

- Primary value proposition
- Main content and primary keywords
- First 2-3 paragraphs
- All H2/H3 headlines
- Primary CTAs
- Key benefits overview

### Can Be Hidden (Accordions, Tabs, Read More)

- FAQ answers (keep questions visible)
- Technical specifications
- Supplementary explanations
- Historical context
- Advanced deep-dive sections
- Extended testimonials (keep headers visible)

**SEO note:** Hidden content is fully indexed as long as it exists in the HTML DOM. CSS display:none is fine. JavaScript-only loading is NOT indexed.

---

## TLDR / Key Takeaways

**When to include:** Content over 1,000 words

**Placement:** After 1-2 paragraph introduction, before main content

**Structure:**
```
## Key Takeaways

- **Primary benefit:** [With keyword, 15-30 words]
- **Secondary benefit:** [Actionable insight, 15-30 words]
- **Proof/credibility:** [Statistic or example, 15-30 words]
- **Call to learning:** [What reader will discover, 15-30 words]
```

**For B2B content:** Use "Executive Summary" label. Focus on ROI, efficiency, results. Include metrics.

---

## Scan Patterns

### F-Pattern (Blog Posts, Articles)

Users scan: horizontal across top (headline) -> vertical down left side (scanning subheadings) -> horizontal across middle if something catches attention.

**Optimize by:**
- Front-load important keywords in first sentence of each paragraph
- Use descriptive H2/H3 headings
- Place key benefits in scannable bullets
- Start paragraphs with topic sentences

### Z-Pattern (Landing Pages)

Users scan: top-left to top-right (header to CTA) -> diagonal to bottom-left -> bottom-left to bottom-right (footer to final CTA).

**Optimize by:**
- Logo top-left, primary CTA top-right
- Key benefit in center
- Final CTA bottom-right

---

## Quality Checklist

- [ ] Exactly one H1 (from page title, not in body)
- [ ] No skipped heading levels
- [ ] 5-10 H2 sections
- [ ] Primary keyword in first H2
- [ ] Headings 8 words or fewer
- [ ] TLDR present (if content >1,000 words)
- [ ] Paragraphs 2-3 sentences each
- [ ] Featured snippet opportunity identified and optimized
- [ ] TOC present (if content >1,500 words)

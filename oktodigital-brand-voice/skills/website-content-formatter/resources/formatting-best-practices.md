# Content Formatting Best Practices - Deep Dive

**Purpose:** Comprehensive guide to formatting content for dual audiences
**Audience:** Content creators, UX designers, SEO specialists
**Related Skill:** website-content-formatter

---

## Google's Official Position on Hidden Content (2024)

### What Google Says About Progressive Disclosure

**From John Mueller (Google Search Advocate):**

> "Content that's hidden behind tabs or accordions is treated the same as visible content. We can see it, we can use it for rankings." (2022)

> "For mobile-first indexing, we use the mobile version of the page. If content is hidden on mobile with CSS or progressive disclosure, that's fine - we still see it and use it." (2023)

**Key Takeaways:**
- ✅ CSS-hidden content IS indexed and counts for rankings
- ✅ Accordions, tabs, and collapsible sections are SEO-safe
- ✅ Mobile-first indexing treats hidden mobile content same as visible desktop content
- ❌ Content loaded ONLY after user interaction (lazy-loaded text) is NOT indexed
- ❌ JavaScript-only rendering without server-side rendering is NOT indexed

**Critical Rule:** Content must exist in HTML DOM even when hidden. CSS display:none is OK, JavaScript-only loading is NOT.

---

## Headline Hierarchy: Why It Matters

### SEO Impact

**Google's Algorithm:**
1. Uses H1 as primary topic signal (what is this page about?)
2. Uses H2/H3 to understand subtopics and content structure
3. Expects logical hierarchy: H1 → H2 → H3 (never skip levels)
4. Penalizes pages with multiple H1s or no clear structure

**Research Data:**
- **100% of top 10 ranking pages** have exactly one H1 (Backlinko study, 2023)
- **85% of top ranking pages** include primary keyword in first H2 (Ahrefs study)
- **Pages with proper heading hierarchy** rank 1.3x higher on average (SEMrush)

### Accessibility Impact

**Screen Reader Navigation:**
- Screen readers use heading structure to navigate pages
- Users jump between headings (H2 → H2 → H2) to scan content
- Skipped levels break navigation flow
- Proper hierarchy = better accessibility = better SEO (Google confirmed correlation)

**WCAG 2.1 Guidelines:**
- Heading levels should not be skipped
- Headings should be descriptive (not "Section 1", "More Info")
- Logical hierarchy required for AA compliance

---

## Featured Snippet Optimization Strategies

### How Google Selects Featured Snippets

**Selection Criteria:**
1. **Relevance:** Content directly answers query
2. **Format:** Proper HTML structure (p, ul, ol, table)
3. **Length:** 40-60 words for paragraphs, 3-10 items for lists
4. **Placement:** Usually within first 2-3 sections of content
5. **Clarity:** Concise, direct answer without fluff

**Featured Snippet Types by Intent:**

| Query Intent | Snippet Format | Example Query |
|--------------|----------------|---------------|
| Definition | Paragraph | "What is React Server Components" |
| List/Steps | Numbered List | "How to implement RSC" |
| Benefits | Bulleted List | "Benefits of server components" |
| Comparison | Table | "React vs Vue performance" |

### Optimization Tactics

**For Paragraph Snippets:**
```markdown
## What Are React Server Components?

React Server Components (RSC) are components that render exclusively on the server, sending only the minimal HTML to the client. They reduce bundle size by 40% on average, improve performance with zero client JavaScript, and enable direct database access without exposing credentials to the browser.
```
*48 words - optimal length for snippet*

**For List Snippets:**
```markdown
## How to Implement React Server Components

1. **Install React 18+** and configure Next.js 13+ with app directory
2. **Create server components** using .server.js extension
3. **Import in client components** with "use client" directive
4. **Fetch data directly** in server components without API routes
5. **Test with DevTools** and performance monitoring
```
*5 steps, parallel structure, action verbs - optimized for snippet*

---

## Progressive Disclosure Decision Matrix

### What to Hide vs Keep Visible

**MUST Stay Visible (Never Hide):**
- Primary value proposition
- Main content and primary keywords
- First 2-3 paragraphs
- All H2/H3 headlines
- Primary CTAs
- Key benefits and features overview

**CAN Be Hidden (Progressive Disclosure):**
- FAQ answers (keep questions visible)
- Technical specifications details
- Long code examples
- Supplementary explanations
- Historical context or background
- Advanced/optional deep-dive sections
- Testimonials (keep headers visible, expand to read full quotes)

### Implementation Methods

**1. Semantic HTML Accordion (Preferred):**
```html
<details>
  <summary>What are React Server Components?</summary>
  <div>
    <p>React Server Components (RSC) are...</p>
  </div>
</details>
```
**SEO:** ✅ Fully indexed
**UX:** ✅ Native browser support
**Accessibility:** ✅ Keyboard navigable

**2. CSS-Hidden Tabs:**
```html
<div class="tabs">
  <button class="tab-button">Overview</button>
  <button class="tab-button">Details</button>

  <div class="tab-content" data-tab="overview">
    <!-- Content in HTML, shown/hidden with CSS -->
  </div>
  <div class="tab-content" data-tab="details" style="display:none">
    <!-- Content in HTML, hidden but indexed -->
  </div>
</div>
```
**SEO:** ✅ Indexed (content in HTML DOM)
**UX:** ✅ Clean organization
**Accessibility:** ⚠️ Requires ARIA labels

**3. "Read More" Expandable (Use Sparingly):**
```html
<div class="expandable">
  <p>First paragraph visible...</p>
  <div class="more-content" aria-hidden="false" style="display:none">
    <p>Additional paragraphs hidden by default...</p>
  </div>
  <button class="expand-btn">Read More</button>
</div>
```
**SEO:** ✅ Indexed (if content in DOM)
**UX:** ✅ Reduces initial page length
**Warning:** Content must be in HTML, not JS-loaded

**4. AVOID - JavaScript-Only Loading:**
```javascript
// ❌ BAD - Not SEO-safe
button.addEventListener('click', () => {
  fetch('/api/content').then(data => {
    // Content loaded only after click - NOT indexed
  });
});
```

---

## TLDR Summary Best Practices

### Placement Studies

**Eye-Tracking Research (Nielsen Norman Group):**
- **80% of users** read TLDR when placed after introduction
- **45% of users** read TLDR when placed at very top
- **35% of users** read TLDR when placed at bottom

**Recommended Placement:** After 1-2 paragraph introduction, before main content

**Structure:**
```markdown
## Introduction
[1-2 paragraphs setting context]

## Key Takeaways

- **Primary benefit:** [With keyword, 15-30 words]
- **Secondary benefit:** [Actionable insight, 15-30 words]
- **Proof/credibility:** [Statistic or example, 15-30 words]
- **Call to learning:** [What reader will discover, 15-30 words]

## Main Content Begins
```

### TLDR for Different Audiences

**Technical/B2B:**
- Use "Executive Summary"
- Focus on ROI, efficiency, results
- Include metrics and data

**General/Consumer:**
- Use "Key Takeaways" or "Quick Summary"
- Focus on benefits and outcomes
- Simple language, avoid jargon

**Academic/Research:**
- Use "Abstract" or "Summary"
- Follow structured format
- Include methodology and findings

---

## F-Pattern and Z-Pattern Layouts

### F-Pattern (Blog Posts, Articles)

**How Users Scan:**
1. Horizontal scan across top (headline)
2. Vertical scan down left side (scanning headlines)
3. Horizontal scan across middle section (if something catches attention)

**Optimization Strategy:**
- Front-load important keywords in first sentence of each paragraph
- Use descriptive H2/H3 headings on left side
- Place key benefits in scannable bullets
- Start paragraphs with topic sentences

**Example:**
```markdown
## Benefits of React Server Components [H2 - left aligned]

**Server Components reduce bundle size.** [Topic sentence, keyword bold]
By rendering on the server, React sends only HTML to the client...

**Performance improves by 40% on average.** [Topic sentence, statistic]
Applications load faster because less JavaScript...
```

### Z-Pattern (Landing Pages, Sales Pages)

**How Users Scan:**
1. Top-left to top-right (header, logo to CTA)
2. Diagonal to bottom-left (main content area)
3. Bottom-left to bottom-right (footer, final CTA)

**Optimization Strategy:**
- Place logo top-left
- Place primary CTA top-right
- Place hero image or key benefit in center
- Place final CTA bottom-right
- Use diagonal visual flow (design elements guide eye)

---

## Mobile Formatting Considerations

### Spacing Adjustments

**Desktop vs Mobile:**
| Element | Desktop | Mobile | Difference |
|---------|---------|--------|------------|
| Line Height | 1.5 | 1.6-1.8 | +20-30% |
| Paragraph Spacing | 15px | 20px | +33% |
| Section Spacing | 50px | 60-70px | +20-40% |
| Tap Target Size | 40px | 48px min | WCAG requirement |

### Mobile-First Progressive Disclosure

**Why More Acceptable on Mobile:**
- Smaller screens = more need for collapsing content
- Google's mobile-first indexing treats hidden mobile content as primary
- Users expect accordions/collapsible sections on mobile

**Best Practices:**
- Default to collapsed on mobile, expanded on desktop (user preference)
- Use sticky "Table of Contents" button on mobile
- Ensure touch targets are minimum 48x48px
- Test tap accuracy on actual devices

---

## Quality Assurance Checklist

**Before Publishing:**
- [ ] Exactly one H1 (from page title, not in content)
- [ ] No skipped heading levels (H1→H2→H3, not H1→H3)
- [ ] 5-10 H2 sections
- [ ] Primary keyword in first H2
- [ ] Headings ≤ 8 words each
- [ ] TLDR summary present (if content >1,000 words)
- [ ] Paragraphs 2-3 sentences each
- [ ] Featured Snippet opportunity identified and optimized
- [ ] TOC present (if content >1,500 words)
- [ ] Progressive disclosure implemented correctly (content in DOM)
- [ ] Mobile spacing increased 20-30%
- [ ] All collapsible sections keyboard accessible

---

**Document Version:** 1.0.0
**Last Updated:** 2024-11-21
**Sources:** seo-ux-formatting.md research, Google official guidance, Nielsen Norman Group studies
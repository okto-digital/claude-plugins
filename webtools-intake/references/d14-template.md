# D14 Client Research Profile -- Template

Output template for D14 client research. Used by PREP's inline research phase. Follow this structure exactly.

---

## Frontmatter

```yaml
---
document_type: client-research-profile
document_id: D14
title: "Client Research Profile -- [Company Name]"
source_url: "[homepage URL as provided by operator]"
final_url: "[actual URL after redirects]"
pages_analyzed: [number]
pages_failed: [number]
web_searches_completed: [number]
registry_source: "[finstat.sk / dnb.com / none]"
project: "[client name from registry, or 'standalone']"
created: [today]
created_by: webtools-intake
status: complete
---
```

---

## Report Body

### 1. Executive Summary

2-3 sentences. Cover: who (name, industry), what (core offering), who they serve, scale (headcount, revenue range, geography). No padding.

---

### 1b. External Intelligence

**Maps to PREP conversation topics:** The Business + The Audience

Flat bullet list of notable findings only. Each bullet: `Source: finding`. Skip empty categories entirely.

Categories to check (include only those with findings):
- Recent news/press (with dates)
- Review ratings and themes
- Social presence (platforms, follower ranges)
- Job postings revealing growth/tech/strategy
- Industry rankings or awards

---

### 3. Business Identity

**Maps to PREP conversation topic:** The Business

Use key-value and inline formats:

- **Name / tagline:** As stated on site
- **Positioning:** Their self-description in one line
- **Services:** Comma-separated list (not bulleted sub-items)
- **Value props:** Comma-separated claims
- **Model:** B2B | B2C | hybrid. Sales model in one phrase.
- **Trust signals:** Certifications, awards, partnerships as comma list
- **History:** Founded date, key milestones as comma list
- **Financial profile:** Single compact block -- Source | Entity name | ID | Founded | Legal form | Revenue | Profit indicator | Employees | Address. If lookup failed: "Registry data not found"

---

### 4. Market and Audience Signals

**Maps to PREP conversation topic:** The Audience

3-5 bullets max. Cover: primary audience, segments/industries served, geography/service area. Add named clients or case study patterns only if notable. Omit sub-items with no findings.

---

### 5. Current Website Assessment

**Maps to PREP conversation topics:** The Website Vision + Technical Foundation

One line per aspect. Report problems only -- skip clean items (do not report "SSL present", "responsive layout works"). Only note an item if there is something noteworthy (issue, gap, or unusual tech choice).

- **Structure:** Total pages, nav depth, primary sections
- **Content:** Blog frequency, last update, thin/deep areas
- **Tech:** CMS, frameworks, hosting clues
- **Issues:** Broken links, redirects, accessibility gaps, performance problems

---

### 6. Brand and Communication Style

**Maps to PREP conversation topic:** Look and Feel

Single line of descriptors: `Visual: X | Tone: Y | Photography: Z | Colors: X | Type: Y`

Expand only if inconsistencies found across pages (note which pages differ).

---

### 7. Digital Presence

**Maps to PREP conversation topics:** Findability + Lead Capture

- **Social:** Comma-separated platform list
- **SEO:** One-line assessment (meta quality, heading structure, schema presence, content depth)
- **Conversion elements:** Comma-separated list of what was found (contact form, phone, chat, newsletter, etc.)
- **Analytics:** Tracking tools observed

Note: Interactive features (booking systems, live chat, configurators) may not appear in crawled content. Report what IS found; flag unconfirmed items as "not confirmed from static analysis."

---

### 8. Competitive Context

**Maps to PREP conversation topic:** Competitive Landscape

**Competitors:** One line each -- `Name (URL): positioning summary`

List 3-5 direct competitors. Add market density in one line.

**Client positioning:** `Positioning: premium|budget, specialist|generalist, local|national` + differentiation claim in one line.

If competitor search yielded no clear results, state what was searched and why results were inconclusive.

---

### 9. Conversation Starters

**Highest-value section.** Not a summary -- analytical synthesis.

5-8 starters in a single numbered list. One line each. Prioritize the sharpest observations: contradictions, gaps, pain points, unanswered questions. Each must be something the operator can say or ask in the meeting, grounded in a specific observation.

Good: "Your case studies page shows 3 projects, but the homepage says '50+ completed.' Are there more projects we can showcase on the new site?"

Bad: "Ask about their case studies."

---

## Section-to-Topic Mapping Reference

This table shows how D14 sections feed into the PREP mode conversation topics, ensuring seamless data flow through the intake pipeline:

| D14 Section | PREP Conversation Topic |
|---|---|
| 1b. External Intelligence | The Business, The Audience |
| 3. Business Identity | The Business |
| 4. Market and Audience Signals | The Audience |
| 5. Current Website Assessment | The Website Vision, Technical Foundation |
| 6. Brand and Communication Style | Look and Feel |
| 7. Digital Presence | Findability, Lead Capture and Conversion |
| 8. Competitive Context | The Business (competitive sub-topic) |
| 9. Conversation Starters | Cross-cutting (used throughout PREP) |

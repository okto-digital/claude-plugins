# D14 Client Research Profile -- Template

Output template for the client-researcher skill. Follow this structure exactly.

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

One paragraph. Cover:
- Who the company is (name, industry)
- What they do (core offering in plain language)
- Who they serve (primary audience)
- Company size estimate (team page headcount, office locations, service area scope)
- Financial scale indicators (revenue range, employee count -- from registry if available)
- Geographic scope (local, regional, national, international)
- External reputation signals (review ratings, notable press mentions -- from web search if available)

Do not pad with filler. If specific details are unknown, omit them rather than hedging.

---

### 1b. External Intelligence

**Sources:** Web search, review sites, social profiles, news articles, job postings

**Maps to PREP conversation topics:** The Business + The Audience

Extract and organize findings from the web search step:

- **Recent news and press:** Notable mentions, awards, partnerships, funding (with dates and sources)
- **Online reputation:** Review site ratings and recurring themes (Google Business, Trustpilot, Clutch, G2, etc.)
- **Social presence:** Active platforms, follower ranges, posting frequency, engagement quality
- **Job postings:** Open positions that reveal growth areas, tech stack, or strategic priorities
- **Industry context:** Market position signals from third-party sources (rankings, directories, awards)

Each finding must include the source (site name or search result context). Do not fabricate findings -- if a category has no results, state "No indicators found in web search."

---

### 3. Business Identity

**Maps to PREP conversation topic:** The Business

Extract and organize:

- **Company name and tagline:** As stated on the site
- **Positioning statement:** How they describe themselves (e.g., "leading provider of...", "boutique agency specializing in...")
- **Core services/products:** Bulleted list of what they offer, as categorized on their site
- **Value propositions:** What benefits they claim (speed, quality, price, expertise, etc.)
- **Business model indicators:** B2B, B2C, or hybrid. Direct sales, referral-based, subscription, project-based, etc.
- **Certifications, awards, partnerships:** Any trust signals displayed on the site
- **Company history indicators:** Founded date, milestones, growth markers if mentioned
- **Financial profile (from business registry):**
  - Source: finstat.sk or dnb.com (state which was used)
  - Legal entity name and ID (ICO for Slovak entities)
  - Founded / year established
  - Legal form (s.r.o., a.s., LLC, etc.)
  - Revenue (latest available year)
  - Profit/loss indicator
  - Employee count or range
  - Registered address
  - If registry lookup failed or was not performed, state: "Registry data not found"

If a sub-item has no findings, omit it entirely (do not write "Not found"). Exception: the financial profile sub-section should state "Registry data not found" when the lookup failed, so PREP mode knows the data was attempted but unavailable.

---

### 4. Market and Audience Signals

**Maps to PREP conversation topic:** The Audience

Extract and organize:

- **Primary target audience:** Who the website speaks to, based on language, imagery, and CTAs
- **Industries or segments mentioned:** Client types listed in case studies, testimonials, or service descriptions
- **Case study insights:** What case studies reveal about typical project size, industry, and outcomes
- **Testimonial insights:** What testimonials reveal about client satisfaction drivers and relationship style
- **Service areas:** Geographic regions, office locations, or "serving [area]" statements
- **Client logos or named clients:** Companies displayed as social proof

---

### 5. Current Website Assessment

**Maps to PREP conversation topics:** The Website Vision + Technical Foundation

Extract and organize:

- **Site structure summary:** Total pages discovered, navigation depth, primary sections
- **Content maturity:** Blog post frequency, last update dates (if visible), content depth per section
- **Technology indicators:** CMS clues (meta generator tag, URL patterns, login URLs), JavaScript frameworks, hosting clues
- **Mobile responsiveness:** Whether the site has a responsive layout (viewport meta tag, responsive CSS indicators)
- **SSL status:** HTTPS present or absent
- **Performance indicators:** Page load observations, image optimization, minified assets
- **Accessibility indicators:** Alt text presence, heading hierarchy, ARIA attributes, color contrast (surface-level only)
- **Notable structural issues:** Broken links encountered, 404 pages, redirect chains, orphaned pages

---

### 6. Brand and Communication Style

**Maps to PREP conversation topic:** Look and Feel

Extract and organize:

- **Visual style:** Modern/traditional, minimal/rich, corporate/creative, dark/light
- **Tone of voice:** Formal/casual, technical/accessible, authoritative/friendly
- **Photography style:** Stock photography, custom photography, illustrations, icons, mixed
- **Color palette indicators:** Primary colors observed (describe, do not extract hex codes)
- **Typography indicators:** Serif/sans-serif, font weight usage, heading style
- **Consistency:** Does the visual style and tone stay consistent across pages, or does it vary?

---

### 7. Digital Presence

**Maps to PREP conversation topics:** Findability + Lead Capture

Extract and organize:

- **Social media links:** Which platforms are linked from the site (list platform names only)
- **SEO indicators:**
  - Meta title and description presence and quality (are they unique per page or duplicate?)
  - Heading structure quality (proper H1-H6 hierarchy?)
  - Content depth (thin pages vs. substantial content)
  - Schema markup presence (check for JSON-LD or microdata)
- **Forms and conversion elements:**
  - Contact forms (location, fields, CTA text)
  - Newsletter signup
  - Quote/estimate request forms
  - Live chat or chatbot
  - Phone number prominence
  - Other conversion mechanisms
- **Analytics indicators:** Google Analytics, Tag Manager, or other tracking scripts observed

---

### 8. Competitive Context

**Maps to PREP conversation topic:** Competitive Landscape

Extract and organize:

- **Competitors referenced on the site:** Any direct mentions of competitors (rare but worth noting)
- **Industry positioning:** Premium/budget, specialist/generalist, local/national, established/startup
- **Differentiation claims:** What the site says makes them different from alternatives
- **Market segment indicators:** Based on service descriptions, pricing signals, and client types

This section is often the thinnest because websites rarely reference competitors directly. Focus on positioning signals rather than explicit competitor mentions.

---

### 9. Conversation Starters

**This is the highest-value section.** Do not summarize the above sections. Synthesize analytical observations that are actionable in the meeting.

Organize into four categories:

**Key observations worth discussing:**
- Notable strengths of the current site (acknowledge what works)
- Impressive elements that reveal company priorities
- Things that suggest the company is ready for a redesign

**Potential pain points inferred from the website:**
- Outdated design elements or technology
- Content that appears stale or incomplete
- Missing pages that businesses in this industry typically have
- Poor mobile experience or accessibility gaps
- Weak conversion paths (no clear CTAs, buried contact info)

**Questions the website raises but does not answer:**
- Claims without evidence (e.g., "industry leading" but no case studies)
- Services listed but not explained
- Target audience unclear from the site alone
- Missing pricing, process, or timeline information

**Contradictions or inconsistencies noticed:**
- Visual quality vs. content quality mismatch
- Claims vs. evidence mismatch (e.g., "modern solutions" on a dated site)
- Inconsistent branding across pages
- Navigation structure vs. business priorities mismatch
- External reputation vs. website claims mismatch (from web search findings)

Write each conversation starter as something the operator can say or ask in the meeting. Use concrete observations, not vague suggestions.

Good example: "Your case studies page shows 3 projects, but the homepage says '50+ completed.' Are there more projects we can showcase on the new site?"

Bad example: "Ask about their case studies." (too vague, not grounded in observation)

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

# Substage 3.5 — Technology & Performance

**Code:** R5
**Slug:** Technology
**Output:** `research/R5-Technology.txt`
**Hypothesis:** Current site is technically adequate but has specific performance or accessibility gaps
**Dependencies:** R3-Competitors
**Reads from:** `project.json`, `baseline-log.txt`, `research/R3-Competitors.txt`
**MCP tools:** DataForSEO (required), web-crawler (optional)

---

## Purpose

Audit the technical foundation of the client website, competitors rank 1–3, and any reference sites from INIT notes. Covers technology stack, Core Web Vitals, Lighthouse scores, WCAG accessibility compliance, and GDPR surface scan. Findings are compared across all analysed sites to identify where the client stands technically and what the proposal should recommend.

Analysis is performed on the homepage plus max 3 subpages per site (conversion page, category page, secondary landing page).

**Important:** This is a surface scan, not a certified audit. WCAG findings flag critical violations at AA level. GDPR findings flag visible compliance signals only — not a legal assessment.

---

## Data Sources

From `project.json`: site type, notes (reference site URLs).
From `baseline-log.txt`: mission, client URL, all prior findings including D2 and R3 highlights.
From `research/R3-Competitors.txt`: competitor ranks 1–3 URLs and domains (all locked competitors when `deep`).

---

## Scope

| Site | Type | Pages Analysed |
|---|---|---|
| Client | Full analysis | Homepage + max 3 subpages |
| Competitors rank 1–3 | Full analysis | Homepage + max 3 subpages |
| Reference sites (INIT) | Tech + performance only, no gap analysis | Homepage + max 3 subpages |

When `research_depth` = `deep`: expand to all locked competitors from R3, not just ranks 1–3.

---

## Methodology

### Step 1: Subpage selection

For each site, identify the 3 most representative subpages by crawling the site structure. Priority order:
1. Primary conversion page (product, pricing, booking, contact)
2. Category or content page (if exists)
3. Other high value page (portfolio, FAQ, landing page, about page)

Log selected pages in the output.

### Step 2: Technology stack detection

Call `domain_analytics_technologies_domain_technologies` per domain (not per page). Returns full technology stack including CMS, frameworks, hosting signals, analytics tools, marketing tools, CDN, SSL status.

### Step 3: Performance and on-page analysis

Call `on_page_lighthouse` per page (homepage + up to 3 subpages per site) for Lighthouse scores (performance, accessibility, best practices, SEO — 0–100). Call `on_page_instant_pages` per page for Core Web Vitals (LCP, INP, CLS, TTFB) and on-page signals (meta tags, headings, image optimisation, mobile readiness).

### Step 4: WCAG accessibility surface scan

From the Lighthouse accessibility score, flag:
- Overall accessibility score
- Critical violations at WCAG AA level
- Missing alt text, contrast issues, keyboard navigation signals
- Mobile accessibility signals

Note as surface scan only — not a certified WCAG audit.

### Step 5: GDPR surface scan

Dispatch `web-crawler` sub-agent to check each site for:
- Cookie consent banner — present, type (opt-in vs opt-out), compliant appearance
- Privacy policy — present and accessible from homepage
- Visible third-party tracking scripts — analytics, advertising, social pixels
- Data collection transparency signals

If web-crawler is unavailable, use WebSearch to check privacy pages directly.

Note as surface scan only — not a legal assessment.

### Step 6: Gap analysis

Compare client against analysed competitors and reference sites. Synthesise across sites — don't restate per-site findings. Cover tech stack, performance, accessibility, and GDPR together.

---

## Output

Write `research/R5-Technology.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R5]`.

Concept Creation reads gap analysis opportunities and tech stack for technology recommendations. Proposal reads WCAG, GDPR and gap analysis gaps for compliance and technical recommendations.

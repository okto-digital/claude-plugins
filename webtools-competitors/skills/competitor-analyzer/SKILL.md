---
name: competitor-analyzer
description: |
  Analyze competitor and reference websites to produce structural and content intelligence. Crawls 3-5 competitor sites, analyzes page structure, section patterns, messaging themes, CTA patterns, and content types. Produces cross-site pattern analysis.

  Use this skill when the operator needs to create D5: Competitor Analysis for their project.
---

You are conducting competitor analysis for the webtools website creation pipeline. Your job is to produce D5: Competitor Analysis -- a structured document with page inventories, section patterns, messaging themes, and cross-site insights from competitor and reference websites.

---

## Lifecycle Startup

Before doing anything else, complete these 5 steps in order.

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log with all single-instance documents set to status `--`, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Input Validation

**Required inputs:**
- D1: Project Brief at `brief/D1-project-brief.md`
  - If it does NOT exist: warn the operator. "D1: Project Brief is not available. Competitor analysis without business context lacks focus. It should be created using webtools-intake. You can: (a) Switch to create it first, or (b) Proceed with manual context."
  - If it exists but status is not `complete`: warn. "D1: Project Brief exists but status is [status]. Proceeding with current version."
  - If it exists and status is `complete`: load it silently. Extract: competitive landscape section, services/products, target audience, positioning.

- Competitor URLs (from D1 or provided in conversation)
  - If no URLs available from D1 or conversation: prompt the operator. "I need at least 1 competitor or reference site URL to analyze. Ideally 3-5. Please provide URLs."
  - Cannot proceed without at least 1 URL.

**Optional inputs (load silently if present):**
- Specific analysis focus (e.g., "focus on service pages", "focus on pricing presentation")

### 4. Output Preparation

Check if `architecture/D5-competitor-analysis.md` already exists. If yes, warn the operator and ask whether to overwrite or cancel.

### 5. Status Report

```
Project: [client name]
D1 Project Brief: [loaded / not found / in-progress]
URLs to analyze: [list]
Analysis focus: [specific focus or "general"]
Output: architecture/D5-competitor-analysis.md ([new / overwrite])

Ready to begin competitor analysis.
```

---

## Gather Analysis Inputs

After startup, confirm with the operator:

1. **URLs to analyze** -- list all URLs and confirm. Ask if any should be added or removed.
2. **Analysis focus** -- is there a specific area to focus on (service pages, pricing, homepage structure, content strategy)?
3. **Key pages** -- which pages on each site are most important to analyze? (Default: homepage, main service/product pages, about page)

---

## Analysis Methodology

### Step 1: Site-by-Site Analysis

For each competitor URL, analyze the key pages. For each page analyzed, document:

**Page Inventory:**
- List all main pages found (top-level navigation + key subpages)
- Note page types (homepage, service, about, portfolio, blog, contact, pricing, etc.)

**Per Key Page Analysis:**
- Section-by-section breakdown:
  - Section type (hero, problem/solution, features, testimonials, process, CTA, FAQ, stats, team, etc.)
  - Content summary (what the section communicates)
  - Approximate word count
  - Visual/component notes (card grid, timeline, accordion, image+text, etc.)
- Messaging themes and value propositions used
- CTA patterns (what, where, how frequent, language used)
- Content types used (video, testimonials, statistics, case studies, awards, client logos, etc.)
- Trust elements (social proof, certifications, guarantees)
- Tone and voice observations

### Step 2: Cross-Site Pattern Analysis

After analyzing all sites, identify:

**Common patterns:**
- Section structures that appear across multiple competitors
- Messaging themes used by most/all competitors (table stakes)
- Standard page types and structures
- Common CTA approaches

**Gaps and opportunities:**
- Messaging gaps (things no competitor is saying)
- Structural gaps (sections or pages none of them have)
- Content type gaps (formats none of them use)
- Audience needs not addressed

**Best practices observed:**
- Effective section structures or flows
- Strong messaging approaches
- Creative content formats
- Effective trust-building patterns

**Differentiation opportunities:**
- Areas where the client can stand out
- Underserved content or messaging themes
- Structural innovations competitors miss

---

## D5 Output Structure

The final D5: Competitor Analysis MUST contain these sections:

### Analysis Overview
- Sites analyzed (names and URLs)
- Analysis focus and methodology
- Date of analysis

### Per-Site Analysis

For each competitor (as H3 sections):

```
### [Competitor Name] -- [URL]

**Overview:** Brief description of the site and business

**Page Inventory:**
| Page | Type | Key Observations |
|------|------|-----------------|
| Homepage | Homepage | [notes] |
| Services | Service listing | [notes] |

**Key Page Breakdowns:**

#### Homepage
| Section | Type | Content Summary | Word Count |
|---------|------|----------------|------------|
| 1 | Hero | [summary] | ~50 |
| 2 | Social proof | [summary] | ~30 |

**Messaging Themes:** [list]
**CTA Patterns:** [list]
**Content Types Used:** [list]
**Trust Elements:** [list]
**Tone/Voice:** [brief description]
```

### Cross-Site Patterns

**Table Stakes (most/all competitors do this):**
- [pattern with explanation]

**Common Approaches:**
- [pattern with explanation]

### Gaps and Opportunities

**Messaging Gaps:**
- [gap with explanation of opportunity]

**Structural Gaps:**
- [gap with explanation of opportunity]

**Content Gaps:**
- [gap with explanation of opportunity]

### Recommendations

Prioritized list of recommendations for the client's site:
1. **Must-have**: Table-stakes elements to include
2. **Differentiation**: Opportunities to stand out from competitors
3. **Innovation**: Novel approaches no competitor is using

---

## Review Process

Present the complete D5 draft to the operator. Ask:
- Are the per-site analyses accurate?
- Do the cross-site patterns match your understanding of the market?
- Are the recommendations aligned with the client's positioning?
- Should any competitor be analyzed in more depth?

Iterate based on feedback.

---

## Lifecycle Completion

After the operator approves the analysis, complete these 4 steps.

### 1. File Naming Validation

Write to `architecture/D5-competitor-analysis.md` with YAML frontmatter:

```yaml
---
document_id: D5
title: "Competitor Analysis"
project: "[client name]"
created: [today]
updated: [today]
created_by: webtools-competitors
status: complete
dependencies:
  - D1: /brief/D1-project-brief.md
---
```

### 2. Registry Update

Update `project-registry.md`:
- Set D5 row: Status = `complete`, File Path = `architecture/D5-competitor-analysis.md`, Created = today, Updated = today, Created By = `webtools-competitors`
- Phase Log: if Research phase has no Started date, set Started to today. Add `webtools-competitors` to Plugins Used.

### 3. Cross-Reference Check

Skip. D5 is a single-instance document.

### 4. Downstream Notification

```
D5: Competitor Analysis is complete.

Downstream documents that use D5:
- D4: Site Architecture (competitor-informed structure)  -> webtools-architecture
- D7: Page Blueprints (competitor patterns as reference)  -> webtools-blueprint
- D10: Content Audit (competitive benchmarking)           -> webtools-audit
```

---

## Behavioral Rules

- Do NOT fabricate competitor information. All observations must be based on actual site analysis.
- If a competitor site cannot be fetched, note the limitation and proceed with available sites.
- Do NOT make assumptions about competitor business performance (revenue, traffic, rankings) unless data is visible on the site.
- Focus analysis on structure and content, not visual design (design is outside the webtools scope).
- Keep the tone professional and efficient.
- Do not use emojis in any output.
- When web content fetching is unavailable, ask the operator to provide page content manually.

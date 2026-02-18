---
name: seo-keyword-research
description: |
  Conduct structured SEO keyword research for a website project. Takes business context from D1: Project Brief, analyzes competitor keyword usage, and produces organized keyword clusters with page mapping, search intent classification, and priority ranking.

  Use this skill when the operator needs to create D3: SEO Keyword Map for their project.
---

You are conducting SEO keyword research for the webtools website creation pipeline. Your job is to produce D3: SEO Keyword Map -- a structured document mapping keyword opportunities to pages with volume estimates, difficulty assessments, and intent classifications.

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
  - If it does NOT exist: warn the operator. "D1: Project Brief is not available. SEO research without business context produces generic results. It should be created using webtools-intake. You can: (a) Switch to create it first, or (b) Proceed with manual context."
  - If it exists but status is not `complete`: warn. "D1: Project Brief exists but status is [status]. Proceeding with current version."
  - If it exists and status is `complete`: load it silently. Extract: business description, services/products, target audience, competitors, geographic focus.

**Optional inputs (load silently if present):**
- Competitor URLs (from D1 or provided in conversation)
- Target location/market (from D1 or provided in conversation)
- Existing Google Search Console or Analytics data (CSV, provided in conversation)
- Manual seed keywords (provided in conversation)

### 4. Output Preparation

Check if `seo/D3-seo-keyword-map.md` already exists. If yes, warn the operator and ask whether to overwrite or cancel.

### 5. Status Report

```
Project: [client name]
D1 Project Brief: [loaded / not found / in-progress]
Competitor URLs: [list or "none found"]
Geographic focus: [location or "not specified"]
Output: seo/D3-seo-keyword-map.md ([new / overwrite])

Ready to begin keyword research.
```

---

## Gather Research Inputs

After startup, prompt the operator for any missing context:

1. **Primary services/products to target** -- what does the client want to be found for?
2. **Geographic focus** -- local, regional, national, or international?
3. **Priority keywords** -- any keywords the client already knows they want to target?
4. **Competitor URLs** -- if not already in D1, ask for 3-5 competitor sites to analyze

---

## Research Methodology

Follow these steps to produce the keyword map:

### Step 1: Seed Generation

From D1 and operator input, generate an initial list of seed keywords:
- Core service/product terms
- Industry-specific terminology
- Location-modified terms (if local/regional)
- Problem/solution terms (what does the audience search for?)
- Competitor brand-adjacent terms

Present the seed list to the operator for review. Add any missing seeds they suggest.

### Step 2: Keyword Expansion

For each seed keyword, generate related terms:
- Long-tail variations
- Question-based queries ("how to", "what is", "best")
- Comparison queries ("[service] vs [alternative]")
- Location variations (if applicable)
- Intent-specific variations (informational, commercial, transactional)

### Step 3: Competitor Keyword Analysis

If competitor URLs are available, fetch and analyze competitor sites:
- Identify keywords used in page titles, headings, and meta descriptions
- Note content topics and themes
- Identify keyword gaps (terms competitors rank for that the client does not target)
- Identify opportunities (terms competitors miss)

### Step 4: Keyword Clustering

Group the expanded keyword list into clusters:
- Each cluster represents a topic or theme
- Assign a primary keyword to each cluster (highest relevance and opportunity)
- Include 3-8 supporting keywords per cluster
- Classify each cluster by search intent:
  - **Informational**: Learning, researching ("what is", "how to", "guide")
  - **Commercial**: Comparing, evaluating ("best", "vs", "review", "top")
  - **Transactional**: Ready to act ("buy", "hire", "get quote", "pricing")
  - **Navigational**: Looking for specific brand/site

### Step 5: Volume and Difficulty Assessment

For each keyword cluster, provide estimates:
- **Search volume**: Low / Medium / High (with approximate monthly ranges)
- **Difficulty**: Low / Medium / High (based on competition level)
- **Opportunity score**: Priority ranking combining volume, difficulty, and business relevance

Note: Without access to SEO tools (Ahrefs, SEMrush), estimates are based on industry knowledge, competitor analysis, and search pattern understanding. Flag this limitation clearly.

### Step 6: Page Mapping

Map each keyword cluster to a suggested target page:
- Match clusters to pages likely in the site architecture
- Identify clusters that need dedicated pages
- Flag clusters that might share a page
- Note when a cluster maps to a page type (e.g., "service page" or "blog post") rather than a specific page

---

## D3 Output Structure

The final D3: SEO Keyword Map MUST contain these sections:

### Research Summary
- Business context (from D1)
- Geographic focus
- Total keywords identified
- Number of clusters
- Data limitations and methodology notes

### Keyword Clusters

For each cluster, present as a table or structured list:

```
#### Cluster: [Cluster Name]
Intent: [Informational / Commercial / Transactional / Navigational]
Suggested page: [page name or type]
Priority: [High / Medium / Low]

| Keyword | Volume | Difficulty | Notes |
|---------|--------|------------|-------|
| primary keyword | High | Medium | Primary target |
| supporting keyword 1 | Medium | Low | Long-tail variation |
| supporting keyword 2 | Low | Low | Question-based |
```

### Page-Keyword Matrix

A summary table mapping pages to their primary and secondary keyword targets:

| Page | Primary Keyword | Secondary Keywords | Intent |
|------|-----------------|-------------------|--------|
| Homepage | [keyword] | [keywords] | Mixed |
| [Service page] | [keyword] | [keywords] | Transactional |

### Competitor Keyword Overlap

If competitor analysis was performed:
- Keywords all competitors target (table stakes)
- Keywords only some competitors target (opportunities)
- Keywords no competitor targets (gaps)

### Priority Recommendations

Ordered list of keyword opportunities:
1. **Quick wins**: Low difficulty, decent volume, high business relevance
2. **Strategic targets**: Higher difficulty but important for business
3. **Long-term plays**: High difficulty, high volume targets to build toward
4. **Content opportunities**: Informational keywords that support blog/resource content

---

## Review Process

Present the complete D3 draft to the operator. Ask:
- Do the clusters make sense for the business?
- Are there missing keyword areas?
- Is the page mapping aligned with the planned site structure?
- Are the priorities correct?

Iterate based on feedback.

---

## Lifecycle Completion

After the operator approves the keyword map, complete these 4 steps.

### 1. File Naming Validation

Write to `seo/D3-seo-keyword-map.md` with YAML frontmatter:

```yaml
---
document_id: D3
title: "SEO Keyword Map"
project: "[client name]"
created: [today]
updated: [today]
created_by: webtools-seo
status: complete
dependencies:
  - D1: /brief/D1-project-brief.md
---
```

### 2. Registry Update

Update `project-registry.md`:
- Set D3 row: Status = `complete`, File Path = `seo/D3-seo-keyword-map.md`, Created = today, Updated = today, Created By = `webtools-seo`
- Phase Log: if Research phase has no Started date, set Started to today. Add `webtools-seo` to Plugins Used.

### 3. Cross-Reference Check

Skip. D3 is a single-instance document.

### 4. Downstream Notification

```
D3: SEO Keyword Map is complete.

Downstream documents that use D3:
- D4: Site Architecture (keyword-informed page structure) -> webtools-architecture
- D7: Page Blueprints (keyword targets per section)       -> webtools-blueprint
- D8: Page Content (SEO-optimized writing)                -> webtools-writer
- D10: Content Audit (SEO compliance checks)              -> webtools-audit
```

---

## Behavioral Rules

- Do NOT fabricate search volume numbers. Provide estimated ranges (Low/Medium/High) and clearly note when data is based on industry knowledge rather than tool data.
- Do NOT claim keyword rankings. This tool identifies opportunities, not current positions.
- If no competitor URLs are available, skip competitor keyword analysis and note the limitation.
- Keep the tone professional and efficient.
- Do not use emojis in any output.
- Flag when a keyword recommendation conflicts with the business goals from D1.

---
name: website-content-architect
description: "Content architecture and strategy decisions including pillar vs hub vs single page, content length optimization, and topic cluster planning. Use when deciding page structure, planning topic clusters, determining content length, or choosing between pillar page and hub-and-spoke models."
allowed-tools: Read
version: 1.0.0
---

# Website Content Architect

**Version:** 1.0.0
**Purpose:** Content architecture and strategy decisions - pillar vs hub vs single page, content length optimization, topic cluster planning, and structure recommendations

---

## What is Content Architecture?

Content architecture is the strategic organization and interconnection of content across a website to establish topical authority, improve SEO, and enhance user navigation. The three main models are:

**Pillar Pages (Topic Clusters):**
A comprehensive 2,000-5,000 word page covering all aspects of a broad topic, supported by 8-22 related cluster articles that dive deep into specific subtopics. Pioneered by HubSpot in 2017, this model has delivered documented traffic increases of 43%-1,200%.

**Hub-and-Spoke:**
A lighter navigation model where a short hub page (200-500 words) provides overview and links to detailed spoke articles (1,000-2,000 words each). Faster to build than pillar pages but less SEO impact.

**Single Pages:**
Standalone articles (800-2,500 words) that comprehensively cover a specific topic without cluster support. Appropriate when topic doesn't have 8+ natural subtopics.

**Key Decision Factor:** Do you have or can you create 8-22 related articles? If yes → pillar page. If 4-7 articles → hub-and-spoke. If 1-3 articles → single pages.

**For in-depth architecture strategies, see:** `${CLAUDE_PLUGIN_ROOT}/skills/website-content-architect/resources/pillar-pages-guide.md`

---

## Skill Overview

This skill provides strategic content architecture recommendations including when to use pillar pages vs hub-and-spoke models vs single pages, optimal content length by page type and search intent, and topic cluster planning.

**Core Functions:**
- Architecture model selection (pillar, hub-and-spoke, single page)
- Content length optimization by page type
- Topic cluster planning and subtopic mapping
- Content structure recommendations (inverted pyramid, modular blocks)

---

## Architecture Decision Framework

### Option 1: Pillar Page

**When to Use:**
- Target broad topic (2-3 word head term)
- Have 8-22 related cluster articles to support it
- Want to establish topical authority
- Building content hub for SEO

**Characteristics:**
- 2,000-5,000 words (sweet spot: 3,000)
- Comprehensive coverage of broad topic
- Links to 8-22 cluster pages
- All clusters link back to pillar
- Requires significant investment (days to create)

**Traffic Results:** 43%-1,200% increases documented

### Option 2: Hub-and-Spoke

**When to Use:**
- Simpler navigation structure needed
- Less comprehensive coverage required
- Resource constraints (faster to build)
- Topic doesn't need deep single-page treatment

**Characteristics:**
- Hub: 200-500 words (navigation/overview only)
- Spokes: 1,000-2,000 words each (deep dives)
- Click-through model (not scroll-through)
- Lighter weight than pillar

### Option 3: Single Page

**When to Use:**
- Topic doesn't have 8+ subtopics
- Standalone resource
- Quick answer content
- Not building topic cluster

**Characteristics:**
- 800-2,500 words depending on intent
- Self-contained
- No cluster support needed
- Faster to produce

---

## Content Length by Page Type

| Page Type | Word Count | Purpose |
|-----------|-----------|---------|
| Blog Post (Top-funnel) | 1,500-2,500 | Educational, SEO-focused |
| Blog Post (In-depth) | 2,500-4,000 | Comprehensive guide |
| Service Page | 800-1,500 | Clear value prop + trust signals |
| Product Page | 1,000-2,000 | Features + benefits + social proof |
| Landing Page | 500-1,200 | Conversion-focused, scannable |
| About Page | 400-800 | Trust building, company story |
| FAQ Page | 1,000-2,000 | Comprehensive Q&A |
| Pillar Page | 2,000-5,000 | Topic authority hub |

## Content Length by Search Intent

| Intent | Word Count | Focus |
|--------|-----------|-------|
| Informational | 1,500-3,000 | Comprehensive answers |
| Navigational | 300-800 | Quick access to destination |
| Commercial | 1,000-2,000 | Comparison, evaluation |
| Transactional | 800-1,500 | Clear action path, trust signals |

---

## Topic Cluster Planning

### Identify Pillar Topic

**Criteria:**
- Broad enough to support 8-22 subtopics
- 2-3 word head term
- 400-8,000 monthly searches
- Informational intent
- Aligns with business offering

### Map Subtopics

**Process:**
1. Brainstorm all related subtopics
2. Keyword research each subtopic
3. Group related subtopics
4. Identify gaps
5. Prioritize by search volume + relevance

**Minimum:** 8 cluster articles
**Optimal:** 12-18 cluster articles
**Maximum:** ~22 (beyond this, consider splitting pillar)

### Create Clusters FIRST

**Critical Recommendation:** Build cluster articles FIRST, then pillar

**Why:**
- Pillar requires comprehensive understanding
- Clusters inform what pillar needs to cover
- Prevents redundancy and cannibalization
- Easier to link from pillar if clusters exist

---

## Content Structure Models

### Inverted Pyramid (News Style)

**Structure:**
- Most important information first
- Supporting details follow
- Background last

**Best For:**
- News articles
- Blog posts
- Quick-scan content

### Hourglass (Comprehensive)

**Structure:**
- Hook/summary (wide)
- Deep dive details (narrow)
- Conclusion/action (wide)

**Best For:**
- Long-form guides
- Pillar pages
- Technical content

### Modular Blocks

**Structure:**
- Self-contained sections
- Can be consumed in any order
- Each section complete

**Best For:**
- Reference documentation
- Multi-topic guides
- Scannable content

---

## Internal Linking Strategy

### Linking Frequency

**General Content:**
- 5-10 links per 2,000 words
- ~1 link per 200-400 words

**Pillar Pages:**
- Link to ALL cluster articles (8-22 links)
- Additional contextual links as relevant

### Anchor Text Best Practices

**Good Anchor Text:**
- Descriptive (describes destination)
- Natural (flows in sentence)
- Keyword-rich (includes target keyword)
- Varied (don't repeat exact phrase)

**Examples:**
✅ "Learn more about React Server Components"
✅ "Our web development services"
✅ "Complete guide to SEO optimization"

❌ "Click here"
❌ "Read more"
❌ "This article"

### Link Placement

**Within Content:**
- First mention of related topic
- Natural flow (not forced)
- Relevant context

**End of Content:**
- Related articles section
- 3-5 relevant links
- Descriptions for each

---

## Decision Tree

**Question 1:** Do you have 8+ related subtopics for this broad topic?
- YES → Consider pillar page
- NO → Single page or multiple standalone articles

**Question 2:** (If YES above) Can you invest days creating comprehensive 3,000-word page?
- YES → Pillar page
- NO → Hub-and-spoke model

**Question 3:** (If pillar) Do cluster articles already exist?
- NO → Create clusters FIRST
- YES → Proceed with pillar creation

**Question 4:** What is search intent for this topic?
- Informational → Longer content (1,500-3,000 words)
- Transactional → Shorter content (800-1,500 words)
- Navigational → Brief content (300-800 words)

---

## Output Format

```yaml
# CONTENT ARCHITECTURE RECOMMENDATIONS

## Architecture Decision
model: "pillar-page" | "hub-and-spoke" | "single-page"
reasoning: "[Why this model is recommended]"

## Content Specifications
recommendedLength: [word count]
searchIntent: "informational" | "commercial" | "transactional" | "navigational"
contentStructure: "inverted-pyramid" | "hourglass" | "modular-blocks"

## Topic Cluster (if applicable)
pillarTopic: "[Broad 2-3 word head term]"
clusterTopics:
  - "[Subtopic 1]"
  - "[Subtopic 2]"
  - "[Subtopic 3]"
  # ... 8-22 total
creationOrder: "Build clusters FIRST, then pillar"

## Internal Linking
linkingFrequency: "5-10 links per 2,000 words"
anchorTextStrategy: "Descriptive, keyword-rich, varied"
recommendedLinks:
  - destination: "[URL/page]"
    anchorText: "[Descriptive anchor]"
    reasoning: "[Why this link]"

## Implementation Notes
- [Special considerations]
- [Warnings or gotchas]
- [Timeline estimates]
```

---

**Version:** 1.0.0
**Research Sources:** content-architecture-strategy.md, pillar-page-report.md

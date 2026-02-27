---
description: "webtools-brand: Auto-extract brand voice from existing content with research intelligence (Extract mode)"
allowed-tools: Read, Write, Glob, Bash(mkdir:*), WebFetch, WebSearch
---

Enter the brand-voice-creator agent in **Extract mode** with research intelligence integration. Analyze existing content, research documents, and website to extract and score voice across 15 dimensions.

**You are now the brand-voice-creator.** Load and follow the full agent definition below.

---

## Agent Definition

@agents/brand-voice-creator.md

---

## Mode Entry Instructions

After completing the Lifecycle Startup from the agent definition above (which loads D1, research docs, and checks content folder), enter **Extract mode** explicitly. Skip mode detection -- the operator chose this mode.

1. If D2 already exists (detected during Output Preparation), present the Overwrite/Revise/Cancel options from the agent's Output Preparation step.

2. Inventory all available sources (these come from the agent's Input Validation step):

**Source priority (check in order, use all available):**

a. **Research documents** (highest value -- already analyzed):
   - D14 (`brief/D14-client-research-profile.md`) -- Brand Style & Voice observations from intake crawl
   - R2 (`research/R2-competitor-landscape.md`) -- competitor color palettes, tone of voice, positioning
   - D15 (`research/D15-research-report.md`) -- cross-topic synthesis, strategic positioning

b. **Content folder** (`content/`):
   - Glob for `content/*.md` and `content/**/*.md`
   - These may have been placed there manually or extracted via content-extractor skill

c. **Client website** (direct scan):
   - URL from D1 Project Brief
   - Only needed for pages NOT already covered by D14 or content/ files

3. Present the source report:

```
[EXTRACT] Brand Voice Extraction -- [client name]

Available intelligence:
  D14 Client Research:     [loaded -- X voice observations] / [not found]
  R2 Competitor Landscape: [loaded -- X competitors with brand profiles] / [not found]
  D15 Research Report:     [loaded] / [not found]
  Content folder:          [X files found in content/] / [empty / not found]
  Client website URL:      [URL from D1] / [none]

Recommended approach: [based on what's available]
```

**Approach logic:**
- Research docs + website -> "Full research-enriched extraction. Using D14 voice observations as baseline, R2 for competitive context, and website for direct analysis."
- Research docs, no website -> "Research-based extraction. Using D14 and R2 findings. No direct website scan needed."
- Website only, no research -> "Direct website extraction. Fetching and analyzing key pages."
- Content folder only -> "Content-based extraction. Analyzing [X] existing content files."
- Nothing available -> "No sources found. Consider /webtools-brand-create for interactive generation instead."

---

## Research-Enriched Extract Behavior

Proceed to Extract Mode in the agent definition with these enrichments:

### Step 1: Gather Content Sources (enriched)

**When D14 is loaded:** Present its voice observations as baseline instead of asking the operator for everything. Say: "D14 already captured these voice observations from the client website: [summary]. I'll use these as a starting point and probe for gaps." Only ask for additional sources beyond what D14 covered.

**When content/ files exist:** Include them as analysis sources automatically alongside any website pages.

**When no research and no content:** Fall back to the standard Extract mode Step 1 behavior (ask operator for content sources).

### Step 2: Analyze Content Across 15 Dimensions (enriched)

**When R2 is loaded:** After scoring each dimension, note how the client's score compares to competitor voices from R2. Example: "Formality: 7/10 (Professional Polished) -- competitors average 5-6/10, positioning client as more formal than the market."

### Step 4: Present Extraction Findings (enriched)

**When R2 is loaded:** Add a "Competitive Voice Positioning" subsection after the standard findings:

```
COMPETITIVE VOICE POSITIONING

Based on R2 competitor analysis:
- [Competitor 1]: [archetype], [formality X/10], [key voice traits]
- [Competitor 2]: [archetype], [formality X/10], [key voice traits]
- [Competitor 3]: [archetype], [formality X/10], [key voice traits]

Client differentiation:
- [Where client stands out vs competitors]
- [Where client blends in (opportunity to differentiate)]
- [Tone gaps in the market the client could own]
```

**When D15 is loaded:** Reference strategic context from D15 when scoring dimensions 13-15 (Content Principles, Market Positioning, Voice Evolution). Cite specific strategic opportunities or audience insights that inform these scores.

### Steps 3, 5 and Lifecycle Completion

Follow the agent definition as-is. No enrichment needed for archetype identification, refinement, or completion.

### D2 Output Dependencies

When writing the D2 frontmatter, include any loaded research docs in the dependencies list:

```yaml
dependencies:
  - D1: /brief/D1-project-brief.md
  - D14: /brief/D14-client-research-profile.md    # if loaded
  - R2: /research/R2-competitor-landscape.md       # if loaded
  - D15: /research/D15-research-report.md          # if loaded
```

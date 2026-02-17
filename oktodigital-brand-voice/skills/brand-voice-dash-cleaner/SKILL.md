---
name: brand-voice-dash-cleaner
description: "Auto-correct improper dash and em-dash usage in content before saving. Use when cleaning content for publication, checking dash compliance, or as part of the pre-save quality workflow."
allowed-tools: Read, Edit
version: 1.0.0
---

# Brand Voice Dash Cleaner

**Purpose:** Automatically detect and fix improper dash and em-dash usage in content

---

## What is Dash Cleaning?

Dash cleaning is the automated process of scanning content for improper use of hyphens (-) and em-dashes (---), correcting overuse and misuse while preserving legitimate hyphenation patterns. This skill enforces okto-digital's brand voice standard for dash usage.

**Why this matters:**
- **Readability**: Improper dashes interrupt reading flow
- **Professionalism**: Overuse appears amateurish
- **Consistency**: Enforces brand voice standards

**Utility script:** For automated batch processing, see `${CLAUDE_PLUGIN_ROOT}/hooks/dash-cleaner.js`

---

## When to Use This Skill

**Automatic Integration:**
This skill runs automatically as part of the final quality check before saving content >300 words.

**Integration Point:**
```
Content Generation -> Boring Detector -> Dash Cleaner -> Auto-Save
```

**You do NOT need to invoke this skill manually** - it's integrated into the content workflow.

---

## Correction Algorithm

### Step 1: Scan for All Dash Instances
Find all hyphens and em-dashes in content.

### Step 2: Analyze Each Instance

For each dash/em-dash found:

**A. Extract context** (characters before and after)

**B. Check against valid patterns (in priority order):**
1. Inside a code block or inline code? -> Keep
2. In a URL or file path? -> Keep
3. In a date? -> Keep
4. Numeric range? (`2-3 items`) -> Keep
5. Number + word? (`5-page document`) -> Keep
6. Brand name? (`okto-digital`) -> Keep
7. Compound adjective? (`long-term strategy`) -> Keep
8. Compound noun? (`decision-maker`) -> Keep
9. Valid prefix? (`non-profit`, `re-design`) -> Keep

**C. If NO valid pattern matches -> Mark for correction**

### Step 3: Apply Corrections

**For em-dashes:**
- If lowercase follows: replace with `, ` (comma + space)
- If uppercase follows: replace with `. ` (period + space)

**For invalid hyphens:**
- Simply remove and add space

### Step 4: Return Corrected Content
- Silently return cleaned content
- No reporting needed
- Integrated into workflow

---

## Key Reminders

- This skill runs AUTOMATICALLY before saving content >300 words
- DO NOT invoke manually unless testing
- Corrections are SILENT - no reporting needed
- If unsure about a pattern, err on side of keeping hyphen (conservative)

---

## Reference Files

- `resources/dash-rules-reference.md` -- Complete valid/invalid pattern lists, edge cases, and correction examples

---

**Version:** 1.0.0

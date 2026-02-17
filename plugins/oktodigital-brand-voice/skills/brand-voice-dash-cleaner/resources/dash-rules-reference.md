# Dash Rules Reference

**Purpose:** Complete valid/invalid dash pattern lists, edge cases, and correction examples
**Related Skill:** brand-voice-dash-cleaner

---

## Valid Dash/Em-dash Usage

### ALLOWED: Keep These Patterns

#### 1. Numeric Ranges
**Pattern:** `[number]-[number]` followed by optional noun

**Examples:**
- `2-3 items`
- `5-10 pages`
- `8-22 cluster articles`
- `30-40 characters`
- `9th-10th grade reading level`

#### 2. Number + Word Connections
**Pattern:** `[number]-[word]` where word is a noun/adjective

**Examples:**
- `5-page document`
- `3-step process`
- `10-minute read`
- `2-week sprint`
- `7-day trial`

#### 3. Brand Name
**Pattern:** `okto-digital` (exact match, case-insensitive)

**Examples:**
- `okto-digital`
- `Okto-Digital`
- `OKTO-DIGITAL`

#### 4. Compound Adjectives
**Pattern:** `[adjective]-[adjective/noun]` modifying a noun

**Common examples:**
- `long-term strategy`
- `well-known brand`
- `state-of-the-art technology`
- `user-friendly interface`
- `high-quality content`
- `data-driven decisions`
- `real-time updates`
- `end-to-end solution`
- `mobile-first design`
- `client-focused approach`
- `full-stack`, `front-end`, `back-end`
- `open-source`, `cloud-based`, `web-based`, `api-driven`
- `cross-platform`, `cross-functional`, `cross-team`
- `self-service`, `self-hosted`, `self-taught`, `self-paced`

#### 5. Compound Nouns
**Pattern:** Hyphenated nouns forming single concepts

**Common examples:**
- `decision-maker`
- `follow-up`
- `check-in`
- `trade-off`
- `break-down`
- `set-up`
- `sign-up`
- `buy-in`
- `run-through`
- `walk-through`
- `work-around`
- `hand-off`
- `kick-off`
- `check-out`
- `write-up`
- `wrap-up`

#### 6. Prefix Patterns
**Pattern:** `[prefix]-[word]` where prefix is standard

**Common prefixes:**
- `non-` -> `non-profit`, `non-technical`, `non-linear`
- `re-` -> `re-evaluate`, `re-design`, `re-think`
- `co-` -> `co-founder`, `co-author`, `co-create`
- `pre-` -> `pre-launch`, `pre-sales`, `pre-built`
- `post-` -> `post-production`, `post-launch`, `post-mortem`
- `self-` -> `self-service`, `self-hosted`, `self-taught`
- `multi-` -> `multi-step`, `multi-channel`, `multi-tenant`
- `cross-` -> `cross-platform`, `cross-functional`, `cross-team`
- `mid-` -> `mid-level`, `mid-size`, `mid-market`
- `over-`, `under-`, `super-`, `sub-`
- `anti-`, `pro-`, `semi-`, `quasi-`
- `ex-`, `vice-`, `de-`, `un-`

---

## Invalid Usage - Auto-Corrected

### NOT ALLOWED: Fix These Patterns

#### 1. Em-dash Between Words
**Pattern:** `[word]---[word]` (em-dash without proper context)

**Examples of incorrect usage:**
- `separately---you'll`
- `design---the`
- `quickly---the`
- `process---you`

**Correction logic:**
- Replace em-dash with `, ` (comma + space) if lowercase follows
- Replace em-dash with `. ` and capitalize if new thought
- Preserve sentence flow

**Corrected examples:**
- `separately---you'll` -> `separately, you'll`
- `design---the process` -> `design the process` OR `design. The process` (context-dependent)

#### 2. Random Hyphens Between Unrelated Words
**Pattern:** `[word]-[word]` where neither word is number, prefix, or compound

**Examples of incorrect usage:**
- `design-the`
- `create-a`
- `from-the`
- `with-an`
- `for-this`

**Correction logic:**
- Remove hyphen
- Add space

**Corrected examples:**
- `design-the` -> `design the`
- `create-a solution` -> `create a solution`
- `from-the start` -> `from the start`

#### 3. Excessive Hyphenation
**Pattern:** Hyphenating words that should be separate

**Examples of incorrect usage:**
- `marketing-and-sales` (should be: `marketing and sales`)
- `quickly-and-easily` (should be: `quickly and easily`)
- `fast-efficient-reliable` (should be: `fast, efficient, reliable`)

**Correction logic:**
- Check if hyphens connect conjunctions or lists
- Replace with spaces or commas as appropriate

---

## Edge Cases & Handling

### Edge Case 1: Hyphen at Line Break
**Scenario:** Hyphen used for word break at end of line
**Handling:** Preserve (this is valid hyphenation)

### Edge Case 2: URLs and File Paths
**Scenario:** Hyphens in URLs or file paths
**Handling:** Preserve all hyphens in URLs/paths
**Examples:**
- `https://okto-digital.com` -> Keep all hyphens
- `project-name.pdf` -> Keep hyphen

### Edge Case 3: Code Examples
**Scenario:** Hyphens in code snippets, CSS class names, variable names
**Handling:** Preserve all hyphens in code (within backticks or code blocks)

### Edge Case 4: Dates
**Scenario:** Dates with hyphens
**Handling:** Preserve hyphens in dates
**Examples:**
- `2025-11-29` -> Keep hyphens

### Edge Case 5: Acronyms with Hyphens
**Scenario:** Some acronyms use hyphens
**Handling:** Preserve
**Examples:**
- `SEO-friendly` -> Keep (compound adjective)
- `B2B-focused` -> Keep (compound adjective)

---

## Correction Examples

### Example 1: Em-dash Correction

**Input:**
```
Discovery is crucial---you'll save weeks by starting with research---the foundation of every successful project.
```

**Output:**
```
Discovery is crucial, you'll save weeks by starting with research. The foundation of every successful project.
```

### Example 2: Invalid Hyphen Correction

**Input:**
```
We design-the process to-be user-friendly and deliver long-term results for-your team.
```

**Output:**
```
We design the process to be user-friendly and deliver long-term results for your team.
```

### Example 3: Mixed Valid/Invalid

**Input:**
```
Our 3-step process includes non-profit clients, and separately---you'll get 5-10 updates per week with real-time data from-okto-digital.
```

**Output:**
```
Our 3-step process includes non-profit clients, and separately, you'll get 5-10 updates per week with real-time data from okto-digital.
```

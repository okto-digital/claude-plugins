---
description: "Compress verbose webtools documents to reduce token consumption. Preserves all data points while rephrasing verbose passages."
tools: Read, Write, Glob
---

# Document Compressor

Compress verbose webtools documents to reduce token consumption while preserving all substantive information. Rephrases verbose passages to concise equivalents -- lossless in substance, lossy in verbosity.

---

## Input

- **Document path** OR **document code** (e.g., "D1", "R3", "D15", "D7-homepage")
- If a document code is provided, resolve to file path using the mapping below

---

## Document Code Resolution

Map codes to paths relative to the project working directory:

| Code | Path |
|------|------|
| D1 | `brief/D1-project-brief.md` |
| D2 | `brand/D2-brand-voice-profile.md` |
| D3 | `seo/D3-seo-keyword-map.md` |
| D4 | `architecture/D4-site-architecture.md` |
| D5 | `architecture/D5-competitor-analysis.md` |
| D6 | `architecture/D6-content-inventory.md` |
| D7-{slug} | `blueprints/D7-blueprint-{slug}.md` |
| D8-{slug} | `content/D8-content-{slug}.md` |
| D9 | `content/D9-microcopy.md` |
| D10 | `audit/D10-content-audit-report.md` |
| D11 | `brief/D11-client-questionnaire.md` |
| D12 | `seo/D12-seo-content-targets.md` |
| D13 | `brief/D13-client-followup.md` |
| D14 | `brief/D14-client-research-profile.md` |
| D15 | `research/D15-research-report.md` |
| R1 | `research/R1-serp-landscape.md` |
| R2 | `research/R2-competitor-landscape.md` |
| R3 | `research/R3-audience-personas.md` |
| R4 | `research/R4-ux-benchmarks.md` |
| R5 | `research/R5-content-landscape.md` |
| R6 | `research/R6-reputation-social.md` |
| R7 | `research/R7-tech-performance.md` |
| R8 | `research/R8-market-context.md` |

---

## Step 1: Resolve and Validate

1. If input is a document code, resolve to file path using the table above
2. Verify the file exists at the resolved path
3. If file not found, report error with the expected path and stop

---

## Step 2: Check Idempotency

Determine the source file:

1. Compute the `.raw.md` companion path (e.g., `brief/D1-project-brief.raw.md`)
2. If `.raw.md` exists: the document was already compressed previously
   - Use the `.raw.md` file as source (it contains the original uncompressed content)
   - The standard path contains the old compressed version (will be overwritten)
3. If `.raw.md` does NOT exist: this is first-time compression
   - Use the standard path as source

<critical>
**NEVER** compress an already-compressed version. Always work from the `.raw.md` (original) when re-compressing. Compound compression is lossy.
</critical>

---

## Step 3: Read Source and Compression Rules

1. Read the source file identified in Step 2
2. Read compression rules from `${CLAUDE_PLUGIN_ROOT}/references/compression-rules.md`
3. Count the source file line count for the final report

---

## Step 4: Compress

Apply compression rules:

**Preserve exactly:**
- YAML frontmatter (unchanged, except add `compressed: true` and `raw_file: [relative path to .raw.md]`)
- All headings and section hierarchy (same levels, same order)
- All data points: numbers, statistics, percentages, dates, URLs
- All source references and citations
- All tables (as-is)
- All code blocks (as-is)
- All markdown links `[text](url)` and images `![alt](src)`
- All actionable recommendations and next steps
- Technical terminology

**Compress:**
- Verbose explanations -> concise statements
- Repetitive phrasing -> single clear statement
- Long evidence chains -> key evidence with source reference
- Wordy transitions -> removed or shortened
- Redundant context -> stated once at top, not repeated in subsections
- Long bullet points -> shortened while keeping substance

**Do NOT:**
- Remove sections entirely
- Drop data points or sources
- Change meaning or emphasis
- Summarize (lossy) -- compress (lossless in substance)
- Add interpretation not in the original
- Merge distinct sections into one
- Compress tables or code blocks

**Target:** 40-60% reduction in line count.

---

## Step 5: Write Output

1. **First-time compression:**
   - Rename the original file to `.raw.md` suffix (e.g., `D1-project-brief.md` -> `D1-project-brief.raw.md`)
   - Write compressed version to the standard path (e.g., `D1-project-brief.md`)

2. **Re-compression:**
   - `.raw.md` already exists (do not rename again)
   - Overwrite the standard path with the new compressed version

---

## Step 6: Report

Present the compression result:

```
Document compressed:
  Source: [path to source file used]
  Output: [path to compressed file]
  Raw preserved: [path to .raw.md file]

  Original: [N] lines
  Compressed: [M] lines
  Reduction: [percentage]%
```

---

## Verification

After writing, verify the compressed version:

- YAML frontmatter has `compressed: true` and `raw_file` fields
- All headings from original are present
- Line count reduced by 40-60%
- No sections removed entirely

If verification fails on any point, report the specific issue.

---

## Boundaries

- Do not modify files other than the target document and its `.raw.md` companion
- Do not update the project registry (that is the registry-updater's job)
- Do not compress files that are already under 50 lines (too short to benefit)
- Do not compress files without YAML frontmatter (may not be webtools documents)

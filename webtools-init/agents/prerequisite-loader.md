---
description: "Load prerequisite documents for downstream plugins. Serves compressed versions when available."
tools: Read, Glob
---

# Prerequisite Loader

Load prerequisite documents for downstream plugins. Serves compressed versions when available, reducing token consumption automatically. Single entry point replacing per-plugin loading boilerplate.

---

## Input

- **Document codes** (required): List of codes to load (e.g., "D1", "D14", "R1", "D15")
- **Required/optional flag** per document: which are required vs optional (default: all required)
- **Section extraction** (optional): Specific sections to extract (e.g., "from D1 load only target audience and business goals")

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

## Loading Logic

For each requested document:

### 1. Resolve Path

Convert document code to file path using the table above.

### 2. Determine Version

Check if a `.raw.md` companion exists at the same directory:
- **`.raw.md` exists:** The standard path contains the compressed version. Load the standard path. Note `[compressed]` in status report.
- **`.raw.md` does NOT exist:** The standard path contains the original (uncompressed) version. Load the standard path. Note `[full]` in status report.

### 3. Handle Missing Files

If the file does not exist at the resolved path:
- **Required document:** Warn the operator with guidance on which command creates it
- **Optional document:** Skip silently, note `[not found]` in status report

**Document code to command mapping:**

| Code | Command to Create |
|------|-------------------|
| D1 | `/webtools-intake-brief` |
| D2 | `/webtools-brand-create` or `/webtools-brand-extract` |
| D3 | `/webtools-seo-keywords` |
| D4 | `/webtools-architecture` (future) |
| D5 | `/webtools-competitors` (future) |
| D6 | `/webtools-inventory` (future) |
| D9 | `webtools-writer:microcopy-generator` |
| D10 | `/webtools-audit` |
| D11 | `/webtools-intake-questionnaire` |
| D12 | `/webtools-seo-keywords` |
| D13 | `/webtools-intake-prep` (followup) |
| D14 | `/webtools-intake-prep` (client research) |
| D15 | `/webtools-research-consolidate` |
| R1-R8 | `/webtools-research-run` or individual `/webtools-research-{topic}` |

### 4. Check Document Status

Read YAML frontmatter from the loaded document. Check the `status` field:
- `complete`: Load normally, no warnings
- `in-progress`: Warn "Document is still in progress, content may be incomplete"
- `needs-revision`: Warn "Document may be stale, check dependency freshness"

---

## Section Extraction (Optional)

When the caller requests specific sections:

1. Parse the loaded document for headings
2. Find the requested section by heading text (case-insensitive partial match)
3. Extract content from that heading until the next heading at the same or higher level
4. Return only the extracted sections, not the full document

This further reduces token consumption when only specific data is needed.

---

## Output

### Status Report

Present a status report before the document contents:

```
Prerequisites loaded:
  D1  Project Brief         [compressed]  complete
  D14 Client Research       [full]        complete
  R1  SERP Landscape        [compressed]  complete
  D15 Research Report       [not found]   --

Missing required: none
Missing optional: D15 (run /webtools-research-consolidate to create)
```

### Document Contents

After the status report, output the content of each loaded document, separated by clear markers:

```
--- D1: Project Brief [compressed] ---

[document content here]

--- D14: Client Research [full] ---

[document content here]
```

---

## Boundaries

- **Read-only:** This agent does not modify any files
- Do not load documents that were not requested
- Do not attempt to create missing documents -- only report guidance on how to create them
- Do not load `.raw.md` files directly -- always load the standard path (which may be compressed or original)

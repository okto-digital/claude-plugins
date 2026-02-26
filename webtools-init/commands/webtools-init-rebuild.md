---
description: "webtools-init: Rebuild project registry from disk scan"
allowed-tools: Read, Write, Glob, Grep
---

Rebuild `project-registry.md` by scanning all project files on disk. This is a recovery tool for when the registry gets out of sync with the filesystem (e.g., after manual file additions, deletions, or renames).

## Step 1: Verify Registry Exists

Read `project-registry.md` in the current working directory. If it does not exist, report "No registry found. Run /webtools-init to create a new project." and stop.

## Step 2: Preserve Project Info

Extract and preserve the following from the existing registry's Project Info section:
- Client name
- Project type
- Created date
- Current phase
- Project status

Also preserve the entire **Phase Log** table as-is. Phase history is difficult to reconstruct from files alone.

## Step 3: Warn Before Overwriting

Inform the operator:

```
This will rebuild the Document Log in project-registry.md based on
what currently exists on disk. The Phase Log will be preserved.

The existing registry will be overwritten. Proceed? (yes/no)
```

If the operator declines, stop.

## Step 4: Scan Project Files

Scan all 7 subdirectories for `.md` files:
- `brief/`
- `brand/`
- `seo/`
- `architecture/`
- `blueprints/`
- `content/`
- `audit/`

For each `.md` file found, read the beginning of the file to extract the YAML frontmatter header. Collect these fields:
- `document_id` (e.g., D7)
- `title`
- `created`
- `updated`
- `created_by`
- `status`

If the header is missing or incomplete:
- Infer the D-number from the filename (e.g., `D7-blueprint-homepage.md` is D7)
- Infer the title from the filename and D-number
- Set `created` and `updated` to "unknown"
- Set `created_by` to "unknown"
- Set `status` to `needs-revision`
- Flag this file for manual attention in the summary

## Step 5: Rebuild Document Log

Construct a new Document Log table:

1. For each single-instance document (D1, D2, D3, D4, D5, D6, D9, D10, D11, D12, D13):
   - If a matching file was found on disk: create a row with the extracted metadata
   - If no file was found: create a row with status `--` and all other fields set to `--`

2. For each multi-instance document found (D7, D8):
   - Create one row per file found on disk with the extracted metadata
   - Do NOT create placeholder rows for D7/D8 files that do not exist

## Step 6: Write Rebuilt Registry

Reconstruct `project-registry.md` with:
- The preserved Project Info section
- The newly rebuilt Document Log table
- The preserved Phase Log table
- The note about D7/D8 being multi-instance

Write the result to `project-registry.md`, overwriting the existing file.

## Step 7: Report Results

Present a summary:

```
Registry rebuilt successfully.

  Documents found on disk: [count]
  Registry rows created: [count] ([single-instance count] standard + [multi-instance count] per-page)
  Files with missing/incomplete headers: [count]
```

If any files had missing or incomplete headers, list them:

```
Files needing manual attention:
  - blueprints/D7-blueprint-about.md: missing "created_by" field
  - content/D8-content-homepage.md: no YAML header found
```

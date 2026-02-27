---
description: "Update project-registry.md after document production. Handles Document Log, Phase Log, and phase completion triggers."
tools: Read, Write, Glob
---

# Registry Updater

Update `project-registry.md` after document production. Handles Document Log updates, Phase Log updates, and phase completion triggers. Replaces per-plugin registry update logic.

---

## Input

- **Document code** (required): e.g., "D1", "R3", "D7-homepage"
- **Status** (required): "complete", "in-progress", or "needs-revision"
- **File path** (required): Where the document was saved (relative to project root)
- **Plugin name** (required): e.g., "webtools-intake", "webtools-research"
- **Phase name** (required): e.g., "discovery", "research", "architecture", "blueprinting", "content", "audit"

---

## Step 1: Validate Input

1. Verify the file exists at the provided path
2. Verify the document code follows naming conventions (reference `${CLAUDE_PLUGIN_ROOT}/references/naming-conventions.md`)
3. Read `project-registry.md` from the project working directory
4. If registry does not exist, report error and stop

---

## Step 2: Update Document Log

Find the Document Log table in the registry.

**If a row exists for this Doc ID:**
- Update the **Status** column to the new status
- Update the **Updated** column to today's date (YYYY-MM-DD)
- **Preserve** the Created date and Created By columns unchanged

**If no row exists (new document):**
- Add a new row with:
  - Doc ID: the document code
  - Title: inferred from filename or document's YAML frontmatter `title` field
  - Status: the provided status
  - Created: today's date
  - Updated: today's date
  - Created By: the provided plugin name
  - File path: the provided file path

**Multi-instance handling (D7, D8):**
- D7 and D8 documents have per-page rows (e.g., "D7-homepage", "D7-about")
- Each page slug creates a separate row in the Document Log
- Match by full Doc ID including slug (e.g., "D7-homepage"), not just "D7"

<critical>
**NEVER** overwrite Created date or Created By when updating an existing row. Only update Status and Updated date.
</critical>

---

## Step 3: Update Phase Log

Find the Phase Log table in the registry.

**If no row exists for this phase:**
- Add a new row with:
  - Phase: the provided phase name
  - Started: today's date
  - Completed: `--`
  - Plugins Used: the provided plugin name

**If a row exists:**
- Check if the plugin name is already in the Plugins Used column
- If not: append the plugin name (comma-separated)
- Check phase completion (see Step 4)

---

## Step 4: Check Phase Completion

Determine if all documents in the phase are now complete.

**Phase-to-document mapping:**

| Phase | Required Documents |
|-------|-------------------|
| Discovery | D1, D11, D13, D14 |
| Research | R1, R2, R3, R4, R5, R6, R7, R8, D15 |
| Architecture | D4, D5, D6 |
| Blueprinting | D7 (all pages -- check D4 for page list) |
| Content | D2, D3, D8 (all pages), D9, D12 |
| Audit | D10 |

For each required document in this phase:
- Check the Document Log for its status
- A phase is complete when ALL required documents have status `complete`
- For multi-instance documents (D7, D8): all page variants must be complete

**If phase is now complete:**
- Set the Completed date in the Phase Log to today's date
- Report phase completion to the operator (see output format)

---

## Step 5: Status Regression Warning

If the registry currently shows a document as `complete` and the update would set it to `in-progress` or `needs-revision`:
- Warn the operator: "Document [code] is currently 'complete'. Updating to '[new status]' represents a status regression."
- Proceed with the update (the caller explicitly requested this status)

---

## Step 6: Check Compression Status

After updating the registry, check if a `.raw.md` companion exists for the document:
- If yes: note "(compressed)" in the output report
- If no: no action needed

---

## Output Format

```
Registry updated:
  Document: [Doc ID] - [title]
  Status: [old status] -> [new status]
  File: [file path]
  Phase: [phase name] ([started/in-progress/complete])
```

**If phase completed, add:**

```
Phase [phase name] complete.
Documents eligible for compression:
  - [Doc ID]: [file path]
  - [Doc ID]: [file path]

Run /webtools-init-compress to compress these documents for downstream efficiency.
```

**If status regression occurred, add:**

```
[WARN] Status regression: [Doc ID] was 'complete', now '[new status]'.
```

---

## Boundaries

- Only modify `project-registry.md` -- do not modify any other files
- Do not trigger compression automatically -- only report that it is available
- Do not create documents -- only update the registry to reflect document state
- Do not delete registry rows -- only add or update
- Verify file existence before updating (do not create ghost entries)

# Lifecycle: Completion Sequence

Canonical 4-step completion sequence. Every webtools plugin embeds this in its system prompt as an "After you finish" instruction block.

---

## Customization Points

Each plugin replaces these placeholders when embedding:

- `{{PLUGIN_NAME}}` -- The plugin name (e.g., "webtools-brand")
- `{{OUTPUT_SPEC}}` -- Output file path(s) and D-number(s)
- `{{OUTPUT_DIR}}` -- Subdirectory for output
- `{{DOWNSTREAM_DOCS}}` -- List of downstream documents affected by this output
- `{{PHASE_NAME}}` -- Which pipeline phase this plugin belongs to

---

## Completion Instructions (embed in every plugin prompt)

**After you finish producing output, execute these 4 steps in order:**

### Step 1: File Naming Validation

Verify the output file follows naming conventions:

- Pattern: `D{number}-{type}-{page-slug}.md`
- File is in the correct subdirectory (`{{OUTPUT_DIR}}/`)
- Single-instance documents (D1-D6, D9-D12): no page slug
- Multi-instance documents (D7, D8): page slug is present and matches a page defined in D4: Site Architecture
- Slug format: lowercase, hyphens only, no spaces, no special characters

If naming is wrong, fix it before proceeding.

### Step 2: Registry Update

Open `project-registry.md` and update:

**Document Log:**
- If this is a new document: add a row with status `complete`, set Created and Updated dates to today, set Created By to `{{PLUGIN_NAME}}`
- If this is an update to an existing document: change status to `complete`, update the Updated date, keep Created date and Created By unchanged
- If the document was left incomplete (operator ended session mid-work): set status to `in-progress`

**Phase Log:**
- If this is the first plugin to run in the `{{PHASE_NAME}}` phase: add a new Phase Log row with Started date set to today
- Add `{{PLUGIN_NAME}}` to the Plugins Used column for the current phase
- If all expected outputs for the phase are complete: set the Completed date

### Step 3: Cross-Reference Integrity Check

For multi-instance documents (D7, D8):
- Read the page list from D4: Site Architecture
- Verify that every page in D4 has a corresponding file, or is explicitly not-yet-created in the registry
- Flag any orphan files: files that exist in the directory but are NOT tracked in the registry
- Flag any ghost entries: registry rows that point to files that do not exist on disk

For single-instance documents: skip this step.

### Step 4: Downstream Impact Notification

Using the dependency map, notify the operator which downstream documents may need updating:

```
[D-number]: [Document Name] is complete.
Downstream documents that may need updating:
{{DOWNSTREAM_DOCS}}
```

Recommended next steps: [list the logical next plugins to run based on pipeline flow]

This is informational only. Never automatically trigger downstream tools.

---

## Notes

- All 4 steps are mandatory after every output, even partial outputs.
- Step 2 keeps the registry as the single source of truth. Never skip it.
- Step 3 only applies to D7 and D8 (multi-instance). All other documents skip it.
- Step 4 helps the operator understand cascade impact. It does not enforce anything.

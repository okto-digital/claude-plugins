# Lifecycle: Startup Sequence

Canonical 5-step startup sequence. Every webtools plugin embeds this in its system prompt as a "Before you do anything" instruction block.

---

## Customization Points

Each plugin replaces these placeholders when embedding:

- `{{PLUGIN_NAME}}` -- The plugin name (e.g., "webtools-brand")
- `{{PLUGIN_LABEL}}` -- Human-readable label (e.g., "Brand Voice Creator")
- `{{REQUIRED_INPUTS}}` -- List of required D-documents with paths
- `{{OPTIONAL_INPUTS}}` -- List of optional D-documents with paths
- `{{OUTPUT_SPEC}}` -- Output file path(s) and D-number(s)
- `{{OUTPUT_DIR}}` -- Subdirectory for output (e.g., "brand")

---

## Startup Instructions (embed in every plugin prompt)

**Before you do any work, execute these 5 steps in order:**

### Step 1: Registry Check

Read `project-registry.md` in the working directory root.

- If it does NOT exist: This is a new project. Create `project-registry.md` using the standard template. Prompt the operator for project info (client name, project type). Populate the Document Log with all single-instance D-documents set to status `--`.
- If it DOES exist: Parse the Document Log and Phase Log to understand current project state.

### Step 2: Directory Validation

Check that all 8 required subdirectories exist:
- `brief/`
- `brand/`
- `seo/`
- `architecture/`
- `blueprints/`
- `content/`
- `audit/`
- `research/`

If any directory is missing, create it silently. Never fail because a directory does not exist.

### Step 3: Input Validation

**Required inputs:** `{{REQUIRED_INPUTS}}`

For each required input document:
1. Check if the file exists at its expected path.
2. Check its status in the registry.
3. If the file is MISSING: notify the operator clearly.
   ```
   Required document [D-number]: [Document Name] is not available.
   - It should be created using: [plugin-name] ([component type])
   - You can: (a) Switch to create it first, or (b) Proceed without it (output quality may be reduced)
   ```
4. If the file EXISTS but status is `in-progress`: warn the operator.
   ```
   [D-number]: [Document Name] exists but status is "in-progress".
   - Working with the current version. Output may need updating after [D-number] is finalized.
   ```
5. If the file EXISTS but status is `needs-revision`: warn the operator.
   ```
   [D-number]: [Document Name] is marked as "needs-revision".
   - Proceeding with current version. Review output after [D-number] is updated.
   ```

**Optional inputs:** `{{OPTIONAL_INPUTS}}`

For each optional input document:
- If it exists: load it silently for additional context.
- If it does not exist: skip silently. No notification needed.

### Step 4: Output Preparation

Output target: `{{OUTPUT_SPEC}}`

- Determine the output file path based on naming conventions.
- If the output file already exists: warn the operator.
  ```
  [D-number]: [Document Name] already exists (status: [status], last updated [date]).
  Do you want to overwrite it or create a revision?
  ```
- If the output file does not exist: proceed normally.

### Step 5: Status Report

Present a brief summary before starting work:

```
Project: [Client Name]
Phase: [Current Phase]
Required inputs found: [list with status]
Optional inputs loaded: [list]
Optional inputs not available: [list]
Output: [filename] (new / overwrite)

Ready to proceed.
```

---

## Notes

- Steps 1-5 run every time, even if the plugin was used in the same session before.
- Step 1 creates the registry if missing. This means any plugin can be the first one run on a new project.
- Step 3 informs but does not block. The operator always decides whether to proceed.
- The status report in Step 5 gives the operator a chance to abort before work begins.

---
description: "webtools-init: Run full project health check"
allowed-tools: Read, Glob, Grep
---

Run a comprehensive, read-only health check on the current webtools project. Do NOT modify any files. Present all findings as console output.

## Prerequisite

Read `project-registry.md` in the current working directory. If it does not exist, report "No project found in this directory. Run /webtools-init first." and stop immediately.

Parse the Document Log and Phase Log from the registry for use in subsequent checks.

## Check 1: Directory Integrity

Verify these 7 subdirectories exist in the current working directory:
`brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`

Report the count of directories present out of 7. List any missing directories. Mark [PASS] if all 7 exist, [FAIL] if any are missing.

## Check 2: Orphan Files

Scan all 7 subdirectories for `.md` files. For each file found, check if a corresponding row exists in the Document Log (match by file path). Report any files that exist on disk but are NOT tracked in the registry. Mark [PASS] if none found, [FAIL] if any orphans exist.

## Check 3: Ghost Entries

For each row in the Document Log with a status other than `--`, check if the referenced file actually exists on disk at the listed path. Report any registry entries that point to non-existent files. Mark [PASS] if none found, [FAIL] if any ghosts exist.

## Check 4: File Naming Validation

For every `.md` file found in the subdirectories, verify the filename follows the naming convention from `${CLAUDE_PLUGIN_ROOT}/references/naming-conventions.md`:
- Starts with `D{number}-`
- Uses lowercase and hyphens only
- Single-instance documents have no page slug
- Multi-instance documents (D7, D8) include a page slug
- File is in the correct subdirectory for its D-number

Report any violations with the filename and the specific rule broken. Mark [PASS] if all files comply, [FAIL] if any violate naming rules.

## Check 5: Document Header Validation

For every `.md` file found in the subdirectories, read the beginning of the file and verify YAML frontmatter is present with the required fields per `${CLAUDE_PLUGIN_ROOT}/references/document-headers.md`:
- `document_id`
- `title`
- `project`
- `created`
- `updated`
- `created_by`
- `status`
- `dependencies`

Report any files with missing or malformed headers, listing the specific fields that are missing. Mark [PASS] if all headers are complete, [WARN] if any have issues.

## Check 6: Page Slug Consistency

Check if `architecture/D4-site-architecture.md` exists. If it does not, report "D4 not available -- skipping slug consistency check" and mark [PASS].

If D4 exists, extract the page list and URL slugs from it. Then:
- Check every D7 file in `blueprints/` -- its page slug must match a page in D4
- Check every D8 file in `content/` (excluding D9) -- its page slug must match a page in D4
- Report any slug mismatches
- Report D7 blueprints that have no corresponding D8 content file (coverage gaps)
- Report D8 content files that have no corresponding D7 blueprint

Mark [PASS] if all slugs match and coverage is complete, [WARN] if there are coverage gaps, [FAIL] if there are slug mismatches.

## Check 7: Dependency Freshness

For each document that exists on disk, read its `updated` date from the YAML header. Then consult `${CLAUDE_PLUGIN_ROOT}/references/dependency-map.md` to identify its dependencies. For each dependency that also exists on disk, compare the `updated` dates. If any dependency has been updated more recently than the document itself, the document is stale.

Report stale documents with the specific dependency that is newer. Mark [PASS] if no stale documents, [WARN] if any are stale.

## Check 8: Status Consistency

Cross-reference registry status values against file existence:
- A file that exists on disk should NOT have status `--` in the registry
- A registry entry with status `complete` or `in-progress` should have a corresponding file on disk
- A registry entry with status `needs-revision` should have a corresponding file on disk

Report any inconsistencies. Mark [PASS] if all consistent, [FAIL] if any mismatch.

## Output Format

Present the results as a single structured report:

```
PROJECT HEALTH CHECK: [Client Name from registry]
Date: [today's date]

[PASS/FAIL] Directory integrity: [n]/7 directories present
[PASS/FAIL] Orphan files: [details]
[PASS/FAIL] Ghost entries: [details]
[PASS/FAIL] File naming: [details]
[PASS/WARN] Document headers: [details]
[PASS/WARN/FAIL] Page slug consistency: [details]
[PASS/WARN] Dependency freshness: [details]
[PASS/FAIL] Status consistency: [details]

Summary: [n] passed, [n] failed, [n] warnings
```

For any non-PASS check, list each specific issue indented under the check header.

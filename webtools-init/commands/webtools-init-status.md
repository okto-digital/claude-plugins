---
description: "webtools-init: Show current project status and next steps"
allowed-tools: Read
---

Display a compact project status overview. Read-only -- do not modify any files.

## Step 1: Load Registry

Read `project-registry.md` in the current working directory. If it does not exist, report "No project found. Run /webtools-init first." and stop.

Parse the Project Info, Document Log, and Phase Log sections.

## Step 2: Display Project Info

```
PROJECT STATUS: [Client Name]
Type: [project type]   Phase: [current phase]   Status: [project status]
```

## Step 3: Display Document Status by Phase

Present the Document Log grouped by pipeline phase. Use these status markers:
- `[--]` not started
- `[IP]` in-progress
- `[OK]` complete
- `[REV]` needs-revision

```
DISCOVERY
  [OK] D11  Client Questionnaire
  [OK] D1   Project Brief

RESEARCH
  [OK] D2   Brand Voice Profile
  [--] D3   SEO Keyword Map
  [OK] D5   Competitor Analysis
  [--] D6   Content Inventory

ARCHITECTURE
  [IP] D4   Site Architecture

BLUEPRINTING
  [OK] D7   Blueprint: Homepage
  [--] D7   Blueprint: About
  [--] D7   Blueprint: Services

CONTENT
  [--] D8   Content: Homepage
  [--] D9   Microcopy

AUDIT
  [--] D10  Content Audit Report
```

Adapt the list dynamically to match the actual Document Log. Multi-instance documents (D7, D8) show one line per existing row. Omit D12 from the display if its status is `--` (it is an external import).

## Step 4: Display Phase Progress

```
PHASES
  [OK] Discovery        Started: 2026-02-16  Completed: 2026-02-17
  [IP] Research          Started: 2026-02-18  Completed: --
  [--] Architecture
  [--] Blueprinting
  [--] Content
  [--] Audit
```

Use `[OK]` for phases with a Completed date, `[IP]` for phases with a Started date but no Completed date, `[--]` for phases not yet started.

## Step 5: Display Completion Stats

Count documents by status across the entire Document Log:

```
PROGRESS: 4 complete, 1 in-progress, 7 not started  (4/12)
```

The denominator counts all rows in the Document Log (including multi-instance D7/D8 rows if they exist).

## Step 6: Suggest Next Actions

Read the dependency map from `${CLAUDE_PLUGIN_ROOT}/references/dependency-map.md`.

For each document with status `--` (not started), check if all its required inputs have status `complete`. If so, it is ready to create.

```
READY TO CREATE
  D3  SEO Keyword Map         -> use: webtools-seo
  D6  Content Inventory        -> use: webtools-inventory
  D4  Site Architecture        -> use: webtools-architecture (D3, D5, D6 optional)
```

If no documents are ready (all blocked by missing dependencies), show the blocking dependencies instead:

```
BLOCKED -- Next documents need:
  D7  Page Blueprints          -> needs: D4 (not started)
  D8  Page Content             -> needs: D7 (not started), D2 (not started)
```

If all documents are complete, show:

```
ALL DOCUMENTS COMPLETE
  Run /webtools-audit to generate the Content Audit Report, or /webtools-init-health for a final integrity check.
```

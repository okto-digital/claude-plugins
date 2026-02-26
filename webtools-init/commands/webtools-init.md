---
description: "webtools-init: Show available commands and project state, or initialize a new project"
allowed-tools: Read, Write, Glob, Bash(mkdir:*)
---

Show available webtools-init commands and current project state. If no project exists, offer to initialize one.

---

## Step 1: Check for Existing Project

Read `project-registry.md` in the current working directory.

- If the file EXISTS: go to **Orientation Display**.
- If the file does NOT exist: go to **Initialize New Project**.

---

## Orientation Display

### 1. Parse Project State

From the registry, extract:
- Client name and project type from Project Info
- Current phase and project status
- Document Log: count documents by status (complete, in-progress, not started where status is `--`)

### 2. Show Overview

```
[INIT] Webtools Init -- [client name]

Commands:
  /webtools-init              Show this overview (or initialize new project)
  /webtools-init-status       Show project status dashboard
  /webtools-init-health       Run project health check
  /webtools-init-rebuild      Rebuild project registry from disk scan

Reference files bundled with this plugin:
  lifecycle-startup.md        Startup sequence template for plugin builders
  lifecycle-completion.md     Completion sequence template for plugin builders
  registry-template.md        Empty registry template
  document-headers.md         YAML frontmatter spec for all D-documents
  dependency-map.md           Full document dependency graph
  naming-conventions.md       File naming and directory mapping rules

Current state:
  Project: [client name] ([project type])
  Phase: [current phase]
  Documents: [X complete, Y in-progress, Z not started]

Suggested next step: /webtools-init-status for detailed progress,
or /webtools-init-health for integrity check.
```

Stop here. Do not proceed to initialization.

---

## Initialize New Project

### 1. Gather Project Info

Ask the operator for:
1. **Client name** -- the name of the client or project (e.g., "Apex Consulting")
2. **Project type** -- one of: `new-build`, `redesign`, `landing-page`, `ecommerce`

Do not proceed until both values are provided.

### 2. Create Directory Structure

Create these 7 subdirectories in the current working directory (skip any that already exist):

- `brief/`
- `brand/`
- `seo/`
- `architecture/`
- `blueprints/`
- `content/`
- `audit/`

### 3. Create Project Registry

Read the registry template from `${CLAUDE_PLUGIN_ROOT}/references/registry-template.md`.

Replace the placeholders:
- `{{CLIENT_NAME}}` with the client name from step 1
- `{{PROJECT_TYPE}}` with the project type from step 1
- `{{DATE}}` with today's date in YYYY-MM-DD format

Write the result to `project-registry.md` in the current working directory.

### 4. Confirm and Guide

Present a summary to the operator:

```
Project initialized successfully.

  Project: [client name]
  Type: [project type]
  Registry: project-registry.md
  Directories: brief/, brand/, seo/, architecture/, blueprints/, content/, audit/

Next step: Run /webtools-intake-questionnaire to generate client intake questions,
or /webtools-intake-brief to create D1: Project Brief.
```

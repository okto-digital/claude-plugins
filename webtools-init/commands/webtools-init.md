---
description: Initialize a new webtools website project
allowed-tools: Read, Write, Bash(mkdir:*)
---

Initialize a new website project for the webtools pipeline. This sets up the folder structure and project registry in the current working directory.

## Step 1: Check for Existing Project

Read `project-registry.md` in the current working directory.

- If the file exists: warn the operator that this directory already contains a project. Show the existing client name and project type from the registry. Ask if they want to reinitialize (this will overwrite the registry). If they decline, stop.
- If the file does not exist: proceed to Step 2.

## Step 2: Gather Project Info

Ask the operator for:
1. **Client name** -- the name of the client or project (e.g., "Apex Consulting")
2. **Project type** -- one of: `new-build`, `redesign`, `landing-page`, `ecommerce`

Do not proceed until both values are provided.

## Step 3: Create Directory Structure

Create these 7 subdirectories in the current working directory (skip any that already exist):

- `brief/`
- `brand/`
- `seo/`
- `architecture/`
- `blueprints/`
- `content/`
- `audit/`

## Step 4: Create Project Registry

Read the registry template from `${CLAUDE_PLUGIN_ROOT}/references/registry-template.md`.

Replace the placeholders:
- `{{CLIENT_NAME}}` with the client name from Step 2
- `{{PROJECT_TYPE}}` with the project type from Step 2
- `{{DATE}}` with today's date in YYYY-MM-DD format

Write the result to `project-registry.md` in the current working directory.

## Step 5: Confirm and Guide

Present a summary to the operator:

```
Project initialized successfully.

  Project: [client name]
  Type: [project type]
  Registry: project-registry.md
  Directories: brief/, brand/, seo/, architecture/, blueprints/, content/, audit/

Next step: Run /questionnaire to generate client intake questions,
or start the Brief Generator agent to create D1: Project Brief.
```

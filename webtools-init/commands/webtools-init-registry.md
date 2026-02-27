---
description: "webtools-init: Update project registry after document production"
allowed-tools: Read, Write, Glob
---

Update project-registry.md after producing a document.

## Usage

`/webtools-init-registry [document-code] [status] [--plugin PLUGIN] [--phase PHASE] [--path PATH]`

Examples:
- `/webtools-init-registry D1 complete --plugin webtools-intake --phase discovery --path brief/D1-project-brief.md`
- `/webtools-init-registry R3 complete --plugin webtools-research --phase research --path research/R3-audience-personas.md`
- `/webtools-init-registry D7-homepage in-progress --plugin webtools-blueprint --phase blueprinting --path blueprints/D7-blueprint-homepage.md`

If arguments are missing, ask the operator for the required information.

## Instructions

@agents/registry-updater.md

Execute the registry updater with the provided arguments. Parse document code, status, plugin name, phase name, and file path from the arguments.

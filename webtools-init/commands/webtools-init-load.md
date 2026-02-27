---
description: "webtools-init: Load prerequisite documents for downstream work"
allowed-tools: Read, Glob
---

Load prerequisite documents into context. Serves compressed versions when available.

## Usage

`/webtools-init-load [document-codes...]`

Examples:
- `/webtools-init-load D1 D14` -- load project brief and client research
- `/webtools-init-load D1 D14 R1 D15` -- load intake + research prerequisites
- `/webtools-init-load D1:optional D14:optional` -- mark both as optional

Codes without a flag are treated as required. Append `:optional` to mark as optional.

If no arguments are provided, ask the operator which documents to load.

## Instructions

@agents/prerequisite-loader.md

Execute the prerequisite loader with the provided document codes. Parse the required/optional flags from the arguments.

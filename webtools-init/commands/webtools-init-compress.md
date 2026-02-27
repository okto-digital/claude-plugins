---
description: "webtools-init: Compress a webtools document to reduce token consumption"
allowed-tools: Read, Write, Glob
---

Compress a webtools document to reduce token consumption while preserving all data points.

## Usage

`/webtools-init-compress [document-code or path]`

Examples:
- `/webtools-init-compress D1` -- compress the project brief
- `/webtools-init-compress R3` -- compress the audience personas research
- `/webtools-init-compress brief/D1-project-brief.md` -- compress by path

If no argument is provided, ask the operator which document to compress.

## Instructions

@agents/document-compressor.md

Execute the document compressor with the provided document code or path.

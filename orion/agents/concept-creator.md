---
name: concept-creator
description: |
  Single-purpose sub-agent that produces one concept section from pre-merged project context.
  Spawned in parallel (up to 9 instances across 3 waves) by the concept-creation skill via dispatch-subagent.
  NOT invoked directly by the operator.
tools:
  - Read
  - Write
mcpServers: []
---

# Concept Creator

Produce one concept section by synthesising pre-merged project context into concrete, evidence-based recommendations. Every recommendation must trace back to a specific research finding, gap analysis answer, or client statement.

## Input

The dispatch prompt provides:
- **C-code and slug** (e.g., "C1", "Sitemap")
- **Concept definition** — full content of the section definition file (purpose, methodology), inlined in the prompt
- **Output template** — full content of the section template file (JSON schema, markdown template), inlined in the prompt
- **Context file path** — path to the pre-merged context JSON file containing all relevant R-files, G-files, upstream C-files, and D1

## Process

### 1. Read definition and template

Both are provided inline in your dispatch prompt. From the definition, extract purpose, scope, and methodology. From the template, extract the JSON schema and markdown format.

### 2. Read context file

Read the context file at the provided path. It is a keyed JSON object where each key is a document code (e.g., "D1-Init", "R2-Keywords", "G17-SEO", "C1-Sitemap") and each value is the full document content. All relevant project data for this section has been pre-selected and merged — you do not need to select or search for files.

### 3. Synthesise and produce output

Follow the methodology in the concept definition file. Produce recommendations grounded in evidence from the context file. For each recommendation, note which source it derives from (e.g., "R3-Competitors gap analysis", "G17-SEO checkpoint: keyword targeting", "client answer in G05-Business").

Use data from all documents in the context file — each was included because it is relevant to this section.

### 4. Write output

Write output using the JSON schema and markdown template from the output template.
- **JSON:** Write `{working_directory}/concept/{C-code}-{slug}.json` as a single line (no newlines, no indentation). Example path: `{working_directory}/concept/C1-Sitemap.json`. Use the absolute working directory path from your dispatch prompt.
- **Markdown:** Write `{working_directory}/concept/{C-code}-{slug}.md` from the JSON

## Rules

<critical>
- **NEVER** fabricate evidence or invent research findings
- **NEVER** make recommendations without traceable source references
- **ALWAYS** read the context file provided in the dispatch prompt
- **ALWAYS** write JSON as a SINGLE LINE — no newlines, no indentation, no spaces after colons or commas. The entire .json file must be one line.
</critical>

- If a document in the context file has no relevant data for your section, note it and continue
- Log cross-section observations in the `notes` array
- Return the full result to the orchestrator — do not summarise

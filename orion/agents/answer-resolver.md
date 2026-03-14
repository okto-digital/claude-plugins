---
name: answer-resolver
description: |
  Revise one domain's gap analysis findings after mechanical answer insertion.
  Produces coherent evidence text and updated summary.
  Spawned in parallel by domain-gap-analysis skill via dispatch-subagent.
  NOT invoked directly by the operator.
tools:
  - Read
  - Write
mcpServers: []
---

# Answer Resolver

## Input

The dispatch prompt provides:
- **G-file path** — absolute path to the domain's JSON file (already has mechanical insertions)
- **Markdown path** — absolute path to the domain's markdown file

## Process

### 1. Read and identify

Read the G-file JSON. Findings needing revision have `evidence` starting with `"Client:"` (mechanical insert) or `reason` of `"Not applicable (client)"`.

### 2. Rewrite evidence

For each `"Client:"` finding, rewrite into coherent evidence. Preserve factual content, append `"(client response)"`, keep under 2 sentences.

Examples:
- `"Client: WordPress"` → `"Client confirmed WordPress as current CMS platform (client response)"`
- `"Client: B2B SaaS, ~€2M revenue"` → `"B2B SaaS model, approximately €2M annual revenue (client response)"`

For N/A findings: leave `"Not applicable (client)"` as-is unless clearly incoherent.

### 3. Update summary and verify counts

Rewrite `summary` to reflect post-resolution state (1-2 sentences). Recalculate all count fields from findings — fix any mismatches. Leave `questions_resolved` as-is (set by resolve-answers.sh).

### 4. Write output

- **G-file:** Write updated JSON to same path, minified single line
- **Markdown:** Regenerate from JSON using the same format as the original (see domain-output-template.md active domain format). Overwrite existing file.

Return: domain name, findings revised count, updated counts.

## Rules

<critical>
- NEVER invent evidence beyond what the client stated
- NEVER change finding status — only rewrite evidence/reason text
- NEVER modify findings without `"Client:"` prefix in evidence
- ALWAYS write JSON as a SINGLE LINE — no newlines, no indentation
- ALWAYS escape special characters in JSON string values: `"` → `\"`, `\` → `\\`, literal newlines → `\n`, tabs → `\t`
- ALWAYS verify bracket closure before writing: every `{` has `}`, every `[` has `]`
- NEVER leave trailing commas in arrays or objects
</critical>

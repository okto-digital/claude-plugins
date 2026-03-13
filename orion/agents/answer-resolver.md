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

### 1. Read the G-file

Read the JSON. Identify findings that need revision:
- Findings where `evidence` starts with `"Client:"` — mechanically inserted, needs rewriting
- Findings where `reason` is `"Not applicable (client)"` — may need minor refinement

### 2. Rewrite evidence text

For each finding with `"Client:"` evidence:
- Rewrite into coherent, professional evidence text
- Preserve the factual content — do not add or infer beyond what the client stated
- Append `"(client response)"` attribution
- Keep under 2 sentences

**Examples:**
- `"Client: WordPress"` → `"Client confirmed WordPress as current CMS platform (client response)"`
- `"Client: B2B SaaS with annual contracts, ~€2M revenue"` → `"B2B SaaS model with annual contract structure, approximately €2M annual revenue (client response)"`
- `"Client: 3 main competitors: X, Y, Z"` → `"Three primary competitors identified: X, Y, Z (client response)"`

For N/A findings with `"Not applicable (client)"`:
- Leave reason as-is unless it is clearly incoherent — the mechanical text is already clear

### 3. Update summary

Rewrite the `summary` field to reflect the post-resolution state:
- Reference the updated counts (found/partial/gap)
- Note client-resolved items if they changed the domain's overall picture
- Keep to 1-2 sentences

### 4. Verify counts

Recalculate all count fields from findings. If any mismatch, correct them:
- `found`: findings with status FOUND
- `partial`: findings with status PARTIAL
- `gap`: findings with status GAP
- `na`: findings with status N/A
- `critical_resolved`: FOUND findings with CRITICAL priority
- `critical_total`: all findings with CRITICAL priority
- `questions_resolved`: leave as-is (set by resolve-answers.sh)

### 5. Write revised G-file

Write the updated JSON to the same path. Minified, single line.

### 6. Write revised markdown

Generate markdown from the revised JSON using this format:

**Active domain:**
```
## {Domain Name}
**{domain-id}** — {found} FOUND, {partial} PARTIAL, {gap} GAP, {na} N/A | {critical_resolved}/{critical_total} CRITICAL resolved | {questions_generated} questions

### {Section Name}
- [FOUND] {checkpoint} — evidence: "{evidence}"
- [PARTIAL] {checkpoint} — evidence: "{evidence}"
- [GAP] {checkpoint} [{priority}]
- [N/A] {checkpoint} — reason: {reason}

---
```

Write to the markdown path, overwriting the existing file.

### 7. Return summary

Report: domain name, findings revised count, updated counts snapshot.

## Rules

<critical>
- NEVER invent evidence beyond what the client stated
- NEVER change finding status — only rewrite evidence/reason text
- NEVER modify findings that were NOT mechanically inserted (no "Client:" prefix)
- ALWAYS write JSON as a SINGLE LINE — no newlines, no indentation
- ALWAYS preserve the original section grouping order in markdown
</critical>

---
name: domain-finalizer
description: |
  Finalize one domain's gap analysis: rewrite client answer evidence, add TLDR,
  update summary and counts. Runs for ALL active domains after answer resolution.
  Spawned in parallel by domain-gap-analysis skill via dispatch-subagent.
  NOT invoked directly by the operator.
tools:
  - Read
  - Write
mcpServers: []
---

# Domain Finalizer

## Input

The dispatch prompt provides:
- **G-file path** — absolute path to the domain's JSON file (may have mechanical answer insertions)
- **Markdown path** — absolute path to the domain's markdown file

## Process

### 1. Read and assess

Read the G-file JSON. Identify:
- Findings with `evidence` starting with `"Client:"` (mechanical inserts needing rewrite)
- Overall domain state for TLDR generation

### 2. Rewrite client evidence

For each `"Client:"` finding, rewrite into coherent evidence. Preserve factual content, append `"(client response)"`, keep under 2 sentences.

Examples:
- `"Client: WordPress"` → `"Client confirmed WordPress as current CMS platform (client response)"`
- `"Client: B2B SaaS, ~€2M revenue"` → `"B2B SaaS model, approximately €2M annual revenue (client response)"`

For N/A findings from client: leave `"Not applicable (client)"` as-is.

Skip this step if no `"Client:"` findings exist.

### 3. Build TLDR

Distill the domain's findings into a `tldr` array — compressed intelligence for downstream phases (concept creation, proposal).

**Selection filter:** "Would this change what we propose, how we design it, or what we prioritize?" If yes → include.

**What to capture:**
- Key FOUND findings that confirm or constrain the approach
- Resolved gaps with their answers (what was decided)
- Remaining gaps that downstream phases must accommodate
- Cross-checkpoint patterns (e.g., "3/4 security checkpoints are gaps — full security overhaul needed")

**Format rules:**
- 5-10 items per domain
- One finding = one self-contained line
- Numbers over adjectives
- Name the implication
- Telegraphic style, no prose

### 4. Update summary and counts

Rewrite `summary` to reflect finalized state (1-2 sentences). Recalculate all count fields from findings — fix any mismatches.

### 5. Write output

- **G-file:** Write updated JSON to same path, minified single line. `tldr` is the first field.
- **Markdown:** Regenerate from JSON using the domain-output-template active domain format (TLDR section first, then findings by section). Overwrite existing file.

Return: domain name, findings revised count, TLDR item count, updated counts.

## Rules

<critical>
- NEVER invent evidence beyond what exists in findings or client responses
- NEVER change finding status — only rewrite evidence/reason text and add TLDR
- NEVER modify findings without `"Client:"` prefix in evidence
- ALWAYS produce a TLDR for every active domain, even those with no questions
- ALWAYS write JSON as a SINGLE LINE — no newlines, no indentation, no spaces after colons or commas
- ALWAYS escape special characters in JSON string values: `"` → `\"`, `\` → `\\`, literal newlines → `\n`, tabs → `\t`
- ALWAYS verify bracket closure before writing: every `{` has `}`, every `[` has `]`
- NEVER leave trailing commas: `[1,2,3]` not `[1,2,3,]`
- NEVER leave unquoted string values — all strings must be wrapped in `""`
</critical>

**Common JSON mistakes:** Client responses with quotes must be escaped as `\"`. Multi-sentence evidence — join into one line or use `\n`. Verify comma between every field in rewritten objects.

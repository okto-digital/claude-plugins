# Naming Conventions

File naming rules, slug format, and directory mapping for the webtools document pipeline.

---

## File Naming Pattern

All documents follow: `D{number}-{type}-{page-slug}.md`

| Component | Rule | Examples |
|-----------|------|---------|
| D-number | `D` followed by 1-2 digit number | `D1`, `D7`, `D10`, `D12` |
| Type | Lowercase, hyphens, describes the document | `project-brief`, `blueprint`, `content` |
| Page slug | Only for multi-instance docs (D7, D8). Matches URL slug from D4. | `homepage`, `about`, `service-web-development` |
| Extension | Always `.md` | -- |

## Single-Instance Documents (no page slug)

| Doc ID | Filename | Directory |
|--------|----------|-----------|
| D1 | `D1-project-brief.md` | `brief/` |
| D2 | `D2-brand-voice-profile.md` | `brand/` |
| D3 | `D3-seo-keyword-map.md` | `seo/` |
| D4 | `D4-site-architecture.md` | `architecture/` |
| D5 | `D5-competitor-analysis.md` | `architecture/` |
| D6 | `D6-content-inventory.md` | `architecture/` |
| D9 | `D9-microcopy.md` | `content/` |
| D10 | `D10-content-audit-report.md` | `audit/` |
| D11 | `D11-client-questionnaire.md` | `brief/` |
| D12 | `D12-seo-content-targets.md` | `seo/` |
| D13 | `D13-client-followup.md` | `brief/` |
| D14 | `D14-client-research-profile.md` | `brief/` |

## Multi-Instance Documents (with page slug)

| Doc ID | Filename Pattern | Directory |
|--------|-----------------|-----------|
| D7 | `D7-blueprint-{page-slug}.md` | `blueprints/` |
| D8 | `D8-content-{page-slug}.md` | `content/` |

## Slug Rules

Page slugs must:
- Be lowercase
- Use hyphens only (no underscores, spaces, or special characters)
- Be URL-friendly
- Match exactly the URL slugs defined in D4: Site Architecture
- Be consistent between D7 and D8 for the same page

**Valid slugs:** `homepage`, `about`, `service-web-development`, `case-study-apex-project`
**Invalid slugs:** `Home Page`, `about_us`, `service/web`, `Service-Page`

## Directory Structure

```
project-root/
├── project-registry.md
├── brief/              <- D1, D11, D13, D14
├── brand/              <- D2
├── seo/                <- D3, D12
├── architecture/       <- D4, D5, D6
├── blueprints/         <- D7 (multiple)
├── content/            <- D8 (multiple), D9
└── audit/              <- D10
```

## Compressed Document Convention (`.raw.md` suffix)

When a document has been compressed for token efficiency, two files exist:

| File | Content |
|------|---------|
| `D1-project-brief.md` | Compressed version (loaded by downstream plugins) |
| `D1-project-brief.raw.md` | Original verbose version (preserved for reference) |

The `.raw.md` suffix indicates the uncompressed original. Downstream plugins always load the standard path (without `.raw.md`) and automatically get the compressed version when available.

- `.raw.md` files are NOT tracked as separate rows in the registry
- `.raw.md` files are NOT flagged as orphans in health checks
- `.raw.md` files follow the same naming pattern as their companion, with `.raw.md` replacing `.md`
- The compressed file's YAML frontmatter includes `compressed: true` and `raw_file: [path to .raw.md]`

## Research Document Naming

Research documents follow a similar pattern but use `R` prefix:

| Doc ID | Filename | Directory |
|--------|----------|-----------|
| R1 | `R1-serp-landscape.md` | `research/` |
| R2 | `R2-competitor-landscape.md` | `research/` |
| R3 | `R3-audience-personas.md` | `research/` |
| R4 | `R4-ux-benchmarks.md` | `research/` |
| R5 | `R5-content-landscape.md` | `research/` |
| R6 | `R6-reputation-social.md` | `research/` |
| R7 | `R7-tech-performance.md` | `research/` |
| R8 | `R8-market-context.md` | `research/` |
| D15 | `D15-research-report.md` | `research/` |

## Validation Rules

1. Every file in the project (except `project-registry.md`) must start with `D{number}-` or `R{number}-`
2. Every file must be in its correct subdirectory per the mapping above
3. D7 and D8 page slugs must match pages defined in D4
4. No duplicate filenames within a directory
5. No files outside the defined subdirectories (except `project-registry.md` at root)
6. `.raw.md` files are valid companions and exempt from orphan checks

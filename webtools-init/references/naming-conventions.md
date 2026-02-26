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
├── brief/              <- D1, D11, D13
├── brand/              <- D2
├── seo/                <- D3, D12
├── architecture/       <- D4, D5, D6
├── blueprints/         <- D7 (multiple)
├── content/            <- D8 (multiple), D9
└── audit/              <- D10
```

## Validation Rules

1. Every file in the project (except `project-registry.md`) must start with `D{number}-`
2. Every file must be in its correct subdirectory per the mapping above
3. D7 and D8 page slugs must match pages defined in D4
4. No duplicate filenames within a directory
5. No files outside the defined subdirectories (except `project-registry.md` at root)

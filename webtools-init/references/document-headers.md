# Document Header Standard

Every document produced by any webtools plugin must begin with this YAML frontmatter block. This header enables any plugin to quickly identify, validate, and understand a document's context.

---

## Format

```yaml
---
document_id: D{number}
title: "{Document Title}"
project: "{Client Name}"
created: YYYY-MM-DD
updated: YYYY-MM-DD
created_by: webtools-{plugin-name}
status: complete
dependencies:
  - D{n}: /path/to/dependency.md
---
```

## Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| `document_id` | Yes | D-number identifier (D1-D14) |
| `title` | Yes | Human-readable document title. For multi-instance: include page name (e.g., "Page Blueprint: Homepage") |
| `project` | Yes | Client project name (must match registry) |
| `created` | Yes | Date first created (YYYY-MM-DD). Never changes after creation. |
| `updated` | Yes | Date last modified (YYYY-MM-DD). Changes on every update. |
| `created_by` | Yes | Plugin name that originally created the document (e.g., "webtools-brand") |
| `status` | Yes | Current status: `in-progress` or `complete` or `needs-revision` |
| `dependencies` | Yes | List of D-documents used as input. Format: `D{n}: /relative/path.md`. Empty list `[]` if no dependencies. |

## Per-Document Specifications

### D1: Project Brief
```yaml
document_id: D1
title: "Project Brief"
created_by: webtools-intake
dependencies: []
```
Note: D11 is optional input but not a formal dependency since D1 can be created without it.

### D2: Brand Voice Profile
```yaml
document_id: D2
title: "Brand Voice Profile"
created_by: webtools-brand
dependencies:
  - D1: /brief/D1-project-brief.md
```

### D3: SEO Keyword Map
```yaml
document_id: D3
title: "SEO Keyword Map"
created_by: webtools-seo
dependencies:
  - D1: /brief/D1-project-brief.md
```

### D4: Site Architecture
```yaml
document_id: D4
title: "Site Architecture"
created_by: webtools-architecture
dependencies:
  - D1: /brief/D1-project-brief.md
```
Note: D3, D5, D6 are optional inputs but not listed as dependencies unless actually used.

### D5: Competitor Analysis
```yaml
document_id: D5
title: "Competitor Analysis"
created_by: webtools-competitors
dependencies:
  - D1: /brief/D1-project-brief.md
```

### D6: Content Inventory
```yaml
document_id: D6
title: "Content Inventory"
created_by: webtools-inventory
dependencies:
  - D1: /brief/D1-project-brief.md
```

### D7: Page Blueprint (multi-instance)
```yaml
document_id: D7
title: "Page Blueprint: {Page Name}"
created_by: webtools-blueprint
dependencies:
  - D1: /brief/D1-project-brief.md
  - D4: /architecture/D4-site-architecture.md
```
Note: One file per page. Page slug in filename must match D4. Additional optional dependencies (D2, D3, D5, D6) listed only if actually used.

### D8: Page Content (multi-instance)
```yaml
document_id: D8
title: "Page Content: {Page Name}"
created_by: webtools-writer
dependencies:
  - D7: /blueprints/D7-blueprint-{page-slug}.md
  - D2: /brand/D2-brand-voice-profile.md
```
Note: One file per page. Page slug must match corresponding D7 and D4.

### D9: Microcopy
```yaml
document_id: D9
title: "Microcopy"
created_by: webtools-writer
dependencies:
  - D1: /brief/D1-project-brief.md
  - D2: /brand/D2-brand-voice-profile.md
  - D4: /architecture/D4-site-architecture.md
```

### D10: Content Audit Report
```yaml
document_id: D10
title: "Content Audit Report"
created_by: webtools-audit
dependencies:
  - D3: /seo/D3-seo-keyword-map.md
```
Note: D8 documents are primary inputs but listed per-page. D2, D5, D12 optional.

### D11: Client Questionnaire
```yaml
document_id: D11
title: "Client Questionnaire"
created_by: webtools-intake
dependencies: []
```

### D12: SEO Content Targets (External)
```yaml
document_id: D12
title: "SEO Content Targets"
created_by: external
dependencies: []
```
Note: Imported from external SEO tools. Not produced by any webtools plugin.

### D13: Client Follow-Up Questionnaire
```yaml
document_id: D13
title: "Client Follow-Up Questionnaire"
created_by: webtools-intake
dependencies:
  - D1: /brief/D1-project-brief.md
```
Note: Generated after meeting in REVIEW mode. Contains follow-up questions for unresolved gaps.

### D14: Client Research Profile
```yaml
document_id: D14
title: "Client Research Profile"
created_by: webtools-intake
dependencies: []
```
Note: Generated from public website crawl before the intake meeting. No dependencies -- works from a URL alone. Optional input to D1 via PREP mode.

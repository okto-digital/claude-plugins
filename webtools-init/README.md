# webtools-init

Project initialization, health checks, registry management, and shared utility agents for the webtools website creation pipeline.

## Overview

This plugin provides the foundation layer for the webtools suite. It creates project folder structures, manages the central project registry, provides diagnostic tools for maintaining project integrity, and bundles utility agents used by all webtools plugins. Load this plugin alongside any other webtools plugin.

## Commands

| Command | Description |
|---------|-------------|
| `/webtools-init` | Initialize a new project or show orientation (folder structure, registry, commands) |
| `/webtools-init-status` | Show project status dashboard with document progress and next actions |
| `/webtools-init-health` | Run comprehensive project health check (directories, registry, naming, headers, dependencies) |
| `/webtools-init-rebuild` | Rebuild project registry from disk scan (recovery tool) |
| `/webtools-init-crawl` | Crawl a URL and return clean markdown |
| `/webtools-init-compress` | Compress a document for token efficiency |
| `/webtools-init-load` | Load prerequisite documents for a downstream plugin |
| `/webtools-init-registry` | Update project registry after document production |

## Utility Agents

Bundled agents available to all webtools plugins via the Task tool:

| Agent | Description |
|-------|-------------|
| `web-crawler` | 7-method cascade web crawling |
| `document-compressor` | Reduce document verbosity, preserve substance |
| `prerequisite-loader` | Load documents with auto-compression detection |
| `registry-updater` | Update registry after document production |

## Reference Files

Canonical reference documents used by all webtools plugins:

| File | Purpose |
|------|---------|
| `references/lifecycle-startup.md` | 5-step startup sequence template |
| `references/lifecycle-completion.md` | 4-step completion sequence template |
| `references/registry-template.md` | Empty project registry template |
| `references/document-headers.md` | YAML frontmatter spec for all documents (D1-D15, R1-R8) |
| `references/dependency-map.md` | Full document dependency graph |
| `references/naming-conventions.md` | File naming and directory mapping rules |
| `references/compression-rules.md` | Compression strategy and rules |
| `references/crawl-methods/` | Web crawling method references (7 methods) |

## Usage

### Starting a New Project

```
/webtools-init
```

Creates 8 project directories (`brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`, `research/`) and the project registry. Prompts for client name and project type.

### Quick Status Check

```
/webtools-init-status
```

Shows document completion by phase, progress stats, and suggests which documents are ready to create next.

### Checking Project Health

```
/webtools-init-health
```

Runs 8 diagnostic checks: directory integrity, orphan files, ghost entries, file naming, document headers, page slug consistency, dependency freshness, and status consistency.

### Recovery

```
/webtools-init-rebuild
```

Scans all 8 project directories and rebuilds the registry. Use when the registry gets out of sync after manual file operations.

## Part of the Webtools Suite

This plugin is the foundation for the webtools website creation pipeline:

1. **webtools-init** (this plugin) -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-research** -- Research topics and consolidated report
4. **webtools-brand** -- Brand voice profiling
5. **webtools-seo** -- SEO keyword research
6. **webtools-competitors** -- Competitor site analysis
7. **webtools-inventory** -- Content inventory and migration
8. **webtools-architecture** -- Site structure planning
9. **webtools-blueprint** -- Page blueprint generation
10. **webtools-writer** -- Content and microcopy generation
11. **webtools-audit** -- Content quality auditing

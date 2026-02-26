# webtools-init

Project initialization, health checks, and registry management for the webtools website creation pipeline.

## Overview

This plugin provides the foundation layer for the webtools suite. It creates project folder structures, manages the central project registry, and provides diagnostic tools for maintaining project integrity. Load this plugin alongside any other webtools plugin.

## Commands

| Command | Description |
|---------|-------------|
| `/webtools-init` | Initialize a new project: create folder structure, registry, and prompt for project info |
| `/webtools-init-health` | Run comprehensive project health check (directories, registry, naming, headers, dependencies) |
| `/webtools-init-rebuild` | Rebuild project registry from disk scan (recovery tool) |
| `/webtools-init-status` | Show current project status, document progress, and suggested next actions |

## Reference Files

This plugin bundles canonical reference documents used by all webtools plugins:

| File | Purpose |
|------|---------|
| `references/lifecycle-startup.md` | 5-step startup sequence template |
| `references/lifecycle-completion.md` | 4-step completion sequence template |
| `references/registry-template.md` | Empty project registry template |
| `references/document-headers.md` | YAML frontmatter spec for all D-documents |
| `references/dependency-map.md` | Full document dependency graph |
| `references/naming-conventions.md` | File naming and directory mapping rules |

## Usage

### Starting a New Project

```
/webtools-init
```

Creates the project folder structure and registry in the current working directory. Prompts for client name and project type.

### Checking Project Health

```
/webtools-init-health
```

Runs 8 diagnostic checks: directory integrity, orphan files, ghost entries, file naming, document headers, page slug consistency, dependency freshness, and status consistency.

### Quick Status Check

```
/webtools-init-status
```

Shows document completion by phase, progress stats, and suggests which documents are ready to create next.

### Recovery

```
/webtools-init-rebuild
```

Scans all project files on disk and rebuilds the registry. Use when the registry gets out of sync after manual file operations.

## Part of the Webtools Suite

This plugin is the foundation for the webtools website creation pipeline:

1. **webtools-init** (this plugin) -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-brand** -- Brand voice profiling
4. **webtools-seo** -- SEO keyword research
5. **webtools-competitors** -- Competitor site analysis
6. **webtools-inventory** -- Content inventory and migration
7. **webtools-architecture** -- Site structure planning
8. **webtools-blueprint** -- Page blueprint generation
9. **webtools-writer** -- Content and microcopy generation
10. **webtools-audit** -- Content quality auditing

# Webtools Command Naming Convention

## Pattern

```
webtools-{plugin}-{action}
```

All webtools commands follow this pattern so they group together in the `/` autocomplete:

- **`webtools`** -- suite prefix, groups all webtools commands adjacently
- **`{plugin}`** -- the specific plugin (e.g., `intake`, `init`, `writer`, `audit`)
- **`{action}`** -- what the command does (e.g., `prep`, `meeting`, `status`, `export`)

When `{action}` is omitted, the command is the **orientation entry point** for that plugin (shows available workflows and current status).

## Rationale

When multiple webtools plugins are loaded in a cowork session, the `/` autocomplete shows all commands from all plugins. Without a naming convention, generic command names give no indication which plugin they belong to.

This convention:
- Groups all webtools commands together in alphabetical autocomplete
- Sub-groups by plugin within the webtools namespace
- Makes the plugin source immediately obvious to operators
- Provides a consistent orientation entry point per plugin

## Full Command Mapping

### webtools-init (4 commands)

| Command | File | Purpose |
|---|---|---|
| `/webtools-init` | `webtools-init.md` | Orientation: project setup and management |
| `/webtools-init-status` | `webtools-init-status.md` | Show project status dashboard |
| `/webtools-init-health` | `webtools-init-health.md` | Run project health check |
| `/webtools-init-rebuild` | `webtools-init-rebuild.md` | Rebuild project registry |

### webtools-intake (7 commands)

| Command | File | Purpose |
|---|---|---|
| `/webtools-intake` | `webtools-intake.md` | Orientation: intake workflows and project state |
| `/webtools-intake-questionnaire` | `webtools-intake-questionnaire.md` | Generate client intake questionnaire (D11) |
| `/webtools-intake-prep` | `webtools-intake-prep.md` | Pre-meeting data analysis and interview guide |
| `/webtools-intake-meeting` | `webtools-intake-meeting.md` | Live meeting companion (submarine mode) |
| `/webtools-intake-review` | `webtools-intake-review.md` | Post-meeting gap analysis and inference review |
| `/webtools-intake-brief` | `webtools-intake-brief.md` | Generate D1: Project Brief |

### webtools-writer (1 command)

| Command | File | Purpose |
|---|---|---|
| `/webtools-writer-export` | `webtools-writer-export.md` | Export content to HTML |

### webtools-audit (1 command)

| Command | File | Purpose |
|---|---|---|
| `/webtools-audit` | `webtools-audit.md` | Run content quality audit |

## Autocomplete Result

All 13 commands group together, sub-grouped by plugin:

```
/webtools-audit
/webtools-init
/webtools-init-health
/webtools-init-rebuild
/webtools-init-status
/webtools-intake
/webtools-intake-brief
/webtools-intake-meeting
/webtools-intake-prep
/webtools-intake-questionnaire
/webtools-intake-review
/webtools-writer-export
```

## Scope

This convention applies to **commands only**. Skills are already namespaced by plugin in the autocomplete (e.g., `webtools-writer:content-generator`). Agents are not directly invokable by operators and do not need naming changes.

## Future Plugins

When new webtools plugins add commands, they follow the same pattern:

- `webtools-brand` -- brand voice profiling commands
- `webtools-seo` -- SEO keyword research commands
- `webtools-architecture` -- site structure planning commands
- `webtools-blueprint` -- page blueprint commands

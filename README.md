# Oktodigital Plugins

Plugins built and maintained by Oktodigital. Built for Claude Cowork, also compatible with Claude Code.

## Installation

### Claude Code (CLI)

```bash
claude plugin marketplace add okto-digital/claude-plugins
claude plugin install oktodigital-brand-voice@oktodigital
```

### Claude Cowork

Install from the Cowork plugin interface or use the CLI commands above.

### Local development

Add to your Claude Code settings (`~/.claude/settings.json`):

```json
{
  "extraKnownMarketplaces": {
    "oktodigital": {
      "source": {
        "source": "directory",
        "path": "/path/to/claude-plugins"
      }
    }
  }
}
```

Then install any plugin:

```bash
claude plugin install oktodigital-brand-voice@oktodigital
```

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [oktodigital-brand-voice](./oktodigital-brand-voice) | Brand voice content generation with 15-dimension voice framework, 9 specialized skills, and website content workflow |

## Structure

```
claude-plugins/
├── .claude-plugin/
│   └── marketplace.json
├── oktodigital-brand-voice/
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   ├── commands/
│   ├── agents/
│   ├── hooks/
│   └── docs/
└── README.md
```

## Contributing

Each plugin lives at the repository root as `<plugin-name>/` and must include a valid `.claude-plugin/plugin.json` manifest. When adding a new plugin, also add its entry to the root `marketplace.json`.

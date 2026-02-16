# Oktodigital Claude Code Plugins

A marketplace of Claude Code plugins built and maintained by Oktodigital.

## Installation

### From GitHub (production)

```
/plugin install <plugin-name>@oktodigital
```

### From local directory (development)

Add to your Claude Code settings (`~/.claude/settings.json`):

```json
{
  "extraKnownMarketplaces": {
    "oktodigital": {
      "source": {
        "source": "directory",
        "path": "/path/to/oktodigital-marketplace"
      }
    }
  }
}
```

Then install any plugin:

```
/plugin install <plugin-name>@oktodigital
```

## Available Plugins

See [marketplace.json](.claude-plugin/marketplace.json) for the full list of available plugins.

## Structure

```
oktodigital-marketplace/
  .claude-plugin/
    marketplace.json          # Marketplace index
  plugins/
    <plugin-name>/
      .claude-plugin/
        plugin.json           # Plugin manifest
      skills/                 # Plugin skills
      commands/               # Plugin commands
      agents/                 # Plugin agents
      hooks/                  # Plugin hooks
      README.md
```

## Contributing

Each plugin lives in `plugins/<plugin-name>/` and must include a valid `.claude-plugin/plugin.json` manifest. When adding a new plugin, also add its entry to the root `marketplace.json`.

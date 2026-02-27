# webtools-seo

SEO keyword research for the webtools website pipeline.

## Overview

This plugin produces D3: SEO Keyword Map -- a structured document mapping keyword opportunities to pages with volume data, difficulty assessments, and intent classifications. It follows a structured methodology: seed generation, expansion, competitor analysis, clustering, and page mapping.

Supports three data tiers with graceful fallback: MCP SEO tools (DataForSEO / SE Ranking) for actual data, WebSearch for signal-based estimates, or industry knowledge estimates when no tools are available.

## Commands

| Command | Description |
|---------|-------------|
| `/webtools-seo` | Orientation: show commands, skills, data sources, and project state |
| `/webtools-seo-keywords` | Run keyword research to produce D3: SEO Keyword Map |

## Components

| Type | Name | Description |
|------|------|-------------|
| Skill | `seo-keyword-research` | Structured keyword research with clustering and page mapping |
| Command | `webtools-seo` | Orientation and status overview |
| Command | `webtools-seo-keywords` | Run keyword research (thin wrapper for skill) |
| Reference | `mcp-tool-mapping` | MCP tool specs for DataForSEO and SE Ranking |

## Data Tiers

The skill automatically detects available tools and selects the best data tier:

| Tier | Source | Volume Format | Difficulty Format | When |
|------|--------|---------------|-------------------|------|
| TIER 1 | DataForSEO or SE Ranking MCP | Actual integer (e.g., 2,400) | KD score 0-100 | MCP tools detected |
| TIER 2 | WebSearch signals | Estimated range (e.g., "Medium (~1K-3K est.)") | Low/Medium/High | No MCP, WebSearch available |
| TIER 3 | Industry knowledge | Low/Medium/High | Low/Medium/High | No tools available |

All tiers produce the same D3 document structure. A Source column in keyword tables shows where each data point came from.

## MCP Integration

### DataForSEO (preferred)

Add to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "dataforseo-mcp-server"],
      "env": {
        "DATAFORSEO_USERNAME": "your_api_login",
        "DATAFORSEO_PASSWORD": "your_api_password",
        "ENABLED_MODULES": "KEYWORDS_DATA,DATAFORSEO_LABS"
      }
    }
  }
}
```

Requires Node.js and a DataForSEO account. Guide: https://dataforseo.com/help-center/connect-claude-to-dataforseo-mcp-very-simple-guide

### SE Ranking

Add to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "seo-data-api-mcp": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "DATA_API_TOKEN",
        "se-ranking/seo-data-api-mcp-server"
      ],
      "env": {
        "DATA_API_TOKEN": "your_api_token"
      }
    }
  }
}
```

Requires Docker and an SE Ranking API token. Guide: https://seranking.com/api/integrations/mcp/

## Research Intelligence

When webtools-research has been run, the skill leverages:

| Document | What it provides |
|----------|-----------------|
| R1: SERP Landscape | SERP-derived seed keywords, competitor keyword patterns |
| R5: Content Strategy | Content gap terms, audience language, topic clusters |
| D15: Research Report | Strategic focus areas for priority alignment |

All optional. The skill silently skips any that are not available.

## Usage

Run `/webtools-seo` to see current status and suggested next step, then `/webtools-seo-keywords` to execute keyword research.

The skill will:

1. Load D1: Project Brief (required)
2. Detect available MCP tools and set data tier
3. Load research intelligence (R1, R5, D15 if available)
4. Gather research inputs (services, geographic focus, seed keywords, competitor URLs)
5. Generate and expand keyword seeds (MCP + research + manual)
6. Analyze competitor keyword usage
7. Cluster keywords by topic and intent
8. Assess volume and difficulty (per active tier)
9. Map clusters to target pages
10. Write D3 to `seo/D3-seo-keyword-map.md`

## Documents

| Doc ID | Document | File Path | Role |
|--------|----------|-----------|------|
| D1 | Project Brief | `brief/D1-project-brief.md` | Required input |
| R1 | SERP Landscape | `research/R1-serp-landscape.md` | Optional input (research intelligence) |
| R5 | Content Strategy | `research/R5-content-strategy.md` | Optional input (research intelligence) |
| D15 | Research Report | `research/D15-research-report.md` | Optional input (research intelligence) |
| D3 | SEO Keyword Map | `seo/D3-seo-keyword-map.md` | Output |

## Part of the Webtools Suite

1. **webtools-init** -- Project setup and management
2. **webtools-intake** -- Client questionnaire and brief generation
3. **webtools-research** -- Multi-topic research with parallel execution
4. **webtools-brand** -- Brand voice profiling
5. **webtools-seo** (this plugin) -- SEO keyword research
6. **webtools-competitors** -- Competitor site analysis
7. **webtools-inventory** -- Content inventory and migration
8. **webtools-architecture** -- Site structure planning
9. **webtools-blueprint** -- Page blueprint generation
10. **webtools-writer** -- Content and microcopy generation
11. **webtools-audit** -- Content quality auditing

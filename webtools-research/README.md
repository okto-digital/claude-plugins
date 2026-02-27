# webtools-research

Research phase intelligence gathering for the webtools website creation pipeline.

## What it does

Bridges the gap between intake (D1 Project Brief, D14 Client Research) and creation (architecture, blueprints, content). Runs systematic intelligence gathering across 8 research topics to inform proposals with real competitive data, audience insights, and market context rather than generic recommendations.

## Research Topics

| ID | Topic | Agent | Depth |
|---|---|---|---|
| R1 | SERP & Search Landscape | serp-researcher | 5-10 core queries + local |
| R2 | Competitor Landscape (Broad) | competitor-mapper | 8-15 players surface scan |
| R3 | Audience & User Personas | audience-researcher | Segments, personas, journey |
| R4 | UX/UI Patterns & Benchmarks | ux-benchmarker | Industry design patterns |
| R5 | Content Landscape & Strategy | content-strategist | Content ecosystem scan |
| R6 | Reputation & Social Proof | reputation-scanner | External signals scan |
| R7 | Technology & Performance | tech-auditor | PageSpeed + tech stack |
| R8 | Industry & Market Context | market-analyst | Market/regulatory scan |

## Output

- **R1-R8**: Individual research topic documents (saved to `research/`)
- **D15**: Consolidated Research Report with executive summary, strategic opportunities, and proposal inputs

## Installation

```
/plugin install webtools-research@oktodigital
```

## Commands

| Command | Purpose |
|---|---|
| `/webtools-research` | Orientation: show topics, status, suggestions |
| `/webtools-research-run` | Orchestrator: select topics, dispatch parallel, consolidate |
| `/webtools-research-serp` | Run R1 SERP & Search Landscape only |
| `/webtools-research-competitors` | Run R2 Competitor Landscape only |
| `/webtools-research-audience` | Run R3 Audience & User Personas only |
| `/webtools-research-ux` | Run R4 UX/UI Patterns only |
| `/webtools-research-content` | Run R5 Content Strategy only |
| `/webtools-research-reputation` | Run R6 Reputation & Social Proof only |
| `/webtools-research-tech` | Run R7 Technology & Performance only |
| `/webtools-research-market` | Run R8 Industry & Market Context only |
| `/webtools-research-consolidate` | Merge completed R-docs into D15 |

## Pipeline Position

```
D1 (Brief) + D14 (Client Research)
    |
RESEARCH PHASE (R1-R8, parallel)
    |
D15 (Research Report)
    |
Proposal writing
    |
Production deep-dives: D3, D5, D6
    |
D4, D7, D8, D10 (creation pipeline)
```

## Prerequisites

- Active webtools project with D1 Project Brief
- D14 Client Research Profile (recommended but not required)

# Project Init — Templates

## JSON Schema

```json
{
  "project": {
    "name": "string",
    "client": "string",
    "url": "string | null",
    "build_type": "new | redesign",
    "site_type": "string",
    "goal": "string",
    "languages": {"primary": "string", "other": []},
    "output_language": "string",
    "location": {"primary": "string", "other": []}
  },
  "research_config": {
    "research_depth": "basic | deep",
    "output_format": "verbose | concise",
    "serp_max_keywords": 50,
    "search_landscape_max_keywords": 100,
    "competitors_max": 5,
    "debug": "ask | true | false"
  },
  "pipeline_defaults": {
    "gap_domains": "ask | all | [list of domain codes]",
    "parallel_execution": "ask | true | false",
    "proposal_style": "ask | full | summary_only"
  },
  "notes": [
    "string",
    "string"
  ]
}
```

---

## Project State Template

```markdown
# Project: {project.client}

**Client:** {project.client}
**Type:** {project.build_type} | {project.site_type}
**Created:** {YYYY-MM-DD}

## Pipeline

| Phase | Name | Status | Output | Updated |
|---|---|---|---|---|
| 1 | INIT | complete | project.json, D1-Init.txt | {YYYY-MM-DD} |
| 2 | Client Intelligence | -- | -- | -- |
| 3 | Research | -- | -- | -- |
| 4 | Domain Gap Analysis | -- | -- | -- |
| 5 | Concept Creation | -- | -- | -- |
| 6 | Proposal & Brief | -- | -- | -- |

## Research Substages

| Sub | Name | Code | Status | Output | Updated |
|---|---|---|---|---|---|
| 3.1 | Client Website Inventory | R1-Inventory | -- | -- | -- |
| 3.2 | SERP & Search Landscape | R2-SERP | -- | -- | -- |
| 3.3 | Keyword Opportunity | R3-Keywords | -- | -- | -- |
| 3.4 | Competitor Landscape | R4-Competitors | -- | -- | -- |
| 3.5 | Industry & Market Context | R5-Market | -- | -- | -- |
| 3.6 | Audience & Personas | R6-Audience | -- | -- | -- |
| 3.7 | Reputation & Social Proof | R7-Reputation | -- | -- | -- |
| 3.8 | Technology & Performance | R8-Technology | -- | -- | -- |
| 3.9 | UX/UI Patterns | R9-UX | -- | -- | -- |
| 3.10 | Content Landscape & Strategy | R10-Content | -- | -- | -- |
```

Phase 1 (INIT) is marked `complete` immediately — producing project.json, D1-Init.txt, and baseline-log.txt IS the INIT phase output.

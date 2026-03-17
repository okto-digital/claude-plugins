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
| 3.1 | SERP & Search Landscape | R1-SERP | -- | -- | -- |
| 3.2 | Keyword Opportunity | R2-Keywords | -- | -- | -- |
| 3.3 | Competitor Landscape | R3-Competitors | -- | -- | -- |
| 3.4 | Industry & Market Context | R4-Market | -- | -- | -- |
| 3.5 | Technology & Performance | R5-Technology | -- | -- | -- |
| 3.6 | Reputation & Social Proof | R6-Reputation | -- | -- | -- |
| 3.7 | Audience & Personas | R7-Audience | -- | -- | -- |
| 3.8 | UX/UI Patterns | R8-UX | -- | -- | -- |
| 3.9 | Content Landscape & Strategy | R9-Content | -- | -- | -- |
```

Phase 1 (INIT) is marked `complete` immediately — producing project.json, D1-Init.txt, and baseline-log.txt IS the INIT phase output.

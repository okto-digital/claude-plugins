# Project Init — Templates

## JSON Schema

```json
{
  "project": {
    "name": "string",
    "client": "string",
    "build_type": "new | redesign",
    "site_type": "string",
    "goal": "string",
    "languages": {"primary": "string", "other": []},
    "location": {"primary": "string", "other": []}
  },
  "research_config": {
    "research_depth": "basic | deep",
    "output_format": "verbose | concise",
    "serp_max_keywords": 50,
    "search_landscape_max_keywords": 100,
    "competitors_max": 5
  },
  "notes": [
    "string",
    "string"
  ]
}
```

### Example (Krocko project)

```json
{"project":{"name":"Krocko Caviar Web","client":"Krocko","build_type":"new","site_type":"ecommerce","goal":"Build B2B/B2C ecommerce for caviar brand targeting HoReCa and events","languages":{"primary":"sk","other":[]},"location":{"primary":"SK","other":["CZ"]}},"research_config":{"research_depth":"basic","output_format":"concise","serp_max_keywords":50,"search_landscape_max_keywords":100,"competitors_max":5},"notes":["Business model is B2B and B2C targeting HoReCa, corporate events and catering","Three segments: HoReCa B2B, end customers B2C, corporate events and catering","Products: caviar, wine, champagne — premium and exclusive positioning","Brand still in development, no name or domain yet, designer is Matej Španík","Requires payment gateway, ERP integration and accounting automation","Investigate FiscalPro integration — fiscalpro.sk","Competitor: royalcaviar.sk","Inspiration site: n25caviar.sk","SEO potential to assess for: kaviar, šampanské, jeseter, losos","Primary market SK for 1-2 years, secondary market CZ","Contract signed for SK and CZ","Paid advertising planned","Partner restaurants to be identified"]}
```

---

## Markdown Template

Generate `D1-Init.md` from D1-Init.json using this template:

```markdown
# Project Brief — [project.name]

## Project
- **Client:** [project.client]
- **Build type:** [project.build_type]
- **Site type:** [project.site_type]
- **Goal:** [project.goal]
- **Primary language:** [project.languages.primary]
- **Additional languages:** [project.languages.other] or "none"
- **Primary market:** [project.location.primary]
- **Additional markets:** [project.location.other] or "none"

## Research Config
- **Research depth:** [research_config.research_depth]
- **Output format:** [research_config.output_format]
- **SERP max keywords:** [research_config.serp_max_keywords]
- **Search landscape max keywords:** [research_config.search_landscape_max_keywords]
- **Max competitors:** [research_config.competitors_max]

## Notes
- [notes[0]]
- [notes[1]]
- ...
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
| 1 | INIT | complete | D1-Init.json | {YYYY-MM-DD} |
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

Phase 1 (INIT) is marked `complete` immediately — producing D1-Init.json IS the INIT phase output.

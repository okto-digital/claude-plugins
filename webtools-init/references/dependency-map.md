# Dependency Map

Full dependency graph for the webtools document pipeline. Used by the downstream-impact notification in the completion sequence and by `/webtools-init-health` for freshness checks.

---

## Forward Dependencies (what each document affects)

| Document | Affects |
|----------|---------|
| D1: Project Brief | D2, D3, D4, D5, D6, D7, D8, D9 |
| D2: Brand Voice Profile | D7, D8, D9, D10 |
| D3: SEO Keyword Map | D4, D7, D8, D10 |
| D4: Site Architecture | D7, D8, D9, D10 |
| D5: Competitor Analysis | D4, D7, D10 |
| D6: Content Inventory | D4, D7, D8 |
| D7: Page Blueprint | D8, D9 |
| D8: Page Content | D10 |
| D9: Microcopy | (none) |
| D10: Content Audit Report | (none) |
| D11: Client Questionnaire | D1 |
| D12: SEO Content Targets | D8, D10 |

## Reverse Dependencies (what each document needs)

| Document | Required Inputs | Optional Inputs | Created By |
|----------|----------------|-----------------|------------|
| D1: Project Brief | (none -- raw client input) | D11 | webtools-intake |
| D2: Brand Voice Profile | D1 | existing website URL, tone examples | webtools-brand |
| D3: SEO Keyword Map | D1 | competitor URLs, analytics data | webtools-seo |
| D4: Site Architecture | D1 | D3, D5, D6 | webtools-architecture |
| D5: Competitor Analysis | D1, competitor URLs | analysis focus | webtools-competitors |
| D6: Content Inventory | D1, existing website URL | sitemap | webtools-inventory |
| D7: Page Blueprint | D1, D4 | D2, D3, D5, D6 | webtools-blueprint |
| D8: Page Content | D7, D2 | D3, D6, D12, raw content | webtools-writer |
| D9: Microcopy | D1, D2, D4 | D7 (all) | webtools-writer |
| D10: Content Audit Report | D8 (at least one), D3 | D2, D5, D12 | webtools-audit |
| D11: Client Questionnaire | project type (via args) | industry | webtools-intake |
| D12: SEO Content Targets | (external) | -- | external tool |

## Pipeline Flow

```
Client Input
    |
[/questionnaire] --> D11: Client Questionnaire
    |
[brief-generator] --> D1: Project Brief
    |                       |
[brand-voice-creator]  [seo-keyword-research]
    |                       |
   D2                      D3
    |                       |
    |    [competitor-analyzer] --> D5
    |    [content-inventory]   --> D6
    |              |                  |
    |         [architecture-planner] --> D4
    |              |
    +----> [blueprint-generator] --> D7 (per page)
                   |                  (consults Knowledge Base)
                   |--- D12 (external import)
                   |
           [content-generator] --> D8 (per page)
                   |
           [microcopy-generator] --> D9
                   |
           [/webtools-audit] --> D10
                   |
           Handoff to Design/Dev
```

## Phase Mapping

| Phase | Documents Produced | Plugins |
|-------|-------------------|---------|
| Discovery | D11, D1 | webtools-intake |
| Research | D2, D3, D5, D6 | webtools-brand, webtools-seo, webtools-competitors, webtools-inventory |
| Architecture | D4 | webtools-architecture |
| Blueprinting | D7 (per page) | webtools-blueprint |
| Content | D8 (per page), D9 | webtools-writer |
| Audit | D10 | webtools-audit |

## Freshness Rules

A downstream document is considered **stale** when its dependency has been updated after the downstream document was last updated. Specifically:

- Compare the `updated` date in the downstream document's header against the `updated` date of each of its dependencies.
- If any dependency is newer, the downstream document is stale.
- Staleness is informational -- it suggests the document should be regenerated, not that it is invalid.

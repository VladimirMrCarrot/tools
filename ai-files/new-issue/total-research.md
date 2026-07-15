---
artifact: deep-research-template
version: 1.2
created: 2026-06-24
updated: 2026-06-25
usage: reusable — fill {PROJECT_CONTEXT} block before running any prompt
---

# Deep Research Prompt Template — Feature Architecture, Competitive & UX Analysis

## HOW TO USE

1. Fill in the {PROJECT_CONTEXT} block below with your feature specifics
2. Choose which prompt to run: A (Technical), B (Competitive), or C (UX/Patterns)
3. Open Perplexity → Focus: Deep Research → paste the filled prompt → run
4. Save output as MD artifact in artifacts/research/

---

## {PROJECT_CONTEXT} — fill before running

PROJECT_NAME: [feature name, e.g. "Analytics Dashboards for FOP"]
APP_TYPE: [e.g. "Mobile banking app iOS + Android"]
TARGET_USERS: [e.g. "FOP — Ukrainian individual entrepreneurs / sole traders"]
FEATURE_GOAL: [e.g. "income and expense tracking dashboard"]
EXISTING_SOLUTION: [e.g. "retail version exists for physical persons in same app"]
DESIGN_GOAL: [e.g. "produce 2-3 solution variants for architect grooming"]
TECH_CONSTRAINTS: [e.g. "see tech-stack.md" or list key constraints inline]

---

## PROMPT A — Technical Architectural Approaches

You are a senior solution architect and fintech analyst.
Conduct a deep technical research on architectural approaches for implementing
[FEATURE_GOAL] in [APP_TYPE].

### Language instruction

Respond entirely in Ukrainian.
Keep in English without translation: technical terms (API, endpoint, CDC, ETL,
CQRS, Kafka, microservice, cache, etc.), proper names of tools, frameworks,
companies, and all code or diagram syntax.

### Project context

PROJECT_NAME: {PROJECT_NAME}
TARGET_USERS: {TARGET_USERS}
EXISTING_SOLUTION: {EXISTING_SOLUTION}
DESIGN_GOAL: {DESIGN_GOAL}
TECH_CONSTRAINTS: {TECH_CONSTRAINTS}

### Research scope

Cover these dimensions for each architectural approach you find:

1. Data aggregation layer — event streaming, batch ETL, CQRS+Event Sourcing, CDC, etc.
2. Rendering approach — client-side vs server-side aggregation, pre-computed vs on-demand
3. Refresh strategy — real-time / near-real-time / periodic — trade-offs
4. Data categorization model — rule-based, ML-based, hybrid
5. Multi-entity / B2B context — approaches specific to SME / sole-trader banking

### Output format requirements

Produce a structured Markdown document:

1. SUMMARY COMPARISON TABLE at the very top:
   | Підхід | Модель оновлення | Складність | Time-to-market | Best fit |

2. For each approach — H2 section containing:
   - Опис: 2-3 речення
   - Architecture data flow diagram in Mermaid (flowchart or sequence)
   - Використовується у: known banks or fintechs with source URLs
   - Переваги: bullet list
   - Недоліки: bullet list
   - Потенціал для reuse: integration with existing retail solution
   - Best fit for: team size, scale, complexity context
   - Джерело: verified URL

3. TRADE-OFF MATRIX table at the end:
   | Підхід | Складність | Time-to-market | Real-time | Scalability | ML-ready | Вартість інфраструктури |
   Rate each: Low / Medium / High

4. RECOMMENDATION section:
   Given a mid-size fintech team and an existing retail analytics solution,
   which 2-3 approaches are most viable as distinct grooming variants and why?

### Formatting rules

- H2 for each approach, H3 for subsections
- Every architecture must include a Mermaid diagram (```mermaid block)
- Tables for comparisons — no prose tables
- Scannable: bullets, headers, diagrams — no walls of text

### Source constraints

- Official engineering blogs: Monzo, Revolut, N26, Starling, PrivatBank, Monobank, Wise, Stripe
- Cloud fintech guides: AWS, GCP, Azure
- ThoughtWorks Tech Radar, Martin Fowler, InfoQ
- Mark unverified: [UNVERIFIED] | Mark older than 2 years: [POTENTIALLY OUTDATED]
- No marketing content

Save result as: {PROJECT_ROOT}/artifacts/research/market-approaches.md

---

## PROMPT B — Competitive System-Level Analysis

You are a fintech competitive intelligence analyst and solution architect.
Conduct a deep research on how leading mobile banking applications serving
small business / sole traders have implemented [FEATURE_GOAL] at the system
architecture level — not UI level.

### Language instruction

Respond entirely in Ukrainian.
Keep in English without translation: technical terms (API, endpoint, CDC, ETL,
microservice, etc.), proper names of tools, frameworks, companies, and all
code or diagram syntax.

### Project context

PROJECT_NAME: {PROJECT_NAME}
TARGET_USERS: {TARGET_USERS}
FEATURE_GOAL: {FEATURE_GOAL}
DESIGN_GOAL: {DESIGN_GOAL}

### Competitors to analyze (priority order)

1. Monobank — FOP / business account (Ukraine)
2. PrivatBank / Privat24 Business (Ukraine)
3. Revolut Business (EU)
4. N26 Business (EU)
5. Starling Bank Business (UK)
6. Monzo Business (UK)

### Output format requirements

1. OVERVIEW TABLE at the very top:
   | Компанія | Аналітичні функції | Модель оновлення | Категоризація | API | Тех. підхід відомий | Якість джерел |

2. Detailed H2 section per competitor:
   - Аналітичні функції
   - Відомий тех. підхід
   - Джерела даних
   - Модель оновлення
   - Тип категоризації
   - API exposure
   - Джерело: verified URL with date
   - Що невідомо: explicit gaps

3. INFERRED ARCHITECTURE DIAGRAM (Mermaid):
   Generic data flow: transaction source → aggregation → storage → API → mobile client

4. SYNTHESIS section:
   a) Таблиця спільних патернів: | Патерн | Використовується у | Частота |
   b) Мінімальний viable tech stack
   c) Open-source reference implementations (with GitHub links)
   d) Специфіка українського ринку — регуляторика, інфраструктура, поведінка користувачів
   e) Рекомендація: найкраще співвідношення feature parity vs зусилля

### Formatting rules

- H2 per competitor, H3 for subsections
- Minimum 2 Mermaid diagrams
- Scannable: no paragraph walls

### Source constraints

- Verified public sources: engineering blogs, conference talks, tech press with named engineers
- No speculation — unknown is better than guessed
- Mark older than 2 years: [POTENTIALLY OUTDATED]

Save result as: {PROJECT_ROOT}/artifacts/research/competitor-analysis.md

---

## PROMPT C — UX & UI Patterns Research

You are a senior product designer and mobile UX researcher specializing in fintech.
Conduct a deep research on UX and UI patterns used for presenting financial analytics
dashboards in mobile banking apps — specifically for small business / sole trader accounts.

### Language instruction

Respond entirely in Ukrainian.
Keep in English without translation: UX/UI terms (bottom sheet, drill-down, onboarding,
empty state, skeleton loader, etc.), proper names of apps, tools, design systems,
pattern libraries, and all diagram syntax.

### Project context

PROJECT_NAME: {PROJECT_NAME}
APP_TYPE: {APP_TYPE}
TARGET_USERS: {TARGET_USERS}
FEATURE_GOAL: {FEATURE_GOAL}
EXISTING_SOLUTION: {EXISTING_SOLUTION}
DESIGN_GOAL: inform UI/UX decisions; understand what patterns work and what
differentiates business-account analytics from retail

### Research scope

1. INFORMATION ARCHITECTURE — entry points, navigation depth, period selection, overview vs detail hierarchy
2. VISUALIZATION PATTERNS — which chart types for which data (donut, bar, line, treemap, waterfall, sparkline, heatmap)
3. BUSINESS vs RETAIL DIFFERENTIATION — additional metrics, multi-account aggregation, export, category customization
4. MICRO-INTERACTIONS & PROGRESSIVE DISCLOSURE — drill-down, loading states, empty states, error states
5. MOBILE-SPECIFIC PATTERNS — gestures, bottom sheets, home screen widgets

### Output format requirements

1. PATTERN OVERVIEW TABLE at the top:
   | Категорія патерну | Поширені підходи | Використовується у | Рекомендовано для {TARGET_USERS} |

2. For each dimension — H2 section:
   - Домінуючі патерни
   - Mermaid diagram (navigation flow or component structure)
   - Таблиця прикладів: | Застосунок | Реалізація | Нотатки |
   - Що працює добре: bullets
   - Що не працює: bullets
   - Специфіка для бізнес-акаунту: bullets

3. COMPETITOR SCREENSHOT REFERENCES section:
   List publicly available UI references (app store screenshots, design case studies)
   with URLs and brief description

4. DESIGN RECOMMENDATIONS section:
   a) Топ-5 патернів для впровадження (з обґрунтуванням)
   b) Топ-3 патерни яких слід уникати (з обґрунтуванням)
   c) Один недооцінений патерн з високою цінністю для бізнес-контексту
   d) Рекомендована IA: Mermaid flowchart навігаційної структури

5. RETAIL vs BUSINESS DELTA TABLE:
   | Функція / Патерн | Retail версія | Рекомендовано для бізнесу | Delta effort |

### Formatting rules

- H2 per dimension, H3 for subsections
- Minimum 3 Mermaid diagrams: navigation flow, component layout, retail-vs-business delta
- All comparisons in Markdown tables
- Scannable: no paragraph walls

### Source constraints

- App store screenshots, official product pages: acceptable as UI evidence
- Design case studies: Dribbble, Behance, UX Collective, Medium design publications
- Pattern libraries: mobbin.com, pttrns.com, screenlane.com
- Official product blogs: Monzo, Revolut, N26, Starling, Monobank, PrivatBank
- Mark older than 2 years: [POTENTIALLY OUTDATED]
- Focus on observable UI patterns only — no speculation about implementation

Save result as: {PROJECT_ROOT}/artifacts/research/ux-patterns.md

---

## OUTPUT ARTIFACT NAMING CONVENTION

| Промт            | Зберегти результат як                                    |
| ---------------- | -------------------------------------------------------- |
| A — Технічний    | {PROJECT_ROOT}/artifacts/research/market-approaches.md   |
| B — Конкурентний | {PROJECT_ROOT}/artifacts/research/competitor-analysis.md |
| C — UX/Патерни   | {PROJECT_ROOT}/artifacts/research/ux-patterns.md         |

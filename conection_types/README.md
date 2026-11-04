# conection_types

Online: https://tools.mrcarrot13666.me/conection_types/ (folder name kept as is for a stable URL)

Interactive UML relationship map on two examples (forest / bank account), UA/EN, dark/light. One self-contained `index.html`:

- diagram: inheritance, realization, composition, aggregation, association, dependency, with multiplicity and arrowheads at the correct ends; every class has an operations line
- sticky section bar with the current section highlighted; on phones it collapses to the current chip, tap it to unfold
- phone cards: photo, two mini class boxes with operations, example, meaning, and the full cheat sheet entry on demand
- cheat sheet (desktop) with notation, test question, forest and software examples, PlantUML line
- "how to choose": four decision questions and the class-vs-object note, on every width
- multiplicity and navigability reference; tables turn into stacked rows on narrow screens, no horizontal scroll
- the same diagram as PlantUML and Mermaid: language switch, code / preview switch, copy button; PlantUML preview is a locally rendered SVG (`puml-forest.svg`, `puml-bank.svg`, kept in sync by `check-puml-preview.py` and `puml-preview.lock`), Mermaid preview renders in the browser (mermaid 10.9.1 from cdnjs with SRI, loaded only on demand)
- UML to database mapping (FK placement, ON DELETE behaviour, join table, inheritance strategies) with sample DDL in the author's SQL style
- self-check: a pool of 18 situations (three per relationship), eight per round in random order with shuffled answers, best round kept in localStorage, weak spots link to the reference

Images are WebP, 900 px wide (`cwebp -q 82 -resize 900 0`); the bank and the plant / photosynthesis photos come from Pexels (Pexels licence, no attribution required).

Regression checklist for future changes: `REGRESSION.md` (quick console check plus a manual pass at 1400 / 905 / 890 / 640 / 390 px).

Syntax highlighting (SQL, PlantUML, Mermaid) is a small built-in tokenizer, no library. The page sets a Content-Security-Policy meta tag: scripts only from itself and cdnjs, styles and fonts only from Google Fonts, no outgoing requests.

Interactions: a pinned desktop hint stays in place while the page scrolls; a scroll-to-top button on every width; tap a diagram preview to open it full screen with pinch, drag, double-tap and wheel zoom; on touch screens hold a code block or a notation cell for half a second and release to copy it. The best self-check round is kept in localStorage (`uml-tree-quiz-best`), together with theme, language and example.

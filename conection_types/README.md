# conection_types

Online: https://tools.mrcarrot13666.me/conection_types/ (folder name kept as is for a stable URL)
Previous version for comparison: https://tools.mrcarrot13666.me/conection_types/v1/ (snapshot of the first diagram, not maintained)

Interactive UML relationship map on two examples (forest / bank account), UA/EN, dark/light. One self-contained `index.html`:

- diagram: inheritance, realization, composition, aggregation, association, dependency, with multiplicity and arrowheads at the correct ends; every class has an operations line
- sticky section bar with the current section highlighted; on phones it collapses to the current chip, tap it to unfold
- phone cards: photo, two mini class boxes with operations, example, meaning, and the full cheat sheet entry on demand
- cheat sheet (desktop) with notation, test question, forest and software examples, PlantUML line; four decision questions folded under it
- multiplicity and navigability reference; tables turn into stacked rows on narrow screens, no horizontal scroll
- full PlantUML source for the current example with copy button
- UML to database mapping (FK placement, ON DELETE behaviour, join table, inheritance strategies) with sample DDL
- self-check: a pool of 18 situations (three per relationship), eight per round in random order with shuffled answers, best round kept in localStorage, weak spots link to the reference

Images are WebP, 900 px wide (`cwebp -q 82 -resize 900 0`); the bank and the plant / photosynthesis photos come from Pexels (Pexels licence, no attribution required).

Regression checklist for future changes: `REGRESSION.md` (quick console check plus a manual pass at 1400 / 905 / 890 / 640 / 390 px).

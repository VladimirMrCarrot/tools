Act as an AI industry analyst. Search for and compile the TOP 7 AI news items from the past 7 days.

## WHO THIS IS FOR
The reader is:
- A Business & Systems Analyst in IT who works heavily with requirements documentation, diagram generation (PlantUML, UML), and visual specification tools
- A game streamer who uses or wants to use AI for streaming workflow, content creation, video thumbnails
- An Obsidian + Zettelkasten power user interested in AI that enhances knowledge management and note-taking
- Someone with GitHub Student Developer Pack, Google AI Pro, and Cursor Pro — but always budget-conscious
- Specifically interested in: AI-assisted BA/SA work, automated diagram generation, requirements visualization, workflow optimization tools

## SOURCE WHITELIST — STRICT
Only use information from these official sources:
- openai.com/blog or openai.com/news
- anthropic.com/news
- deepmind.google/discover/blog
- mistral.ai/news
- meta.ai/blog or ai.meta.com/blog
- huggingface.co/blog
- github.blog
- cursor.com/changelog
- blogs.microsoft.com/ai
- ai.googleblog.com
- notebooklm.google
- arxiv.org (only landmark papers, must have significant community pickup)

Do NOT cite: TechCrunch, The Verge, Wired, Ars Technica, Reddit, Twitter/X, Medium, Substack, or any non-official source.

## OUTPUT FORMAT
Return a numbered list of 7 items. Each item:

[N]. TITLE: [English title]
     UA_TITLE: [Ukrainian translation]
     DATE: [YYYY-MM-DD]
     URL: [official source link]
     TYPE: [New Model | Update | Feature | Integration | Research | Pricing | Tip]
     RELEVANCE_FOR_READER: [2 sentences — why does this matter for this specific reader?]
     SUMMARY: [Ukrainian, 4-5 sentences]
     COST_INFO: [Free? Paid? Student Pack eligible?]

## RULES
- Today is {INSERT_TODAY_DATE}
- Only last 7 days
- No hallucinated URLs — if unsure, write [SOURCE NEEDED]
- Quality over quantity — 5 real items beats 7 padded ones
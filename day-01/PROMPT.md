# Prompt — meeting notes → action table

Copy from the line below through the end.

---

You extract action items from meeting notes. Output ONLY a Markdown table with columns:

| Action | Owner | Due | Notes |

Hard rules:
1. Include only concrete next actions (verbs: ship, send, fix, schedule, review, decide, draft, ping). Skip decisions that need no follow-up and skip pure status updates.
2. Owner must appear in the notes as a name or @handle. If missing or unclear, write `unset` — never invent a person.
3. Due must be an explicit date (prefer YYYY-MM-DD) or a clear relative date already in the notes. If missing, write `unset` — never invent a date.
4. Notes column: one short clarifying phrase, or leave empty.
5. Deduplicate near-identical actions. Prefer the more specific wording.
6. Do not write a summary, intro, or closing — table only.
7. If today's date is provided below, resolve relative phrases ("Friday", "next week") against it; otherwise leave relative-only items as `unset` unless the notes already contain a calendar date.

Today's date (optional): {{TODAY}}

Meeting notes:
{{NOTES}}

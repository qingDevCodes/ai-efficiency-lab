# Day 01 — Messy meeting notes → owner + due-date action table

## Problem

Meeting notes are a wall of text. Action items get buried, owners are fuzzy, and due dates disappear.

## What you get

One pasteable prompt that turns raw notes into a Markdown table:

`Action | Owner | Due | Notes`

Rules baked in:

- Actions only (no fluff summary)
- Owner must be a real name/`@handle` from the notes — otherwise `unset`
- Due date must be stated or clearly implied — otherwise `unset`
- Never invent people or dates

## How to run (under 2 minutes)

1. Copy everything in [`PROMPT.md`](./PROMPT.md).
2. Paste your notes (or use [`samples/input.md`](./samples/input.md)).
3. Run in ChatGPT / Claude / Cursor.
4. Compare to [`samples/output.md`](./samples/output.md).

## When to use

- Product syncs, standups, client calls
- You need a shareable checklist in Slack/Linear within minutes

## Limitations

- Ambiguous owners stay `unset` on purpose — fix them in the table, don't let the model guess
- Dates like "next week" need a reference date; pass today's date in the prompt if you care

## Pass criteria

See [`EVIDENCE.md`](./EVIDENCE.md).

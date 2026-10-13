# Evidence — Day 01

## Pass

Given [`samples/input.md`](./samples/input.md), a model following [`PROMPT.md`](./PROMPT.md) should produce a table that:

1. Has no prose outside the table
2. Marks owner `unset` for "kill the beta badge" (no owner in notes)
3. Keeps Oct 20 on the one-pager row
4. Keeps the slipped Oct 10 analytics item for @jordan
5. Does **not** invent a due date for "before Friday" or "this week" unless `{{TODAY}}` was filled in

Compare against [`samples/output.md`](./samples/output.md). Small wording differences are fine; invented owners/dates are a fail.

## How this was verified

Text fixture only (no paid API in-repo). Paste prompt + input into any chat model and diff the table.

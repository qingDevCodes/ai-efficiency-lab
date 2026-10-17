# Evidence — Day 04

## Pass

Given [`samples/input.md`](./samples/input.md), notes produced with [`PROMPT.md`](./PROMPT.md) should:

1. Include every customer-facing PR: #412, #415, #418, #421, #424, #427, #429
2. Leave out internal PRs: #416, #419, #422, #425, #435, #436
3. Leave out the reverted CSV export (#430) and its revert (#433)
4. Put the vague `fix: timezone` (#434) under NEEDS A HUMAN with a question, not in the notes
5. Open with Breaking changes, listing the `client_id` → `customer_id` rename (#418) and what to do
6. Fold the bulk-send fix (#421) into the new bulk-send bullet (#412)
7. End every bullet with its PR number(s)
8. Contain no number that isn't in the log (no made-up percentages or dates)

`check.py` tests 1–5, 7 and 8 automatically. Point 6 you check by eye.

## What was run

All times Asia/Shanghai (UTC+8).

| When | What |
| --- | --- |
| 2026-10-17 21:04 | Wrote `samples/input.md` (16-line fake commit log) and `PROMPT.md` |
| 2026-10-17 21:04 | Wrote release notes in `samples/output.md` following `PROMPT.md` |
| 2026-10-17 21:04 | `python3 check.py samples/input.md samples/output.md -q` → **20/20 checks passed, ALL PASS** |
| 2026-10-17 21:04 | Negative test: added the reverted CSV export back and "about 40% faster" → **18/20, 2 FAIL**, exit code 1 |
| 2026-10-17 21:04 | Rendered [`day04-screenshot.html`](./day04-screenshot.html) with headless Chrome → `day04-before-after.png` |

Screenshot of the run: [`day04-before-after.png`](./day04-before-after.png)

## How to reproduce

```bash
python3 check.py samples/input.md samples/output.md      # every check
python3 check.py samples/input.md samples/output.md -q   # failures + summary only
```

No API calls and nothing to install beyond Python 3. Paste prompt + log into any chat model, save the answer, run the checker on it.

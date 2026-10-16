# Evidence — Day 02

## Pass

Given [`samples/input.md`](./samples/input.md), a model following [`PROMPT.md`](./PROMPT.md) should produce three emails that:

1. Each contain: order A39281, Harbor Lights Co, 200 cases of LED strips, promised Oct 12, shipped Oct 15, 3% credit on this order
2. Contain **no** delivery ETA, tracking promise, "won't happen again", or future-order offer
3. Do **not** mention the carrier (that was an `internal:` note)
4. A (formal) has no contractions or exclamation marks; C (firm) has no "just" / "hopefully"
5. Each body stays under 120 words

Compare against [`samples/output.md`](./samples/output.md). Different wording is fine; a changed fact or an added promise is a fail.

## What was run

All times Asia/Shanghai (UTC+8).

| When | What |
| --- | --- |
| 2026-10-15 21:08 | Wrote `samples/input.md` (raw delay note with `internal:` lines) and `PROMPT.md` |
| 2026-10-15 21:08 | Generated the three emails in `samples/output.md` with an AI assistant following `PROMPT.md` |
| 2026-10-15 21:09 | First checker run → ALL PASS, but on re-read email B ended with "I'll get back to you" (a soft promise the regex didn't catch). Rewrote that line to "If anything's unclear, just reply to this email." |
| 2026-10-15 21:11 | `python3 check.py samples/output.md -q` → **ALL PASS** (6/6 facts in each email, 0 new promises/leaks, tone rules OK; body word counts A 72 / B 80 / C 75) |
| 2026-10-15 21:11 | Negative test: injected "It should arrive by Oct 18 and this will not happen again" into email C → `FAIL [C] … new promises/leaks 2`, exit code 1 |
| 2026-10-15 21:11 | Rendered [`day02-screenshot.html`](./day02-screenshot.html) with headless Chrome → `day02-before-after.png` |

Screenshot of the run: [`day02-before-after.png`](./day02-before-after.png)

## How to reproduce

```bash
python3 check.py samples/output.md      # per-check detail
python3 check.py samples/output.md -q   # one line per email
```

Text fixtures only, no paid API in-repo. Paste prompt + input into any chat model, save the answer, run the checker on it.

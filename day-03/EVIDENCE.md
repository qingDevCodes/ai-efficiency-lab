# Evidence — Day 03

## Pass

Given [`samples/input.md`](./samples/input.md), a model following [`PROMPT.md`](./PROMPT.md) should produce a ticket that:

1. Has all eight sections: Summary, Severity, Expected vs Actual, Repro steps, Environment, Impact, MISSING, Suggested next owner action
2. Preserves order ids `O-18421` / `O-18429`, the `"2pm deploy"`, Safari, iPhone, and finance asking
3. Uses `UNSET` for gaps (expected side, versions, exact customer count, etc.)
4. Does **not** invent Safari/iOS version numbers, user counts, or error codes
5. Severity is one of P0–P3 with a reason grounded in stated facts
6. MISSING is a checklist with concrete questions (≥3)

Compare against [`samples/output.md`](./samples/output.md). Different wording is fine; invented facts or missing UNSET for clear gaps is a fail.

## What was run

All times Asia/Shanghai (UTC+8).

| When | What |
| --- | --- |
| 2026-10-16 21:10 | Wrote `samples/input.md` (Maya CS Slack dump) and `PROMPT.md` |
| 2026-10-16 21:10 | Wrote structured ticket in `samples/output.md` following `PROMPT.md` |
| 2026-10-16 21:10 | `python3 check.py samples/output.md -q` → **ALL PASS** (8/8 sections, 7/7 facts, UNSET×6, MISSING items 6) |
| 2026-10-16 21:10 | Negative test: injected `Safari 17.2` + `47 customers` → `2 FAIL`, exit code 1 |
| 2026-10-16 21:11 | Rendered [`day03-screenshot.html`](./day03-screenshot.html) with headless Chrome → `day03-before-after.png` |

Screenshot of the run: [`day03-before-after.png`](./day03-before-after.png)

## How to reproduce

```bash
python3 check.py samples/output.md      # per-check detail
python3 check.py samples/output.md -q   # one-line summary
```

Text fixtures only, no paid API in-repo. Paste prompt + input into any chat model, save the answer, run the checker on it.

# Prompt — vague bug report → engineer-ready triage ticket

Copy from the line below through the end. Replace `{{REPORT}}` with the raw Slack/email dump.

---

Turn the bug report below into one structured triage ticket an engineer can open without guessing.

Output exactly these sections, in this order, as markdown:

1. **Summary** — one line
2. **Severity** — P0 / P1 / P2 / P3, plus one short reason grounded only in stated facts
3. **Expected vs Actual** — two bullets; write `UNSET` for either side if the report never said it
4. **Repro steps** — numbered list of only what was stated; never invent steps; if none given, one line: `UNSET`
5. **Environment** — browser / OS / version / account (or whatever was named); each missing field = `UNSET`
6. **Impact** — who is blocked and how many; `UNSET` if not stated
7. **MISSING** — concrete questions still needed before an engineer can start (checklist)
8. **Suggested next owner action** — one line

Hard rules:

- Do not invent repro steps, versions, user counts, error codes, stack traces, or root causes.
- Quote short key phrases from the report in backticks when they matter (e.g. `"tap Pay and nothing happens"`).
- Preserve identifiers exactly (order ids, ticket ids, deploy times) as written.
- Severity must cite only stated facts (e.g. "started after today's deploy", "finance is asking") — never invent blast radius.
- Stop after the ticket. No essay, no "hope this helps", no root-cause speculation.

Bug report:
{{REPORT}}

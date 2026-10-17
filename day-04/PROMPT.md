# Prompt — raw git log → release notes a customer can read

Copy from the line below through the end. Replace `{{LOG}}` with your `git log --oneline` output (or a list of merged PR titles).

---

Turn the commit log below into release notes for customers, not for engineers.

Output markdown with these sections, in this order. Drop any section that ends up empty, except NEEDS A HUMAN.

1. **Breaking changes** — what changed and exactly what the reader has to do
2. **New**
3. **Improved**
4. **Fixed**
5. **NEEDS A HUMAN** — commits whose customer impact you can't tell from the message alone. One line each: the PR number and the question you'd ask the author.

Rules:

- One bullet per change, in plain words a customer understands. End every bullet with its PR number(s), e.g. `(#412)`.
- Leave out chore, ci, test, docs, refactor, build and dependency bumps unless the message says users will notice something.
- If a commit was reverted in the same log, leave out both the commit and the revert.
- If a fix only repairs something that is new in this same release, fold it into that feature's bullet instead of listing it under Fixed.
- Don't invent numbers, percentages, dates, customer names, or reasons that aren't in the log. Copy limits that are in the log exactly.
- Don't guess at vague messages like `fix: stuff` or `fix: timezone`. Put them in NEEDS A HUMAN.
- Security fixes go under Fixed and say what was wrong, not how to exploit it.
- No intro, no outro, no emoji.

Commit log:
{{LOG}}

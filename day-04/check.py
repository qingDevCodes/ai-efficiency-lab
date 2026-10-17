"""Checker for day-04 release notes.

Usage: python3 check.py samples/input.md samples/output.md [-q]
(-q prints only failures plus the summary line)

Reads the raw commit log, works out which PRs are customer-facing,
internal, reverted, or too vague, then checks the release notes against it.
No API calls; it only reads the two files.
"""
import re
import sys

args = [a for a in sys.argv[1:] if not a.startswith("-")]
quiet = "-q" in sys.argv
log = open(args[0], encoding="utf-8").read()
notes = open(args[1], encoding="utf-8").read()

INTERNAL = {"chore", "ci", "test", "docs", "refactor", "build", "deps", "style"}
VAGUE = re.compile(r"^(fix|chore|feat)(\([^)]*\))?:\s*(stuff|misc|timezone|wip|bug|fixes?)\s*\(#\d+\)$", re.I)

commits = []
for line in log.splitlines():
    m = re.match(r"^[0-9a-f]{7}\s+(.*)$", line.strip())
    if not m:
        continue
    msg = m.group(1)
    prs = re.findall(r"#(\d+)", msg)
    commits.append((msg, prs[-1] if prs else None, prs))

reverted = set()
for msg, pr, prs in commits:
    if msg.startswith("Revert"):
        reverted.update(prs)  # original PR and the revert PR

facing, internal, vague, breaking = set(), set(), set(), set()
for msg, pr, prs in commits:
    if pr is None or pr in reverted:
        continue
    kind = re.match(r"^(\w+)", msg).group(1).lower()
    if VAGUE.match(msg):
        vague.add(pr)
    elif kind in INTERNAL:
        internal.add(pr)
    else:
        facing.add(pr)
    if re.match(r"^\w+(\([^)]*\))?!:", msg) or "BREAKING" in msg:
        breaking.add(pr)

def section(name):
    m = re.search(rf"^##\s*{name}\s*$(.*?)(?=^##\s|\Z)", notes, flags=re.M | re.S | re.I)
    return m.group(1) if m else None

human = section("NEEDS A HUMAN") or ""
main = re.split(r"^##\s*NEEDS A HUMAN", notes, flags=re.M | re.I)[0]
cited_main = set(re.findall(r"#(\d+)", main))
cited_human = set(re.findall(r"#(\d+)", human))

results = []
def check(ok, label):
    results.append((ok, label))

for pr in sorted(facing):
    check(pr in cited_main, f"customer-facing #{pr} is in the notes")
for pr in sorted(internal):
    check(pr not in cited_main, f"internal #{pr} left out")
for pr in sorted(reverted):
    check(pr not in cited_main and pr not in cited_human, f"reverted #{pr} left out")
for pr in sorted(vague):
    check(pr in cited_human and pr not in cited_main, f"vague #{pr} sent to NEEDS A HUMAN")

heads = re.findall(r"^##\s*(.+?)\s*$", notes, flags=re.M)
if breaking:
    br = section("Breaking changes") or ""
    check(heads and heads[0].lower().startswith("breaking"), "Breaking changes is the first section")
    for pr in sorted(breaking):
        check(f"#{pr}" in br, f"breaking #{pr} listed under Breaking changes")

bullets = [l for l in main.splitlines() if l.strip().startswith("- ")]
check(all(re.search(r"\(#\d+(, #\d+)*\)\s*$", b) for b in bullets), "every bullet ends with its PR number(s)")

log_numbers = set(re.findall(r"\d+(?:\.\d+)?", log))
note_numbers = set(re.findall(r"(?<![#\w])\d+(?:\.\d+)?%?", re.sub(r"#\d+", "", notes)))
invented = sorted(n for n in note_numbers if n.rstrip("%") not in log_numbers or n.endswith("%"))
check(not invented, "no numbers that aren't in the log" + (f" (found: {', '.join(invented)})" if invented else ""))

fails = sum(1 for ok, _ in results if not ok)
for ok, label in results:
    if not quiet or not ok:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
print(f"{len(results) - fails}/{len(results)} checks passed" + ("  ALL PASS" if not fails else f"  {fails} FAIL"))
sys.exit(1 if fails else 0)

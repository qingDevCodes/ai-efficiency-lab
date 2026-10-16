"""Tiny structure/fact checker for day-03 sample output.

Usage: python3 check.py samples/output.md [-q]
Checks that required sections exist, order ids are preserved,
UNSET is used for missing env/impact bits, and no invented
Safari/iOS version numbers appear.
"""
import re
import sys

quiet = "-q" in sys.argv
text = open(sys.argv[1], encoding="utf-8").read()

REQUIRED_HEADERS = [
    ("Summary", r"^##\s*Summary\b"),
    ("Severity", r"^##\s*Severity\b"),
    ("Expected vs Actual", r"^##\s*Expected vs Actual\b"),
    ("Repro steps", r"^##\s*Repro steps\b"),
    ("Environment", r"^##\s*Environment\b"),
    ("Impact", r"^##\s*Impact\b"),
    ("MISSING", r"^##\s*MISSING\b"),
    ("Suggested next owner action", r"^##\s*Suggested next owner action\b"),
]

REQUIRED_FACTS = {
    "order O-18421": r"O-18421",
    "order O-18429": r"O-18429",
    "2pm deploy": r"2pm deploy",
    "tap Pay quote": r"tap Pay and nothing happens",
    "Safari mentioned": r"Safari",
    "iPhone mentioned": r"iPhone",
    "finance asking": r"finance",
}

MUST_UNSET = {
    "Expected UNSET or explicit gap": r"Expected:.*UNSET|UNSET \(report never stated",
    "version UNSET": r"[Vv]ersion:\s*UNSET|App / site version:\s*UNSET",
    "count UNSET": r"count UNSET|exact count UNSET|How many.*\?",
}

BANNED_INVENTIONS = {
    "invented Safari version": r"Safari\s+\d",
    "invented iOS version": r"iOS\s+\d",
    "invented user count": r"\b\d+\s+(customers|users|people)\b",
    "invented error code": r"\b(HTTP\s*[45]\d\d|E_[A-Z0-9]+|error code\s+\d+)\b",
}

fail = 0
lines = []

for name, pat in REQUIRED_HEADERS:
    ok = re.search(pat, text, flags=re.M) is not None
    fail += not ok
    lines.append(f"  {'PASS' if ok else 'FAIL'}  section: {name}")

for name, pat in REQUIRED_FACTS.items():
    ok = re.search(pat, text) is not None
    fail += not ok
    lines.append(f"  {'PASS' if ok else 'FAIL'}  fact: {name}")

# Severity must be P0–P3
sev = re.search(r"\*\*?P([0-3])\*\*?", text)
ok_sev = sev is not None
fail += not ok_sev
lines.append(f"  {'PASS' if ok_sev else 'FAIL'}  severity P0–P3 present")

# MISSING must have checklist items
missing_items = len(re.findall(r"^\s*[-*]\s*\[[ xX]?\]", text, flags=re.M))
ok_miss = missing_items >= 3
fail += not ok_miss
lines.append(f"  {'PASS' if ok_miss else 'FAIL'}  MISSING checklist (≥3 items, found {missing_items})")

unset_count = len(re.findall(r"\bUNSET\b", text))
ok_unset = unset_count >= 3
fail += not ok_unset
lines.append(f"  {'PASS' if ok_unset else 'FAIL'}  UNSET used (≥3, found {unset_count})")

for name, pat in MUST_UNSET.items():
    ok = re.search(pat, text) is not None
    fail += not ok
    lines.append(f"  {'PASS' if ok else 'FAIL'}  gap marked: {name}")

for name, pat in BANNED_INVENTIONS.items():
    # Allow the MISSING section to *ask* about versions/counts; ban only invented specifics like "Safari 17"
    # Scope ban to non-MISSING sections roughly: check whole text for version-number patterns
    hit = re.search(pat, text, flags=re.I)
    if hit:
        fail += 1
        lines.append(f"  FAIL  no {name} (hit: {hit.group(0)!r})")
    else:
        lines.append(f"  PASS  no {name}")

status = "ALL PASS — structured ticket, facts kept, gaps UNSET, nothing invented" if fail == 0 else f"{fail} FAIL — do not hand to eng as-is"
if quiet:
    print(("PASS" if fail == 0 else "FAIL") + f"  sections {sum(1 for n,p in REQUIRED_HEADERS if re.search(p,text,re.M))}/{len(REQUIRED_HEADERS)} | facts {sum(1 for n,p in REQUIRED_FACTS.items() if re.search(p,text))}/{len(REQUIRED_FACTS)} | UNSET×{unset_count} | MISSING items {missing_items}")
    print(status)
else:
    print("\n".join(lines))
    print()
    print(status)
sys.exit(1 if fail else 0)

"""Tiny fact/promise checker for day-02 sample output.

Usage: python3 check.py samples/output.md [-q]
Checks each email (A/B/C) for the required facts and for phrases that
would be a new promise or a leaked internal note.
"""
import re
import sys

FACTS = {
    "order A39281": r"A39281",
    "Harbor Lights": r"Harbor Lights",
    "200 cases LED strips": r"200 cases of LED strips",
    "promised Oct 12": r"October 12|Oct 12",
    "shipped Oct 15": r"October 15|Oct 15",
    "3% credit": r"3% credit",
}
BANNED = {
    "delivery ETA": r"\b(ETA|arrive|arriving|delivered by|expect delivery)\b",
    "tracking promise": r"\btracking\b",
    "never again": r"won't happen again|will not happen again|never happen again",
    "future-order promise": r"future orders?|next order",
    "carrier blame (internal)": r"\bcarrier\b",
}
TONE = {
    "A": [("contraction", r"\b\w+'(s|re|ll|t|ve|m|d)\b"), ("exclamation", r"!")],
    "C": [("softener", r"\b(just|hopefully)\b")],
}

quiet = "-q" in sys.argv
text = open(sys.argv[1], encoding="utf-8").read()
parts = re.split(r"^## ([ABC])\)", text, flags=re.M)
emails = {parts[i]: parts[i + 1].split("\n---")[0] for i in range(1, len(parts), 2)}

fail = 0
for key, body in emails.items():
    words = len(re.findall(r"\b\w+\b", body.split("**Subject:**", 1)[1].split("\n", 1)[1]))
    lines, f_ok, b_hits, t_hits = [], 0, [], []
    for name, pat in FACTS.items():
        ok = re.search(pat, body) is not None
        f_ok += ok
        lines.append(f"  {'PASS' if ok else 'FAIL'}  fact: {name}")
    for name, pat in BANNED.items():
        hit = re.search(pat, body, flags=re.I)
        if hit:
            b_hits.append(name)
        lines.append(f"  {'FAIL' if hit else 'PASS'}  no {name}")
    for name, pat in TONE.get(key, []):
        hit = re.search(pat, body, flags=re.I)
        if hit:
            t_hits.append(name)
        lines.append(f"  {'FAIL' if hit else 'PASS'}  tone: no {name}")
    fail += (len(FACTS) - f_ok) + len(b_hits) + len(t_hits)
    if quiet:
        bad = b_hits + t_hits
        status = "PASS" if f_ok == len(FACTS) and not bad else "FAIL"
        print(f"{status}  [{key}] {words:>3} words | facts {f_ok}/{len(FACTS)} | new promises/leaks {len(b_hits)} | tone {'ok' if not t_hits else ','.join(t_hits)}")
    else:
        print(f"[{key}] {words} words")
        print("\n".join(lines))
print(f"{"" if quiet else chr(10)}{'ALL PASS — 3 emails, same facts, no new promises' if fail == 0 else f'{fail} FAIL — do not send as-is'}")
sys.exit(1 if fail else 0)

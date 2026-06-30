#!/usr/bin/env python3
"""
status.py — print a venture's 24-step progress dashboard and key metrics.

Parses the venture's dashboard.md for step checkboxes (`- [x] 7. ...` = done) and the
"Key metrics" block, and counts logged interviews and competitor profiles.

Usage:
    python3 status.py ventures/<slug>
"""
import os
import re
import sys

THEMES = [
    ("1  Who is your customer?", range(1, 7)),
    ("2  What can you do for the customer?", range(7, 12)),
    ("3  How do they acquire it?", range(12, 14)),
    ("4  How do you make money?", range(14, 20)),
    ("5  How do you build it?", range(20, 24)),
    ("6  How do you scale?", range(24, 25)),
]
STEP_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s*(\d+)\.", re.MULTILINE)


def bar(done, total, width=20):
    filled = int(round(width * done / total)) if total else 0
    return "[" + "#" * filled + "-" * (width - filled) + f"] {done}/{total}"


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: status.py <venture-dir>")
    venture = sys.argv[1].rstrip("/")
    if not os.path.isdir(venture):
        sys.exit(f"error: {venture} is not a directory")

    name = os.path.basename(venture)
    dashboard = os.path.join(venture, "dashboard.md")
    done_steps = set()
    metrics_block = ""
    if os.path.isfile(dashboard):
        with open(dashboard, encoding="utf-8") as fh:
            text = fh.read()
        for mark, num in STEP_RE.findall(text):
            if mark.lower() == "x":
                done_steps.add(int(num))
        m = re.search(r"##+\s*Key metrics(.*?)(?:\n##\s|\Z)", text, re.DOTALL | re.IGNORECASE)
        if m:
            metrics_block = m.group(1).strip()
    else:
        print(f"(no dashboard.md found in {venture} — showing zeros)\n")

    print(f"\nVenture: {name}")
    print("=" * 52)
    total_done = 0
    for label, steps in THEMES:
        steps = list(steps)
        d = sum(1 for s in steps if s in done_steps)
        total_done += d
        print(f"Theme {label:<38}{bar(d, len(steps))}")
    print("-" * 52)
    print(f"{'OVERALL':<44}{bar(total_done, 24)}\n")

    # Live evidence counts.
    def count_md(sub):
        d = os.path.join(venture, sub)
        if not os.path.isdir(d):
            return 0
        skip = {"readme.md", "matrix.md"}
        return sum(1 for f in os.listdir(d) if f.lower().endswith(".md") and f.lower() not in skip)

    print(f"Interviews logged ....... {count_md('interviews')}")
    print(f"Competitor profiles ..... {count_md('competitors')}")
    print(f"Research notes .......... {count_md('research')}\n")

    if metrics_block:
        print("Key metrics")
        print(metrics_block + "\n")


if __name__ == "__main__":
    main()

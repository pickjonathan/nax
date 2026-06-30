#!/usr/bin/env python3
"""
status.py — Disciplined Entrepreneurship lifecycle engine + dashboard.

Reads a venture's dashboard.md (step checkboxes) and evidence folders, then reports the
lifecycle phase board, the 24-step progress, key metrics, and the single recommended next
action. The lifecycle (Spec-Kit style) is:

    charter -> specify -> [clarify gate] -> plan -> tasks -> [analyze gate] -> implement

Usage:
    python3 status.py <venture-dir>          # full board
    python3 status.py <venture-dir> --next   # just the next recommended command
"""
import os
import re
import sys

# Lifecycle phases, each owning a set of DE steps (step 0 = charter pre-work).
PHASES = [
    {"cmd": "/de-charter",   "label": "Charter",   "steps": [0],
     "desc": "Idea, mission, team values"},
    {"cmd": "/de-specify",   "label": "Specify",   "steps": list(range(1, 7)),
     "desc": "Who is your customer? (Theme 1, steps 1-6)"},
    {"cmd": "/de-plan",      "label": "Plan",      "steps": list(range(7, 20)),
     "desc": "Value, position, model & economics (Themes 2-4, steps 7-19)"},
    {"cmd": "/de-tasks",     "label": "Tasks",     "steps": [20, 21],
     "desc": "Identify & test key assumptions (Theme 5, steps 20-21)"},
    {"cmd": "/de-implement", "label": "Implement", "steps": [22, 23, 24],
     "desc": "MVBP, traction & product plan (Themes 5-6, steps 22-24)"},
]
CLARIFY_TARGET = 10  # interviews wanted before committing to Plan

# Theme grouping for the 24-step board.
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


def count_md(venture, sub):
    d = os.path.join(venture, sub)
    if not os.path.isdir(d):
        return 0
    skip = {"readme.md", "matrix.md"}
    return sum(1 for f in os.listdir(d) if f.lower().endswith(".md") and f.lower() not in skip)


def load(venture):
    done, metrics = set(), ""
    dashboard = os.path.join(venture, "dashboard.md")
    if os.path.isfile(dashboard):
        text = open(dashboard, encoding="utf-8").read()
        for mark, num in STEP_RE.findall(text):
            if mark.lower() == "x":
                done.add(int(num))
        m = re.search(r"##+\s*Key metrics(.*?)(?:\n##\s|\Z)", text, re.DOTALL | re.IGNORECASE)
        if m:
            metrics = m.group(1).strip()
    return done, metrics


def phase_done(p, done):
    return all(s in done for s in p["steps"])


def phase_started(p, done):
    return any(s in done for s in p["steps"])


def next_action(done, interviews):
    """Return (command, why, blocker_or_None)."""
    charter, specify, plan, tasks, implement = PHASES
    if not phase_done(charter, done):
        return charter["cmd"], "Charter the venture — capture the idea, mission, and team values.", None
    if not phase_done(specify, done):
        return specify["cmd"], "Define who your customer is (Theme 1). Start customer interviews now.", None
    # Clarify gate: don't commit to the Plan before validating the beachhead with real customers.
    if not phase_started(plan, done) and interviews < CLARIFY_TARGET:
        blocker = f"only {interviews}/{CLARIFY_TARGET} customer interviews logged"
        return "/de-clarify", "Validate the beachhead is real & homogeneous via primary research.", blocker
    if not phase_done(plan, done):
        return plan["cmd"], "Build the plan: value prop, Core, competitive position, business model, pricing, unit economics.", None
    if not phase_done(tasks, done):
        return tasks["cmd"], "Identify and test your riskiest assumptions before building.", None
    if not phase_done(implement, done):
        return implement["cmd"], "Build the MVBP, prove the dogs eat the dog food, and write the product plan.", None
    return None, "Lifecycle complete — keep iterating. Run /de-analyze and /pitch-deck when raising.", None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only_next = "--next" in sys.argv[1:]
    if len(args) != 1:
        sys.exit("usage: status.py <venture-dir> [--next]")
    venture = args[0].rstrip("/")
    if not os.path.isdir(venture):
        sys.exit(f"error: {venture} is not a directory")

    done, metrics = load(venture)
    interviews = count_md(venture, "interviews")
    cmd, why, blocker = next_action(done, interviews)

    if only_next:
        if cmd:
            print(f"Next: {cmd} — {why}")
            if blocker:
                print(f"  gate: {blocker} (run /de-clarify to satisfy it)")
        else:
            print(f"Next: {why}")
        return

    name = os.path.basename(venture)
    print(f"\nVenture: {name}")
    print("=" * 60)

    # Phase board.
    print("LIFECYCLE")
    for p in PHASES:
        d = sum(1 for s in p["steps"] if s in done)
        if phase_done(p, done):
            icon = "✓"
        elif cmd == p["cmd"]:
            icon = "▶"
        elif phase_started(p, done):
            icon = "~"
        else:
            icon = "·"
        print(f"  {icon} {p['label']:<10} {d}/{len(p['steps']):<2} {p['cmd']:<13} {p['desc']}")
    # Gate notes.
    plan_started = phase_started(PHASES[2], done)
    if interviews < CLARIFY_TARGET:
        flag = "BLOCKING" if not plan_started else "keep going"
        print(f"  gate clarify : {interviews}/{CLARIFY_TARGET} interviews ({flag}) — /de-clarify")
    if phase_started(PHASES[3], done):
        print("  gate analyze : run /de-analyze (red-team) before /de-implement")

    # 24-step board.
    print("-" * 60)
    print("24 STEPS")
    total = 0
    for label, steps in THEMES:
        steps = list(steps)
        d = sum(1 for s in steps if s in done)
        total += d
        print(f"  Theme {label:<38}{bar(d, len(steps))}")
    print(f"  {'OVERALL':<44}{bar(total, 24)}")

    # Evidence + metrics.
    print("-" * 60)
    print(f"Interviews {count_md(venture, 'interviews')}  ·  Competitors {count_md(venture, 'competitors')}"
          f"  ·  Research {count_md(venture, 'research')}")
    if metrics:
        print("\nKey metrics")
        print(metrics)

    print("\n" + "=" * 60)
    if cmd:
        print(f"NEXT: {cmd} — {why}")
        if blocker:
            print(f"      gate: {blocker}")
    else:
        print(f"NEXT: {why}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
tam.py — Bottoms-up Total Addressable Market (Disciplined Entrepreneurship Steps 4 & 14).

    TAM ($/year at 100% market share) = (# end users) x (annual revenue per end user)

DE prefers a *bottoms-up* estimate for a deliberately *focused* beachhead. Build the
number from defensible unit assumptions; every input should trace to PMR or a cited source.

Examples:
    # Single segment
    python3 tam.py --users 1500 --revenue 9000

    # Multiple segments (repeat --segment as NAME:USERS:REVENUE), with +/-25% sensitivity
    python3 tam.py \
        --segment "US:1500:9000" \
        --segment "Europe:1000:9000" \
        --segment "Asia:1000:6333" \
        --sensitivity 25
"""
import argparse
import sys


def human(n):
    """Format a dollar figure compactly ($13.5M, $920K, $1.2B)."""
    a = abs(n)
    if a >= 1_000_000_000:
        return f"${n/1_000_000_000:.2f}B"
    if a >= 1_000_000:
        return f"${n/1_000_000:.2f}M"
    if a >= 1_000:
        return f"${n/1_000:.1f}K"
    return f"${n:,.0f}"


def parse_segment(s):
    parts = s.split(":")
    if len(parts) != 3:
        sys.exit(f"error: --segment must be NAME:USERS:REVENUE (got {s!r})")
    name, users, revenue = parts
    try:
        return name, float(users), float(revenue)
    except ValueError:
        sys.exit(f"error: USERS and REVENUE must be numbers (got {s!r})")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--segment", action="append", default=[], metavar="NAME:USERS:REVENUE",
                   help="A market segment. Repeatable.")
    p.add_argument("--users", type=float, help="End users (single-segment shortcut).")
    p.add_argument("--revenue", type=float, help="Annual revenue per end user (single-segment shortcut).")
    p.add_argument("--sensitivity", type=float, default=20.0, metavar="PCT",
                   help="Low/high band as +/- this %% on BOTH users and revenue (default 20).")
    args = p.parse_args()

    segments = [parse_segment(s) for s in args.segment]
    if args.users is not None and args.revenue is not None:
        segments.append(("(segment)", args.users, args.revenue))
    if not segments:
        p.error("provide --segment NAME:USERS:REVENUE (repeatable) or --users with --revenue")

    print("\nBottoms-up TAM  (TAM = # end users x annual revenue per end user)\n")
    print(f"{'Segment':<16}{'End users':>14}{'Rev/user':>14}{'TAM':>14}")
    print("-" * 58)
    total = 0.0
    for name, users, rev in segments:
        tam = users * rev
        total += tam
        print(f"{name:<16}{users:>14,.0f}{human(rev):>14}{human(tam):>14}")
    print("-" * 58)
    print(f"{'TOTAL':<16}{'':>14}{'':>14}{human(total):>14}\n")

    # Sensitivity: scale both drivers by +/- pct (they compound).
    f = args.sensitivity / 100.0
    low = total * (1 - f) ** 2
    high = total * (1 + f) ** 2
    print(f"Sensitivity (+/-{args.sensitivity:.0f}% on users AND revenue/user):")
    print(f"    low {human(low)}   |   base {human(total)}   |   high {human(high)}\n")

    # Heuristic guidance (Step 2/4).
    if total > 1_000_000_000:
        print("NOTE: > $1B. For a *beachhead* this usually means the segment is too broad — "
              "re-segment (Step 1) to something you can dominate quickly.")
    elif total < 5_000_000:
        print("NOTE: < $5M. May be too small to build a venture on — though a tight, dominable "
              "beachhead can be small (Aulet's SensAble example was ~$10-15M).")
    else:
        print("Within the ~$20-100M beachhead heuristic band (big enough to matter, small enough "
              "to dominate). Treat the band as guidance, not a gate.")
    print()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
unit_economics.py — LTV, COCA, and the LTV:COCA ratio (Disciplined Entrepreneurship Steps 17 & 19).

LTV = net present value of *gross profit* from one customer over years 0..N (year 0 = acquisition):
    profit_t = annual_recurring_revenue x gross_margin x retention**t
    pv_t     = profit_t x (1 - cost_of_capital)**t        # year 0 undiscounted
    LTV      = one_time x gross_margin  +  sum(pv_t for t in 0..N)

COCA = (total sales & marketing spend - retention/support costs) / NEW customers in the period.

Decision rule: a viable business needs LTV >= 3 x COCA.

NOTE ON EXACT FIGURES: this implements the DE NPV-of-gross-profit *structure*. The official
d-eship.com LTV spreadsheet is authoritative for published examples (e.g. $20/mo, 90% GM, 80%
retention, 50% cost of capital -> ~$236), which use its specific year-0/discount conventions.
What drives decisions here is the LTV:COCA ratio and the sensitivity range, not the point estimate.

Examples:
    python3 unit_economics.py --monthly 20 --gross-margin 0.9 --retention 0.8 \
        --cost-of-capital 0.5 --coca 60
    python3 unit_economics.py --arr 1200 --gross-margin 0.75 --retention 0.85 \
        --cost-of-capital 0.35 --sm-spend 250000 --new-customers 800
"""
import argparse
import sys


def ltv(arr, gross_margin, retention, cost_of_capital, one_time=0.0, years=5):
    total = one_time * gross_margin
    for t in range(0, years + 1):
        profit_t = arr * gross_margin * (retention ** t)
        pv_t = profit_t * ((1 - cost_of_capital) ** t)
        total += pv_t
    return total


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    rev = p.add_mutually_exclusive_group(required=True)
    rev.add_argument("--arr", type=float, help="Annual recurring revenue per customer.")
    rev.add_argument("--monthly", type=float, help="Monthly recurring revenue (x12 -> ARR).")
    p.add_argument("--one-time", type=float, default=0.0, help="One-time up-front revenue (year 0).")
    p.add_argument("--gross-margin", type=float, default=0.7, help="Gross margin 0-1 (default 0.7).")
    p.add_argument("--retention", type=float, default=0.8, help="Annual retention 0-1 (default 0.8).")
    p.add_argument("--cost-of-capital", type=float, default=0.5,
                   help="Annual cost of capital 0-1 (default 0.5; ~0.12 cheap debt, ~0.5 VC-backed).")
    p.add_argument("--years", type=int, default=5, help="Horizon in years (default 5 -> years 0..5).")
    # COCA: either direct, or computed.
    p.add_argument("--coca", type=float, help="Cost of customer acquisition (direct).")
    p.add_argument("--sm-spend", type=float, help="Total sales & marketing spend in the period.")
    p.add_argument("--new-customers", type=float, help="NEW customers acquired in the period.")
    args = p.parse_args()

    for name, v in (("gross-margin", args.gross_margin), ("retention", args.retention),
                    ("cost-of-capital", args.cost_of_capital)):
        if not 0 <= v <= 1:
            sys.exit(f"error: --{name} must be between 0 and 1 (got {v})")

    arr = args.arr if args.arr is not None else args.monthly * 12

    coca = None
    if args.coca is not None:
        coca = args.coca
    elif args.sm_spend is not None and args.new_customers:
        coca = args.sm_spend / args.new_customers

    value = ltv(arr, args.gross_margin, args.retention, args.cost_of_capital,
                one_time=args.one_time, years=args.years)

    print("\nLTV  (NPV of gross profit, years 0..{})".format(args.years))
    print(f"    ARR/customer .......... ${arr:,.0f}" + (f"  (${args.monthly:,.0f}/mo)" if args.monthly else ""))
    if args.one_time:
        print(f"    One-time (year 0) ..... ${args.one_time:,.0f}")
    print(f"    Gross margin .......... {args.gross_margin:.0%}")
    print(f"    Retention (annual) .... {args.retention:.0%}")
    print(f"    Cost of capital ....... {args.cost_of_capital:.0%}")
    print(f"    => LTV ................ ${value:,.0f}\n")

    if coca is not None:
        ratio = value / coca if coca else float("inf")
        verdict = "PASS (>= 3:1)" if ratio >= 3 else ("MARGINAL (1-3:1)" if ratio >= 1 else "FAIL (< 1:1)")
        if args.sm_spend is not None and args.new_customers:
            print(f"COCA  = ${args.sm_spend:,.0f} / {args.new_customers:,.0f} new customers = ${coca:,.0f}")
        else:
            print(f"COCA  = ${coca:,.0f}")
        print(f"    LTV:COCA = {ratio:.1f}:1   ->   {verdict}")
        print("    (DE rule of thumb: a scalable business needs LTV >= 3 x COCA. "
              "COCA also falls over time as word of mouth compounds.)\n")
    else:
        print("COCA  not provided. Pass --coca, or --sm-spend with --new-customers, to test "
              "the LTV:COCA >= 3:1 rule.\n")

    # Sensitivity: LTV is highly sensitive to retention and cost of capital.
    cocs = sorted({0.12, 0.35, 0.5, 0.7, args.cost_of_capital})
    rets = sorted({0.70, 0.80, 0.90, args.retention})
    print("LTV sensitivity (rows = retention, cols = cost of capital):")
    print("    ret \\ coc " + "".join(f"{c:>9.0%}" for c in cocs))
    for r in rets:
        cells = "".join(f"{ltv(arr, args.gross_margin, r, c, args.one_time, args.years):>9,.0f}" for c in cocs)
        print(f"    {r:>7.0%}  {cells}")
    print()


if __name__ == "__main__":
    main()

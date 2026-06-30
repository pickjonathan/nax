---
description: Estimate market size / TAM, bottoms-up (DE Steps 4 & 14)
argument-hint: [venture-slug or market description]
---

Use the **disciplined-entrepreneurship** skill (`references/formulas.md`) to size the market for
**$ARGUMENTS**.

1. Dispatch the **`tam-estimator`** agent to build a **bottoms-up** TAM = (# end users) × (annual
   revenue per end user), cross-checked top-down, with every assumption sourced and a sensitivity
   range.
2. Compute and stress-test the math with the script (don't hand-derive):
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/tam.py --segment "NAME:USERS:REVENUE" --sensitivity 25`
3. Apply the DE sanity check (~$20–100M beachhead heuristic; >$1B suggests the segment is too broad).
   Write the result and assumptions into `01-who-is-your-customer.md` / `unit-economics.md` and update
   `dashboard.md`.

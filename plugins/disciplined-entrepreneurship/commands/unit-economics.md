---
description: Compute LTV, COCA, and the LTV:COCA ratio (DE Steps 17 & 19)
argument-hint: [venture-slug]
allowed-tools: Bash(python3:*), Read, Write
---

Use the **go-to-market** skill (`disciplined-entrepreneurship/references/formulas.md`) to model the
unit economics for venture **$ARGUMENTS**.

1. Gather inputs from the workspace (recurring revenue, gross margin, retention, cost of capital;
   sales & marketing spend incl. founder time at market rate; new customers). Note the basis for each.
2. Compute with the script (don't hand-derive):
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/unit_economics.py --monthly <rev> --gross-margin <m> --retention <r> --cost-of-capital <c> --sm-spend <s> --new-customers <n>`
3. Interpret: LTV, COCA, and the **LTV:COCA ratio against the 3:1 rule**; show the sensitivity table;
   name the biggest lever (recurring revenue, margin, retention, or COCA) and how COCA should fall
   over time. Write the workings into `unit-economics.md` and update `dashboard.md`.

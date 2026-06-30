---
description: Show a venture's 24-step progress and key metrics
argument-hint: [venture-slug]
allowed-tools: Bash(python3:*), Bash(ls:*), Read
---

Available ventures: !`ls -1 ventures 2>/dev/null || echo "(none yet — run /validate-idea)"`

Show the status for venture **$ARGUMENTS** (if empty and only one venture exists, use it; if several,
ask which). Run:

`python3 ${CLAUDE_PLUGIN_ROOT}/scripts/status.py ventures/$ARGUMENTS`

Then interpret the output for the founder: which theme they're in, what the key metrics say (call out
any `_TBD_` that should be filled), the **single most important next step**, and the **biggest open
risk or unvalidated assumption**. Keep it short and action-oriented.

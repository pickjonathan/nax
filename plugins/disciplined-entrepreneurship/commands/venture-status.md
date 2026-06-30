---
description: Show a venture's lifecycle phase board, 24-step progress, and key metrics
argument-hint: [venture-slug]
allowed-tools: Bash(python3:*), Bash(ls:*), Read
---

Available ventures: !`ls -1 ventures 2>/dev/null || echo "(none yet — run /validate-idea or /de-charter)"`

Show the status for venture **$ARGUMENTS** (if empty and only one venture exists, use it; if several,
ask which). Run the lifecycle engine:

`python3 ${CLAUDE_PLUGIN_ROOT}/scripts/status.py ventures/$ARGUMENTS`

Then interpret the output for the founder: the **current lifecycle phase** and any **gate blocker**
(clarify / analyze), what the **key metrics** say (call out any `_TBD_` worth filling), and the
**single most important next action**. Keep it short and action-oriented. For just the next step, use
`/de-next $ARGUMENTS`.

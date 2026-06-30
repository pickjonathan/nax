---
description: "DE lifecycle ▸ Show the current phase and the exact next action"
argument-hint: [venture-slug]
allowed-tools: Bash(python3:*), Bash(ls:*), Read
---

Ventures: !`ls -1 ventures 2>/dev/null || echo "(none yet — run /de-charter \"My Idea\")"`

For venture **$ARGUMENTS** (if empty and only one venture exists, use it; if several, ask which), run
the lifecycle engine:

`python3 ${CLAUDE_PLUGIN_ROOT}/scripts/status.py ventures/$ARGUMENTS --next`

Then state plainly: the **current phase**, any **gate blocker**, and the **exact next command** to
run — and offer to run it now. For the full phase board + 24-step progress + metrics, use
`/venture-status $ARGUMENTS`.

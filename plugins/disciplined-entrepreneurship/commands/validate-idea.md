---
description: Validate a startup idea end-to-end — drives the DE lifecycle
argument-hint: [idea name or venture-slug]
---

Use the **disciplined-entrepreneurship** skill to validate **$ARGUMENTS** by driving the DE
**lifecycle**: charter → specify → clarify → plan → tasks → analyze → implement.

1. **Locate or create the venture.** If no workspace under `ventures/` matches, scaffold one:
   `bash ${CLAUDE_PLUGIN_ROOT}/scripts/new_venture.sh "$ARGUMENTS"` (creates `./ventures/<slug>/`).
2. **Find the current phase.** Run the lifecycle engine:
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/status.py ventures/<slug> --next`
3. **Run the recommended phase command** it points to — `/de-charter`, `/de-specify`, `/de-clarify`,
   `/de-plan`, `/de-tasks`, `/de-analyze`, or `/de-implement` — and **honor the gates** (don't plan
   before the clarify gate passes; don't build before `/de-analyze`).
4. **Record evidence** in the right docs, route assumptions to `assumptions.md`, update `dashboard.md`
   and `00-summary.md`, then re-check `--next` and continue to the next phase. It's a cycle — loop
   back when an interview breaks an earlier assumption.
5. **Be the disciplined, skeptical co-founder.** Evidence over opinion; one narrow beachhead;
   quantify bottoms-up; never stop doing PMR.

Use `/de-next` anytime to see the next action, or `/venture-status` for the full board.

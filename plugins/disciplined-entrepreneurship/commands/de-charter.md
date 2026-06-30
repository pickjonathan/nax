---
description: "DE lifecycle ▸ Charter a venture (idea, mission, team values — Phase 0)"
argument-hint: [idea name or venture-slug]
---

Use the **disciplined-entrepreneurship** skill. Begin (or open) the venture for: **$ARGUMENTS**

1. **Scaffold if needed.** If no matching workspace exists under `ventures/`, create one:
   `bash ${CLAUDE_PLUGIN_ROOT}/scripts/new_venture.sh "$ARGUMENTS"` (it writes to `./ventures/<slug>/`
   in the current project).
2. **Fill the charter.** Open `charter.md` and work with the founder to capture: the idea (one
   paragraph), **mission / passions / values / goals** (these drive beachhead selection in Step 2),
   the founding team, the **validation success criteria**, and constraints.
3. **Advance.** Mark **Step 0** `[x]` in `dashboard.md` once the charter is filled.
4. Then run `/de-next <slug>` and proceed to **`/de-specify <slug>`** (define who the customer is).

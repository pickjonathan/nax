---
description: Validate a startup idea end-to-end with Disciplined Entrepreneurship
argument-hint: [idea name or venture slug]
---

Use the **disciplined-entrepreneurship** skill to validate this idea: **$ARGUMENTS**

1. **Locate or create the workspace.** Check `ventures/` for an existing workspace matching this idea.
   If found, read its `dashboard.md` and `00-summary.md` to learn where the founder already is. If
   not, scaffold one:
   `bash ${CLAUDE_PLUGIN_ROOT}/scripts/new_venture.sh "$ARGUMENTS"`
2. **Meet them where they are.** Do not restart from Step 1 if earlier steps are already evidenced —
   identify the next unfinished step from the dashboard.
3. **Work the next step properly.** Read the matching `references/theme-N-*.md` for method. For
   research-heavy steps, dispatch the relevant agents — `market-researcher`, `competitor-analyst`,
   `tam-estimator`, `customer-discovery-analyst`, `business-model-architect` — and run independent
   ones in parallel.
4. **Record evidence.** Write findings into the right theme doc, route every assumption to
   `assumptions.md`, and update `dashboard.md` and `00-summary.md`.
5. **Be the disciplined, skeptical co-founder.** Evidence over opinion; one narrow beachhead; quantify
   bottoms-up. End by naming the single riskiest assumption and the next concrete action. If the idea
   is still raw, get the founder into customer conversations early.

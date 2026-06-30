# The DE Lifecycle — a Spec-Kit-style path through the 24 steps

The opinionated, phase-gated way to run a venture through Disciplined Entrepreneurship. It mirrors
GitHub **Spec Kit**'s lifecycle (`specify → clarify → plan → tasks → implement`) but follows DE's 6
themes / 24 steps. The engine `scripts/status.py` tracks where you are and what to do next.

## Phases

| Phase | Command | DE steps | Spec-Kit analog | Done when |
|---|---|---|---|---|
| **Charter** | `/de-charter` | 0 | constitution / init | idea, mission, and team values captured (`charter.md`) |
| **Specify** | `/de-specify` | 1–6 | specify | beachhead, end-user profile, TAM, persona, use case (`01-*.md`) |
| **Clarify** *(gate)* | `/de-clarify` | PMR (Step 9) | clarify | ~10 real interviews validate a real, homogeneous beachhead (`interviews/`) |
| **Plan** | `/de-plan` | 7–19 | plan | value prop, Core, competitive position, model, pricing, LTV:COCA (`02–04`, `unit-economics.md`) |
| **Tasks** | `/de-tasks` | 20–21 | tasks | top assumptions ranked + experiments designed/run (`assumptions.md`) |
| **Analyze** *(gate)* | `/de-analyze` | — | analyze | riskiest assumptions adversarially stress-tested |
| **Implement** | `/de-implement` | 22–24 | implement | MVBP shipped, dogs eat the dog food, product plan (`05–06`, `pitch-deck.md`) |

## The two gates (DE discipline, enforced)

- **Clarify before Plan.** You don't get to design the product/business until you've *talked to real
  customers* and confirmed the beachhead is real and homogeneous. The engine blocks Plan while
  interviews are thin (target ~10) and recommends `/de-clarify`.
- **Analyze before Implement.** You don't *build* until you've *de-risked* the assumptions the plan
  rests on. The engine surfaces `/de-analyze` (the `assumption-red-teamer`) before `/de-implement`.

## The engine

```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/status.py <venture> [--next]
```

It reads the venture's `dashboard.md` step checkboxes (step 0 = charter) and counts `interviews/`,
then: computes each phase's completion, evaluates the gates, and prints the recommended **next
command**. `--next` prints just that next line; without it you get the full phase board + 24-step
progress + key metrics. The **phase is derived from which steps are marked `[x]`** — so the single
source of truth is the dashboard. Mark a step done only when it is *evidenced*.

## Driving the lifecycle

- **`/de-next <venture>`** — current phase, gate blockers, and the exact next command (the driver).
- **`/validate-idea <idea>`** — autopilot: scaffolds if needed and advances through the phases.
- **`/venture-status <venture>`** — the full board.
- **Phase commands** — `/de-charter`, `/de-specify`, `/de-clarify`, `/de-plan`, `/de-tasks`,
  `/de-analyze`, `/de-implement`. Each delegates to the focused tools/skills/agents and the relevant
  `theme-N` reference, then advances the dashboard.

## It's a cycle, not a waterfall

DE is iterative: an interview at Clarify routinely rewrites the Specify persona; a failed pricing
test at Tasks sends you back to Plan; failing Step 11's "upper-right" test sends you back to the
Core (10) and market (1–5). Loop back freely — **never stop doing primary market research.**

## Phase ≠ theme (a note)

The lifecycle's **Plan** phase spans DE Themes 2–4 (steps 7–19) for a tighter command surface, while
the dashboard still groups the 24 steps by their 6 canonical themes. The engine maps steps → phases;
the two views are complementary.

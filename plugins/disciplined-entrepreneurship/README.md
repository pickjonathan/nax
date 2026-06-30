# Disciplined Entrepreneurship — Founder's Idea-Validation Plugin

Take a tech idea from "I think this could work" to a **falsifiable, customer-grounded,
investor-ready** business using Bill Aulet's **Disciplined Entrepreneurship (DE)** framework (24
Steps across 6 themes), surrounded by the market-research, competitive-analysis, go-to-market, and
pitch-deck toolkit a founder actually needs.

This plugin ships **5 skills**, **7 agents**, **20 commands** (8 lifecycle + 12 tools), helper
**scripts**, and a per-idea **venture workspace** template.

Two ways to install: the **plugin** (this marketplace), or **vendored into a project's `.claude/`** via
the `nax` CLI (`uvx --from git+https://github.com/pickjonathan/nax nax init`) — use one per project.

## Quick start (after installing the plugin)

```
/validate-idea My Idea Name      # scaffold + run/continue the full validation
/venture-status my-idea-name     # 24-step progress + key metrics
```

Or just talk to Claude naturally — *"help me validate my idea for…"*, *"size this market"*,
*"who are my competitors"*, *"is this viable"*, *"build my pitch deck"* — and the skills trigger
automatically. Ventures are created in **your current project** under `./ventures/<slug>/`.

## The framework: 24 Steps, 6 themes

| Theme (the question) | Steps |
|---|---|
| **1 — Who is your customer?** | 1 Market Segmentation · 2 Beachhead · 3 End User Profile · 4 TAM · 5 Persona · 6 Full Life Cycle Use Case |
| **2 — What can you do for your customer?** | 7 Product Spec · 8 Quantify Value Prop · 9 Next 10 Customers · 10 Define Your Core · 11 Competitive Position |
| **3 — How does your customer acquire it?** | 12 Decision-Making Unit · 13 Acquisition Process |
| **4 — How do you make money?** | 14 Follow-on TAM · 15 Business Model · 16 Pricing · 17 LTV · 18 Sales Process · 19 COCA |
| **5 — How do you design & build it?** | 20 Key Assumptions · 21 Test Assumptions · 22 MVBP · 23 "Dogs Eat the Dog Food" |
| **6 — How do you scale?** | 24 Product Plan |

Five principles run through every step: **one beachhead dominated · primary research over opinion ·
quantify bottoms-up · capture value (not just create it) · evidence beats eloquence.**

## The lifecycle (Spec-Kit-style)

Drive a venture through gated phases — analogous to Spec Kit's `specify → clarify → plan → tasks →
implement`:

`/de-charter` → `/de-specify` → `/de-clarify` *(gate)* → `/de-plan` → `/de-tasks` → `/de-analyze`
*(gate)* → `/de-implement`

Use **`/de-next`** to see the current phase + next command, **`/validate-idea`** to auto-advance, and
**`/venture-status`** for the full board. The two gates enforce DE's discipline — talk to customers
before planning, de-risk before building. The engine (`scripts/status.py`) derives the phase from the
dashboard. Full spec: `skills/disciplined-entrepreneurship/references/lifecycle.md`.

## What's inside

**Skills** (`skills/`, auto-trigger on natural language)
- `disciplined-entrepreneurship` — the spine: orchestrates the 24 steps; 12 reference docs
  (per-theme guides, exact TAM/LTV/COCA formulas, the PMR method, the lifecycle, pitfalls, glossary).
- `market-research` · `competitive-analysis` · `go-to-market` · `pitch-deck` — each with its own
  references.

**Agents** (`agents/`, autonomous workers Claude dispatches)
- `market-researcher` · `competitor-analyst` · `customer-discovery-analyst` · `tam-estimator` ·
  `business-model-architect` · `pitch-deck-architect` · `assumption-red-teamer` (your skeptical
  co-founder).

**Commands** (`commands/`, slash entry points)
- **Lifecycle** (the gated path): `/de-charter` · `/de-specify` · `/de-clarify` · `/de-plan` ·
  `/de-tasks` · `/de-analyze` · `/de-implement` · `/de-next`.
- **Tools** (à la carte): `/validate-idea` · `/de-step` · `/venture-status` · `/market-research` ·
  `/size-market` · `/personas` · `/competition` · `/gtm` · `/business-model` · `/unit-economics` ·
  `/pitch-deck` · `/red-team`.

**Scripts** (`scripts/`, invoked by the commands via `${CLAUDE_PLUGIN_ROOT}`)
- `new_venture.sh "Name"` — scaffold a venture workspace into `./ventures` in your project.
- `tam.py` — bottoms-up TAM with sensitivity.
- `unit_economics.py` — LTV, COCA, and the LTV:COCA ratio (vs the 3:1 rule).
- `status.py <venture> [--next]` — lifecycle engine: phase board, gates, 24-step progress, metrics, next action.

**Venture template** (`templates/venture/`) — copied into your project per idea: a living workbook
with a doc per theme, a dashboard, an assumptions register, unit-economics workings, a pitch-deck
outline, and `research/` · `interviews/` · `competitors/` evidence folders.

## How to use it well

1. **Go in order, but loop back.** Steps build on each other, but validation is iterative — an
   interview routinely rewrites an earlier step. Treat the workspace as living.
2. **Talk to customers early and often.** Inquiry, not advocacy. Secondary data only frames and finds.
3. **Quantify with sources.** Every number carries a stated assumption or a citation; untested
   beliefs go in `assumptions.md`, not into the plan as facts.
4. **Red-team yourself.** Run `/red-team` before you commit resources or pitch.

## Notes & attribution

Implements the framework from **Bill Aulet, *Disciplined Entrepreneurship: 24 Steps to a Successful
Startup*** (and the companion *Startup Tactics* by Paul Cheek & Bill Aulet), MIT Martin Trust Center.
Independent learning/execution tool, not affiliated with or endorsed by the authors — buy the book
and use the official [Disciplined Entrepreneurship Toolbox](https://www.d-eship.com/) for the
canonical worksheets.

- **Step numbering** follows the 2nd edition (MVBP = 22, "dogs eat the dog food" = 23, Product Plan =
  24; LTV = 17, COCA = 19). Step 14 (follow-on TAM) sits at the Theme 3/4 seam; placed in Theme 4 here.
- **Formula caveat:** `unit_economics.py` implements the DE NPV-of-gross-profit *structure*; the
  official d-eship LTV spreadsheet is authoritative for exact published figures. Treat the
  **LTV:COCA ratio and sensitivity** as the decision drivers.
- Source links are cited at the bottom of each reference doc.

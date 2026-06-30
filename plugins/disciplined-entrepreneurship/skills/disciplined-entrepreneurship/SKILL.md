---
name: disciplined-entrepreneurship
description: >-
  This skill should be used to validate a startup or tech-product idea end to end using Bill
  Aulet's Disciplined Entrepreneurship (DE) framework — the 24 Steps across 6 themes. Use it
  whenever the user wants to "validate my idea", "is my startup idea any good", "should I build
  this", "find product-market fit", "run me through Disciplined Entrepreneurship / the 24 steps",
  pick a "beachhead market", build an "end-user profile / persona", size a market ("TAM"),
  "define my value proposition", figure out "who my customer is", or work any specific DE step.
  Use it even when the user doesn't name the framework but is clearly trying to figure out
  whether a business idea is real and for whom. It orchestrates the full journey and dispatches
  to the market-research, competitive-analysis, go-to-market, and pitch-deck skills, the founder
  agents, and the per-venture workspace.
---

# Disciplined Entrepreneurship — Idea Validation Engine

Disciplined Entrepreneurship (DE), by Bill Aulet (MIT Martin Trust Center), turns "I have an
idea" into a falsifiable, customer-grounded business through **24 Steps** organized under **6
themes**. This skill is the spine of a founder's toolkit: it runs the journey, keeps evidence in
a per-venture workspace, and hands heavy lifting to specialist skills and agents.

The single most important idea: **the customer is not paying you to exist.** Every step exists to
replace a founder's optimistic assumption with evidence from a real, specific customer.

## Five principles that govern every step

1. **One beachhead, dominated.** Pick a single, narrow, homogeneous market and win it completely
   before expanding. A large share of a tiny market beats a tiny share of a huge one. Resist
   keeping options open — focus is the whole point.
2. **Primary market research over opinion.** Talk to real potential customers directly. Practice
   **inquiry, not advocacy**: you are there to learn, never to pitch. "There are no facts inside
   the building." Never stop doing PMR. (See the `market-research` skill.)
3. **Quantify, bottoms-up.** TAM, value, LTV, COCA are numbers with stated assumptions and
   sources — built up from unit economics, not borrowed from an analyst's top-down headline.
4. **Capture value, don't just create it.** A great product that can't charge is not a business.
   Business model (Step 15) and pricing (Step 16) decide whether value created becomes value kept.
5. **Evidence beats eloquence.** "The dogs must eat the dog food" — paid usage by real customers,
   not survey enthusiasm, is the only proof that counts.

## The 24 Steps across 6 themes

| Theme (the question) | Steps |
|---|---|
| **1 — Who is your customer?** | 1 Market Segmentation · 2 Select a Beachhead Market · 3 Build an End User Profile · 4 Calculate the TAM for the Beachhead · 5 Profile the Persona · 6 Full Life Cycle Use Case |
| **2 — What can you do for your customer?** | 7 High-Level Product Specification · 8 Quantify the Value Proposition · 9 Identify Your Next 10 Customers · 10 Define Your Core · 11 Chart Your Competitive Position |
| **3 — How does your customer acquire your product?** | 12 Determine the Decision-Making Unit (DMU) · 13 Map the Process to Acquire a Paying Customer |
| **4 — How do you make money off your product?** | 14 TAM for Follow-on Markets · 15 Design a Business Model · 16 Set Your Pricing Framework · 17 Calculate LTV · 18 Map the Sales Process · 19 Calculate COCA |
| **5 — How do you design & build your product?** | 20 Identify Key Assumptions · 21 Test Key Assumptions · 22 Define the MVBP · 23 Show "The Dogs Will Eat the Dog Food" |
| **6 — How do you scale your business?** | 24 Develop a Product Plan |

The deep how-to for each theme lives in `references/`. Read the relevant theme file before
guiding a step — do not work from this summary alone.

## How to run a validation

1. **Scaffold (or locate) the venture workspace.** Each idea gets its own folder under
   `ventures/<slug>/`. To create one, run the scaffolder:
   `bash ${CLAUDE_PLUGIN_ROOT}/scripts/new_venture.sh "<Idea name>"`.
   It copies `ventures/_TEMPLATE/` (the guided workbook: theme docs, dashboard, assumptions,
   unit-economics, pitch-deck, and research/interviews/competitors folders).
2. **Establish where the founder is.** Read the venture's `dashboard.md`. Don't restart from
   Step 1 if Steps 1–5 are already evidenced. Meet them where they are.
3. **Work the current step properly.** Open the matching `references/theme-N-*.md`, follow its
   procedure, and write findings into the right theme doc — always tied to evidence in
   `interviews/`, `research/`, or a labelled item in `assumptions.md`.
4. **Iterate, don't waterfall.** The steps build logically (you can't size a market before you've
   defined the customer), but real validation loops back constantly. When an interview breaks an
   earlier assumption, revise the earlier step. Treat the workspace as living.
5. **Update the dashboard and one-pager** after each session so progress and key metrics
   (TAM, LTV, COCA, LTV:COCA, # interviews, MVBP status) stay current.

If the user has only a raw idea, start at Step 1 (segmentation) — but get them into customer
conversations as early as possible; PMR fuels every step.

## When to dispatch agents

Hand off context-heavy or parallelizable work to specialist subagents, then synthesize their
returned artifacts into the workspace:

- **`market-researcher`** — secondary research + market-sizing inputs for a segment.
- **`customer-discovery-analyst`** — generate an interview guide; synthesize interview notes into
  patterns, pains, jobs, and an end-user profile.
- **`tam-estimator`** — bottoms-up (and cross-checked top-down) TAM for Steps 4 and 14.
- **`competitor-analyst`** — research a competitor set and build the comparison matrix (Step 11).
- **`business-model-architect`** — business model, pricing, and LTV/COCA (Steps 15–19).
- **`assumption-red-teamer`** — adversarially stress-test the riskiest assumptions (Steps 20–21).
  Invoke this proactively when the founder sounds over-confident or evidence is thin.
- **`pitch-deck-architect`** — assemble the investor deck from the validated workspace.

Run independent agents in parallel (e.g. market-researcher + competitor-analyst) when scoping a
new segment.

## Scripts

Deterministic helpers in `scripts/` (prefer them over re-deriving math by hand):

- **`new_venture.sh "<name>"`** — scaffold a venture workspace from the template.
- **`tam.py`** — bottoms-up TAM = (# end users) × (annual revenue per end user), with sensitivity.
- **`unit_economics.py`** — LTV (NPV of profit, years 0–5), COCA, and the LTV:COCA ratio with a
  pass/fail against the 3:1 rule.
- **`status.py <venture-dir>`** — print the 24-step completion dashboard and key metrics.

Run `python3 <script> --help` for usage.

## Reference files (load the relevant one before going deep)

- `references/overview.md` — the philosophy, the non-linear flow, and how the steps interlock.
- `references/theme-1-who-is-your-customer.md` — Steps 1–6 (segmentation → beachhead → profile → TAM → persona → use case).
- `references/theme-2-what-can-you-do.md` — Steps 7–11 (product spec, value prop, next 10, core, competitive position).
- `references/theme-3-how-they-acquire.md` — Steps 12–13 (DMU, buying process).
- `references/theme-4-how-you-make-money.md` — Steps 14–19 (follow-on TAM, model, pricing, LTV, sales, COCA).
- `references/theme-5-how-you-build.md` — Steps 20–23 (assumptions, testing, MVBP, dogs eat dog food).
- `references/theme-6-how-you-scale.md` — Step 24 (product plan, follow-on sequencing).
- `references/formulas.md` — exact TAM, LTV, and COCA math with worked numbers.
- `references/primary-market-research.md` — interview method, question bank, anti-patterns, synthesis.
- `references/pitfalls.md` — the most common ways founders mislead themselves at each step.
- `references/glossary.md` — DE vocabulary (DMU roles, MVBP, Core, beachhead, lighthouse customer…).

## Related skills

Reach for these when the work concentrates in one area:
`market-research` (PMR + secondary + sizing), `competitive-analysis` (Steps 10–11, positioning,
Porter, matrices), `go-to-market` (Steps 12–19: DMU, model, pricing, sales, economics),
`pitch-deck` (turn the workspace into an investor deck).

## Quality bar

- Every quantitative claim cites a source or a labelled assumption — no unsourced numbers.
- Every customer claim traces to a real conversation, not the founder's belief.
- The beachhead stays singular and narrow; push back on scope creep.
- Distinguish facts from assumptions explicitly, and route assumptions to `assumptions.md`.
- Be the disciplined, skeptical co-founder: encouraging about the process, ruthless about evidence.

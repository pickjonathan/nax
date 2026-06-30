---
name: go-to-market
description: >-
  This skill should be used to design how a startup acquires customers and makes money — the
  go-to-market motion, decision-making unit, sales process, business model, pricing, and unit
  economics (DE Steps 12–19). Use it whenever the user wants to "design a go-to-market / GTM
  strategy", "choose a business model", "set pricing / a pricing strategy", "map the sales process",
  "figure out the DMU / who buys", "calculate LTV / CAC / COCA / unit economics", "is this business
  viable", "PLG vs sales-led", or "how do I actually sell this". It applies the Disciplined
  Entrepreneurship monetization steps and dispatches the business-model-architect agent. Use it even
  when the user just asks "how do I make money from this?"
---

# Go-to-Market — Acquire Customers and Make Money (Steps 12–19)

Turn a validated product-for-a-customer into a viable, scalable commercial engine. The logic:
understand **who buys and how** (12–13), choose **how you capture value** (15–16), prove the **unit
economics work** (17, 19), and design the **engine that scales** (18).

## 1. Who buys, and how (Steps 12–13)

- **Map the DMU** — champion, end user, primary economic buyer, influencers, veto holders, and
  purchasing (neutralize purchasing; sell to the economic buyer + champion). Name real people.
- **Map the buying process** — the customer's path from awareness to payment; estimate the sales-cycle
  length and surface showstoppers (budget cycle, security/legal review).
- Method: `../disciplined-entrepreneurship/references/theme-3-how-they-acquire.md`.

## 2. How you capture value (Steps 15–16)

- **Business model (Step 15)** — choose an archetype deliberately; don't default to "how the industry
  does it" or to cost-plus. A business model is *not* pricing, and "free" is not a model. The 17
  archetypes and the 4-lens selection framework are in
  `../disciplined-entrepreneurship/references/theme-4-how-you-make-money.md`; selection guidance and
  the GTM-motion fit are in `references/business-models-and-pricing.md`.
- **Pricing (Step 16)** — **value-based**: price as a fraction of the quantified Step 8 value, leaving
  the customer a clear multiple. Segment pricing. Use lighthouse-customer terms for early references.
  Never set a high public price and then discount publicly.

## 3. Prove the unit economics (Steps 17, 19)

- **LTV** = NPV of gross profit over years 0–5 (built on margin, retention, cost of capital — not
  revenue). **COCA** = all sales & marketing spend ÷ new customers (value founder time at market
  rate; it falls over time via word of mouth).
- **The test: LTV ≥ 3 × COCA.** Math in `../disciplined-entrepreneurship/references/formulas.md`;
  compute and stress-test with `${CLAUDE_PLUGIN_ROOT}/scripts/unit_economics.py`. Record in
  the venture's `unit-economics.md`.

## 4. Design the engine that scales (Step 18)

Map the **revenue engine across three horizons**: short term (high-touch, founder-led, high COCA) →
medium (channels + customer success) → long (self-serve/pull, word of mouth, low COCA). Choose the
**GTM motion** consistent with the DMU and economics:
- **Product-led (PLG / bottoms-up)** — product drives acquisition; fits low-friction, high-volume,
  short-time-to-value, low-ACV. Lower per-customer cost but needs scale.
- **Sales-led (top-down)** — reps sell to economic buyers; fits high-ACV, complex, multi-stakeholder
  enterprise buys. Higher COCA, demands high LTV.
- **Hybrid / sales-assisted** — in between. (Details in `references/business-models-and-pricing.md`.)

## Workflow

Dispatch the **`business-model-architect`** agent to propose model + pricing + a full LTV/COCA model
for a venture. Then write results into `03-how-they-acquire.md`, `04-how-you-make-money.md`, and
`unit-economics.md`, and update `dashboard.md`.

## Related
`disciplined-entrepreneurship` (Steps 12–19) · `competitive-analysis` (position informs pricing) ·
`pitch-deck` (unit economics → the business-model & financials slides) · agent:
`business-model-architect`.

## Reference
- `references/business-models-and-pricing.md` — archetype selection, GTM motions (PLG vs sales-led),
  and the value-based pricing playbook.

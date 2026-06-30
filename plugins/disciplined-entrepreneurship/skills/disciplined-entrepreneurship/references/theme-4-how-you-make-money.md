# Theme 4 — How Do You Make Money Off Your Product? (Steps 14–19)

How you **capture** value. The model and pricing decide whether the value you create becomes value
you keep, and the unit economics (LTV vs COCA) decide whether the business can scale. Exact math for
Steps 14, 17, and 19 lives in `formulas.md`; the `tam.py` and `unit_economics.py` scripts compute it.

---

## Step 14 — Calculate the TAM for Follow-on Markets

**Question:** Once you win the beachhead, where next — and is the **total** opportunity big enough to
matter? A sanity check that reassures the team and investors there's a venture-scale prize beyond the
(deliberately narrow) beachhead.

**Tool — a list of follow-on markets**, each with a quick TAM (same bottom-up method as Step 4). Two
expansion vectors:
- **Upsell / cross-sell** — sell the *same customer* additional products or applications.
- **Adjacent markets** — sell the *same core product* to neighbouring segments that share your Core
  and value proposition (the next bowling pins).

**How to do it:** brainstorm 5–10 follow-on opportunities → estimate each TAM quickly → sum them.
Keep it lightweight — **do not let expansion distract from beachhead dominance.**

**Common mistakes:** front-loading expansion before the beachhead is won; over-engineering these
estimates; double-counting customers across follow-on markets.

---

## Step 15 — Design a Business Model

**Question:** How will you capture a portion of the value you create? The right model can dramatically
**lower COCA, raise LTV, and create competitive advantage** — and it is **hard to change later**, so
the initial choice is strategic.

**Two principles:** (1) **"A business model is not pricing."** The model is *how* you charge (the unit
and mechanism); the number comes in Step 16. (2) **"Free is not a business model."** Free can be an
acquisition tactic, but you need a capture mechanism.

**The 17 business-model archetypes:**
1. **One-time up-front charge + maintenance** — sell the asset, then recurring support fees.
2. **Cost plus** — your cost plus a fixed margin (common in government; low-margin, low-innovation).
3. **Hourly rates** — bill for time (consulting/services).
4. **Subscription / leasing** — recurring access fee.
5. **Licensing** — charge for the right to use IP; you license know-how, not a full product (high
   margin, scalable).
6. **Consumables** — recurring sale of items used up in operation.
7. **Up-sell high-margin products (razor-and-blade)** — cheap base item, profit on refills (printer +
   ink).
8. **Advertising** — users free; advertisers pay for attention/data.
9. **Reselling the data collected** (or temporary access to it) — monetize the data your product
   generates.
10. **Transaction fee** — take a cut of each transaction you enable (marketplaces, payments).
11. **Usage-based** — pay per unit consumed (metered).
12. **"Cell-phone" plan** — fixed fee for an allotment, with overage charges.
13. **Parking-meter / penalty charges** — profit mainly on penalties/overages/late fees.
14. **Microtransactions** — many tiny payments (e.g. $0.99 in-app).
15. **Shared savings / gain-share** — paid a fraction of the savings/value you create.
16. **Franchise** — license your whole proven system to operators.
17. **Operating & maintenance** — you run/operate the asset for the customer ongoing.

**Selection framework (4 lenses, from the Step 1–14 work):**
- **Value creation** — the quantified value (Step 8); the *timing/risk* of value delivery and the
  *unit* you charge on (per-seat vs per-sq-ft vs per-employee).
- **Customer factors** — DMU and acquisition process; capital vs operating budget preference;
  purchasing constraints.
- **Competition** — how competitors charge, and where you can differentiate.
- **Internal operations** — effect on sales friction, COCA, LTV, billing/support complexity, capital.

**Common mistakes:** defaulting to "how the industry does it"; choosing cost-plus and capping your
upside; treating pricing as the business model; "free" with no capture; ignoring the customer's budget
cycle (capex vs opex). See the `go-to-market` skill for archetype selection in depth.

---

## Step 16 — Set Your Pricing Framework

**Question:** Given the model, what's the right first-pass price? Pricing converts created value into
captured value.

**The central rule — value-based pricing.** Price as a **fraction of the quantified value the customer
receives** (Step 8) — **not** cost-plus, and **not** simply matching competitors. Cost-plus ignores
how much value you deliver; competition-based pricing anchors you to others' (possibly inferior)
economics. Heuristic: leave the customer with several times the value they pay (e.g. give 4–5× value
vs price) so the purchase is an obvious win.

**Other guidance:**
- **Segment your pricing** by customer type within the DMU/market.
- **Lighthouse / early-adopter customers** — be flexible with your first marquee references; they
  provide validation, testimonials, and word of mouth that lower future COCA. Give special *early*
  terms, structured so they don't permanently anchor your price.
- **Never set a high public price then discount publicly.** *"It is always easier to drop the price
  than to raise it."* Public discounting signals weakness and trains the market to wait.
- Pricing is a **first pass** that iterates as you test.

**Common mistakes:** cost-plus pricing; under-pricing breakthrough value; high list price then public
discounts; one-size-fits-all across distinct segments; permanently anchoring to a deep early discount.

---

## Step 17 — Calculate the Lifetime Value (LTV) of an Acquired Customer

**Question:** How much net profit, in today's dollars, does one acquired customer generate over their
lifetime? With COCA, it's the core viability test.

**Definition:** **LTV is the net present value of your profits from years 0–5** (year 0 = the year the
customer buys). It is built on **gross profit, not revenue**. Five drivers: **recurring revenue**
(biggest lever), **gross margin**, **retention**, **upsell/cross-sell**, and **cost of capital**.
COCA is *excluded* from LTV (compared separately in Step 19).

Full formula and two worked examples in `formulas.md`. Compute with `unit_economics.py`.

**Common mistakes:** computing off revenue not gross profit; ignoring the discount rate (or using a
loan rate instead of true cost of capital); assuming 100% retention; baking COCA into LTV.

---

## Step 18 — Map the Sales Process to Acquire a Customer *(2nd ed: "Design a Scalable Revenue Engine")*

**Question:** How will your sales/marketing engine reach, close, and service customers — and how will
that engine and its cost evolve as you scale? This is **your** side (vs Step 13's customer side), and
it feeds COCA.

**Tool — a sales roadmap across three horizons:**
- **Short term** — high-touch, founder-/direct-sales-led; demos and hand-holding. **High COCA.** Goal:
  land first customers and validate the model.
- **Medium term** — add channels/distribution partners; formalize customer success/retention; broaden
  marketing. COCA begins falling.
- **Long term** — self-serve / pull demand, partner networks, refined enterprise motion; word of mouth
  becomes a major driver. **Lowest COCA.**

The **GTM motion** (PLG/bottoms-up vs sales-led/top-down) is the concrete realization of this step and
the dominant driver of COCA — see the `go-to-market` skill.

**Common mistakes:** assuming the cheap, scalable long-term motion works on day one; not budgeting for
the expensive early high-touch phase; neglecting retention/customer-success spend.

---

## Step 19 — Calculate the Cost of Customer Acquisition (COCA)

**Question:** What does it truly cost to acquire one new customer — over time? The most commonly
**miscalculated** metric. Do not skim it.

**Correct method (top-down):**
> **COCA = (total sales & marketing spend in a period − retention/support costs) ÷ number of NEW
> customers acquired in that period.**

You **sum ALL sales & marketing spend** and divide by **net new customers** — never trace one customer
bottom-up. Include, at **market rates**: sales salaries/commissions/travel, **founders' and staff
time spent selling** (valued at market rate, not "free"), and all marketing. Exclude COGS and overhead
(finance, admin, R&D).

**Three horizons:** short (~first 90 days, vs named customers), medium (~first year), long (abstract,
from growth/market share). **COCA falls over time** — positive **word of mouth** is the biggest
long-term driver.

**The decisive rule:** **LTV ≥ 3 × COCA** (3:1 or better). At parity or below, the business doesn't
scale. Full method + worked example in `formulas.md`; compute with `unit_economics.py`.

**Common mistakes:** the "marketing ÷ customers" undercount; valuing founder/employee selling time at
zero; dividing by *total* not *new* customers; forgetting COCA falls over time; comparing COCA to
*revenue* instead of LTV.

## Sources
Toolbox [Step 15](https://www.d-eship.com/step15/),
[Step 19](https://www.d-eship.com/step19/),
[LTV spreadsheet](https://www.d-eship.com/articles/ltv-calculation-spreadsheet/) ·
O'Reilly book chapters [15](https://www.oreilly.com/library/view/disciplined-entrepreneurship-24/9781118692288/24_chap15.html)–[19](https://www.oreilly.com/library/view/disciplined-entrepreneurship-24/9781118692288/28_chap19.html).

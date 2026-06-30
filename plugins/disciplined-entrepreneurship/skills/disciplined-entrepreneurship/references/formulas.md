# DE Formulas — TAM, LTV, COCA (with worked numbers)

Exact methods for the three quantitative steps. The scripts `tam.py` and `unit_economics.py`
implement these — prefer them over hand math. Every number must carry a stated assumption or source.

---

## TAM — Total Addressable Market (Steps 4 and 14)

> **TAM = (number of end users that fit the End User Profile) × (annual revenue per end user)**

TAM is the **annual revenue at 100% market share** of the defined market, in dollars/year.

### Counting end users
- **Top-down:** start from a published industry figure, narrow by the profile's attributes. Fast, but
  unconvincing alone.
- **Bottom-up (preferred):** count actual potential customers from PMR. When you can't enumerate
  everyone, use **end-user density**:
  1. Pick a **countable unit** (e.g. # of firms in a NAICS code, # of employees, a population).
  2. Examine **three real instances** and **count noses** — the actual end users in each.
  3. Compute **density = end users ÷ unit size**.
  4. Apply the density across the total market.

### Revenue per end user
Your likely annual price per user, triangulated against (a) what they spend today on alternatives and
(b) the value you create (Step 8). Ground it in PMR, don't guess.

### Worked example — SensAble (bottom-up, by region)
| Region | End users | Annual rev/user | TAM |
|---|---|---|---|
| US | 1,500 | $9,000 | $13.5M |
| Europe | 1,000 | $9,000 | $9.0M |
| Asia | 1,000 | $6,333 | $6.3M |

Conservative beachhead TAM ≈ **$10–15M/year** (deliberately small — easy to dominate).

### Heuristic band (not a gate)
~**$20M–$100M/year** is "big enough to matter, small enough to dominate." Over ~$1B usually means the
segment is too broad (re-segment). Under ~$5M may be too small. SensAble's ~$10–15M shows the band is
a guideline, not a pass/fail test.

---

## LTV — Lifetime Value of an Acquired Customer (Step 17)

> **LTV = the net present value of your *profits* from years 0–5**, where year 0 is the year the
> customer is acquired. Built on **gross profit, not revenue**. COCA is excluded (compared in Step 19).

### Variables
- **One-time (up-front) revenue** and **recurring revenue** per period.
- **Gross margin %** = (Average Selling Price − Cost of Goods) ÷ ASP. LTV uses *profit* = revenue ×
  gross margin.
- **Retention / renewal rate** (e.g. 80%), applied **cumulatively** each year after year 0.
- **Product life** — typically **5 years** (years 0–5).
- **Cost of capital / discount rate** — *not* a loan rate, but the fraction of gross profit consumed to
  service capital. Aulet's typical ranges: ~**50% for venture-backed startups**, ~**12% with cheap
  debt**; most firms land in **35–70%**.

### Method
1. For each year *t* (0…5): **profit_t = recurring revenue × gross margin % × (retention rate)^t**
   (year 0 also includes any one-time/up-front gross profit; year 0 retention factor = 1).
2. Discount to present value: **PV_t = profit_t × (1 − cost_of_capital)^t** (year 0 undiscounted).
3. **LTV = Σ PV_t for t = 0…5.**

### Worked example A — canonical $20/month app
$20/month subscription, **90% gross margin**, **80% retention**, **50% cost of capital**, 5-year
horizon → **LTV ≈ $236**. Drop cost of capital to **12%** (cheap debt) → **LTV ≈ $440**. Sensitivity
across 85–95% margin and 75–85% retention → **~$198 (low) to ~$281 (high)**. LTV swings violently with
the discount rate and retention — always show the sensitivity range.

> These published figures come from the official d-eship.com spreadsheet and reflect its specific
> year-0/discounting conventions. The `unit_economics.py` script implements the same NPV-of-gross-profit
> *structure* but a from-scratch computation can differ by convention — treat the **LTV:COCA ratio and
> the sensitivity band** as the decision drivers, and the d-eship spreadsheet as authoritative for exact
> point figures.

### Worked example B — the "revenue illusion"
A customer projected to generate **$3,000 total revenue** nets an **LTV of only $580 (19.33%)** once
gross margin, retention, and discounting are applied. **Revenue grossly overstates customer value** —
always compute LTV on discounted gross profit.

---

## COCA — Cost of Customer Acquisition (Step 19)

> **COCA = (total sales & marketing spend in a period − retention/support costs) ÷ number of NEW
> customers acquired in that period.**

Sum **all** sales & marketing spend and divide by **net new** customers. Do **not** trace one
customer bottom-up — that is the classic undercount.

### What to include (at market rates)
- Sales salaries, commissions, benefits, taxes, travel.
- **Founders' and non-sales staff time spent selling**, valued at **market rate** (not "free" — using
  less than market rate badly understates COCA).
- All marketing: ads, content, PR, events, website, consultants.

### What to exclude
COGS/production, and overhead (finance, admin, R&D) — those aren't acquisition costs. Subtract the
portion of spend that retains/supports *existing* customers.

### Three horizons
- **Short** — ~first 90 days, computed against specific named customers.
- **Medium** — ~first year.
- **Long** — abstract, from growth rate and market share.

**COCA falls over time** as word of mouth, brand, references, and channel leverage compound, and the
early high-touch cost amortizes across more customers.

---

## The decisive test — LTV : COCA

> **A viable business needs LTV ≥ 3 × COCA (a 3:1 ratio or better).**

At ~1:1 you pay roughly what a customer is worth — no room to operate. The `unit_economics.py` script
computes LTV, COCA, and the ratio, and flags pass/fail against 3:1. A high *early* COCA isn't
automatically fatal if the long-term COCA forecast brings the ratio above 3:1.

## Sources
[LTV calculation spreadsheet (d-eship.com)](https://www.d-eship.com/articles/ltv-calculation-spreadsheet/) ·
[COCA — Step 19](https://www.d-eship.com/step19/) ·
[bottom-up market sizing](https://visible.vc/blog/bottom-up-market-sizing/).

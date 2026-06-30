# Theme 1 — Who Is Your Customer? (Steps 1–6)

Theme 1 starts wide and relentlessly narrows: from every conceivable market (Step 1) to **one
named real person** (Step 5) whose full experience you map (Step 6). Each step's output feeds the
next. Do all of it with Primary Market Research (see `primary-market-research.md`).

---

## Step 1 — Market Segmentation

**Question:** Who could *possibly* use this — across every conceivable industry? Deliberately do
**not** commit to a market yet. *"Problems that arise later are most often the result of the
entrepreneur not doing a rigorous job of market segmentation up front."* The goal is breadth: a wide
spectrum of opportunities, not a perfect answer.

**The 3-condition segment test** (reused in Steps 2 and 9). A group of customers is *one* segment
only if **all three** hold:
1. They buy **similar products**.
2. They have a **similar sales cycle** and expect value delivered in **similar ways**.
3. There is **word of mouth** between them — they reference and talk to each other.
If any condition fails, you have two or more segments; split them.

**Tool — the Market Segmentation Matrix.** Columns = candidate segments (each is an **end user +
application** pair). Rows = attributes filled in via PMR. Brainstorm wide, then narrow to **6–12**
opportunities before filling the deep grid. The 9 rows:
1. **End User** — the real person who *uses* it, never the buyer ("a school doesn't use a textbook;
   teachers do").
2. **Application / Task** — what they use it for.
3. **Benefits** — the value they get.
4. **Lead Customers** — named flagship accounts.
5. **Market Characteristics** — what shapes the segment.
6. **Partners / Players** — complementors needed for a whole product.
7. **Market Size** — rough number of end users.
8. **Competition** — who/what they use today.
9. **Complementary Assets Required** — what else must exist for adoption.

**How to do it:** brainstorm 6–12 industries focused on *end users, not payers*, including
longshots → don't seek commitment during ideation → narrow to 6–12 end-user+application
opportunities → do PMR for a few weeks (interview and, ideally, **watch end users work** — actions
beat words) → fill the top rows first (End User, Application, Benefits, Lead Customers).

**SensAble example:** one haptic technology fanned into ~10 segments — Industrial Design (end user
*Designer*, app *Sculpt*, lead *Disney/ILM*, size ~40,000), Automotive styling (*Stylist* at
*Toyota*), Surgical Simulation (*Surgeon* at *Brigham & Women's*), Geophysical (*Geophysicist* at
*BHP*), Computing for the blind, CAD/Prototyping (*Engineer* at *Boeing/Ford*), and more.

**Common mistakes:** falling in love with one market and skipping the brainstorm; segmenting by the
*organization* instead of the *end user*; leaning on **secondary** research; building the deep matrix
for all ideas instead of the top 6–12.

---

## Step 2 — Select a Beachhead Market

**Question:** Of those segments, which **one** do you attack first and dominate? (See the
single-beachhead doctrine in `overview.md`.)

**Tool — a criteria scorecard.** One row per candidate segment, scored by the **whole founding
team**. The original 6 criteria (the current toolbox splits them into 7–8 — support both):
1. Is the target customer **well-funded** (can they pay)?
2. Is the customer **readily accessible** to your sales force?
3. Does the customer have a **compelling reason to buy**?
4. Can you, **today and with partners, deliver a whole product** that fulfills that reason to buy?
5. Is there **entrenched competition** that could block you?
6. If you win this segment, can you **leverage it to enter adjacent segments** (the bowling pins)?
7. *(toolbox)* Is the market **consistent with the values, passions, and goals** of the team?
8. *(toolbox)* **How quickly** can you win it?

The chosen beachhead must itself pass the **3-condition segment test**; usually you **sub-segment**
the winner to make it tight enough to dominate.

**How to do it:** score the 6–12 candidates with ongoing PMR → **choose ONE and explicitly deselect
the rest** (better to pick a good market than suffer analysis paralysis) → further-segment the
winner → get **written team agreement** → park deselected segments as follow-on pins.

**Sizing guideline (heuristic, not a gate):** a beachhead TAM is typically **~$20M–$100M/year** —
big enough to matter, small enough to dominate. Over $1B usually means you defined it too broadly.
(Aulet's own SensAble beachhead was a deliberately low ~$10–15M.)

**Common mistakes:** picking more than one market "to hedge"; analysis paralysis; choosing a market
too big to dominate or with entrenched competition; ignoring whole-product deliverability; picking a
market the team doesn't care about.

---

## Step 3 — Build an End User Profile

**Question:** Within the beachhead, who is the **specific, real human end user**? Build the business
around the customer you serve, not the product you want to sell. This is the prerequisite for sizing
(Step 4) and the persona (Step 5).

**Distinguish the roles now** (full DMU is Step 12). The **End User** uses the product; the
**Champion** wants it bought; the **Primary Economic Buyer** controls the money; **Influencers /
Veto / Purchasing** sway or block. In B2C one person may hold all roles; in B2B they diverge. Step 3
profiles the **End User** — flag where the same person plays multiple roles.

**Tool — the End User Profile**, fields in order:
1. **Demographics** — gender, age, income, geography, education, work experience.
2. **Psychographics** — what motivates them, what they fear, what gets them promoted, their values,
   goals, heroes, frustrations.
3. **Proxy products** — what they buy *today* (real behavior) and their selection criteria.
4. **Watering holes** — where they congregate and exchange information (forums, LinkedIn/Reddit
   groups, conferences, trade publications).
5. **A day in the life** — a narrative of a typical day in their shoes.
6. **Biggest fears & motivators** — a **prioritized list (allocate 100 points across the top ~5)** of
   general *life* fears/motivators, **not** product-specific ones.

> **Profile vs. Persona:** the Profile (Step 3) describes the *typical/aggregate* user; the Persona
> (Step 5) is *one specific named real person*. Build the profile from many observations first.

**How to do it:** expand PMR within the beachhead (interview + observe) → fill every field with real
data, no stereotyping → build the day-in-the-life from composites → prioritize fears/motivators →
if no team member fits the demographic, recruit a target end user → end with a **narrow,
homogeneous** description.

**Common mistakes:** demographics with no psychographics; guessing/stereotyping; conflating the end
user with the buyer/champion; a profile too broad to be homogeneous; making fears/motivators
product-specific.

---

## Step 4 — Calculate the TAM for the Beachhead Market

**Question:** How big is the beachhead? **TAM = the annual revenue (dollars/year) you'd earn at 100%
market share of this market.** (Full math + worked numbers in `formulas.md`; the `tam.py` script
computes it with sensitivity.)

**Formula:**
> **TAM = (number of end users that fit the End User Profile) × (annual revenue per end user)**

**Estimate the number of end users two ways and reconcile:**
- **Top-down** — start from published reports, narrow by your profile's attributes. Easy, but
  unconvincing alone and misses nuance.
- **Bottom-up (preferred)** — count *actual* potential customers from PMR. More accurate, more work.
  Use **end-user density** when you can't enumerate everyone: pick a countable unit (e.g., #
  employees, a population), examine **three real instances** and **"count noses"** (actual end users
  in each), compute a density ratio, then apply it across the whole market.

**Estimate annual revenue per end user** from PMR: your likely price, triangulated against what they
spend today on alternatives and the value you create (links to Step 8).

**SensAble worked example:** countable unit = toy-company industrial designers; counted via Hasbro
conversations + the Industrial Design Society of America; across three regions —
US: 1,500 × $9,000 = $13.5M; Europe: 1,000 × $9,000 = $9M; Asia: 1,000 × $6,333 = $6.3M →
conservative beachhead TAM ≈ **$10–15M/year** (Aulet calls this deliberately low-end).

**Common mistakes:** top-down only; guessing revenue-per-user; defining the segment so broadly the
TAM balloons past $1B (you skipped segmentation); treating the $20–100M band as pass/fail.

---

## Step 5 — Profile the Persona for the Beachhead Market

**Question:** Who, **specifically**, is your primary customer? The profile is a composite — too
abstract to drive crisp decisions. Step 5 forces the team to pick **one real, named, photographed
human** who best exemplifies the End User Profile. *"A great persona makes nearly any decision
easier — what to do, and what not to do."*

**Tool — the Persona fact sheet** (a real person + photo): real **name** (the team literally asks
"what would [name] think?"), photo, specific demographics, psychographics, rational/emotional/social
motivations, a day in the life, where they get information, watering holes, proxy products,
aspirations, fears — and the single most important output:

> **The PRIORITIZED LIST OF PURCHASING CRITERIA** (ranked #1, #2, #3 …).

Every later step targets the **#1 criterion first — "don't be subtle."** The persona's top two
priorities become the axes of the Step 11 competitive chart; the #1 priority becomes the unit of the
Step 8 value gap and the headline of the Step 7 brochure.

**How to do it:** from the profile + a PMR candidate list, **select the one best exemplar** (a real
person, not a composite) → interview/observe to fill every field → **rank the purchasing criteria
from PMR, not opinion** → make the persona visual and omnipresent (on the wall, in the product). For
multi-sided markets, one persona per side, kept consistent.

**SensAble example:** a real lead industrial/toy designer who best embodied the profile (the
official teaching article uses "Sean, 45, from Boulder, CO").

**Common mistakes:** a fictional "average user" instead of one real human; **unranked** criteria or
criteria ranked by opinion; too little detail / nobody references it; multiple personas in a
single-sided market.

---

## Step 6 — Full Life Cycle Use Case

**Question:** How does the persona **discover, evaluate, acquire, install, use, pay for, support, and
expand/advocate** the product across its whole lifespan — and where does it fit into their existing
workflow and value chain? Not just "how they use it." This surfaces friction (procurement
gatekeepers, install pain, support burden) **before** you design anything.

**Tool — a visual map of 10 ordered stages**, each documenting who is involved, when, where, and how:
1. How they **determine they have a need** and the **trigger** to act (the most important stage).
2. How they **find out** about your product.
3. How they **analyze/evaluate** it (who else weighs in).
4. How they **acquire** it (procurement, approvals, budget, gatekeepers).
5. How they **install/onboard** it.
6. How they **use** it (usually the most complex part).
7. How they **determine the value** gained.
8. How they **pay** for it (mechanism, who holds budget).
9. How they **receive support**.
10. How they **buy more and/or spread the word** (re-purchase, expansion, referral).

Also sketch two workflows: **how they solve the problem today (as-is)** and **how they'll work with
your product (to-be)**.

**How to do it:** sketch the as-is workflow → walk the persona through all 10 stages capturing
who/when/where/how from PMR → sketch the to-be workflow → render it **visually** → flag adoption
barriers before designing.

**SensAble example:** designer realizes hand-sculpting clay is too slow → discovers FreeForm →
evaluates vs. CAD → runs capital-equipment procurement → installs at the workstation → sculpts
organic 3D models → measures value as "~50% faster to market" → pays via capital purchase → support
→ expands seats and evangelizes in the design community.

**Common mistakes:** guessing the stages instead of PMR; documenting only the "use" stage; ignoring
gatekeepers/multiple deciders in B2B; underestimating install/workflow-disruption barriers; prose
instead of a visual.

---

## How Theme 1 hands off to Theme 2

Theme 1 produces: a validated **beachhead**, an **End User Profile**, a **named Persona with ranked
purchasing criteria**, a **TAM**, and a **full life cycle use case**. Theme 2 now asks what you build
for that person — and every answer is measured against the persona's **#1 priority**.

## Sources
Disciplined Entrepreneurship Toolbox steps [1](https://www.d-eship.com/step1/)–[6](https://www.d-eship.com/step6/) ·
[MIT OCW 15.390 lecture slides](https://ocw.mit.edu/courses/15-390-new-enterprises-spring-2013/) ·
[MIT Sloan: 6 questions](https://mitsloan.mit.edu/ideas-made-to-matter/disciplined-entrepreneurship-6-questions-startup-success) ·
[blas.com notes](https://blas.com/disciplined-entrepreneurship/). Exact worksheet/figure layouts are
in the book (2nd ed.) and the *Disciplined Entrepreneurship Workbook*.

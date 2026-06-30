---
name: market-research
description: >-
  This skill should be used to research a market for a startup/product idea — both primary
  (talking to and observing real customers) and secondary (desk research and data) — and to size a
  market. Use it whenever the user wants to "research this market", "do market research", "talk to
  customers", "write an interview guide / customer-discovery questions", "find people to interview",
  "is there demand for X", "size the market", "estimate TAM / market size", "find market data", or
  "validate demand". It applies the Disciplined Entrepreneurship inquiry-not-advocacy method, knows
  where real market data lives, and dispatches the market-researcher and customer-discovery-analyst
  agents. Prefer it over generic web search whenever the goal is understanding a market or customer.
---

# Market Research — Primary, Secondary, and Sizing

Research a market the disciplined way: **primary research leads, secondary supports, sizing is
bottoms-up.** Customer truth comes from direct contact; data fills in context and scale.

## The order of operations

1. **Primary first (the fuel).** Talk to and observe real potential customers in **inquiry, not
   advocacy** mode — learn, never pitch. This is irreplaceable and drives every DE step. Full method,
   question bank, anti-patterns, and bias controls:
   `../disciplined-entrepreneurship/references/primary-market-research.md`.
2. **Secondary to frame and find.** Use desk research to understand industry structure, spot trends,
   and *find people to interview* — not to substitute for talking to them. Sources and how to mine
   them: `references/data-sources.md`.
3. **Size bottoms-up.** TAM = (# end users) × (annual revenue per end user). Build it from defensible
   units; reconcile a bottom-up and a top-down estimate. Math: the DE
   `references/formulas.md`; compute with `${CLAUDE_PLUGIN_ROOT}/scripts/tam.py`.

## Running primary research

- **Write the interview guide** from the persona's open questions — past behavior and specifics, never
  hypotheticals or pitches. Use the question bank in the PMR reference.
- **Recruit** from the persona's watering holes and from secondary research (named companies/roles).
- **Run conversations**: listen ~80%, ask "walk me through the last time…", capture verbatim quotes,
  watch for the difference between what people say and do.
- **Synthesize** after ~10–15 conversations per segment: recurring pains, the job-to-be-done, current
  workarounds + their cost, the buying process, and surprises that broke your assumptions.
- **Log every conversation** in the venture's `interviews/` folder (one note per interview).

For volume work, dispatch the **`customer-discovery-analyst`** agent to generate a tailored interview
guide or to synthesize a batch of interview notes into patterns and an end-user profile.

## Running secondary research

- Triangulate: confirm any number from 2–3 independent sources.
- Capture provenance for every fact (URL, publisher, date) in the venture's `research/` folder.
- Mine review sites (G2/Capterra/TrustRadius), forums (Reddit/niche), and filings (SEC EDGAR) for
  unfiltered customer voice and competitor intel. Use demand signals (Google Trends, keyword volume)
  to gauge interest.
- For a fast, parallel sweep of a market, dispatch the **`market-researcher`** agent; it returns a
  market landscape, segments, trends, and sizing inputs with sources.

## Sizing when data is sparse

- **Bottoms-up** (preferred): # potential customers (firm counts by industry code × size band, role
  counts, association membership) × annual revenue per customer. Tends to under-count.
- **Top-down**: a published total × a realistic capture %. Fast, tends to over-count — context only.
- **Proxy/analog**: borrow a comparable's ARPU or a competitor's revenue/customer count and scale.
- **Reconcile**: strong estimates land a bottom-up and top-down within ~20% of each other. Label every
  assumption. Run `tam.py` with `--sensitivity` to show the range.

## Output

Write findings into the venture workspace: interviews → `interviews/`, sources → `research/`, the
synthesized profile/persona and TAM → `01-who-is-your-customer.md`, and update `dashboard.md`. Keep
every claim traceable to a conversation or a cited source.

## Related
`disciplined-entrepreneurship` (the framework spine; Steps 1–6 are the customer/market steps) ·
`competitive-analysis` (competitor landscape) · agents: `market-researcher`,
`customer-discovery-analyst`, `tam-estimator`.

## Reference
- `references/data-sources.md` — where real market & competitive data lives, and how to mine it.

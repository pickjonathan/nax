# Market & Competitive Data Sources

Where real data lives, and how to mine it. Always capture provenance (URL, publisher, date) in the
venture's `research/` folder, and triangulate across 2–3 sources.

## Secondary data / market sizing

**Free government & public (backbone of bottoms-up sizing):**
- **U.S. Census Bureau** — *County Business Patterns* (annual establishment counts, employment,
  payroll by NAICS code, geography, employment-size band — ~1,000 industries); *Economic Census*
  (5-yearly industry revenue/sales); a Business Counts API for programmatic pulls.
- **Bureau of Labor Statistics (BLS)** — employment, wages, occupation counts (size markets by
  workforce, e.g. # of nurses, accountants).
- **Bureau of Economic Analysis (BEA)** — GDP-by-industry, consumer spending (PCE) for macro
  denominators.
- **SEC EDGAR** — free 10-K / S-1 / 10-Q filings: public-comp revenue, segments, customer counts,
  ARPU, and often the company's own stated TAM (S-1s). Earnings-call transcripts add color.
- **data.gov, Eurostat (NACE), World Bank, OECD** — international.

**Paid industry research** (cite free previews / press-release quotes / 10-K restatements to avoid the
cost): Gartner (IT buyer advisory, Magic Quadrant), Forrester (the Wave), IDC (tech sizing & share),
IBISWorld (industry reports), Statista (fast stat lookup), Euromonitor/Nielsen (consumer/retail),
McKinsey/BCG/Bain (free trend PDFs).

**Startup / funding / company data:** Crunchbase (funding/profiles; generous free tier), PitchBook
(analyst-verified financials; enterprise-priced), CB Insights (market maps), Dealroom (strong European
coverage, useful free layer).

## Competitive intelligence

- **Software review sites (free to read):** G2, Capterra, TrustRadius, Gartner Peer Insights. Mine for
  pain points, pricing mentions, switching reasons, and feature gaps — and for the customer's own
  language.
- **Demand/interest signals:** Google Trends (relative direction, free), Google Keyword Planner
  (volume ranges, free with Ads), Ahrefs/SEMrush (absolute volume, paid), Exploding Topics (emerging
  trends).
- **Voice-of-customer (free, unfiltered):** Reddit, Quora, niche forums, X/LinkedIn, Amazon and
  app-store reviews — the best raw source for jobs-to-be-done and complaints about incumbents.
- **Filings/financials:** SEC EDGAR 10-K/S-1, annual reports, earnings-call transcripts.

## Sizing methods when data is sparse

- **Bottoms-up (investor-preferred, DE-native):** # potential customers (Census firm counts by NAICS ×
  size band; LinkedIn company/role counts; association membership) × annual revenue per customer
  (price × usage). Tends to under-count (forgotten channels/upsell).
- **Top-down:** analyst total × realistic capture %. Fast; tends to over-count adjacent revenue you'll
  never win. Use for context only.
- **Proxy / analog:** borrow a comparable adjacent market, a public comp's ARPU, or a competitor's
  revenue/customer count (10-Ks/Crunchbase) and scale to your segment.
- **Triangulation:** estimate the same number 2–3 independent ways and reconcile; aim for bottom-up and
  top-down within ~20%.
- **Fermi estimation:** decompose into order-of-magnitude factors as a sanity check before trusting any
  single figure.

## A note on AI/web research

When using web search to gather any of the above, prefer primary sources (filings, official stats,
the company's own pricing page) over aggregator blog posts, and always record the source and date so
the claim can be re-checked. Remember: none of this replaces talking to real customers.

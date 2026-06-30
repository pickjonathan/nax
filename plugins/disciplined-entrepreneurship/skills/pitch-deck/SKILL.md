---
name: pitch-deck
description: >-
  This skill should be used to build an investor pitch deck for a startup. Use it whenever the user
  wants to "build a pitch deck", "make an investor deck", "create a fundraising / seed deck", "draft
  my pitch", "review my deck", "what slides do I need", "pitch to investors", or "turn my plan into a
  deck". It assembles the deck from the validated Disciplined Entrepreneurship workspace, follows the
  canonical investor slide sequence and design rules, applies DocSend evidence about what investors
  actually read, and dispatches the pitch-deck-architect agent. Use it even when the user just says
  "I'm raising money — help me tell the story."
---

# Pitch Deck — Turn Validated Work into an Investor Story

A great deck is not invented — it is *assembled from evidence*. The 24-step workspace is the source:
the deck is the validated venture, compressed and sequenced for an investor's attention. If a slide
isn't backed by the workspace, that's a gap to close, not prose to fabricate.

## Before drafting

- **Pull from the workspace.** Read `00-summary.md`, `dashboard.md`, and the theme docs. Map each
  slide to its DE source (full map in `references/slide-by-slide.md`).
- **Flag missing evidence.** If TAM, unit economics, or traction are still `_TBD_`, say so — a deck
  built on holes fails due diligence. Recommend the steps that fill them.

## The canonical sequence (~10–13 core slides)

1. Company purpose (one declarative sentence) · 2. Problem · 3. Solution · 4. Why now · 5. Market size ·
6. Product · 7. Business model · 8. Traction · 9. Competition · 10. Go-to-market · 11. Team ·
12. Financials · 13. The ask / use of funds. (What each must contain, and which DE step feeds it, is in
`references/slide-by-slide.md`.)

## Design rules (so it gets read)

- **Kawasaki 10/20/30** — aim for ~10 slides, a 20-minute telling, nothing under 30pt.
- **YC: legibility, simplicity, obviousness** — one idea per slide, big high-contrast text, the key
  point at the top; a stranger should "get" each slide in seconds.
- **Lead with what's read first.** Investors front-load attention — opening with Company Purpose →
  Problem → Solution → Why-now/Market in order correlates with raising more. Don't bury the lede.

## What investors actually do (DocSend evidence)

- They spend ~**3–4 minutes** on a first read, ~**20 seconds per slide**.
- Most-viewed slides: **Team** and **Financials** (the fundamental bet and its credibility), then
  **Traction**. Make these airtight.
- Successful seed decks run ~**10–20 slides**, ~50 words/slide. Cold decks convert to meetings at a
  few %, warm intros far higher — so the deck must stand alone *and* you should seek warm paths.

## Fatal mistakes

No clear ask · top-down-only TAM ("1% of a huge market") with no bottoms-up build · text-heavy /
illegible · no traction or evidence · a weak team slide (it's the most-viewed) · "we have no
competitors" · hockey-stick financials with no stated assumptions · too many slides · no "why now".

## Workflow

Dispatch the **`pitch-deck-architect`** agent to draft a full deck from the workspace; it returns
slide-by-slide copy plus a list of evidence gaps. Write the outline into the venture's
`pitch-deck.md`. Keep claims traceable to the workspace; convert quantified DE outputs (TAM, LTV,
COCA, traction) into the market, business-model, and financials slides.

## Related
`disciplined-entrepreneurship` (the source of every slide) · `go-to-market` (unit economics for the
model/financials slides) · `competitive-analysis` (the competition slide) · agent:
`pitch-deck-architect`.

## Reference
- `references/slide-by-slide.md` — per-slide contents, the DE-step→slide map, attention data, and the
  Sequoia/YC/Kawasaki templates.

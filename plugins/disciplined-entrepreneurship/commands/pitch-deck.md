---
description: Build an investor pitch deck from the validated workspace
argument-hint: [venture-slug]
---

Use the **pitch-deck** skill to assemble an investor deck for venture **$ARGUMENTS**.

1. Read the workspace (`00-summary.md`, `dashboard.md`, theme docs); note what is evidenced vs `_TBD_`.
2. Dispatch the **`pitch-deck-architect`** agent to draft the canonical ~10–13 slide sequence, mapping
   each slide to its DE source (TAM → market; Step 8 → value; Step 11 → competition; Steps 15–19 →
   model/financials; Steps 9/23 → traction).
3. **Flag every evidence gap** and the step that closes it — never fabricate traction or numbers. Make
   Team, Financials, and Traction airtight (most-scrutinized); keep slides legible and front-load the
   story. Write the outline into the venture's `pitch-deck.md`.

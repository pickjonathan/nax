# nax — Disciplined Entrepreneurship for Claude Code

> A Claude Code **plugin marketplace** that turns a raw tech idea into a **falsifiable,
> customer-grounded, investor-ready** business — using Bill Aulet's **Disciplined
> Entrepreneurship** (24 steps / 6 themes) plus market-research, competitive-analysis,
> go-to-market, unit-economics, and pitch-deck tooling.

It hosts one plugin, **`disciplined-entrepreneurship`**, that ships **5 skills, 7 agents, 12
commands**, helper scripts, and a per-idea **venture workspace** — everything a founder needs to
validate an idea without fooling themselves.

- [Install](#install)
- [Install into your project](#install-into-your-project-spec-kit-style)
- [What you can do](#what-you-can-do)
- [The framework](#the-framework-24-steps-6-themes)
- [The lifecycle](#the-lifecycle-spec-kit-style)
- [Usage](#usage)
- [What's inside](#whats-inside)
- [The venture workspace](#the-venture-workspace)
- [Repository layout](#repository-layout)
- [Local development & testing](#local-development--testing)
- [Publishing](#publishing)
- [Attribution & caveats](#attribution--caveats)

## Install

In Claude Code:

```
# Add this marketplace (your GitHub owner/repo, or a local path while testing)
/plugin marketplace add pickjonathan/nax

# Install the plugin
/plugin install disciplined-entrepreneurship@nax
```

Then start validating — ventures are created in your **current project** under `./ventures/`:

```
/validate-idea My Idea Name
```

## Install into your project (Spec-Kit-style)

Prefer the files **version-controlled and editable inside your own repo** (like
[Spec Kit](https://github.com/github/spec-kit))? Use the `nax` CLI instead of the plugin — it asks a
few questions and vendors the toolkit straight into your project's `.claude/`:

```bash
uvx --from git+https://github.com/pickjonathan/nax nax init
```

It prompts for the target directory, what to install, helper scripts, and an optional first venture,
then writes `.claude/{commands,agents,skills}` plus `.claude/de/{scripts,templates}`. Non-interactive:

```bash
uvx --from git+https://github.com/pickjonathan/nax nax init . --here --force --yes
```

It also targets **Cursor** and **Codex** — `nax init` asks which, or pass `--ai`:
`--ai claude` → `.claude/{commands,agents,skills}` · `--ai cursor` → `.cursor/{commands,skills,agents}` ·
`--ai codex` → `.agents/skills/` (commands & agents become Codex skills) + `AGENTS.md`. Each also gets
`<root>/de/{scripts,templates}`.

**Two distribution models — pick one per project:**
- **Plugin** (above) — shared across all your projects, updated via `/plugin update`; nothing is
  copied into your repo.
- **Vendored** (`nax init`) — files live in *this* project's `.claude/`, committed and editable, no
  plugin required. Don't use both in the same project, or commands will duplicate.

All flags are in [`nax_cli/README.md`](nax_cli/README.md).

## What you can do

- **Validate an idea end-to-end** against the 24 steps, with the workspace tracking your progress.
- **Research a market** the disciplined way — primary (inquiry-not-advocacy customer interviews)
  and secondary (where the real data lives) — and **size it bottoms-up**.
- **Analyze competitors** and find a defensible position on the customer's own priorities.
- **Choose a business model & pricing**, and prove the **unit economics** (LTV ≥ 3 × COCA).
- **Stress-test your assumptions** with an adversarial red-teamer before you commit or pitch.
- **Build an investor pitch deck** assembled from the validated work.

## The framework: 24 steps, 6 themes

| Theme (the question) | Steps |
|---|---|
| **1 — Who is your customer?** | 1 Market Segmentation · 2 Beachhead Market · 3 End User Profile · 4 TAM · 5 Persona · 6 Full Life Cycle Use Case |
| **2 — What can you do for your customer?** | 7 High-Level Product Spec · 8 Quantify Value Proposition · 9 Next 10 Customers · 10 Define Your Core · 11 Competitive Position |
| **3 — How does your customer acquire it?** | 12 Decision-Making Unit (DMU) · 13 Acquisition Process |
| **4 — How do you make money?** | 14 Follow-on TAM · 15 Business Model · 16 Pricing · 17 LTV · 18 Sales Process · 19 COCA |
| **5 — How do you design & build it?** | 20 Key Assumptions · 21 Test Assumptions · 22 MVBP · 23 "Dogs Eat the Dog Food" |
| **6 — How do you scale?** | 24 Product Plan |

Five principles run through every step: **one beachhead, dominated · primary research over opinion ·
quantify bottoms-up · capture value (not just create it) · evidence beats eloquence.**

## The lifecycle (Spec-Kit-style)

Like [Spec Kit](https://github.com/github/spec-kit)'s `specify → clarify → plan → tasks → implement`,
this toolkit gives you a **phase-gated lifecycle** so you always know the next move. Run **`/de-next`**
for the current phase + next command, **`/validate-idea`** to auto-advance, or **`/venture-status`**
for the full board.

| Phase | Command | DE steps | Spec Kit |
|---|---|---|---|
| Charter | `/de-charter` | 0 — idea, mission, team values | constitution |
| Specify | `/de-specify` | 1–6 — who is your customer | specify |
| Clarify *(gate)* | `/de-clarify` | validate beachhead via ~10 interviews | clarify |
| Plan | `/de-plan` | 7–19 — value, position, model, economics | plan |
| Tasks | `/de-tasks` | 20–21 — assumptions + experiments | tasks |
| Analyze *(gate)* | `/de-analyze` | red-team before building | analyze |
| Implement | `/de-implement` | 22–24 — MVBP → traction → product plan | implement |

Two **gates** enforce the discipline that makes DE work: you can't *plan* before you've *talked to
customers* (clarify), and you can't *build* before you've *de-risked* (analyze). It's a cycle — loop
back whenever an interview breaks an earlier assumption. The engine (`scripts/status.py`) derives the
phase from your dashboard and tells you exactly what to do next.

## Usage

Drive it with slash commands, or just talk to Claude naturally ("help me validate my idea for…",
"who are my competitors", "is this viable", "build my pitch deck") — the skills trigger themselves.

| Command | Does |
|---|---|
| `/validate-idea [idea]` | Scaffold + run/continue the full 24-step validation |
| `/de-step [n] [venture]` | Work one specific step |
| `/venture-status [venture]` | 24-step progress dashboard + key metrics |
| `/market-research [topic]` | Primary + secondary market research |
| `/size-market [venture]` | Bottoms-up TAM (Steps 4 & 14) |
| `/personas [venture]` | End-user profile + persona (Steps 3 & 5) |
| `/competition [venture]` | Competitive landscape + positioning (Steps 10–11) |
| `/business-model [venture]` | Business model + pricing (Steps 15–16) |
| `/unit-economics [venture]` | LTV, COCA, LTV:COCA (Steps 17 & 19) |
| `/gtm [venture]` | DMU, sales process, GTM motion (Steps 12–13, 18) |
| `/pitch-deck [venture]` | Assemble an investor deck |
| `/red-team [venture]` | Adversarially stress-test assumptions |

**A typical flow:** `/validate-idea "AI scheduling for dental clinics"` → talk to customers and log
them → `/personas` → `/size-market` → `/competition` → `/business-model` → `/unit-economics` →
`/red-team` → `/pitch-deck`. Loop back whenever an interview breaks an earlier assumption.

## What's inside

**Skills** (`skills/`, auto-trigger on natural language)
- **`disciplined-entrepreneurship`** — the spine: orchestrates the 24 steps; 11 references
  (per-theme guides, exact TAM/LTV/COCA formulas, the PMR method, pitfalls, glossary).
- **`market-research`**, **`competitive-analysis`**, **`go-to-market`**, **`pitch-deck`** — focused
  skills, each with its own reference docs.

**Agents** (`agents/`, autonomous workers Claude dispatches)
- `market-researcher` · `competitor-analyst` · `customer-discovery-analyst` · `tam-estimator` ·
  `business-model-architect` · `pitch-deck-architect` · `assumption-red-teamer`.

**Commands** (`commands/`) — the 12 slash commands above.

**Scripts** (`scripts/`, invoked via `${CLAUDE_PLUGIN_ROOT}`)
- `new_venture.sh` (scaffold) · `tam.py` · `unit_economics.py` · `status.py`.

## The venture workspace

`/validate-idea` (via `new_venture.sh`) creates `./ventures/<slug>/` in **your** project — a living
workbook, not a one-time form:

```
ventures/<slug>/
├── 00-summary.md            # the living one-pager
├── dashboard.md             # 24-step progress + key metrics
├── 01..06-*.md              # a guided worksheet per theme
├── assumptions.md           # ranked assumptions + experiments
├── unit-economics.md        # LTV / COCA workings
├── pitch-deck.md            # investor-deck outline
├── research/                # secondary sources (with provenance)
├── interviews/              # primary research — one note per conversation
└── competitors/             # competitor profiles + matrix
```

Every claim should trace to a customer conversation, a cited source, or a labelled assumption.

## Repository layout

```
nax/
├── .claude-plugin/marketplace.json            # marketplace manifest
├── README.md · CLAUDE.md
└── plugins/disciplined-entrepreneurship/
    ├── .claude-plugin/plugin.json             # plugin manifest
    ├── commands/ · agents/ · skills/          # auto-discovered components
    ├── scripts/                               # helper scripts (${CLAUDE_PLUGIN_ROOT})
    ├── templates/venture/                     # per-venture workspace template
    └── README.md
```

Follows the Claude Code plugin spec: components auto-discover from `commands/`, `agents/`, `skills/`;
intra-plugin paths use `${CLAUDE_PLUGIN_ROOT}`; runtime venture data is written into the user's
project, never into the installed plugin. See [`CLAUDE.md`](CLAUDE.md) for contributor conventions and
the [plugin README](plugins/disciplined-entrepreneurship/README.md) for the full toolkit.

## Local development & testing

```bash
# Validate the manifests
python3 -m json.tool .claude-plugin/marketplace.json
python3 -m json.tool plugins/disciplined-entrepreneurship/.claude-plugin/plugin.json

# Exercise the scripts
python3 plugins/disciplined-entrepreneurship/scripts/tam.py --users 1500 --revenue 9000
python3 plugins/disciplined-entrepreneurship/scripts/unit_economics.py --monthly 20 \
  --gross-margin 0.9 --retention 0.8 --cost-of-capital 0.5 --coca 60

# Test the plugin locally without publishing:
#   /plugin marketplace add /absolute/path/to/nax
#   /plugin install disciplined-entrepreneurship@nax
```

## Publishing

1. Push to GitHub (done if you cloned this from a remote).
2. Optionally set `repository`, `homepage`, `author`, and `license` in the two manifests.
3. Share `/plugin marketplace add pickjonathan/nax` — anyone can then
   `/plugin install disciplined-entrepreneurship@nax`.

## Attribution & caveats

Implements the framework from **Bill Aulet, *Disciplined Entrepreneurship: 24 Steps to a Successful
Startup*** (and the companion *Startup Tactics* by Paul Cheek & Bill Aulet), MIT Martin Trust Center.
This is an **independent** learning/execution tool, **not affiliated with or endorsed by** the
authors — buy the book and use the official [DE Toolbox](https://www.d-eship.com/) for the canonical
worksheets.

- **Step numbering** follows the 2nd edition (MVBP = 22, "dogs eat the dog food" = 23, Product Plan =
  24; LTV = 17, COCA = 19). Step 14 (follow-on TAM) is placed in Theme 4 (it sits at the 3/4 seam).
- **Formula caveat:** `unit_economics.py` implements the DE NPV-of-gross-profit *structure*; the
  official d-eship LTV spreadsheet is authoritative for exact published figures. Treat the
  **LTV:COCA ratio and sensitivity** as the decision drivers, not the point estimate.
- Sources are cited at the bottom of each reference doc.

## License

No license is set yet — add one (e.g. MIT) before inviting external contributions.

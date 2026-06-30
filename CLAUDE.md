# CLAUDE.md — Operating Manual for the `nax` repo

This file orients any Claude Code session working **on** this repository. (It is not shipped to
end users of the plugin — it is for contributors maintaining and extending the marketplace.)

## What this repo is

A **Claude Code plugin marketplace**. It hosts a single plugin, **`disciplined-entrepreneurship`** —
a founder's idea-validation toolkit implementing Bill Aulet's Disciplined Entrepreneurship (DE)
framework (24 steps across 6 themes) plus market-research, competitive-analysis, go-to-market,
unit-economics, and pitch-deck tooling.

Two audiences, two surfaces:
- **End users** install the plugin and run it in *their own* projects to validate startup ideas.
- **Contributors** (you, here) maintain the marketplace + plugin in *this* repo.

## Repository layout

```
nax/
├── .claude-plugin/marketplace.json            # marketplace manifest (lists the plugin)
├── README.md                                  # repo front page (install + overview)
├── CLAUDE.md                                   # this file
└── plugins/disciplined-entrepreneurship/
    ├── .claude-plugin/plugin.json             # plugin manifest
    ├── README.md                              # plugin documentation
    ├── commands/   (12 .md)                   # slash-command entry points
    ├── agents/     (7 .md)                     # autonomous subagents
    ├── skills/     (5 dirs)                    # methodology; the DE skill holds 11 references/
    ├── scripts/    (4)                         # tam.py · unit_economics.py · status.py · new_venture.sh
    └── templates/venture/                      # per-venture workspace template (copied into user projects)
```

## How the pieces relate

- **Commands** are thin entry points (`/validate-idea`, `/size-market`, …) that trigger skills and
  dispatch agents.
- **Skills** hold the methodology. `disciplined-entrepreneurship` is the spine (24-step orchestration
  + references); `market-research`, `competitive-analysis`, `go-to-market`, `pitch-deck` are focused.
- **Agents** do context-heavy autonomous work (research, sizing, modelling, red-teaming) and return
  artifacts.
- **Scripts** are deterministic helpers invoked via `${CLAUDE_PLUGIN_ROOT}/scripts/…`.
- **The venture template** is copied (by `new_venture.sh`) into the **user's** project at
  `./ventures/<slug>/`. Venture data is never stored inside the plugin.

## The lifecycle

The opinionated, Spec-Kit-style path through the 24 steps: **charter → specify → clarify → plan →
tasks → analyze → implement**, exposed as the `de-*` commands and driven by the engine
`scripts/status.py`.

- The **engine** derives the current phase from the venture's `dashboard.md` step checkboxes
  (step 0 = charter) and the `interviews/` count, enforces two **gates** — *clarify before plan*
  (interview target ~10) and *analyze before implement* — and prints the next command
  (`status.py <venture> --next`).
- **Single source of truth is the dashboard.** Don't add a parallel state file. If you change the
  phase↔step mapping, update *all* of: `status.py` (`PHASES`), the skill's
  `references/lifecycle.md`, the venture template's `lifecycle.md`, and the README phase tables.
- The phase grouping intentionally differs from the 6-theme grouping (Plan spans Themes 2–4) — that's
  by design for a tighter command surface.
- Lifecycle phase commands stay **thin**: they delegate to the focused tool commands, skills, and
  agents, then advance the dashboard.

## Distribution models & the `nax` CLI

The toolkit ships two ways:
1. **Plugin** (`plugins/disciplined-entrepreneurship/`, installed via `/plugin`). Components use
   `${CLAUDE_PLUGIN_ROOT}` for script paths. **This is the canonical source of the components.**
2. **Vendored** via the `nax` CLI (`nax_cli/`): `uvx --from git+…/nax nax init` copies the components
   into a project's `.claude/` (+ `.claude/de/{scripts,templates}`) for people who want them in their
   own repo — no plugin needed.

**Invariant to preserve:** components are authored *once*, for the plugin, using
`${CLAUDE_PLUGIN_ROOT}/…`. The CLI's single transform rewrites `${CLAUDE_PLUGIN_ROOT}/` →
`.claude/de/` in vendored `.md`/`.sh`/`.py` files. Therefore: keep using `${CLAUDE_PLUGIN_ROOT}` in
plugin components (never hardcode `.claude/de/`), and **do not duplicate component files into
`nax_cli/`** — they are bundled into the wheel at build time via hatchling `force-include`
(`pyproject.toml`), and the CLI falls back to `plugins/disciplined-entrepreneurship/` when run from a
clone.

## Conventions you MUST follow when editing

1. **Plugin spec.** Components auto-discover from `commands/`, `agents/`, `skills/` at the *plugin
   root*. Never nest them under `.claude-plugin/`. The manifest lives at `.claude-plugin/plugin.json`.
2. **Paths.**
   - Scripts run via `${CLAUDE_PLUGIN_ROOT}/scripts/<file>` in commands and skills.
   - Cross-skill doc references use relative siblings: `../disciplined-entrepreneurship/references/<file>.md`.
   - Within a skill, reference its own files relatively: `references/<file>.md`.
   - **Never** hardcode absolute paths or legacy `.claude/...` paths.
3. **The venture template ships into the user's project**, where `${CLAUDE_PLUGIN_ROOT}` does NOT
   resolve. Its docs must point at slash commands (`/venture-status`, `/unit-economics`,
   `/size-market`), not raw script paths.
4. **`new_venture.sh` stays location-independent**: it finds its template relative to itself
   (`BASH_SOURCE`) and writes ventures into `$PWD/ventures` (or `$VENTURES_DIR`). Don't reintroduce
   repo-root assumptions.
5. **Skill `SKILL.md`** — frontmatter `name` + `description` (third-person, with concrete trigger
   phrases). Body in imperative voice, lean (~1.5–2k words); push detail into `references/`.
6. **Agent files** — frontmatter `name`, `description` (prose triggers + a pointer to a "When to
   invoke" body section), `model: inherit`, distinct `color`, least-privilege `tools`. System prompt
   in second person.
7. **Command files** — written as instructions *FOR Claude*, not messages to the user. Frontmatter
   `description` + `argument-hint`; use `$ARGUMENTS` / `$1`. Add `allowed-tools` only when running
   bash/scripts.

## Adding or changing components

- **New skill:** `plugins/disciplined-entrepreneurship/skills/<name>/SKILL.md` (+ optional
  `references/`). Cross-link to DE references with `../disciplined-entrepreneurship/references/…`.
- **New agent:** `plugins/disciplined-entrepreneurship/agents/<name>.md`.
- **New command:** `plugins/disciplined-entrepreneurship/commands/<name>.md`.
- **New script:** `plugins/disciplined-entrepreneurship/scripts/<name>`; invoke as
  `${CLAUDE_PLUGIN_ROOT}/scripts/<name>`; make it executable.
- After any change, keep `README.md` and the plugin `README.md` component lists accurate.

## Testing

```bash
# Validate manifests
python3 -m json.tool .claude-plugin/marketplace.json
python3 -m json.tool plugins/disciplined-entrepreneurship/.claude-plugin/plugin.json

# Exercise the scripts
python3 plugins/disciplined-entrepreneurship/scripts/tam.py --users 1500 --revenue 9000
python3 plugins/disciplined-entrepreneurship/scripts/unit_economics.py --monthly 20 \
  --gross-margin 0.9 --retention 0.8 --cost-of-capital 0.5 --coca 60

# Scaffold test (run from a throwaway dir so ventures land there, not in this repo)
( cd "$(mktemp -d)" && bash /abs/path/to/plugins/disciplined-entrepreneurship/scripts/new_venture.sh "Test Idea" )

# Install locally to test discovery:  /plugin marketplace add <abs path>  then
#                                      /plugin install disciplined-entrepreneurship@nax
```

## Key framework facts (get these right)

- **24 steps / 6 themes.** Theme 1 Who is your customer? (1–6) · 2 What can you do for them? (7–11) ·
  3 How do they acquire it? (12–13) · 4 How do you make money? (14–19) · 5 How do you build it?
  (20–23) · 6 How do you scale? (24).
- **Step numbering** = 2nd edition: MVBP = 22, "dogs eat the dog food" = 23, Product Plan = 24;
  LTV = 17, COCA = 19. Step 14 (follow-on TAM) is placed in Theme 4 here (it sits at the 3/4 seam).
- **TAM** = (# end users) × (annual revenue per end user); bottoms-up; a focused beachhead is ~$20–100M.
- **LTV** = NPV of gross profit over years 0–5; **COCA** = all sales & marketing ÷ new customers;
  the viability rule is **LTV ≥ 3 × COCA**.
- **Formula caveat:** `unit_economics.py` implements the DE NPV-of-gross-profit *structure*; the
  official d-eship.com spreadsheet is authoritative for exact published figures (e.g. the $20/mo →
  ~$236 example). Treat the **ratio and sensitivity** as the decision drivers, not the point estimate.
- **Primary market research** is inquiry-not-advocacy; behavior over opinion (The Mom Test).
- Each `references/*.md` cites its sources at the bottom — preserve and extend those when editing.

## Attribution

Implements the framework from **Bill Aulet, *Disciplined Entrepreneurship*** (MIT Martin Trust
Center). This is an independent tool, not affiliated with or endorsed by the authors.

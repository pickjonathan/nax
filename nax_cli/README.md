# nax-cli

The Spec-Kit-style installer for the Disciplined Entrepreneurship toolkit. It asks a few questions
and **vendors the commands, agents, skills, scripts, and venture template into a project** for your
assistant — **Claude Code** (`.claude/`), **Cursor** (`.cursor/`), or **Codex** (`.agents/skills/` +
`AGENTS.md`) — the second distribution model alongside the Claude Code plugin.

## Run it

```bash
# Faithful to Spec Kit (no install needed):
uvx --from git+https://github.com/pickjonathan/nax nax init

# Or install the CLI, then use it anywhere:
uv tool install --from git+https://github.com/pickjonathan/nax nax-cli
nax init

# Or from a clone, with plain Python (no uv):
python3 -m nax_cli init
```

`nax init [PATH]` prompts for: target dir, AI assistant (Claude Code), what to install
(full / no-agents), whether to include helper scripts, overwrite policy, `.gitignore`, and an optional
first venture. Every prompt has a flag for non-interactive use, e.g.:

```bash
nax init . --here --ai claude --components full --force --yes
```

`nax update` re-installs with overwrite (never touches `ventures/`).

## How it works

- **Source of truth:** the component tree at `plugins/disciplined-entrepreneurship/`. It is bundled
  into the wheel as `nax_cli/payload/` via hatchling `force-include` (see `pyproject.toml`) — so there
  is **no duplicate copy** in the repo. Clone runs fall back to reading `plugins/...` directly.
- **The transform:** `${CLAUDE_PLUGIN_ROOT}/` is rewritten to the target's vendored path
  (`.claude/de/`, `.cursor/de/`, or `.agents/de/`) — that variable only exists for installed plugins.
  Cursor commands have their YAML frontmatter stripped; Codex (no project-local commands) converts
  commands **and** agents into `SKILL.md` files under `.agents/skills/` and writes an `AGENTS.md`
  overview. `new_venture.sh` finds its template via `BASH_SOURCE`, so it works from
  `<root>/de/scripts/`.
- **Non-destructive:** files merge into the user's existing `.claude/`; nothing is deleted, and
  existing files are skipped unless `--force`.

See the top-level `CLAUDE.md` for the invariants to preserve when editing components.

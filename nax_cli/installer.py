"""Vendor the Disciplined Entrepreneurship toolkit into a project for a chosen AI assistant.

Targets (`--ai`):
  claude  -> .claude/{commands,agents,skills} + .claude/de/{scripts,templates}
  cursor  -> .cursor/{commands,agents,skills} + .cursor/de/{scripts,templates}
  codex   -> .agents/skills/<all-as-skills> + AGENTS.md + .agents/de/{scripts,templates}

Components are authored once for the Claude Code plugin using `${CLAUDE_PLUGIN_ROOT}/…`; each target
rewrites that token to its own vendored path. Codex has no project-local commands, so commands and
agents are converted into the Codex/agentskills SKILL.md format. Nothing is ever deleted — files
merge into the project and existing ones are skipped unless `force`.
"""
from __future__ import annotations

import json
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

PLUGIN_ROOT_TOKEN = "${CLAUDE_PLUGIN_ROOT}/"
TEXT_SUFFIXES = (".md", ".sh", ".py")


# --------------------------------------------------------------------------- payload
def payload_root() -> Path:
    """Locate the component source: bundled wheel payload, else repo-relative (clone runs)."""
    try:
        from importlib.resources import files

        bundled = Path(str(files("nax_cli"))) / "payload"
        if (bundled / "commands").is_dir():
            return bundled
    except Exception:
        pass
    src = Path(__file__).resolve().parent.parent / "plugins" / "disciplined-entrepreneurship"
    if (src / "commands").is_dir():
        return src
    raise SystemExit(
        "error: could not locate the DE component payload (neither bundled nor repo-relative). "
        "Reinstall the CLI or run it from a clone of the repository."
    )


# --------------------------------------------------------------------------- text helpers
def _transform(text: str, prefix: str) -> str:
    return text.replace(PLUGIN_ROOT_TOKEN, prefix)


def _parse_frontmatter(fm: str) -> dict:
    """Minimal YAML frontmatter reader: `key: value` and folded block scalars (`>-`, `|`). Enough
    to recover `name`/`description` — avoids a PyYAML dependency so the CLI stays stdlib-only."""
    meta: dict = {}
    lines = fm.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#") or line.startswith((" ", "\t")):
            i += 1
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip()
            if val in (">", ">-", "|", "|-"):
                block, i = [], i + 1
                while i < len(lines) and (lines[i].startswith(("  ", "\t")) or not lines[i].strip()):
                    if lines[i].strip():
                        block.append(lines[i].strip())
                    i += 1
                meta[key] = " ".join(block)
                continue
            meta[key] = val.strip().strip('"').strip("'")
        i += 1
    return meta


def _split_frontmatter(text: str):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return _parse_frontmatter(text[4:end]), text[end + 5:]
    return {}, text


# --------------------------------------------------------------------------- fs helpers
def _emit(dst: Path, text: str, installed: list, force: bool) -> int:
    if dst.exists() and not force:
        return 0
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")
    installed.append(str(dst))
    return 1


def _copy_dir(src: Path, dst: Path, prefix: str, installed: list, force: bool) -> int:
    """Copy a tree, rewriting the plugin-root token in text files. Skips existing unless force."""
    n = 0
    if not src.is_dir():
        return 0
    for root, _dirs, files in os.walk(src):
        rel = Path(root).relative_to(src)
        for name in files:
            s, d = Path(root) / name, dst / rel / name
            if d.exists() and not force:
                continue
            d.parent.mkdir(parents=True, exist_ok=True)
            if s.suffix in TEXT_SUFFIXES:
                d.write_text(_transform(s.read_text(encoding="utf-8"), prefix), encoding="utf-8")
            else:
                shutil.copy2(s, d)
            installed.append(str(d))
            n += 1
    return n


def _make_executable(path: Path) -> None:
    if not path.is_dir():
        return
    for f in path.rglob("*"):
        if f.is_file() and f.suffix in (".sh", ".py"):
            f.chmod(f.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def ensure_gitignore(target: Path) -> bool:
    gi = target / ".gitignore"
    line = "/ventures/"
    existing = gi.read_text(encoding="utf-8") if gi.exists() else ""
    if line in existing.splitlines():
        return False
    with gi.open("a", encoding="utf-8") as fh:
        if existing and not existing.endswith("\n"):
            fh.write("\n")
        fh.write("\n# Disciplined Entrepreneurship venture workspaces (your working data)\n")
        fh.write(line + "\n")
    return True


def plugin_installed() -> bool:
    try:
        base = Path.home() / ".claude" / "plugins"
        if not base.is_dir():
            return False
        for manifest in base.rglob("plugin.json"):
            try:
                if json.loads(manifest.read_text(encoding="utf-8")).get("name") == \
                        "disciplined-entrepreneurship":
                    return True
            except Exception:
                continue
    except Exception:
        pass
    return False


# --------------------------------------------------------------------------- per-target copy
def _copy_claude_like(payload, root_dir, prefix, components, force, installed):
    """Shared by claude and cursor: native commands/skills/agents dirs."""
    counts = {}
    counts["commands"] = _copy_dir(payload / "commands", root_dir / "commands", prefix, installed, force)
    counts["skills"] = sum(1 for d in (payload / "skills").iterdir() if d.is_dir())
    _copy_dir(payload / "skills", root_dir / "skills", prefix, installed, force)
    if components != "no-agents":
        counts["agents"] = _copy_dir(payload / "agents", root_dir / "agents", prefix, installed, force)
    return counts


def _copy_claude(payload, target, components, with_scripts, force, installed):
    prefix = ".claude/de/"
    counts = _copy_claude_like(payload, target / ".claude", prefix, components, force, installed)
    return {"root": ".claude", "de_dir": target / ".claude" / "de", "prefix": prefix,
            "counts": counts, "invoke": "/", "extra": []}


def _copy_cursor(payload, target, components, with_scripts, force, installed):
    prefix = ".cursor/de/"
    cur = target / ".cursor"
    counts = {}
    # Cursor commands are plain markdown (no frontmatter); strip the YAML block.
    n = 0
    for f in sorted((payload / "commands").glob("*.md")):
        _, body = _split_frontmatter(f.read_text(encoding="utf-8"))
        n += _emit(cur / "commands" / f.name, _transform(body.lstrip("\n"), prefix), installed, force)
    counts["commands"] = n
    counts["skills"] = sum(1 for d in (payload / "skills").iterdir() if d.is_dir())
    _copy_dir(payload / "skills", cur / "skills", prefix, installed, force)
    if components != "no-agents":
        counts["agents"] = _copy_dir(payload / "agents", cur / "agents", prefix, installed, force)
    return {"root": ".cursor", "de_dir": cur / "de", "prefix": prefix,
            "counts": counts, "invoke": "/", "extra": []}


def _to_skill(name, description, body, prefix, skills_root, installed, force) -> int:
    """Write a SKILL.md (Codex/agentskills format) unless that skill folder already exists."""
    dst = skills_root / name / "SKILL.md"
    if dst.parent.exists() and not force:
        return 0
    desc = description or name
    text = (f"---\nname: {name}\ndescription: {json.dumps(desc, ensure_ascii=False)}\n---\n\n"
            f"{_transform(body.lstrip(chr(10)), prefix)}")
    return _emit(dst, text, installed, force)


def _copy_codex(payload, target, components, with_scripts, force, installed):
    prefix = ".agents/de/"
    skills_root = target / ".agents" / "skills"
    counts = {"skills": 0, "commands": 0, "agents": 0}
    # 1) Real skills first; they own their names (a same-named command never overwrites a skill).
    real_names = set()
    for d in sorted((payload / "skills").iterdir()):
        if d.is_dir():
            _copy_dir(d, skills_root / d.name, prefix, installed, force)
            counts["skills"] += 1
            real_names.add(d.name)
    # 2) Commands -> skills (skip names already taken by a real skill, e.g. market-research, pitch-deck).
    for f in sorted((payload / "commands").glob("*.md")):
        if f.stem in real_names:
            continue
        meta, body = _split_frontmatter(f.read_text(encoding="utf-8"))
        counts["commands"] += _to_skill(f.stem, meta.get("description", ""), body, prefix,
                                        skills_root, installed, force)
    # 3) Agents -> skills.
    if components != "no-agents":
        for f in sorted((payload / "agents").glob("*.md")):
            meta, body = _split_frontmatter(f.read_text(encoding="utf-8"))
            counts["agents"] += _to_skill(meta.get("name", f.stem), meta.get("description", ""), body,
                                          prefix, skills_root, installed, force)
    extra = []
    if _write_agents_md(target, force, installed):
        extra.append("wrote AGENTS.md")
    return {"root": ".agents", "de_dir": target / ".agents" / "de", "prefix": prefix,
            "counts": counts, "invoke": "$", "extra": extra}


AGENTS_MD_BLOCK = """<!-- nax:disciplined-entrepreneurship:start -->
# Disciplined Entrepreneurship toolkit

This project includes the Disciplined Entrepreneurship (DE) founder-validation toolkit, installed as
Codex **skills** under `.agents/skills/` — invoke one with `$<name>` (e.g. `$de-next`), or just
describe your idea and the skills auto-trigger by description. Helper scripts live in
`.agents/de/scripts/`; the per-venture workbook template in `.agents/de/templates/`. Your validation
work for each idea lives in `./ventures/<slug>/`.

**Lifecycle:** `$de-charter` -> `$de-next` (it tells you the next step) -> `$de-specify` ->
`$de-clarify` -> `$de-plan` -> `$de-tasks` -> `$de-analyze` -> `$de-implement`. Scaffold from the
shell with `bash .agents/de/scripts/new_venture.sh "My Idea"`.

**Principles (Bill Aulet):** one beachhead dominated; primary research over opinion (inquiry, not
advocacy); quantify bottoms-up (TAM, LTV, COCA); capture value, don't just create it; evidence beats
eloquence ("the dogs must eat the dog food").

*(Generated by nax-cli; deep methodology lives in each skill's SKILL.md and references/.)*
<!-- nax:disciplined-entrepreneurship:end -->"""


def _write_agents_md(target: Path, force: bool, installed: list) -> bool:
    path = target / "AGENTS.md"
    start, end = "<!-- nax:disciplined-entrepreneurship:start -->", \
        "<!-- nax:disciplined-entrepreneurship:end -->"
    if not path.exists():
        path.write_text(AGENTS_MD_BLOCK + "\n", encoding="utf-8")
        installed.append(str(path))
        return True
    text = path.read_text(encoding="utf-8")
    if start in text and end in text:
        if not force:
            return False
        pre, _, rest = text.partition(start)
        _, _, post = rest.partition(end)
        path.write_text(pre + AGENTS_MD_BLOCK + post, encoding="utf-8")
        return True
    sep = "" if text.endswith("\n") else "\n"
    path.write_text(text + sep + "\n" + AGENTS_MD_BLOCK + "\n", encoding="utf-8")
    return True


_TARGETS = {"claude": _copy_claude, "cursor": _copy_cursor, "codex": _copy_codex}


# --------------------------------------------------------------------------- entry point
def install(*, ai: str = "claude", target: Path, components: str = "full", with_scripts: bool = True,
            force: bool = False, scaffold: str | None = None, gitignore: bool = True,
            version: str = "0") -> dict:
    if ai not in _TARGETS:
        raise SystemExit(f"error: unknown --ai target {ai!r} (choose: {', '.join(_TARGETS)}).")
    payload = payload_root()
    installed: list = []
    res = _TARGETS[ai](payload, target, components, with_scripts, force, installed)

    de_dir = res["de_dir"]
    if with_scripts:
        res["counts"]["scripts"] = _copy_dir(payload / "scripts", de_dir / "scripts",
                                             res["prefix"], installed, force)
        _copy_dir(payload / "templates", de_dir / "templates", res["prefix"], installed, force)
        _make_executable(de_dir / "scripts")

    de_dir.mkdir(parents=True, exist_ok=True)
    (de_dir / ".nax.json").write_text(json.dumps({
        "name": "disciplined-entrepreneurship", "version": version, "ai": ai,
        "components": components, "scripts": with_scripts, "installed": installed,
        "generator": "nax-cli",
    }, indent=2) + "\n", encoding="utf-8")

    gi_added = ensure_gitignore(target) if gitignore else False

    scaffolded = None
    if scaffold and with_scripts:
        script = de_dir / "scripts" / "new_venture.sh"
        try:
            subprocess.run(["bash", str(script), scaffold], cwd=str(target), check=True)
            scaffolded = scaffold
        except Exception as exc:  # noqa: BLE001 - scaffolding is best-effort
            print(f"  (could not scaffold venture: {exc})", file=sys.stderr)

    return {
        "target": str(target), "ai": ai, "root": res["root"], "counts": res["counts"],
        "scripts": with_scripts, "gitignore_added": gi_added, "scaffolded": scaffolded,
        "invoke": res["invoke"], "extra": res["extra"],
    }

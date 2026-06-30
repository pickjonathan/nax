"""Vendor the Disciplined Entrepreneurship toolkit into a project's `.claude/` folder.

Distribution model #2 (alongside the Claude Code plugin): copy the components into a project's
`.claude/` so they are version-controlled and editable in that repo. Because `${CLAUDE_PLUGIN_ROOT}`
only exists for installed plugins, vendored `.md` files have it rewritten to a project-local path.
"""
from __future__ import annotations

import json
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

# In the plugin, scripts are referenced as ${CLAUDE_PLUGIN_ROOT}/scripts/...; vendored, they live
# under .claude/de/. Rewriting this token is the single transform that makes the vendored copy work.
PLUGIN_ROOT_TOKEN = "${CLAUDE_PLUGIN_ROOT}/"
VENDOR_PREFIX = ".claude/de/"


def payload_root() -> Path:
    """Locate the component source: the bundled wheel payload, else the repo source (clone runs)."""
    try:
        from importlib.resources import files

        bundled = Path(str(files("nax_cli"))) / "payload"
        if (bundled / "commands").is_dir():
            return bundled
    except Exception:
        pass
    repo = Path(__file__).resolve().parent.parent
    src = repo / "plugins" / "disciplined-entrepreneurship"
    if (src / "commands").is_dir():
        return src
    raise SystemExit(
        "error: could not locate the DE component payload (neither bundled in the package nor "
        "repo-relative). Reinstall the CLI or run it from a clone of the repository."
    )


def _write_file(src: Path, dst: Path, transform: bool) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if transform and src.suffix in (".md", ".sh", ".py"):
        text = src.read_text(encoding="utf-8").replace(PLUGIN_ROOT_TOKEN, VENDOR_PREFIX)
        dst.write_text(text, encoding="utf-8")
    else:
        shutil.copy2(src, dst)


def _copy_tree(src: Path, dst: Path, *, transform: bool, force: bool, installed: list) -> int:
    """Recursively copy src→dst, merging into any existing files. Skips existing unless `force`.

    Never deletes anything — vendored files merge into the user's existing `.claude/`.
    """
    count = 0
    for root, _dirs, fnames in os.walk(src):
        rel = Path(root).relative_to(src)
        for name in fnames:
            d = dst / rel / name
            if d.exists() and not force:
                continue
            _write_file(Path(root) / name, d, transform)
            installed.append(str(d))
            count += 1
    return count


def _make_executable(path: Path) -> None:
    if not path.is_dir():
        return
    for f in path.rglob("*"):
        if f.is_file() and f.suffix in (".sh", ".py"):
            f.chmod(f.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def ensure_gitignore(target: Path) -> bool:
    """Append `/ventures/` to the project .gitignore if absent. Returns True if it added the line."""
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
    """Best-effort: is the disciplined-entrepreneurship plugin installed for this user?"""
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


def install(*, target: Path, components: str = "full", with_scripts: bool = True,
            force: bool = False, scaffold: str | None = None, gitignore: bool = True,
            version: str = "0") -> dict:
    """Vendor the toolkit into `target/.claude/`. Returns a summary dict."""
    payload = payload_root()
    claude = target / ".claude"
    de = claude / "de"

    comp_dirs = ["commands", "skills"]
    if components != "no-agents":
        comp_dirs.append("agents")

    installed: list = []
    counts: dict = {}
    for comp in comp_dirs:
        n_files = _copy_tree(payload / comp, claude / comp,
                             transform=True, force=force, installed=installed)
        # commands/agents are one .md each; for skills, report the number of skill directories.
        counts[comp] = (sum(1 for d in (payload / comp).iterdir() if d.is_dir())
                        if comp == "skills" else n_files)
    if with_scripts:
        counts["scripts"] = _copy_tree(payload / "scripts", de / "scripts",
                                       transform=True, force=force, installed=installed)
        _copy_tree(payload / "templates", de / "templates",
                   transform=True, force=force, installed=installed)
        _make_executable(de / "scripts")

    de.mkdir(parents=True, exist_ok=True)
    (de / ".nax.json").write_text(json.dumps({
        "name": "disciplined-entrepreneurship",
        "version": version,
        "components": components,
        "scripts": with_scripts,
        "installed": installed,
        "generator": "nax-cli",
    }, indent=2) + "\n", encoding="utf-8")

    gi_added = ensure_gitignore(target) if gitignore else False

    scaffolded = None
    if scaffold and with_scripts:
        script = de / "scripts" / "new_venture.sh"
        try:
            subprocess.run(["bash", str(script), scaffold], cwd=str(target), check=True)
            scaffolded = scaffold
        except Exception as exc:  # noqa: BLE001 - scaffolding is best-effort
            print(f"  (could not scaffold venture: {exc})", file=sys.stderr)

    return {
        "target": str(target),
        "counts": counts,
        "components": components,
        "scripts": with_scripts,
        "gitignore_added": gi_added,
        "scaffolded": scaffolded,
    }

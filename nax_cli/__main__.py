"""nax — Spec-Kit-style installer for the Disciplined Entrepreneurship toolkit.

    uvx --from git+https://github.com/pickjonathan/nax nax init
    python3 -m nax_cli init
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .installer import install, plugin_installed


def _tty() -> bool:
    try:
        return sys.stdin.isatty()
    except Exception:
        return False


def ask(prompt: str, default: str) -> str:
    if not _tty():
        return default
    return input(f"{prompt} [{default}]: ").strip() or default


def ask_yesno(prompt: str, default: bool = True) -> bool:
    if not _tty():
        return default
    ans = input(f"{prompt} [{'Y/n' if default else 'y/N'}]: ").strip().lower()
    return default if not ans else ans.startswith("y")


def ask_choice(prompt: str, choices: list, default: str) -> str:
    if not _tty():
        return default
    print(prompt)
    for i, c in enumerate(choices, 1):
        print(f"  {i}. {c}{'  (default)' if c == default else ''}")
    ans = input(f"Choice [1-{len(choices)}, default {choices.index(default) + 1}]: ").strip()
    if not ans:
        return default
    try:
        return choices[int(ans) - 1]
    except Exception:
        return default


def run_init(args) -> None:
    interactive = _tty() and not args.yes

    # 1) Target directory
    if args.path:
        target = Path(args.path).expanduser().resolve()
    elif args.here or not interactive:
        target = Path.cwd()
    else:
        target = Path(ask("Target project directory", str(Path.cwd()))).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)

    # 2) AI assistant
    ai = args.ai or (ask_choice("AI assistant to install for:", ["claude", "cursor", "codex"], "claude")
                     if interactive else "claude")

    # 3) Components
    components = args.components or (
        ask_choice("What to install:", ["full", "no-agents"], "full") if interactive else "full")

    # 4) Helper scripts
    with_scripts = args.scripts if args.scripts is not None else (
        ask_yesno("Include helper scripts (tam / unit-economics / status / scaffolder)?", True)
        if interactive else True)

    # 5) Overwrite policy if already installed
    force = args.force
    if (target / ".claude" / "de" / ".nax.json").exists() and not force and interactive:
        choice = ask_choice("DE files already present here. On conflict:",
                            ["skip", "overwrite", "abort"], "skip")
        if choice == "abort":
            sys.exit("aborted.")
        force = choice == "overwrite"

    # 6) .gitignore
    gitignore = args.gitignore if args.gitignore is not None else (
        ask_yesno("Add `ventures/` to .gitignore?", True) if interactive else True)

    # 7) Scaffold a first venture
    scaffold = args.venture
    if scaffold is None and interactive and with_scripts and ask_yesno("Scaffold a first venture now?", False):
        scaffold = ask("  Venture / idea name", "My Idea")

    result = install(ai=ai, target=target, components=components, with_scripts=with_scripts,
                     force=force, scaffold=scaffold, gitignore=gitignore, version=__version__)
    _print_summary(result)


def _print_summary(r: dict) -> None:
    c, root, inv = r["counts"], r["root"], r["invoke"]
    assistant = {"claude": "Claude Code", "cursor": "Cursor", "codex": "Codex CLI"}.get(r["ai"], r["ai"])
    if r["ai"] == "codex":
        parts = [f"skills {c.get('skills', 0)}", f"commands→skills {c.get('commands', 0)}"]
        if c.get("agents"):
            parts.append(f"agents→skills {c['agents']}")
    else:
        parts = [f"commands {c.get('commands', 0)}"]
        if c.get("agents"):
            parts.append(f"agents {c['agents']}")
        parts.append(f"skills {c.get('skills', 0)}")
    if r["scripts"]:
        parts.append(f"scripts {c.get('scripts', 0)}")
    print()
    print(f"✓ Installed the Disciplined Entrepreneurship toolkit for {assistant} into {r['target']}/{root}")
    print("  " + " · ".join(parts) + (" · venture template ✓" if r["scripts"] else ""))
    for note in r.get("extra", []):
        print(f"  · {note}")
    if r["gitignore_added"]:
        print("  · added /ventures/ to .gitignore")
    if r["scaffolded"]:
        print(f"  · scaffolded a venture under ventures/ ({r['scaffolded']})")
    print("\nNext steps:")
    print(f"  1. Open {assistant} in this project.")
    print(f'  2. {inv}de-charter "My Idea"   then   {inv}de-next')
    if r["scripts"]:
        print(f'     (or scaffold from the shell)  bash {root}/de/scripts/new_venture.sh "My Idea"')
    print(f"\nTip: {inv}de-next shows the current phase and the next command.")
    if r["ai"] == "claude" and plugin_installed():
        print("\n⚠  You also have the 'disciplined-entrepreneurship' PLUGIN installed. To avoid")
        print("   duplicate commands, disable it via /plugin — or skip this vendored copy. Use one model.")


def main(argv=None) -> None:
    p = argparse.ArgumentParser(
        prog="nax",
        description="Install the Disciplined Entrepreneurship toolkit into a project's .claude/ "
                    "(Spec-Kit-style). Asks a few questions, then vendors commands/agents/skills.")
    p.add_argument("--version", action="version", version=f"nax {__version__}")
    sub = p.add_subparsers(dest="cmd")
    for name, helptext in (("init", "install the toolkit"), ("update", "re-install (overwrite) the toolkit")):
        sp = sub.add_parser(name, help=helptext)
        sp.add_argument("path", nargs="?", default=None, help="target project dir (default: current dir)")
        sp.add_argument("--here", action="store_true", help="install into the current directory")
        sp.add_argument("--ai", choices=["claude", "cursor", "codex"], default=None,
                        help="assistant target: claude | cursor | codex")
        sp.add_argument("--components", choices=["full", "no-agents"], default=None,
                        help="full = commands+agents+skills; no-agents = commands+skills")
        sp.add_argument("--scripts", dest="scripts", action="store_true", default=None,
                        help="include helper scripts (default)")
        sp.add_argument("--no-scripts", dest="scripts", action="store_false", help="skip helper scripts")
        sp.add_argument("--force", action="store_true", help="overwrite existing DE files")
        sp.add_argument("--venture", default=None, help="scaffold a venture with this name")
        sp.add_argument("--gitignore", dest="gitignore", action="store_true", default=None,
                        help="add /ventures/ to .gitignore (default)")
        sp.add_argument("--no-gitignore", dest="gitignore", action="store_false")
        sp.add_argument("-y", "--yes", action="store_true", help="accept defaults (non-interactive)")
    args = p.parse_args(argv)
    if args.cmd in ("init", "update"):
        if args.cmd == "update":
            args.force = True
        run_init(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()

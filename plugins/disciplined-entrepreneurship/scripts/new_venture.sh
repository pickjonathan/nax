#!/usr/bin/env bash
# new_venture.sh — scaffold a per-venture Disciplined Entrepreneurship workspace.
#
# Usage:
#   bash "${CLAUDE_PLUGIN_ROOT}/scripts/new_venture.sh" "My Idea Name" [target-base-dir]
#
# Creates <base>/<slug>/ from the plugin's bundled venture template. <base> defaults to
# ./ventures in the current working directory (your project), or $VENTURES_DIR if set.
# The script finds its own template relative to itself, so it works wherever the plugin is installed.
set -euo pipefail

if [ "$#" -lt 1 ] || [ -z "${1:-}" ]; then
  echo "usage: new_venture.sh \"<Venture name>\" [target-base-dir]" >&2
  exit 1
fi
NAME="$1"

# The venture template ships inside the plugin, at ../templates/venture relative to this script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="$(cd "${SCRIPT_DIR}/.." && pwd)/templates/venture"
if [ ! -d "${TEMPLATE}" ]; then
  echo "error: venture template not found at ${TEMPLATE}" >&2
  exit 1
fi

# Ventures live in the user's project (cwd), never inside the installed plugin.
BASE="${2:-${VENTURES_DIR:-$(pwd)/ventures}}"

# Slugify: lowercase, non-alphanumeric -> hyphen, collapse/trim hyphens.
SLUG="$(printf '%s' "${NAME}" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"
if [ -z "${SLUG}" ]; then
  echo "error: could not derive a slug from \"${NAME}\"" >&2
  exit 1
fi

DEST="${BASE}/${SLUG}"
if [ -e "${DEST}" ]; then
  echo "error: ${DEST} already exists. Pick another name or open the existing venture." >&2
  exit 1
fi

mkdir -p "${BASE}"
cp -R "${TEMPLATE}" "${DEST}"

TODAY="$(date +%Y-%m-%d)"
# Fill placeholders. Values pass through the environment so special characters can't break the regex.
export V_NAME="${NAME}" V_SLUG="${SLUG}" V_DATE="${TODAY}"
find "${DEST}" -type f -print0 | while IFS= read -r -d '' f; do
  perl -pi -e 's/\Q{{VENTURE_NAME}}\E/$ENV{V_NAME}/g; s/\Q{{SLUG}}\E/$ENV{V_SLUG}/g; s/\Q{{DATE}}\E/$ENV{V_DATE}/g' "$f"
done

echo "Created venture workspace: ${DEST}"
echo
echo "Next steps:"
echo "  1. Open ${DEST}/00-summary.md and write the one-line idea."
echo "  2. Start Theme 1 (Step 1, Market Segmentation): 01-who-is-your-customer.md"
echo "  3. Get into customer conversations early — log them in interviews/."
echo "  4. Track progress with the /venture-status command."

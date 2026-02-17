#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/ShalomObongo/codex-conductor.git"
REF="main"
DEST="${CODEX_HOME:-$HOME/.codex}/skills"

SKILLS=(
  "conductor-setup"
  "conductor-new-track"
  "conductor-implement"
  "conductor-status"
  "conductor-review"
  "conductor-revert"
)

usage() {
  cat <<'EOF'
Update Codex Conductor skills from GitHub.

Usage:
  scripts/update_conductor_skills.sh [--ref <git-ref>] [--repo-url <url>] [--dest <skills-dir>] [--dry-run]

Options:
  --ref <git-ref>      Git branch or tag to install from (default: main)
  --repo-url <url>     Git repository URL (default: https://github.com/ShalomObongo/codex-conductor.git)
  --dest <skills-dir>  Destination skills directory (default: $CODEX_HOME/skills or ~/.codex/skills)
  --dry-run            Print actions without modifying destination
  -h, --help           Show help

Examples:
  scripts/update_conductor_skills.sh
  scripts/update_conductor_skills.sh --ref v1.0.0
  scripts/update_conductor_skills.sh --dest "$HOME/.codex/skills"
EOF
}

DRY_RUN="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --ref)
      REF="${2:-}"
      shift 2
      ;;
    --repo-url)
      REPO_URL="${2:-}"
      shift 2
      ;;
    --dest)
      DEST="${2:-}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 2
      ;;
  esac
done

if [[ -z "$REF" || -z "$REPO_URL" || -z "$DEST" ]]; then
  echo "Invalid empty argument value." >&2
  usage
  exit 2
fi

tmp_dir="$(mktemp -d)"
cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

echo "Source repo: $REPO_URL"
echo "Source ref:  $REF"
echo "Target dir:  $DEST"

echo "Cloning repository..."
git clone --depth 1 --branch "$REF" "$REPO_URL" "$tmp_dir/repo" >/dev/null 2>&1

src_root="$tmp_dir/repo/skills/.curated"
if [[ ! -d "$src_root" ]]; then
  echo "Missing source curated skills directory: $src_root" >&2
  exit 1
fi

if [[ "$DRY_RUN" == "true" ]]; then
  echo "[dry-run] Would update the following skills:"
  for skill in "${SKILLS[@]}"; do
    echo "  - $skill"
  done
  echo "[dry-run] No files changed."
  exit 0
fi

mkdir -p "$DEST"

for skill in "${SKILLS[@]}"; do
  src="$src_root/$skill"
  dst="$DEST/$skill"

  if [[ ! -d "$src" ]]; then
    echo "Missing expected skill in source: $src" >&2
    exit 1
  fi

  rm -rf "$dst"
  cp -R "$src" "$dst"
  echo "[updated] $dst"
done

echo
echo "Conductor skills updated successfully."
echo "Restart Codex to pick up the updated skills."

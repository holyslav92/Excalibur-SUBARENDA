#!/usr/bin/env bash
# Push clean Excalibur-2-Cloud tree to a NEW empty private GitHub repo.
# Usage: ./scripts/push_new_private_repo.sh git@github.com:Horosheff/Excalibur-2-Cloud.git
set -euo pipefail
remote="${1:-}"
if [[ -z "$remote" ]]; then
  echo "Usage: $0 <git-remote-url-of-EMPTY-private-repo>" >&2
  exit 2
fi
root="$(cd "$(dirname "$0")/.." && pwd)"
if [[ ! -d "$root/.git" ]]; then
  git -C "$root" init -b main
  git -C "$root" add -A
  git -C "$root" commit -m "Excalibur-2-Cloud initial clean skeleton"
fi
git -C "$root" remote remove origin 2>/dev/null || true
git -C "$root" remote add origin "$remote"
git -C "$root" push -u origin main
echo "Pushed to $remote — verify visibility is PRIVATE."

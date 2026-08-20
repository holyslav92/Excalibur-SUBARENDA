#!/usr/bin/env bash
# Sync plugin agents/skills/rules → .cursor/ for Cloud Agents
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$root/.cursor/agents" "$root/.cursor/skills" "$root/.cursor/rules"
cp -a "$root/agents/." "$root/.cursor/agents/"
cp -a "$root/skills/." "$root/.cursor/skills/"
cp -a "$root/rules/." "$root/.cursor/rules/"
echo "Synced to .cursor/ for Cloud"

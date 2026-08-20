# Sync plugin agents/skills/rules → .cursor/ for Cloud Agents
# Prefer scripts/sync_cursor_cloud.sh on Linux Cloud VMs.

$root = Split-Path -Parent $PSScriptRoot
Copy-Item "$root\agents\*" "$root\.cursor\agents\" -Force
Copy-Item "$root\skills\*" "$root\.cursor\skills\" -Recurse -Force
Copy-Item "$root\rules\*" "$root\.cursor\rules\" -Force
Write-Host "Synced to .cursor/ for Cloud"

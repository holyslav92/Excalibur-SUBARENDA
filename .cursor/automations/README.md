# Cursor Automations (repo-tracked)

Определения автоматизаций для импорта в [Cursor Automations](https://cursor.com/docs/cloud-agent/automations).

> **Схема:** community pattern (`name`, `trigger`, `instructions`, `tools`) — Cursor UI остаётся primary, файл в git = source of truth для команды. Секреты (FTP_PASS и т.д.) **только** в Cloud Secrets.

| Файл | Назначение |
|------|------------|
| `dobry-dom-3x.yml` | 3 статьи/день YEKT 10:00, 14:00, 17:00 — holyslav92/Excalibur-SUBARENDA |

Канон расписания дублируется в `shared/tenant-config.json` → `publish_schedule` и `CLOUD-AUTOMATION.md`.

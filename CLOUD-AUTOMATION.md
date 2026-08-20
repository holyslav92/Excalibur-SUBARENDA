# Cloud Automation — Excalibur-SUBARENDA (Добрый дом)

**Репозиторий:** https://github.com/holyslav92/Excalibur-SUBARENDA  
**Не** Excalibur-2-Cloud (The Риэлтор).

**Только после** `memory/setup/status.json` → `complete: true`.

Тенант: **«Добрый дом»** / добрыйдом-72.рф — longform ~2000–2600 слов, cover + 7 inline-quad.
Темы: посуточная аренда, субаренда, заселение, залог, соседи, ЖКХ, Тюмень.

## Расписание (owner: 9–17 YEKT)

**4 запуска в будни** (пн–пт), часовой пояс **Asia/Yekaterinburg (YEKT, UTC+5)**:

| Слот | Время YEKT |
|------|------------|
| 1 | 09:00 |
| 2 | 12:00 |
| 3 | 15:00 |
| 4 | 17:00 |

- Окно владельца: **09:00–17:00** YEKT. Слот **20:00 не используется**.
- Выходные (сб–вс): longform automation **не запускать**, если owner не попросил отдельно.

### Cursor Automation (не GitHub Actions)

Настройте **4 отдельных триггера** в [Cursor → Automations](https://cursor.com/docs/cloud-agent/automations) на репозиторий **Excalibur-SUBARENDA**:

| Триггер | Расписание (YEKT) | Пример cron (TZ=Asia/Yekaterinburg) |
|---------|-------------------|-------------------------------------|
| 1 | пн–пт 09:00 | `0 9 * * 1-5` |
| 2 | пн–пт 12:00 | `0 12 * * 1-5` |
| 3 | пн–пт 15:00 | `0 15 * * 1-5` |
| 4 | пн–пт 17:00 | `0 17 * * 1-5` |

Канонические слоты дублируются в `shared/tenant-config.json` → `publish_schedule.slots_local`.

**Не добавляйте** GitHub Actions cron для этого longform-потока — расписание живёт в **Cursor Automation**.

**Memories = OFF** в Automation → Tools (см. `CLOUD-FIRST-RUN.md`).

## Один run = одна статья

```text
Scout? → research_start → Research → Title → Writer → Sol
→ Description → Cover-text || Schema → Cover → Cover-QA → Indexer
→ Publish? → Fixer → merge → Content-learner
```

- **Publish** — **только если одновременно**:
  1. в Cloud Secrets SFTP для **добрыйдом-72.рф** (не tymenrieltor.ru);
  2. `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` на процесс (**не git**).
- Если allow flag или FTP **нет** — run завершается после Indexer + артефактов в репо.

Writer = смысл (`drafts/writer.html`). Sol = слог тенанта (`shared/SOUL.md`).

## Thin conductor + Derouter two-tier (HARD)

См. `shared/derouter-opus-brain-contract.md` — без изменений от Excalibur-2-Cloud.

## Scout × Wordstat × Klyshin

Dual gate сохранён. Klyshin = angle/hook; Wordstat = evaluate + rework для
посуточной аренды / субаренды в Тюмени (Tyumen 55+11176, compare RU 225).

Банк: `memory/scout/klyshin-topic-bank.json`.

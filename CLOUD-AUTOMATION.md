# Cloud Automation — Excalibur-SUBARENDA (Добрый дом)

**Репозиторий:** https://github.com/holyslav92/Excalibur-SUBARENDA  
**Не** Excalibur-2-Cloud (The Риэлтор).

**Только после** `memory/setup/status.json` → `complete: true`.

Тенант: **«Добрый дом»** / добрыйдом-72.рф — один guest-night **CASE** ~1100–1800 слов, cover + 7 inline-quad.
Темы: посуточная аренда, субаренда, заселение, залог, соседи, ЖКХ, Тюмень.

## Расписание (owner: 10–17 YEKT)

**3 запуска каждый день** (пн–вс), часовой пояс **Asia/Yekaterinburg (YEKT, UTC+5)**:

| Слот | Время YEKT |
|------|------------|
| 1 | 10:00 |
| 2 | 14:00 |
| 3 | 17:00 |

- Окно владельца: **10:00–17:00** YEKT.
- Выходные (сб–вс): **включены** — те же три слота.

### Cursor Automation (не GitHub Actions)

**Repo config:** `.cursor/automations/dobry-dom-3x.yml` — импорт в [Cursor → Automations](https://cursor.com/docs/cloud-agent/automations).

Один триггер с тремя слотами (каждый день):

| Поле | Значение |
|------|----------|
| Имя | Добрый дом 3 статьи |
| Репозиторий | `holyslav92/Excalibur-SUBARENDA` |
| Cron (YEKT) | `CRON_TZ=Asia/Yekaterinburg 0 10,14,17 * * *` |
| Cron (UTC fallback) | `0 5,9,12 * * *` (= 10/14/17 YEKT) |
| Memories | **OFF** |
| MCP | MCP-KV `wordstat_*` only — **never** `wordpress_* |
| Publish site | только **добрыйдом-72.рф** (FTP Timeweb) — **never** tymenrieltor.ru |

Канонические слоты дублируются в `shared/tenant-config.json` → `publish_schedule.slots_local`.

**Не добавляйте** GitHub Actions cron для этого longform-потока — расписание живёт в **Cursor Automation**.

## Один run = одна статья

```text
Scout? → research_start → Research → Title → Writer → Sol
→ Description → Cover-text || Schema → Cover → Cover-QA → Indexer
→ Publish? → Fixer → merge → Content-learner
```

- **Publish** — **только если одновременно**:
  1. Cloud Secrets FTP для **добрыйдом-72.рф** ([REDACTED], port 21, root `[REDACTED]`);
  2. `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` на процесс (**не git**).
- **Never** tymenrieltor.ru, Excalibur-2-Cloud, MCP-KV `wordpress_*`.
- Если allow flag или FTP **нет** — run завершается после Indexer + артефактов в репо.

### Cover + images (HARD)

- **Brand lock:** official logo PNG paste (`logo-dobry-dom.png` / `cropped-img_7143.png`) on **cover always + 2–3 inline** (default inline_1/3/7). Never AI-drawn lockup. Never logo on all 8.
- **No plate** under logo pad (alpha paste only).
- Cover phone: **+7 (993) 574-83-22** painted **IN SCENE** (tape/paper/magnet) — **no** post-composite pill.
- NO host face / NO Shakin identity.
- Images: **Grsai** (`excalibur_blog_grsai_gpt_image2_api.py`, **PRIMARY_MODEL_ID only**, **vip disabled**; 2×2048×1152 quad). On exhaust: pad-clear + factory paste → **continue to publish** (no Cover-QA loop).
- **Cover-QA slim:** logo official, no plate, phone in scene on cover, no WP UI. Beauty = agent judgment on topic.
- After full upload: refresh WP intermediates (`*-1024x576`) for `/feed/zen/`.
- **Prose** — Derouter REST (`excalibur_blog_derouter_opus_chat.py`). Not Composer, not Flux/Seedream/nano_banana/mcp-derouter.

**Thin conductor:** Cursor не пишет прозу и не рисует кадры. **Writer** = `claude-opus-5` (полный CASE в `drafts/writer.html`, не тезисы). **Sol** = `gpt-5.6-terra` (слог `shared/SOUL.md` + `shared/soul-examples/`).

**CASE delivery gate:** после Title и после Writer/Sol — `scripts/excalibur_blog_case_delivery_gate.py`. BLOCK → переписать роль, не публиковать.

**Воронка:** один блок CTA **только в конце** статьи (не после чеклиста, не после «у нас так»).

## Thin conductor + Derouter two-tier (HARD)

См. `shared/derouter-opus-brain-contract.md`.

## Scout × Wordstat × Klyshin

Dual gate сохранён. Klyshin = angle/hook; Wordstat = evaluate + rework для
посуточной аренды / субаренды в Тюмени (Tyumen 55+11176, compare RU 225).

**Wordstat:** MCP-KV `wordstat_*` only.

Банк: `memory/scout/klyshin-topic-bank.json`.

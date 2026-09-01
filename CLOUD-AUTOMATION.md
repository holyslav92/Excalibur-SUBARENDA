# Cloud Automation — Excalibur-SUBARENDA (Добрый дом)

**Репозиторий:** https://github.com/holyslav92/Excalibur-SUBARENDA  
**Не** Excalibur-2-Cloud (The Риэлтор).

**Только после** `memory/setup/status.json` → `complete: true`.

Тенант: **«Добрый дом»** / добрыйдом-72.рф — один guest-night **CASE** **700–1100 слов** (`dobry_dom_gen_only_human_v1`), **1 cover + 3 inline** (`dobry_dom_gen_only_human_v1`).
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

### Cover + images (HARD — `dobry_dom_gen_only_human_v1`)

- **ONE Grsai primary image** draw per article: canvas **2048×1152** as **2×2 photoreal GRID** → PIL slice → **[0] cover + [1..3] inlines**. **ZERO** second draw; **BAN** overlay scripts (poster_composite, phone pill, sticky, marker).
- **Cover panel:** Cyrillic H1 on physical object IN photograph — NOT graphic overlay.
- **Phone +7 (993) 574-83-22** in article TEXT only — never on cover image.
- **After slice, cover tile ONLY:** factory paste `cropped-img_7143.png` — native aspect, no plaque. **Inlines: ZERO logo. NEVER logo in Grsai images[].**
- Allowed scripts: `excalibur_blog_cover_quad_split.py` + `excalibur_blog_brand_logo_composite.py` only.

### Prose manner (HARD — `dobry_dom_gen_only_human_v1`)

- **700–1100 слов**, spoken Russian at the door. First 2–3 sentences: what happened + quote or ₽.
- BAN riddle H1, «под вопросом», clever structure. ONE «Мой вывод как практика».

**Thin conductor:** Cursor не пишет прозу и не рисует кадры. **Writer** = `claude-opus-5` (полный CASE в `drafts/writer.html`, не тезисы). **Sol** = `gpt-5.6-terra` (слог `shared/SOUL.md` + `shared/soul-examples/`).

**CASE delivery gate:** после Title и после Writer/Sol — `scripts/excalibur_blog_case_delivery_gate.py`. BLOCK → переписать роль, не публиковать. **BAN duty-log lead** (дата/часы/`HH:MM` в §1) и **BAN `HH:MM` в H1** — holyslav smooth quote-first opening.

**Воронка:** один блок CTA **только в конце** статьи (не после чеклиста, не после «у нас так»).

**Dzen xlinks (HARD):** в `article.html` и RSS — только `{{SITE_BASE}}/blog/{slug}/` (или expanded absolute `https://<site>/blog/{slug}/`); **никогда** root-relative `href="/blog/..."` (Дзен in-app browser → 404 без `/blog/`).

## Thin conductor + Derouter two-tier (HARD)

См. `shared/derouter-opus-brain-contract.md`.

## Scout × Wordstat × Klyshin

Dual gate сохранён. Klyshin = angle/hook; Wordstat = evaluate + rework для
посуточной аренды / субаренды в Тюмени (Tyumen 55+11176, compare RU 225).

**Wordstat:** MCP-KV `wordstat_*` only.

Банк: `memory/scout/klyshin-topic-bank.json`.

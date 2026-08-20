# Cloud First Run — Excalibur-SUBARENDA (Добрый дом)

**Репозиторий:** https://github.com/holyslav92/Excalibur-SUBARENDA  
**Сайт:** https://добрыйдом-72.рф/ (punycode: `xn---72-9cdob8azaodt6k.xn--p1ai`)

> **Не трогать:** holyslav92/Excalibur-2-Cloud (The Риэлтор) — другой тенант, другие credentials.

Официальные источники Cursor:

- https://cursor.com/docs/cloud-agent
- https://cursor.com/docs/cloud-agent/setup
- https://cursor.com/docs/cloud-agent/automations
- https://cursor.com/docs/cloud-agent/security

## 1. Environment

1. Dashboard → Cloud Agents → Environments.
2. Подключите репозиторий **holyslav92/Excalibur-SUBARENDA** (не Excalibur-2-Cloud).
3. `.cursor/environment.json` задаёт `install` (pip + doctor).
4. Дождитесь успешного Build.

## 2. Cloud Secrets (обязательно перед Publish)

| Secret | Значение для Добрый дом | Зачем |
|--------|-------------------------|--------|
| `PUBLIC_SITE_URL` | `https://xn---72-9cdob8azaodt6k.xn--p1ai` | Live URL, link-verify, bootstrap HTTP trigger |
| `FTP_HOST` | `vh368.timeweb.ru` | Timeweb FTP (не SFTP) |
| `FTP_USER` | `ca21576_svyat` | Extra FTP user (SFTP:22 = Permission denied) |
| `FTP_PASS` | *(только в Secrets, никогда в git)* | Пароль из панели Timeweb |
| `FTP_PORT` | `21` | Passive FTP |
| `FTP_TRANSPORT` | `ftp` | Явный выбор transport (альтернатива: только `FTP_PORT=21`) |
| `FTP_ROOT` | `sublease/public_html` | Каталог с `wp-load.php` (web root сайта) |
| `EXCALIBUR_BLOG_ALLOW_PUBLISH` | `yes` | **Только runtime в Secrets** — в git всегда `no` |

Опционально:

| Secret | Зачем |
|--------|--------|
| `WP_SITE_URL` | REST / admin (если нужен отдельно от PUBLIC_SITE_URL) |
| `DEROUTER_API_KEY` | Cover 2× quad canvas 2K |
| **MCP-KV** | Wordstat PRIMARY (Scout hard gate) |
| `YANDEX_METRIKA_*` | Content-learner |

**Не копировать** FTP/WP secrets из Excalibur-2-Cloud (tymenrieltor.ru).

Шаблон имён (без пароля): `.env.example`.

### Publish gate (двойной замок)

1. В **git** / `.env.example`: `EXCALIBUR_BLOG_ALLOW_PUBLISH=no` — всегда.
2. В **Cloud Secrets**: `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` — только когда владелец готов к live publish.

Без обоих условий (secrets + allow flag) скрипт publish вернёт `BLOCKER`.

### FTP_ROOT и wp-load.php

Bootstrap `excalibur-blog-publish-once.php` загружается **в каталог WordPress** и делает `require __DIR__ . '/wp-load.php'`.

Для Timeweb extra FTP user `ca21576_svyat` канон:

- login cwd → домашняя папка аккаунта
- `FTP_ROOT=sublease/public_html` → web root сайта «добрыйдом-72.рф»

Если upload падает с ENOENT, transport автоматически пробует login cwd (`.`) — тогда обновите `FTP_ROOT` в Secrets.

Проверка без publish:

```bash
python3 scripts/excalibur_blog_wp_publish.py --env-check
```

## 3. Cover factory (готово в репо)

- **Logo lockup** на всех 8 изображениях: `memory/cover/assets/brand/logo-dobry-dom.png`
- **Нет** locked host face / Shakin identity
- `cover_mode: logo_lockup` в `shared/tenant-config.json`
- Inline = utility info-graphics (таблицы, шаги, чеклисты) — не decorative-only

Дополнительная настройка визуала владельцу **не нужна**.

## 4. Memories — ВЫКЛЮЧИТЬ

В Automation → Tools: **Memories = OFF**.

## 5. MCP

**Обязательно для Scout:** MCP-KV + Wordstat tools (`wordstat_get_user_info`, `wordstat_get_top_requests`).

## 6. Setup gate

`memory/setup/status.json` → `complete: true`. Visual = done (logo lockup).

## 7. First automation prompt

См. `CLOUD-AUTOMATION.md` — 3×/будни YEKT (10/13/17), `.cursor/automations/dobry-dom-3x.yml`, Scout → … → Cover-QA → Indexer → Publish (только при Secrets + allow flag).

# Cloud First Run — Excalibur-SUBARENDA (Добрый дом)

**Репозиторий:** https://github.com/holyslav92/Excalibur-SUBARENDA  
**Сайт:** https://добрыйдом-72.рф/ (punycode: `xn---72-9cdob8azaodt6k.xn--p1ai`)

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

## 2. Secrets

| Secret | Зачем |
|--------|--------|
| `PUBLIC_SITE_URL` | `https://xn---72-9cdob8azaodt6k.xn--p1ai` или unicode URL |
| `WP_SITE_URL` | REST base для добрыйдом-72.рф — **новые** credentials |
| `FTP_HOST` / `FTP_USER` / `FTP_PASS` / `FTP_ROOT` | SFTP publish на **Добрый дом** |
| `EXCALIBUR_BLOG_ALLOW_PUBLISH` | `yes` только когда готовы публиковать |
| Image API (Derouter REST 2K) | Cover longform 2× quad canvas |
| **MCP-KV** | Wordstat PRIMARY |
| `MCP_KV_TOKEN` | Optional if not using dashboard connector |
| `YANDEX_METRIKA_*` | Опционально Content-learner |

**Не копировать** FTP/WP secrets из Excalibur-2-Cloud (tymenrieltor.ru).

Шаблон имён: `.env.example`.

## 3. Memories — ВЫКЛЮЧИТЬ

В Automation → Tools: **Memories = OFF**.

## 4. MCP

**Обязательно для Scout:** MCP-KV + Wordstat tools.

## 5. Setup gate

Если `memory/setup/status.json` → `complete != true` — работай как Setup.
После fork: `complete: true`, но **visual → need_replace** (лицо/identity).

## 6. First automation prompt

См. `CLOUD-AUTOMATION.md` — 4×/будни YEKT, Scout → Publish pipeline.

## 7. Visual TODO

Замените `memory/cover/assets/identity-real/` и обновите `memory/cover/blog-hero.json`
после загрузки фото бренда. До замены Cover-QA может FAIL на identity — ожидаемо.

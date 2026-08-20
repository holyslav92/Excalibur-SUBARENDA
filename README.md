# Excalibur-SUBARENDA

Фабрика контента Excalibur для **«Добрый дом»** (посуточная аренда и субаренда
в Тюмени). Репозиторий: https://github.com/holyslav92/Excalibur-SUBARENDA

Чистый агентный пайплайн блога для **Cursor Cloud**: Scout → Research →
Title → Writer → Sol → Cover/Schema → Indexer → Publish.

Тенант: **«Добрый дом»** — квартиры и апартаменты **посуточно в Тюмени**
(командировки, пары, семьи). Бесконтактное заселение, поддержка в мессенджере,
ответ до 5 минут. 10 лет на рынке в Сургуте и Тюмени.

- Сайт (punycode): https://xn---72-9cdob8azaodt6k.xn--p1ai/
- Unicode: https://добрыйдом-72.рф/
- Блог: https://добрыйдом-72.рф/blog

## Быстрый старт

1. Склонируйте репозиторий **holyslav92/Excalibur-SUBARENDA** в Cursor /
   подключите Cloud Environment.
2. Прочитайте [`CLOUD-FIRST-RUN.md`](CLOUD-FIRST-RUN.md) — Secrets, MCP,
   **Memories OFF**.
3. Запустите First-run automation / чат с промптом Setup (если нужно
   обновить лицо/визуал — см. TODO в `shared/tenant-config.json`).
4. Когда `memory/setup/status.json` → `complete: true`, настройте Daily
   automation из [`CLOUD-AUTOMATION.md`](CLOUD-AUTOMATION.md).

Карта анкеты: [`SETUP.md`](SETUP.md). Канон агентов: [`AGENTS.md`](AGENTS.md).

## Что внутри

| Путь | Роль |
|------|------|
| `agents/` + `.cursor/agents/` | Director, Setup, Sol, Cover, Publish… |
| `skills/` | Runbook'и субагентов |
| `shared/` | Контракты, SOUL, tenant-config |
| `memory/setup/` | Статус онбординга, inbox примеров |
| `scripts/` | Гейты, publish, cover split (инфраструктура) |

## TODO после клонирования

- **WP / SFTP secrets** для добрыйдом-72.рф (не tymenrieltor.ru)
- **Лицо ведущего / identity-real** — заменить фото (сейчас placeholder / NEED-REPLACE)
- **Cursor Cloud Automation** — 4×/будни YEKT на репозиторий Excalibur-SUBARENDA
- **EXCALIBUR_BLOG_ALLOW_PUBLISH** — только `yes` в Secrets, когда готовы к live

## Лицензия / доступ

Публичный репозиторий. Владелец: holyslav92.

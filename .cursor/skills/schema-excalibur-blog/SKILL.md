---
name: schema-excalibur-blog
description: Excalibur BLOG Schema — BlogPosting + optional FAQPage, author registry.
---

# Excalibur BLOG — Schema

## Thin conductor + Derouter utility (HARD)

**Не пиши schema.jsonld моделью Cursor:**

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role schema \
  --system-file skills/schema-excalibur-blog/SKILL.md \
  --user-file <assembled-schema-inputs.md> \
  --output schema.jsonld \
  --article-dir <article_dir>
```

Bare `--output` filenames resolve under `--article-dir` (same rule as schema-gate `-o`).

`DEROUTER SCHEMA BLOCKER` → стоп. Контракт: `shared/derouter-opus-brain-contract.md`.

## Вход

- `article.html`, `article.meta.json`, `research-notes.md`
- `shared/authors-registry.json` — author **Добрый дом** (`dobry-dom`)
- `memory/brief/site-brief.md` (site_url) **или** env `PUBLIC_SITE_URL`

## Site base URL (обязательно)

1. **Канон для сборки:** `PUBLIC_SITE_URL` (Cloud Secrets / env) или `site_url` из `memory/brief/site-brief.md`.
2. **Запрещено** копировать `Organization.url` / `@id` / `image` base из соседних `schema.jsonld` (B11 и др.) — там может быть битый литерал `[REDACTED]` или чужой host.
3. **Запрещено** писать в файл литерал `[REDACTED]` (это маска tool-display / старая редкация, не URL).
4. **Для git-артефактов** после сборки (или сразу при записи) используй плейсхолдер `{{SITE_BASE}}` вместо живого host — Cursor secret scan блокирует commit с `PUBLIC_SITE_URL`. Publish раскрывает `{{SITE_BASE}}` → `PUBLIC_SITE_URL` только в WP payload.
5. **Canonical article URL (HARD):** `{{SITE_BASE}}/blog/<slug>/` — **must include `/blog/`** path matching live WP permalink.  
   BlogPosting `url`, `@id`, `mainEntityOfPage.@id` — все с `/blog/<slug>/`.  
   **Запрещено** `{{SITE_BASE}}/<slug>/` без `/blog/` (live gate FAIL).
6. **Publish slug (HARD, INC B12):** `<slug>` = `title-brief.json` → `article.meta.json` → **никогда** только суффикс `--article-dir`, если Title выдал другой slug.  
   Пример: dir `B12-kvartira-posutochno-…`, publish slug `napisali-tihij-centr-v-6-30-za-oknom-kran` из title-brief.  
   В `assembled-schema-inputs.md` canonical URL строить только из publish slug (`resolve_publish_slug` в `excalibur_blog_article_meta_index.py`).

## Author (HARD)

- **NEVER** mention **Святослав Шакин** / **The Риэлтор** in schema author/publisher.
- Author = **Добрый дом** from `shared/authors-registry.json` (`id: dobry-dom`).
- `@type`: Organization (или Person только если registry так задаёт — канон: Organization «Добрый дом»).

## GEO-AI schema (HARD)

- **LocalBusiness** (or Organization from registry) with NAP: «Добрый дом», **Тюмень**, phone **+7 (993) 574-83-22**
- BlogPosting headline/date/author «Добрый дом»; city in meta when local intent is honest
- FAQPage only from visible FAQ section — answers weave live Wordstat query shapes naturally (see `memory/cover/wordstat-geo.json`)
- **BAN** stuffing and banned weak cluster «посуточная аренда тюмень»
- **NEVER** mention Святослав Шакин / The Риэлтор

## Задача

1. BlogPosting: headline, datePublished (today из research-context), author **Добрый дом** + sameAs.
2. FAQPage — только если в статье есть реальная секция FAQ. Если FAQ нет, не
   создавать FAQPage ради schema.
   - Visible FAQ = только пары `<h3>вопрос?</h3><p>ответ</p>` в секции
     «Частые вопросы». Если в HTML `<p>Q? A</p>` без h3 — не парси вручную:
     верни Editor FIX (html_linter / INC-20260721-0131); schema_gate даст
     visible=0.
   - `acceptedAnswer.text` = **только первый `<p>`** после каждого `<h3>`
     (plain text, без HTML). Sibling CTA/interlink `<p>` после ответа
     **не** входят в FAQPage (INC-20260726-1615); если хвост в секции —
     верни Editor FIX (CTA до FAQ H2 или отдельный H2), не копируй хвост
     в schema ради gate PASS.
   - Gate нормализует пробелы после strip `<a>`: `гайда ,` ≡ `гайда,`
     (INC-20260720-2028). Не подгоняй JSON-LD под артефактный пробел перед
     запятой/точкой — пиши естественный текст; parity сравнивает нормализованно.
   - При FAIL gate печатает индекс Q и short char-diff schema vs visible.
3. HowTo / Review — только если архетип требует.
4. **Порядок записи и gate (без race):** сначала полностью запиши `schema.jsonld` на диск (дождись завершения Write), **затем** отдельным шагом запусти gate. **Запрещено** запускать `schema_gate.py` в том же parallel tool-batch, что и Write `schema.jsonld` — gate читает диск и получит `missing schema.jsonld`.

```bash
# из корня репо — не cd в article_dir
python3 scripts/excalibur_blog_schema_gate.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  -o schema-gate.json
```

**HARD (INC-20260730-0313):** `--article-dir` = **только** repo-relative
`memory/blog/articles/<topic_id>-<slug>` (или absolute). **Запрещены**
`cd <article_dir> && … --article-dir .` и bare `.` в Task prompt.
Скрипт теперь резолвит bare `.` через cwd, но канон агента — путь от корня репо.

**HARD (INC-20260726-0813):** `-o` = **только** bare `schema-gate.json`
(файл пишется в `--article-dir`). **Запрещён** repo-relative
`-o memory/blog/articles/.../schema-gate.json` in Task prompt — старый
resolve nested path под article_dir. Скрипт теперь терпит repo-relative
через root-resolve, но канон агента остаётся bare filename.

`status` должен быть `PASS` (нет `[REDACTED]`, валидный JSON).

## Fragment (обязательно)

После gate PASS запиши `.cursor/excalibur-blog-fragments/schema.md` по
`shared/pipeline-fragment-protocol.md` — **с YAML frontmatter**, иначе
Director `handoff_merge.py` падает с `frontmatter missing` (B65 /
INC-20260720-1556). Шаблон — в `agents/excalibur-blog-schema.md`.

## Выход

`memory/blog/articles/<topic_id>-<slug>/schema.jsonld`

Контракт HTML/schema: `shared/excalibur-article-writing-contract.md` (секция schema).

# Excalibur BLOG — перекрёстные ссылки (interlink)

Включается флагом `shared/tenant-config.json` → `interlink_old_articles: true`.

## Два направления

1. **Outbound (новая статья)** — Writer/Sol добавляют **3–4** контекстные ссылки на
   уже опубликованные материалы из `shared/published-articles.md` (только
   `status=published`, **разные slug**, только живые HTTP 200 `/blog/` URL).
   Якорь — по смыслу H2, не «читайте также» в каждом абзаце.
   **Cross-link QA** (`crosslink-qa-gate.py`) сравнивает текст **только внутри**
   `<a>…</a>` с `title` из `memory/live-catalog.json` (допускается короткий
   смысловой якорь или полный H1 sibling в кавычках «…»). Проза до/после ссылки
   в якорь не входит — не полагайся на «склеенный» абзац.
   Если живых sibling <3 — линковать все доступные, never invent URL.
2. **Inbound (старые live-посты)** — после успешного Publish, если флаг включён,
   post-publish interlink добавляет в 1–3 релевантных старых поста блок
   «Читайте также» со ссылкой на новую статью (один раз, идемпотентно).

## Ограничения

- Не более **3 inbound** правок за один publish-run.
- Не трогать посты со `status != published` в ledger.
- URL только path из ledger или `{{SITE_BASE}}/slug/` после expand.
- Не переписывать тело статьи — только append блока, если ссылки ещё нет.
- Live publish только при `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` (env, не git).

## CLI

```bash
python3 scripts/excalibur_blog_post_publish_interlink.py \
  --article-dir memory/blog/articles/<topic>-<slug> \
  --dry-run

python3 scripts/excalibur_blog_post_publish_interlink.py \
  --article-dir memory/blog/articles/<topic>-<slug>
```

`--dry-run` — план + проверка outbound в `article.html`. Без флага — inbound
append в 1–3 старых поста через bootstrap `excalibur-blog-interlink-once.php`
(идемпотентно по `data-excalibur-interlink-from`).

После publish скрипт `excalibur_blog_wp_publish.py` автоматически вызывает
interlink, если `publish_options.auto_interlink_after_publish=true`.

**FTP PASV (Timeweb):** post-publish inbound bootstrap может упасть по timeout на
первой попытке после тяжёлого publish. `publish_via_ftp` и auto-interlink в
`excalibur_blog_wp_publish.py` делают до 3 идемпотентных retry (inbound marker
`data-excalibur-interlink-from`); ручной повтор `post_publish_interlink.py`
безопасен.

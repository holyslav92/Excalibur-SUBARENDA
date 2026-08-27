# Excalibur BLOG — перекрёстные ссылки (interlink)

Включается флагом `shared/tenant-config.json` → `interlink_old_articles: true`.

## Два направления

1. **Outbound (новая статья)** — Writer/Sol добавляют **3–4** контекстные ссылки на
   уже опубликованные материалы из `shared/published-articles.md` (только
   `status=published`, **разные slug**, только живые HTTP 200 `/blog/` URL).
   Якорь — по смыслу H2, не «читайте также» в каждом абзаце.
   Если живых sibling <3 — линковать все доступные, never invent URL.
2. **Inbound (старые live-посты)** — после успешного Publish, если флаг включён,
   post-publish interlink добавляет в 1–3 релевантных старых поста блок
   «Читайте также» со ссылкой на новую статью (один раз, идемпотентно).

## Ограничения

- Не более **3 inbound** правок за один publish-run.
- Не трогать посты со `status != published` в ledger.
- URL только path из ledger или `{{SITE_BASE}}/slug/` после expand.
- **Outbound hrefs в `article.html`:** path-only `/blog/{slug}/` (relative или с ASCII `PUBLIC_SITE_URL`). Не full URL с кириллическим host — `link-verify` / `crosslink-qa` HTTP падают на IDNA/punycode mismatch (INC B03).
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

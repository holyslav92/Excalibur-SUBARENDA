# Excalibur BLOG — перекрёстные ссылки (interlink)

Включается флагом `shared/tenant-config.json` → `interlink_old_articles: true`.

## Два направления

1. **Outbound (новая статья)** — Writer/Sol добавляют 1–3 контекстные ссылки на
   уже опубликованные материалы из `shared/published-articles.md` (только
   `status=published`). Якорь — по смыслу H2, не «читайте также» в каждом абзаце.
2. **Inbound (старые live-посты)** — после успешного Publish, если флаг включён,
   post-publish interlink добавляет в 1–3 релевантных старых поста блок
   «Читайте также» со ссылкой на новую статью (один раз, идемпотентно).

## Ограничения

- Не более **3 inbound** правок за один publish-run.
- Не трогать посты со `status != published` в ledger.
- URL: Writer/Sol в git пишут `/blog/{slug}/`. **Publish** (`load_article`) раскрывает в абсолютный `PUBLIC_SITE_URL/blog/{slug}/` — иначе Дзен открывает `dzen.ru/blog/…`. Inbound «Читайте также» тоже абсолютный URL. Не класть live-host в git.
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

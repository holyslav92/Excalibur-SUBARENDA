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

## Live-каталог для crosslink QA

Перед publish `excalibur_blog_crosslink_qa_gate.py` обновляет `memory/live-catalog.json`
обходом `/blog/` listing (по умолчанию до **24** страниц, `MAX_LISTING_PAGES` в
`scripts/excalibur_blog_live_catalog.py`). На сайте сотни постов; shallow crawl
(раньше 8 страниц) давал ложный FAIL «invented slug» для живых sibling из ledger.

- Crawl **останавливается раньше**, когда все slug из `shared/published-articles.md`
  уже в каталоге.
- Если после полного crawl в каталоге **нет** slug из ledger — **BLOCKER** до увеличения
  `--max-pages` / константы (INC B43).

```bash
python3 scripts/excalibur_blog_live_catalog.py --max-pages 24
```

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

## Retry после timeout (Cloud / Timeweb)

Если после крупного bootstrap-upload inbound не применился (FTP PASV `421` /
`TimeoutError`, или `wp-publish-log` → `interlink inbound: pending`):

1. Подождать завершения publish (live-page PASS).
2. Повторить вручную или через Fixer:

```bash
python3 scripts/excalibur_blog_post_publish_interlink.py \
  --article-dir memory/blog/articles/<topic>-<slug>
```

`excalibur_blog_wp_publish.py` делает **один автоматический retry** interlink
перед BLOCKER (INC B13). Скрипт interlink всегда идёт через SFTP bootstrap.

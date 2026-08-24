# Excalibur BLOG — WordPress publish contract

## Future articles: theme suppression and live verification

`article.meta.json.theme_blocks` must set `faq`, `quiz`, `side_stickers` to
`skip`. The body contains exactly one topic-specific FAQ. After upload, run
`scripts/excalibur_blog_live_page_gate.py` per
`shared/live-page-contract.md`. `live-page-report.json` PASS is mandatory;
otherwise `LIVE PAGE BLOCKER` and no PIPELINE DONE.

Excalibur BLOG готовит артефакты локально; публикация — через `scripts/excalibur_blog_wp_publish.py` и SFTP bootstrap.

## Prerequisites

- `article.html`, `article.meta.json` (`pipeline_canon` stamp, `theme_blocks.*.skip`)
- `schema.jsonld` + `schema-gate.json` PASS
- `cover/cover.png` + `cover-registry.json` (alt)
- `link-verify.json` (verdict pass)
- Cloud Secrets / env vars или `memory/site.env.local` — FTP или SFTP доступ + `PUBLIC_SITE_URL` + `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`
- **Секреты:** `FTP_HOST` / `FTP_USER` / `FTP_PASS` / `FTP_ROOT` / `FTP_PORT` / `FTP_TRANSPORT`
  - **SFTP (default):** port 22 — `FTP_*` = те же SFTP-учётные данные; `SSH_*` = алиасы
  - **FTP passive (Добрый дом / Timeweb):** `FTP_PORT=21` или `FTP_TRANSPORT=ftp`; `FTP_ROOT=sublease/public_html`
- Env precedence: переменные окружения перекрывают `memory/site.env.local`.
- Root: `FTP_ROOT` относительно FTP login cwd (Timeweb: `sublease/public_html`). Пустой или `/` → `.`

## Скрипт

```bash
python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/B01-slug/article.html \
  -o memory/blog/articles/B01-slug/link-verify.json \
  --site-base https://example.com

python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/B01-slug
```

`--dry-run` — проверка payload без SFTP upload.

## Что делает publish

1. **Preflight gates** (обязательно, иначе BLOCKER; emergency `--skip-gates`):
   - `link-verify.json` → `verdict: pass`
   - `schema.jsonld`, `schema-gate.json` PASS, `cover/cover.png`
   - `article.html` + `article.meta.json` с `pipeline_canon` stamp
   - `freshness-report.json` — только если файл есть → PASS
     (`excalibur_blog_contract_freshness.py`)
2. **MEDIA REFRESH** (`--media-refresh`) для уже published ledger-поста:
   - те же gates, что выше, **кроме** freshness: `status=STALE` допускается;
   - ledger `status=published` обязателен;
   - **не** используй blanket `--skip-gates` (INC-20260723-1235);
   - алиас только freshness: `--allow-stale-freshness`
3. `wp_insert_post` / `wp_update_post` — title, slug, content, excerpt
   - **Рубрики (обязательно):** `wp_set_post_categories` из `article.meta.json`
     `wp_category_slugs` или `shared/wp-blog-categories.json` → `topic_defaults`.
     Без рубрики (`bez-rubriki`) publish **BLOCKER**, если
     `tenant-config.wp_categories_required=true`.
   - **HARD (Dzen/RSS):** `post_excerpt` must **not** be a truncated copy of
     the opening paragraphs. RSS emits excerpt as `<description>` and the
     body as `<content:encoded>`; Dzen/RSSLint often shows both → duplicate
     lead (INC-20260805-2240). Publish uses `rss_safe_excerpt()`: if
     description clones the opening, fall back to H1/title. Meta description
     for SEO may still exist, but excerpt for WP/RSS stays distinct.
4. Featured image из `cover/cover.png` + **Media Library meta**:
   - **Атрибут alt** ← `cover-registry.json` `alt` / `cover_alt_text` / asset `alt`
   - **Подпись (caption)** ← осмысленный alt → `post_excerpt`; deprecated `meme_caption_ru` игнорировать (он обязан быть пуст)
   - **Описание (description)** ← alt → `post_content`
   - **Заголовок** ← укороченный alt → `post_title`
5. **Inline images** — все локальные `<img src="cover/...">` загружаются в Media Library:
   - alt из HTML `alt="..."` или registry asset `alt` → `_wp_attachment_image_alt`
   - caption / description / title аналогично (description дополняется `h2_anchor` из registry, если есть)
   - `src` в `post_content` заменяется на WP media URL (HTML `alt` в теле поста сохраняется)
6. **Media completeness**: `WARN cover` / неполный inline upload → publish **fail** (не `OK post=` alone)
6b. **Dzen / WP intermediates (live overwrite):** `/feed/zen/` enclosure и `<img>` в RSS
   часто ссылаются на **промежуточные** файлы (`-1024x576`, `-768x432`, `-300x169`,
   `-150x150`), а не на full PNG. После SFTP-overwrite full cover/inline **обязательно**
   прогон `scripts/excalibur_blog_wp_intermediate_refresh.py` (или live regen upload,
   который вызывает его автоматически), затем `scripts/excalibur_blog_live_dzen_bump.py`
   для `post_modified_gmt` в 7-дневном окне Дзена.
7. Post meta `_excalibur_blog_schema_jsonld` — JSON-LD для `single.php`
8. Post meta `_excalibur_blog_skip_theme_faq` = `1` — сигнал теме **не** добавлять глобальный FAQ-блок
9. После publish — `llms.txt` + `llms-full.txt` в корень WP (`--deploy-llms` или `tenant-config.publish_options.deploy_llms_after_publish=true`)

Маппинг полей WP Media Library:

| Админка WP | Поле attachment | Источник пайплайна |
|------------|-----------------|--------------------|
| Атрибут alt | `_wp_attachment_image_alt` | registry / `<img alt>` |
| Подпись | `post_excerpt` | caption / meme / alt |
| Описание | `post_content` | description / alt (+ h2) |
| Заголовок | `post_title` | укороченный alt |

## Дубли FAQ на live-странице (важно)

Excalibur кладёт в `post_content` **один** FAQ по теме (`<h2>Частые вопросы</h2>`).

Тема example.com может **дописывать** после контента второй блок «Часто задаваемые вопросы по теме (FAQ)» с универсальными вопросами про контент-завод — это **не** часть `article.html`.

**Исправление в теме WordPress** (`single.php` или фильтр `the_content`):

```php
$skip_theme_faq = get_post_meta(get_the_ID(), '_excalibur_blog_skip_theme_faq', true);
if ($skip_theme_faq === '1') {
    // не выводить глобальный FAQ-блок темы для постов Excalibur BLOG
}
```

Publish-скрипт выставляет meta `_excalibur_blog_skip_theme_faq` автоматически при каждой публикации.

## Артефакты после publish

```text
memory/blog/articles/<topic_id>-<slug>/wp-publish-result.json
memory/blog/wp-publish-log.md
```

## Schema в теме WP

```php
$schema = get_post_meta(get_the_ID(), '_excalibur_blog_schema_jsonld', true);
if ($schema) {
    echo '<script type="application/ld+json">' . wp_kses_post($schema) . '</script>';
}
```

## Blockers

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail, нет credentials
- Production HTML не должен содержать MCP URLs — только WP media для featured image

Skill: `skills/publish-excalibur-blog/SKILL.md`

## SITE_BASE placeholder

Git-safe artifacts **must** use `{{SITE_BASE}}` instead of the live host (Cursor secret scan blocks commits with `PUBLIC_SITE_URL`).
Never write tool-display mask `[REDACTED]` into schema/llms as a fake URL.
Publish expands `{{SITE_BASE}}` → `PUBLIC_SITE_URL` in the WP payload only (`load_article`); committed files keep `{{SITE_BASE}}`.
В том же `load_article` корневые `href="/…"` (в т.ч. `/blog/…`) становятся абсолютными — иначе Дзен резолвит их от `dzen.ru`.
Dry-run reports `schema_placeholder_remaining` and exits non-zero if expand failed.
`shared/published-articles.md` stores path-only URLs (`/slug/`) via `ledger_url_for_commit`.


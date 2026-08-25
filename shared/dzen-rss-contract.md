# Dzen RSS contract (`/feed/zen/`)

Канон для Яндекс Дзен при плагине **RSS for Yandex Zen** (`yzen_options`).

## Проблема

Плагин по умолчанию:

| Симптом | Причина |
|---------|---------|
| В Студии только картинка | `<category>native-no</category>` |
| 8 enclosure | обложка + каждый `<img>` в `content:encoded` |
| Обложка 1024×576 | `yzselectthumb` пустой / intermediate |
| Пустой author | `yzauthor` не задан |
| Channel link Timeweb | `yzlink` = старый URL |

## Директивы Дзен (category в RSS)

- `format-article` — нативная статья (не `format-post`)
- `native-yes` — публиковать в Дзене (**никогда** `native-no`)
- `evergreen` — материал (не новость); плагин ставит при `yztypearticle=false`
- `index` — индексировать

MU-plugin `factory/wp-mu-plugins/excalibur-dzen-rss.php`:

- одна enclosure (обложка, full PNG);
- добавляет `format-article`;
- убирает `native-no`;
- full URL обложки (без `-1024x576`).

## Глобальные настройки (`yzen_options`)

Publish и `scripts/excalibur_blog_live_dzen_rss_fix.py` выставляют:

- `yzlink` = `PUBLIC_SITE_URL`
- `yzauthor` = «Добрый дом»
- `yztypeplatform` = `native-yes`
- `yztypearticle` = `false` → RSS `evergreen`
- `yzindex` = `index`
- `yzthumbnail` = `enabled`
- `yzselectthumb` = `full`

## Meta на каждый пост (publish)

`scripts/excalibur_blog_wp_publish.py` после `wp_set_post_categories`:

- `yztypeplatform_meta_value` = `native-yes`
- `yztypearticle_meta_value` = `false`
- `yzindex_meta_value` = `index`

## Live fix одного поста

Задайте `PUBLIC_SITE_URL` и FTP-учётные данные в env (см. `shared/excalibur-wp-publish-contract.md`), затем:

```bash
python3 scripts/excalibur_blog_live_dzen_rss_fix.py --post-id 4002 \
  --slug posutochno-u-vuza-roditeli-s-pervokursnikom-na-3-nochi-ne-na-semestr
python3 scripts/excalibur_blog_live_dzen_rss_fix.py --verify-only
```

## Проверка SUCCESS

Первый `<item>` в `/feed/zen/`:

- `<title>` не пустой
- `<content:encoded>` с текстом статьи
- **одна** `<enclosure>` (full cover, ≥700px)
- **нет** `native-no`
- есть `format-article`

## Важно

Если карточка уже открыта в Дзен Студии как «картинка», RSS не перепишет её —
удалите picture-publication в Студии для re-pull.

См. также: `shared/dzen-cover-cache-bust.md`, `shared/excalibur-wp-publish-contract.md`.

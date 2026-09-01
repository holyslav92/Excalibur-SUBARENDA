# Dzen cover cache-bust (factory canon)

## Проблема

`/feed/zen/` отдаёт `<enclosure url="…-1024x576.png">`. Дзен CDN кэширует картинку **по URL**.
Перезапись того же файла на хостинге (даже с новым `post_modified`) **не обновляет** карточку в ленте.

## Правило (обязательно)

При любом обновлении обложки для Дзена:

1. **Новое имя файла** с version suffix, напр. `{slug}-cover-dzen-v4.png` (не `-cover.png` / `-cover-1.png`).
2. Загрузить **full** + **`-1024x576`** intermediate (и другие WP sizes при необходимости).
3. Обновить WP: featured image, первый `<img>` в контенте, OG meta → **новые** URL.
4. **guid поста не менять** — иначе Дзен создаст дубликат.
5. Bump `post_modified_gmt`.
6. Проверить `/feed/zen/`: строка enclosure **должна измениться**.

## Скрипт

```bash
PYTHONPATH=scripts python3 scripts/excalibur_blog_dzen_cover_cache_bust.py
PYTHONPATH=scripts python3 scripts/excalibur_blog_dzen_cover_cache_bust.py --slug <slug> --version-suffix dzen-v4
PYTHONPATH=scripts python3 scripts/excalibur_blog_dzen_cover_cache_bust.py --slug <slug> --upload-subdir 2026/09 --old-cover-remote <slug>-cover.png
PYTHONPATH=scripts python3 scripts/excalibur_blog_dzen_cover_cache_bust.py --verify-only
```

Транспорт: **SFTP primary** (`excalibur_blog_wp_publish.publish_via_sftp`).

## Aug-22 batch (v3)

| slug | old enclosure fragment | new fragment |
|------|------------------------|--------------|
| dogovor-arendy-pravila-prozhivaniya-posutochno | `…-cover-1-1024x576.png` | `…-cover-dzen-v3-1024x576.png` |
| otmena-bronirovaniya-posutochno-vozvrat-predoplaty | `…-cover-1024x576.png` | `…-cover-dzen-v3-1024x576.png` |
| pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti | `…-cover-1024x576.png` | `…-cover-dzen-v3-1024x576.png` |
| zabroniroval-posutochno-vyyasnilos-kvartira-v-subarende | `…-cover-2-1024x576.png` | `…-cover-dzen-v3-1024x576.png` |

Отчёт: `memory/blog/dzen-cover-cache-bust-report.json`.

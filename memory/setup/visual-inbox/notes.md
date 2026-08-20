# Visual inbox — Добрый дом

Дата: 2026-08-20

## cover_mode

`logo_lockup` — логотип «Добрый дом» на **всех 8** изображениях (cover + 7 inlines). **Нет** locked host face.

## Logo lockup

Официальный логотип уже в репозитории:
- `memory/cover/assets/brand/logo-dobry-dom.png`
- WP media: `blog-hero.json` → `reference_url_hosted`

Для обновления логотипа положите `logo-dobry-dom.png` сюда и выполните:

```bash
python3 scripts/excalibur_blog_identity_real.py --stage-from-inbox
python3 scripts/excalibur_blog_hero_reference_url.py --force
```

## Identity-real (НЕ использовать)

`identity-real/` — **отключён** для Добрый дом. Не загружать Shakin/face-studio photos.

## Longform

Обложка + 7 inline-quad. 2× quad-canvas 2K (Derouter REST). Logo на каждом кадре.

## Запреты

Shakin identity lock, host_reference mode, decorative-only inline, missing logo on any of 8.

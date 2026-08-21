# Cover assets — Добрый дом

Локальные референсы для `cover_mode=brand_logo_paste`. Чужие CDN/catbox не использовать для бренда.

## Official logo (PRIMARY — factory paste only)

| Файл | Роль |
|------|------|
| `brand/logo-dobry-dom.png` | **Единственный** allowed lockup — alpha PNG, 1:1 paste после генерации |

**NEVER** просить image model нарисовать логотип, wordmark, curtains+flower, dashed frame или gold house.
Factory paste: `scripts/excalibur_blog_brand_logo_composite.py` → TOP-RIGHT 8–12% на cover + 2–3 inline.

Legacy alias `brand/dobry-dom-logo.png` — тот же файл (backward compat).

Hosted URL: `blog-hero.json` → `reference_url_hosted` (WP media on добрыйдом-72.рф).

## Identity-real (DISABLED)

`identity-real/` — **не используется** для Добрый дом. NO Shakin / face-studio identity lock.

## Scene composition only (NOT face)

`scene-composition-only/hero-ref-*.jpg` — AI mood refs. **Запрещено** как FACE source.

## Longform

8 изображений: cover + 7 inline. 2× quad-canvas 2K (Derouter REST) → split 2×2.

Logo paste: cover always + **2–3 of 7** inlines (default inline_1, inline_3, inline_7). Inline = utility info-graphics.

Inbox: `memory/setup/visual-inbox/` (logo updates → copy to `brand/logo-dobry-dom.png`).

## Запреты

Shakin/face-studio identity lock, plastic/uncanny face, AI hero-ref как лицо, decorative-only inline,
AI-drawn «Добрый дом» lockup in generation, logo on all 7 inlines, 2+ logos per frame.

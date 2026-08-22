# Cover assets — Добрый дом

Локальные референсы для `cover_mode=brand_logo_paste`. Чужие CDN/catbox не использовать для бренда.

## Official logo (PRIMARY — factory paste only)

| Файл | Роль |
|------|------|
| `brand/logo-dobry-dom.png` | **Единственный** allowed lockup — alpha PNG overlay после генерации (без белой/серой подложки) |

**Источник (LOCKED):** `wp-content/uploads/2026/03/cropped-img_7143.png`

**Канон:** alpha only — `prepare_logo_rgba` crop `getbbox()`, `alpha_composite` onto scene.  
**NEVER** redraw, **NEVER** white/gray plate/card/tablichka behind lockup.

**NEVER** просить image model нарисовать логотип, wordmark, curtains+flower, dashed frame, gold house **или белую/серую табличку/карточку/подложку** под logo pad.
Factory paste: `scripts/excalibur_blog_brand_logo_composite.py` → TOP-RIGHT 8–12% на cover + 2–3 inline.

Legacy alias `brand/dobry-dom-logo.png` — тот же файл (backward compat).

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
AI-drawn «Добрый дом» lockup in generation, logo on all 7 inlines, 2+ logos per frame,
white/gray rectangular plate under logo pad.

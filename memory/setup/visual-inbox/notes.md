# Visual inbox — The Риэлтор

Дата: 2026-08-18 (обновлено: identity-real)

## cover_mode

`host_reference` — на обложке **Святослав Шакин** (узнаваемое лицо, 28 лет).

## Identity lock (live photos ONLY)

Положите **оригинальные бинарники** (не AI) с точными именами:

- `face-hoodie-airpods.jpeg` — крупный план, родинки (PRIMARY)
- `face-office-selfie.jpeg` — селфи, серая футболка
- `face-greenhouse-yahweh.png` — оранжерея, YAHWEH (likeness only)
- `face-immortal-regiment.jpeg` — только лицо (не клонировать сцену)

После загрузки:

```bash
python3 scripts/excalibur_blog_identity_real.py --stage-from-inbox
```

Копии остаются здесь; канон — `memory/cover/assets/identity-real/`.

**Важно:** вложения в чат Cloud Agent **не сохраняются** на диск VM — кладите файлы в этот каталог через workspace (drag-and-drop), не только в сообщение.

## Scene composition (NOT face)

`scene-composition-only/` в assets — AI hero-ref для mood. **Не** использовать как лицо.

## Emotion bank

6 эмоций в `blog-hero.json`; каждый кадр — другая поза/сцена.

## Longform

Обложка + 7 inline-quad. 2× quad-canvas 2K (mcp-derouter).

## Запреты

AI-reconstructed faces, plastic look, клон референсных сцен, pink-cat, EXCALIBUR, белое худи.

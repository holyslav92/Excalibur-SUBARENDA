# Cover assets — The Риэлтор

Локальные референсы для `cover_mode=host_reference`. Чужие CDN/catbox не использовать.

## Identity lock (PRIMARY) — live photos

Каталог `identity-real/` — **единственный** source of truth для лица:

| Файл | Роль |
|------|------|
| `identity-real/face-hoodie-airpods.jpeg` | PRIMARY geometry lock |
| `identity-real/face-office-selfie.jpeg` | Round face, stubble |
| `identity-real/face-greenhouse-yahweh.png` | Full body likeness (no scene clone) |
| `identity-real/face-immortal-regiment.jpeg` | Face only (no scene clone) |

i2i **ротирует** все четыре (`blog-hero.json` → `i2i_reference_rotation`).

## Scene composition only (NOT face)

`scene-composition-only/hero-ref-*.jpg` — AI mood refs. **Запрещено** как FACE source.

## Legacy likeness (secondary, not primary)

| Файл | Роль |
|------|------|
| `portrait.jpg` | Старый full-body navy blazer (сайт) |
| `portrait-landing.jpg` | Поясной, сумерки |
| `portrait-640.webp` | Webp |

## Emotion bank

Cover выбирает одну эмоцию на статью; **новая** поза/сцена каждый раз.

## Longform

8 изображений: cover + 7 inline. 2× quad-canvas 2K (mcp-derouter) → split 2×2.

Inbox: `memory/setup/visual-inbox/` (копии identity-real + logo).

## Запреты

Чужое лицо, plastic/uncanny face, AI hero-ref как лицо, pink-cat, белое худи, клон любой референсной сцены.

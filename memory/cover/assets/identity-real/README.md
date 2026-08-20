# Identity-real — live photos (SOURCE OF TRUTH)

## FACE (единственный i2i source)

| Файл | Роль |
|------|------|
| `face-studio-2026-06-23.jpg` | **face_primary** — ONLY `/images/edits` input; jaw, stubble, hairline, eyes |

Live URL: `https://tymenrieltor.ru/wp-content/uploads/2026/06/2026-06-23-15.57.42.jpg`

## Body / scene (НЕ лицо)

| Файл | Роль |
|------|------|
| `face-hoodie-airpods.jpeg` | `body_build_only` — medium-slim build, не FACE |
| `face-office-selfie.jpeg` | `body_build_only` — medium-slim build, не FACE |
| `face-greenhouse-yahweh.png` | `scene_composition_only` — не FACE, не клонировать оранжерею |
| `face-immortal-regiment.jpeg` | `scene_composition_only` — не FACE, не клонировать марш |

Копии держать в `memory/setup/visual-inbox/`.

## i2i

`pick_identity_reference()` → **всегда** `face-studio-2026-06-23.jpg` (без ротации).

## Запрещено как FACE source

- hoodie / office / greenhouse / regiment (см. роли выше)
- `scene-composition-only/hero-ref-*.jpg`
- `portrait.jpg` / `portrait-landing.jpg`

## Staging

```bash
python3 scripts/excalibur_blog_identity_real.py --stage-from-inbox
python3 scripts/excalibur_blog_identity_real.py --check
```

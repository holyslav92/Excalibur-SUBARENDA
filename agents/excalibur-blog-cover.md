---
name: excalibur-blog-cover
description: "④a Cover: 2× quad canvas Derouter REST 2K, light/meme/Wordstat, logo lockup, anti-repeat."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский · **Шаг:** ④a (параллель с `excalibur-blog-schema`)

## Канон (читать первым)

- `memory/cover/cover-canon.json` — light/bright, мемы, Wordstat stickers, logo lockup, anti-repeat 14д
- `skills/cover-excalibur-blog/SKILL.md`
- `shared/blog-cover-quad-canvas-contract.md`

**REJECTED навсегда (daypart formula):** morning desk+document / day street / evening close talk / night split — не использовать.

## Роль

Cover генерирует **2×** quad-холста 2×2 (**Derouter REST** + `DEROUTER_IMAGE_MODEL`, api-direct 2K PRIMARY) → `cover.png` + `inline-01…07.png`.

Каждая обложка **изобретается с нуля** (surprise, variety). Anti-repeat: `memory/cover/used-motifs.json`.

## Вход

- `article.html` + Sol PASS + `cover/cover-text.json` gate PASS
- `research-notes.md` / handoff — **Wordstat фразы** для stickers
- `memory/cover/blog-hero.json`, `cover-design-code.json`, `quad-style-dobry-dom.json`
- `memory/cover/assets/brand/logo-dobry-dom.png` — официальный логотип

## Cover agent обязан

1. **Изобрести** новую сцену: composition, location, meme, props, stickers, joke — не из inventory.
2. Заполнить `cover_motifs` в `quad-manifest.json` и пройти motif gate.
3. **Light & bright:** sun flare, light leak, glow, airy #FFFFFF — teal curtains + terracotta accents; no dark cinematic.
4. **Logo lockup:** логотип «Добрый дом» на **всех 8** изображениях (cover + 7 inlines) — читаемый corner lockup, не гигантский watermark.
5. **Мемы:** meme cat + catalog people-meme **small stickers** on cover; inline = infographic; no co-host/stock man.
6. **1–3 Wordstat stickers** — live high-frequency RU queries (Тюмень/область), из research/handoff.
7. **NO host face / NO Shakin identity** — люди по теме статьи OK (гости, семьи, уборщики), но без identity lock.

## Пайплайн

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_hero_reference_url.py
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge

# quad-manifest.json: scene_hint, cover_motifs, wordstat_stickers (1-3 phrases)
python3 scripts/excalibur_blog_cover_motif_gate.py check \
  --topic-id <id> --composition "..." --location "..." --meme "..." ...

python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json --fallback-kie
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json --fallback-kie

python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html

python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> --composition "..." ...
```

## quad-manifest.json (добавить)

```json
{
  "cover_motifs": {
    "composition": "…",
    "location": "…",
    "meme": "…",
    "prop_set": "…",
    "sticker_set": "…",
    "joke": "…"
  },
  "wordstat_stickers": ["фраза из Wordstat 1", "фраза 2"]
}
```

## Longform слоты

| Canvas | Слоты |
|--------|-------|
| 1 | cover, inline_1…3 |
| 2 | inline_4…7 |

## Inline utility (v3)

- Канон: `memory/cover/inline-visual-types.json`
- **Тест пользы:** каждый inline учит факт/порядок/число/сравнение по H2 — FAIL если decorative-only или ряд иконок+3 слова
- **Logo lockup** на каждом inline
- **NO host face / NO Shakin** на inline
- Cover-text labels = **факты** из статьи, не слоганы
- Cover-QA checks: `logo_lockup_all_8`, `inline_utility_all_7`, `inline_no_decorative_only`

## Blockers

| Код | Причина |
|-----|---------|
| COVER MOTIF BLOCKER | collision 14-day anti-repeat |
| LOGO BLOCKER | нет logo-dobry-dom.png / reference_url |
| DEROUTER API KEY MISSING / DEROUTER BLOCKER / KIE API BLOCKER | нет canvas URL/local_path после 2K |
| IMAGE MODEL BLOCKER | Flux/Seedream/nano_banana/z-image или off-pipeline demo |
| COVER STYLE BLOCKER | dark cinematic, daypart formula, inventory default props, decorative-only inline |

## Fragment

`.cursor/excalibur-blog-fragments/cover.md` — `status: PASS|BLOCKER`, artifacts: cover + inline-01…07.

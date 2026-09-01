---
name: excalibur-blog-cover
description: "④a Cover: ONE Grsai 2K 2×2 grid → slice 4 + pixel-faithful logo paste on cover tile only."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский · **Шаг:** ④a (параллель с `excalibur-blog-schema`)

## Канон (читать первым)

- `memory/cover/cover-canon.json` → `dobry_dom_one_2k_slice4_v1`
- `skills/cover-excalibur-blog/SKILL.md`
- `shared/blog-cover-quad-canvas-contract.md`

**REJECTED навсегда (daypart formula):** morning desk+document / day street / evening close talk / night split — не использовать.

## Роль

Cover делает **ONE** Grsai draw 2048×1152 как **2×2 grid** → mechanical slice → `cover.png` + `inline-01…03.png` (4 images total).

Каждая обложка **изобретается с нуля** (surprise, variety). Anti-repeat: `memory/cover/used-motifs.json`.

## Вход

- `article.html` + Sol PASS + `cover/cover-text.json` gate PASS
- `research-notes.md` / handoff — **Wordstat фразы** для inline labels
- `memory/cover/blog-hero.json`, `cover-design-code.json`, `cover-canon.json`
- `memory/cover/assets/brand/logo-dobry-dom.png` (`cropped-img_7143.png`) — **единственный** allowed lockup (factory paste pixel-faithful, native aspect, NOT square)

## HARD BAN — never ship model-drawn logo

Image model **NEVER** renders final brand: «Добрый дом» wordmark, green curtains+red flower icon, dashed logo frame,
gold house-with-heart, subtitle «УЮТНЫЕ КВАРТИРЫ В АРЕНДУ», any brand lockup.
Cover panel may reserve **top-right pad** (8–12% width). **AFTER slice**, factory pastes official PNG on **cover tile ONLY**:
`scripts/excalibur_blog_brand_logo_composite.py`.

**FORBIDDEN:** square crop of logo file; white/gray plaque; logo on inline tiles; second Grsai draw; 8-frame batch.

## Cover agent обязан

1. **Изобрести** новую сцену: composition, location, props, stickers — не из inventory.
2. Заполнить `cover_motifs` в `quad-manifest.json` и пройти motif gate.
3. **Light & bright:** airy Comfort+ Tyumen daily-rental; no dark cinematic.
4. **Factory logo paste:** **cover tile only** — official PNG top-right 8–12%, **pixel-faithful native aspect**.
5. **Inlines:** three distinct article scenes — **ZERO** company lockup.
6. **1–3 Wordstat stickers** на inline panels — live high-frequency RU queries (Тюмень/область).
7. **NO host face / NO Shakin identity** — люди по теме статьи OK, но без identity lock.

## Пайплайн

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge

python3 scripts/excalibur_blog_cover_motif_gate.py check \
  --topic-id <id> --composition "..." --location "..." --meme "..." ...

python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/slice4-mcp-batch.json --result cover/slice4-mcp-result.json

python3 scripts/excalibur_blog_cover_quad_split.py --article-dir "$ARTICLE" --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_slice4_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"

python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> --composition "..." ...
```

## Longform слоты (slice4)

| Panel | Output |
|-------|--------|
| top-left [0] | cover.png |
| top-right [1] | inline-01.png |
| bottom-left [2] | inline-02.png |
| bottom-right [3] | inline-03.png |

## Blockers

| Код | Причина |
|-----|---------|
| COVER MOTIF BLOCKER | collision 14-day anti-repeat |
| LOGO BLOCKER | нет logo-dobry-dom.png / square crop / plaque / composite stamp FAIL |
| SLICE4 BLOCKER | second draw / 8-frame batch / logo on inline |
| GRSAI API KEY MISSING / GRSAI BLOCKER | нет canvas URL/local_path после 2K |
| COVER STYLE BLOCKER | dark cinematic, daypart formula, inventory default props |

## Fragment

`.cursor/excalibur-blog-fragments/cover.md` — `status: PASS|BLOCKER`, artifacts: cover + inline-01…03.

---
name: cover-excalibur-blog
description: "④a Cover: scene-only hallway 2K + factory poster composite (type/meme/phone) + 2× inline quads."
---

# Cover Agent — longform 8 images (scene_composite_v1)

## Philosophy

**COVER = empty tender-light hallway (Grsai scene-only)** + factory poster composite: Cormorant SemiBold Italic + Onest ~860 headline, exactly ONE catalog meme PNG paste, kitchen-tablo phone +7 (993) 574-83-22, official alpha logo overlay AFTER.

**INLINES unchanged** — 2× quad designed grid; meme optional (max 1 cat/article); ZERO company logos on inlines.

**HARD BAN on COVER:** overlapping type layers, magnified letter crops, Trade Offer/Drake/Wojak drawn by model, collage stickers on headline, white/gray plaque under logo, model-drawn lockup, 0/2+ memes, people-heavy scene, phone pill, model-drawn logo.

## Generation policy (HARD)

| Rule | Value |
|------|-------|
| Cover canvas | **Scene-only** 2048×1152 → poster composite → `cover.png` 1200×675 |
| Inline canvases | 2× quad 2048×1152 (inline_1..4, inline_5..7) |
| Provider | **Grsai** — PRIMARY_MODEL_ID only |
| VIP retry | **disabled** |
| Max attempts | **2** per canvas → pad-clear + poster composite + logo paste if needed |
| Prose/scene | Derouter Terra `--role cover-scene` only |

## Архитектура

```text
scene-only cover canvas 2048×1152 (Grsai, max 2 attempts — ZERO text/meme/phone/logo)
  → cover_standalone_apply.py → resize + pad-clear
  → cover_poster_composite.py → Cormorant+Onest type + 1 meme PNG + kitchen-tablo phone
2× quad canvas 2048×1152
  canvas 1: inline_1..4
  canvas 2: inline_5..7
→ split 2×2 → inline-01..07.png
→ brand_logo_composite.py (logo overlay ONLY — no phone pill)
→ Cover-QA slim (anti-collage gates) → Indexer
```

## Brand lock

- **NEVER** logo as Grsai reference
- Empty **top-right pad 8–12%** in generation
- **AFTER poster composite:** factory pastes official alpha PNG
- Phone **+7 (993) 574-83-22** drawn by `cover_poster_composite.py` on cream/sage kitchen-tablo — never in Grsai generation, never pill from brand_logo_composite

## Anti-collage gates (HARD — FAIL if broken)

- 2+ large overlapping text blocks
- Giant cropped glyph >12% canvas
- TRADE OFFER / Drake / Wojak template drawn by model
- Scene canvas with model typography/meme/phone before poster composite

## Meme rotation (HARD)

- Catalog: `memory/cover/meme-top100.json` (≥60 ids, topic tags)
- Used log: `memory/cover/meme-used.json` — skip last **8** cover meme ids
- Picker: `python3 scripts/excalibur_blog_meme_rotate.py pick --manifest <article>/cover/quad-manifest.json`
- **Paste** `memory/cover/memes/<id>.png` — never draw meme in Grsai

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> \
  --composition "..." --location "..." --prop-set "..."
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/cover-mcp-batch.json --result cover/cover-mcp-result.json
python3 scripts/excalibur_blog_cover_standalone_apply.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_cover_poster_composite.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

Contract: `shared/blog-cover-quad-canvas-contract.md` · Canon: `dobry_dom_scene_composite_v1`

---
name: cover-excalibur-blog
description: "④a Cover: standalone type+meme+phone-sticker poster 2K + 2× inline quads, factory logo overlay."
---

# Cover Agent — longform 8 images (type_meme_sticker_v3)

## Philosophy

**COVER = designed magazine TYPE poster** — spectacular Cyrillic headline hero + exactly ONE catalog meme sticker + LARGE hotel-lobby information-board phone. Steal inline designed-text/grid energy — NOT people-photo scene.

**INLINES unchanged** — 2× quad designed grid; meme optional (max 1 cat/article); logo on 2–3 of 7.

**Ban on COVER:** 0 memes, 2+ memes, people-heavy scene, tiny in-scene phone, Wordstat sticker soup, torn-paper/gold-glitter/sticky collage, split white-panel+photo, phone pill, model-drawn logo, house-with-heart, logo plate.

## Generation policy (HARD)

| Rule | Value |
|------|-------|
| Cover canvas | **Standalone** 2048×1152 → `cover.png` 1200×675 |
| Inline canvases | 2× quad 2048×1152 (inline_1..4, inline_5..7) |
| Provider | **Grsai** — PRIMARY_MODEL_ID only |
| VIP retry | **disabled** |
| Max attempts | **2** per canvas → pad-clear + logo paste if needed |
| Prose/scene | Derouter Terra `--role cover-scene` only |

## Архитектура

```text
standalone cover canvas 2048×1152 (Grsai, max 2 attempts)
  → cover_standalone_apply.py → cover.png 1200×675
2× quad canvas 2048×1152
  canvas 1: inline_1..4
  canvas 2: inline_5..7
→ split 2×2 → inline-01..07.png
→ brand_logo_composite.py (logo overlay ONLY — no phone pill)
→ Cover-QA slim → Indexer
```

## Brand lock

- **NEVER** logo as Grsai reference
- Empty **top-right pad 8–12%** in generation
- **AFTER apply:** factory pastes official alpha PNG
- Phone **+7 (993) 574-83-22** as **LARGE hotel-lobby information-board tablo** — never pill, never peel-pill, never magnet, never tiny in-scene

## Meme rotation (HARD)

- Catalog: `memory/cover/meme-top100.json` (≥60 ids, topic tags)
- Used log: `memory/cover/meme-used.json` — skip last **8** cover meme ids
- Picker: `python3 scripts/excalibur_blog_meme_rotate.py pick --manifest <article>/cover/quad-manifest.json`
- Pick by **topic-tag overlap** with article; prefer `memory/cover/memes/<id>.png` when present
- Cat memes still max **1** of 8 frames (cover+7 inlines)

## Cover prompt (NOT a template)

Each cover prompt is rebuilt from **THIS** article case: H1, bait/switch, figure, quote — unique Cyrillic punchlines, no recycled wood+Harold+peel-pill stamps.

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
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

Contract: `shared/blog-cover-quad-canvas-contract.md` · Canon: `dobry_dom_type_meme_sticker_v3`

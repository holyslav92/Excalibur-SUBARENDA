---
name: cover-excalibur-blog
description: "④a Cover: standalone scene poster 2K + 2× inline quads, factory logo overlay, phone in-scene."
---

# Cover Agent — longform 8 images (scene_poster_v2)

## Philosophy

**COVER = editorial scene poster** — designed inline energy as a full-bleed cinematic still. One glance = the guest-night wound. **NO meme/collage on cover.**

**INLINES unchanged** — 2× quad designed grid; meme allowed (max 1 cat/article); logo on 2–3 of 7.

**Ban on COVER:** meme cutouts, Wordstat sticker soup, torn-paper/gold-glitter/sticky collage, split white-panel+photo, phone pill, model-drawn logo, house-with-heart, logo plate.

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
- Phone **+7 (993) 574-83-22** **IN SCENE** — never pill

## Runbook

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

Contract: `shared/blog-cover-quad-canvas-contract.md` · Canon: `dobry_dom_scene_poster_v2`

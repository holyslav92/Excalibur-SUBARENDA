# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — Cover dobry_dom_dzen_story_collage_v2 + inline quads (Grsai 2K)

Cover после `article.html` + Sol PASS.

## Brand lock FOREVER (Cover-QA slim — FAIL if broken)

Canon: `memory/cover/cover-canon.json` (`dobry_dom_dzen_story_collage_v2`), `shared/tenant-config.json` → `cover_wow_rules`.

**Philosophy:** ONE Grsai primary image API generation (16:9, ≥2048×1152, non-VIP, max 2 gens) produces the **COMPLETE** cover — photoreal Dzen story-collage scene + Cyrillic two-beat H1 + yellow/peach brush on ONE keyword + one yellow sticky punch + phone +7 (993) 574-83-22 + official «Добрый дом» lockup top-right (curtains + flower + terracotta name, transparent, NO plaque). Factory ships PNG as-is (resize/thumb only). **NO** `excalibur_blog_cover_poster_composite.py`. **NO** `excalibur_blog_brand_logo_composite.py` on cover.

**REPLACES** `dobry_dom_dzen_story_collage_v1` scene-only + factory overlay. Do NOT require empty cream hallway + catalog meme as the layout.

### HARD anti-collage gates (FAIL if broken — kept)

- 2+ large overlapping text blocks
- Giant cropped glyph >12% canvas (magnified letter crops like «тно» / «баума»)
- TRADE OFFER / Drake / Wojak template drawn by model
- Overlapping type layers, collage stickers covering headline, white/gray plaque under logo
- WordPress UI, empty hallway default, realtor phone +7 922

### Logo — drawn IN generation (NEVER factory paste on cover)

- Model MUST draw/integrate official «Добрый дом» lockup small top-right: curtains + flower + terracotta name.
- Transparent integrated look — **NO** white/gray/beige plaque/square under logo.
- Logo PNG reference is **optional** and **never required**; if used, must not cause plaque paste.
- **NEVER** run `excalibur_blog_brand_logo_composite.py` after cover generation.
- Cover: one integrated logo. Inlines: **0 of 7** (default).

### Phone — IN generation

- Number **+7 (993) 574-83-22** only (never +7 922).
- Phone drawn IN Grsai generation — readable at Dzen thumb.
- **NEVER** factory post-composite phone bar/pill from `excalibur_blog_cover_poster_composite.py`.

### COVER MUST (dobry_dom_dzen_story_collage_v2)

1. **Story collage scene** from Grsai — photoreal bright apartment/context; hero varies by THIS case.
2. **Two-beat Cyrillic headline** — Onest ~860 black; yellow/peach brush on ONE keyword — IN generation.
3. **Yellow sticky note** — one short punch — IN generation.
4. **Phone** +7 (993) 574-83-22 — IN generation.
5. **«Добрый дом» lockup** top-right — IN generation, no plaque.

### COVER BAN

Empty hallway as required layout, factory poster composite, factory logo PNG paste, overlapping text blocks, magnified letter crops, Trade Offer/Drake/Wojak templates, logo plate, phone pill, WordPress UI, 2+ memes, realtor +7 922.

## Longform: 8 изображений

- `cover.png` 1200×675 (from standalone `cover-canvas.png` 2048×1152)
- `inline-01.png` … `inline-07.png` (7× `figure.inline-quad`)
- **1 standalone cover canvas** + **2 inline quad canvases** `2048×1152` (2×2)

| Canvas | Файл | Слоты |
|--------|------|-------|
| 0 (cover) | `cover/cover-canvas.png` | full Grsai editorial 16:9 |
| 1 | `cover/canvas-quad-01.png` | inline_1…inline_4 |
| 2 | `cover/canvas-quad-02.png` | inline_5…inline_7 + quiet pad (not exported) |

PRIMARY: **Grsai** (`GRSAI_API_KEY`), `resolution: 2K`, 16:9, **vip disabled**, max **2** attempts.

## Workflow

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_quad_manifest.py --article-dir <dir> --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> --composition "..." ...
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir <dir> --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/cover-mcp-batch.json --result cover/cover-mcp-result.json
python3 scripts/excalibur_blog_cover_standalone_apply.py --article-dir <dir>
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

## Blockers

- `COVER QA BLOCKER` — missing headline/phone in generation, overlapping text blocks, giant glyph crop, model-drawn Trade Offer, phone pill, logo plate, WordPress UI
- `forbid_overlapping_text_blocks` / `forbid_giant_cropped_glyph` / `forbid_model_drawn_meme_template` on cover.png
- Empty hallway + blinking_white_guy as **required** layout — REJECTED; hero must be theme-derived
- `poster-composite-stamp.json` / `logo-composite-stamp.json` — **NOT required** on cover (factory overlay disabled)

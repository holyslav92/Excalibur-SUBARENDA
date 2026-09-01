# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — Cover scene_composite_v1 + inline quads (Grsai 2K)

Cover после `article.html` + Sol PASS.

## Brand lock FOREVER (Cover-QA slim — FAIL if broken)

Canon: `memory/cover/cover-canon.json` (`dobry_dom_scene_composite_v1`), `shared/tenant-config.json` → `cover_wow_rules`.

**Philosophy:** Grsai generates ONLY empty tender-light hallway. Factory post-process: Cormorant SemiBold Italic + Onest ~860 headline, exactly ONE catalog meme PNG paste, kitchen-tablo phone +7 (993) 574-83-22, official alpha logo overlay AFTER — never as model reference. INLINES = designed grid unchanged.

### HARD anti-collage gates (FAIL if broken)

- 2+ large overlapping text blocks
- Giant cropped glyph >12% canvas (magnified letter crops like «тно» / «баума»)
- TRADE OFFER / Drake / Wojak template drawn by model (meme must be pasted PNG only)
- Overlapping type layers, collage stickers covering headline, white/gray plaque under logo, model-drawn lockup

### Logo — NEVER draw in generation

- Prompt MUST reserve **empty clear top-right corner 8–12%**: no logo, no house icon, no «Добрый дом» lettering, no plate.
- **NEVER** send `cropped-img_7143.png` / `logo-dobry-dom.png` as Grsai reference.
- **AFTER** standalone cover apply: factory pastes official alpha PNG — `scripts/excalibur_blog_brand_logo_composite.py`.
- Cover: logo always. Inlines: **2–3 of 7** (default inline_1/3/7).
- **GATE fail:** white/gray/beige plate under logo; logo over headline/phone.

### Phone — kitchen-tablo factory post-composite

- Number **+7 (993) 574-83-22** only (never +7 922).
- Phone is drawn by `excalibur_blog_cover_poster_composite.py` on cream/sage kitchen-tablo — NOT in Grsai generation.
- **Do NOT** post-paste pill/button/banner/chip from brand_logo_composite.
- **GATE fail:** phone pill; model-drawn phone in scene canvas; missing tablo after poster composite.

### COVER MUST (scene_composite_v1)

1. Empty tender-light hallway scene from Grsai (no Cyrillic/digits/meme/logo/phone in generation).
2. Factory headline L1 Cormorant SemiBold Italic terracotta + L2 Onest ~860 charcoal — unique per article case.
3. Exactly ONE catalog meme PNG pasted from `memory/cover/memes/<id>.png` / meme-top100.json.
4. Kitchen-tablo phone +7 (993) 574-83-22 drawn by poster composite.
5. Official alpha logo PNG overlay top-right AFTER poster composite.
6. Default ZERO people.

### COVER BAN (keep legacy fails)

0 memes, 2+ memes / meme soup, people-heavy group photo, Wordstat sticker soup, torn-paper/gold-glitter/sticky collage, split white-panel+photo, phone pill, model-drawn logo, house-with-heart, logo plate, empty stock, WP UI, overlapping text blocks, magnified letter crops, Trade Offer/Drake/Wojak drawn, collage stickers on headline.

## Longform: 8 изображений

- `cover.png` 1200×675 (from standalone `cover-canvas.png` 2048×1152)
- `inline-01.png` … `inline-07.png` (7× `figure.inline-quad`)
- **1 standalone cover canvas** + **2 inline quad canvases** `2048×1152` (2×2)

| Canvas | Файл | Слоты |
|--------|------|-------|
| 0 (cover) | `cover/cover-canvas.png` | empty scene-only hallway 16:9 |
| 1 | `canvas-quad-01.png` | inline_1…inline_4 |
| 2 | `canvas-quad-02.png` | inline_5…inline_7 + quiet pad (not exported) |

PRIMARY: **Grsai** (`GRSAI_API_KEY`), `resolution: 2K`, 16:9, **vip disabled**, max **2** attempts.

## Cover canon (Добрый дом scene_composite_v1)

1. **Scene-only hallway** — Grsai empty tender-light scene; no Cyrillic/digits/meme/logo/phone.
2. **Factory poster composite** — Cormorant+Onest type, 1 meme PNG paste, kitchen-tablo phone.
3. **Brand logo paste** — NO logo in generation; factory pastes PNG TOP-RIGHT 8–12% AFTER poster composite.
4. **Anti-repeat 14д** — `memory/cover/used-motifs.json`.
5. **Meme rotation 8** — `memory/cover/meme-used.json` + `scripts/excalibur_blog_meme_rotate.py`.
5. **Light & bright** — natural daylight; dark cinematic запрещён.
6. **REQUIRED meme on cover** — exactly ONE from meme-top100.json; inlines may add more (max 1 cat/article total).
7. **NO people-heavy scene** — default zero people on cover.

## Workflow

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_quad_manifest.py --article-dir <dir> --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> --composition "..." ...
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir <dir> --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/cover-mcp-batch.json --result cover/cover-mcp-result.json
python3 scripts/excalibur_blog_cover_standalone_apply.py --article-dir <dir>
python3 scripts/excalibur_blog_cover_poster_composite.py --article-dir <dir>
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir <dir>
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

## Blockers

- `COVER QA BLOCKER` — missing headline/meme/phone after poster composite, overlapping text blocks, giant glyph crop, model-drawn Trade Offer, people-heavy scene, phone pill, logo plate, missing poster-composite-stamp.json
- `forbid_overlapping_text_blocks` / `forbid_giant_cropped_glyph` / `forbid_model_drawn_meme_template` on cover.png

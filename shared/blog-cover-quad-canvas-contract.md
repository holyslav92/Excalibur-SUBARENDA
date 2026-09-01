# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — Cover dobry_dom_dzen_story_collage_v1 + inline quads (Grsai 2K)

Cover после `article.html` + Sol PASS.

## Brand lock FOREVER (Cover-QA slim — FAIL if broken)

Canon: `memory/cover/cover-canon.json` (`dobry_dom_dzen_story_collage_v1`), `shared/tenant-config.json` → `cover_wow_rules`.

**Philosophy:** Grsai generates photoreal Dzen click-thumbnail **story collage** (hero varies by article theme — person, objects, or key detail). Factory post-process: Onest ~860 black two-beat headline + yellow/peach brush highlight on ONE keyword, ONE yellow sticky-note punch, phone bar +7 (993) 574-83-22, optional catalog meme PNG paste, official alpha logo overlay AFTER — never as model reference. INLINES = designed grid unchanged.

**REPLACES** `dobry_dom_scene_composite_v1` empty-hallway-only default. Do NOT require empty cream hallway + catalog meme as the layout.

### HARD anti-collage gates (FAIL if broken — kept from scene_composite)

- 2+ large overlapping text blocks
- Giant cropped glyph >12% canvas (magnified letter crops like «тно» / «баума»)
- TRADE OFFER / Drake / Wojak template drawn by model (meme must be pasted PNG only when used)
- Overlapping type layers, collage stickers covering headline, white/gray plaque under logo, model-drawn lockup

### Logo — NEVER draw in generation

- Prompt MUST reserve **empty clear top-right corner 8–12%**: no logo, no house icon, no «Добрый дом» lettering, no plate.
- **NEVER** send `cropped-img_7143.png` / `logo-dobry-dom.png` as Grsai reference.
- **AFTER** standalone cover apply: factory pastes official alpha PNG — `scripts/excalibur_blog_brand_logo_composite.py`.
- Cover: logo always. Inlines: **0 of 7** (default).
- **GATE fail:** white/gray/beige plate under logo; logo over headline/phone.

### Phone — factory post-composite phone bar

- Number **+7 (993) 574-83-22** only (never +7 922).
- Phone is drawn by `excalibur_blog_cover_poster_composite.py` as bottom phone bar — NOT in Grsai generation.
- **Do NOT** post-paste pill/button/banner/chip from brand_logo_composite.
- **GATE fail:** phone pill; model-drawn phone in scene canvas; missing phone bar after poster composite.

### COVER MUST (dobry_dom_dzen_story_collage_v1)

1. **Story collage scene** from Grsai — photoreal bright apartment/context; hero varies by THIS case (person OR objects OR story detail); NOT default empty hallway; no Cyrillic/digits/meme/logo/phone in generation.
2. Factory headline — Onest ~860 black two beats; yellow/peach brush highlight behind ONE keyword.
3. Factory yellow sticky note — one short punch line (Cyrillic).
4. Phone bar +7 (993) 574-83-22 drawn by poster composite.
5. Optional: ONE catalog meme PNG pasted when manifest picks id.
6. Official alpha logo PNG overlay top-right AFTER poster composite.

### COVER BAN

Empty hallway as required layout, always blinking_white_guy/roll_safe meme, magazine empty interior poster, 2+ memes / meme soup, people-heavy group photo, Wordstat sticker soup, gold-glitter/sticky soup in generation, phone pill, model-drawn logo, house-with-heart, logo plate, empty stock, WP UI, overlapping text blocks, magnified letter crops, Trade Offer/Drake/Wojak drawn, collage stickers on headline.

## Longform: 8 изображений

- `cover.png` 1200×675 (from standalone `cover-canvas.png` 2048×1152)
- `inline-01.png` … `inline-07.png` (7× `figure.inline-quad`)
- **1 standalone cover canvas** + **2 inline quad canvases** `2048×1152` (2×2)

| Canvas | Файл | Слоты |
|--------|------|-------|
| 0 (cover) | `cover/cover-canvas.png` | story collage scene 16:9 |
| 1 | `canvas-quad-01.png` | inline_1…inline_4 |
| 2 | `canvas-quad-02.png` | inline_5…inline_7 + quiet pad (not exported) |

PRIMARY: **Grsai** (`GRSAI_API_KEY`), `resolution: 2K`, 16:9, **vip disabled**, max **2** attempts.

## Cover canon (Добрый дом dzen_story_collage_v1)

1. **Story collage scene** — Grsai photoreal case scene; hero theme-derived; no Cyrillic/digits/meme/logo/phone in generation.
2. **Factory poster composite** — Onest headline + brush highlight + sticky note + phone bar (+ optional meme paste).
3. **Brand logo paste** — NO logo in generation; factory pastes PNG TOP-RIGHT 8–12% AFTER poster composite.
4. **Anti-repeat 14д** — `memory/cover/used-motifs.json`.
5. **Meme rotation 8** — `memory/cover/meme-used.json` + `scripts/excalibur_blog_meme_rotate.py` (optional on cover).
6. **Light & bright** — natural daylight; dark cinematic запрещён.
7. **Cat optional** — max 1 across cover+7 inlines.

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

- `COVER QA BLOCKER` — missing headline/phone after poster composite, overlapping text blocks, giant glyph crop, model-drawn Trade Offer, phone pill, logo plate, missing poster-composite-stamp.json
- `forbid_overlapping_text_blocks` / `forbid_giant_cropped_glyph` / `forbid_model_drawn_meme_template` on cover.png
- Empty hallway + blinking_white_guy as **required** layout — REJECTED; hero must be theme-derived

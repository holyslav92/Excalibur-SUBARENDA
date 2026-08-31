# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — Cover type+meme+phone-sticker v3 + inline quads (Grsai 2K)

Cover после `article.html` + Sol PASS.

## Brand lock FOREVER (Cover-QA slim — FAIL if broken)

Canon: `memory/cover/cover-canon.json` (`dobry_dom_type_meme_sticker_v3`), `shared/tenant-config.json` → `cover_wow_rules`.

**Philosophy:** COVER = designed magazine TYPE poster (spectacular headline + exactly 1 catalog meme + large phone sticker). Steal inline designed-text/grid energy — NOT people-photo scene. INLINES = designed grid unchanged.

### Logo — NEVER draw in generation

- Prompt MUST reserve **empty clear top-right corner 8–12%**: no logo, no house icon, no «Добрый дом» lettering, no plate.
- **NEVER** send `cropped-img_7143.png` / `logo-dobry-dom.png` as Grsai reference.
- **AFTER** standalone cover apply: factory pastes official alpha PNG — `scripts/excalibur_blog_brand_logo_composite.py`.
- Cover: logo always. Inlines: **2–3 of 7** (default inline_1/3/7).
- **GATE fail:** white/gray/beige plate under logo; logo over headline/phone.

### Phone — LARGE die-cut sticker

- Number **+7 (993) 574-83-22** only (never +7 922).
- **Do NOT** post-paste pill/button/banner/chip.
- Phone MUST be **generated as ONE LARGE die-cut vinyl peel-sticker graphic** — BIG, Dzen-thumb readable.
- **NOT** tiny in-scene door/intercom number. **NOT** beige/gray UI pill.
- **GATE fail:** phone pill; tiny in-scene-only phone; post-composite overlay.

### COVER MUST (type_meme_sticker_v3)

1. Spectacular Cyrillic display headline 2–8 words as hero typography.
2. Exactly ONE named meme from `meme-top100.json` as designed sticker graphic.
3. LARGE phone die-cut sticker +7 (993) 574-83-22.
4. Default ZERO people — max tiny silhouette if case needs.

### COVER BAN (keep legacy fails)

0 memes, 2+ memes / meme soup, people-heavy group photo, Wordstat sticker soup, torn-paper/gold-glitter/sticky collage, split white-panel+photo, phone pill, model-drawn logo, house-with-heart, logo plate, empty stock, WP UI.

## Longform: 8 изображений

- `cover.png` 1200×675 (from standalone `cover-canvas.png` 2048×1152)
- `inline-01.png` … `inline-07.png` (7× `figure.inline-quad`)
- **1 standalone cover canvas** + **2 inline quad canvases** `2048×1152` (2×2)

| Canvas | Файл | Слоты |
|--------|------|-------|
| 0 (cover) | `cover/cover-canvas.png` | standalone 16:9 type poster |
| 1 | `canvas-quad-01.png` | inline_1…inline_4 |
| 2 | `canvas-quad-02.png` | inline_5…inline_7 + quiet pad (not exported) |

PRIMARY: **Grsai** (`GRSAI_API_KEY`), `resolution: 2K`, 16:9, **vip disabled**, max **2** attempts.

## Cover canon (Добрый дом type_meme_sticker_v3)

1. **Type-led magazine poster** — spectacular headline hero + 1 catalog meme + large phone sticker.
2. **Brand logo paste** — NO logo in generation; factory pastes PNG TOP-RIGHT 8–12%.
3. **Phone large sticker** — +7 (993) 574-83-22 as die-cut vinyl graphic, NOT tiny in-scene.
4. **Anti-repeat 14д** — `memory/cover/used-motifs.json`.
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
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir <dir>
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

## Blockers

- `COVER QA BLOCKER` — missing headline/meme/large phone sticker, people-heavy scene, phone pill, logo plate, missing top-right pad
- `forbid_split_white_collage` / `require_cover_meme_sticker` / `forbid_people_heavy_cover` on cover.png

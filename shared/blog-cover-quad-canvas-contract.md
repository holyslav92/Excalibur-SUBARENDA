# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — Cover scene poster v2 + inline quads (Grsai 2K)

Cover после `article.html` + Sol PASS.

## Brand lock FOREVER (Cover-QA slim — FAIL if broken)

Canon: `memory/cover/cover-canon.json` (`dobry_dom_scene_poster_v2`), `shared/tenant-config.json` → `cover_wow_rules`.

**Philosophy:** COVER = editorial scene poster (inline-quality design energy as cinematic still). INLINES = designed grid unchanged.

### Logo — NEVER draw in generation

- Prompt MUST reserve **empty clear top-right corner 8–12%**: no logo, no house icon, no «Добрый дом» lettering, no plate.
- **NEVER** send `cropped-img_7143.png` / `logo-dobry-dom.png` as Grsai reference.
- **AFTER** standalone cover apply: factory pastes official alpha PNG — `scripts/excalibur_blog_brand_logo_composite.py`.
- Cover: logo always. Inlines: **2–3 of 7** (default inline_1/3/7).
- **GATE fail:** white/gray/beige plate under logo; logo over headline/phone.

### Phone — IN scene only

- Number **+7 (993) 574-83-22** only (never +7 922).
- **Do NOT** post-paste pill/button/banner.
- Phone MUST be **generated in the artwork**: door intercom, paper on door, host card, fridge magnet — readable, in-scene.
- **GATE fail:** phone pill; post-composite overlay.

### COVER BAN (scene_poster_v2)

Meme cutouts, Wordstat sticker soup, torn-paper/gold-glitter/sticky collage, split white-panel+photo, phone pill, model-drawn logo, house-with-heart, logo plate, empty stock, WP UI.

## Longform: 8 изображений

- `cover.png` 1200×675 (from standalone `cover-canvas.png` 2048×1152)
- `inline-01.png` … `inline-07.png` (7× `figure.inline-quad`)
- **1 standalone cover canvas** + **2 inline quad canvases** `2048×1152` (2×2)

| Canvas | Файл | Слоты |
|--------|------|-------|
| 0 (cover) | `cover/cover-canvas.png` | standalone 16:9 scene poster |
| 1 | `canvas-quad-01.png` | inline_1…inline_4 |
| 2 | `canvas-quad-02.png` | inline_5…inline_7 + quiet pad (not exported) |

PRIMARY: **Grsai** (`GRSAI_API_KEY`), `resolution: 2K`, 16:9, **vip disabled**, max **2** attempts.

## Cover canon (Добрый дом scene_poster_v2)

1. **Editorial scene poster** — full-bleed cinematic still of guest-night wound; optional 2–6 word Cyrillic hook.
2. **Brand logo paste** — NO logo in generation; factory pastes PNG TOP-RIGHT 8–12%.
3. **Phone in scene** — +7 (993) 574-83-22 on door plate / host card / paper / magnet.
4. **Anti-repeat 14д** — `memory/cover/used-motifs.json`.
5. **Light & bright** — natural daylight; dark cinematic запрещён.
6. **NO memes on cover** — meme energy on inlines only (max 1 cat/article).
7. **NO Shakin/rieltor host** — Russian guests by topic only.

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

- `COVER QA BLOCKER` — collage/meme on cover, phone pill, logo plate, missing top-right pad
- `forbid_split_white_collage` / `forbid_cover_meme_collage` on cover.png

# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — Quad Canvas (Grsai / Derouter REST 2K)

Cover после `article.html` + Sol PASS.

## Brand lock FOREVER (Cover-QA slim — FAIL if broken)

Canon: `shared/tenant-config.json` → `cover_wow_rules`, `memory/cover/visual-notes-dobry-dom.json`.

**Philosophy:** beauty = agent judgment on topic; brand lock = official logo overlay + phone in scene + no plate + no WP UI.

### Logo — NEVER draw in generation

- Prompt MUST reserve **empty clear top-right corner**: no logo, no house icon, no «Добрый дом» lettering, no plate, no sticker, no business card.
- **NEVER** send `cropped-img_7143.png` / `logo-dobry-dom.png` as Grsai/Derouter generation reference (`urls`/aroma/`input_urls`).
- **AFTER** split: factory pastes official alpha PNG only — `scripts/excalibur_blog_brand_logo_composite.py`.
- Cover: logo always. Inlines: **2–3 of 7** (default inline_1/3/7). Same top-right pad.
- **GATE fail:** white/gray/beige rectangle/card/circle under logo; logo over meme/cat/sticky/headline/phone.

### Phone — IN scene only

- Number **+7 (993) 574-83-22** only (never +7 922).
- **Do NOT** post-paste pill/button/banner (`draw_phone_on_cover` forbidden).
- Phone MUST be **generated in the artwork**: tape strip, torn paper, door plate, fridge magnet, poster edge — readable, pretty, quiet zone on bottom edge or side margin.
- **GATE fail:** phone pill overlapping cat/meme/sticky/headline; opaque fill covering joke.

Factory logo paste: `scripts/excalibur_blog_brand_logo_composite.py` — logo overlay only, no phone overlay.

## Longform: 8 изображений

- `cover.png` 1200×675
- `inline-01.png` … `inline-07.png` (7× `figure.inline-quad`, data-slot `inline_1`…`inline_7`)
- **2 canvas** `2048×1152` (2×2, панели 16:9)

| Canvas | Файл | Слоты |
|--------|------|-------|
| 1 | `canvas-quad-01.png` | cover, inline_1…3 |
| 2 | `canvas-quad-02.png` | inline_4…7 |

PRIMARY: **Grsai** (`GRSAI_API_KEY`) or **Derouter REST** (`DEROUTER_API_KEY`), `resolution: 2K`, 16:9.

## Image model lock (HARD — owner)

```text
1. GRSAI_API_KEY → scripts/excalibur_blog_grsai_gpt_image2_api.py (2K, no logo reference)
2. DEROUTER_API_KEY → scripts/excalibur_blog_derouter_gpt_image2_api.py (fallback)
3. neither → BLOCKER
```

**FORBIDDEN:** logo as generation reference; post-composite phone pill; flux2-pro-*, Seedream, nano_banana*, z-image.

Contracts: `shared/grsai-gpt-image-api-contract.md`, `shared/derouter-gpt-image-api-contract.md`

## Cover canon (Добрый дом)

Канон: `memory/cover/cover-canon.json` · Style: `memory/cover/quad-style-dobry-dom.json`

1. **WOW magazine poster** — bold readable Russian display hook + scene; high-key collage.
2. **Brand logo paste** — NO logo in generation; factory pastes PNG TOP-RIGHT 8–12% on cover + 2–3 inlines.
3. **Phone in scene** — +7 (993) 574-83-22 on tape/paper/magnet, never pill overlay.
4. **Anti-repeat 14д** — `memory/cover/used-motifs.json` + `excalibur_blog_cover_motif_gate.py`.
5. **Light & bright** — high-key, sun flare; dark cinematic запрещён.
6. **Memes** — max **1 cat-meme** per article (cover OR one inline, not both); other meme slots = people-memes/reaction templates from `meme-top100.json` (≤12–15% frame); Cover-QA FAIL if 2+ cat frames.
7. **Wordstat stickers** — 1–3 readable stickers с live Wordstat (Тюмень regions 55+11176).
8. **NO Shakin/rieltor host** — Russian guests by topic only.

## Workflow

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_quad_manifest.py --article-dir <dir> --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> --composition "..." ...
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir <dir> --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir <dir>
python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> ...
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

## Visual locks (Добрый дом)

- Панели `#FFFFFF` high-key; ink `#141821`; gold `#dcc5a1` один accent
- **Cover:** WOW poster; bold Cyrillic hook; Wordstat stickers; ONE meme sticker (people-meme preferred; cat only if single cat slot); TOP-RIGHT empty logo pad; phone in-scene on bottom/side quiet zone
- **Inline (7 шт.)** — logo paste on **2–3** panels only; people-meme sticker ≤15% frame; cat-meme only if article's ONE cat slot
- Запреты: WordPress UI, logo reference in gen, phone pill overlay, overlapping logo/phone over cat/headline

## Blockers

- `COVER QA BLOCKER` — brand lock check false in `cover/cover_qa.json` or Python phone/plate gates
- logo composite stamp FAIL or inline logo count outside 2–3
- post-composite phone pill detected on cover.png

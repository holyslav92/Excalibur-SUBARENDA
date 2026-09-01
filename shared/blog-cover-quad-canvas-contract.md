# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — Cover dobry_dom_dzen_story_collage_v2 + inline quads (Grsai 2K)

Cover после `article.html` + Sol PASS.

## Brand lock FOREVER (Cover-QA slim — FAIL if broken)

Canon: `memory/cover/cover-canon.json` (`dobry_dom_dzen_story_collage_v2`), `shared/tenant-config.json` → `cover_wow_rules`.

**Philosophy:** ONE Grsai primary image API generation produces the editorial cover — photoreal Dzen story scene + Cyrillic two-beat H1 + brush + sticky + phone **IN generation**. Official logo is **NEVER invented** — pass `memory/cover/assets/brand/logo-dobry-dom.png` in Grsai `images[]` on **every** cover gen; factory **re-pastes** the same alpha PNG 1:1 top-right after gen (only allowed post-step). **NO** `excalibur_blog_cover_poster_composite.py`.

### Logo — reference + factory paste 1:1 (NEVER model-invented)

- `images[]` / `urls` MUST include official alpha PNG: `memory/cover/assets/brand/logo-dobry-dom.png` (canonical `cropped-img_7143.png`).
- Cover shows **that file 1:1** top-right 8–12% — curtains + flower + terracotta «Добрый дом».
- **NEVER** model-invented lockup, house-with-heart, extra subtitle, or second logo (`forbid_ai_drawn_logo` = true).
- **AFTER** generation: `excalibur_blog_brand_logo_composite.py` pastes same official PNG 1:1 top-right (crop getbbox, no white/gray plaque).
- Inlines: **0 of 7** company logos.

### Phone / type — IN generation only

- Cyrillic headline, sticky, phone +7 (993) 574-83-22 — drawn IN Grsai generation.
- **NEVER** factory poster composite for type/phone/sticky.

### HARD anti-collage gates (FAIL if broken)

- 2+ large overlapping text blocks, giant cropped glyph >12%, Trade Offer/Drake/Wojak templates, logo plate, WordPress UI, empty hallway default, +7 922.

## Workflow

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_quad_manifest.py --article-dir <dir> --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> --composition "..." ...
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir <dir> --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/cover-mcp-batch.json --result cover/cover-mcp-result.json
python3 scripts/excalibur_blog_cover_standalone_apply.py --article-dir <dir>
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir <dir>
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

## Blockers

- Missing `logo_reference_in_generation` / official PNG in batch `images[]`
- Missing `logo-composite-stamp.json` PASS after cover
- Model-invented logo on pre-composite canvas
- `poster-composite-stamp.json` — **NOT required** (poster overlay disabled)

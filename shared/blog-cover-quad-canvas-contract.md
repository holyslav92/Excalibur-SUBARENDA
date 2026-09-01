# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — `dobry_dom_gen_only_human_v1`

Cover после `article.html` + Sol PASS.

## Canon (HARD)

`memory/cover/cover-canon.json` → `dobry_dom_gen_only_human_v1`

**ONE Grsai primary image model draw** per article: canvas **2048×1152** prompted as **2×2 GRID** of four complete 16:9 panels → deterministic PIL quarter slice → **[0] cover + [1..3] inlines**. **ZERO** second draw. **BAN** 8-frame / quad-mcp-batch-01|02 / standalone cover-mcp.

### Logo — pixel-faithful paste on cover tile ONLY (NOT square)

- Official file: `cropped-img_7143.png` → `memory/cover/assets/brand/logo-dobry-dom.png` (curtains + red flower + terracotta «Добрый дом», RGBA alpha).
- **AFTER slice**, **cover tile only**: `excalibur_blog_brand_logo_composite.py` pastes official PNG top-right ~8–12% tile width.
- **Native aspect ratio** after `getbbox()` crop — **NOT** a square stamp of the full canvas file.
- **FORBIDDEN:** model-drawn/redrawn brand mark; white/gray plaque; logo on inline tiles.
- **NO** `excalibur_blog_cover_poster_composite.py`.

### Workflow

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_quad_manifest.py --article-dir <dir> --merge
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir <dir> --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir <dir> \
  --batch cover/slice4-mcp-batch.json --result cover/slice4-mcp-result.json
python3 scripts/excalibur_blog_cover_quad_split.py --article-dir <dir> --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir <dir>
python3 scripts/excalibur_blog_slice4_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

RSS/WP: **1 featured + 3 in-body** images.

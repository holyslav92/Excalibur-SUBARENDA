---
name: cover-excalibur-blog
description: "④a Cover: ONE Grsai 2K 2×2 grid → slice 4 (cover+3 inline) + pixel-faithful logo paste on cover tile only."
---

# Cover Agent — `dobry_dom_one_2k_slice4_v1`

## Philosophy

**ONE Grsai primary image model draw** per article: canvas **2048×1152** as **2×2 GRID** of four complete 16:9 panels → deterministic PIL quarter slice → **[0] cover + [1..3] inlines**. **ZERO** second draw. **BAN** 8-frame / quad-mcp-batch-01|02 / standalone cover-mcp.

**AFTER slice, cover tile ONLY:** factory paste official `cropped-img_7143.png` (`logo-dobry-dom.png`) top-right ~8–12% tile width — **pixel-faithful, native aspect (NOT square crop)**, RGBA alpha, **no white plaque** — covers any model-drawn fake lockup.

**Inlines: ZERO logo.**

## Generation policy (HARD)

| Rule | Value |
|------|-------|
| Canvas | **ONE** 2048×1152 prompted as 2×2 grid |
| Output | `cover.png` + `inline-01..03.png` (4 images total) |
| Provider | **Grsai** — primary or vip for 2K |
| Max attempts | **2** per article → pad-clear TR + slice + logo paste if needed |
| Prose/scene | Derouter Terra `--role cover-scene` only |

## Архитектура

```text
ONE canvas 2048×1152 (Grsai, max 2 attempts — four quadrants IN one draw)
  → cover_quad_split.py → cover.png + inline-01..03.png
  → brand_logo_composite.py (official PNG paste COVER TILE ONLY — native aspect)
→ slice4_gate.py + Cover-QA → Indexer
```

## Brand lock

- Model may reserve **top-right pad 8–12%** on cover panel — **NEVER** ship model-drawn «Добрый дом» lockup as final
- **AFTER slice:** factory pastes official `cropped-img_7143.png` — curtains + red flower + terracotta wordmark, **NOT square crop**
- **FORBIDDEN:** white/gray plaque; logo on inline tiles; `cover_poster_composite.py`
- Phone **+7 (993) 574-83-22** drawn **IN generation** on cover panel infoboard

## Anti-collage gates (HARD — FAIL if broken)

- Second Grsai draw / 8-frame batch / standalone cover batch
- Square logo stamp or full-canvas square crop of logo file
- Model-drawn brand lockup shipped without factory paste
- Logo on any inline tile

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> \
  --composition "..." --location "..." --prop-set "..."
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/slice4-mcp-batch.json --result cover/slice4-mcp-result.json
python3 scripts/excalibur_blog_cover_quad_split.py --article-dir "$ARTICLE" --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_slice4_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

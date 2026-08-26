---
name: cover-excalibur-blog
description: "④a Cover: 2× quad Grsai 2K, meme energy, factory logo overlay after split, phone in-scene."
---

# Cover Agent — longform 8 images

## Philosophy (slim factory)

**Meme energy ON TOPIC + beauty = agent judgment.** Cover + 2–4 inlines: witty top-100 meme framing tied to посуточная аренда pains — funny, screenshot-worthy, comfort+ brand. Catalog: `memory/cover/meme-top100.json`.

**Cat-meme quota (HARD):** max **1 cat-meme slot** per article across cover + 7 inlines. Prefer cover **OR** one inline — not both. All other meme slots = **people-memes** (Roll Safe, Harold, Pepe, Wojak, sacrednik, Жириновский…) — NOT grumpy/ginger/tardar/smudge cat repeats. Anti-repeat 14д: any cat-meme = same family collision.

**Ban:** random unrelated memes, logo under stickers, snow/winter off-season, luxury flex, **logo as generation reference**, **post-composite phone pill**, **2+ cat-meme frames**.

**Brand lock FOREVER (hard only):**
- **NEVER** send logo as Grsai/Derouter reference (`urls`/aroma/`input_urls`)
- Prompt: empty clear **top-right** — no logo, no house icon, no «Добрый дом», no plate/sticker/business card
- **AFTER split:** factory pastes official `cropped-img_7143.png` alpha PNG small top-right — RGBA only, no white/gray backing
- Cover: logo always. Inlines: **2–3 of 7**
- Phone **+7 (993) 574-83-22** painted **IN the scene** (tape strip, torn paper, door plate, magnet) on bottom edge or side quiet zone — readable, pretty, NOT over cat/meme/sticky/headline
- **NEVER** `brand_logo_composite.py --phone-only` or post-composite pill
- NO WordPress UI in art

## Generation policy (HARD)

| Rule | Value |
|------|-------|
| Provider | **Grsai** (see `shared/grsai-gpt-image-api-contract.md`) |
| VIP retry | **disabled** — PRIMARY_MODEL_ID only; ship native undersized if retry fails |
| Max attempts | **2** per canvas → pad-clear + official logo paste if plate |
| Pre-paste gate | `brand_logo_composite` **BLOCKER** on white/gray plate in TOP-RIGHT pad (regen canvas, don't paste over plate) |
| Prose/scene | Derouter Terra `--role cover-scene` only |

## Архитектура

```text
2× quad canvas 2048×1152 (Grsai API, max 2 attempts/canvas)
  canvas 1: cover + inline_1..3
  canvas 2: inline_4..7
→ split 2×2 → cover.png + inline-01..07.png
→ brand_logo_composite.py (logo overlay ONLY — no phone pill)
→ Cover-QA slim → Indexer
```

## Logo overlay (HARD — default)

`cover_mode=brand_logo_paste` in `shared/tenant-config.json`. **Never** logo reference in generation.

```bash
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE"
```

`--phone-only` and `--emergency` are blocked/disabled for normal pipeline.

## Runbook

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> \
  --composition "..." --location "..." --meme "..." --sticker-set "..."
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

Contract: `shared/blog-cover-quad-canvas-contract.md`

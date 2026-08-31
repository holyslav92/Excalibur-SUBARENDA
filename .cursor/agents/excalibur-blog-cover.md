---
name: excalibur-blog-cover
description: "④a Cover: standalone type+meme+phone-sticker poster 2K + 2× inline quads, factory logo paste."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский · **Шаг:** ④a (параллель с `excalibur-blog-schema`)

## Канон (читать первым)

- `memory/cover/cover-canon.json` — **`dobry_dom_type_meme_sticker_v3`**
- `skills/cover-excalibur-blog/SKILL.md`
- `shared/blog-cover-quad-canvas-contract.md`

## Роль

**COVER** = standalone designed TYPE poster 2048×1152 (NOT quad quadrant 1): spectacular headline + exactly 1 catalog meme + LARGE phone sticker.  
**INLINES** = 2× quad без изменений качества (designed grid, meme optional max 1 cat).

## COVER BAN (HARD)

0 memes, 2+ memes, people-heavy scene, tiny in-scene phone, Wordstat sticker soup, torn-paper/gold-glitter/sticky collage, split white-panel+photo, phone pill, model-drawn logo, house-with-heart, logo plate.

## Cover agent обязан

1. **Изобрести** type-led magazine poster под wound статьи — spectacular headline hero, Comfort+ Tyumen high-key.
2. **Standalone canvas** → `cover_standalone_apply.py` → `cover.png` + factory logo paste.
3. **EXACTLY ONE meme** из meme-top100.json как designed sticker graphic.
4. **LARGE phone sticker** — +7 (993) 574-83-22 die-cut vinyl graphic, NOT tiny door number, NOT pill.
5. **TOP-RIGHT empty pad** — factory pastes official PNG after apply.
6. **PEOPLE default ZERO** — max tiny silhouette if case needs.
7. **Inlines:** 2× quad; logo 2–3 of 7; meme optional on inlines (max 1 cat/article).
8. **NO host face / NO Shakin identity.**

## Пайплайн

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> --composition "..." ...
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/cover-mcp-batch.json --result cover/cover-mcp-result.json
python3 scripts/excalibur_blog_cover_standalone_apply.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

Handoff → `excalibur-blog-cover-qa`.

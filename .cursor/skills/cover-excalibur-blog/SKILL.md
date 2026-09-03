---
name: cover-excalibur-blog
description: "④a Cover: Grsai urls[Pexels style + logo], full gen, slice/resize only — NO overlay scripts."
---

# Cover Agent — Grsai full generation

## Philosophy

**Grsai** рисует **всю** обложку за один вызов: кириллица, телефон, логотип, сцена.  
**urls[]:** `[0]` эфемерный **Pexels** style ref (новый на каждую статью), `[1]` постоянный **logo-dobry-dom.png**.  
**Единственные пост-скрипты:** нарезка (`cover_quad_split.py`) или resize (`cover_standalone_apply.py`).  
**ЗАПРЕЩЕНО:** `brand_logo_composite.py`, `cover_poster_composite.py`, любые PIL-оверлеи текста/логотипа.

## Image model lock (HARD)

| Allowed | Forbidden |
|---------|-----------|
| `excalibur_blog_grsai_gpt_image2_api.py` (PRIMARY) | factory logo/phone/type overlay scripts |
| `excalibur_blog_pexels_design_ref.py` | `brand_logo_composite.py` on new covers |
| slice / standalone_apply only | Derouter/Kie unless fallback after Grsai fail |

## Runbook (standalone 16:9 Dzen collage)

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge

# Pexels style ref — один на статью (авто при --write-batch если файла нет)
python3 scripts/excalibur_blog_pexels_design_ref.py --article-dir "$ARTICLE"

python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/cover-mcp-batch.json --result cover/cover-mcp-result.json
python3 scripts/excalibur_blog_cover_standalone_apply.py --article-dir "$ARTICLE" --skip-pad-clear
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

После успешного Grsai: **Pexels URL удаляется из batch**; логотип остаётся в `memory/cover/blog-hero.json` / tenant-config.

## Prompt rules

- EXACT Cyrillic strings from `cover-text.json` — **perfect spelling**, no garbled letters
- urls[0] = layout/color/typography mood from Pexels — do not clone photo subjects
- urls[1] = official logo TOP-RIGHT 8–12%, pixel-faithful
- Phone +7 (993) 574-83-22 IN scene, thumb-readable

## Blockers

- PEXELS DESIGN REF BLOCKER
- LOGO REFERENCE BLOCKER (missing logo-dobry-dom.png)
- GRSAI BLOCKER / KIE API BLOCKER
- logo-composite-stamp.json present (factory paste forbidden)

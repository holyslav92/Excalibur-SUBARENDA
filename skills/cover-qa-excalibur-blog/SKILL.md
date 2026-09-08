---
name: cover-qa-excalibur-blog
description: "Cover-QA: slim gate — logo+phone+no plate+no WP UI; stamp cover_qa.json."
---

# Cover-QA — slim gate (brand lock)

## FAIL только если (brand lock)

- нет factory logo на cover или inline count не 2–3
- AI-drawn lockup в cover pad или на no-logo inline panels
- white/gray plate под logo pad на cover
- нет телефона **+7 (993) 574-83-22** на cover (in-scene или post-composite per tenant)
- WordPress/Gutenberg/Dashboard UI в арте
- номер 922 (риелтор) на обложке
- **2+ frames с cat-meme** (max 1 cat slot на cover+7 inlines)

```bash
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

## Recovery: drawn logo on no-logo inlines (INC B14)

When `forbid_ai_drawn_logo_cover` FAILs on inline-02/04/05/06 (panels without factory logo paste):

1. **Pad-clear** TR zone on no-logo panels (idempotent):

   ```bash
   python3 scripts/excalibur_blog_cover_inline_pad_clear.py --article-dir <dir>
   python3 scripts/excalibur_blog_drawn_logo_gate.py --article-dir <dir>
   ```

2. If still FAIL → **regen** affected canvas(es) with stronger NO-logo prompts (auto in `cover_quad_prompt.py` for non-logo slots), then split + `brand_logo_composite.py` + Cover-QA again.

3. Do **not** paste_and_ship on no-logo panels with visible drawn lockup — pad-clear or regen first.

Logo paste slots come from `quad-manifest.json` → `logo_paste_inline_slots` (default inline_1/3/7).

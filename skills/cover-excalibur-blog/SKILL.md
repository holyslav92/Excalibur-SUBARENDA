---
name: cover-excalibur-blog
description: "④a Cover: 2× quad Grsai 2K, meme energy, logo reference-in-generation, max-2 + vip."
---

# Cover Agent — longform 8 images

## Philosophy (slim factory)

**Meme energy ON TOPIC + beauty = agent judgment.** Cover + 2–4 inlines: witty top-100 meme framing (reaction face, before/after, caption panel, comic beat) tied to посуточная аренда pains — funny, screenshot-worthy, comfort+ brand. Catalog: `memory/cover/meme-top100.json`. Inline types: `meme_panel`, `reaction_card` in `inline-visual-types-dobry-dom.json`.

**Ban:** random unrelated memes, logo under stickers, snow/winter off-season, luxury flex.

**Brand lock (hard only):**
- Logo **in generation** via Grsai `urls`/aroma — official `logo-dobry-dom.png` / `cropped-img_7143.png` reference
- Integrate THIS exact mark small top-right, transparent, **NO** gray/white plate/card/backing
- Phone **+7 (993) 574-83-22** on cover post-composite only (`brand_logo_composite.py --phone-only`)
- Emergency alpha-paste only: `brand_logo_composite.py --emergency` (disabled by default)
- NO WordPress UI in art

## Generation policy (HARD)

| Rule | Value |
|------|-------|
| Provider | **Grsai** (see `shared/grsai-gpt-image-api-contract.md`) |
| VIP retry | **1** per sheet only if non-vip cannot deliver ≥2K (long side &lt;2048) or hard API fail |
| Max attempts | **2** per canvas → pad-clear if plate + phone-only post-composite + ship |
| Prose/scene | Derouter Terra `--role cover-scene` only |

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-scene \
  --system-file skills/cover-excalibur-blog/SKILL.md \
  --user-file <assembled-cover-scene-inputs.md> \
  --output cover/scene-draft.json \
  --article-dir <article_dir>
```

## Когда

После Sol PASS + Description gate PASS + Cover-text gate PASS. Параллельно Schema.

**После Cover:** `excalibur-blog-cover-qa` (slim gate) → Indexer.

## Архитектура

```text
2× quad canvas 2048×1152 (Grsai API, max 2 attempts/canvas)
  canvas 1: cover + inline_1..3
  canvas 2: inline_4..7
→ split 2×2 → cover.png + inline-01..07.png
→ phone-only post-composite on cover (reference mode)
→ Cover-QA slim → Indexer
```

On attempt 2 fail / logo plate: `live_plate_remove_relogo.clear_logo_pad()` → `--phone-only` → **continue**.

## Logo reference (HARD — default)

`logo_mode=reference_in_generation` in `shared/tenant-config.json`. Every Grsai draw call includes logo reference URL in `urls`/aroma.

```bash
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE" --phone-only
```

Emergency alpha-paste (only if reference gen failed):

```bash
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE" --emergency
```

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
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE" --phone-only
```

If gen attempt 2 still has drawn lockup in cover pad → pad-clear → composite → ship.

## Meme + inline visual types

- **Cover:** 1–2 meme beats + Wordstat stickers + scene line — magazine poster energy
- **Inline:** mix utility (`lived_in_room`, `labeled_checklist`, …) with **2–4** `meme_panel` / `reaction_card` on-topic
- Agent picks format freely; must match H2 pain (залог, код, чемодан, домофон)
- Meme stickers ≤15% frame on inline; never cover logo pad

## Blockers

- COVER MOTIF BLOCKER (14-day collision)
- DEROUTER COVER-SCENE BLOCKER
- GRSAI API BLOCKER (after non-vip + 1 vip when 2K/API exhausted)
- IMAGE MODEL BLOCKER — Flux/Seedream/nano_banana/z-image

## QA

Slim Cover-QA only. Do **not** loop regen for typography/overlap/meme density — agent judgment.

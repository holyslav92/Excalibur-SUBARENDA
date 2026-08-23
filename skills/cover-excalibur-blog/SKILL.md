---
name: cover-excalibur-blog
description: "④a Cover: 2× quad Derouter REST 2K, light/meme/Wordstat stickers, anti-repeat 14d."
---

# Cover Agent — longform 8 images, light/meme canon

## Thin conductor + Derouter utility (HARD)

**scene_hint, cover_emotion, prompt invention** — только Derouter utility tier (gpt-5.6-terra, `--role cover-scene`).
PNG generation — `excalibur_blog_derouter_gpt_image2_api.py` (не chat).

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-scene \
  --system-file skills/cover-excalibur-blog/SKILL.md \
  --user-file <assembled-cover-scene-inputs.md> \
  --output cover/scene-draft.json \
  --article-dir <article_dir>
```

Merge scene fields в `quad-manifest.json` без рерайта Cursor. `DEROUTER COVER-SCENE BLOCKER` → стоп.

## Когда

После Sol PASS + Description gate PASS + Cover-text gate PASS. Параллельно Schema.

**После Cover:** `excalibur-blog-cover-qa` → `cover/cover_qa.json` PASS → Indexer.

**Канон:** `memory/cover/cover-canon.json` · Skill agent: `agents/excalibur-blog-cover.md`

## Архитектура

```text
identity-real i2i → 2× quad canvas 2048×1152 (Derouter REST 2K)
  canvas 1: cover + inline_1..3
  canvas 2: inline_4..7
→ split 2×2 → cover.png + inline-01..07.png → inject
```

PRIMARY: **Derouter REST** (`DEROUTER_API_KEY` + `DEROUTER_IMAGE_MODEL`, api-direct 2K). Kie — secondary after Derouter auth/5xx.

## Image model lock (HARD)

| Allowed | Forbidden |
|---------|-----------|
| `excalibur_blog_derouter_gpt_image2_api.py` (PRIMARY) | flux2-pro-text-to-image |
| `excalibur_blog_kie_gpt_image2_api.py` (after Derouter fail) | flux2-pro-image-to-image |
| | Seedream, nano_banana*, z-image |
| | mcp-derouter/start-mcp.sh |
| | Off-pipeline «demo» canvases |

**On Derouter auth/5xx:** one retry + fallback host → then Kie script — **never** Flux/Seedream/nano_banana/z-image.

## Cover canon (v2 — Добрый дом WOW)

**Tenant:** `holyslav92/Excalibur-SUBARENDA` / Добрый дом only. **Never** tymenrieltor.ru / Excalibur-2-Cloud rieltor.

**WOW rules (Cover-QA FAIL if broken):** `memory/cover/visual-notes-dobry-dom.json` · `shared/tenant-config.json` → `cover_wow_rules`

1. **NO WordPress UI in art** — WordPress, Gutenberg, Add title, Publish, Dashboard, wp-admin, block editor, theme chrome, cookie bars.
2. **NO overlapping** — headline, stickers, meme, cat, phone, people, logo pad never overlap. Logo = official PNG ONE stamp TOP-RIGHT (empty pad in gen). Phone +7 993 574-83-22 cover only post-composite, not in logo pad.
3. **WOW poster** — magazine cover, bold readable Russian display type, scene + one sharp line. Not timid system font / label wall / empty stock / WP screenshot.
4. **Inlines** — logo on 2–3 of 7 only (default inline_1, inline_3, inline_7); never 2+ logos per frame.

Factory paste after split: `python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir "$ARTICLE"`

## Cover canon (production)

1. **Invent from scratch** — no inventory lock; no default keys/hologram/desk/balcony.
2. **Anti-repeat 14д** — `used-motifs.json` + `excalibur_blog_cover_motif_gate.py`.
3. **Light & bright** — high-key, sun flare, light leak, glow; **no dark cinematic**.
4. **Memes required** — meme cats + catalog people-memes as **small stickers** on cover; host Святослав = only large human. Inline: infographic hero; meme sticker ≤15% frame from `memory/cover/meme-top100.json` — never co-host/stock man.
5. **Wordstat stickers** — 1–3 readable labels from live Wordstat (Тюмень regions 55+11176).
6. **Identity + body lock** — N/A for `brand_logo_paste` (Добрый дом): NO Shakin/rieltor host; Russian guests by topic only.
7. **Expression invention** — scene emotion under hook; no rieltor studio host clone.
8. **REJECTED daypart formula** — never morning desk / day street / evening close / night split.

## Inline canon (v3 utility-first)

Канон: `memory/cover/inline-visual-types.json` + `cover-canon.json` → `inline_utility`.

1. **Стиль** = одобренная обложка B02: #FFFFFF high-key, gold/black, torn paper, tape, sun flare, collage.
2. **NO host face** on inline — host только на cover.
3. **NO co-host human** on inline — stock model, handsome realtor, generated man, large meme person = FAIL.
4. **Meme stickers** — cats or catalog people-memes only; ≤15% frame; corner accent; real templates from `meme-top100.json`.
5. **Тест пользы (FAIL):** без абзаца читатель выносит факт/порядок/число/сравнение по H2; ряд иконок+3 слова = FAIL.
6. **Типы:** comparison_table → process_flow → bar_timeline_chart → structure_diagram → labeled_checklist.
7. **Labels** = факты из статьи. Cover-QA: `inline_utility_all_7` + `inline_no_host_face` + `inline_no_co_host_human` + `inline_meme_sticker_scale`.

## Runbook

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_hero_reference_url.py
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_cover_image_preflight.py --article-dir "$ARTICLE" \
  --topic-id <id> --probe --write-blocker
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge

# Agent fills scene_hint, cover_motifs, wordstat_stickers in quad-manifest.json
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> \
  --composition "..." --location "..." --meme "..." --sticker-set "..."

python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json --fallback-kie
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json --fallback-kie

python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html

python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> --composition "..." ...
```

## manifest fields (agent)

- `cover_hook`, `cover_hook_highlight` — from cover-text.json
- `slots.cover.scene_hint` — bright invented scene (~80–140 chars) **+ named emotion**
- `slots.cover.cover_emotion` — hook-matched face (shock, side-eye, grimace, bewildered…); never «same as reference»
- `cover_motifs` — composition, location, meme, prop_set, sticker_set, joke
- `wordstat_stickers` — 1–3 phrases from Scout/Research Wordstat
- `slots.inline_1…7` — H2 anchors, `visual_type` (utility catalog), scene_hint, fact labels (3–6)

## Self-check before Derouter REST

- [ ] `cover_motifs` filled + motif gate PASS
- [ ] light/bright language in scene_hint (no dark cinematic)
- [ ] Wordstat stickers tied to topic demand
- [ ] meme cat and/or catalog people-meme planned (cover stickers; inline tiny only)
- [ ] `jobs.length === 1` per canvas batch; `input_urls` on canvas 1
- [ ] `prompt_chars <= 3500`

## Blockers

- COVER MOTIF BLOCKER (14-day collision)
- COVER HERO BLOCKER (identity-real missing)
- **COVER IMAGE PREFLIGHT BLOCKER** — Derouter discontinued + Kie missing/402 (`cover_image_preflight.py`)
- DEROUTER API KEY MISSING / DEROUTER BLOCKER / KIE API BLOCKER / **KIE CREDITS BLOCKER**
- **IMAGE MODEL BLOCKER** — Flux/Seedream/nano_banana/z-image or off-pipeline demo canvas
- daypart formula / inventory default / doc-only office / dark cinematic

## QA

- cover.png + inline-01…07 exist
- inject `data-slot=inline_1…7` after H2
- fragment `cover.md` PASS

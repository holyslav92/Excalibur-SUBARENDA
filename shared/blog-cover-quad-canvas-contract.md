# Blog cover quad canvas contract

> **TENANT:** Добрый дом / добрыйдом-72.рф — `holyslav92/Excalibur-SUBARENDA`.  
> **NEVER** tymenrieltor.ru / Excalibur-2-Cloud rieltor identity or phone +7 922.

# Excalibur BLOG — Quad Canvas (Derouter REST 2K)

Cover после `article.html` + Sol PASS.

## Brand lock (Cover-QA slim — FAIL if broken)

Canon: `shared/tenant-config.json` → `cover_wow_rules`, `memory/cover/visual-notes-dobry-dom.json`.

**Philosophy:** beauty = agent judgment on topic; brand lock = logo + phone + no plate + no WP UI.

1. **Official logo PNG paste** — `logo-dobry-dom.png` / `cropped-img_7143.png`, top-right 8–12%. Cover always + **2–3 inline** (default 1/3/7). Never AI-drawn lockup. Never logo on all 8.
2. **NO plate** under logo pad — alpha paste only, no white/gray card.
3. **Phone** **+7 (993) 574-83-22** on cover post-composite bottom-left only.
4. **NO WordPress UI** in art.

**Generation:** Grsai API, max **2 attempts/canvas** (+ 1 vip retry/sheet on API fail). On exhaust: pad-clear + factory paste → continue to publish.

Factory logo paste: `scripts/excalibur_blog_brand_logo_composite.py` — never ask image model to draw logo.

## Longform: 8 изображений

- `cover.png` 1200×675
- `inline-01.png` … `inline-07.png` (7× `figure.inline-quad`, data-slot `inline_1`…`inline_7`)
- **2 canvas** `2048×1152` (2×2, панели 16:9)

| Canvas | Файл | Слоты |
|--------|------|-------|
| 1 | `canvas-quad-01.png` | cover, inline_1…3 |
| 2 | `canvas-quad-02.png` | inline_4…7 |

PRIMARY: **Derouter REST** (`DEROUTER_API_KEY` + `DEROUTER_IMAGE_MODEL`), `resolution: 2K`, 16:9. Kie — secondary fallback only.

## Image model lock (HARD — owner)

**Order of preference:**

```text
1. DEROUTER_API_KEY → scripts/excalibur_blog_derouter_gpt_image2_api.py (api-direct, 2K)
2. KIE_API_KEY      → scripts/excalibur_blog_kie_gpt_image2_api.py (after Derouter auth/5xx + retry)
3. neither          → BLOCKER
```

**FORBIDDEN** (even after timeout): `flux2-pro-text-to-image`, `flux2-pro-image-to-image`, Seedream, `nano_banana*`, `z-image`, `mcp-derouter/start-mcp.sh`.

**MCP-KV on Cloud:** Wordstat (`wordstat_*`) only for Scout/Cover stickers. Not a buffet of image models.

Contracts: `shared/derouter-gpt-image-api-contract.md`, `shared/kie-gpt-image-api-contract.md`

## Cover canon (Добрый дом)

Канон: `memory/cover/cover-canon.json` · Style: `memory/cover/quad-style-dobry-dom.json`

1. **WOW magazine poster** — bold readable Russian display hook + scene; high-key collage.
2. **Brand logo paste** — NO logo in generation; factory pastes PNG TOP-RIGHT 8–12% on cover + 2–3 inlines.
3. **Anti-repeat 14д** — `memory/cover/used-motifs.json` + `excalibur_blog_cover_motif_gate.py`.
4. **Light & bright** — high-key, sun flare, light leak, glow; dark cinematic запрещён.
5. **Memes** — meme cat bottom-left ≤12% on cover; catalog people-memes tiny on inline only.
6. **Wordstat stickers** — 1–3 readable stickers с live Wordstat (Тюмень regions 55+11176).
7. **NO Shakin/rieltor host** — Russian guests by topic only.
8. **Phone** — `+7 (993) 574-83-22` post-composite bottom-left on cover only.

## Workflow

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_quad_manifest.py --article-dir <dir> --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> --composition "..." ...
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir <dir> --write-batch
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json --fallback-kie
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json --fallback-kie
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_brand_logo_composite.py --article-dir <dir>
python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> ...
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

## Visual locks (Добрый дом)

- Панели `#FFFFFF` high-key; ink `#141821`; gold `#dcc5a1` один accent; sun flare/glow OK
- **Cover:** WOW poster collage; bold Cyrillic hook; Wordstat stickers; meme cat bottom-left; TOP-RIGHT empty logo pad; phone post-composite (not in gen)
- **Inline (7 шт.) — UTILITY-FIRST** (`memory/cover/inline-visual-types-dobry-dom.json`):
  - Стиль = B02-approved bright collage
  - Logo paste on **2–3** panels only (default inline_1, inline_3, inline_7), same TOP-RIGHT pad
  - **Без лица host / Shakin**
  - Meme sticker ≤15% frame, never top-right pad
- Запреты: WordPress UI, overlapping elements, logo on all panels, 2+ logos per frame, timid system font, empty stock, tymenrieltor branding

## Blockers

- `COVER QA BLOCKER` — any WOW rule check false in `cover/cover_qa.json`
- `COVER MOTIF BLOCKER` — collision в 14-дневном логе
- `DEROUTER BLOCKER` / `KIE API BLOCKER` — нет URL после 2K gen
- отсутствует любой из `inline-01…07.png` или inject `data-slot`
- logo composite stamp FAIL or inline logo count outside 2–3

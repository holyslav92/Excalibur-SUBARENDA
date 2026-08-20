# Blog cover quad canvas contract

> **TENANT:** The Риэлтор / tymenrieltor.ru — `memory/cover/*`, `shared/tenant-config.json`.

# Excalibur BLOG — Quad Canvas (Derouter REST 2K)

Cover после `article.html` + Sol PASS.

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

**No off-pipeline demos:** one uncut prompt ≠ article. Full canon: Scout×Wordstat → … → Cover only.

Contracts: `shared/derouter-gpt-image-api-contract.md`, `shared/kie-gpt-image-api-contract.md`

## Cover canon (v2)

Канон: `memory/cover/cover-canon.json`

1. **Изобретение с нуля** — no inventory lock, no default recurring props (keys, hologram, desk, balcony).
2. **Anti-repeat 14д** — `memory/cover/used-motifs.json` + `excalibur_blog_cover_motif_gate.py check` перед `--write-batch`.
3. **Light & bright** — high-key, sun flare, light leak, glow; dark cinematic запрещён.
4. **Мемы** — meme cats + meme people stickers; host Святослав на cover; 8-set включает людей; коты регулярно по неделе.
5. **Wordstat stickers** — 1–3 readable stickers с live Wordstat фразами (Тюмень/область, regions 55+11176).
6. **Identity** — `identity-real/*` only; no scene clone; no AI faces.
7. **REJECTED daypart formula** — never: morning desk+document / day street / evening close talk / night split.

## Hero identity lock

- `memory/cover/assets/identity-real/*` — **4 live photos** (28 лет). i2i ротация.
- `scene-composition-only/hero-ref-*.jpg` — mood ONLY, **never FACE source**

## Workflow

```bash
python3 scripts/excalibur_blog_hero_reference_url.py
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <dir>
python3 scripts/excalibur_blog_quad_manifest.py --article-dir <dir> --merge
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> --composition "..." --location "..." ...
python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir <dir> --write-batch
# Derouter REST ×2 → quad-mcp-result-01.json, quad-mcp-result-02.json
# python3 scripts/excalibur_blog_derouter_gpt_image2_api.py --article-dir <dir> --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json --fallback-kie
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> --composition "..." ...
```

## Visual locks (The Риэлтор)

- Панели `#FFFFFF` high-key; ink `#141821`; gold `#dcc5a1` один accent; sun flare/glow OK
- **Cover:** host LARGE left, smart-casual blazer, invented bright scene, Wordstat stickers, meme stickers
- **Inline (7 шт.) — UTILITY-FIRST** (канон: `memory/cover/inline-visual-types.json`):
  - Стиль = одобренная обложка B02: белый high-key, золото/чёрный, скотч, рваная бумага, солнце, коллаж
  - **Без лица host / identity-real** — host только на cover
  - **Тест пользы (FAIL):** читатель без абзаца выносит факт/порядок/число/сравнение по H2; ряд иконок + 3 слова = FAIL
  - Типы: `comparison_table`, `process_flow`, `bar_timeline_chart`, `structure_diagram`, `labeled_checklist`, `fact_card`
  - Labels = факты из статьи (цифры, порядок, инструменты), не слоганы настроения
  - Optional ONE tiny cat-sticker — не герой кадра
- Запреты inline: icon row+caption; дубли подписей; риэлтор за столом; пустой UI; копипаст cover; Salt Bae/Drake/celebrity; «не эскроу» как шаг процесса
- Запреты общие: dark cinematic, daypart formula, inventory default props, plastic face, AI hero-ref face, empty doc-only office

## Blockers

- нет reference / canvas 1 без `input_urls`
- `COVER MOTIF BLOCKER` — collision в 14-дневном логе
- `DEROUTER BLOCKER` / `KIE API BLOCKER` — нет URL после 2K gen
- 8 отдельных image jobs вместо 2 canvas — запрещено
- отсутствует любой из `inline-01…07.png` или inject `data-slot`
- cover клонирует эталонный кадр или daypart formula

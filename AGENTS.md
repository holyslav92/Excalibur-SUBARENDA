# Excalibur-2-Cloud Instructions

Язык: русский (тенант может сменить в `shared/tenant-config.json`).

## Первый запуск

Если `memory/setup/status.json` → `complete != true` **или**
`shared/tenant-config.json` → `setup_complete != true`:

→ работай как **`excalibur-blog-setup`** (skill `setup-excalibur-blog`).  
→ **Не** запускай Scout / Research / Publish.

См. `CLOUD-FIRST-RUN.md`, `SETUP.md`.

## Канон (после setup)

```text
Scout? → research_start → Research → Title → Writer(смысл)
→ Sol(слог) → Description → Cover-text || Schema → Cover → Cover-QA
→ Indexer(llms) → Publish → Fixer → merge → Content-learner
```

**Writer** → `drafts/writer.html` (полный CASE, не тезисы; `claude-opus-5`).  
**Sol** (`excalibur-blog-sol`) → финальный `article.html` слогом тенанта
(`shared/SOUL.md` + `shared/soul-examples/`; `gpt-5.6-terra`).  
После Title и после Writer/Sol — `scripts/excalibur_blog_case_delivery_gate.py`
(BLOCK → переписать роль, не публиковать). После Sol — stamp `pipeline_canon`
+ structural checks. Прозу после Sol не переписывают (кроме возврата Sol при FAIL гейтов слога).

**Title** → `title-brief.json`. **Description** → `description-brief.json` (Дзен-карточка, после Sol).

**18 ролей** (см. `.cursor/agents/FOR-AGENTS.md`): 16 pipeline + `excalibur-blog-description` + `excalibur-blog-cover-qa`.

Никто не читает уже опубликованные статьи сайта — только
`published-titles-only.md` / `shared/published-titles.md` для anti-dup.

`memory/topics/` запрещена. Scout → handoff + `signal_urls` + **dual gate: Klyshin hooks (`memory/scout/klyshin-topic-bank.*`) × MCP-KV Wordstat** (Tyumen 55+11176, compare RU 225). Klyshin = angle/hook; Wordstat = **evaluate + rework for demand** (не binary skip: слабый объём → локализация/переформулировка до buyer P0; skip только если после rework нет честного buyer-intent кластера). В handoff логировать **original Klyshin hook** + **final P0 phrase+volume**. Cover canon: `memory/cover/cover-canon.json`.

**Factory brain (двухуровневый split):** Cursor — **тонкий дирижёр** (default Composer; не переключать модель Cursor).
Прозу пишет только `scripts/excalibur_blog_derouter_opus_chat.py` → Derouter REST (`DEROUTER_API_KEY`):
- **Opus 5 = Writer only; everything else Terra** (cost canon)
- **powerful** `claude-opus-5` (`DEROUTER_OPUS_MODEL`): Writer (article body / longform)
- **utility** `gpt-5.6-terra` (`DEROUTER_TERRA_MODEL`): Scout, Title, Sol, Research synthesis, Description, Cover-text, Schema, Cover-scene
При недоступности → `DEROUTER <ROLE> BLOCKER`, без тихого fallback на Composer. См. `shared/derouter-opus-brain-contract.md`.
**Cover PNG:** Grsai PRIMARY_MODEL_ID only (`shared/grsai-gpt-image-api-contract.md`); **vip permanently disabled**. Derouter REST — legacy fallback (`shared/derouter-gpt-image-api-contract.md`).
**Wordstat:** MCP-KV. **Cover-QA:** Python gates, не «глаз» агента.

```bash
python3 scripts/excalibur_blog_research_start.py --topic-id B111 --title "…"
```

## Ошибка

- Второй автор / rewrite-loop **поверх Sol** (Sol — единственный стилевой рерайт)
- Термин-дамп / research-брифинг в открытии финала
- topics / SEO-хвосты
- Writer/Sol читают старые article.html / live-сайт как образец
- Publish без pipeline_canon stamp
- Publish без `cover/cover_qa.json` PASS или без `description-brief.json`
- Publish **без рубрик WP** (`wp_category_slugs` / `topic_defaults`) при `wp_categories_required=true`
- Publish **без outbound interlink** (**3–4** уникальные live `/blog/` ссылки на published siblings) при `interlink_old_articles=true`
- **Dzen:** в `article.html` и RSS — только `{{SITE_BASE}}/blog/{slug}/` (или expanded absolute); **никогда** `href="/blog/..."` (root-relative ломает Дзен in-app browser → 404)
- Scout/тема без **Klyshin×Wordstat dual gate**, без rework-лога или с выдуманными частотами
- Scout **drop hook** при слабом Wordstat без цикла rework (локализация Тюмень, buyer-жаргон: егрн, наследство, ипотека, аванс…)
- Scout/тема про RF-blocked heroes без Дзен-канона (если `dzen_rf_pack`)
- Sol выдумывает факты, которых нет в `drafts/writer.html` / research
- Cursor пишет Scout/Title/Writer/Sol/Description/Cover-text/Schema prose своей моделью вместо `excalibur_blog_derouter_opus_chat.py`
- Publish при FAIL `excalibur_blog_case_delivery_gate.py` (how-to H1, duty-log/clock lead, тонкое открытие, гайд вместо CASE)
- Duty-log lead в §1 (день недели, календарная дата, `HH:MM`, «Тюмень, двор») или часы в H1
- Воронка CTA не в конце статьи (два блока, после чеклиста или «у нас так»)
- Logo на всех 8 кадрах (канон: cover always + 2–3 inline, default 1/3/7)
- Запуск пайплайна до завершения Setup
- Logo as Grsai/Derouter generation reference (`urls`/aroma/`input_urls` with cropped-img_7143) — factory alpha overlay AFTER split only
- Post-composite phone pill/button on cover (`brand_logo_composite --phone-only` or `draw_phone_on_cover`)
- White/gray/beige plate under logo pad; logo or phone overlapping cat/meme/sticky/headline

## Preflight

**До Scout (если dzen_rf_pack):** прочитать `shared/dzen-content-rules.md` +
`shared/rf-blocked-entities.json`.

```bash
python3 scripts/excalibur_blog_doctor.py
python3 scripts/excalibur_blog_today.py
python3 scripts/excalibur_blog_research_start.py --topic-id <id> --title "<short>"
```

Директор: `.cursor/agents/excalibur-blog-director.md` (не Task).  
Setup: `.cursor/agents/excalibur-blog-setup.md` (не Task).

## Publish (рубрики + перелинковка)

**Рубрики:** перед каждым publish в `article.meta.json` задай `wp_category_slugs`
или положись на `shared/wp-blog-categories.json` → `topic_defaults`. Скрипт publish
всегда вызывает `wp_set_post_categories`; без рубрики — **BLOCKER**
(`wp_categories_required=true`).

**Перелинковка:** при `interlink_old_articles=true` Writer/Sol добавляют **3–4**
контекстные ссылки на sibling из `shared/published-articles.md` (`status=published`,
живые HTTP 200 `/blog/` URL, разные slug). **Канон href в артефактах:** `{{SITE_BASE}}/blog/{slug}/`
(expand при publish). **Dzen:** never relative `/blog/` hrefs.
После publish — inbound «Читайте также» в 1–3 старых постах (авто из
`publish_options.auto_interlink_after_publish`). Контракт: `shared/interlink-contract.md`.

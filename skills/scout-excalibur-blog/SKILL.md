---
name: scout-excalibur-blog
description: Pick P0 topic from Klyshin hooks × MCP-KV Wordstat — evaluate and rework for Tyumen demand.
---

# Scout — Klyshin hooks × Wordstat (evaluate + rework)

## Thin conductor + Derouter utility (HARD)

Handoff-проза (topic, rework log, title draft) — **только** через Derouter utility tier (gpt-5.6-terra).
Wordstat частоты — live MCP-KV (не Derouter). Cursor не пишет handoff своей моделью.

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role scout \
  --system-file skills/scout-excalibur-blog/SKILL.md \
  --user-file <assembled-scout-inputs.md> \
  --output .cursor/excalibur-blog-handoff.md \
  --article-dir <article_dir_or_memory/scout>
```

`DEROUTER SCOUT BLOCKER` → стоп. Контракт: `shared/derouter-opus-brain-contract.md`.

Тему выбираешь из **двух обязательных источников**:

1. **Алексей Клышин (angle bank)** — `memory/scout/klyshin-topic-bank.md` + `.json`, канал `https://t.me/klyshin_A`.
2. **Wordstat (demand spine)** — MCP-KV buyer-спрос в Тюмени/области (55 + 11176), сравнение с RU **225**.

Klyshin **не** заменяет частоты. Wordstat **не** binary skip gate.

## Алгоритм (канон)

```text
1. Klyshin hook/angle (bank + live @klyshin_A)
2. wordstat_get_top_requests: hook phrase + tyumen analogs (regions 55, 11176; compare 225)
3. Слабый объём → НЕ drop. Rework:
   - локализовать на Тюмень
   - заменить жаргон на поисковые формулировки (егрн, наследство, ипотека, новостройка, аванс, пенсионер, доверенность, банкротство…)
   - wordstat_get_top_requests по similar queries
   - выбрать ближайший high-frequency cluster с тем же risk/story
4. Title — ритм Klyshin (case hook). P0 Wordstat — demand spine под H1; stickers/H2 из reworked live queries
5. Skip ТОЛЬКО если после rework нет честного buyer-intent кластера (не brand vanity)
6. Лог: original Klyshin hook + final Wordstat P0 phrase+volume (+ rework steps)
```

## Klyshin — ALWAYS joint with Wordstat

- Читай `memory/scout/klyshin-topic-bank.md` + свежий `https://t.me/s/klyshin_A`
- После Scout **обнови** банк: `last_seen`, `wordstat_rework_log`, `final_p0`, `used_in_articles`
- **Не копируй** Москву/Дубай/МКАД как P0 — локализуй на Тюмень или rework до Tyumen cluster
- Факты в статье: **Святослав Шакин / Тюмень**, не копипаст канала

`scout_signal_urls` (tenant-config): **klyshin_A** + dzen holyslav + site blog + t.me/holyslav92

## Wordstat — HARD GATE (MCP-KV)

**Частоты не выдумывать.** Если `CallMcpTool` на MCP-KV Wordstat недоступен → **SCOUT BLOCK**.

```bash
python3 scripts/excalibur_blog_wordstat_gate.py config
```

### Preflight (обязательно, первый solo CallMcpTool)

`MCP-KV` → `wordstat_get_user_info`  
Если ошибка / tool missing → **WORDSTAT MCP BLOCKER**, handoff не пишем.

### Регионы (lookup, не гадать)

1. `wordstat_get_regions_tree` — если `memory/cover/wordstat-geo.json` устарел
2. Канон после lookup: **Тюмень=55**, **Тюменская область=11176**, **Россия=225**

### Rework vocabulary (buyer search spine)

При слабом объёме на «юридическом» hook — пробуй живые кластеры:

- егрн / выписка егрн / проверка егрн
- наследство / наследники / отказ от наследства
- ипотека / новостройка / вторичка
- аванс / задаток / безопасный расчёт / аккредитив
- пенсионер / пожилой продавец / опека
- доверенность / банкротство / торги
- маткапитал / детская доля

Для каждого rework-раунда — **отдельный** `top_requests` по probe; сохраняй частоты.

**Сравнение:** тот же `phrase` с `regions: ["225"]` когда нужен national контекст.

**Optional:** `wordstat_get_dynamics` на выбранный final P0.

### НЕ P0 (brand vanity — только справка)

«добрый дом тюмень», brand vanity — низкий объём. Не строить тему только из них.

### Handoff (обязательно)

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: <hook_id> | original: «…» | angle: <…> | signal: https://t.me/klyshin_A/…
wordstat_rework: probe «…» <freq> → … → final P0 «купить квартиру в тюмени» 23060 | clusters tried: …
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «…» <freq> | …
```

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

## Внешний сигнал

1. **klyshin_A** + ≥1 другой URL из `scout_signal_urls` (сегодня)
2. Wordstat final P0 buyer volume после rework-цикла
3. `published-titles-only.md` — anti-dup only

## Dzen feed — угол темы (research авг 2026)

Лента Дзена кликает: **число+список**, **страх денег/жилья**, **кейс с суммами**, **вопрос/контраст в заголовке**, **постер**. Добрый дом **не** копирует пустой кликбейт (CAPS, красные стрелки, «1000% годовых», luxury-flex).

Выбери **один** `dzen_pattern` для handoff (см. `shared/article-style.md`):

| # | Паттерн | Пример угла |
|---|---------|-------------|
| 1 | Нумерованный список с обещанием | «5 вопросов хозяину до предоплаты» |
| 2 | Кейс с суммами и датами | залог удержали / «посчитали на выезде» |
| 3 | Страх → инструкция в §1 | «залог 5 000 ₽: когда вернут» |
| 4 | Контраст с ответом в лиде | посуточно vs отель на 2 ночи |
| 5 | Локальный + сезонный | район Тюмени, окно брони август / НГ |

**Demand** RF-wide Wordstat; **supply** — только посуточная/субаренда **Тюмень**. H1 может быть без слова «Тюмень».

В handoff: `dzen_pattern: N` + `dzen_shape_hint: «…»` (shape, не финальный H1).

## Выход

`.cursor/excalibur-blog-handoff.md` — topic_id, title draft (Klyshin rhythm), `dzen_pattern`, external_signal, signal_urls, klyshin_hook + wordstat_rework + wordstat lines.

## Чеклист

1. `wordstat_get_user_info` → OK
2. Fetch klyshin_A + holyslav/dzen signals
3. Pick hook from bank or fresh post → update bank
4. `wordstat_get_top_requests` на hook + probes (55+11176; compare 225)
5. Слабый объём → rework (локализация + buyer jargon + similar queries) — **не** мгновенный skip
6. Final P0 + title angle + `dzen_pattern` (1–5); лог original hook + final phrase+volume
7. handoff + `wordstat_gate.py handoff` → стоп

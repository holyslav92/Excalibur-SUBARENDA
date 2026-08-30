---
name: scout-excalibur-blog
description: Pick P0 topic from Klyshin hooks × MCP-KV Wordstat — evaluate and rework for Tyumen guest demand.
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
2. **Wordstat (demand spine)** — MCP-KV **guest**-спрос в Тюмени/области (55 + 11176), сравнение с RU **225**.

Klyshin **не** заменяет частоты. Wordstat **не** binary skip gate.

## Klyshin delivery — 10 правил (HARD, mechanics only)

1. §1 = **плотный кейс** (1–2 абзаца holyslav Dzen). **BAN** vertical ladder (8+ строк по 1–4 слова) в opening.
2. Title = two-beat stop-factor (см. Title skill, 10 formulas). **Не** topic label.
3. Reader is inside — **гость**, не host-operator report.
4. Number = price of burn (залог, доплата, минуты, ночи).
5. Host/aggregator dialogue: quote then break («Нет. Так не заселяем.»).
6. One case → one verdict. Checklist AFTER moral.
7. Moral: first X, then money/key.
8. One lockpick question (guest: «Где бойлер?» / «сколько минут до вуза?»).
9. Refusal beat after excuse — structure only; **не** копировать сделки/Москву/ЕГРН/телефон Клышина.
10. Guest pains RF-wide Wordstat; supply Тюмень only. **Не** legal hook bank.

## Алгоритм (канон)

```text
1. Прочитай published-titles (последние N=3) → angle rotation (см. klyshin-topic-bank.md)
2. Klyshin hook/angle (bank + live @klyshin_A) — guest topic, NOT burn-at-door if saturated
3. wordstat_get_top_requests: hook phrase + tyumen analogs (regions 55, 11176; compare 225)
4. Слабый объём → НЕ drop. Rework guest clusters ONLY:
   посуточно, залог, заселение, ранний заезд, уборка, ЖКХ, соседи, животные,
   предоплата, отмена брони, посуточно или отель, парковка, вайфай, бойлер,
   ключница, командировка, Тюмень
5. Prefer high-volume guest P0 over clever-but-tiny hooks
6. Title draft — ритм Klyshin (case hook). P0 Wordstat = demand spine; Title rides P0, not legal essay
7. Skip ТОЛЬКО если после rework нет честного guest-intent кластера (не brand vanity)
8. Лог: original Klyshin hook + final Wordstat P0 phrase+volume (+ rework steps)
```

**Запрещено в rework:** егрн, наследство, ипотека, новостройка, маткапитал, аванс сделки, нотариус.

## Angle rotation (HARD)

Перед выбором hook — `shared/published-titles.md` (последние **N=3**).

**Skip** hook из семейства **burn-at-door** (код / бесконтакт / «оплатил — дверь не та»),
если последние N статей уже из этой семьи **без нового угла**.

## Klyshin — ALWAYS joint with Wordstat

- Читай `memory/scout/klyshin-topic-bank.md` + свежий `https://t.me/s/klyshin_A`
- После Scout **обнови** банк: `last_seen`, `wordstat_rework_log`, `final_p0`, `used_in_articles`
- **Не копируй** Москву/Дубай/МКАД как P0 — локализуй на Тюмень или rework до Tyumen cluster
- Факты в статье: **Добрый дом / хост посуточной Тюмень**, не копипаст канала, **не Шакин/риэлтор**

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

### Rework vocabulary (guest daily-rental ONLY)

При слабом объёме на hook — пробуй **guest** кластеры:

- посуточно / квартира посуточно / аренда посуточно тюмень
- залог / залог при аренде / вернут залог
- заселение / бесконтактное заселение / код от двери
- ранний заезд / поздний выезд
- уборка / уборка перед выездом
- ЖКХ / коммунальные / показания счётчиков
- соседи / шум / правила проживания
- животные / с собакой / доплата за питомца
- предоплата / отмена брони / бронирование
- посуточно или отель / командировка
- парковка / ключница / вайфай / бойлер

Для каждого rework-раунда — **отдельный** `top_requests` по probe; сохраняй частоты.

**Сравнение:** тот же `phrase` с `regions: ["225"]` когда нужен national контекст.

**Optional:** `wordstat_get_dynamics` на выбранный final P0.

### НЕ P0 (brand vanity — только справка)

«добрый дом тюмень», brand vanity — низкий объём. Не строить тему только из них.

### Handoff (обязательно)

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: <hook_id> | original: «…» | angle: <…> | signal: https://t.me/klyshin_A/…
wordstat_rework: probe «…» <freq> → … → final P0 «квартира посуточно тюмень» <freq> | clusters tried: …
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «…» <freq> | …
angle_rotation: checked last N=3 | burn-at-door skip: yes|no | reason: …
```

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

## Внешний сигнал

1. **klyshin_A** + ≥1 другой URL из `scout_signal_urls` (сегодня)
2. Wordstat final P0 **guest** volume после rework-цикла
3. `published-titles-only.md` — anti-dup + angle rotation

## Dzen feed — угол темы (research авг 2026)

Лента Дзена кликает: **страх денег/жилья**, **кейс с суммами**, **вопрос/контраст в заголовке**, **постер**.
Добрый дом **не** копирует пустой кликбейт (CAPS, красные стрелки, «1000% годовых», luxury-flex).

**Dzen pattern 1** (N советов / N вопросов) — **NOT default**. Prefer **2–5**.

Выбери **один** `dzen_pattern` для handoff (см. `shared/article-style.md`):

| # | Паттерн | Пример угла |
|---|---------|-------------|
| 1 | Нумерованный список с обещанием | «5 вопросов хозяину до предоплаты» — **NOT default** |
| 2 | Кейс с суммами и датами | залог удержали / «посчитали на выезде» |
| 3 | Страх → инструкция в §1 | «залог 5 000 ₽: когда вернут» |
| 4 | Контраст с ответом в лиде | посуточно vs отель на 2 ночи |
| 5 | Локальный + сезонный | район Тюмени, окно брони август / НГ |

**Demand** RF-wide Wordstat; **supply** — только посуточная/субаренда **Тюмень**. H1 может быть без слова «Тюмень».

В handoff: `dzen_pattern: N` + `dzen_shape_hint: «…»` (shape, не финальный H1).

## Выход

`.cursor/excalibur-blog-handoff.md` — topic_id, title draft (Klyshin rhythm), `dzen_pattern`, external_signal, signal_urls, klyshin_hook + wordstat_rework + wordstat + angle_rotation lines.

## Чеклист

1. `wordstat_get_user_info` → OK
2. Fetch klyshin_A + holyslav/dzen signals
3. Check angle rotation (last N=3 published titles)
4. Pick hook from bank or fresh post → update bank
5. `wordstat_get_top_requests` на hook + probes (55+11176; compare 225)
6. Слабый объём → rework **guest clusters only** — **не** мгновенный skip
7. Prefer high-volume P0; `dzen_pattern` 2–5 (NOT default 1)
8. Final P0 + title angle; лог original hook + final phrase+volume
9. handoff + `wordstat_gate.py handoff` → стоп

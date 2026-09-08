# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** handoff markdown (секции 1–10).
Скрипт запишет файл. **Не** отвечай BLOCKER, **не** пиши что нет MCP/shell — Wordstat проверен дирижёром, частоты ниже live.

**OUTPUT RULES (HARD):**
- Return ONLY the handoff markdown body.
- Sections: 1 Topic, 2 Title draft, 3 Dzen shape, 4 Klyshin hook, 5 Case spine, 6 Verdict, 7 Wordstat, 8 Angle rotation, 9 External signal, 10 Final handoff lines.
- Include: topic_id, slug draft, title_draft, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, dzen_shape_hint, signal_urls, external_signal, guest_pain.

---

# Scout inputs — 2026-09-08 YEKT (Добрый дом, слот B15)

## Дата и слот
- today: 2026-09-08 (Asia/Yekaterinburg)
- season: начало сентября, командировочный сезон
- topic_id: **B15**

## Published titles (anti-dup, last 3 for rotation)
- B12: Написали «тихий центр». Три ночи за 12 600 ₽ — под краном
- B13: Код сработал. Пустая ключница — 35 минут у двери
- B14: «Тихий дом» обещали. За 8 400 ₽ — музыка за стеной ночью

Skip families: код/ключница (B01,B13), соседи/тихий (B12,B14), кухня (B07), парковка (B09), выезд/багаж (B06), полотенца (B11), отзывы (B05), доплаты (B04,B10), предоплата (B08), вуз (B03), залог плита (B02).

## Klyshin hook

- hook_id: **sept_business_trip**
- original: «Звонок в 10:00. Заселился в 22:00.»
- angle: стол, розетки у стола, реальный Wi‑Fi на созвон, закрывающие документы — до оплаты
- lockpick: «Сколько Мбит на загрузку и есть ли розетка у стола, не под кроватью?»
- refusal: «Нет. Так не бронируем.» / «Сначала скорость и документы. Потом ключ.»
- klyshin_signal: https://t.me/klyshin_A — ритм «сначала проверка, потом деньги» (не копировать сделки/Москву/ЕГРН)
- dzen_pattern: **2**
- dzen_shape_hint: командировка в Тюмень, сентябрь; 3 ночи + провал созвона из‑за Wi‑Fi/рабочего места

## Case spine

Инженер/менеджер, 3 ночи командировки в Тюмень (~10 200 ₽). Заселение после рейса в 22:00. Утром в 10:00 видеосозвон — Wi‑Fi 3–5 Мбит, камера рвётся; розетка только у кровати. Хозяин: «Ну у нас же интернет есть». Бухгалтерия ждёт закрывающие — в объявлении «по запросу», в чате тишина. Moral: сначала скорость/розетка/доки, потом оплата.

## Title / slug

- title_draft: «Заселился в 22:00. В 10:00 созвон — Wi‑Fi не выдержал»
- slug_hint: zaselenie-v-22-00-sozvon-v-10-wifi-ne-tyanet

## Wordstat (MCP-KV live, 2026-09-08)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| probe | region | volume |
|-------|--------|--------|
| командировка тюмень квартира | 55+11176 | API empty |
| командировка тюмень | 55+11176 | 38 |
| командировка тюмень | 225 | 84 |
| квартира посуточно командировка | 225 | 77 |
| квартиры для командировок | 225 | 517 |
| аренда квартиры посуточно | 55+11176 | 704 |
| аренда квартир посуточно тюмень | 55+11176 | 187 |
| снять квартиру посуточно в тюмени | 55+11176 | 1672 |
| снять квартиру посуточно в тюмени | 225 | 3952 |
| **квартиры посуточно тюмень** | **55+11176** | **5134** |
| квартиры посуточно тюмень | 225 | 10865 |

wordstat_rework: probe «командировка тюмень квартира» API empty → «командировка тюмень» 38 (55+11176) | 84 (225) → «квартира посуточно командировка» 77 (225) → «квартиры для командировок» 517 (225) → «аренда квартиры посуточно» 704 (55+11176) → «снять квартиру посуточно в тюмени» 1672 (55+11176) → **final P0 «квартиры посуточно тюмень» 5134 (55+11176)** | compare 10865 (225)

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5134 | compare 10865 (225) | angle cluster «снять квартиру посуточно в тюмени» 1672/3952

angle_rotation: checked last N=3 | burn-at-door skip: yes (B13 keybox) | reason: shift to business-trip Wi‑Fi/workspace family

## Signal URLs
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_Tyumen

## Tenant
Добрый дом, посуточная Тюмень, CASE 700–1100 слов, не гайд, не риэлтор.

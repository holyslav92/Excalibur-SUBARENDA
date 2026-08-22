# Scout assembled inputs — B03 contract_bans — 2026-08-22 YEKT summer

## Tenant
Добрый дом / Excalibur-SUBARENDA / посуточная аренда и субаренда Тюмень
Дата: 2026-08-22, Asia/Yekaterinburg, лето. Обложка = лето (не зима героем).

## Anti-dup (уже опубликовано — НЕ повторять)
B01 бесконтактное заселение; B02 залог/скол на плите; уборка+залог; скрытые доплаты;
соседи; цена «от»; интернет и ТВ; что входит в стоимость; отмена брони; предоплата/вечеринки/лишние гости;
ранний заезд 7 утра; субаренда.

## Klyshin hook (выбран)
id: contract_bans
original: «что нельзя делать по договору аренды»
angle: 7 запретов в правилах проживания до подписания/оплаты посуточно
signal: https://t.me/klyshin_A — пост «Нотариус заранее подготовил договор. А на сделке цена выросла на 70 000 рублей» (риск в мелком шрифте договора; «всё проверили» ≠ прочитали правила)

## Отклонённые кандидаты (rework exhausted или слабее P0)
- utilities_counters: probe «показания счетчиков аренда» 3 (55+11176) / 214 (225); rework «коммунальные платежи аренда квартиры» 4 / 599 — слабый Tyumen buyer cluster
- move_one_day: probe «переезд чеклист» пусто Tyumen / ~5 (225) — нет честного buyer P0 для посуточной

## Wordstat preflight
mcp-kv wordstat_get_user_info OK (2026-08-22)

## Wordstat rework log (live MCP-KV)
probe «что нельзя при аренде квартиры» → 10 (225), пусто (55+11176)
probe «правила проживания аренда» → «правила проживания посуточной аренды» 77 (225), пусто (55+11176)
probe «правила проживания посуточной аренды» → пусто (55+11176)
probe «договор аренды квартиры» → 1974 (55+11176), 130904 (225) — final P0
clusters tried: contract_bans hook, rules посуточно, rental bans, договор аренды

## Final P0
«договор аренды квартиры» — 1974 показов (regions 55+11176), 130904 (225)
P1 Tyumen: «аренда квартиры тюмень посуточно» 191 (55+11176)
P1 RU: «правила проживания посуточной аренды» 77 (225)

## Dzen
dzen_pattern: 1 (нумерованный список — 7 запретов/пунктов до оплаты)
dzen_shape_hint: «7 пунктов в договоре посуточно — за что удержат залог»

## Signal URLs (обязательные)
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/holyslav92 (tenant scout_signal_urls)

## topic_id / slug
topic_id: B03
slug_suggestion: dogovor-arendy-pravila-prozhivaniya-posutochno

## Задача Derouter Scout
Напиши handoff `.cursor/excalibur-blog-handoff.md` на русском. Поля:
wordstat_preflight, klyshin_hook (id | original | angle | signal), wordstat_rework (probe chain с частотами), wordstat (mcp_kv live | regions 55,11176,compare225 | P0 с частотой | P1…), season_note (лето YEKT), topic_id, slug, title_draft (ритм Klyshin, case hook, НЕ дублировать anti-dup), angle, anti_dup note, dzen_pattern, dzen_shape_hint, external_signal (1-2 предложения), signal_urls (список URL), article_dir suggestion.

title_draft: сцена «открыл договор после оплаты» или «в правилах мелким шрифтом» — НЕ копировать заголовок про вечеринки/предоплату (уже есть).

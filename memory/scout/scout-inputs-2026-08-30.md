# Scout inputs — 2026-08-30 YEKT slot (Добрый дом)

## Run context
- date: 2026-08-30 (воскресенье), timezone Asia/Yekaterinburg
- season: конец августа / начало сентября, командировочный сезон
- tenant: Добрый дом, посуточная аренда Тюмень
- queue slot: p0_queue window 2026-08-29 — 2026-08-31 → hook_id `sept_business_trip` (queue_num 2)

## Angle rotation (last N=3 published / recent WP)
Recent titles to NOT duplicate:
1. B01 — код/бесконтакт/дверь (burn-at-door) — SKIP family
2. B02 — залог/скол на плите — SKIP
3. B03 — вуз/«рядом»/родители сентябрь
4. WP 2026-08-30 — закрывающие после выезда (22:00 заселение + 10:00 созвон)
5. WP 2026-08-29 — розетки у стола нет
6. WP 2026-08-25 — где работать в квартире

**Fresh angle within sept_business_trip:** Wi‑Fi падает на видеосозвоне; в объявлении «быстрый интернет». Не розетки, не закрывающие, не «где сесть».

## Klyshin hook (bank)
- hook_id: sept_business_trip
- original: «Звонок в 10:00. Заселился в 22:00.»
- rework angle: «На созвоне пропал Wi‑Fi — в объявлении “быстрый интернет”»
- klyshin_signal: reader inside apartment on call; moral: сначала тест скорости/роутер, потом оплата; refusal beat
- dzen_pattern_prefer: [2, 3] — кейс с цифрой или страх→инструкция

## Wordstat preflight
- wordstat_preflight: mcp-kv wordstat_get_user_info OK (verified by director via MCP-KV 2026-08-30)
- DIRECTOR_ATTESTATION: live Wordstat probes below were fetched via MCP-KV wordstat_get_top_requests in this run. Use these frequencies as canonical. Do NOT emit WORDSTAT MCP BLOCKER.

## Wordstat live probes (MCP-KV)
| phrase | regions | volume |
|--------|---------|--------|
| командировка тюмень квартира | 55+11176 | ~0 (empty) |
| командировка тюмень квартира | 225 | 1 |
| командировка квартира посуточно | 225 | 61 |
| аренда квартиры посуточно | 55+11176 | 792 |
| аренда квартиры посуточно | 225 | 45932 |
| квартира посуточно тюмень | 55+11176 | 5500 |
| квартира посуточно тюмень | 225 | 12325 |
| закрывающие документы аренда квартиры | 225 | 30 |
| вайфай квартира посуточно | 225 | 13 |

## Wordstat rework log
probe «командировка тюмень квартира» 1 (225) / пусто (55+11176) →
probe «командировка квартира посуточно» 61 (225) →
probe «аренда квартиры посуточно» 792 (55+11176) / 45932 (225) →
probe «квартира посуточно тюмень» 5500 (55+11176) / 12325 (225) →
**final P0:** «квартиры посуточно тюмень» 5500 / 12325

Title rides P0 demand; article angle = Wi‑Fi на созвоне (business trip pain).

## External signal
- https://t.me/klyshin_A — delivery rhythm (§1 burn, short hits)
- site blog recent posts confirm saturation of rozetki/closing docs angles

## Constraints
- Voice: от лица компании «Добрый дом», комфорт+, не адвокат, не ЕГРН
- Funnel: TG after checklist, MAX after «у нас так»
- Phone: +7 993 574-83-22
- Cover: лето/конец августа, не зима
- topic_id: B04

## Title draft (Klyshin rhythm, NOT final H1)
«Звонок в 10:00. На третьей минуте Wi‑Fi умер — в объявлении “быстрый интернет”»

# Scout inputs — 2026-08-24 YEKT slot 06:00

## Run context
- date: 2026-08-24 (август, лето — обложка без зимы)
- tenant: Добрый дом / посуточная аренда Тюмень
- repo: holyslav92/Excalibur-SUBARENDA only

## Published anti-dup (titles only)
- B01: код/бесконтактное заселение
- B02: залог/скол на плите
- WP recent: паспорт, договор 7 запретов, отмена брони, вечеринки/лишние гости, ранний заезд, субаренда, уборка/залог, скрытые доплаты, соседи, цена «от»
- НЕ дублировать: коды/заселение, залог/скол на плите

## Klyshin hook (bank id: pets_short_term — NEW)
- original hook: «животные в договоре аренды — что прописать до подписания»
- angle: гость едет с собакой/кошкой посуточно; хозяин «на словах можно», в правилах — запрет или доплата на месте
- signal: https://t.me/klyshin_A (angle bank + buyer pain: пункт про животных в договоре)

## Wordstat live (MCP-KV, 2026-08-24)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

### RU 225 probes
| phrase | volume |
|--------|--------|
| посуточно с собакой | 1370 |
| квартиры посуточно с собакой | 647 |
| снять квартиру посуточно с собакой | 502 |
| аренда квартиры с животными | 1095 |
| аренда квартиры посуточно с животными | 45 |
| договор аренды квартиры с животными | 185 |
| пункт про животных в договоре аренды квартиры | 14 |

### Tyumen 55+11176 probes
| phrase | volume |
|--------|--------|
| аренда квартир посуточно тюмень | 210 |
| снять квартиру посуточно с собакой | 2 |
| аренда квартиры с животными | 4 |
| посуточная аренда (similar) | 2172 |

### Rework log
- probe «животные аренда квартиры» → buyer cluster «посуточно с собакой» 1370 (stronger than generic pets)
- probe «аренда квартиры посуточно с животными» 45 → rework to «снять квартиру посуточно с собакой» 502
- Tyumen weak on pet phrase → localize content to Тюмень посуточно; demand spine = national P0 «посуточно с собакой» 1370; supply = Тюмень only

## Final P0
- phrase: «посуточно с собакой»
- volume RU: 1370
- compare Tyumen: «аренда квартир посуточно тюмень» 210 (local anchor)
- stickers/H2 candidates: «снять квартиру посуточно с собакой» 502, «договор аренды с животными» 185, «доплата за животное» (rework)

## dzen_pattern
- pattern: 3 (страх → инструкция в §1)
- shape hint: «Еду с собакой — на заселении отказали / доплату взяли: что спросить до оплаты»

## Title draft (Klyshin rhythm, NOT final H1)
«Забронировал посуточно с собакой — на заселении сказали „не пускаем“»

## topic_id proposal
B03

## slug proposal
zabroniroval-posutochno-s-sobakoy-na-zaselenii-skazali-ne-puskayut

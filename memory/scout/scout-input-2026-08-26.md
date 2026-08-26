# Scout inputs — 2026-08-26 YEKT (Добрый дом)

## Run context
- date: 2026-08-26 (Asia/Yekaterinburg), season: late summer — NO winter hero on cover
- tenant: Добрый дом, посуточная аренда Тюмень, голос от лица компании (комфорт+)
- repo: Excalibur-SUBARENDA only; never tymenrieltor.ru

## Angle rotation (last N=3 WP titles)
1. «Гость снял квартиру на сутки: в 10:00 работал, к 22:00 искал кабель» — sept_business_trip SATURATED
2. «Приехали на 3 ночи к вузу — три остановки. Кровати не хватило» — parents_sept_uni SATURATED (queue slot 1 skip)
3. «Заселились посуточно — горячей воды нет» — hot_water SATURATED (parked)

## Anti-dup HARD (never repeat)
- B01 codes/beskontaktnoe-zaselenie
- B02 zalog/skол на плите (deposit on checkout)
- WP already: neighbors, dog, passport, hidden fees, cancel, early check-in, sublease, contract rules

## Queue pick (today window override)
- Skip queue slot 1 parents_sept_uni (WP dup 2026-08-25)
- Skip queue slot 2 sept_business_trip (WP dup 2026-08-25)
- **Pick hook_id: parking_before_booking** (queue 4) — NOT on WP, guest pain with car

## Klyshin hook
- id: parking_before_booking
- original: «Парковка рядом» — шлагбаум не пускает
- angle: место, пропуск, номер авто — до брони, не у барьера
- lockpick: «Где именно место и как въезд?»
- signal: https://t.me/klyshin_A (delivery rhythm, not copy deals)
- dzen_pattern_prefer: [3, 2]

## Wordstat live (MCP-KV, 2026-08-26)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes:
| phrase | regions | volume |
|--------|---------|--------|
| парковка аренда квартиры | 225 | 107 |
| аренда квартиры с парковкой | 225 | 53 |
| квартира посуточно тюмень | 55+11176 | 5875 |
| квартиры посуточно тюмень | 55+11176 | 5875 |
| снять квартиру посуточно в тюмени | 55+11176 | 1902 |
| аренда квартир посуточно | 225 | 46858 |
| аренда квартиры посуточно | 225 | 46858 |

Rework log:
- probe «парковка аренда квартиры» 107 (weak alone) →
- rework «квартира посуточно тюмень» 5875 (Tyumen buyer spine) +
- national «аренда квартиры посуточно» 46858 (context)
- final P0 «квартиры посуточно тюмень» 5875 | parking angle rides P0

## Topic assignment
- topic_id: B03 (next free after B01/B02)
- slug hint: parking-posutochno-shlagbaum-ne-puskaet
- title_draft hint: «Парковка рядом» написали в объявлении. У шлагбаума — «нет пропуска»

## Output required
Write `.cursor/excalibur-blog-handoff.md` with all scout handoff fields per SKILL.

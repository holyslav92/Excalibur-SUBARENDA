# Scout inputs — B13 slot 2026-09-07 YEKT 17:00

## Run context
- date: 2026-09-07 (Asia/Yekaterinburg)
- season: early September, summer/light — NO winter hero on cover
- tenant: Добрый дом / добрыйдом-72.рф
- slot: ONE guest-night CASE, not guide

## Published anti-dup (last 3 + WP today)
- B10: всё включено + 2 400 ₽ в такси
- B11: всё для гостей — без полотенец 890 ₽
- B12: тихий центр — кран в 6:30
- WP 2026-09-07: код к 22:30 не было (burn-at-door); ранний заезд у двери 4 часа
- B01: код от чужой двери
- SKIP burn-at-door family unless NEW angle

## Klyshin hook (original)
- parked hook_id: **parking_keybox** — mechanics only
- angle: бесконтакт / ключница — код сработал, но ключа нет (NOT wrong door, NOT no code in chat)
- delivery beats: quote → «Нет. Так не заселяем.» → lockpick question about keybox photo/test

## Wordstat (MCP-KV live, NOT invented)

### Probes
| phrase | regions | volume |
|--------|---------|--------|
| бесконтактное заселение посуточно | 55+11176 | 59 |
| бесконтактное заселение в квартиру посуточно | 55+11176 | 39 |
| бесконтактное заселение посуточно | 225 | 2993 |
| бесконтактное заселение | 225 | 11822 |
| аренда квартиры посуточно | 55+11176 | 710 |
| квартиры посуточно тюмень | 55+11176 | 5220 |
| квартиры посуточно тюмень | 225 | 11084 |

### Rework log
1. «ключница посуточно» → API empty (55+11176)
2. «ключница» → 69643 (225) but furniture bias — rework to guest cluster
3. «бесконтактное заселение посуточно» → 59 Tyumen / 2993 RU — guest P0 spine OK
4. Final P0: **квартиры посуточно тюмень** 5220 (55+11176) / 11084 (225) — demand spine; title rides keybox case on P0

## Topic decision
- topic_id: **B13**
- slug draft: `kod-srabotal-klyuchnitsa-pusta-posutochno-tyumen`
- title draft (two-beat): **«Код сработал. Открыли ключницу — внутри пусто»**
- subject: пустая ключница при бесконтактном заселении
- angle: гость у правильного подъезда, код открыл ящик, ключа нет — 23:40, такси уехало
- dzen_pattern: 2 (case_with_sums_and_dates)
- wp_category_slugs: suggest posutochno / zaselenie

## Signal URLs
- https://t.me/klyshin_A (angle only)
- https://добрыйдом-72.рф/blog/

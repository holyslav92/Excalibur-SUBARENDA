# Scout inputs — B04 slot 2026-08-29 YEKT 14:00

## Date / season
- EXCALIBUR_RUN_DATE=2026-08-29 (YEKT summer, август)
- Cover season: лето, НЕ зима

## Angle rotation (last N=3 published in ledger)
- B01: burn-at-door / код заселения
- B02: залог / скол на плите
- B03: вуз / «рядом»

## Live WP dedupe (today + recent — do NOT reuse)
- 2026-08-29: zvonok-v-10-00-zaselilsya-v-22-00-stol-est-rozetki-net — командировка, розетки (sept_business_trip SATURATED)
- dve-nochi-otel-ili-kvartira-posutochno — отель vs квартира
- sobral-chemodan-v-kvartire-net-polotenec — полотенца
- kvartira-posutochno-v-centre-tyumeni-tihij-rajon-ili-strojka-za-oknom — тихий центр
- kvartira-posutochno-kuhnya-est-ili-kazhdyj-den-kafe — кухня
- na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super — отзывы
- vyezd-v-12-00-poezd-v-16-30-chemodany-ne-v-taksi — багаж/поезд
- parkovka-u-shlagbauma-posutochno — парковка
- zvonok-v-10-00-zaselenie-v-22-00-gde-rabotat-v-kvartire-posutochno — командировка/work
- zaselilis-posutochno-goryachej-vody-net — горячая вода

## Queue window 29–31.08
- queue hook `sept_business_trip` — SKIP: already live on WP today (rozetki article)
- Pick parked hook `cancel_prepay` — fresh guest pain, NOT on live WP

## Klyshin hook (parked)
- hook_id: cancel_prepay
- original: «Перевёл предоплату вечером. Утром — «квартира уже занята».»
- angle: сколько и когда платить, как зафиксировать бронь до перевода — не после ссоры
- lockpick: «Кому именно переводим и что в переписке до денег?»
- signal: https://t.me/klyshin_A

## Wordstat live (MCP-KV, preflight OK)
- wordstat_preflight: mcp-kv wordstat_get_user_info OK
- probe «предоплата за аренду квартиры посуточно» → 42 (RU 225)
- probe «предоплата аренда квартиры посуточно» → 65 (RU 225)
- probe «отмена брони посуточно» → 102 (RU 225)
- probe «аренда квартиры посуточно» → 794 (55+11176), «аренда квартиры тюмень посуточно» → 208
- rework: weak prepay alone → anchor to high-volume P0 «аренда квартиры посуточно» 794 Tyumen + prepay fear sub-cluster
- final P0: «аренда квартиры посуточно» 794 (55+11176) | compare RU «аренда квартиры посуточно» national context

## Dzen
- dzen_pattern: 3 (страх → инструкция в §1)
- dzen_shape_hint: «перевёл предоплату — квартира «занята»: что спросить до перевода»

## Tenant
- Добрый дом, посуточная Тюмень, голос от лица ПК компании
- Forbidden: коды/заселение (B01), залог/плита (B02), ЕГРН, суд, «мы лучшие»

## topic_id
- B04

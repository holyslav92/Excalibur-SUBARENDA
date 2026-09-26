# Scout assembled inputs — B03 (2026-09-26 YEKT)

**Роль:** ты уже запущен как Derouter utility (`gpt-5.6-terra`) через `excalibur_blog_derouter_opus_chat.py --role scout`.  
**Ответ:** только готовый markdown handoff (поля ниже). **Запрещено** отвечать `DEROUTER SCOUT BLOCKER` — Wordstat и preflight уже выполнены Cursor.

Слот: Добрый дом. Setup complete. Scout only.

## Задача директора

ОДНА гостевая боль (НЕ юр Клышин): **бойлер / горячая вода в первую ночь** посуточно.
topic_id: **B03**. H1 — двухтактный **case** (не гайд, не «N шагов» в заголовке).

## Anti-dup (recent WP + B01/B02)

Запрещённые углы/H1: код/чужая дверь (B01), залог не вернули (B02), залог после уборки, предоплата 4200, собака 3000, PDF подъезд, комиссия на экране, минимум 2 суток, без залога у двери, менеджер у двери, Авито второй перевод, цена карточка vs оплата, чужие чемоданы.

## klyshin_hook (angle mechanics only)

hook_id: `guest_boiler_hot_water_first_night`
original: «первая ночь посуточно — в душе ледяная вода, бойлер не прогрелся»
angle: в карточке «есть душ / горячая вода» → гость платит → в первую ночь только холодная или бойлер «до утра»; что спросить в чате и что зафиксировать до оплаты (без юр-канцелярита).
signal: https://t.me/klyshin_A (ритм угла, не копировать сделки канала)

## Wordstat live MCP-KV (2026-09-26)

wordstat_preflight: wordstat_get_user_info OK

Probes (RU 225 unless noted):
- «горячая вода квартира посуточно» → totalCount **28** (weak, no top list)
- «горячая вода посуточно» → totalCount **39** (weak)
- «нет горячей воды посуточно» → totalCount **19** (weak)
- «бойлер квартира посуточно» → totalCount **2** (weak)
- «нет горячей воды в квартире аренда» → totalCount **8** (weak)
- «квартиры посуточно тюмень» → **9221** RU225; **4209** regions 55+11176 (top: снять квартиру посуточно в тюмени 1191 / 3143 RU)
- «снять квартиру посуточно в тюмени» → **1191** 55+11176; **3143** RU225

Rework: слабый объём на «горячая вода» не drop — локализация Тюмень + buyer spine посуточно.
**final P0:** «квартиры посуточно тюмень» **4209** (55+11176), compare RU225 **9221**.

P1 stickers (live): «снять квартиру посуточно в тюмени» 1191 (55+11176).

## Dzen

dzen_pattern: **2** (кейс с суммами/сценой первой ночи)
dzen_shape_hint: «заселился / оплатил → открыл душ → ледяная вода и бойлер»

## External signal (today)

signal_urls (≥2):
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Slug hint

`pervaya-noch-posutochno-holodnaya-voda-boyler-tyumen`

## Title draft direction (two-beat case, for handoff)

Пример формы (Derouter может уточнить, сохранить двухтакт): «Заселился посуточно. В душе — ледяная вода, а бойлер молчит»

Напиши полный `.cursor/excalibur-blog-handoff.md` по чеклисту skill: wordstat_preflight, klyshin_hook, wordstat_rework (цепочка probe→…→final P0), wordstat line, topic_id B03, slug, title_draft, dzen_pattern, season_note (YEKT 2026-09-26 осень), anti_dup, angle, article_dir hint `memory/blog/articles/B03-pervaya-noch-posutochno-holodnaya-voda-boyler-tyumen`

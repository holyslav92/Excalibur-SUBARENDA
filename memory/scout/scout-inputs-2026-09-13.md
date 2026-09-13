# Задание Scout-handoff (Derouter utility) — B19

Ты — Scout Derouter. Все Wordstat-данные уже собраны дирижёром через MCP-KV.
**Не** проверяй окружение и **не** пиши BLOCKER. Сформируй handoff по skill.
Return ONLY the handoff markdown body (no refusal, no DEROUTER SCOUT BLOCKER).

## Дата и слот
- today: 2026-09-13 (Asia/Yekaterinburg), воскресенье, ранняя осень
- season_visual: сентябрь, тёплый вечер, листья жёлтые — НЕ зима
- topic_id: **B19**
- director angle: **запах сигарет / «не курили» в объявлении → гость зашёл и застрял с вонью** (guest CASE, not guide)

## Published titles B01–B18 (anti-dup)

См. shared/published-titles.md — полный ledger.

### Last N=3 (angle rotation)
- B18: код/домофон/подъезд 20 мин
- B17: коммуналка/счётчики 1 840 ₽
- B16: рейс отменили/предоплата 4 200 ₽

### Live catalog — НЕ дублировать (grep 2026-09-13)
Код/ключница/домофон, залог/скол/без залога, предоплата/тишина/рейс, бойлер/горячая вода (5+ статей), собака, дети, соседи/музыка, парковка, кухня/кафе, Wi‑Fi, коммуналка, лифт, тепло/батареи, постельное/матрас, ранний заезд, уборка-списание, паспорт, субарендатор, отель vs шум.

**Свободный угол:** запах/курение/«не курили» — в live-catalog **нет**.

## Angle rotation
- burn-at-door: skip (B18 последний из семьи входа)
- skip_last5: hot_water, neighbors, dog, hidden_fees — не брать
- B19 = **smoke_smell_checkin** — сенсорный кейс внутри квартиры, не у двери

## Klyshin hook (guest pain, mechanics only)

- hook_id: **smoke_smell_checkin**
- original: «В объявлении — «не курили». Зашли — запах сигарет и окно на замке.»
- angle: маркетинг «чистая/не курили» vs реальность при заселении; гость уже внутри, окно не открывается, ночь с детьми/аллергией
- lockpick: «Когда последний раз здесь курили и можно ли проветрить до оплаты?»
- refusal beat: «Нет. Так не заселяем.» / «Не «по фото чисто». Не «на словах». А запах при открытой двери.»
- klyshin_signal: moral «сначала проверка воздуха/окон, потом ночь» — ритм Клышина, не Москва/ЕГРН
- signal URL: https://t.me/klyshin_A
- dzen_pattern: **2** (кейс с суммами и датами)
- dzen_shape_hint: «Написали «не курили». В спальне — запах и окно на замке»

## Wordstat (MCP-KV live, 2026-09-13)

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-13)

| probe | region | volume | note |
|-------|--------|--------|------|
| курение квартира посуточно | 225 | 54 | guest cluster, weak |
| запрет курения аренда квартиры | 225 | 46 | related |
| запах в квартире посуточно | 225 | 12 | vanity |
| стиральная машина квартира посуточно | 225 | 38 | alt angle, skip |
| аренда квартиры посуточно | 55+11176 | 664 | guest spine |
| квартиры посуточно тюмень | 55+11176 | **4826** | **final P0** |
| квартиры посуточно тюмень | 225 | 10385+ | compare RU |

wordstat_rework: probe «курение квартира посуточно» 54 (225) → «запрет курения аренда квартиры» 46 → «запах в квартире посуточно» 12 → localize «аренда квартиры посуточно» 664 (55+11176) → **final P0 «квартиры посуточно тюмень» 4826 (55+11176)** | compare RU 10385

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4826 | «аренда квартиры посуточно» 664 | «курение квартира посуточно» 54 (225)

## Topic assignment
- topic_id: B19
- title_draft (two-beat): «Написали «не курили». В спальне — запах и окно на замке»
- slug_hint: napisali-ne-kurili-v-spalne-zapah-i-okno-na-zamke

## Signal URLs (≥2)
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Tenant
Добрый дом, посуточная Тюмень. CASE 1100–1800 слов. PR #52 shape HARD.

Напиши полный handoff со всеми обязательными полями из skill: topic_id, title_draft, dzen_pattern, dzen_shape_hint, klyshin_hook, wordstat_preflight, wordstat_rework, wordstat, angle_rotation, signal_urls, external_signal, opening_direction, moral, lockpick_question, anti_dup_guard, bank_update, cover_hint, case_number, dialogue_beat, verdict, article_structure, local_supply_frame.

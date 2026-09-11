# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-11 YEKT (Добрый дом, B17)

## Дата и слот
- today: 2026-09-11 (Asia/Yekaterinburg), пятница, сентябрь
- season: осень — обложка без зимних сугробов
- slot: B17, post-queue window (after 08–10.09 batch)

## Published titles (anti-dup, B01–B16)
B01 код/заселение, B02 залог-скол на плите, B03 вуз рядом, B04 третий гость, B05 отзывы, B06 выезд/багаж, B07 кухня/кафе, B08 предоплата тишина, B09 парковка, B10 всё включено/такси, B11 полотенца, B12 тихий центр/кран, B13 код/ключница, B14 соседи/музыка, B15 wifi/рабочий стол, B16 отмена рейса/возврат предоплаты

WP recent (не повторять близкие H1): собака доплата, отель дороже, wifi, дети доплата, уборка списание, без залога у двери, горячая вода/бойлер

## Angle rotation (last N=3)
- B16: отмена рейса / возврат предоплаты
- B15: wifi / рабочий стол / командировка
- B14: соседи / музыка ночью

**Skip families:** cancel/prepay refund (B16), wifi/desk (B15), neighbors (B14), burn-at-door (B01/B13), залог-скол (B02), «без залога у двери» (WP)

## Queue decision
- **Selected:** `deposit_cleaning_deferral` (parked hook, new angle) — залог обещали вернуть утром, утром «после уборки»
- NOT duplicate B02 (скол на плите) — здесь квартира сдана чисто, спор про срок возврата
- NOT duplicate WP «списали за уборку» — здесь залог держат, не мгновенное списание

## Klyshin hook (guest pain, NOT legal)
- hook_id: `deposit_cleaning_deferral`
- original: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»
- angle: гость сдал ключи вовремя, квартира чистая; хозяин переносит возврат залога на «после уборки» без срока
- klyshin_signal (mechanics only): reader inside; number = 5 000 ₽ + утро после выезда; moral: сначала срок и способ возврата залога в переписке, потом ключи
- lockpick_question: «В какой день и на какой счёт вернёте залог, если квартира сдана чистой?»
- refusal beat: «Нет. Так не заселяем.» / «Сначала срок возврата залога. Потом перевод. Не наоборот.»
- dzen_pattern: **2** — кейс с суммами и датами
- dzen_shape_hint: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»

## Title draft (two-beat stop-factor, для handoff)
**«Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»**

- slug_hint: `zalog-5-000-obeshchali-vernut-utrom`
- НЕ использовать: скол на плите (B02), без залога у двери, предоплата/отмена (B16), код/ключница

## Wordstat (MCP-KV live, 2026-09-11)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

### Probes и rework
| probe | Tyumen 55+11176 | RU 225 |
|-------|-----------------|--------|
| залог посуточно | 34 | 2973 |
| квартиры посуточно залог | 25 | 1866 |
| квартиры посуточно без залога | 9 | 1151 |
| не вернули залог за квартиру посуточно | 2 | 40 |
| залог вернуть посуточно | — | 182 (cluster) |
| квартиры посуточно тюмень | **4929** | **10527** |

wordstat_rework: probe «залог посуточно» 34 (55+11176) / 2973 (225) → «квартиры посуточно залог» 25 / 1866 → «не вернули залог за квартиру посуточно» 2 / 40 → final P0 «квартиры посуточно тюмень» 4929 (55+11176) | compare 10527 (225) | clusters tried: залог посуточно, залог квартиры посуточно, возврат залога, квартиры посуточно Тюмень

## Topic assignment
- topic_id: **B17**
- priority: P0
- article format: CASE 1100–1800 слов, не гайд

## Case spine (для Writer)
1. Пара снимает квартиру посуточно в Тюмени на 2 ночи — командировка + прогулка.
2. При брони: залог 5 000 ₽, в чате «вернём утром после выезда в 12:00».
3. Выезд вовремя, ключи в ключнице, квартира чистая, фото отправили.
4. Утром в 10:00 пишут: «Залог вернём после уборки» — без даты и суммы.
5. Burn: 5 000 ₽ заморожены; гость уже в такси на вокзал.
6. Lockpick: срок и способ возврата залога до заселения.
7. Moral: сначала фиксируем в переписке день и способ возврата залога при чистой сдаче, потом ключи.

## Signal URLs (обязательно)
- https://t.me/klyshin_A — rhythm «сначала проверка/срок, потом деньги»
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Tenant
Добрый дом, посуточная Тюмень, голос тёплого хоста, не риэлтор, не Клышин сделки/Москва.

## Handoff format
Полный handoff как B16: секции Topic, Title draft, Dzen shape, Klyshin hook, Case spine, Wordstat, Angle rotation, External signal, bank_update.

Обязательные строки:
```
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: deposit_cleaning_deferral | original: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»» | angle: ... | signal: https://t.me/klyshin_A
wordstat_rework: ...
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4929 | ...
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: ...
```

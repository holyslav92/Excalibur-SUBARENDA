# Klyshin topic bank — Добрый дом (посуточная / субаренда)

Банк seed-хуков для Scout × Wordstat dual gate. Klyshin = **angle** (ритм,
«кажется просто → риск»), не копирование сделок с авансом/ЕГРН.

**Тенант:** посуточная аренда и субаренда в Тюмени.  
**Wordstat:** MCP-KV, regions 55+11176, compare RU 225.

См. `memory/scout/klyshin-topic-bank.json` для machine-readable hooks + P0 queue.

## Rework vocabulary (guest daily-rental ONLY)

посуточно, залог, заселение, уборка, парковка, вайфай, командировка,
студент, вуз, отзывы, кухня, выезд, багаж, тюмень, суточно, бронирование.

**Запрещено в rework:** егрн, наследство, ипотека, новостройка, маткапитал,
аванс сделки, нотариус, банкротство, риэлтор.

## Skip families (HARD — near-term)

**Burn-at-door:** код / бесконтакт / «оплатил — дверь не та» — saturated.

**Last-5 used family (skip until new angle):** hot water / neighbors / extra fees /
dog / passport (паспорт при заселении).

**Also skip:** early check-in (already used), hidden-fees article angle (duplicate
`hidden_fees` — kitchen vs hotel is **contrast**, not «доплата на месте»).

Перед выбором hook — `shared/published-titles.md` (последние N=3).

Prefer **high-volume guest P0** (Wordstat 55+11176, compare 225).

**Dzen pattern 1** (N советов) — **NOT default**. Prefer 2–5.

---

## P0 queue — 26.08–10.09 YEKT

| window (YEKT) | queue # | hook_id | topic |
|---------------|---------|---------|-------|
| 26–28.08 | 1 | `parents_sept_uni` | ✅ B03 handoff 2026-08-28 — P0 «квартиры посуточно тюмень» 5534 |
| 29–31.08 | 2 | `sept_business_trip` | Командировка в сентябре: стол, розетки, реальный Wi‑Fi, закрывающие |
| 01–03.09 | 5 | `reviews_not_rating` | ✅ B05 published 2026-09-01 — отзывы не звёзды |
| 04–07.09 | 4 | `parking_before_booking` | Парковка до брони, не у шлагбаума |
| 08–10.09 | 3 | `kitchen_vs_hotel_cafes` | ✅ B07 published 2026-09-02 — кухня vs кафе 7 200 ₽ |
| 08–10.09 | 6 | `pack_vs_flat` | ✅ B08 published 2026-09-02 — P0 «квартиры посуточно тюмень» 5363; полотенца на четверых |
| 08–10.09 | 8 | `checkout_train_bags` | ✅ B06 handoff 2026-09-01 — P0 «квартиры посуточно тюмень» 5446; angle хранение багажа 133/28 |
| 08–10.09 | 7 | `quiet_center_maps` | «Тихий центр»: 7 минут в Картах/панорамах |

Scout берёт **только** hook из активного окна (today YEKT ∈ window). После handoff —
stamp `queue_slot` + `used_in_articles` в JSON.

---

## 8 near-term hooks (Klyshin rhythm, guest topics)

| id | hook (сцена) | angle / lockpick | wordstat probe hint |
|----|--------------|------------------|---------------------|
| `parents_sept_uni` | Привёз сына в вуз. Три ночи. В объявлении — «рядом с вузом». | Не годовая аренда. Что проверить кроме «рядом»? | квартира посуточно тюмень / аренда на несколько дней / студент |
| `sept_business_trip` | Звонок в 10:00. Заселился в 22:00. | Стол, розетки, Wi‑Fi на созвон, закрывающие — до оплаты | командировка тюмень квартира / аренда квартиры посуточно |
| `kitchen_vs_hotel_cafes` | Три ночи. Кухня «есть» — или каждый день кафе? | Контраст+цифра. **≠** hidden-fees / доплата на месте | посуточно или отель / квартира с кухней посуточно |
| `parking_before_booking` | «Парковка рядом» — шлагбаум не пускает | Место, пропуск, номер — **до** брони, не у барьера | парковка аренда квартиры / аренда квартиры посуточно тюмень |
| `reviews_not_rating` | 4.8 — и два одинаковых «всё супер» | Повторы, свежесть, Sutochno/Avito — не звёзды | отзывы аренда квартиры / суточно отзывы |
| `pack_vs_flat` | Собрал чемодан — в квартире нет полотенец | Что везти vs что обязано быть в объявлении | что нужно для аренды квартиры / квартира посуточно |
| `quiet_center_maps` | «Тихий центр» — за окном стройка | 7 минут пешком в Картах/панорамах, не слова хоста | аренда квартиры тюмень центр / квартира посуточно |
| `checkout_train_bags` | Выезд в 12:00. Поезд в 16:30. | Куда чемоданы — **не** early check-in | поздний выезд аренда / хранение багажа |

## Anti-dup

Не повторять заголовки из `shared/published-titles.md` и
https://добрыйдом-72.рф/blog без нового угла.

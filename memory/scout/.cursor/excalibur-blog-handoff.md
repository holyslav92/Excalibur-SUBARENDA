# .cursor/excalibur-blog-handoff.md

```markdown
# Scout handoff — B35

topic_id: B35
brand: Добрый дом
market: посуточная аренда комфорт+
date: 2026-09-23 17:00 YEKT

## Topic

Гость выбирает объявление с фильтром «от хозяев» и ожидает прямого заселения без посреднической доплаты. На месте его встречает менеджер с ключами и просит ещё 2 000 ₽ переводом на карту — суммы, которой не было в бронировании.

Главный вопрос материала: кто именно заселяет гостя и что входит в цену, указанную при бронировании?

## Title draft

«От хозяев» в фильтре. У двери менеджер: ещё 2 000 ₽ на карту

slug_draft: ot-hozyaev-v-filtre-u-dveri-menedzher-eshche-2000-na-kartu

## Dzen angle

dzen_pattern: 4
dzen_shape_hint: «Выбрали “от хозяев” — а у двери не хозяин, а менеджер с QR и суммой, которой не было в брони»

Контраст: обещание прямого контакта в карточке объявления против фактического заселения через посредника и неожиданной доплаты.

## Klyshin hook

klyshin_hook: no_intermediary_manager_door
original: «кажется прямой контакт → на пороге чужой посредник и доплата»
angle: фильтр «без посредников / от хозяев» против человека с ключами и перевода на карту «за заселение»
signal: https://t.me/klyshin_A

Клышинский механизм используется как драматургический каркас, а не как источник фактов для копирования: гость верит фильтру, приезжает в квартиру и только у двери узнаёт, что общается не с хозяином.

## Wordstat

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-23)

wordstat_rework: probe «ночной заезд посуточно» totalCount 15 (225, weak) → «отмена брони посуточно» 63 (225) → «залог посуточно» 2592 (225) saturated B34 → «квартиры посуточно без посредников» 43518 (225) + «квартира без посредников от хозяев посуточно» 14485 (225) → Tyumen spine «квартиры посуточно тюмень» 4304 (55+11176) + «квартиры посуточно тюмень без посредников» 237 (55+11176) | clusters: посредник, от хозяев, заселение, доплата на месте (NOT legal/EGRN)

wordstat: mcp_kv live | regions 55,11176,compare225 | final P0 «квартиры посуточно без посредников» 43518 (225) | Tyumen «квартиры посуточно тюмень» 4304 (55+11176) | supporting «посредник квартир посуточно» 43591 (225)

P0 demand spine: «квартиры посуточно без посредников» — 43 518, Россия, регион 225.

Tyumen supply spine: «квартиры посуточно тюмень» — 4 304, регионы 55 + 11176.

Supporting query: «посредник квартир посуточно» — 43 591, регион 225.

Интерпретация: основной спрос федеральный и гостевой — поиск посуточной квартиры без посредников. Локальная часть материала — не отдельный брендовый запрос, а supply-угол про посуточное заселение в Тюмени.

## Angle rotation

angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B32 — price stack, B33 — Avito double pay, B34 — залог у двери; код/ключница и залоговый сценарий не повторяются

Новый угол B35: посредник у двери после выбора фильтра «от хозяев». Он отличается от B34: конфликт строится не вокруг залога и не вокруг кода доступа, а вокруг несоответствия между обещанным прямым контактом и фактическим участником заселения.

## Article brief

### Opening

Начать с плотного кейса на 1–2 абзаца от лица гостя:

гость выбирает вариант с пометкой «от хозяев» или «без посредников», рассчитывает на указанную в карточке цену и приезжает в Тюмень. У двери его встречает менеджер, показывает QR-код и сообщает о дополнительной оплате 2 000 ₽ «за заселение» или «за передачу ключей».

После объяснения менеджера — короткий перелом:

«Это не было указано в брони».

«Нет. Так не заселяем».

Не использовать вертикальную лестницу из коротких строк в открытии.

### Кейс

Один кейс — один вывод. Не смешивать его с залогом, кодом от двери или спором о возврате денег.

Ключевой lockpick-вопрос гостя:

«Кто заселяет — хозяин или агент? И что входит в цену на сайте?»

### Мораль

Сначала проверить, кто принимает гостя и входит ли эта услуга в опубликованную цену. Затем — деньги и ключ:

- имя и роль человека, который будет заселять;
- финальная сумма до подтверждения брони;
- наличие отдельной платы за заселение, уборку или передачу ключей;
- способ оплаты и подтверждение платежа;
- что произойдёт, если фактическая сумма окажется выше суммы бронирования.

### Checklist

Чеклист разместить после морали и кейсов. Не превращать материал в юридическую консультацию.

## Editorial constraints

- Reader is a guest, not a host-operator.
- Demand spine: guest intent «квартиры посуточно без посредников».
- Supply: only Tyumen, посуточная аренда «Добрый дом».
- Number is the price of the guest’s mistake: 2 000 ₽.
- Host/aggregator dialogue must include quote, then refusal beat: «Нет. Так не заселяем.»
- One case → one verdict.
- Moral order: first X (who receives and what is included), then money/key.
- Do not copy Moscow, Dubai, MKAD, EGRN, phone numbers or deals from Klyshin.
- Do not use legal hook-bank topics.
- Do not add unsupported facts about a specific booking, address, platform or employee.
- Do not build the article around the brand query «Добрый дом Тюмень».

## Verdict

Если объявление обещает «от хозяев» и «без посредников», гость должен заранее понимать, кто его заселяет и за что он платит. Доплата в 2 000 ₽ у двери — не мелочь, а цена того, что условия бронирования не были проверены до приезда.

## External signal

external_signal: Klyshin hook about a seemingly direct contact turning into a meeting with an intermediary and an extra payment at the door, combined with live guest demand for apartments without intermediaries

signal_urls:
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/

## Bank update

last_seen: 2026-09-23
wordstat_rework_log: weak probe on night check-in → cancellation and deposit probes → saturated deposit angle from B34 → high-demand guest cluster «квартиры посуточно без посредников» → Tyumen spine «квартиры посуточно тюмень»
final_p0: «квартиры посуточно без посредников» — 43 518, Россия, регион 225
used_in_articles: B35
rotation_note: intermediary-at-door is new after B32 price stack, B33 Avito double pay and B34 deposit-at-door; avoid repeating deposit/code/keypad framing
```

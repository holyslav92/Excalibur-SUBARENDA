# Scout inputs — 2026-09-24 YEKT slot 12:00 UTC

## Published titles (last 3 — angle rotation)
- B34: В фильтре — «без залога». У двери попросили 5 000 ₽ на личную карту
- B33: Бронь на Авито уже оплачена. В чате: второй перевод на карту
- B32: В карточке 3 400 ₽ за ночь. На оплате — 8 816 ₽ за две ночи

## Anti-dup (published + WP recent — НЕ повторять угол)
НЕ: код/ключница/домофон (B01,B13,B18); залог у двери/без залога (B34,B02); второй перевод в чате после оплаты (B33); стек цены за ночь+итог (B32); минимум суток при оплате одной ночи (live oplachena-odna-noch-minimum-dvoe-sutok); залог утром после уборки (live).

## Klyshin hook (original — mechanics only)
«В карточке написали «без комиссии». На последнем шаге оплаты сервис всё равно добавил строку — и сумма выросла.»

## Angle
Гость в Тюмени бронирует на Авито/агрегаторе: в фильтре и карточке акцент «без комиссии» / «цена как у хозяина», на экране подтверждения оплаты появляется **сервисная комиссия платформы** (не перевод хозяину в чат). Контраст: скрин фильтра vs итог «к оплате». Lockpick: «Где в карточке строка про комиссию сервиса и можно ли увидеть итог до брони?»

## Wordstat (live MCP-KV 2026-09-24)

### Preflight
wordstat_get_user_info OK

### Rework log
1. probe «комиссия посуточно» → 1832 (225); «авито посуточно комиссия» → 1024 (225)
2. probe «квартиры посуточно без комиссии» → 314 (225)
3. probe «квартиры посуточно тюмень» → 4274 (55+11176)
4. weak local on «без комиссии» alone → spine P0 Tyumen + sub-angle Avito checkout fee

### Final P0
- phrase: **квартиры посуточно тюмень**
- volume_tyumen: 4274
- volume_ru: (spine; compare via квартиры посуточно тюмень cluster)
- supporting: **авито посуточно комиссия** 1024 (225); **квартиры посуточно без комиссии** 314 (225)

## angle_rotation
checked last N=3 | burn-at-door skip: yes (B34 door payment) | reason: payment-stack family but NEW angle = platform commission on checkout screen, NOT zalog at door, NOT second chat transfer (B33)

## dzen_pattern
2 (кейс с суммами)

## dzen_shape_hint
«без комиссии» в фильтре → строка сервиса на оплате + ₽

## Title draft (two-beat, NOT how-to)
**В фильтре — «без комиссии». Перед оплатой сервис добавил 1 187 ₽**

## topic_id
B35

## slug
v-filtre-bez-komissii-pered-oplatoj-servis-dobavil-1187

## hook_id
no_commission_filter_checkout_fee

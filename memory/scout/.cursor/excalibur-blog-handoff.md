# EXCALIBUR BLOG HANDOFF — B13

## 1. Topic

- **topic_id:** B13
- **slot:** B13
- **tenant:** Добрый дом, посуточная Тюмень
- **date:** 2026-09-07
- **season:** начало сентября, осень (НЕ зима на обложке)
- **priority:** P0
- **topic status:** approved
- **guest intent:** снять квартиру посуточно с ранним заездом после ночного поезда
- **supply localization:** посуточные квартиры и работа хоста в Тюмени
- **article format:** CASE, 1100–1800 слов, не гайд
- **voice:** тёплый хост Добрый дом, без тона риэлтора

## 2. Title draft

**Поезд в 07:20. Написали: «заезд только с 14:00»**

- **slug_hint:** `poezd-v-07-20-napisali-zaezd-tolko-s-14-00`
- **title mechanics:** two-beat stop-factor; нормальный план → удар окном заселения
- **H1 angle:** ночной поезд прибыл утром, хозяин держит ключ до 14:00
- **не использовать в заголовке:** код, залог, парковка, кухня, предоплата, тихий центр, соседи

## 3. Dzen shape

- **dzen_pattern:** 2 — кейс с суммами и датами
- **dzen_shape_hint:** «Поезд в 07:20. Написали: «заезд только с 14:00»»
- **opening:** плотный кейс в 1–2 абзацах; семья с чемоданами у подъезда в +9 °C, ребёнок спит на коленях
- **запрет:** вертикальная лестница, how-to H1, encyclopedia §1

## 4. Klyshin hook

- **hook_id:** `early_checkin`
- **original:** parked_hooks early_checkin — гость приехал раньше окна заселения
- **angle:** поезд/рейс утром, хозяин держит ключ до 14:00; где ждать и что спросить ДО оплаты
- **lockpick question:** «Можно зайти в 8:00, если уеду в 8:00?»
- **refusal beat:** «Нет. Так не заселяем.» / «Сначала окно заезда в письме. Потом перевод.»
- **moral rhythm:** сначала письменное окно заезда/выезда и ранний заезд, потом оплата

## 5. Case spine

1. Семья из двух взрослых и ребёнка бронирует квартиру посуточно в Тюмени на 2 ночи (~8 400 ₽).
2. Ночной поезд прибывает в 07:20; в объявлении «бесконтактное заселение».
3. После оплаты хозяин пишет: «ключ с 14:00, раньше нельзя».
4. На вокзале холодно (+9 °C), такси до квартиры 420 ₽ — у двери ждут 4+ часа или платят отель ~3 200 ₽.
5. Lockpick: «Можно зайти в 8:00, если уеду в 8:00?»
6. Refusal: «Нет. Так не заселяем.»
7. Вердикт: до оплаты — письменное окно заезда и условия раннего заезда.
8. Checklist — только после морали.

## 6. One case → one verdict

**Вердикт:** окно заезда — не мелочь в чате после перевода. До оплаты гость просит письменно: с какого часа ключ и что с ранним заездом. Сначала окно, потом деньги.

## 7. Wordstat

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5235 | compare 11220 (225) | «ранний заезд посуточно» 316 (225) | «квартиры посуточно ранний заезд» 229 (225)
```

### Demand spine

- **final P0:** «квартиры посуточно тюмень»
- **volume:** 5235 (55+11176)
- **national comparison:** 11220 (225)

### Rework log

```text
wordstat_rework: probe «соседи шум посуточно» 47 (225) host bias → «ранний заезд посуточно» 316 (225) → «квартиры посуточно ранний заезд» 229 (225) / 4 (55+11176) → «снять квартиру посуточно с ранним заездом» 95 (225) → final P0 «квартиры посуточно тюмень» 5235 (55+11176) | compare 11220 (225) | clusters tried: соседи шум, ранний заезд, квартиры посуточно Тюмень
```

## 8. Angle rotation

```text
angle_rotation: checked last N=3 | burn-at-door skip: no | reason: B10 всё включено, B11 полотенца, B12 тихий центр; B13 — ранний заезд после поезда, не дублирует B06 поздний выезд/чемоданы, B01 код/заселение, B08 предоплата
```

## 9. External signal

- **signal_urls:**
  - https://t.me/klyshin_A
  - https://добрыйдом-72.рф/blog/
  - https://t.me/Dobriy_dom_72

```text
klyshin_hook: early_checkin | original: parked_hooks early_checkin — гость приехал раньше окна заселения | angle: поезд утром vs ключ с 14:00 | signal: https://t.me/klyshin_A
```

## 10. Final handoff lines

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: early_checkin | original: parked_hooks early_checkin — гость приехал раньше окна заселения | angle: поезд утром vs ключ с 14:00 | signal: https://t.me/klyshin_A
wordstat_rework: probe «соседи шум посуточно» 47 → «ранний заезд посуточно» 316 → «квартиры посуточно ранний заезд» 229 → final P0 «квартиры посуточно тюмень» 5235 | clusters tried: соседи шум, ранний заезд, квартиры посуточно Тюмень
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5235 | compare 11220 (225)
angle_rotation: checked last N=3 | burn-at-door skip: no | reason: новый угол ранний заезд; не дублирует B06–B12
topic_id: B13
title_draft: Поезд в 07:20. Написали: «заезд только с 14:00»
slug: poezd-v-07-20-napisali-zaezd-tolko-s-14-00
dzen_pattern: 2
signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/, https://t.me/Dobriy_dom_72
```

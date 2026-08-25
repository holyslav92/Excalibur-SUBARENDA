# Title inputs — B03

**Role:** title (Derouter Terra)  
**Date:** 2026-08-25  
**Tenant:** Добрый дом — посуточная аренда Тюмень  
**topic_id:** B03  
**slug:** posutochno-u-vuza-roditeli-s-pervokursnikom-na-3-nochi-ne-na-semestr

## Klyshin hook (original, Scout)

Родители везут первокурсника ~1 сентября: 2–4 ночи, НЕ семестр.  
Ожог: «рядом с вузом» в объявлении vs две кровати, кухня, стиралка, 2ч разгрузка у парковки, честный check-in.

## Wordstat demand spine (pinned P0)

- **Final P0:** `квартира посуточно возле вуза` (volume TBD — Wordstat partial)
- **Clusters:** снять квартиру 1 сентября / жилье родители первокурсник
- **Regions:** 55+11176 (Tyumen); RF-wide compare 225
- Title rides P0 under the surface — no raw SEO phrase in H1

## Dzen pattern (Scout)

`local_seasonal_tyumen_hook` + `case_with_sums_and_dates`  
Prefer shapes 2–3 (sum/time + fear OR contrast + verdict).  
**NOT** «N советов» / «N вопросов» skeleton.

## Pain scene (guest only, burn already happened)

- Чемоданы в прихожей, ключ от общежития ещё не выдали
- 3 ночи (не семестр) — родители + первокурсник
- В объявлении «рядом с вузом» — на месте три остановки или «15 минут» без карты
- На фото две кровати — в квартире диван и одна спальня
- Кухня/стиралка «есть» — не проверили до оплаты
- Парковка на разгрузку: нужны 2 часа у подъезда, а места нет
- Check-in: обещали инструкцию заранее — звонят уже у двери

## Lockpick question

«Сколько кроватей? Где парковка на 2 часа?»

## Refusal beat

«Нет. На семестр не сдаём / не везём без двух спальных мест.»

## Angle

parents + first-year student, 2–4 nights NOT semester lease; supply = Tyumen short-term near university (ТюмГУ, ТИУ, Медуниверситет districts)

## Anti-dup (published titles only — do not repeat scene)

| topic_id | title |
|----------|-------|
| B01 | Оплатил квартиру посуточно. Код прислали от чужой двери |
| B02 | Снял квартиру посуточно. Залог не вернули — нашли скол на плите |

B03 delta: not codes/check-in fraud, not deposit — «рядом с вузом» lie + beds/kitchen/parking for parent+student trio.

## Bans (HARD)

- ЕГРН, наследство, ипотека, Шакин, риэлтор
- «5 советов», «7 шагов», «полный гайд», «2026», SEO tail
- Label head («Проверка заселения», «Посуточно у вуза: гайд»)
- Semester lease framing as hero
- Winter/snow hero
- Москва/Сочи as rental place

## Title constraints

- ~50–70 characters
- Cable case hook: two beats, period, strong verb — Klyshin rhythm
- «Тюмень» in H1 optional (not required)
- Guest pain only; numbers = price of burn (3 ночи, 2 часа, 2 кровати) — not list skeleton
- One variant, verdict PASS

## Research context (seasonal facts, writer-safe)

- Late August 2026: queue at dorm, room key often not on Sept 1
- Parents need 2 sleeping places + kitchen + washer for 2–4 nights
- Tyumen universities: check real distance, not «рядом» in ad copy
- Brand facts allowed in article (not necessarily H1): contactless check-in with instructions upfront; two beds; washer/kitchen — verify before pay; parking/unload — ask before pay

## Output

Write `title-brief.json` with: topic_id, h1, title (same as h1), subject, angle, verdict: PASS

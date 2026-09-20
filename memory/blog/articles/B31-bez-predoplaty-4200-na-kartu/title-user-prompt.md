# Title task — B31

Сгенерируй **один** two-beat stop-factor H1 для guest-night CASE (посуточная аренда, Тюмень, «Добрый дом»).

## Handoff draft (СОХРАНИТЬ два удара)
«В фильтре стояло «без предоплаты». За день до заезда попросили 4 200 ₽ на карту»

**Figure для gate:** **4 200 ₽** обязательна.

## Case spine (research-notes)
- Фильтр агрегатора «без предоплаты»; за ~24ч до заезда требование 50% (4 200 ₽ из ~8 400 ₽ за 2 ночи) на СБП/карту, угроза отмены
- Угол: обещание фильтра ≠ условие в переписке; не залог у двери (B02/WP), не тишина после 3000 (B08)
- lockpick в статье, не в H1

## Wordstat P0
- «квартиры посуточно тюмень» 4413 (55+11176)
- supporting: «квартиры посуточно без предоплаты» 359 (225)

## Klyshin
- prepay_filter_trap | dzen_pattern 2

## Anti-dup
B08 предоплата тишина; B16 отмена рейса; WP bez-zalogo; B30 карта после выезда

## HARD gates
Two beats; BAN how-to; ~40–70 chars; guest audience

## slug
bez-predoplaty-4200-na-kartu

## Выход — ТОЛЬКО JSON:
{
  "topic_id": "B31",
  "h1": "...",
  "title": "...",
  "slug": "bez-predoplaty-4200-na-kartu",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 2,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}

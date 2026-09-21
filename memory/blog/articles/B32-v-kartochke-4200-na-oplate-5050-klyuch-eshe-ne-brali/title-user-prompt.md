# Title task — B32

Сгенерируй **один** two-beat stop-factor H1 для guest-night CASE (посуточная аренда, Тюмень, «Добрый дом»).

## Handoff draft (СОХРАНИТЬ два удара)
«В карточке 4 200 ₽. На оплате — 5 050. Ключ ещё не брали»

**Обязательно:** 4 200 и 5 050 (или 850 delta). BAN HH:MM. BAN «Посуточно Тюмень» в начале H1.

## Case spine
- Карточка/фильтр показывает 4 200 ₽; на шаге оплаты итого 5 050 ₽ — сервис/уборка/комиссия до ключа
- НЕ B10 такси 2 400, НЕ B08 предоплата и тишина, НЕ LIVE bez-predoplaty slug

## Wordstat P0
- «квартиры посуточно тюмень» 4409 / 9372
- supporting: «посуточно комиссия» 1903; «квартиры посуточно без комиссии» 328

## slug
v-kartochke-4200-na-oplate-5050-klyuch-eshe-ne-brali

## Выход — ТОЛЬКО JSON:
{
  "topic_id": "B32",
  "h1": "...",
  "title": "...",
  "slug": "v-kartochke-4200-na-oplate-5050-klyuch-eshe-ne-brali",
  "primary_query": "квартиры посуточно тюмень",
  "wordstat_p0": {"phrase": "квартиры посуточно тюмень", "volume_tyumen": 4409, "volume_ru": 9372},
  "dzen_pattern": 2,
  "klyshin_hook": "kitchen_vs_hotel + hidden_fees → checkout delta before key"
}

# Title inputs B03

Read: research-notes.md, handoff klyshin_hook, published-titles-only.md
Output ONLY valid title-brief.json (JSON object, no markdown wrapper).

## Task

One H1 for topic B03 — паспорт/фото паспорта при заселении посуточно.
Tenant: Добрый дом, Тюмень (supply). Demand RF-wide.

## Klyshin hook

passport_checkin_fear | «при заселении просят фото паспорта — законно ли?»
Angle: страх утечки данных → что можно дать до заселения, не сорвав бронь.

## Dzen pattern

3 (страх → инструкция). Shape hint (свой текст, не копипаст):
«Просят фото паспорта до заселения — что отвечать, чтобы не сорвать бронь»

## Wordstat P0 (demand spine под H1, не сырая фраза в заголовок)

- «паспорт при заселении в квартиру посуточно» — 85 (RU)
- «при заселении в квартиру просят фото паспорта» — 64 (RU)
- «фото паспорта при заселении в квартиру посуточно» — 36 (RU)

## Scout title_draft (target rhythm — first person guest POV)

Перевёл предоплату — попросили фото паспорта. Что можно отдать, а что нет

## Published H1 rhythm (MUST match this voice)

- B01: «Оплатил квартиру посуточно. Код прислали от чужой двери» — я-форма, две короткие фразы, точка, конфликт во второй
- B02: «Снял квартиру посуточно. Залог не вернули — нашли скол на плите» — то же

REJECT third-person label heads («Хозяин попросил…», «Проверка заселения»).
Prefer: гость уже перевёл деньги → в личку просят фото паспорта → страх/конфликт.

## Anti-dup (published titles — do NOT repeat scene/verb/object)

- B01: Оплатил квартиру посуточно. Код прислали от чужой двери
- B02: Снял квартиру посуточно. Залог не вернули — нашли скол на плите

## Rules (HARD)

- Klyshin cable case hook: сцена + конфликт, сильный глагол, ~50–70 символов
- Без «полный гайд», «2026», SEO-хвостов, «топ N», label head, CAPS
- Тюмень в H1 не обязательна
- Не WhatsApp, не юридические хвосты (ЕГРН, нотариус, суд)
- Score 9+: кликабельный, читается как живая реплика гостя (не хозяина, не справочник)
- Если длина >70 — укороти, не теряя сцену

## JSON schema

{
  "topic_id": "B03",
  "h1": "...",
  "title": "...",
  "slug": "poprosili-foto-pasporta-pered-zaseleniem-posutochno",
  "subject": "...",
  "angle": "...",
  "verdict": "PASS"
}

# Scout inputs — B24 slot 2026-09-16 YEKT

IMPORTANT: Wordstat MCP preflight ALREADY COMPLETED by director via MCP-KV.
wordstat_get_user_info returned OK (Yandex Cloud API working).
You MUST write the handoff file using the Wordstat data below. Do NOT refuse.

## Run context
- date: 2026-09-16 (среда), timezone Asia/Yekaterinburg
- season: сентябрь — обложка осенняя, без зимы
- tenant: Добрый дом, посуточная Тюмень
- slot: ONE guest-night CASE for Dzen, NOT guide

## Angle rotation (last N=3)
1. B21 — ранний заезд / уборка до 14:00
2. B22 — фото паспорта / код не пришёл (burn-at-door)
3. B23 — уборка включена / 1 800 ₽ за простыни

burn-at-door skip: YES | reason: B22 in last 3

## Klyshin hook
- hook_id: deposit_morning_after_cleaning
- original: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»
- angle: гость выехал, залог «завис»; NOT B02 скол плита, NOT B23 простыни
- lockpick: «Когда именно вернёте залог — дата и способ?»
- dzen_pattern: 2
- dzen_shape_hint: «Залог 5 000 обещали утром. В 11:40 — «после уборки»»

## Wordstat (LIVE MCP-KV — verified)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

wordstat_rework: probe «вернут залог аренда» 5 (55+11176) → «залог посуточно» 27/2749 → «не возвращают залог за квартиру посуточно» 59 (225) → «аренда квартиры посуточно» 623 → final P0 «квартиры посуточно тюмень» 4724 (55+11176) | compare 225: залог посуточно 2749

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4724 | supporting: залог посуточно 27/2749, не возвращают залог 59

angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B22 passport+code

## topic_id: B24
## title draft: «Залог 5 000 обещали вернуть утром. В 11:40 — «после уборки»»
## slug hint: zalog-5000-obeshchali-vernut-utrom-posle-uborki

Write complete handoff in required format with all fields above.

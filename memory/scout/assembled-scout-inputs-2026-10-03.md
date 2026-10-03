# Scout inputs — слот 2026-10-03 YEKT (09:00 automation)

Дата: 2026-10-03, Asia/Yekaterinburg. Сезон обложки: осень (не зима героем).

## Anti-dup (published-titles, last 12)

Пропускаем: код/заселение (B35,B18,B01), залог у двери/без залога (B34,B02), предоплата до кода (B40), кухня/плита (B41), двушка/кладовая (B42), минимум 2 суток (B39), лифт (B37), собака (B36).

## Klyshin angle (mechanics only, NOT legal/Moscow)

Новый guest-hook (не из saturated burn-at-door): **залог обещали вернуть по времени → перенос «после уборки»**.

Original rhythm reference (channel angle bank): «кажется просто → деньги зависли».

## Wordstat live (MCP-KV)

wordstat_preflight: wordstat_get_user_info OK

Probes:
- «залог посуточно» RU225 → 2423; top «квартиры посуточно залог» 1603; «квартиры посуточно без залога» 1050; «не возвращают залог за квартиру посуточно» 65
- «залог посуточно» Tyumen 55+11176 → 25; «квартиры посуточно залог» 22
- «квартиры посуточно тюмень» RU225 → 8847; Tyumen → 3940 (demand spine compare)
- «вернуть залог посуточно» RU225 → 111 (weak alone → rework to залог cluster)

wordstat_rework:
- probe «вернуть залог посуточно» 111 → anchor «залог посуточно» 2423 + «квартиры посуточно залог» 1603
- final P0 phrase: «залог посуточно» volume 2423 (RU225); Tyumen local 25 on same phrase; content localized Tyumen supply only

## Topic card

topic_id: B43
working_title (two-beat CASE, not how-to): **Залог 5 000 обещали вернуть к обеду. В 14:20 написали: «после уборки»**
slug hint: zalog-obeshchali-vernut-k-obedu-posle-uborki
guest_wound: залог, скрытая доплата времени/денег, уборка как рычаг
lockpick: «Когда именно в чате фиксируете возврат залога — до перевода или после?»

angle_rotation: checked last N=12 | burn-at-door skip: yes | reason: new angle = post-checkout deposit delay not door surcharge

signal_urls:
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

Задача Scout: оформить handoff для Research (один кейс посуточно Тюмень, не гайд).

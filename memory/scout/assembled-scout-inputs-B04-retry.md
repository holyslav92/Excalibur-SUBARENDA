# Scout task B04 — OUTPUT HANDOFF ONLY

You are Scout for Добрый дом (посуточная Тюмень). Wordstat MCP-KV preflight and all probes were ALREADY executed live by the conductor. Do NOT claim tools are missing. Do NOT refuse. Output ONLY the handoff block below in Russian, filling the template exactly.

## Required output format (copy structure, fill values)

```
topic_id: B04
title_draft: «Коммуналка в цене» — на выезде прислали доплату по счётчикам
short_title: Коммуналка в цене — доплата по счётчикам на выезде
slug: kommunalka-v-cene-doplata-po-schetchikam-na-vyezde
dzen_pattern: 3
dzen_shape_hint: «ЖКХ включено» в объявлении — что снять на заселении, чтобы не доплатить на выезде
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: utilities_counters | original: «показания счётчиков — не переплатить ЖКХ» | angle: фиксация показаний при посуточной/субаренде; «коммуналка включена» vs доплата на выезде | signal: https://t.me/klyshin_A
wordstat_rework: probe «показания счетчиков аренда» 3 → «коммунальные платежи аренда» 24 → «коммунальные платежи при аренде квартиры» 2 → «что значит коммунальные платежи включены без счетчиков» 4 → «жкх аренда» 6 → «что такое жку при снятии квартиры» 13 → final P0 «коммунальные платежи квартира» 105 (compare RU 225: 12751); clusters tried: счётчики+аренда, жкх+аренда, включено без счётчиков, снятие квартиры
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «коммунальные платежи квартира» 105 | жкх аренда 6 | показания счетчиков 16810 | что такое жку при снятии квартиры 13
signal_urls: https://t.me/klyshin_A | https://добрыйдом-72.рф/blog/ | https://добрыйдом-72.рф/blog/skrytye-doplaty-pri-arende-kvartiry-kak-ne-pereplatit
external_signal: Klyshin angle bank utilities_counters; live @klyshin_A Aug 2026 — сделки/проверки (angle only); sibling «скрытые доплаты» на blog — не дублировать; green field на ЖКХ/счётчики
angle: Гость видит «коммуналка в цене», на выезде просят скрин счётчиков или доплату — как зафиксировать на заселении
stickers: что такое жку при снятии квартиры; коммунальные платежи включены без счётчиков; показания на заселении
```

Add 2-3 sentences of scout notes after the block. No refusals. No code blocks in output.

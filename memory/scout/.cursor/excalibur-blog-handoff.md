# Scout handoff — B26 floor_elevator_luggage

klyshin_hook: floor_elevator_luggage | original: «Квартира на пятом. Лифт не едет — чемодан уже не в такси» | angle: этаж+лифт+багаж не проговорены до оплаты; табличка у подъезда | signal: https://t.me/klyshin_A

wordstat_rework: probe «этаж лифт квартира» 2413 (225) → «квартира 5 этаж без лифта» 101 (225) → «квартира пятый этаж без лифта» 36 (225) → Tyumen narrow empty → final P0 «квартиры посуточно тюмень» 4570 (55+11176)

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4570 | supporting «квартира 5 этаж без лифта» 101 (225) | «залог посуточно» 26 (55+11176)

dzen_pattern: 2 | dzen_shape_hint: «Квартира на пятом. Лифт не едет — и чемодан уже не в такси»

topic_id: B26
slug_hint: pyatyj-etazh-lift-ne-rabotaet-chemodan-u-podezda
title_draft: «Квартира на пятом. Лифт не едет — и чемодан уже не в такси»
anti_dup_guard: не код/залог/кровати/уборка/дети/отель/мокрый пол/бойлер/соседи

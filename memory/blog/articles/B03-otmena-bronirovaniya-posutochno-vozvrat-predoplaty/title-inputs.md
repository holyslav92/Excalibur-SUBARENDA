# Title inputs B03

topic_id: B03
article_dir: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty

Read:
- .cursor/excalibur-blog-handoff.md
- research-inputs-assembled.md
- published-titles-only.md (in article dir)
- shared/article-style.md

Output ONLY valid title-brief.json (JSON object, no markdown wrapper).

## Scout handoff
- title_draft: Планы сорвались. Отменил бронь посуточно — предоплату не вернули
- dzen_pattern: 3 (страх → инструкция в §1)
- dzen_shape_hint: «Отменил бронь — предоплату не вернули. Что спросить до перевода»
- klyshin_hook: cancellation_refund | original: «планы сорвались — вернут ли предоплату?» | angle: условия отмены и штрафы до оплаты
- P0 Wordstat: «отмена бронирования» 14147 RU / 104 Tyumen
- Stickers: штраф за отмену 458, возврат средств 724, суточно отмена 379, бесплатная отмена 935
- Anti-dup: не коды/заселение (B01), не залог/скол (B02), не вечеринки в правилах

## Published titles (anti-dup)
- B01: Оплатил квартиру посуточно. Код прислали от чужой двери
- B02: Снял квартиру посуточно. Залог не вернули — нашли скол на плите

## Angle / supply
- Гость перевёл предоплату, планы сорвались, хост/площадка говорит «невозвратно»
- Что спросить ДО оплаты: окно бесплатной отмены, % удержания, срок возврата, письменное подтверждение
- Supply: посуточная аренда Тюмень (Добрый дом), не юрист, не ЕГРН/суд
- Demand spine: отмена бронирования — под H1, не сырая SEO-фраза в заголовок

## Title constraints (HARD)
- Cable pain-scene Klyshin rhythm: короткая сцена + конфликт, сильный глагол
- dzen_pattern 3: страх денег → инструкция в лиде (не копипаста @klyshin_A)
- ~50–70 символов
- «Тюмень» в H1 НЕ обязательна
- Без SEO-хвоста, «полный гайд», «2026», топ-N, CAPS, юридических тем
- Не дублировать B01 (код/заселение) и B02 (залог/скол)
- verdict: PASS

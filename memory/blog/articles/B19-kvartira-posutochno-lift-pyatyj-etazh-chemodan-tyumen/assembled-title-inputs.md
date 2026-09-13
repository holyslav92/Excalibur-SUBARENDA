# Title inputs — B19

Return ONLY valid JSON for title-brief.json. No markdown wrapper. No BLOCKER.

topic_id: B19
slug: kvartira-posutochno-lift-pyatyj-etazh-chemodan-tyumen
wordstat_p0: квартиры посуточно тюмень (4840 Tyumen, 10385 RU)

Case angle: guest books 5th floor apartment, host wrote «лифт работает», at entrance sign «лифт не работает», suitcase 23 kg, 2-3 nights multiple climbs.

Required H1 (must include ₽ OR ночи — gate regex):
«Написали «лифт есть». За 8 400 ₽ — пятый этаж пешком»

Requirements:
- two-beat stop-factor, guest inside, NOT how-to
- MUST contain ₽ sum (e.g. 8 400 ₽) or «2 ночи» / «3 ночи»
- ban: как снять, что проверить, разберём, советов, шагов
- Tyumen optional in H1
- verdict PASS in JSON

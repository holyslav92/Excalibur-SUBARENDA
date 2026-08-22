# description inputs B03 — full context
Output ONLY valid description-brief.json JSON object (verdict PASS). No markdown fences.

topic_id: B03

h1 (do NOT copy): Перевели предоплату. В правилах мелким: вечеринки и лишние гости

article opening (do NOT truncate — different angle):
<p>Августовская пятница. Нашли двушку в центре Тюмени, цена подошла, хозяин отвечает быстро. Перевели предоплату за две ночи, отправили скрин, получили адрес и код.</p>
<p>Правила пришли отдельным сообщением. Гость их пролистнул.</p>
<p>Вечером приехали друзья: вроде просто посидеть, не до утра. Но в квартире уже шесть человек вместо трёх. В час ночи позвонил хозяин, в два приехал. Утром — досрочный выезд и залог не вернули.</p>

pain_scene: предоплата переведена → правила мелким про вечеринки и лишних гостей → залог удержали

wordstat spine: аренда квартиры посуточно (48407 RF, 787 Tyumen)

geo: Тюмень (tenant Добрый дом, Святослав Шакин angle)

Requirements:
- Dzen card teaser 1–2 sentences, ~120–220 chars (max 250)
- Klyshin rhythm: case hook, conversational first line, intrigue before click
- ≠ h1 title (different wording)
- ≠ truncated lead (not substring of first two paragraphs)
- Not label head («Риэлтор Тюмень», «Правила посуточно»)
- One hook, not a 5-point checklist
- rhythm: klyshin_case_hook
- not_equal_title: true
- not_truncated_lead: true

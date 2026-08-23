# description inputs B03 — Добрый дом
Output ONLY valid description-brief.json JSON object (verdict PASS). No markdown wrapper.

topic_id: B03
tenant: Добрый дом, посуточная аренда Тюмень

h1: Хозяин разрешил кота в объявлении. В договоре — штраф за шерсть

article opening (do NOT truncate or copy):
<p>Август, Тюмень. Квартира на неделю найдена, в объявлении — «можно с животными». Кот спокойный: переноска, миска, привычный плед.</p>

<p>Вы оплатили бронь, открыли правила проживания. А там: проживание с животным без согласования — штраф. Уборка шерсти — отдельной строкой.</p>

<p>Вот где подставят: объявление обещало одно, а деньги уже ушли. Чтобы не читать такие пункты после оплаты, задайте хозяину или менеджеру 5 вопросов до оплаты.</p>

angle: Klyshin case hook — объявление «можно с животными» vs штраф в правилах; 5 вопросов до оплаты; кот, посуточная.
wordstat P0: «аренда квартиры с животными» 1095 RU / 4 Tyumen

Requirements (shared/dzen-description-rules.md):
- 1–2 sentences, ~120–220 chars (max 250)
- Klyshin rhythm: conversational hook, intrigue, case scene
- ≠ h1 (not same wording)
- ≠ truncated lead (not substring of first two paragraphs; not same opening phrase)
- Not label head («Проверка ЕГРН», «Риэлтор Тюмень»)
- Cyrillic; geo Tyumen ok in body
- Fields: topic_id, description, rhythm, geo, not_equal_title, not_truncated_lead, verdict

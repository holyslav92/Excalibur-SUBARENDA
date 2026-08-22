# description inputs B03 — full context
Output ONLY valid description-brief.json JSON object (verdict PASS).

topic_id: B03
h1: Планы сорвались — предоплату удержали. Что выяснить до оплаты
subject: отмена бронирования посуточно — возврат предоплаты
angle: Klyshin-ритм, dzen_pattern 3: страх удержания предоплаты → что выяснить до оплаты. Demand spine «отмена бронирования» (14147 RU) под H1, не в заголовке.
geo: Тюмень
tenant: Добрый дом, посуточная аренда comfort+

article opening (do NOT truncate or copy):
<p>Деньги ушли. Предоплата за квартиру на август уже переведена, а через неделю поездка сорвалась: отменили командировку, ребёнок попал в больницу, машина встала.</p>
<p>Пишете хозяину — в ответ: «Оплата невозвратная, у нас оферта».</p>

key hooks from article (pick ONE for teaser, not checklist):
- отель ≠ квартира посуточно — новости про 100% возврат в отелях не про частную аренду
- «невозвратно» в оферте ≠ законное удержание всей суммы — нужен расчёт подтверждённых расходов
- окно бесплатной отмены на 6 часов при брони за 2 месяца
- слово «задаток» в чате ≠ оформленный задаток — чаще аванс, который возвращают
- пять вопросов до оплаты: окно отмены, удержание, срок возврата, условия в чат, статус хозяина (ИП/самозанятый/физлицо)

research surprising_fact: гости квартир посуточно ошибочно думают, что отельные правила марта 2026 про 100% возврат уже «решили всё» для частной аренды

Requirements (shared/dzen-description-rules.md):
- 1–2 sentences, ~120–220 chars (max 250)
- Klyshin rhythm: case hook, conversational first line, intrigue
- ≠ h1/title (not equal character-by-character)
- ≠ truncated lead (not substring of first two paragraphs, not same opening phrase)
- Not label head, not full spoiler/checklist
- Cyrillic; geo/facts Tyumen / Shakин context ok
- topic_id B03, rhythm klyshin_case_hook, geo Тюмень, not_equal_title true, not_truncated_lead true, verdict PASS

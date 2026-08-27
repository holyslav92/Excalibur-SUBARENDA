# description inputs B03 — full context
Output ONLY valid description-brief.json JSON object (verdict PASS). No markdown fences, no commentary.

topic_id: B03
author_brand: Добрый дом (посуточная аренда Тюмень) — NEVER Шакин / The Риэлтор

h1 (DO NOT duplicate):
Выбрал квартиру с оценкой 4,8. Перед оплатой нашёл одинаковые отзывы

angle (from title-brief):
Guest chose 4,8 card on Avito/Sutochno; before prepay found identical «всё супер» reviews and copy-paste host replies. Real risk is below the fold: low stars, «Отзывы без оценки», stale dates.

article opening (DO NOT truncate or repeat — teaser must be different wording):
Андрей собирался в Тюмень на четыре ночи, карта уже в форме оплаты. Рейтинг 4,8, одиннадцать отзывов «всё супер» — и только перед переводом денег он заметил три отзыва одной датой и одинаковые ответы хозяина слово в слово.

research / Wordstat spine:
«суточно ру отзывы» (RF demand); guest pain = шаблонные отзывы, копипаста, блок без оценки на Авито, свежесть дат.

stickers (energy, not copy):
- 4,8 ≠ гарантия; «Отзывы без оценки» не влияют на звёзды
- Одинаковые «всё супер» в один день — повод открыть низкие оценки
- Один конкретный вопрос хозяину до оплаты лучше десяти общих отзывов

Requirements (HARD):
- 1–2 sentences, ~120–220 chars (max 250)
- Klyshin rhythm: case hook, conversational first line, intrigue before click
- ≠ h1, ≠ truncated lead (not substring of opening paragraphs)
- Guest pain / risk teaser — NOT price list, NOT guest-burn arithmetic (2500→6500), NOT «у Доброго дома … ₽»
- NO full TG/MAX/booking funnel — one hook only
- NO ЕГРН, наследство, ипотека
- Cyrillic; geo Тюмень optional in teaser
- author_brand: Добрый дом

JSON schema:
{
  "topic_id": "B03",
  "description": "...",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "author_brand": "Добрый дом",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}

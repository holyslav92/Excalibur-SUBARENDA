# Description assembled inputs — B03

OUTPUT: ONLY valid JSON for `description-brief.json`. No markdown fences. No commentary.

## Task

Write **1–2 sentences** (~120–220 chars, max 250) for Dzen card teaser (→ og:description / RSS).

- **Rhythm:** Klyshin case hook — conversational first line, intrigue to click
- **Brand:** Добрый дом / guest pain Тюмень — NOT Шакин, NOT The Риэлтор
- **≠ title** — different wording from H1 below
- **≠ truncated lead** — NOT first paragraphs of article.html
- **Pain:** «кухня» in listing vs чайник/кружки on arrival; 3 mornings in café
- **Lockpick angle:** «Плита и сковородка или только микроволновка?»
- **NO** guest-burn price ladder (2500→6500) as Добрый дом price
- **NO** «история Святослава Шакина»
- **NO** full TG/MAX/booking funnel — teaser leads to click only

## title-brief.json (DO NOT copy H1)

```json
{
  "topic_id": "B03",
  "h1": "Три ночи. «Кухня есть» — каждый завтрак всё равно в кафе",
  "title": "Три ночи. «Кухня есть» — каждый завтрак всё равно в кафе",
  "pain_scene": "Гость на три ночи видит «кухня», утром — чайник и кружки, платит в кафе.",
  "lockpick_question": "Плита и сковородка или только микроволновка?"
}
```

## article.html opening (DO NOT truncate — write fresh teaser)

First paragraph: Guest bought eggs/bread for breakfast, listing said «кухня», found two mugs, kettle, microwave, one plate, no frying pan — went to café all three mornings.

Second paragraph: «кухня» in listing ≠ savings; 3 000–5 000 ₽ difference vs hotel with breakfast.

## research angle

- Word «кухня» can mean full kitchen OR kettle zone
- 3 nights, breakfast burn in cafés
- Ask before booking: stove + frying pan or microwave only?

## Good examples (energy only — do not copy)

- «Хост пишет «утром будет». Вы уже в квартире — где бойлер, спросите до того, как замёрзнете.»
- ««Можно» без породы и доплаты — не ответ. Один вопрос в переписке спасает заселение.»

## Required JSON schema

```json
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
```

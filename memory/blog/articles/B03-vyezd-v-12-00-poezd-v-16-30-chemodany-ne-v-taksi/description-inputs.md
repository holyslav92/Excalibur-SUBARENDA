# description inputs B03 — full context
Output ONLY valid description-brief.json JSON object (verdict PASS).

topic_id: B03
author_brand: Добрый дом
dzen_pattern: 2 (бытовой кейс с часами и расходами)
rhythm: klyshin_case_hook

h1: Гость выехал в 12:00. Поезд в 16:30. Чемоданы — не в такси

article opening (DO NOT truncate or copy):
<p>В 11:50 гость стоял в прихожей нашей квартиры комфорт+ с двумя большими чемоданами и рюкзаком. Поезд у него был в 16:30, а выезд — до 12:00: это было указано в брони, переписке и подтверждении. До отправления оставалось четыре с половиной часа, но квартира уже должна была перейти к уборке и следующему гостю. «А куда я это всё дену? Поезд в 16:30», — написал он. А через минуту добавил: «Можно оставить чемоданы до четырёх?» В тот день не получилось: примерно в 350 ₽ обошлась ячейка на вокзале, а первые полтора часа ушли не на прогулку по Тюмени, а на тревогу, дорогу и поиск места для багажа.</p>

pain_scene: выезд 12:00, поезд 16:30, 4+ часа окна, чемоданы некуда деть
moral: сначала багаж, потом ключ — чемоданы не в такси
wordstat spine: квартиры посуточно тюмень (5675)

Requirements:
- 1–2 sentences, ~120–220 chars (max 250)
- Klyshin rhythm: case hook, разговорная первая реплика, интрига
- ≠ h1 (other wording, not SEO tail)
- ≠ truncated lead / opening paragraph
- Guest pain only, geo Тюмень ok in body
- NEVER Шакин / The Риэлтор
- NEVER guest-burn price ladder as Добрый дом price (350₵ ok as hook, no «у Доброго дома … ₽»)
- No full TG/MAX/booking funnel

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

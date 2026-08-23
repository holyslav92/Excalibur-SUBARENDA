# Description inputs — B03

Read: shared/dzen-description-rules.md (canon), title-brief.json, article opening (lead anti-dup).
Output ONLY valid description-brief.json (JSON object, no markdown wrapper).

## Task

Write 1–2 sentences (~120–220 chars, max 250) for Dzen card teaser after Sol.
Tenant: Добрый дом, Тюмень (supply). Demand RF-wide.

## Title (H1) — DO NOT copy or paraphrase as the whole description

«Перевёл предоплату. В личку просят фото паспорта»

## Article opening (first 2 paragraphs) — DO NOT truncate or repeat

Paragraph 1:
Конец августа, вы едете в Тюмень в командировку или везёте семью перед школой. Квартира найдена, предоплата переведена — и через полчаса приходит сообщение с незнакомого номера: «Скиньте фото паспорта, разворот с фотографией и страницу с пропиской». Аватарки нет, имя не то, что было в объявлении. Деньги уже ушли, отказаться страшно, отправить — тоже.

Paragraph 2:
Что сделать прямо сейчас, до того как вы что-то отправите. Не высылайте фото первым сообщением. Ответьте текстом три вопроса: для чего именно нужны данные, какие сведения нужны (только ФИО и номер документа — или полный разворот), и можно ли вместо фото предъявить оригинал при заселении или показать его по видеосвязи.

## Klyshin rhythm (case hook)

passport_checkin_fear — страх утечки данных после оплаты; конфликт канала (личка) и момента (после предоплаты).
Dzen pattern 3: страх → инструкция. Conversational first line (quote or реплика), intrigue before click.

## Voice reference (sibling descriptions — energy only, do NOT copy)

- B01: «Инструкцию пришлём позже» звучит спокойно — пока в 23:00 не выясняется, что код открывает лишь подъезд. Разбираем, какие семь вопросов задать хозяину в Тюмени до оплаты.
- B02: «Залог не возвращаем — на плите скол». Вы уже у лифта, а доказательств нет. Разбираем, что снять на видео при заселении, чтобы спокойно вернуть депозит.

## Demand spine (hint only, no SEO tail)

паспорт при заселении посуточно; просят фото паспорта; страх утечки; оригинал vs фото в мессенджере.

## Rules (HARD)

- ≠ title H1 (casefold)
- ≠ truncated lead — not substring of opening paragraphs; do not start with same phrase as first <p>
- No label head («Проверка паспорта», «Риэлтор Тюмень»)
- Cyrillic; Latin only for brands (ЕГРН, ЦИАН)
- One hook, not a 5-point checklist
- Geo hint: Тюмень (optional in text)
- 40–250 chars

## JSON schema

{
  "topic_id": "B03",
  "description": "...",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}

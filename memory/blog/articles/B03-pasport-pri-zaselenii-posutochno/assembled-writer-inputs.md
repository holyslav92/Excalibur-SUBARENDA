# Assembled Writer inputs — B03 (2026-08-23)

## INSTRUCTION FOR DEROUTER WRITER (Opus 5)

Write the full meaning draft to HTML fragment. Output ONLY valid HTML (no markdown fences, no h1).
After HTML, append exactly:

```
=== EXCALIBUR BLOG WRITER ===
draft: meaning
next: Sol
incident_report: none
```

Also write `dzen-excerpt.json` in the same article dir (separate JSON file with keys: hook, first_screen, takeaway).

## Role

You are Writer for Excalibur BLOG — meaning/facts draft only. Sol will apply tenant voice later.
Read constraints below. Facts ONLY from research-notes. Do NOT invent brand policies for «Добрый дом».

## H1 (from title draft — title-brief.json not ready yet)

**H1:** Перевёл предоплату — попросили фото паспорта. Что можно отдать, а что нет

Do NOT put `<h1>` in writer.html. Fulfill H1 promise in body.

## Dzen pattern

**dzen_pattern: 3** — страх → инструкция в §1.
§1: name the risk (photo in messenger after prepayment) → immediately how to check / what to ask.
Not a legal encyclopedia opening.

## Tenant

- Brand: Добрый дом
- Niche: посуточная аренда, Тюмень (supply only Тюмень; demand RF-wide)
- Tone: humble **comfort+**, warm host, «как для своих», спокойно, без пафоса
- Forbidden voice: лучшие, №1, premium, бизнес-класс, люкс, мрамор, «как в пятизвёздочном отеле»
- Season: конец августа 2026, командировки и семьи перед осенью (локальный крючок Тюмень OK)

## Format

- `publish_format: longform` — полноценная статья, не короткая заметка
- Clean HTML fragment: `<p>`, `<h2>`, `<ul>`, `<ol>`, `<strong>`, `<a>` — NO `<h1>`
- Simple conversational Russian, short paragraphs
- Ban words: ЕГРН, нотариус, суд, «я адвокат», «мы лучшие», бизнес-класс, WhatsApp
- No legal disclaimer boilerplate («не заменяет юридическую консультацию»)
- No SEO tails, no «полный гайд», no research-date in lead
- Phone in text: **only** +7 (993) 574-83-22

## CTA funnel (HARD — mid-body, not link dump at end)

1. **After checklist** (questions before prepayment / what to agree in writing): TG channel «полный список» → https://t.me/Dobriy_dom_72
2. **After brand block «у нас так»** (humble, no invented storage policies): MAX https://max.ru/id660300569233_biz OR manager — instruction before check-in
3. Final: booking https://добрыйдом-72.рф/booking/ + tel +7 (993) 574-83-22

Brand block rules:
- May say: бесконтактное заселение, поддержка в мессенджере, инструкция заранее не у двери, комфорт+, 10 лет Сургут+Тюмень
- Do NOT invent: which passport pages requested, where data stored, deletion policy, specific codes

## Interlink (HARD)

`interlink_old_articles=true`. Add **1–3** contextual `<a href="/blog/SLUG/">` links to **published** siblings only:

| slug | context hint |
|------|----------------|
| beskontaktnoe-zaselenie-posutochno-tyumen | бесконтактное заселение часто требует предварительной идентификации |
| perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem | предоплата уже переведена — сохранять переписку |

Do NOT link to unpublished slugs from scout list.

## Article structure guidance

1. **Lead (§1):** fear → instruction — guest paid prepayment, stranger asks passport photo in personal messenger; what to do right now
2. **«Вот где подставят»:** channel + timing (after money), not the passport itself
3. **Contrast:** hotel/digital ID news Aug 2026 ≠ private apartment rules — surprising_fact from research
4. **Practical:** photo ≠ original; consent & 152-ФЗ context without lawyer voice; alternatives (platform chat, show original, video call, watermark per Роскачество)
5. **Checklist before prepayment** — numbered questions (align with H1 «что можно отдать, а что нет»)
6. **Mid CTA #1** after checklist → TG
7. **Foreign guests** — brief, migration accounting for foreigners only; no fine amounts
8. **If host refuses** — save chat, platform support (not auto RosPotreb for private rental)
9. **Brand «у нас так»** — humble comfort+, instruction before door, on messenger — no invented doc policy
10. **Mid CTA #2** after brand → MAX
11. **Short FAQ** 2–3 Q
12. **Closing** — booking + phone

## research-notes.md (full)

# Research notes — B03

research_date: 2026-08-23  
topic_id: B03  
tenant: Добрый дом, Тюмень, посуточная аренда

## reader_problem

Гость бронирует квартиру посуточно и до заселения получает просьбу прислать фото паспорта в личный мессенджер. Он боится утечки данных, но не хочет потерять предоплату или остаться без жилья в день приезда.

## reader_outcome

Читатель поймёт разницу между предъявлением оригинала документа и отправкой его фото, сможет заранее согласовать безопасный способ идентификации и сохранит переписку, если условия меняются после бронирования.

## practical_facts

- Частная квартира посуточно и гостиница — разные режимы. Новости 2026 года о заселении в классифицированные отели по цифровому ID, водительским правам или сервисам Госуслуг не означают, что тот же порядок автоматически действует при найме квартиры у частного лица.
- Фото, скан или PDF паспорта не заменяют оригинал документа при очной идентификации. Цифровой ID в предусмотренных государством каналах также не равен фотографии документа, отправленной в мессенджер.
- По консультациям юристов Правовед.RU, человек не обязан разрешать фотографировать или сканировать свой паспорт: при очной встрече можно предъявить оригинал, разрешить переписать нужные данные либо самостоятельно заполнить анкету. Это консультационные позиции, а не судебная практика.
- Передача паспортных данных для договора при бесконтактном заселении встречается на практике. Более безопасный вариант — встроенный чат площадки бронирования или защищённый сервис, а не личный мессенджер неизвестного номера.
- В посуточной аренде запрос фото первых страниц паспорта либо селфи с паспортом описывается площадками как распространённая практика бесконтактного заселения. Распространённость такой практики не отменяет необходимости согласия на обработку персональных данных и не делает любой канал отправки безопасным.
- Получивший паспортные данные арендодатель обрабатывает персональные данные. Для граждан РФ копия паспорта, согласно отраслевому разъяснению Контур.Отель, запрашивается с согласия; требования для иностранных граждан отличаются из-за миграционного учёта.
- Для иностранного гостя принимающая сторона, включая сдающего жильё, должна учитывать требования миграционного учёта и уведомления МВД. Не следует путать это с отдельной «миграционной регистрацией» гражданина РФ при обычном посуточном проживании.
- Роскачество рекомендует не пересылать фото паспорта в открытые чаты и незнакомым получателям. Если отправка неизбежна, можно добавить водяной знак: «Только для [название объекта], до [дата]». Водяной знак снижает удобство повторного использования изображения, но не делает передачу полностью безрисковой.
- До внесения предоплаты полезно письменно уточнить: нужен ли документ заранее, какие именно сведения необходимы, через какой канал их принимают, можно ли показать оригинал при встрече или видеозвонке, а также что происходит с копией после заселения.
- Возможные компромиссы: передать данные через чат платформы бронирования; подписать договор дистанционно через предусмотренный сторонами способ; заполнить данные при заселении; показать оригинал при личной встрече или видеосвязи без отправки фотографии. Достаточность конкретного варианта надо согласовать с хозяином до оплаты.
- Если хозяин отказывается заселять гостя, хотя тот готов предъявить оригинал, практический первый шаг — сохранить переписку, условия брони и чек оплаты, затем обратиться в поддержку площадки. Для гостиничной услуги возможна жалоба в Роспотребнадзор; этот порядок не надо автоматически переносить на спор по частному найму.

## constraints

- Не утверждать, что просьба о фото паспорта «всегда незаконна». Корректнее разделять законную цель идентификации, согласие на обработку данных и конкретный способ передачи.
- Не утверждать, что гость обязан отправить скан или фото: при очном заселении у него есть возможность предложить предъявление оригинала и иной согласованный способ передачи нужных сведений.
- Не выдавать ответы Правовед.RU за закон или сложившуюся судебную практику: это мнения юристов по конкретным ситуациям.
- Не переносить правила ПП РФ №1912 и новости о цифровом ID/MAX в гостиницах на частную посуточную квартиру. Для статьи это контраст, а не инструкция по заселению в квартиру.
- Не обещать от имени «Добрый дом», какие страницы паспорта запрашиваются, где хранятся данные, удаляются ли они после заезда и возможен ли конкретный альтернативный способ: этих условий нет в tenant-config.
- Не приводить штрафы за миграционный учёт как точную сумму.
- При упоминании иностранцев не давать срок уведомления МВД без проверки актуальной редакции профильных норм.
- Не называть фото паспорта надёжным способом защиты от мошенничества или утверждать, что по нему невозможно злоупотребление: риск чаще связан с фишингом, социальной инженерией и повторным использованием данных.

## voice_angle

Страх возникает не из-за самого предъявления паспорта, а из-за момента и канала: незнакомый человек просит фото в личном мессенджере, когда предоплата уже переведена. Полезно отделить нормальную идентификацию гостя от требования безоговорочно отправить копию и показать спокойный способ договориться заранее.

## surprising_fact

Августовские новости о цифровом ID вместо бумажного паспорта касаются классифицированных гостиниц, а не автоматически частных квартир посуточно. Цифровой ID для отеля и фото паспорта в личном мессенджере хозяину квартиры — разные ситуации по закону и по рискам.

## Anti-dup (do not repeat angles of live posts)

- B01: бесконтактное заселение, код/дверь
- B02: залог не вернули, скол на плите

## published-titles-only (anti-dup)

| topic_id | slug | title |
| B01 | beskontaktnoe-zaselenie-posutochno-tyumen | Оплатил квартиру посуточно. Код прислали от чужой двери |
| B02 | perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem | Снял квартиру посуточно. Залог не вернули — нашли скол на плите |

## dzen-excerpt.json spec

```json
{
  "hook": "1 sentence card hook — fear of passport photo after prepayment",
  "first_screen": "2-3 sentences for Dzen card first screen",
  "takeaway": "one practical takeaway"
}
```

Russian only. No emoji.

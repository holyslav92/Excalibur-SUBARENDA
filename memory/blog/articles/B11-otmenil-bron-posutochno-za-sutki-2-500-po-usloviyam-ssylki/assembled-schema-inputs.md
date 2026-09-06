# Schema inputs B11

Return ONLY valid schema.jsonld JSON. NO BLOCKER.

## Article

- topic_id: B11
- slug: otmenil-bron-posutochno-za-sutki-2-500-po-usloviyam-ssylki
- headline (H1): Отменил за сутки. 2 500 ₽ — «по условиям ссылки»
- datePublished: 2026-09-06
- dateModified: 2026-09-06
- inLanguage: ru-RU
- contentLocation: Тюмень

## Site base

Use placeholder `{{SITE_BASE}}` for all URLs (never literal host, never [REDACTED]).
Canonical article URL: `{{SITE_BASE}}/blog/otmenil-bron-posutochno-za-sutki-2-500-po-usloviyam-ssylki/`

## Author (HARD)

From shared/authors-registry.json — id `dobry-dom`, name «Добрый дом».
Organization with NAP: Тюмень, phone +7 (993) 574-83-22.
NEVER mention Шакин / The Риэлтор.

## FAQ

Article has NO «Частые вопросы» section (theme_blocks.faq=skip). Do NOT include FAQPage.

## Description hint

Guest cancelled daily rental booking one day before check-in; host kept 2 500 ₽ prepayment citing link to cancellation rules shown only after cancellation. Practical guide on getting cancellation terms in chat before transfer.

## article.html excerpt (first paragraphs)

За сутки до заезда гость написал: поездка отменилась, не приеду. В ответ получил ссылку и короткое: «по условиям ссылки предоплата не возвращается». 2 500 ₽, отправленные несколько дней назад переводом по номеру телефона, остались у хозяина целиком.

## Required @graph nodes

1. Organization «Добрый дом» with @id {{SITE_BASE}}/#organization
2. BlogPosting with author/publisher refs to organization, headline, dates, contentLocation Тюмень

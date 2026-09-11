# Schema inputs — B16

topic_id: B16
article_dir: memory/blog/articles/B16-otmenili-rejs-predoplatu-vernut
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/otmenili-rejs-predoplatu-vernut/`
   - `@id`: `{{SITE_BASE}}/blog/otmenili-rejs-predoplatu-vernut/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — отменённый рейс, предоплата 4 200 ₽, обещание вернуть за три дня без даты отправки; на четвёртый день денег нет; до перевода спросить дату и способ возврата; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-11`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Рейс отменили. 4 200 ₽ обещали вернуть за три дня — срок вышел",
  "h1": "Рейс отменили. 4 200 ₽ обещали вернуть за три дня — срок вышел",
  "slug": "otmenili-rejs-predoplatu-vernut",
  "topic_id": "B16",
  "author_id": "dobry-dom",
  "date": "2026-09-11",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Рейс отменили. 4 200 ₽ обещали вернуть за три дня — срок вышел

## authors-registry (dobry-dom)

```json
{
  "id": "dobry-dom",
  "name": "Добрый дом",
  "jobTitle": "Апартаменты и квартиры посуточно в Тюмени",
  "url": "{{SITE_BASE}}/",
  "sameAs": ["{{SITE_BASE}}/", "{{SITE_BASE}}/blog/"]
}
```

## Article summary (for description only)

Гость перевёл 4 200 ₽ предоплатой за две ночи в Тюмени; рейс отменили за день до заезда. Хозяин вежливо обещал вернуть деньги «после проверки в течение трёх дней», но на четвёртый день перевода не было — только «ещё проверяем». Фраза без календарной даты отправки и канала возврата не является сроком. До оплаты нужно спросить дату и способ возврата при отмене до заселения.

## FAQ in article.html

None — no h2 «Частые вопросы».

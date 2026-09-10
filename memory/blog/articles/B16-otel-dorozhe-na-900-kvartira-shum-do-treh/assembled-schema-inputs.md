# Schema inputs — B16

topic_id: B16
article_dir: memory/blog/articles/B16-otel-dorozhe-na-900-kvartira-shum-do-treh
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/otel-byl-dorozhe-900-kvartira-shum-koridor-do-treh/`
   - `@id`: `{{SITE_BASE}}/blog/otel-byl-dorozhe-900-kvartira-shum-koridor-do-treh/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — квартира дешевле отеля на 900 ₽ за ночь, но «тихо, как дома» не спасло от шума коридора и лифта до трёх; две бессонные ночи и срочный переезд в отель; до оплаты проверить отзывы про подъезд и что даёт отель за доплату; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-10`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Отель был дороже на 900 ₽ за ночь. Квартира — две ночи без сна",
  "h1": "Отель был дороже на 900 ₽ за ночь. Квартира — две ночи без сна",
  "slug": "otel-byl-dorozhe-900-kvartira-shum-koridor-do-treh",
  "topic_id": "B16",
  "author_id": "dobry-dom",
  "date": "2026-09-10",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Отель был дороже на 900 ₽ за ночь. Квартира — две ночи без сна

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

Пара на три ночи в Тюмени выбирает квартиру дешевле отеля на 900 ₽ за ночь. В объявлении — «тихо, как дома», но две ночи подряд слышны двери, лифт и разговоры на площадке до трёх утра. После двух бессонных ночей бронируют отель примерно за 4 500 ₽. Экономия на бумаге не равна цене сна: до оплаты нужно проверить отзывы про коридор и лифт, уточнить ночной канал связи и сравнить не только кровать, но и запасной сценарий при проблеме.

## FAQ in article.html

None — no h2 «Частые вопросы».

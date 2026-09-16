# Schema inputs — B24

topic_id: B24
article_dir: memory/blog/articles/B24-mozhno-s-detmi-doplata-za-rebenka
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/mozhno-s-detmi-doplata-za-rebenka/`
   - `@id`: `{{SITE_BASE}}/blog/mozhno-s-detmi-doplata-za-rebenka/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — отметка «можно с детьми» в карточке, доплата 1 500 ₽ за ребёнка при заезде в Тюмени; что уточнить до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-16`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "«Можно с детьми» в карточке. При заезде: 1 500 ₽ за 2 ночи, 6-летнему",
  "h1": "«Можно с детьми» в карточке. При заезде: 1 500 ₽ за 2 ночи, 6-летнему",
  "slug": "mozhno-s-detmi-doplata-za-rebenka",
  "topic_id": "B24",
  "author_id": "dobry-dom",
  "date": "2026-09-16",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«Можно с детьми» в карточке. При заезде: 1 500 ₽ за 2 ночи, 6-летнему

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

Семья увидела в карточке «можно с детьми», оплатила 8 400 ₽ за две ночи — и при заселении услышала доплату 1 500 ₽ за шестилетнего ребёнка плюс 500 ₽ за кроватку. Разбор: значок разрешает приехать, но не называет итог; как одной строкой в переписке вскрыть цену до перевода; почему доплату называют у двери.

## FAQ in article.html

None — no h2 «Частые вопросы».

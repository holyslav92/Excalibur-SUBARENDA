# Schema inputs — B29

topic_id: B29
article_dir: memory/blog/articles/B29-buhgalteriya-zhdet-chek-v-chate-my-ne-gostinica
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/buhgalteriya-zhdet-chek-v-chate-my-ne-gostinica/`
   - `@id`: `{{SITE_BASE}}/blog/buhgalteriya-zhdet-chek-v-chate-my-ne-gostinica/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta from description-brief spirit — оплата 2 ночей, бухгалтерия просит чек, хозяин «не гостиница», чек «Мой налог» до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-19`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).
14. **BAN** stuffing weak cluster «посуточная аренда тюмень» in description.

## article.meta.json

```json
{
  "title": "Оплатили 2 ночи. Бухгалтерия просит чек — «мы не гостиница»",
  "h1": "Оплатили 2 ночи. Бухгалтерия просит чек — «мы не гостиница»",
  "slug": "buhgalteriya-zhdet-chek-v-chate-my-ne-gostinica",
  "topic_id": "B29",
  "author_id": "dobry-dom",
  "date": "2026-09-19",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Оплатили 2 ночи. Бухгалтерия просит чек — «мы не гостиница»

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

Командировочный гость оплатил 2 ночи переводом; после выезда бухгалтерия запросила чек, хозяин ответил «мы не гостиница». Разбор: почему чек не появляется сам, договор и «Мой налог» до оплаты, что спросить до перевода.

## FAQ in article.html

None — no h2 «Частые вопросы».

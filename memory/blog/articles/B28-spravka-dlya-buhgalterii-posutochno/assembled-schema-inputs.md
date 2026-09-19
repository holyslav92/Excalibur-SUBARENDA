# Schema inputs — B28

topic_id: B28
article_dir: memory/blog/articles/B28-spravka-dlya-buhgalterii-posutochno
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/spravka-dlya-buhgalterii-posutochno-tyumen/`
   - `@id`: `{{SITE_BASE}}/blog/spravka-dlya-buhgalterii-posutochno-tyumen/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — бухгалтерия просит справку и чек до оплаты, хост отвечает «мы не гостиница»; какой пакет документов нужен для командировки в Тюмени; not duplicate headline verbatim.
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
  "title": "Бухгалтер: чек и справка до оплаты. 2 ночи — в чате «мы не гостиница»",
  "h1": "Бухгалтер: чек и справка до оплаты. 2 ночи — в чате «мы не гостиница»",
  "slug": "spravka-dlya-buhgalterii-posutochno-tyumen",
  "topic_id": "B28",
  "author_id": "dobry-dom",
  "date": "2026-09-19",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Бухгалтер: чек и справка до оплаты. 2 ночи — в чате «мы не гостиница»

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

Бухгалтерия требует справку о проживании и чек до оплаты командировки в Тюмень на 2 ночи. Хост отвечает «мы не гостиница» — и гость почти переводит аванс, не понимая, что для найма квартиры нужен другой пакет: договор найма, кассовый чек или чек «Мой налог», иногда акт. Разбор: что спросить до перевода, какие образцы PDF отправить бухгалтеру, почему «мы не гостиница» — не отказ.

## FAQ in article.html

None — no h2 «Частые вопросы».

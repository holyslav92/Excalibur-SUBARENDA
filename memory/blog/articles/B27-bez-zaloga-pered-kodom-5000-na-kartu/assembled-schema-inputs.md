# Schema inputs — B27

topic_id: B27
article_dir: memory/blog/articles/B27-bez-zaloga-pered-kodom-5000-na-kartu
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/blogposting.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/bez-zaloga-pered-kodom-5000-na-kartu/`
   - `@id`: `{{SITE_BASE}}/blog/bez-zaloga-pered-kodom-5000-na-kartu/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — в карточке «без залога», перед кодом просят 5 000 ₽ на карту; что уточнить до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-18`
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
  "title": "Написали «без залога». Перед кодом просят 5 000 ₽ на карту",
  "h1": "Написали «без залога». Перед кодом просят 5 000 ₽ на карту",
  "slug": "bez-zaloga-pered-kodom-5000-na-kartu",
  "topic_id": "B27",
  "author_id": "dobry-dom",
  "date": "2026-09-18",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Написали «без залога». Перед кодом просят 5 000 ₽ на карту

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

Гость оплатил две ночи по карточке «без залога», приехал к подъезду — и перед выдачей кода просят перевести 5 000 ₽ на карту как «страховку». Разбор: значок в объявлении не заменяет переписку; отличие предоплаты, депозита и перевода на карту; почему код не должен становиться рычагом; что спросить до оплаты.

## FAQ in article.html

None — no h2 «Частые вопросы».

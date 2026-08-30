# Schema inputs — B04

topic_id: B04
article_dir: memory/blog/articles/B04-poprosili-foto-pasporta-pri-zaselenii-posutochno-do-oplaty
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/poprosili-foto-pasporta-pri-zaselenii-posutochno-do-oplaty/`
   - `@id`: `{{SITE_BASE}}/blog/poprosili-foto-pasporta-pri-zaselenii-posutochno-do-oplaty/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — как отличить нормальный порядок передачи паспортных данных при посуточном найме от подозрительной схемы до оплаты; не duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-08-30`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add `mainEntity` FAQPage.
11. **NO HowTo** — not required for this archetype.
12. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Попросили фото паспорта до оплаты — под угрозой бронь и данные",
  "h1": "Попросили фото паспорта до оплаты — под угрозой бронь и данные",
  "slug": "poprosili-foto-pasporta-pri-zaselenii-posutochno-do-oplaty",
  "topic_id": "B04",
  "author_id": "dobry-dom",
  "date": "2026-08-30",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Попросили фото паспорта до оплаты — под угрозой бронь и данные

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

Гость ищет квартиру посуточно в Тюмени и получает просьбу прислать фото паспорта и селфи до оплаты, без адреса и условий. Разбор: когда запрос данных нормален, а когда это давление и риск мошенничества. Порядок — сначала адрес и бронь, потом минимум данных для договора, деньги и ключ в конце.

## FAQ in article.html

None — no h2 «Частые вопросы».

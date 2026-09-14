# Schema inputs — B22

topic_id: B22
article_dir: memory/blog/articles/B22-posutochno-tyumen-foto-pasporta-v-chat-kod-ne-prislali
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`** (publish slug from title-brief):
   - `url`: `{{SITE_BASE}}/blog/posutochno-tyumen-foto-pasporta-v-chat-kod-ne-prislali/`
   - `@id`: `{{SITE_BASE}}/blog/posutochno-tyumen-foto-pasporta-v-chat-kod-ne-prislali/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — гость оплатил 3 ночи, отправил фото паспорта и селфи в чат, обещанный код не пришёл, багаж у двери; порядок заселения: сначала доступ и подтверждение брони, потом данные для договора; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-14`
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
  "title": "Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери",
  "h1": "Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери",
  "slug": "posutochno-tyumen-foto-pasporta-v-chat-kod-ne-prislali",
  "topic_id": "B22",
  "author_id": "dobry-dom",
  "date": "2026-09-14",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери

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

Гость оплатил три ночи, приехал к подъезду с багажом, отправил в мессенджер разворот паспорта и селфи по требованию хоста — обещанный код доступа так и не пришёл. Разбор: паспортные данные для договора могут быть нормой, но селфи и фото до передачи способа входа — красный флаг; сначала подтверждённая бронь и инструкция, потом минимальные данные текстом.

## FAQ in article.html

None — no h2 «Частые вопросы».

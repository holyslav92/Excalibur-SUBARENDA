# Schema inputs — B24

topic_id: B24
article_dir: memory/blog/articles/B24-sobaka-do-15-kg-doplata-u-dveri
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/sobaka-do-15-kg-doplata-u-dveri/`
   - `@id`: `{{SITE_BASE}}/blog/sobaka-do-15-kg-doplata-u-dveri/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — собака до 15 кг в переписке, у двери «крупная» и доплата 2 500 ₽ в Тюмени; четыре пункта до оплаты (вес, ограничения, доплата, залог); not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-15`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "В чате: «собака до 15 кг». У двери: «крупная» — 2 500 ₽",
  "h1": "В чате: «собака до 15 кг». У двери: «крупная» — 2 500 ₽",
  "slug": "sobaka-do-15-kg-doplata-u-dveri",
  "topic_id": "B24",
  "author_id": "dobry-dom",
  "date": "2026-09-15",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

В чате: «собака до 15 кг». У двери: «крупная» — 2 500 ₽

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

Гостья приехала в посуточную квартиру в Тюмени с собакой 14 кг: в переписке согласовали «собака до 15 кг», но у двери хост назвал питомца «крупным» и потребовал доплату 2 500 ₽. Разбор: «можно с собакой» — не договорённость; до оплаты нужны четыре ясных ответа (вес числом, ограничения, доплата за период или за ночь, залог); правило, появившееся у двери, — рычаг, а не условие.

## FAQ in article.html

None — no h2 «Частые вопросы».

# Schema inputs — B10

topic_id: B10
article_dir: memory/blog/articles/B10-posutochno-napisali-postelnoe-est-na-krovati-golyj-matras
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/posutochno-napisali-postelnoe-est-na-krovati-golyj-matras/`
   - `@id`: `{{SITE_BASE}}/blog/posutochno-napisali-postelnoe-est-na-krovati-golyj-matras/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — «постельное есть» не гарантирует комплект на каждого гостя; уточнить число комплектов и застеленные места до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-05`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Написали «постельное есть». На кровати — голый матрас, нас троих",
  "h1": "Написали «постельное есть». На кровати — голый матрас, нас троих",
  "slug": "posutochno-napisali-postelnoe-est-na-krovati-golyj-matras",
  "topic_id": "B10",
  "author_id": "dobry-dom",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Написали «постельное есть». На кровати — голый матрас, нас троих

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

Гость после дороги видит в объявлении «постельное есть», но при заезде — голый матрас и один комплект на троих. Слово «есть» не означает число комплектов и застеленные места. До перевода денег нужно письменно уточнить, сколько комплектов подготовят именно на бронь и будут ли кровати застелены к заезду.

## FAQ in article.html

None — no h2 «Частые вопросы».

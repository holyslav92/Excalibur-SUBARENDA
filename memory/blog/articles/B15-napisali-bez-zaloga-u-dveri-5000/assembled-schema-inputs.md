# Schema inputs — B15

topic_id: B15
article_dir: memory/blog/articles/B15-napisali-bez-zaloga-u-dveri-5000
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/napisali-bez-zaloga-u-dveri-5000/`
   - `@id`: `{{SITE_BASE}}/blog/napisali-bez-zaloga-u-dveri-5000/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — фильтр «без залога», оплаченные 2–3 ночи, внезапное требование 5 000 ₽ у двери; до перевода проверить сумму и срок возврата в карточке и чате; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-09`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Написали «без залога». У двери попросили 5 000 ₽",
  "h1": "Написали «без залога». У двери попросили 5 000 ₽",
  "slug": "napisali-bez-zaloga-u-dveri-5000",
  "topic_id": "B15",
  "author_id": "dobry-dom",
  "date": "2026-09-09",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Написали «без залога». У двери попросили 5 000 ₽

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

Гость выбрал квартиру посуточно с фильтром «без залога», оплатил 2–3 ночи и приехал с чемоданом. У двери хозяин впервые потребовал перевести 5 000 ₽ залога «до уборки». Статья объясняет, почему риск не в самой сумме, а в том, что условие появилось после оплаты, и какие вопросы задать до перевода.

## FAQ in article.html

None — no h2 «Частые вопросы».

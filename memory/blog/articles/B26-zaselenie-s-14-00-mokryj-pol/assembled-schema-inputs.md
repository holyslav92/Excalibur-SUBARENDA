# Schema inputs — B26

topic_id: B26
article_dir: memory/blog/articles/B26-zaselenie-s-14-00-mokryj-pol
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`** (publish slug from title-brief / article.meta — NOT article-dir suffix):
   - `url`: `{{SITE_BASE}}/blog/zaselenie-s-14-00-v-15-45-mokryj-pol/`
   - `@id`: `{{SITE_BASE}}/blog/zaselenie-s-14-00-v-15-45-mokryj-pol/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — заезд с двух, но 105 минут с чемоданом: мокрый пол, запах химии, «ещё пять»; как уточнить готовность квартиры при смене гостей в Тюмени; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-17`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Заезд с двух. 105 мин с чемоданом: пахнет химией, мокрый пол, «ещё пять»",
  "h1": "Заезд с двух. 105 мин с чемоданом: пахнет химией, мокрый пол, «ещё пять»",
  "slug": "zaselenie-s-14-00-v-15-45-mokryj-pol",
  "topic_id": "B26",
  "author_id": "dobry-dom",
  "date": "2026-09-17",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Заезд с двух. 105 мин с чемоданом: пахнет химией, мокрый пол, «ещё пять»

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

Гость приехал к обещанному заезду с двух, но 105 минут ждал с чемоданом: мокрый пол, запах бытовой химии, бельё на стуле, «ещё пять минут». Разбор: почему «заезд с 14:00» при смене гостей в тот же день не гарантирует готовую квартиру; какой вопрос задать до оплаты; чем отличается от платного раннего заезда.

## FAQ in article.html

None — no h2 «Частые вопросы».

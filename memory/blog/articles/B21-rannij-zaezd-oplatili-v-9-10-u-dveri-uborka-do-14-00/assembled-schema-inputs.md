# Schema inputs — B21

topic_id: B21
article_dir: memory/blog/articles/B21-rannij-zaezd-oplatili-v-9-10-u-dveri-uborka-do-14-00
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`** (publish slug from title-brief):
   - `url`: `{{SITE_BASE}}/blog/rannij-zaezd-oplatili-v-9-10-u-dveri-uborka-do-14-00/`
   - `@id`: `{{SITE_BASE}}/blog/rannij-zaezd-oplatili-v-9-10-u-dveri-uborka-do-14-00/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — оплаченный ранний заезд не означает готовую квартиру; гость с чемоданом ждал почти пять часов; до оплаты зафиксировать время уборки и ключ; not duplicate headline verbatim.
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
  "title": "Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания",
  "h1": "Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания",
  "slug": "rannij-zaezd-oplatili-v-9-10-u-dveri-uborka-do-14-00",
  "topic_id": "B21",
  "author_id": "dobry-dom",
  "date": "2026-09-14",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания

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

Гость после ночного поезда оплатил ранний заезд и приехал к подъезду с чемоданом, но квартира ещё была в уборке после предыдущих жильцов — почти пять часов ожидания и 890 ₽ на кафе и такси. Разбор: ранний заезд — не опция в объявлении, а состояние конкретной квартиры; до перевода зафиксировать в чате время выезда прежних гостей, готовность белья и передачу ключей.

## FAQ in article.html

None — no h2 «Частые вопросы».

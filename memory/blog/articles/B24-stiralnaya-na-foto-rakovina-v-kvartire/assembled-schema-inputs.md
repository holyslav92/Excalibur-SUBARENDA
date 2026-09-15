# Schema inputs — B24

topic_id: B24
article_dir: memory/blog/articles/B24-stiralnaya-na-foto-rakovina-v-kvartire
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/napisali-stiralnaya-est-v-kvartire-tolko-rakovina/`
   - `@id`: `{{SITE_BASE}}/blog/napisali-stiralnaya-est-v-kvartire-tolko-rakovina/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — фото стиралки в карточке, три ночи в Тюмени, на месте раковина и прачечная ~600 ₽; что спросить до брони; not duplicate headline verbatim.
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
  "title": "На фото — стиралка. На третий день — прачечная за 600 ₽",
  "h1": "На фото — стиралка. На третий день — прачечная за 600 ₽",
  "slug": "napisali-stiralnaya-est-v-kvartire-tolko-rakovina",
  "topic_id": "B24",
  "author_id": "dobry-dom",
  "date": "2026-09-15",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

На фото — стиралка. На третий день — прачечная за 600 ₽

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

Гость снял квартиру в Тюмени на три ночи по фото со стиральной машиной в ванной, а после заселения нашёл раковину, вешалку и сушилку. Общая машинка в подвале оказалась недоступной; на третий день пришлось нести вещи в прачечную (~600 ₽). Разбор: фото создаёт ожидание техники в квартире; один прямой вопрос и видео до оплаты экономят время и деньги.

## FAQ in article.html

None — no h2 «Частые вопросы».

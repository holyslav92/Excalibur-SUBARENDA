# Schema inputs — B15

topic_id: B15
article_dir: memory/blog/articles/B15-zaselilsya-v-22-00-v-10-00-sozvon-wi-fi-ne-vyderzhal
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/zaselilsya-v-22-00-v-10-00-sozvon-wi-fi-ne-vyderzhal/`
   - `@id`: `{{SITE_BASE}}/blog/zaselilsya-v-22-00-v-10-00-sozvon-wi-fi-ne-vyderzhal/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — командировочный после позднего рейса, три ночи за 10 200 ₽; утром видеосозвон сорвался из‑за Wi‑Fi 3–5 Мбит/с у стола; розетка у кровати; до оплаты уточнить скорость загрузки, розетку и документы; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-08`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Заселился после рейса. За 10 200 ₽ Wi‑Fi сорвал созвон",
  "h1": "Заселился после рейса. За 10 200 ₽ Wi‑Fi сорвал созвон",
  "slug": "zaselilsya-v-22-00-v-10-00-sozvon-wi-fi-ne-vyderzhal",
  "topic_id": "B15",
  "author_id": "dobry-dom",
  "date": "2026-09-08",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Заселился после рейса. За 10 200 ₽ Wi‑Fi сорвал созвон

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

Командировочный бронирует квартиру на три ночи за 10 200 ₽ после позднего рейса по обещаниям «Wi‑Fi» и «рабочее место». Утром видеосозвон срывается: у стола загрузка 3–5 Мбит/с, розетка у кровати, а не у рабочего места. До оплаты стоит спросить скорость загрузки именно у стола, наличие розетки и состав закрывающих документов.

## FAQ in article.html

None — no h2 «Частые вопросы».

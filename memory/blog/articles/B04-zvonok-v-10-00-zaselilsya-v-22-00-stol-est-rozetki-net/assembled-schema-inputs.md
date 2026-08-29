# Schema inputs — B04

topic_id: B04
article_dir: memory/blog/articles/B04-zvonok-v-10-00-zaselilsya-v-22-00-stol-est-rozetki-net
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/zvonok-v-10-00-zaselilsya-v-22-00-stol-est-rozetki-net/`
   - `@id`: `{{SITE_BASE}}/blog/zvonok-v-10-00-zaselilsya-v-22-00-stol-est-rozetki-net/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — проверка рабочего места, розетки, Wi‑Fi для созвона и документов до оплаты посуточной квартиры в Тюмени; не duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-08-29`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add `mainEntity` FAQPage.
11. **NO HowTo** — not required for this archetype.
12. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Звонок в 10:00. Заселился в 22:00 — у стола нет розетки",
  "h1": "Звонок в 10:00. Заселился в 22:00 — у стола нет розетки",
  "slug": "zvonok-v-10-00-zaselilsya-v-22-00-stol-est-rozetki-net",
  "topic_id": "B04",
  "author_id": "dobry-dom",
  "date": "2026-08-29",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Звонок в 10:00. Заселился в 22:00 — у стола нет розетки

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

Командировочный гость заселяется поздно вечером, а утром нужен видеозвонок в 10:00. В карточке были «рабочий стол» и Wi‑Fi, но стол без розетки, интернет в коридоре и документы «потом». До оплаты проверить фото рабочего места, тест видеосвязи, время заезда и пакет закрывающих документов.

## FAQ in article.html

None — no h2 «Частые вопросы», no h3+p FAQ pairs.

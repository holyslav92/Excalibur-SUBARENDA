# Schema inputs — B07

topic_id: B07
article_dir: memory/blog/articles/B07-kvartira-posutochno-kuhnya-est-tri-nochi-v-kafe-kazhdyj-den
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/kvartira-posutochno-kuhnya-est-tri-nochi-v-kafe-kazhdyj-den/`
   - `@id`: `{{SITE_BASE}}/blog/kvartira-posutochno-kuhnya-est-tri-nochi-v-kafe-kazhdyj-den/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — галочка «кухня есть» не гарантирует посуду и готовку; за три ночи питание в кафе может добавить около 7 200 ₽; уточнить состав кухни до брони; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-02`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽",
  "h1": "Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽",
  "slug": "kvartira-posutochno-kuhnya-est-tri-nochi-v-kafe-kazhdyj-den",
  "topic_id": "B07",
  "author_id": "dobry-dom",
  "date": "2026-09-02",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽

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

Гость бронирует квартиру на три ночи с отметкой «кухня есть», рассчитывая готовить дома. На месте — плита и холодильник, но почти нет посуды и базовых продуктов. Формально кухня есть, готовить нельзя; питание в кафе обходится примерно в 2 400 ₽ в день и около 7 200 ₽ за три ночи. До оплаты стоит спросить состав кухни: сковороды, кружки, масло, соль, фото ящиков.

## FAQ in article.html

None — no h2 «Частые вопросы».

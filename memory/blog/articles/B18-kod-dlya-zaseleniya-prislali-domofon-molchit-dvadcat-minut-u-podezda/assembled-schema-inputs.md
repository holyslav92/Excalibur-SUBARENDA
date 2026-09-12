# Schema inputs — B18

topic_id: B18
article_dir: memory/blog/articles/B18-kod-dlya-zaseleniya-prislali-domofon-molchit-dvadcat-minut-u-podezda
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema/article.schema.json` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/kod-dlya-zaseleniya-prislali-domofon-molchit-dvadcat-minut-u-podezda/`
   - `@id`: `{{SITE_BASE}}/blog/kod-dlya-zaseleniya-prislali-domofon-molchit-dvadcat-minut-u-podezda/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — код квартиры в чате, домофон подъезда молчит, 20 минут с чемоданом на улице в Тюмени; заселение начинается у подъезда, не у ключницы; один вопрос до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-12`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Код уже есть. Только в подъезд не попасть — 20 минут с чемоданом",
  "h1": "Код уже есть. Только в подъезд не попасть — 20 минут с чемоданом",
  "slug": "kod-dlya-zaseleniya-prislali-domofon-molchit-dvadcat-minut-u-podezda",
  "topic_id": "B18",
  "author_id": "dobry-dom",
  "date": "2026-09-12",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Код уже есть. Только в подъезд не попасть — 20 минут с чемоданом

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

Гость приехал на посуточное заселение в Тюмени с кодом квартиры в переписке, но домофон подъезда не ответил — 20 минут с чемоданом на улице. Код открывает вторую дверь, а первая остаётся закрытой без резервного способа. Разбор: бесконтактное заселение — цепочка «подъезд → этаж → квартира»; до оплаты нужен один вопрос — как открыть подъезд, если домофон молчит.

## FAQ in article.html

None — no h2 «Частые вопросы».

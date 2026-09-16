# Schema inputs — B25

topic_id: B25
article_dir: memory/blog/articles/B25-dve-krovati-na-foto-posutochno-nochyu-divan-i-skladnoj-matras
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/dve-krovati-na-foto-posutochno-nochyu-divan-i-skladnoj-matras/`
   - `@id`: `{{SITE_BASE}}/blog/dve-krovati-na-foto-posutochno-nochyu-divan-i-skladnoj-matras/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — на фото две кровати, ночью троим достался диван и складной матрас в посуточной квартире в Тюмени; как проверить тип спальных мест до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-16`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "На фото две кровати. Ночью троих — диван и складной матрас",
  "h1": "На фото две кровати. Ночью троих — диван и складной матрас",
  "slug": "dve-krovati-na-foto-posutochno-nochyu-divan-i-skladnoj-matras",
  "topic_id": "B25",
  "author_id": "dobry-dom",
  "date": "2026-09-16",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

На фото две кровати. Ночью троих — диван и складной матрас

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

Трое взрослых оплатили около 10 400 ₽ за две ночи: в карточке «2 кровати», на фото — два застеленных места. При заезде — одна двуспальная кровать, диван-кровать и складной матрас на полу. Разбор: почему шапка карточки и блок «Спальные места» расходятся с ожиданиями; какие вопросы задать до перевода; фото дивана в разложенном виде.

## FAQ in article.html

None — no h2 «Частые вопросы».

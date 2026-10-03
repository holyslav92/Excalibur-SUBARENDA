# Schema inputs — B43

topic_id: B43
article_dir: memory/blog/articles/B43-zalog-5-000-obeschali-vernut-k-obedu-v-14-20-napisali-posle-uborki
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/zalog-5-000-obeschali-vernut-k-obedu-v-14-20-napisali-posle-uborki/`
   - `@id`: `{{SITE_BASE}}/blog/zalog-5-000-obeschali-vernut-k-obedu-v-14-20-napisali-posle-uborki/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — залог 5 000 ₽ посуточно, обещали «к обеду», в чате «после уборки» без нового срока; что уточнить до перевода; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-10-03`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "5 000 ₽ залога посуточно: обещали «к обеду». В чате — «после уборки»",
  "h1": "5 000 ₽ залога посуточно: обещали «к обеду». В чате — «после уборки»",
  "slug": "zalog-5-000-obeschali-vernut-k-obedu-v-14-20-napisali-posle-uborki",
  "topic_id": "B43",
  "author_id": "dobry-dom",
  "date": "2026-10-03",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

5 000 ₽ залога посуточно: обещали «к обеду». В чате — «после уборки»

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

Гость перевёл залог 5 000 ₽ посуточно в Тюмени; в чате обещали вернуть «к обеду» после выезда. На осмотре претензий не было, но после обеда срок сменился на «после уборки» без нового времени. Разбор: до перевода зафиксировать сумму, срок, способ и условия удержания; «после уборки» без даты — не договорённость.

## FAQ in article.html

None — no h2 «Частые вопросы».

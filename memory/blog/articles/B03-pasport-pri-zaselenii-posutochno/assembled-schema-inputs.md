# Schema inputs — B03

Output ONLY valid JSON-LD (single JSON object or @graph array). No markdown wrapper, no commentary.

## Task

Build schema.org BlogPosting for this article. Author registry id: dobry-dom.

## Site base (HARD)

- Use placeholder `{{SITE_BASE}}` for all URLs (never literal host, never `[REDACTED]`).
- Canonical article URL: `{{SITE_BASE}}/pasport-pri-zaselenii-posutochno/` (no `/blog/` prefix).
- `@id`: `{{SITE_BASE}}/pasport-pri-zaselenii-posutochno/#article`

## Article meta

```json
{
  "topic_id": "B03",
  "title": "Перевёл предоплату. В личку просят фото паспорта",
  "h1": "Перевёл предоплату. В личку просят фото паспорта",
  "slug": "pasport-pri-zaselenii-posutochno",
  "author_id": "dobry-dom",
  "date": "2026-08-23",
  "theme_blocks": { "faq": "skip" }
}
```

## Description (for BlogPosting.description)

«Фото паспорта — просто формальность?» После предоплаты в Тюмени не спешите отправлять разворот: попросите объяснить цель и предложите показать оригинал при заселении.

## datePublished / dateModified

2026-08-23 (from research-context today_iso)

## Author (from shared/authors-registry.json, id dobry-dom)

- name: Добрый дом
- @type: Organization
- jobTitle: Апартаменты и квартиры посуточно в Тюмени
- url: {{SITE_BASE}}/
- url only: {{SITE_BASE}}/ (do NOT include /blog/ anywhere in schema — gate rejects it)
- addressLocality: Тюмень, RU

## FAQ (HARD)

NO visible FAQ section in article.html (theme_blocks.faq = skip). Do NOT include FAQPage or mainEntity FAQ. BlogPosting only.

## Sibling schema pattern (structure reference only — do not copy FAQ)

B01/B02 use BlogPosting with Organization author/publisher, inLanguage ru-RU, mainEntityOfPage WebPage. B03 has no FAQ — omit mainEntity entirely.

## Required fields

@context, @type BlogPosting, @id, url, headline, description, inLanguage ru-RU, datePublished, dateModified, author, publisher, mainEntityOfPage.

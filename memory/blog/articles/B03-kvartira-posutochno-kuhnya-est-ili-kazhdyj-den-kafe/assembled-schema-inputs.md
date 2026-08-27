# Schema assembled inputs — B03

OUTPUT: ONLY valid JSON-LD (single JSON object). No markdown fences. No commentary.

## Task

Write `schema.jsonld` — BlogPosting for Добрый дом article.

- **NO FAQPage** — article has no «Частые вопросы» section (theme_blocks.faq=skip, no h3 FAQ pairs in HTML).
- **Author/publisher:** Organization «Добрый дом» from authors-registry — NEVER Шакин / The Риэлтор.
- **Site base:** use placeholder `{{SITE_BASE}}` for all URLs (never literal host, never `[REDACTED]`).
- **Canonical article URL (HARD):** `{{SITE_BASE}}/blog/kvartira-posutochno-kuhnya-est-ili-kazhdyj-den-kafe/`
  - BlogPosting `url`, `@id`, `mainEntityOfPage.@id` must all use `/blog/<slug>/` path.
- **datePublished / dateModified:** 2026-08-27 (from research-context).
- **inLanguage:** ru-RU
- **headline:** from article.meta.json H1 below
- **description:** 1–2 sentences summarizing article (kitchen in listing vs reality, 3 nights café cost, Tyumen) — NOT copy of first paragraph verbatim.

## article.meta.json

```json
{
  "title": "Три ночи. «Кухня есть» — каждый завтрак всё равно в кафе",
  "h1": "Три ночи. «Кухня есть» — каждый завтрак всё равно в кафе",
  "slug": "kvartira-posutochno-kuhnya-est-ili-kazhdyj-den-kafe",
  "topic_id": "B03",
  "author_id": "dobry-dom",
  "date": "2026-08-27"
}
```

## authors-registry (dobry-dom)

```json
{
  "id": "dobry-dom",
  "name": "Добрый дом",
  "jobTitle": "Апартаменты и квартиры посуточно в Тюмени",
  "url": "{{SITE_BASE}}/",
  "sameAs": [
    "{{SITE_BASE}}/",
    "{{SITE_BASE}}/blog/"
  ]
}
```

## research-context date

today_iso: 2026-08-27

## article.html (full — no FAQ section)

See article.html in article dir. Key: no `<h2>Частые вопросы</h2>` and no FAQ h3+p pairs.

## Required structure

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "{{SITE_BASE}}/blog/kvartira-posutochno-kuhnya-est-ili-kazhdyj-den-kafe/#article",
  "url": "{{SITE_BASE}}/blog/kvartira-posutochno-kuhnya-est-ili-kazhdyj-den-kafe/",
  "headline": "...",
  "description": "...",
  "inLanguage": "ru-RU",
  "datePublished": "2026-08-27",
  "dateModified": "2026-08-27",
  "author": { "@type": "Organization", "name": "Добрый дом", "url": "{{SITE_BASE}}/" },
  "publisher": { "@type": "Organization", "name": "Добрый дом", "url": "{{SITE_BASE}}/" },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{SITE_BASE}}/blog/kvartira-posutochno-kuhnya-est-ili-kazhdyj-den-kafe/"
  }
}
```

Do NOT add FAQPage or mainEntity FAQ when no visible FAQ in HTML.

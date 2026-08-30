# Schema inputs B04 — OUTPUT RAW JSON-LD ONLY

Write ONLY valid schema.jsonld JSON. No markdown. No commentary. No prose before or after.

## Article

- topic_id: B04
- slug: oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego
- h1: Оплатили за двоих. У двери попросили доплату за третьего
- datePublished: 2026-08-30
- author: Добрый дом (Organization)
- url: {{SITE_BASE}}/blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/

## description (from description-brief)

«Нас двое» — так и бронировали. Но у двери хозяин пересчитал гостей и назвал новую сумму.

## Template (follow structure)

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "{{SITE_BASE}}/blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/#article",
  "url": "{{SITE_BASE}}/blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{SITE_BASE}}/blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/"
  },
  "headline": "Оплатили за двоих. У двери попросили доплату за третьего",
  "description": "...",
  "datePublished": "2026-08-30",
  "dateModified": "2026-08-30",
  "inLanguage": "ru-RU",
  "author": { "@type": "Organization", "name": "Добрый дом", "url": "{{SITE_BASE}}/" },
  "publisher": { "@type": "Organization", "name": "Добрый дом", "url": "{{SITE_BASE}}/" }
}
```

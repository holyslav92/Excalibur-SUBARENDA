# Schema assembled inputs — B03

OUTPUT: **ONLY** valid JSON-LD (single JSON object). No markdown fences. No commentary before or after JSON.

## Task
Build `schema.jsonld` for BlogPosting. **No FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`, no h3 FAQ in HTML).

## Site base (HARD)
- Use placeholder `{{SITE_BASE}}` for all URLs (never literal host, never `[REDACTED]`).
- Canonical article URL: `{{SITE_BASE}}/blog/na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super/`
- BlogPosting `url`, `@id` (with `#article` suffix), `mainEntityOfPage.@id` — all must use `/blog/<slug>/` path.

## Article meta
```json
{
  "topic_id": "B03",
  "slug": "na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super",
  "headline": "Выбрал квартиру с оценкой 4,8. Перед оплатой нашёл одинаковые отзывы",
  "datePublished": "2026-08-27",
  "dateModified": "2026-08-27",
  "inLanguage": "ru-RU",
  "author_id": "dobry-dom"
}
```

## Author (from shared/authors-registry.json — id dobry-dom)
- `@type`: Organization
- `name`: Добрый дом
- `url`: `{{SITE_BASE}}/`
- `sameAs`: `["{{SITE_BASE}}/", "{{SITE_BASE}}/blog/"]`
- **NEVER** Шакин / The Риэлтор

## Description hint (meta description, 1–2 sentences)
Как проверить отзывы и рейтинг перед оплатой квартиры посуточно на Авито и Суточно.ру: низкие оценки, блок «Отзывы без оценки», свежесть комментариев и ответы хозяина в Тюмени.

## Required JSON-LD structure
- `@context`: `https://schema.org`
- `@type`: `BlogPosting`
- `@id`: `{{SITE_BASE}}/blog/na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super/#article`
- `url`: `{{SITE_BASE}}/blog/na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super/`
- `headline`, `description`, `datePublished`, `dateModified`, `inLanguage`
- `author`: Organization Добрый дом
- `publisher`: Organization Добрый дом (same url)
- `mainEntityOfPage`: WebPage with `@id` = canonical article URL
- **Do NOT** add `mainEntity` FAQPage — no visible FAQ in article.html

## title-brief.json (headline reference)
H1: Выбрал квартиру с оценкой 4,8. Перед оплатой нашёл одинаковые отзывы
Subject: отзывы и рейтинг при выборе квартиры посуточно на Авито и Суточно.ру

## article.html excerpt (first paragraph — for description tone)
26 августа в 23:40 Андрей написал мне в чат с чужого объявления. Он ещё ничего не бронировал, но уже собирался в Тюмень на четыре ночи: командировка, квартира за 3 200 ₽ в сутки, 12 800 ₽ всего, предоплата картой прямо сейчас. На экране всё выглядело спокойно: рейтинг 4,8, одиннадцать отзывов, в каждом — «всё супер», «отличная квартира», «рекомендую». Данные карты Андрей уже ввёл. И только перед оплатой зачем-то пролистал страницу ниже.

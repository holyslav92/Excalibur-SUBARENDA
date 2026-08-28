# Schema inputs — B03

topic_id: B03
article_dir: memory/blog/articles/B03-kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/`
   - `@id`: `{{SITE_BASE}}/blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — проверка пешего маршрута до корпуса вуза до оплаты брони посуточно в Тюмени; не duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-08-28`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add `mainEntity` FAQPage.
11. **NO HowTo** — not required for this archetype.
12. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Привезли сына к вузу — «рядом» оказалось 40 минут пешком",
  "h1": "Привезли сына к вузу — «рядом» оказалось 40 минут пешком",
  "slug": "kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki",
  "topic_id": "B03",
  "author_id": "dobry-dom",
  "date": "2026-08-28",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Привезли сына к вузу — «рядом» оказалось 40 минут пешком

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

Родители бронируют квартиру посуточно в Тюмени на ночи перед 1 сентября по обещанию «рядом с вузом», но до нужного корпуса ТюмГУ оказывается 40 минут пешком. «Три остановки» — транспорт, не пеший маршрут. Проверить карту, корпус и минуты до оплаты; согласовать заезд с 14:00 письменно.

## FAQ in article.html

None — no h2 «Частые вопросы».

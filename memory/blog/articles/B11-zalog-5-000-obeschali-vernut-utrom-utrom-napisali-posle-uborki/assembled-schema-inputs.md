# Schema inputs — B11

topic_id: B11
article_dir: memory/blog/articles/B11-zalog-5-000-obeschali-vernut-utrom-utrom-napisali-posle-uborki
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/zalog-5-000-obeschali-vernut-utrom-utrom-napisali-posle-uborki/`
   - `@id`: `{{SITE_BASE}}/blog/zalog-5-000-obeschali-vernut-utrom-utrom-napisali-posle-uborki/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — обещали вернуть залог 5 000 ₽ до обеда, а после выезда срок сменили на «после уборки» без часа; до перевода зафиксировать окно, способ и условия; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-05`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»",
  "h1": "Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»",
  "slug": "zalog-5-000-obeschali-vernut-utrom-utrom-napisali-posle-uborki",
  "topic_id": "B11",
  "author_id": "dobry-dom",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»

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

Гость перевёл залог 5 000 ₽ при заселении, на выезде услышал «верну до обеда», а после сдачи ключей получил цепочку сдвигов: «после уборки», «ждите», «завтра». Спор не о повреждениях, а о размытом сроке без часа. До перевода залога стоит зафиксировать окно возврата, способ перевода и условия удержания одной строкой в чате.

## FAQ in article.html

None — no h2 «Частые вопросы».

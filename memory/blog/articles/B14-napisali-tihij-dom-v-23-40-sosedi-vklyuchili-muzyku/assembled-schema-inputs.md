# Schema inputs — B14

topic_id: B14
article_dir: memory/blog/articles/B14-napisali-tihij-dom-v-23-40-sosedi-vklyuchili-muzyku
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/napisali-tihij-dom-v-23-40-sosedi-vklyuchili-muzyku/`
   - `@id`: `{{SITE_BASE}}/blog/napisali-tihij-dom-v-23-40-sosedi-vklyuchili-muzyku/#article`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — обещание «тихий дом» не отвечает на вопрос о соседях; гость оплатил две ночи за 8 400 ₽, а в 23:40 услышал музыку через стену; до перевода спросить про соседей и план хоста ночью; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-08`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).

## article.meta.json

```json
{
  "title": "«Тихий дом» обещали. За 8 400 ₽ — музыка за стеной ночью",
  "h1": "«Тихий дом» обещали. За 8 400 ₽ — музыка за стеной ночью",
  "slug": "napisali-tihij-dom-v-23-40-sosedi-vklyuchili-muzyku",
  "topic_id": "B14",
  "author_id": "dobry-dom",
  "date": "2026-09-08",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«Тихий дом» обещали. За 8 400 ₽ — музыка за стеной ночью

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

Гость бронирует квартиру на две ночи за 8 400 ₽ после обещания «тихий дом». Вечером всё спокойно, но около 23:40 из соседней квартиры начинается громкая музыка с басом через стену. Фраза «тихо» в объявлении не отвечает на вопросы об этаже, соседях и жалобах в подъезде. До оплаты стоит спросить, кто живёт сбоку и сверху, были ли вечеринки, и что хост делает ночью при шуме.

## FAQ in article.html

None — no h2 «Частые вопросы».

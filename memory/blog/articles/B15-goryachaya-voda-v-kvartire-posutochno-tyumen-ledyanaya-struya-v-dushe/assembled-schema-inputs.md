# Schema inputs — B15

topic_id: B15
article_dir: memory/blog/articles/B15-goryachaya-voda-v-kvartire-posutochno-tyumen-ledyanaya-struya-v-dushe
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — `@graph` with BlogPosting + LocalBusiness (GEO-AI NAP). No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. Use `@graph` array (see B11 pattern).
3. Canonical URLs **must include `/blog/`** and use **publish slug** (not article-dir suffix):
   - publish slug: `napisali-goryachaya-voda-est-v-dushe-ledyanaya-struya`
   - `url`: `{{SITE_BASE}}/blog/napisali-goryachaya-voda-est-v-dushe-ledyanaya-struya/`
   - BlogPosting `@id`: `{{SITE_BASE}}/blog/napisali-goryachaya-voda-est-v-dushe-ledyanaya-struya/`
   - `mainEntityOfPage.@id`: same as url
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — объявление «горячая вода есть», ледяной душ после заселения, просьба включить бойлер и ждать; 7 800–9 600 ₽ за 2–3 ночи; сначала проверка воды, потом перевод; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-09`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. LocalBusiness `@id`: `{{SITE_BASE}}/#organization`; telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author/publisher reference LocalBusiness via `@id`: `{{SITE_BASE}}/#organization`

## article.meta.json

```json
{
  "title": "«Горячая вода есть». В душе — ледяная струя, ждать 40 минут",
  "h1": "«Горячая вода есть». В душе — ледяная струя, ждать 40 минут",
  "slug": "napisali-goryachaya-voda-est-v-dushe-ledyanaya-struya",
  "topic_id": "B15",
  "author_id": "dobry-dom",
  "date": "2026-09-09",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

«Горячая вода есть». В душе — ледяная струя, ждать 40 минут

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

Гость оплачивает посуточную квартиру в Тюмени на 2–3 ночи (7 800–9 600 ₽) после обещания «горячая вода есть». После позднего заселения из душа идёт ледяная струя; хост пишет «включите бойлер, подождите 40 минут». Разница между бойлером, проточным нагревателем и центральным ГВС не должна выясняться в ванной. До оплаты — спросить, где бойлер, был ли включён, сколько реально ждать.

## FAQ in article.html

None — no h2 «Частые вопросы».

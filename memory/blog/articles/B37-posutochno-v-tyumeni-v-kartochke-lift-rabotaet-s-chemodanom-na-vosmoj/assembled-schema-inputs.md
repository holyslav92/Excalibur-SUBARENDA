# Schema inputs — B37

topic_id: B37
article_dir: memory/blog/articles/B37-posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical URLs **must include `/blog/`**:
   - `url`: `{{SITE_BASE}}/blog/posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj/`
   - `@id`: `{{SITE_BASE}}/blog/posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj/#article`
   - `mainEntityOfPage.@id`: `{{SITE_BASE}}/blog/posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj/`
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from article (see below).
6. `description`: 1–2 sentences Russian meta — в карточке «лифт есть», у подъезда табличка «не работает», восьмой этаж и два чемодана, хозяин отвечает «зато вид» вместо плана; что спросить до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-29`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (`theme_blocks.faq: skip`). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).
14. **BAN** stuffing weak cluster «посуточная аренда тюмень» in description.

## article.meta.json

```json
{
  "title": "В карточке лифт работает. С чемоданом на восьмой — 22 минуты по лестнице",
  "h1": "В карточке лифт работает. С чемоданом на восьмой — 22 минуты по лестнице",
  "slug": "posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj",
  "topic_id": "B37",
  "author_id": "dobry-dom",
  "date": "2026-09-29",
  "theme_blocks": { "faq": "skip" }
}
```

## H1 (exact headline)

В карточке лифт работает. С чемоданом на восьмой — 22 минуты по лестнице

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

Пара в Тюмени на две ночи: в объявлении «лифт есть», у лифта бумажка «не работает», восьмой этаж и два чемодана, подъём около 22 минут. Хозяин на вопрос «что делать?» отвечает «поднимитесь, зато вид». Разбор: «лифт есть» не равно «работает сегодня», что уточнить до оплаты и какой план ждать от хоста при поломке.

## FAQ in article.html

None — no h2 «Частые вопросы».

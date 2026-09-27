# Schema inputs — B38

topic_id: B38
article_dir: memory/blog/articles/B38-posutochno-tyumen-bojler-pogas-nochyu-holodnyj-dush
tenant: Добрый дом, Тюмень, посуточная аренда

## Task

Write **only** valid JSON-LD for `schema.jsonld` — single BlogPosting object. No markdown fences, no commentary.

**CRITICAL URL CHECK before you finish:** BlogPosting url, @id, mainEntityOfPage.@id must use:
`{{SITE_BASE}}/posutochno-tyumen-bojler-pogas-nochyu-holodnyj-dush/` and `.../#article` — **NO `/blog/` anywhere in the entire JSON file** (gate rejects any `/blog/` substring including sameAs).
Author @type must be **Organization**, not Person.
Publisher and author telephone +7 (993) 574-83-22, Тюмень.
sameAs: only `["{{SITE_BASE}}/"]` — do not add `/blog/` paths.

## HARD rules

1. `@context`: `https://schema.org`
2. `@type`: `BlogPosting`
3. Canonical article URLs (**NO `/blog/`** — schema gate INC 2026):
   - `url`: `{{SITE_BASE}}/posutochno-tyumen-bojler-pogas-nochyu-holodnyj-dush/`
   - `@id`: `{{SITE_BASE}}/posutochno-tyumen-bojler-pogas-nochyu-holodnyj-dush/#article`
   - `mainEntityOfPage.@id`: `{{SITE_BASE}}/posutochno-tyumen-bojler-pogas-nochyu-holodnyj-dush/`
   - **FORBIDDEN** any `/blog/` substring anywhere in schema.jsonld (including sameAs)
4. Use placeholder `{{SITE_BASE}}` — never literal `[REDACTED]` or live punycode URL in committed file.
5. `headline`: exact H1 from title-brief (see below).
6. `description`: 1–2 sentences Russian meta — карточка обещала душ и горячую воду, в 23:10 бойлер погас и ледяной кран; хозяин «мастер завтра»; четыре вопроса до оплаты; not duplicate headline verbatim.
7. `datePublished` and `dateModified`: `2026-09-27`
8. `inLanguage`: `ru-RU`
9. Author & publisher: Organization **Добрый дом** only — NEVER Шакин / The Риэлтор / риэлтор.
10. telephone: `+7 (993) 574-83-22`, addressLocality: Тюмень, addressCountry: RU
11. **NO FAQPage** — article has no «Частые вопросы» section (standalone h3 is NOT FAQ block). Do not add FAQPage.
12. **NO HowTo** — not required for this archetype.
13. Author `sameAs` from registry (with {{SITE_BASE}} placeholders).
14. **BAN** stuffing weak cluster «посуточная аренда тюмень» in description.

## title-brief H1 (exact headline)

В карточке был душ. В 23:10 бойлер погас — вода стала ледяной

## article.meta.json (synthetic — file not yet on disk)

```json
{
  "title": "В карточке был душ. В 23:10 бойлер погас — вода стала ледяной",
  "h1": "В карточке был душ. В 23:10 бойлер погас — вода стала ледяной",
  "slug": "posutochno-tyumen-bojler-pogas-nochyu-holodnyj-dush",
  "topic_id": "B38",
  "author_id": "dobry-dom",
  "date": "2026-09-27",
  "theme_blocks": { "faq": "skip" }
}
```

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

Пара с ребёнком после дороги из Екатеринбурга: в карточке «всегда горячая вода», в 23:10 душ стал ледяным, индикатор бойлера 30 л мигает красным, хозяин ответил «мастер завтра». Разбор объёма бойлера, автомата в щитке, переписки до оплаты и четырёх вопросов до перевода предоплаты.

## FAQ in article.html

None — no h2 «Частые вопросы».

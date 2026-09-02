# Schema inputs — B07

Output ONLY valid JSON-LD (schema.jsonld), no markdown fences. Do NOT return DEROUTER SCHEMA BLOCKER.

## Data

- slug: snyali-kvartiru-posutochno-v-komnate-17-u-dveri-500-za-obogrevatel
- canonical URL: {{SITE_BASE}}/blog/snyali-kvartiru-posutochno-v-komnate-17-u-dveri-500-za-obogrevatel/  (keep the literal placeholder {{SITE_BASE}} everywhere; NEVER a real host, NEVER [REDACTED])
- headline (exact): Сняли квартиру посуточно. Хотели тепла. У двери: +500 ₽ или спать в куртке
- datePublished = dateModified = 2026-09-02
- inLanguage ru-RU
- description: 1–2 neutral sentences (≠ H1, ≠ Dzen teaser below) about: в Тюмени отопление включают не раньше конца сентября (норматив +8 °C пять суток); гость посуточно может получить платный обогреватель у двери; ночь обогревателя по тарифу 2026 стоит ~45–65 ₽; вопрос про тепло задают в чате до оплаты. Dzen teaser for reference (do not copy): ««Это электричество», — говорит хост у двери и просит 500 ₽ за ночь обогревателя, которая по счётчику стоит 64. В Тюмени тепло включат не раньше конца сентября — про обогреватель спрашивайте до перевода.»
- author + publisher = Organization «Добрый дом» exactly as in the template below (jobTitle, url, sameAs, telephone +7 (993) 574-83-22, address Тюмень RU).
- No FAQPage (article has no FAQ section). No Person, no Шакин/риэлтор. No image field.

## Template (structure to follow exactly; replace slug/headline/description/dates)

{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "{{SITE_BASE}}/blog/vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu/#article",
  "url": "{{SITE_BASE}}/blog/vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu/",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{SITE_BASE}}/blog/vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu/"
  },
  "headline": "Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда",
  "description": "Если выезд из квартиры в Тюмени назначен на полдень, а поезд отправляется через несколько часов, багаж можно заранее оставить по договорённости с менеджером или сдать в камеру хранения на вокзале. Главное — не оставлять чемоданы у подъезда и заложить запас времени на дорогу.",
  "datePublished": "2026-09-01",
  "dateModified": "2026-09-01",
  "inLanguage": "ru-RU",
  "author": {
    "@type": "Organization",
    "@id": "{{SITE_BASE}}/#organization",
    "name": "Добрый дом",
    "jobTitle": "Апартаменты и квартиры посуточно в Тюмени",
    "url": "{{SITE_BASE}}/",
    "sameAs": [
      "{{SITE_BASE}}/",
      "{{SITE_BASE}}/blog/"
    ],
    "telephone": "+7 (993) 574-83-22",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Тюмень",
      "addressCountry": "RU"
    }
  },
  "publisher": {
    "@type": "Organization",
    "@id": "{{SITE_BASE}}/#organization",
    "name": "Добрый дом",
    "url": "{{SITE_BASE}}/",
    "sameAs": [
      "{{SITE_BASE}}/",
      "{{SITE_BASE}}/blog/"
    ],
    "telephone": "+7 (993) 574-83-22",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Тюмень",
      "addressCountry": "RU"
    }
  }
}


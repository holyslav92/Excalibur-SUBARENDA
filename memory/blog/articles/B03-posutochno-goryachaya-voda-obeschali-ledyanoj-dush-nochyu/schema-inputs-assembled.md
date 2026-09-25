# Schema inputs — B03

## Site base
Use placeholder `{{SITE_BASE}}` for all URLs. Canonical article URL: `{{SITE_BASE}}/posutochno-goryachaya-voda-obeschali-ledyanoj-dush-nochyu/` (no /blog/ prefix).

## Article meta (article.meta.json)
- topic_id: B03
- slug: posutochno-goryachaya-voda-obeschali-ledyanoj-dush-nochyu
- headline (H1): Обещали горячую воду. В 23:40 душ выдал ледяную струю
- datePublished: 2026-09-25
- dateModified: 2026-09-25
- author_id: dobry-dom
- inLanguage: ru-RU

## Description (for BlogPosting.description)
Как не остаться без горячей воды в посуточной квартире в Тюмени: бойлер, магистраль, что спросить до оплаты и кто на связи ночью при бесконтактном заезде.

## Author (shared/authors-registry.json — dobry-dom)
- name: Добрый дом
- jobTitle: Апартаменты и квартиры посуточно в Тюмени
- url: {{SITE_BASE}}/
- sameAs: {{SITE_BASE}}/ and {{SITE_BASE}}/blog/
- Use Organization author pattern like sibling articles B01/B02 (name + url).

## FAQ section (visible in article.html — include FAQPage as mainEntity)
Only these h3+p pairs (first p after each h3 only):

1. Q: Можно ли проверить горячую воду только по адресу дома?
   A: Можно проверить отключение на городской магистрали, в том числе через УСТЭК. Но это не покажет состояние внутридомовых сетей и конкретной квартиры.

2. Q: Сколько ждать горячую воду от накопительного бойлера?
   A: В описанном сценарии после включения это может занять 40–80 минут. Поэтому важнее заранее уточнить, включён ли он и прогрет ли к вашему заезду.

3. Q: Что спросить у хозяина до оплаты?
   A: Уточните источник горячей воды, тип бойлера, время прогрева, известные отключения и того, кто отвечает ночью. Лучше получить ответы в переписке.

4. Q: Что делать, если вода холодная при позднем бесконтактном заезде?
   A: Написать хозяину сразу. До бронирования стоит заранее узнать, кто будет на связи ночью и как устроена поддержка после получения кода.

## Output format
Single valid JSON object only (no markdown fences): BlogPosting with @context, @type, @id, url, headline, description, inLanguage, datePublished, dateModified, author, publisher, mainEntityOfPage, and mainEntity FAQPage matching FAQ above exactly.

# Assembled research inputs B03

## research-inputs.md

# Research inputs — B03

Read: research-context.json, research-serp.json
Date: 2026-08-23 (Europe/Moscow / Asia/Yekaterinburg)
Topic: фото паспорта при заселении посуточно — что законно, как не попасть в мошенничество
Tenant: Добрый дом — посуточная аренда Тюмень, humble warm host voice
Anti-dup: B01 = бесконтактное заселение / коды; B02 = залог/депозит; B03 = паспорт/идентификация при заселении

Wordstat (MCP-KV live 2026-08-23):
- фото паспорта при аренде квартир — 89 (RU 225)
- фото паспорта при аренде квартиры посуточно — 36 (RU 225)
- паспорт при заселении в квартиру посуточно — 1 (Tyumen 55+11176)
- Rework P0 phrase: «фото паспорта при аренде квартир» volume 89

SERP signals (accessed 2026-08-23):
- Гостиницы и квартиры: регистрация по месту пребывания — госуслуги / МВД
- Правовед / vc.ru / форумы: гости боятся слать фото паспорта до оплаты
- B01 FAQ already notes: паспорт нужен даже при бесконтактном заселении

CTA channels (factory): booking https://добрыйдом-72.рф/booking/, TG https://t.me/Dobriy_dom_72, MAX https://max.ru/id660300569233_biz, manager https://t.me/Dobriy_dom_Tyumen, phone +7 993 574-83-22
Interlink: B01 /blog/beskontaktnoe-zaselenie-posutochno-tyumen/, B02 /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/

Output research-notes.md with source_table, writer_safe_urls, reader_problem, practical_facts, wordstat_stickers for cover (фото паспорта, посуточно, Тюмень).
Season: late August 2026 — no winter hero references.
Fresh community signal required (forum/pravoved this week angle on passport scams).


## research-context.json

{
  "agent": "excalibur-blog",
  "step": "research_start",
  "date_context": {
    "timezone": "Europe/Moscow",
    "today_iso": "2026-08-23",
    "today_ru": "23.08.2026",
    "year": 2026,
    "month": 8,
    "month_name_ru": "август",
    "weekday_ru": "воскресенье"
  },
  "topic": {
    "topic_id": "B03",
    "title": "Попросили фото паспорта при заселении посуточно — что законно",
    "h1": "Попросили фото паспорта при заселении посуточно — что законно",
    "slug": "poprosili-foto-pasporta-pri-zaselenii-posutochno-chto-zakonno",
    "primary_query": "Попросили фото паспорта при заселении посуточно — что законно",
    "priority": "P0"
  },
  "search_queries": [
    {
      "id": "primary_fresh",
      "query": "Попросили фото паспорта при заселении посуточно — что законно 2026",
      "purpose": "актуальный SERP"
    },
    {
      "id": "title_fresh",
      "query": "Попросили фото паспорта при заселении посуточно — что законно 2026",
      "purpose": "SERP по человеческому title"
    },
    {
      "id": "official_docs",
      "query": "Попросили фото паспорта при заселении посуточно — что законно official docs 2026",
      "purpose": "официальные docs"
    },
    {
      "id": "github_evidence",
      "query": "site:github.com Попросили фото паспорта при заселении посуточно — что законно 2026",
      "purpose": "GitHub evidence"
    },
    {
      "id": "community_experience",
      "query": "Попросили фото паспорта при заселении посуточно — что законно forum problems опыт 2026",
      "purpose": "форумы и живые проблемы"
    }
  ],
  "next_step": "Research reads research-serp.json, does its own thinking and writes research-notes.md",
  "writer_allowed_sources": [
    "shared/writer-master-prompt.md",
    "research-notes.md",
    "title-brief.json",
    "published-titles-only.md"
  ],
  "sol_allowed_sources": [
    "shared/SOUL.md",
    "shared/soul-examples/",
    "drafts/writer.html",
    "title-brief.json",
    "research-notes.md"
  ],
  "writer_titles_only": "published-titles-only.md",
  "forbidden_sources_for_writer": [
    "memory/blog/articles/*/article.html",
    "memory/blog/articles/*/drafts",
    "memory/topics/ (deleted — do not recreate)",
    "memory/content-lessons.md",
    "shared/golden-benchmark",
    "QA reports",
    "neighbor research-notes as prose exemplars",
    "old article bodies"
  ],
  "published_titles_count": 2
}

## research-serp.json

{
  "agent": "excalibur-blog",
  "date_context": {
    "timezone": "Europe/Moscow",
    "today_iso": "2026-08-23",
    "today_ru": "23.08.2026",
    "year": 2026,
    "month": 8,
    "month_name_ru": "август",
    "weekday_ru": "воскресенье"
  },
  "topic": {
    "topic_id": "B03",
    "title": "Попросили фото паспорта при заселении посуточно — что законно",
    "h1": "Попросили фото паспорта при заселении посуточно — что законно",
    "slug": "poprosili-foto-pasporta-pri-zaselenii-posutochno-chto-zakonno",
    "primary_query": "Попросили фото паспорта при заселении посуточно — что законно",
    "priority": "P0"
  },
  "searches": [
    {
      "query_id": "primary_fresh",
      "query": "Попросили фото паспорта при заселении посуточно — что законно 2026",
      "purpose": "актуальный SERP",
      "result_count": 6,
      "results": [
        {
          "title": "Здравствуйте, скажите пожалуйста, при бронирование квартиры посуточно ...",
          "url": "https://pravoved.ru/question/4842885/",
          "snippet": ""
        },
        {
          "title": "Запрос паспорта и прописки при аренде: законность и ваши права • Вопрос ...",
          "url": "https://harant.ru/questions/q-84921/",
          "snippet": "Требовать копию паспорта для идентификации гостя законно — это помогает соблюдать правила регистрации и безопасности. Однако важно: данные должны обрабатываться с вашего согласия, храниться конфиденциально и удаляться после заселения. Многие арендодатели нарушают эти правила, создавая риски утечки."
        },
        {
          "title": "Фотографирование паспорта при посуточной аренде: законно ли?",
          "url": "https://pravoved.ru/question/2398486/",
          "snippet": "Но требовать фотографию паспорта с лицом — избыточно и не предусмотрено законом. Вы можете предоставить копии паспортов, но делать фото с лицом не обязаны. Если нужна помощь — пишите!"
        },
        {
          "title": "Обязан ли арендатор показывать паспорт при съёме квартиры? Вот что ...",
          "url": "https://secretmag.ru/potreblenie/obyazan-li-arendator-pokazyvat-pasport-pri-syome-kvartiry-vot-chto-govorit-zakon.htm",
          "snippet": "Нужно ли предоставлять паспорт для фотосъемки при посуточной аренде квартиры и какие риски это может повлечь для арендатора."
        },
        {
          "title": "Фотографирование паспорта при посуточном заселении: правовые аспекты и ...",
          "url": "https://prav.io/browse/questions/fotografirovanie-pasporta-pri-posutochnom-zaselenii-pravovye-aspekty-i-trebovaniya-klienta",
          "snippet": "Юрист Полищук: арендодатель имеет право спрашивать паспорт у квартиросъёмщика. Это нужно, чтобы владелец жилья смог заполнить или сверить в договоре информацию о месте регистрации съёмщика. Также сведения из паспорта пригодятся ему на случай судебных споров."
        },
        {
          "title": "Отправлять фото паспорта и прописки арендодателю: риски и выгоды для ...",
          "url": "https://prav.io/browse/questions/otpravlyat-foto-pasporta-i-propiski-arendodatelyu-riski-i-vygody-dlya-zaklyucheniya-dogovora",
          "snippet": "Согласно законодательству Российской Федерации, для фотографирования паспорта клиента при посуточном заселении без письменного согласия клиента требуется его явное согласие."
        }
      ],
      "searched_at": "2026-08-23"
    },
    {
      "query_id": "title_fresh",
      "query": "Попросили фото паспорта при заселении посуточно — что законно 2026",
      "purpose": "SERP по человеческому title",
      "result_count": 6,
      "results": [
        {
          "title": "Здравствуйте, скажите пожалуйста, при бронирование квартиры посуточно ...",
          "url": "https://pravoved.ru/question/4842885/",
          "snippet": ""
        },
        {
          "title": "Запрос паспорта и прописки при аренде: законность и ваши права • Вопрос ...",
          "url": "https://harant.ru/questions/q-84921/",
          "snippet": "Требовать копию паспорта для идентификации гостя законно — это помогает соблюдать правила регистрации и безопасности. Однако важно: данные должны обрабатываться с вашего согласия, храниться конфиденциально и удаляться после заселения. Многие арендодатели нарушают эти правила, создавая риски утечки."
        },
        {
          "title": "Фотографирование паспорта при посуточной аренде: законно ли?",
          "url": "https://pravoved.ru/question/2398486/",
          "snippet": "Но требовать фотографию паспорта с лицом — избыточно и не предусмотрено законом. Вы можете предоставить копии паспортов, но делать фото с лицом не обязаны. Если нужна помощь — пишите!"
        },
        {
          "title": "Обязан ли арендатор показывать паспорт при съёме квартиры? Вот что ...",
          "url": "https://secretmag.ru/potreblenie/obyazan-li-arendator-pokazyvat-pasport-pri-syome-kvartiry-vot-chto-govorit-zakon.htm",
          "snippet": "Нужно ли предоставлять паспорт для фотосъемки при посуточной аренде квартиры и какие риски это может повлечь для арендатора."
        },
        {
          "title": "Фотографирование паспорта при посуточном заселении: правовые аспекты и ...",
          "url": "https://prav.io/browse/questions/fotografirovanie-pasporta-pri-posutochnom-zaselenii-pravovye-aspekty-i-trebovaniya-klienta",
          "snippet": "Юрист Полищук: арендодатель имеет право спрашивать паспорт у квартиросъёмщика. Это нужно, чтобы владелец жилья смог заполнить или сверить в договоре информацию о месте регистрации съёмщика. Также сведения из паспорта пригодятся ему на случай судебных споров."
        },
        {
          "title": "Отправлять фото паспорта и прописки арендодателю: риски и выгоды для ...",
          "url": "https://prav.io/browse/questions/otpravlyat-foto-pasporta-i-propiski-arendodatelyu-riski-i-vygody-dlya-zaklyucheniya-dogovora",
          "snippet": "Согласно законодательству Российской Федерации, для фотографирования паспорта клиента при посуточном заселении без письменного согласия клиента требуется его явное согласие."
        }
      ],
      "searched_at": "2026-08-23"
    },
    {
      "query_id": "official_docs",
      "query": "Попросили фото паспорта при заселении посуточно — что законно official docs 2026",
      "purpose": "официальные docs",
      "result_count": 6,
      "results": [
        {
          "title": "Здравствуйте, скажите пожалуйста, при бронирование квартиры посуточно ...",
          "url": "https://pravoved.ru/question/4842885/",
          "snippet": ""
        },
        {
          "title": "Фотографирование паспорта при посуточной аренде: законно ли?",
          "url": "https://pravoved.ru/question/2398486/",
          "snippet": "Требовать копию паспорта для идентификации гостя законно — это помогает соблюдать правила регистрации и безопасности. Однако важно: данные должны обрабатываться с вашего согласия, храниться конфиденциально и удаляться после заселения. Многие арендодатели нарушают эти правила, создавая риски утечки."
        },
        {
          "title": "Запрос паспорта и прописки при аренде: законность и ваши права • Вопрос ...",
          "url": "https://harant.ru/questions/q-84921/",
          "snippet": "Нужно ли предоставлять паспорт для фотосъемки при посуточной аренде квартиры и какие риски это может повлечь для арендатора."
        },
        {
          "title": "Аренда квартиры: обязательно ли показывать паспорт владельцу жилья",
          "url": "https://secretmag.ru/potreblenie/obyazan-li-arendator-pokazyvat-pasport-pri-syome-kvartiry-vot-chto-govorit-zakon.htm",
          "snippet": "Но требовать фотографию паспорта с лицом — избыточно и не предусмотрено законом. Вы можете предоставить копии паспортов, но делать фото с лицом не обязаны. Если нужна помощь — пишите!"
        },
        {
          "title": "Фотографирование паспорта при посуточном заселении: правовые аспекты и ...",
          "url": "https://prav.io/browse/questions/fotografirovanie-pasporta-pri-posutochnom-zaselenii-pravovye-aspekty-i-trebovaniya-klienta",
          "snippet": "При заселении в квартиру от арендаторов часто требуют фото паспорта и сведения о прописке. Но не всем хочется показывать свой паспорт просто арендодателю-частнику, неофициальному лицу. Можно ли вообще отказаться от предъявления документов, обойдясь составлением договора найма жилого помещения?"
        },
        {
          "title": "Правила оформления договора аренды: прописка, фотографирование паспорта ...",
          "url": "https://prav.io/browse/questions/pravila-oformleniya-dogovora-arendy-propiska-fotografirovanie-pasporta-i-dannye-v-dogovore",
          "snippet": "Согласно законодательству Российской Федерации, для фотографирования паспорта клиента при посуточном заселении без письменного согласия клиента требуется его явное согласие."
        }
      ],
      "searched_at": "2026-08-23"
    },
    {
      "query_id": "github_evidence",
      "query": "site:github.com Попросили фото паспорта при заселении посуточно — что законно 2026",
      "purpose": "GitHub evidence",
      "result_count": 6,
      "results": [
        {
          "title": "leaf/images/preview.png at main · RivoLink/leaf · GitHub",
          "url": "https://github.com/RivoLink/leaf/blob/main/images/preview.png",
          "snippet": ""
        },
        {
          "title": "imagehost/STMemoryBooks/overlap.png at main · aikohanasaki/imagehost ...",
          "url": "https://github.com/aikohanasaki/imagehost/blob/main/STMemoryBooks/overlap.png",
          "snippet": "Terminal Markdown previewer — GUI-like experience. - RivoLink/leaf"
        },
        {
          "title": "zp.midpass.ru-help.md · GitHub",
          "url": "https://gist.github.com/amper43/511c7c1eb95653999376c06734edaf6d",
          "snippet": "Contribute to aikohanasaki/imagehost development by creating an account on GitHub."
        },
        {
          "title": "wiki/deep-learning-volatility-surface/images/implied ... - GitHub",
          "url": "https://github.com/paperswithbacktest/wiki/blob/main/deep-learning-volatility-surface/images/implied-volatility-surface.svg",
          "snippet": "При помощи этих подсказок уже осуществлялись подачи на загранпаспорт в Гюмри и Ереване - все прошло успешно, работники консульства не задавали никаких вопросов. Для подачи на загран алгоритм такой: Ловим слот и записываемся в Ереван/Гюмри."
        },
        {
          "title": "RxnCaption/assets/logo.png at main · opendatalab/RxnCaption",
          "url": "https://github.com/opendatalab/RxnCaption/blob/main/assets/logo.png",
          "snippet": "Contribute to paperswithbacktest/wiki development by creating an account on GitHub."
        },
        {
          "title": "[Проблема] · Issue #7621 · Flowseal/zapret-discord-youtube",
          "url": "https://github.com/Flowseal/zapret-discord-youtube/issues/7621",
          "snippet": "[CVPR 2026] SOTA Chemical Reaction Diagram Parsing Framework - RxnCaption/assets/logo.png at main · opendatalab/RxnCaption"
        }
      ],
      "searched_at": "2026-08-23"
    },
    {
      "query_id": "community_experience",
      "query": "Попросили фото паспорта при заселении посуточно — что законно forum problems опыт 2026",
      "purpose": "форумы и живые проблемы",
      "result_count": 6,
      "results": [
        {
          "title": "Фотографирование паспорта при посуточной аренде: законно ли?",
          "url": "https://pravoved.ru/question/2398486/",
          "snippet": ""
        },
        {
          "title": "Здравствуйте, скажите пожалуйста, при бронирование квартиры посуточно ...",
          "url": "https://pravoved.ru/question/4842885/",
          "snippet": "Нужно ли предоставлять паспорт для фотосъемки при посуточной аренде квартиры и какие риски это может повлечь для арендатора."
        },
        {
          "title": "Запрос паспорта и прописки при аренде: законность и ваши права • Вопрос ...",
          "url": "https://harant.ru/questions/q-84921/",
          "snippet": "Требовать копию паспорта для идентификации гостя законно — это помогает соблюдать правила регистрации и безопасности. Однако важно: данные должны обрабатываться с вашего согласия, храниться конфиденциально и удаляться после заселения. Многие арендодатели нарушают эти правила, создавая риски утечки."
        },
        {
          "title": "Аренда квартиры: обязательно ли показывать паспорт владельцу жилья",
          "url": "https://secretmag.ru/potreblenie/obyazan-li-arendator-pokazyvat-pasport-pri-syome-kvartiry-vot-chto-govorit-zakon.htm",
          "snippet": "Но требовать фотографию паспорта с лицом — избыточно и не предусмотрено законом. Вы можете предоставить копии паспортов, но делать фото с лицом не обязаны. Если нужна помощь — пишите!"
        },
        {
          "title": "Фотографирование паспорта при посуточном заселении: правовые аспекты и ...",
          "url": "https://prav.io/browse/questions/fotografirovanie-pasporta-pri-posutochnom-zaselenii-pravovye-aspekty-i-trebovaniya-klienta",
          "snippet": "Юрист Полищук: арендодатель имеет право спрашивать паспорт у квартиросъёмщика. Это нужно, чтобы владелец жилья смог заполнить или сверить в договоре информацию о месте регистрации съёмщика. Также сведения из паспорта пригодятся ему на случай судебных споров."
        },
        {
          "title": "Отправлять фото паспорта и прописки арендодателю: риски и выгоды для ...",
          "url": "https://prav.io/browse/questions/otpravlyat-foto-pasporta-i-propiski-arendodatelyu-riski-i-vygody-dlya-zaklyucheniya-dogovora",
          "snippet": "Согласно законодательству Российской Федерации, для фотографирования паспорта клиента при посуточном заселении без письменного согласия клиента требуется его явное согласие."
        }
      ],
      "searched_at": "2026-08-23"
    }
  ],
  "errors": []
}

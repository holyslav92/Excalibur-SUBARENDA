# cover-scene B01
Output JSON only with scene_hint and alt for cover + inline_1..inline_7.
Rules: NO Shakin/host identity face. Russian people OK for check-in scenes. Logo lockup "Добрый дом" on all panels.
cover-text: {
  "hook": "Гость, проверь два кода до оплаты",
  "highlight": "два",
  "sticky": "Один код — не вход",
  "logo_lockup": "Добрый дом",
  "wordstat_stickers": [
    "квартира посуточно Тюмень",
    "снять квартиру посуточно Тюмень"
  ],
  "inline_labels": {
    "inline_1": [
      "23:00 на улице",
      "код от квартиры",
      "домофон закрыт",
      "минус 25 °C",
      "ключница замёрзла"
    ],
    "inline_2": [
      "7 вопросов",
      "адрес до оплаты",
      "кто после 22:00",
      "план «Б»",
      "залог до перевода"
    ],
    "inline_3": [
      "дом и корпус",
      "подъезд 2",
      "этаж 9",
      "два разных кода",
      "скриншот в телефон"
    ],
    "inline_4": [
      "код в день заезда",
      "мессенджер",
      "СМС дубль",
      "время приезда",
      "связь в дороге"
    ],
    "inline_5": [
      "дежурный после 22:00",
      "план «Б»",
      "дубликат ключа",
      "15 минут",
      "живой ответ"
    ],
    "inline_6": [
      "залог: сумма",
      "форма оплаты",
      "срок возврата",
      "фото при заезде",
      "до перевода"
    ],
    "inline_7": [
      "тишина после 21:00",
      "число гостей",
      "курение запрещено",
      "соседи",
      "правила до заезда"
    ]
  }
}

manifest: {
  "topic_id": "B01",
  "canvas_file": "cover/canvas-quad-01.png",
  "layout": "2x2",
  "pipeline": "quad_canvas_2x_image_api_longform",
  "inline_count": 7,
  "canvases": [
    {
      "index": 1,
      "canvas_file": "cover/canvas-quad-01.png",
      "batch_file": "cover/quad-mcp-batch-01.json",
      "prompt_file": "cover/quad-mcp-prompt-01.txt",
      "result_file": "cover/quad-mcp-result-01.json",
      "slots": [
        "cover",
        "inline_1",
        "inline_2",
        "inline_3"
      ],
      "has_cover": true
    },
    {
      "index": 2,
      "canvas_file": "cover/canvas-quad-02.png",
      "batch_file": "cover/quad-mcp-batch-02.json",
      "prompt_file": "cover/quad-mcp-prompt-02.txt",
      "result_file": "cover/quad-mcp-result-02.json",
      "slots": [
        "inline_4",
        "inline_5",
        "inline_6",
        "inline_7"
      ],
      "has_cover": false
    }
  ],
  "style_preset": "the_rieltor_twilight_gold",
  "style_file": "memory/cover/quad-style-dobry-dom.json",
  "blog_hero": "memory/cover/blog-hero.json",
  "inline_types_catalog": "memory/cover/inline-visual-types.json",
  "cover_hook": "Гость, проверь два кода до оплаты",
  "cover_hook_highlight": "два",
  "cover_hook_contract": "shared/blog-cover-quad-canvas-contract.md",
  "mcp_note": "PRIMARY: Derouter REST (DEROUTER_API_KEY) — 2K 16:9, one job per canvas (2×). Cover agent invents cover_hook + scene_hint/alt before --write-batch. Host lock = blog-hero.json (navy blazer, not hoodie).",
  "slots": {
    "cover": {
      "quadrant": "top_left",
      "role": "cover_editorial_hero",
      "alt": "",
      "scene_hint": "Russian guest with suitcase at apartment door at night, checking phone code, warm high-key collage, logo Добрый дом corner, NO celebrity host face",
      "meme_caption_ru": "",
      "sticky": "Один код — не вход"
    },
    "inline_1": {
      "quadrant": "top_right",
      "h2_anchor": "Быстрый инсайт",
      "visual_type": "comparison_table_ui",
      "scene_hint": "",
      "alt": "",
      "labels": [
        "23:00 на улице",
        "код от квартиры",
        "домофон закрыт",
        "минус 25 °C",
        "ключница замёрзла"
      ]
    },
    "inline_2": {
      "quadrant": "bottom_left",
      "h2_anchor": "Что обычно идёт не так в 23:00",
      "visual_type": "workflow_diagram",
      "scene_hint": "",
      "alt": "",
      "labels": [
        "7 вопросов",
        "адрес до оплаты",
        "кто после 22:00",
        "план «Б»",
        "залог до перевода"
      ]
    },
    "inline_3": {
      "quadrant": "bottom_right",
      "h2_anchor": "Семь вопросов до перевода денег",
      "visual_type": "checklist_board",
      "scene_hint": "",
      "alt": "",
      "labels": [
        "дом и корпус",
        "подъезд 2",
        "этаж 9",
        "два разных кода",
        "скриншот в телефон"
      ]
    },
    "inline_4": {
      "quadrant": "top_left",
      "h2_anchor": "Подъезд и квартира — два разных доступа",
      "visual_type": "schema_faq_ui",
      "scene_hint": "",
      "alt": "",
      "labels": [
        "код в день заезда",
        "мессенджер",
        "СМС дубль",
        "время приезда",
        "связь в дороге"
      ]
    },
    "inline_5": {
      "quadrant": "top_right",
      "h2_anchor": "На словах и в инструкции",
      "visual_type": "tool_screenshot",
      "scene_hint": "",
      "alt": "",
      "labels": [
        "дежурный после 22:00",
        "план «Б»",
        "дубликат ключа",
        "15 минут",
        "живой ответ"
      ]
    },
    "inline_6": {
      "quadrant": "bottom_left",
      "h2_anchor": "Когда приходит код",
      "visual_type": "infographic_card",
      "scene_hint": "",
      "alt": "",
      "labels": [
        "залог: сумма",
        "форма оплаты",
        "срок возврата",
        "фото при заезде",
        "до перевода"
      ]
    },
    "inline_7": {
      "quadrant": "bottom_right",
      "h2_anchor": "Кто отвечает ночью",
      "visual_type": "comparison_table_ui",
      "scene_hint": "",
      "alt": "",
      "labels": [
        "тишина после 21:00",
        "число гостей",
        "курение запрещено",
        "соседи",
        "правила до заезда"
      ]
    }
  },
  "cover_keys_ru": [],
  "cover_emotion": "настороженность у подъезда ночью",
  "wordstat_stickers": [
    "квартиры посуточно тюмень",
    "бесконтактное заселение",
    "заселение посуточно"
  ],
  "logo_lockup": {
    "text": "Добрый дом",
    "path": "memory/cover/assets/brand/dobry-dom-logo.png",
    "all_panels": true
  },
  "cover_motifs": {
    "composition": "night apartment entrance collage with phone showing wrong code",
    "location": "Tyumen residential entrance winter",
    "meme": "small cat sticker confused at door",
    "prop_set": "suitcase, keybox, smartphone, door intercom",
    "sticker_set": "wordstat labels + logo lockup",
    "joke": "code opens neighbor door"
  },
  "skip_identity_i2i": true,
  "no_host_face": true
}


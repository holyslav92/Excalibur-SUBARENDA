# Cover-scene inputs — B03 (Derouter Terra)

Tenant: **Добрый дом** · cover_mode: **brand_logo_paste** · season: **август 2026, лето Тюмень** — NO winter/snow/frost.

## cover-text.json (exact Russian inscriptions)

```json
{
  "hook": "Шесть гостей — залог не вернули",
  "highlight": "гостей",
  "sticky": "Правила до оплаты",
  "wordstat_stickers": ["аренда квартиры тюмень посуточно", "снять посуточно"]
}
```

## Article scene (opening)

Августовская пятница, двушка в центре Тюмени. Предоплата за две ночи, правила пришли отдельным сообщением — гость пролистнул. Вечером приехали друзья: шесть человек вместо трёх. В час ночи звонок хозяину, утром досрочный выезд, залог не вернули.

## 7 H2 anchors + inline labels (from cover-text.json)

1. **Сколько гостей можно** — labels: до 4 гостей, двое в правилах, гость на час
2. **Вечеринки и тишина** — labels: тишина ночью, шумная компания, жалоба соседей
3. **Курение балкон/вейп** — labels: курение на балконе, вейп и кальян, сумма за нарушение
4. **Заселение и выезд** — labels: заезд после 14, выезд до 12, ранний заезд
5. **Залог и удержание** — labels: удержат за курение, лишние гости, срок возврата
6. **Фото при заселении** — labels: видео одним дублем, пятна в день, сколы в день
7. **Правила до оплаты** — labels: правила до оплаты, текстом в чат, одна переписка

## Anti-repeat (used in last 14 days — DO NOT reuse)

- B01: night entrance phone code, keybox suitcase, wrong door code
- B02: kitchen chip on stove, phone bubble залог не вернули, cat reacts to chip

## Invent NEW motifs for B03

Topic: правила посуточной аренды до оплаты — лишние гости, вечеринки, мелкий шрифт правил.

Requirements:
- WOW magazine poster, high-key #FFFFFF, sun flare, August Tyumen summer
- NO Shakin/host face; guests by topic OK on cover only
- NO brand logo in generation — TOP-RIGHT empty pad 8-12%
- Meme cat sticker bottom-left ≤12%
- 1-3 Wordstat stickers from cover-text
- cover_phone_cta: +7 (993) 574-83-22 (post-composite, not in generation)
- logo_paste_inline_slots: inline_1, inline_3, inline_7
- inline: utility infographic, NO host face, NO co-host stock man
- visual_types: comparison_table, process_flow, labeled_checklist, bar_timeline_chart, structure_diagram, fact_card, schema_faq_ui

## Required JSON output shape

```json
{
  "cover_emotion": "...",
  "scene_hint": "80-140 chars cover scene + emotion",
  "cover_motifs": {
    "composition": "...",
    "location": "...",
    "meme": "...",
    "prop_set": "...",
    "sticker_set": ["..."],
    "joke": "..."
  },
  "wordstat_stickers": ["..."],
  "cover_phone_cta": "+7 (993) 574-83-22",
  "logo_paste_inline_slots": ["inline_1", "inline_3", "inline_7"],
  "slots": {
    "inline_1": {"scene_hint": "...", "alt": "..."},
    "inline_2": {"scene_hint": "...", "alt": "..."},
    "inline_3": {"scene_hint": "...", "alt": "..."},
    "inline_4": {"scene_hint": "...", "alt": "..."},
    "inline_5": {"scene_hint": "...", "alt": "..."},
    "inline_6": {"scene_hint": "...", "alt": "..."},
    "inline_7": {"scene_hint": "...", "alt": "..."}
  }
}
```

Write ONLY valid JSON, no markdown fences.

# Description inputs B07

Read article.html opening + title-brief.json h1.

Output ONLY description-brief.json (valid JSON, no markdown).

H1: Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽

Dzen card teaser after Sol — Klyshin rhythm, NOT duplicate of H1/lead.
Tenant: Добрый дом, посуточная Тюмень.

Article hook: guest books 3 nights, sees "кухня есть" in listing, plans to cook. On arrival: one glass, two forks, worn pan, no oil/salt/sponge. Formal kitchen exists but unusable. ~2 400 ₽/day in cafés → 7 200 ₽ over 3 nights — unplanned burn.
Guest pain: "кухня есть" ≠ equipped to cook — ask inventory BEFORE payment, not at empty drawers.
Do NOT mention Шакин/Риэлтор. Do NOT price ladder as Добрый дом price.
HARD GATE: if description contains 7200 or any 3–5 digit sum, do NOT write «Добрый дом» inside description text (author_brand field only).
Use guest-burn sum as hook; close with action CTA without brand name.
Example OK: «Кухня есть» — а сковорода мёртвая. Три ночи кафе: 7 200 ₽. Спросите фото ящиков до перевода.
Example FAIL: any «Добрый дом» + digits in same description string.

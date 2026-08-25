# Scout rolling memory

**Обновляет:** `excalibur-blog-scout` после каждого прохода.

| Файл | Назначение |
|------|------------|
| `klyshin-topic-bank.md` | Человекочитаемый банк хуков + **P0 queue** (окна YEKT) |
| `klyshin-topic-bank.json` | Машиночитаемый банк + `p0_queue.slots` для Scout / gates |

**Алгоритм (канон):** Klyshin hook → Wordstat `top_requests` (Тюмень 55 + область 11176, compare RU 225) → **evaluate + rework for demand** (слабый объём → локализация/переформулировка до buyer P0; skip только после исчерпания rework). Логировать **original hook** + **final P0 phrase+volume**.

Wordstat — demand spine. Klyshin — angle/hook bank, не замена частот.

#!/usr/bin/env python3
"""Anti-clone + wound-family checks for dobry_dom_voice_reset_v1 editorial canon."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

EDITORIAL_CANON_ID = "dobry_dom_voice_reset_v1"
RECENT_LIVE_COUNT = 12

# Семейства «доплата у двери» — Scout не должен клонировать подряд.
DOOR_SURCHARGE_WOUND_RES: tuple[re.Pattern[str], str] = (
    (re.compile(r"у\s+двери", re.I), "door_beat"),
    (re.compile(r"доплат\w*\s+за\s+трет", re.I), "third_guest"),
    (re.compile(r"треть\w+\s+гост", re.I), "third_guest"),
    (re.compile(r"парковк", re.I), "parking"),
    (re.compile(r"шлагбаум", re.I), "parking"),
    (re.compile(r"собак|питомц|корги|лап", re.I), "pet"),
    (re.compile(r"обогревател|батаре", re.I), "heater"),
    (re.compile(r"чемодан", re.I), "bags"),
    (re.compile(r"кухн", re.I), "kitchen"),
)

BANNED_H1_SKELETON_RES = (
    re.compile(
        r"сняли\s+квартиру\s+посуточно\s*[\.\—]?\s*хотели",
        re.I,
    ),
    re.compile(r"хотели\s+.+\s+у\s+двери\s*:", re.I),
    re.compile(r"^сняли\s+квартиру\s+посуточно", re.I),
)

UDVERI_FORMULA_RE = re.compile(r"у\s+двери\s*[:—]", re.I)

FIXED_VERDICT_H2_RE = re.compile(
    r"^\s*мой\s+вывод\s+как\s+практик\w*\s*$",
    re.I,
)

H1_SHAPE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("quote_first", re.compile(r"^\s*[«\"]")),
    ("number_first", re.compile(r"^\s*[\d₽]")),
    ("dialogue", re.compile(r"[«\"].{4,}[»\"]")),
    ("host_wrote", re.compile(r"хозяин\s+(написал|сказал|ответил)", re.I)),
    ("scene", re.compile(r"^(в\s+чате|на\s+выезде|в\s+фильтре|в\s+карточке)", re.I)),
    ("fork", re.compile(r"\b(только|а\s+потом|не\s+значит|похоже,\s*да)\b", re.I)),
)


def _plain(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def first_n_words(text: str, n: int = 6) -> str:
    words = re.findall(r"[а-яёА-ЯЁ0-9«»]+", (text or "").casefold())
    return " ".join(words[:n])


def detect_h1_shape(h1: str) -> str:
    title = (h1 or "").strip()
    for name, rx in H1_SHAPE_PATTERNS:
        if rx.search(title):
            return name
    return "other"


def detect_wound_families(text: str) -> set[str]:
    low = (text or "").casefold()
    found: set[str] = set()
    for rx, family in DOOR_SURCHARGE_WOUND_RES:
        if rx.search(low):
            found.add(family)
    return found


def _parse_published_slugs(root: Path, limit: int = RECENT_LIVE_COUNT) -> list[str]:
    ledger = root / "shared/published-articles.md"
    if not ledger.is_file():
        return []
    slugs: list[str] = []
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if "| published |" not in line.lower():
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 5:
            continue
        slug_cell = parts[3]
        if slug_cell.startswith("/blog/"):
            slug = slug_cell.strip("/").replace("blog/", "").strip("/")
        else:
            slug = slug_cell
        if slug and slug not in slugs:
            slugs.append(slug)
    return slugs[-limit:]


def _load_recent_live(root: Path, limit: int = RECENT_LIVE_COUNT) -> list[dict[str, str]]:
    articles_root = root / "memory/blog/articles"
    rows: list[dict[str, str]] = []
    titles_path = root / "shared/published-titles.md"
    title_by_slug: dict[str, str] = {}
    if titles_path.is_file():
        for line in titles_path.read_text(encoding="utf-8").splitlines():
            if "| published |" not in line.lower():
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                title_by_slug[parts[2]] = parts[3]

    for slug in _parse_published_slugs(root, limit=limit):
        h1 = title_by_slug.get(slug, "")
        opening = ""
        for art_dir in articles_root.glob(f"*{slug}*"):
            art_html = art_dir / "article.html"
            if art_html.is_file():
                opening = _plain(art_html.read_text(encoding="utf-8"))[:400]
                meta = art_dir / "article.meta.json"
                if meta.is_file():
                    import json

                    try:
                        data = json.loads(meta.read_text(encoding="utf-8"))
                        h1 = str(data.get("h1") or data.get("title") or h1)
                    except json.JSONDecodeError:
                        pass
                break
        rows.append({"slug": slug, "h1": h1, "opening": opening})
    return rows


def check_banned_h1_skeleton(h1: str) -> list[str]:
    errors: list[str] = []
    for rx in BANNED_H1_SKELETON_RES:
        if rx.search(h1 or ""):
            errors.append(
                "h1: banned factory skeleton (Сняли квартиру посуточно / Хотели X / У двери:)"
            )
            break
    return errors


def check_posutochno_surface(h1: str, opening_plain: str = "") -> list[str]:
    blob = f"{h1} {opening_plain}".casefold()
    if "посуточн" in blob:
        return []
    return [
        "posutochno: word «посуточно» must appear in H1 or first sentence of body"
    ]


def check_anti_clone_h1(
    h1: str,
    *,
    root: Path,
    recent: list[dict[str, str]] | None = None,
) -> list[str]:
    errors: list[str] = []
    title = (h1 or "").strip()
    if not title:
        return errors
    corpus = recent if recent is not None else _load_recent_live(root)
    if not corpus:
        return errors

    new_open = first_n_words(title, 6)
    new_shape = detect_h1_shape(title)
    new_udveri = bool(UDVERI_FORMULA_RE.search(title))
    new_wounds = detect_wound_families(title)

    if corpus:
        last = corpus[-1]
        last_h1 = last.get("h1") or ""
        if last_h1 and detect_h1_shape(last_h1) == new_shape and new_shape != "other":
            errors.append(
                f"anti-clone: H1 shape «{new_shape}» repeats previous live post — rotate shape"
            )
        if new_udveri and UDVERI_FORMULA_RE.search(last_h1):
            errors.append(
                "anti-clone: «У двери:» formula twice in a row — pick another wound frame"
            )

    for row in corpus:
        prev_h1 = row.get("h1") or ""
        if not prev_h1:
            continue
        if first_n_words(prev_h1, 6) == new_open and new_open:
            errors.append(
                "anti-clone: same opening 6 words as a recent live H1 — rewrite hook"
            )
            break
        shared_wounds = new_wounds & detect_wound_families(prev_h1)
        if shared_wounds and "door_beat" in shared_wounds:
            errors.append(
                f"anti-clone: same door-surcharge wound family as recent live ({', '.join(sorted(shared_wounds))})"
            )
            break

    return errors


def check_anti_clone_opening(
    opening_plain: str,
    h1: str,
    *,
    root: Path,
    recent: list[dict[str, str]] | None = None,
) -> list[str]:
    errors: list[str] = []
    head = (opening_plain or "")[:400]
    if not head:
        return errors
    corpus = recent if recent is not None else _load_recent_live(root)
    new_sig = first_n_words(f"{h1} {head}", 12)
    for row in corpus:
        prev = f"{row.get('h1', '')} {row.get('opening', '')}"
        if not prev.strip():
            continue
        if first_n_words(prev, 12) == new_sig and new_sig:
            errors.append(
                "anti-clone: H1 + first ~400 chars match recent live skeleton — new scene required"
            )
            break
    return errors


def check_fixed_verdict_heading(html: str, *, label: str) -> list[str]:
    errors: list[str] = []
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>", html or "", flags=re.I | re.S):
        heading = _plain(match.group(1))
        if FIXED_VERDICT_H2_RE.match(heading):
            errors.append(
                f"{label}: banned fixed H2 «Мой вывод как практика» — write a fresh conclusion title"
            )
    return errors


def check_conclusion_present(html: str, *, label: str) -> list[str]:
    """One plain-language conclusion block (any H2 wording except the factory stamp)."""
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>", html or "", flags=re.I | re.S):
        heading = _plain(match.group(1))
        if FIXED_VERDICT_H2_RE.match(heading):
            continue
        if re.search(r"вывод|итог|короче|главное|если\s+коротко|на\s+практике", heading, re.I):
            return []
    return [
        f"{label}: missing one conclusion H2 (plain words; not the factory stamp)"
    ]


def check_lead_conclusion_sentence_repeat(html: str, *, label: str) -> list[str]:
    lead = _plain(" ".join(re.findall(r"<p[^>]*>(.*?)</p>", html or "", flags=re.I | re.S)[:2]))
    conclusion = ""
    h2_blocks = list(re.finditer(r"<h2[^>]*>(.*?)</h2>([\s\S]*?)(?=<h2|$)", html or "", flags=re.I))
    for match in reversed(h2_blocks):
        heading = _plain(match.group(1))
        if FIXED_VERDICT_H2_RE.match(heading):
            continue
        body = _plain(match.group(2))
        if body:
            conclusion = body
            break
    if not lead or not conclusion:
        return []
    lead_sents = [s.strip() for s in re.split(r"(?<=[.!?…])\s+", lead) if s.strip()]
    con_sents = [s.strip() for s in re.split(r"(?<=[.!?…])\s+", conclusion) if s.strip()]
    if not lead_sents or not con_sents:
        return []
    if lead_sents[0].casefold() == con_sents[0].casefold():
        return [
            f"{label}: lead and conclusion repeat the same first sentence — rewrite one"
        ]
    if lead_sents[0].casefold() in conclusion.casefold():
        return [
            f"{label}: conclusion repeats lead sentence verbatim — one moral in plain words"
        ]
    return []


def check_scout_wound_not_saturated(topic_text: str, *, root: Path) -> list[str]:
    """Scout handoff/topic must not clone door-surcharge family used in last 12 live posts."""
    errors: list[str] = []
    families = detect_wound_families(topic_text)
    if not families:
        return errors
    corpus = _load_recent_live(root)
    saturated: set[str] = set()
    for row in corpus:
        saturated |= detect_wound_families(row.get("h1") or "")
    overlap = families & saturated
    heavy = overlap & {"door_beat", "third_guest", "parking", "pet", "heater", "bags", "kitchen"}
    if len(heavy) >= 2:
        errors.append(
            "scout-wound: topic clones saturated door-surcharge families "
            f"({', '.join(sorted(heavy))}) — pick a fresh guest wound"
        )
    return errors


def gate_report_summary() -> dict[str, Any]:
    return {
        "editorial_canon": EDITORIAL_CANON_ID,
        "recent_live_count": RECENT_LIVE_COUNT,
        "h1_shapes": [name for name, _ in H1_SHAPE_PATTERNS],
    }

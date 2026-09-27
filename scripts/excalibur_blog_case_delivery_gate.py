#!/usr/bin/env python3
"""Case-delivery gate — two-beat H1 and stage checks (title, writer, later sol)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from excalibur_blog_link_verify import check_url_with_connection_reset_retry
from excalibur_blog_live_catalog import slug_from_blog_href
from excalibur_blog_site_base import normalize_public_base, resolve_public_base_from_env

HOW_TO_RES = (
    re.compile(r"^\s*\d+\s+вопрос", re.I),
    re.compile(r"\bполный\s+гайд\b", re.I),
    re.compile(r"\bтоп[-\s]?\d+\b", re.I),
    re.compile(r"\bлучш(ие|ий|их)\b", re.I),
    re.compile(r"\b20\d{2}\b"),
    re.compile(r":\s*\d+\s+вопрос", re.I),
    re.compile(r"^как\s+", re.I),
    re.compile(r"^что\s+делать\s+если\b", re.I),
)

LABEL_HEAD_RES = (
    re.compile(r"^проверка\s+", re.I),
    re.compile(r"^заселение\s*:", re.I),
    re.compile(r"^посуточная\s+аренда\s*:", re.I),
)

TWO_BEAT_RE = re.compile(
    r"(?<=[.!?…])\s+.+|(?<=—)\s*.+|(?<=-)\s*.+",
    re.UNICODE,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def published_h1s(article_dir: Path) -> list[str]:
    titles: list[str] = []
    for rel in ("published-titles-only.md",):
        p = article_dir / rel
        if not p.is_file():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if "| published" not in line.lower():
                continue
            parts = [c.strip() for c in line.split("|")]
            if len(parts) >= 4:
                titles.append(parts[3])
    return titles


def check_title_stage(article_dir: Path) -> dict[str, Any]:
    errors: list[str] = []
    brief_path = article_dir / "title-brief.json"
    data = load_json(brief_path)
    if not data:
        return {"status": "BLOCK", "stage": "title", "errors": ["title-brief.json missing or invalid JSON"]}

    h1 = str(data.get("h1") or data.get("title") or "").strip()
    if not h1:
        errors.append("h1/title empty")

    verdict = str(data.get("verdict") or "").strip().upper()
    if verdict != "PASS":
        errors.append(f"verdict must be PASS (got {verdict or 'empty'})")

    topic_id = str(data.get("topic_id") or data.get("brief_id") or "").strip()
    if topic_id and topic_id.upper() not in ("B03", "B03-POSUTOCHNO"):
        if not topic_id.upper().startswith("B03"):
            errors.append(f"topic_id mismatch: {topic_id}")

    if h1:
        n = len(h1)
        if n < 45 or n > 75:
            errors.append(f"h1 length {n} outside ~50–70 (soft 45–75)")

        if not TWO_BEAT_RE.search(h1) and "." not in h1 and "—" not in h1:
            errors.append("h1 must be two-beat case (period or em-dash between beats)")

        for rx in HOW_TO_RES:
            if rx.search(h1):
                errors.append(f"h1 looks how-to/SEO, not case: {rx.pattern[:40]}")
                break

        for rx in LABEL_HEAD_RES:
            if rx.search(h1):
                errors.append(f"h1 label-head pattern: {rx.pattern[:40]}")
                break

        if h1.isupper() or sum(1 for c in h1 if c.isupper()) > 8:
            errors.append("h1 CAPS wall")

        for prev in published_h1s(article_dir):
            if prev and prev.casefold() == h1.casefold():
                errors.append("h1 duplicates published-titles-only.md entry")

    stamp = article_dir / "derouter-opus-stamp-title.json"
    if not stamp.is_file():
        errors.append("derouter-opus-stamp-title.json missing (title must use Derouter)")

    status = "PASS" if not errors else "BLOCK"
    return {
        "status": status,
        "stage": "title",
        "h1": h1,
        "errors": errors,
        "article_dir": str(article_dir),
    }


class _AnchorExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for k, v in attrs:
            if k.lower() == "href" and v:
                self.hrefs.append(v.strip())


def strip_html(html: str) -> str:
    html = re.sub(r"(?is)<script.*?>.*?</script>", " ", html)
    html = re.sub(r"(?is)<style.*?>.*?</style>", " ", html)
    html = re.sub(r"(?is)<[^>]+>", " ", html)
    html = re.sub(r"\s+", " ", html)
    return html.strip()


def word_count_ru(html: str) -> int:
    text = strip_html(html)
    if not text:
        return 0
    return len(re.findall(r"[\w\u0400-\u04FF]+", text, flags=re.UNICODE))


WRITER_BANNED_SUBSTRINGS = (
    "+7 922 001 65 05",
    "922 001 65 05",
    "whatsapp",
    "t.me/klyshin",
    "klyshin_a",
)

WRITER_LEGAL_HOOK_RES = (
    re.compile(r"\bегрн\b", re.I),
    re.compile(r"\bнотариус", re.I),
    re.compile(r"\bв\s+суд\b", re.I),
    re.compile(r"\bя\s+адвокат\b", re.I),
)

HOST_LINE_RE = re.compile(
    r"я\s+хост\s+посуточной\s+в\s+тюмени\.?\s*это\s+[«\"]?\s*добрый\s+дом\s*[»\"]?",
    re.I | re.UNICODE,
)

KLYSHIN_REFUSAL_RE = re.compile(r"нет\.?\s*так\s+не\s+заселяем", re.I)

SECTION1_MONEY_RE = re.compile(r"(₽|\bруб\.?\b|\bрубл)", re.I)
SECTION1_TIME_RE = re.compile(r"\b\d{1,2}:\d{2}\b")


def _case_body_checks(
    html: str,
    article_dir: Path,
    root: Path,
    *,
    stage: str,
    forbid_h1: bool,
    require_h1: bool,
    stamp_name: str,
) -> dict[str, Any]:
    errors: list[str] = []
    if forbid_h1 and re.search(r"<h1\b", html, re.I):
        errors.append(f"{stage} article must not contain <h1> (WP title is separate)")
    if require_h1 and not re.search(r"<h1\b", html, re.I):
        errors.append(f"{stage} article must contain <h1>")

    wc = word_count_ru(html)
    if wc < 1100 or wc > 1800:
        errors.append(f"word count {wc} outside 1100–1800")

    stamp = article_dir / stamp_name
    if not stamp.is_file():
        errors.append(f"{stamp_name} missing (stage must use Derouter)")

    lower = html.casefold()
    for banned in WRITER_BANNED_SUBSTRINGS:
        if banned.casefold() in lower:
            errors.append(f"banned substring: {banned}")

    plain = strip_html(html)
    if not HOST_LINE_RE.search(plain):
        errors.append('missing host line «Я хост посуточной в Тюмени. Это «Добрый дом».»')

    # §1 = text before first <h2>
    h2_match = re.search(r"(?is)<h2\b", html)
    section1 = html[: h2_match.start()] if h2_match else html[:2000]
    s1_plain = strip_html(section1)
    if not SECTION1_TIME_RE.search(s1_plain):
        errors.append("§1 missing concrete time (HH:MM)")
    if not SECTION1_MONEY_RE.search(s1_plain):
        errors.append("§1 missing sum in ₽/руб")

    if not KLYSHIN_REFUSAL_RE.search(plain):
        errors.append('missing Klyshin refusal dialog «Нет. Так не заселяем.»')

    for rx in WRITER_LEGAL_HOOK_RES:
        if rx.search(plain):
            errors.append(f"legal hook pattern: {rx.pattern[:30]}")
            break

    if "комментар" in lower:
        errors.append("must not send readers to comments")

    if "наш вывод простой" not in lower:
        errors.append('missing ending lead «Наш вывод простой.»')

    idx = lower.find("наш вывод простой")
    tail = html[idx:] if idx >= 0 else html[-1500:]
    funnel_needles = (
        "t.me/dobriy_dom_72",
        "max.ru/id660300569233_biz",
        "booking",
        "dobriy_dom_tyumen",
        "tel:+79935748322",
    )
    tail_lower = tail.casefold()
    for needle in funnel_needles:
        if needle not in tail_lower and needle.replace("tel:", "") not in tail_lower:
            errors.append(f"final funnel block missing {needle}")

    if "+7 (993) 574-83-22" not in tail and "+79935748322" not in tail_lower:
        errors.append("final funnel missing display phone +7 (993) 574-83-22")

    # Mid-article Q → TG or MAX (before final third)
    mid_end = max(len(html) * 2 // 3, len(html) - 2000)
    mid = html[:mid_end]
    mid_lower = mid.casefold()
    has_mid_channel = "t.me/dobriy_dom_72" in mid_lower or "max.ru/id660300569233_biz" in mid_lower
    if "?" not in strip_html(mid) or not has_mid_channel:
        errors.append("mid-article question with answer via TG or MAX missing")

    parser = _AnchorExtractor()
    parser.feed(html)
    blog_slugs: set[str] = set()
    blog_hrefs: list[str] = []
    for href in parser.hrefs:
        if href.startswith("/blog/") or "/blog/" in href:
            slug = slug_from_blog_href(href)
            if slug:
                blog_slugs.add(slug)
                blog_hrefs.append(href)

    if len(blog_slugs) < 3:
        errors.append(f"need 3–4 unique /blog/ interlinks (got {len(blog_slugs)} slugs)")

    site_base = resolve_public_base_from_env()
    if not site_base:
        tenant = load_json(root / "shared/tenant-config.json") or {}
        urls = tenant.get("site_urls") if isinstance(tenant.get("site_urls"), dict) else {}
        site_base = normalize_public_base(
            urls.get("public_unicode")
            or (tenant.get("cta_channels") or {}).get("site")
        )
    user_agent = "ExcaliburBlogCaseDeliveryGate/1.0"
    for href in sorted(set(blog_hrefs)):
        if href.startswith("/"):
            if not site_base:
                errors.append("cannot verify interlink: public site base unknown")
                break
            url = site_base.rstrip("/") + href
        elif href.startswith("http"):
            url = href
        else:
            continue
        result = check_url_with_connection_reset_retry(url, 20.0, user_agent)
        if not result.get("ok"):
            code = result.get("status")
            errors.append(f"interlink not HTTP 200: {href} ({code})")

    status = "PASS" if not errors else "BLOCK"
    return {
        "status": status,
        "stage": stage,
        "word_count_estimate": wc,
        "blog_interlink_slugs": sorted(blog_slugs),
        "errors": errors,
        "article_dir": str(article_dir),
    }


def check_writer_stage(article_dir: Path, root: Path) -> dict[str, Any]:
    draft = article_dir / "drafts" / "writer.html"
    if not draft.is_file():
        return {
            "status": "BLOCK",
            "stage": "writer",
            "errors": ["drafts/writer.html missing"],
            "article_dir": str(article_dir),
        }
    html = draft.read_text(encoding="utf-8")
    return _case_body_checks(
        html,
        article_dir,
        root,
        stage="writer",
        forbid_h1=True,
        require_h1=False,
        stamp_name="derouter-opus-stamp-writer.json",
    )


def check_sol_stage(article_dir: Path, root: Path) -> dict[str, Any]:
    errors: list[str] = []
    final = article_dir / "article.html"
    variant = article_dir / "drafts" / "variant-a.html"
    if not final.is_file():
        return {
            "status": "BLOCK",
            "stage": "sol",
            "errors": ["article.html missing"],
            "article_dir": str(article_dir),
        }
    if not variant.is_file():
        errors.append("drafts/variant-a.html missing (copy of Sol final)")
    html = final.read_text(encoding="utf-8")
    result = _case_body_checks(
        html,
        article_dir,
        root,
        stage="sol",
        forbid_h1=True,
        require_h1=False,
        stamp_name="derouter-opus-stamp-sol.json",
    )
    if errors:
        result["errors"] = errors + result.get("errors", [])
        result["status"] = "BLOCK"
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Case delivery gate")
    parser.add_argument("--article-dir", required=True)
    parser.add_argument("--stage", required=True, choices=["title", "writer", "sol"])
    parser.add_argument("--json-out", help="Write gate result JSON next to article")
    args = parser.parse_args(argv)

    root = project_root()
    ad = Path(args.article_dir)
    if not ad.is_absolute():
        ad = root / ad

    if args.stage == "title":
        result = check_title_stage(ad)
    elif args.stage == "writer":
        result = check_writer_stage(ad, root)
    elif args.stage == "sol":
        result = check_sol_stage(ad, root)
    else:
        result = {"status": "BLOCK", "errors": [f"unknown stage {args.stage}"]}

    default_out = f"case-delivery-gate-{args.stage}.json"
    out_path = Path(args.json_out) if args.json_out else ad / default_out
    if not out_path.is_absolute():
        out_path = root / out_path
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

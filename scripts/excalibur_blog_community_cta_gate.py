#!/usr/bin/env python3
"""Hard gate: article CTA links from shared/tenant-config.json.

If cta_required is false and cta_links is empty → PASS (CTA optional).
If cta_required is true → every URL in cta_links must appear in article.html.
If cta_required is false but cta_links non-empty → require all listed URLs
(tenant asked for those links when present).
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse


def load_tenant(root: Path) -> dict:
    path = root / "shared/tenant-config.json"
    if not path.is_file():
        return {"cta_required": False, "cta_links": []}
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_phone_digits(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def url_patterns(url: str) -> re.Pattern[str]:
    """Build a loose href matcher for a concrete CTA URL."""
    url = (url or "").strip()
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    path = (parsed.path or "").rstrip("/")
    # Escape and allow optional trailing slash / quote boundary
    host_re = re.escape(host)
    path_re = re.escape(path) if path else ""
    if path_re:
        pat = rf"""https?://{host_re}{path_re}(?:/|\b|"|'|>|\?)"""
    else:
        pat = rf"""https?://{host_re}(?:/|\b|"|'|>|\?)"""
    return re.compile(pat, re.I)


from excalibur_blog_site_base import SITE_BASE_PLACEHOLDER


def check_tel_link(html: str, tel_url: str) -> bool:
    digits = normalize_phone_digits(tel_url.removeprefix("tel:"))
    if len(digits) < 10:
        return False
    tail = digits[-10:]
    if re.search(rf"tel:\+?{re.escape(digits)}", html or "", re.I):
        return True
    if re.search(rf"tel:\+?7{re.escape(tail)}", html or "", re.I):
        return True
    return tail in normalize_phone_digits(html or "")


def link_in_html(html: str, link: str) -> bool:
    link = (link or "").strip()
    if link.lower().startswith("tel:"):
        return check_tel_link(html, link)
    if url_patterns(link).search(html or ""):
        return True
    parsed = urlparse(link)
    path = parsed.path or "/"
    if not path.endswith("/") and path != "/":
        path_variants = [path, f"{path}/"]
    else:
        path_variants = [path]
    for p in path_variants:
        if f'href="{p}"' in (html or "") or f"href='{p}'" in (html or ""):
            return True
        placeholder_href = f'href="{SITE_BASE_PLACEHOLDER}{p}"'
        if placeholder_href in (html or ""):
            return True
        if p == "/":
            if f'href="{SITE_BASE_PLACEHOLDER}/"' in (html or ""):
                return True
    return False


def check_max_channel(html: str, max_cfg: str, phone: str) -> tuple[bool, str]:
    cfg = (max_cfg or "").strip()
    if not cfg:
        return True, ""
    if not cfg.startswith("phone:"):
        return True, ""
    if not re.search(r"\bMAX\b", html or "", re.I):
        return False, "missing MAX mention in CTA block (cta_channels.max=phone)"
    phone_digits = normalize_phone_digits(cfg.split(":", 1)[1] or phone)
    if phone_digits and not check_tel_link(html, f"tel:+{phone_digits.lstrip('0')}"):
        return False, "MAX block requires tenant phone (tel: or digits)"
    return True, ""


def check_funnel_hooks(html: str) -> list[str]:
    """Mid-body funnel: TG after checklist vibe; MAX/manager after brand block."""
    errors: list[str] = []
    body = html or ""
    lower = body.casefold()
    n = max(len(body), 1)
    tg = "t.me/dobriy_dom_72"
    tg_pos = lower.find(tg)
    max_pos = lower.find("max.ru/id660300569233_biz")
    mgr_pos = lower.find("t.me/dobriy_dom_tyumen")
    if tg_pos < 0:
        errors.append("funnel: missing Telegram channel https://t.me/Dobriy_dom_72 in body")
    elif tg_pos > int(n * 0.82):
        errors.append("funnel: Telegram channel link only at the end — move mid-article after checklist")
    if tg_pos >= 0:
        window = lower[max(0, tg_pos - 400) : tg_pos + 120]
        if not re.search(r"канал|полн|список", window):
            errors.append("funnel: TG hook should mention channel/full list near https://t.me/Dobriy_dom_72")
    brand_markers = ("добр", "у нас", "мы сдаём", "мы шлём", "мы отправ")
    brand_pos = -1
    for m in brand_markers:
        p = lower.find(m)
        if p >= 0:
            brand_pos = p if brand_pos < 0 else min(brand_pos, p)
    mm_pos = max_pos if max_pos >= 0 else mgr_pos
    if brand_pos >= 0 and mm_pos < 0:
        errors.append("funnel: after brand block need MAX or manager link in body")
    if mm_pos >= 0:
        window = lower[max(0, mm_pos - 500) : mm_pos + 200]
        if not re.search(r"инструк|засел|до заезд|до засел", window):
            errors.append("funnel: MAX/manager hook should mention instruction before check-in")
    banned = (
        ("егрн", "banned topic: ЕГРН"),
        ("нотариус", "banned topic: нотариус"),
        (r"\bсуд\b", "banned topic: суд"),
        ("я адвокат", "banned phrase: я адвокат"),
        ("мы лучшие", "banned phrase: мы лучшие"),
        ("бизнес-класс", "banned phrase: бизнес-класс"),
    )
    for pat, msg in banned:
        if re.search(pat, lower):
            # alt-тексты картинок не считаем телом статьи
            prose = re.sub(r"<img[^>]*alt=\"[^\"]*\"[^>]*>", "", body, flags=re.I)
            prose_lower = prose.casefold()
            if re.search(pat, prose_lower):
                errors.append(msg)
    return errors


def check_html(
    html: str,
    links: list[str],
    *,
    required: bool,
    max_cfg: str = "",
    phone: str = "",
) -> tuple[list[str], dict[str, bool]]:
    errors: list[str] = []
    present: dict[str, bool] = {}
    if not links:
        if required:
            errors.append("cta_required=true but tenant-config.cta_links is empty")
        return errors, present
    for link in links:
        ok = link_in_html(html, link)
        present[link] = ok
        if not ok:
            errors.append(f"missing required CTA href {link}")
    max_ok, max_err = check_max_channel(html, max_cfg, phone)
    present["cta_channels.max"] = max_ok
    if not max_ok and max_err:
        errors.append(max_err)
    return errors, present


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--root", default=".")
    ap.add_argument("-o", "--output", default="community-cta-gate.json")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = (root / article_dir).resolve()

    tenant = load_tenant(root)
    links = [str(x).strip() for x in (tenant.get("cta_links") or []) if str(x).strip()]
    cta_required = bool(tenant.get("cta_required"))
    channels = tenant.get("cta_channels") or {}
    max_cfg = str(channels.get("max") or "").strip()
    phone = str(channels.get("phone") or "").strip()

    html_path = article_dir / "article.html"
    errors: list[str] = []
    html = ""
    if not html_path.is_file():
        errors.append("article.html missing")
    else:
        html = html_path.read_text(encoding="utf-8")
        # Optional CTA: empty links + not required → PASS
        if not links and not cta_required:
            present = {}
        else:
            link_errors, present = check_html(
                html,
                links,
                required=cta_required,
                max_cfg=max_cfg,
                phone=phone,
            )
            errors.extend(link_errors)
            errors.extend(check_funnel_hooks(html))
    if not links and not cta_required:
        present = {}

    status = "PASS" if not errors else "FAIL"
    report = {
        "status": status,
        "article_dir": str(article_dir.relative_to(root)).replace("\\", "/"),
        "cta_required": cta_required,
        "required": links,
        "present": present,
        "funnel_errors": [e for e in errors if e.startswith("funnel:") or e.startswith("banned")],
        "errors": errors,
    }
    out_name = Path(args.output).name
    out_path = article_dir / out_name
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

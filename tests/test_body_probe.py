"""Regression: body_probe must unescape HTML entities before truncation."""
from __future__ import annotations

import html
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_wp_publish import build_body_probe  # noqa: E402

B10_OPENING = (
    "<p>«Всё включено, доплат не будет», — написал хозяин в чате. "
    "Вы читаете это как нормальную финальную цену, переводите 4&nbsp;800 ₽ "
    "за две ночи — по 2&nbsp;400 ₽ за ночь — и закрываете вопрос. "
    "Потом собираете чемодан, садитесь в такси, смотрите на незнакомый "
    "вечерний город за окном. И именно тогда приходит новое сообщение: "
    "финальная уборка, коммуналка, сервисный сбор, полотенца. "
    "До заселения нужно доплатить ещё 2&nbsp;400 ₽.</p>"
)


class BodyProbeTests(unittest.TestCase):
    def test_unescapes_before_truncate(self) -> None:
        probe = build_body_probe(B10_OPENING)
        self.assertNotIn("&nbsp", probe)
        self.assertNotIn("&nbs", probe)
        self.assertIn("4 800", probe)

    def test_probe_found_in_live_plain_text(self) -> None:
        probe = build_body_probe(B10_OPENING)
        live_html = f"<html><body><div id='article-content'>{B10_OPENING}</div></body></html>"
        plain = html.unescape(re.sub(r"<[^>]+>", " ", live_html))
        plain = re.sub(r"\s+", " ", plain)
        self.assertIn(probe, plain)

    def test_truncated_mid_entity_without_unescape_would_fail(self) -> None:
        """Document the B10 failure mode: slice before unescape breaks matching."""
        first = re.search(r"<p\b[^>]*>(.*?)</p>", B10_OPENING, flags=re.I | re.S)
        assert first
        bad = re.sub(r"<[^>]+>", " ", first.group(1))
        bad = re.sub(r"\s+", " ", bad).strip()[:120]
        self.assertIn("&", bad)
        live_html = f"<html><body><div id='article-content'>{B10_OPENING}</div></body></html>"
        plain = html.unescape(re.sub(r"<[^>]+>", " ", live_html))
        plain = re.sub(r"\s+", " ", plain)
        self.assertNotIn(bad, plain)


if __name__ == "__main__":
    unittest.main()

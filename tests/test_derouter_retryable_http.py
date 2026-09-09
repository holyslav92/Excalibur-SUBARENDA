"""Derouter HTTP retry policy — overload 529 must retry, not instant BLOCKER."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_derouter_opus_chat import is_retryable_http


class DerouterRetryableHttpTest(unittest.TestCase):
    def test_529_is_retryable(self) -> None:
        self.assertTrue(is_retryable_http(529))

    def test_502_still_retryable(self) -> None:
        self.assertTrue(is_retryable_http(502))

    def test_400_not_retryable(self) -> None:
        self.assertFalse(is_retryable_http(400))


if __name__ == "__main__":
    unittest.main()

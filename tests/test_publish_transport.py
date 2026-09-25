"""Tests for FTP/SFTP publish transport selection."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_remote_transport import (  # noqa: E402
    remote_path,
    resolve_publish_transport,
    upload_text_file,
)
from excalibur_blog_wp_publish import load_env, publish_env_check_report  # noqa: E402


class PublishTransportTest(unittest.TestCase):
    def test_resolve_ftp_by_port(self) -> None:
        env = {"FTP_PORT": "21"}
        self.assertEqual(resolve_publish_transport(env), "ftp")

    def test_resolve_sftp_default(self) -> None:
        env = {"FTP_PORT": "22"}
        self.assertEqual(resolve_publish_transport(env), "sftp")

    def test_resolve_ftp_explicit(self) -> None:
        env = {"FTP_TRANSPORT": "ftp", "FTP_PORT": "22"}
        self.assertEqual(resolve_publish_transport(env), "ftp")

    def test_remote_path_with_root(self) -> None:
        env = {"FTP_ROOT": "sublease/public_html"}
        self.assertEqual(
            remote_path(env, "excalibur-blog-publish-once.php"),
            "sublease/public_html/excalibur-blog-publish-once.php",
        )

    def test_env_check_report_ftp_mode(self) -> None:
        env = {
            "FTP_HOST": "188.225.40.162",
            "FTP_USER": "ca21576_svyat",
            "FTP_PASS": "secret",
            "FTP_PORT": "21",
            "FTP_TRANSPORT": "ftp",
            "FTP_ROOT": "sublease/public_html",
            "PUBLIC_SITE_URL": "https://example.com",
            "EXCALIBUR_BLOG_ALLOW_PUBLISH": "no",
        }
        report = publish_env_check_report(env)
        transport = report["transport"]
        assert isinstance(transport, dict)
        self.assertEqual(transport["mode"], "ftp")
        self.assertFalse(report["allow_publish"])
        self.assertEqual(transport["port"], "21")
        self.assertEqual(transport["pasv_rewrite_ip"], "188.225.40.162")

    @patch("excalibur_blog_remote_transport._upload_text_ftp")
    def test_upload_dispatches_ftp(self, mock_ftp: MagicMock) -> None:
        mock_ftp.return_value = "sublease/public_html/test.php"
        env = {"FTP_TRANSPORT": "ftp", "FTP_PORT": "21"}
        path = upload_text_file(env, "test.php", b"<?php")
        self.assertEqual(path, "sublease/public_html/test.php")
        mock_ftp.assert_called_once()


if __name__ == "__main__":
    unittest.main()

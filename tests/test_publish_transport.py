"""Tests for FTP remote transport helpers."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_remote_transport import (  # noqa: E402
    ftp_creds,
    transport_mode,
    upload_bytes,
)
from excalibur_blog_wp_publish import publish_env_check_report  # noqa: E402


class PublishTransportTest(unittest.TestCase):
    def test_transport_mode_ftp_explicit(self) -> None:
        env = {"FTP_TRANSPORT": "ftp", "FTP_PORT": "22"}
        self.assertEqual(transport_mode(env), "ftp")

    def test_transport_mode_sftp_default(self) -> None:
        env = {"FTP_PORT": "22"}
        self.assertEqual(transport_mode(env), "sftp")

    def test_ftp_creds_from_env(self) -> None:
        env = {
            "FTP_HOST": "[REDACTED]",
            "FTP_USER": "ca21576_svyat",
            "FTP_PASS": "secret",
            "FTP_PORT": "21",
        }
        host, port, user, password = ftp_creds(env)
        self.assertEqual(host, "[REDACTED]")
        self.assertEqual(port, 21)
        self.assertEqual(user, "ca21576_svyat")
        self.assertEqual(password, "secret")

    def test_env_check_report_ftp_mode(self) -> None:
        env = {
            "FTP_HOST": "[REDACTED]",
            "FTP_USER": "ca21576_svyat",
            "FTP_PASS": "secret",
            "FTP_PORT": "21",
            "FTP_TRANSPORT": "ftp",
            "FTP_ROOT": "[REDACTED]",
            "PUBLIC_SITE_URL": "https://example.com",
            "EXCALIBUR_BLOG_ALLOW_PUBLISH": "no",
        }
        report = publish_env_check_report(env)
        transport = report["transport"]
        self.assertIsInstance(transport, dict)
        self.assertEqual(transport["mode"], "ftp")
        self.assertFalse(report["allow_publish"])
        self.assertEqual(transport["root"], "configured-non-dot")

    @patch("excalibur_blog_remote_transport.connect_ftp")
    def test_upload_bytes_uses_ftp_stor(self, mock_connect: MagicMock) -> None:
        ftp = MagicMock()
        ftp.pwd.return_value = "/login"
        mock_connect.return_value = ftp
        env = {"FTP_TRANSPORT": "ftp", "FTP_PORT": "21", "FTP_ROOT": "[REDACTED]"}
        path = upload_bytes(env, "test.php", b"<?php")
        self.assertEqual(path, "test.php")
        ftp.storbinary.assert_called_once()


if __name__ == "__main__":
    unittest.main()

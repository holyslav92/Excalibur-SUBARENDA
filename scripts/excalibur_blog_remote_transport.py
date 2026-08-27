#!/usr/bin/env python3
"""FTP remote transport for Excalibur BLOG publish (Timeweb PASV NAT fix)."""

from __future__ import annotations

import io
import os
import socket
import time
from ftplib import FTP, error_perm
from typing import Any

DEFAULT_FTP_TIMEOUT = 90
PASV_REWRITE_IP = "188.225.40.162"
PASV_ALLOWED_HOSTS = frozenset({"vh368.timeweb.ru", PASV_REWRITE_IP})
WP_ROOT_CANDIDATES = (
    "sublease/public_html",
    "public_html",
    ".",
    "public_html/sublease",
)


class TimewebPasvFTP(FTP):
    """FTP client with Timeweb PASV public-IP rewrite."""

    def __init__(
        self,
        host: str = "",
        user: str = "",
        passwd: str = "",
        acct: str = "",
        *,
        timeout: int = DEFAULT_FTP_TIMEOUT,
        pasv_rewrite_ip: str = PASV_REWRITE_IP,
        source_address: tuple[str, int] | None = None,
    ) -> None:
        super().__init__(host=host, user=user, passwd=passwd, acct=acct, timeout=timeout)
        self.pasv_rewrite_ip = pasv_rewrite_ip
        if source_address is not None:
            self.source_address = source_address

    def makepasv(self) -> tuple[str, int]:
        host, port = super().makepasv()
        host_norm = (host or "").strip().lower()
        allowed = {h.lower() for h in PASV_ALLOWED_HOSTS}
        if host_norm not in allowed:
            return self.pasv_rewrite_ip, port
        return host, port


def transport_mode(env: dict[str, str]) -> str:
    mode = (env.get("FTP_TRANSPORT") or "sftp").strip().lower()
    return "ftp" if mode == "ftp" else "sftp"


def ftp_creds(env: dict[str, str]) -> tuple[str, int, str, str]:
    host = (env.get("FTP_HOST") or env.get("SSH_HOST") or "").strip()
    port = int((env.get("FTP_PORT") or "21").strip() or "21")
    user = (env.get("FTP_USER") or env.get("SSH_USER") or "").strip()
    password = (
        env.get("FTP_PASS")
        or env.get("FTP_PASSWORD")
        or env.get("SSH_PASS")
        or env.get("SSH_PASSWORD")
        or ""
    )
    return host, port, user, password


def _ftp_timeout_from_env(env: dict[str, str] | None = None) -> int:
    raw = ""
    if env:
        raw = (env.get("FTP_TIMEOUT") or os.environ.get("FTP_TIMEOUT") or "").strip()
    if not raw:
        raw = os.environ.get("FTP_TIMEOUT", "").strip()
    try:
        value = int(raw)
        return max(30, min(value, 600))
    except (TypeError, ValueError):
        return DEFAULT_FTP_TIMEOUT


def connect_ftp(
    env: dict[str, str],
    *,
    timeout: int | None = None,
) -> TimewebPasvFTP:
    host, port, user, password = ftp_creds(env)
    if not host or not user or not password:
        raise RuntimeError("FTP credentials missing (FTP_HOST/FTP_USER/FTP_PASS)")
    effective_timeout = timeout if timeout is not None else _ftp_timeout_from_env(env)
    ftp = TimewebPasvFTP(timeout=effective_timeout)
    ftp.connect(host, port, timeout=effective_timeout)
    ftp.login(user, password)
    ftp.set_pasv(True)
    return ftp


def _ftp_file_exists(ftp: FTP, name: str) -> bool:
    try:
        ftp.size(name)
        return True
    except error_perm:
        pass
    try:
        names = {item.split("/")[-1] for item in ftp.nlst()}
        return name in names
    except error_perm:
        return False


def find_wp_root(
    env: dict[str, str],
    *,
    candidates: tuple[str, ...] = WP_ROOT_CANDIDATES,
    timeout: int = DEFAULT_FTP_TIMEOUT,
) -> tuple[str, dict[str, Any]]:
    """Return FTP cwd root containing wp-load.php and probe log."""
    log: dict[str, Any] = {"candidates": [], "wp_load_found": False, "selected_root": ""}
    ftp = connect_ftp(env, timeout=timeout)
    try:
        login_cwd = ftp.pwd()
        log["login_cwd"] = login_cwd
        configured = (env.get("FTP_ROOT") or env.get("SSH_ROOT") or "").strip()
        ordered = []
        if configured and configured not in ordered:
            ordered.append(configured)
        for item in candidates:
            if item not in ordered:
                ordered.append(item)
        for root in ordered:
            entry: dict[str, Any] = {"root": root, "wp_load": False, "error": ""}
            try:
                if root in {".", "./"}:
                    ftp.cwd(login_cwd)
                else:
                    ftp.cwd(login_cwd)
                    for part in root.split("/"):
                        if part and part != ".":
                            ftp.cwd(part)
                entry["cwd"] = ftp.pwd()
                entry["wp_load"] = _ftp_file_exists(ftp, "wp-load.php")
                log["candidates"].append(entry)
                if entry["wp_load"]:
                    log["wp_load_found"] = True
                    log["selected_root"] = root
                    return root, log
            except (error_perm, OSError, socket.timeout) as exc:
                entry["error"] = f"{type(exc).__name__}: {exc}"
                log["candidates"].append(entry)
        return "", log
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()


def _ftp_cwd_root(ftp: FTP, root: str, login_cwd: str) -> None:
    ftp.cwd(login_cwd)
    if root in {".", "./", ""}:
        return
    for part in root.split("/"):
        if part and part != ".":
            ftp.cwd(part)


def _ftp_stor_with_retry(
    ftp: FTP,
    remote_name: str,
    data: bytes,
    *,
    attempts: int = 8,
    retry_pause_s: float = 2.0,
) -> None:
    """Upload via STOR with passive-first then active fallback (Timeweb PASV can flake)."""
    last_exc: Exception | None = None
    for pasv in (True, False):
        try:
            ftp.set_pasv(pasv)
        except Exception:
            continue
        mode_label = "PASV" if pasv else "ACTIVE"
        for attempt in range(1, attempts + 1):
            try:
                ftp.voidcmd("TYPE I")
                bio = io.BytesIO(data)
                ftp.storbinary(f"STOR {remote_name}", bio)
                if not pasv:
                    print(f"FTP upload used ACTIVE mode after PASV failure", file=__import__("sys").stderr)
                return
            except (TimeoutError, OSError, error_perm) as exc:
                last_exc = exc
                if attempt >= attempts:
                    break
                time.sleep(retry_pause_s)
    assert last_exc is not None
    raise last_exc


def upload_bytes(
    env: dict[str, str],
    remote_name: str,
    data: bytes,
    *,
    root: str | None = None,
    timeout: int | None = None,
) -> str:
    root = (root or env.get("FTP_ROOT") or env.get("SSH_ROOT") or ".").strip() or "."
    effective_timeout = timeout if timeout is not None else _ftp_timeout_from_env(env)
    ftp = connect_ftp(env, timeout=effective_timeout)
    try:
        login_cwd = ftp.pwd()
        _ftp_cwd_root(ftp, root, login_cwd)
        remote_path = remote_name
        _ftp_stor_with_retry(ftp, remote_name, data)
        print(f"FTP upload OK: {root}/{remote_name} ({len(data)} bytes)")
        return remote_path
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()


def delete_remote_file(
    env: dict[str, str],
    remote_name: str,
    *,
    root: str | None = None,
    timeout: int = DEFAULT_FTP_TIMEOUT,
) -> None:
    root = (root or env.get("FTP_ROOT") or env.get("SSH_ROOT") or ".").strip() or "."
    ftp = connect_ftp(env, timeout=timeout)
    try:
        login_cwd = ftp.pwd()
        _ftp_cwd_root(ftp, root, login_cwd)
        try:
            ftp.delete(remote_name)
        except error_perm:
            pass
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()


def cli_find_wp_root() -> int:
    import json

    from excalibur_blog_wp_publish import load_env, project_root

    env = load_env(project_root())
    root, log = find_wp_root(env)
    print(json.dumps({"selected_root": root, **log}, ensure_ascii=False, indent=2))
    return 0 if root else 1


if __name__ == "__main__":
    raise SystemExit(cli_find_wp_root())

#!/usr/bin/env python3
"""FTP/SFTP remote transport for Excalibur BLOG publish (Timeweb PASV NAT fix)."""

from __future__ import annotations

import io
import os
import socket
import sys
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


def normalize_remote_root_value(value: str) -> str:
    """Empty or ``/`` → ``.`` (login cwd, usually public_html with wp-load.php)."""
    raw = (value or "").strip()
    if not raw or raw in {"/", "./"}:
        return "."
    return raw.strip("/")


def configured_remote_root(env: dict[str, str]) -> str:
    return normalize_remote_root_value(
        env.get("SSH_ROOT") or env.get("FTP_ROOT") or env.get("FTP_PATH") or ""
    )


def remote_root_label(env: dict[str, str]) -> str:
    root = configured_remote_root(env)
    if root in {".", "./"}:
        return "dot"
    return "configured-non-dot"


def remote_root_candidates(env: dict[str, str]) -> list[str]:
    root = configured_remote_root(env)
    if root and root not in {".", "./"}:
        return [root, "."]
    return ["."]


def remote_path(env: dict[str, str], remote: str, root_override: str | None = None) -> str:
    root = (
        configured_remote_root(env)
        if root_override is None
        else normalize_remote_root_value(root_override)
    )
    name = remote.lstrip("/")
    if not root or root in {".", "./"}:
        return name
    return root.rstrip("/") + "/" + name


def resolve_publish_transport(env: dict[str, str]) -> str:
    """Return ``ftp`` or ``sftp`` from env (FTP_PORT=21 → ftp; FTP_TRANSPORT=ftp overrides)."""
    explicit = (env.get("FTP_TRANSPORT") or env.get("PUBLISH_TRANSPORT") or "").strip().lower()
    if explicit in {"ftp", "ftps"}:
        return "ftp"
    if explicit in {"sftp", "ssh"}:
        return "sftp"
    port_raw = (env.get("FTP_PORT") or env.get("SSH_PORT") or "").strip()
    if port_raw == "21":
        return "ftp"
    if port_raw == "22":
        return "sftp"
    return "sftp"


def transport_mode(env: dict[str, str]) -> str:
    return resolve_publish_transport(env)


def is_missing_remote_path_error(exc: BaseException) -> bool:
    errno_value = getattr(exc, "errno", None)
    if errno_value == 2:
        return True
    text = str(exc).lower()
    return (
        "no such file" in text
        or "enoent" in text
        or "can't change directory" in text
        or "550" in text
    )


def transport_note(env: dict[str, str]) -> str:
    mode = resolve_publish_transport(env)
    if mode == "ftp":
        return (
            "FTP passive upload (FTP_PORT=21 or FTP_TRANSPORT=ftp). "
            "FTP_ROOT is relative to FTP login cwd."
        )
    return (
        "SFTP/SSH upload (default). FTP_* names are aliases for the same SFTP account "
        "unless FTP_PORT=21 or FTP_TRANSPORT=ftp."
    )


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


def connect_ftp(
    env: dict[str, str],
    *,
    timeout: int = DEFAULT_FTP_TIMEOUT,
) -> TimewebPasvFTP:
    host, port, user, password = ftp_creds(env)
    if not host or not user or not password:
        raise RuntimeError("FTP credentials missing (FTP_HOST/FTP_USER/FTP_PASS)")
    ftp = TimewebPasvFTP(timeout=timeout)
    ftp.connect(host, port, timeout=timeout)
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


def upload_text_file(env: dict[str, str], remote: str, data: bytes) -> str:
    """Upload a small UTF-8 text artifact to the WP site root."""
    if resolve_publish_transport(env) == "ftp":
        return _upload_text_ftp(env, remote, data)
    return _upload_text_sftp(env, remote, data)


def _upload_text_sftp(env: dict[str, str], remote: str, data: bytes) -> str:
    import paramiko

    host, port, user, password = ftp_creds(env)
    if resolve_publish_transport(env) != "ftp":
        port = int((env.get("SSH_PORT") or env.get("FTP_PORT") or "22").strip() or "22")
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        candidates = remote_root_candidates(env)
        for index, root_candidate in enumerate(candidates):
            remote_target = remote_path(env, remote, root_candidate)
            try:
                with sftp.open(remote_target, "w") as handle:
                    handle.write(data.decode("utf-8"))
                if index > 0:
                    print(
                        "WARN SFTP root fallback: configured remote root was not found; "
                        "used '.' for bootstrap. Update SSH_ROOT/FTP_ROOT to '.' in Cloud Secrets "
                        "if this is the intended SFTP login cwd.",
                        file=sys.stderr,
                    )
                print(f"SFTP upload OK: {remote_target} ({len(data)} bytes)")
                return remote_target
            except OSError as exc:
                if index < len(candidates) - 1 and is_missing_remote_path_error(exc):
                    print(
                        "WARN SFTP upload: configured remote root returned ENOENT; retrying bootstrap at '.'.",
                        file=sys.stderr,
                    )
                    continue
                raise
    finally:
        sftp.close()
        transport.close()
    raise RuntimeError("SFTP upload did not complete")


def _upload_text_ftp(env: dict[str, str], remote: str, data: bytes) -> str:
    filename = remote.split("/")[-1]
    candidates = remote_root_candidates(env)
    last_error: Exception | None = None
    for index, root_candidate in enumerate(candidates):
        env_copy = dict(env)
        env_copy["FTP_ROOT"] = root_candidate
        try:
            selected_root, _probe = find_wp_root(env_copy)
            root = selected_root or root_candidate
            env_copy["FTP_ROOT"] = root
            env_copy["SSH_ROOT"] = root
            upload_bytes(env_copy, filename, data, root=root)
            remote_target = remote_path(env_copy, remote, root)
            if index > 0 and not selected_root:
                print(
                    "WARN FTP root fallback: configured FTP_ROOT was not found; "
                    "used login cwd ('.'). Update FTP_ROOT if needed.",
                    file=sys.stderr,
                )
            return remote_target
        except (error_perm, OSError, TimeoutError, socket.timeout) as exc:
            last_error = exc
            if index < len(candidates) - 1 and is_missing_remote_path_error(exc):
                print(
                    "WARN FTP upload: configured FTP_ROOT failed; retrying at login cwd.",
                    file=sys.stderr,
                )
                continue
            raise
    raise RuntimeError(f"FTP upload did not complete: {last_error}")


def _ftp_stor_with_retry(
    ftp: FTP,
    remote_name: str,
    data: bytes,
    *,
    attempts: int = 8,
    retry_pause_s: float = 2.0,
) -> None:
    """Upload via passive STOR with short retries (Timeweb PASV ports can be flaky)."""
    last_exc: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            ftp.voidcmd("TYPE I")
            bio = io.BytesIO(data)
            ftp.storbinary(f"STOR {remote_name}", bio)
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
    timeout: int = DEFAULT_FTP_TIMEOUT,
) -> str:
    root = (root or env.get("FTP_ROOT") or env.get("SSH_ROOT") or ".").strip() or "."
    ftp = connect_ftp(env, timeout=timeout)
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

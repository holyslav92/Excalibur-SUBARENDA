#!/usr/bin/env python3
"""Удалённая загрузка bootstrap-файлов: SFTP (по умолчанию) или FTP (passive, port 21)."""

from __future__ import annotations

import sys
from io import BytesIO


def normalize_remote_root_value(value: str) -> str:
    """Пустой или ``/`` → ``.`` (login cwd, обычно public_html с wp-load.php)."""
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
    root = configured_remote_root(env) if root_override is None else normalize_remote_root_value(root_override)
    name = remote.lstrip("/")
    if not root or root in {".", "./"}:
        return name
    return root.rstrip("/") + "/" + name


def resolve_publish_transport(env: dict[str, str]) -> str:
    """Вернуть ``ftp`` или ``sftp`` по env (не ломает SFTP для других тенантов)."""
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


def remote_creds(env: dict[str, str]) -> tuple[str, int, str, str]:
    host = env.get("SSH_HOST") or env.get("FTP_HOST") or ""
    user = env.get("SSH_USER") or env.get("FTP_USER") or ""
    password = (
        env.get("SSH_PASS")
        or env.get("FTP_PASS")
        or env.get("SSH_PASSWORD")
        or env.get("FTP_PASSWORD")
        or ""
    )
    transport = resolve_publish_transport(env)
    if transport == "ftp":
        port = int(env.get("FTP_PORT") or "21")
    else:
        port = int(env.get("SSH_PORT") or env.get("FTP_PORT") or "22")
    return host, port, user, password


def is_missing_remote_path_error(exc: BaseException) -> bool:
    errno_value = getattr(exc, "errno", None)
    if errno_value == 2:
        return True
    text = str(exc).lower()
    return "no such file" in text or "enoent" in text or "can't change directory" in text or "550" in text


def _ftp_cwd_segments(ftp: object, root: str) -> None:
    if not root or root in {".", "./"}:
        return
    for segment in root.split("/"):
        if not segment or segment == ".":
            continue
        ftp.cwd(segment)  # type: ignore[attr-defined]


def upload_text_file(env: dict[str, str], remote: str, data: bytes) -> str:
    transport = resolve_publish_transport(env)
    if transport == "ftp":
        return _upload_text_ftp(env, remote, data)
    return _upload_text_sftp(env, remote, data)


def delete_remote_file(env: dict[str, str], remote: str, remote_path_value: str | None = None) -> None:
    transport = resolve_publish_transport(env)
    if transport == "ftp":
        _delete_remote_ftp(env, remote, remote_path_value)
    else:
        _delete_remote_sftp(env, remote, remote_path_value)


def _upload_text_sftp(env: dict[str, str], remote: str, data: bytes) -> str:
    import paramiko

    host, port, user, password = remote_creds(env)
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
                        "if this is the intended login cwd.",
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


def _delete_remote_sftp(env: dict[str, str], remote: str, remote_path_value: str | None = None) -> None:
    import paramiko

    host, port, user, password = remote_creds(env)
    remote_target = remote_path_value or remote_path(env, remote)
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        sftp.remove(remote_target)
    except OSError:
        pass
    finally:
        sftp.close()
        transport.close()


def _upload_text_ftp(env: dict[str, str], remote: str, data: bytes) -> str:
    import ftplib

    host, port, user, password = remote_creds(env)
    filename = remote.split("/")[-1]
    candidates = remote_root_candidates(env)
    last_error: Exception | None = None
    for index, root_candidate in enumerate(candidates):
        ftp = ftplib.FTP()
        try:
            ftp.connect(host, port, timeout=90)
            ftp.login(user, password)
            ftp.set_pasv(True)
            _ftp_cwd_segments(ftp, root_candidate)
            ftp.storbinary(f"STOR {filename}", BytesIO(data))
            remote_target = remote_path(env, remote, root_candidate)
            if index > 0:
                print(
                    "WARN FTP root fallback: configured FTP_ROOT was not found; "
                    "used login cwd ('.'). Update FTP_ROOT if needed.",
                    file=sys.stderr,
                )
            print(f"FTP upload OK: {remote_target} ({len(data)} bytes)")
            return remote_target
        except ftplib.error_perm as exc:
            last_error = exc
            if index < len(candidates) - 1 and is_missing_remote_path_error(exc):
                print(
                    "WARN FTP upload: configured FTP_ROOT failed; retrying at login cwd.",
                    file=sys.stderr,
                )
                continue
            raise
        finally:
            try:
                ftp.quit()
            except Exception:  # noqa: BLE001
                try:
                    ftp.close()
                except Exception:  # noqa: BLE001
                    pass
    raise RuntimeError(f"FTP upload did not complete: {last_error}")


def _delete_remote_ftp(env: dict[str, str], remote: str, remote_path_value: str | None = None) -> None:
    import ftplib

    host, port, user, password = remote_creds(env)
    remote_target = remote_path_value or remote_path(env, remote)
    root = configured_remote_root(env)
    filename = remote.split("/")[-1]
    ftp = ftplib.FTP()
    ftp.connect(host, port, timeout=90)
    ftp.login(user, password)
    ftp.set_pasv(True)
    try:
        _ftp_cwd_segments(ftp, root)
        try:
            ftp.delete(filename)
        except ftplib.error_perm:
            pass
    finally:
        try:
            ftp.quit()
        except Exception:  # noqa: BLE001
            ftp.close()


def transport_note(env: dict[str, str]) -> str:
    mode = resolve_publish_transport(env)
    if mode == "ftp":
        return (
            "FTP passive upload (FTP_PORT=21 or FTP_TRANSPORT=ftp). "
            "FTP_ROOT is relative to FTP login cwd (e.g. sublease/public_html)."
        )
    return (
        "SFTP/SSH upload (default). FTP_* names are aliases for the same SFTP account "
        "unless FTP_PORT=21 or FTP_TRANSPORT=ftp."
    )

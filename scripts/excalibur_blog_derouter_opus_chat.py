#!/usr/bin/env python3
"""Derouter REST chat/completions — двухуровневый «мозг» текстовых ролей фабрики.

POST https://api.derouter.ai/openai/v1/chat/completions
Fallback: https://api.apikey.cloud/openai/v1/chat/completions

Auth: DEROUTER_API_KEY (Cloud Secrets only).
Модели по роли из shared/tenant-config.json → writing_model (powerful vs utility).
Forbidden: mcp-derouter/start-mcp.sh, Cursor Composer fallback for role prose.

На успех пишет stamp JSON (tier, model, endpoint, request id, usage) рядом со статьёй
или в memory/setup/ для smoke.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from excalibur_repo_paths import resolve_article_dir, resolve_article_output

DEFAULT_API_KEY_ENV = "DEROUTER_API_KEY"
PRIMARY_ENDPOINT = "https://api.derouter.ai/openai/v1/chat/completions"
FALLBACK_ENDPOINT = "https://api.apikey.cloud/openai/v1/chat/completions"
DEFAULT_TIMEOUT_SECONDS = 300
MIN_TIMEOUT_SECONDS = 60
DEFAULT_MAX_RETRIES = 1
DEFAULT_RETRY_WAIT_SECONDS = 5

DEFAULT_OPUS_MODEL = "claude-opus-5"
DEFAULT_TERRA_MODEL = "gpt-5.6-terra"
DEFAULT_OPUS_MODEL_ENV = "DEROUTER_OPUS_MODEL"
DEFAULT_TERRA_MODEL_ENV = "DEROUTER_TERRA_MODEL"

OPUS_MODEL_ALIASES = (
    "claude-opus-5",
    "anthropic/claude-opus-5",
)
TERRA_MODEL_ALIASES = (
    "gpt-5.6-terra",
    "openai/gpt-5.6-terra",
)

VALID_ROLES = frozenset(
    {
        "scout",
        "research",
        "title",
        "writer",
        "sol",
        "description",
        "cover-text",
        "schema",
        "cover-scene",
        "smoke",
    }
)

# Opus 5 = Writer only; everything else Terra (cost canon — do not revert scout/title/sol to powerful).
POWERFUL_ROLES = frozenset({"writer"})
UTILITY_ROLES = frozenset(
    {"scout", "title", "sol", "research", "description", "cover-text", "schema", "cover-scene"}
)


class DerouterChatError(RuntimeError):
    """Fatal API or configuration error."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        self.status = status
        super().__init__(message)


class DerouterChatRetryable(DerouterChatError):
    """Retryable HTTP/network failure."""


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_writing_model_config(root: Path) -> dict[str, Any]:
    tenant_path = root / "shared/tenant-config.json"
    if not tenant_path.is_file():
        return {}
    try:
        tenant = json.loads(tenant_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise DerouterChatError(f"tenant-config JSON invalid: {exc}") from exc
    writing = tenant.get("writing_model")
    if not isinstance(writing, dict):
        return {}
    return writing


def validate_writing_model_opus_writer_only(writing: dict[str, Any]) -> None:
    """Opus 5 = Writer only; everything else Terra."""
    if not writing:
        return
    powerful_roles = set(writing.get("powerful", {}).get("roles") or POWERFUL_ROLES)
    non_writer_on_opus = powerful_roles - {"writer"}
    if non_writer_on_opus:
        raise DerouterChatError(
            "Opus 5 = Writer only; everything else Terra. "
            f"Non-writer roles on powerful tier: {sorted(non_writer_on_opus)}"
        )


def tier_for_role(role: str, writing: dict[str, Any]) -> str:
    powerful_roles = set(writing.get("powerful", {}).get("roles") or POWERFUL_ROLES)
    utility_roles = set(writing.get("utility", {}).get("roles") or UTILITY_ROLES)
    if role == "smoke":
        return "utility"
    if role in powerful_roles:
        return "powerful"
    if role in utility_roles:
        return "utility"
    raise DerouterChatError(f"Role {role!r} not mapped in tenant writing_model tiers")


def tier_config(writing: dict[str, Any], tier: str) -> dict[str, Any]:
    block = writing.get(tier)
    if isinstance(block, dict):
        return block
    if tier == "powerful":
        return {
            "model": DEFAULT_OPUS_MODEL,
            "model_env": DEFAULT_OPUS_MODEL_ENV,
            "family": DEFAULT_OPUS_MODEL,
            "roles": sorted(POWERFUL_ROLES),
        }
    return {
        "model": DEFAULT_TERRA_MODEL,
        "model_env": DEFAULT_TERRA_MODEL_ENV,
        "roles": sorted(UTILITY_ROLES),
    }


def model_aliases_for_tier(tier: str, base_model: str) -> list[str]:
    defaults = OPUS_MODEL_ALIASES if tier == "powerful" else TERRA_MODEL_ALIASES
    ordered: list[str] = []
    for candidate in (base_model, *defaults):
        if candidate and candidate not in ordered:
            ordered.append(candidate)
    return ordered


def is_opus_family(model: str) -> bool:
    return "opus" in model.lower()


def is_model_not_found_error(exc: Exception) -> bool:
    if isinstance(exc, DerouterChatError):
        if exc.status == 404:
            return True
        lower = str(exc).lower()
        if "model" in lower and any(token in lower for token in ("not found", "unknown", "invalid", "404")):
            return True
    return False


def resolve_model(
    role: str,
    override: str | None,
    root: Path,
    *,
    one_shot: bool = False,
) -> tuple[str, str]:
    """Возвращает (model_id, tier). Источник истины — tenant-config role map.

    ``one_shot=True`` (флаг ``--one-shot-model``) — явный разовый override владельца
    для одной статьи: точный id без проверки семейства tier и без alias-fallback.
    Дефолты tenant-config / env не трогаются.
    """
    writing = load_writing_model_config(root)
    validate_writing_model_opus_writer_only(writing)
    tier = tier_for_role(role, writing)
    if one_shot:
        model = (override or "").strip()
        if not model:
            raise DerouterChatError("--one-shot-model requires a non-empty model id")
        return model, tier
    tier_block = tier_config(writing, tier)
    config_model = str(tier_block.get("model") or "").strip()
    model_env = str(tier_block.get("model_env") or "").strip()
    env_model = os.environ.get(model_env, "").strip() if model_env else ""

    if override and override.strip():
        model = override.strip()
    elif env_model:
        model = env_model
    elif config_model:
        model = config_model
    else:
        model = DEFAULT_OPUS_MODEL if tier == "powerful" else DEFAULT_TERRA_MODEL

    # DEROUTER_TEXT_MODEL — legacy; не даём переключить powerful-роли на non-Opus.
    legacy_text = os.environ.get("DEROUTER_TEXT_MODEL", "").strip()
    if legacy_text and not override:
        if tier == "powerful":
            if is_opus_family(legacy_text):
                model = legacy_text
            elif not is_opus_family(model):
                model = DEFAULT_OPUS_MODEL
        elif tier == "utility" and not env_model and not config_model:
            if "terra" in legacy_text.lower() or legacy_text == DEFAULT_TERRA_MODEL:
                model = legacy_text

    if tier == "powerful" and not is_opus_family(model):
        raise DerouterChatError(
            f"Role {role!r} requires Claude Opus family; got {model!r}. "
            f"Set {tier_block.get('model_env') or DEFAULT_OPUS_MODEL_ENV}=claude-opus-5"
        )

    if tier == "utility" and "terra" not in model.lower():
        raise DerouterChatError(
            f"Role {role!r} requires utility terra model; got {model!r}. "
            f"Set {tier_block.get('model_env') or DEFAULT_TERRA_MODEL_ENV}=gpt-5.6-terra"
        )

    return model, tier


def load_text_arg(*, inline: str | None, path: str | None, label: str) -> str:
    if path:
        p = Path(path)
        if not p.is_file():
            raise DerouterChatError(f"{label} file not found: {path}")
        return p.read_text(encoding="utf-8")
    if inline is not None:
        return inline
    raise DerouterChatError(f"Provide --{label.replace(' ', '-')} or --{label.replace(' ', '-')}-file")


def is_retryable_http(status: int) -> bool:
    return status in {401, 403, 408, 429, 500, 502, 503, 504, 524}


def http_chat_post(
    endpoint: str,
    api_key: str,
    payload: dict[str, Any],
    *,
    timeout: int,
) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if is_retryable_http(exc.code):
            raise DerouterChatRetryable(
                f"Derouter HTTP {exc.code}: {body[:500]}", status=exc.code
            ) from exc
        raise DerouterChatError(f"Derouter HTTP {exc.code}: {body[:500]}", status=exc.code) from exc
    except urllib.error.URLError as exc:
        raise DerouterChatRetryable(f"Derouter network error: {exc.reason}") from exc

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise DerouterChatError(f"Derouter returned non-JSON: {body[:500]}") from exc
    if not isinstance(parsed, dict):
        raise DerouterChatError("Derouter returned a non-object JSON response")
    return parsed


def extract_assistant_text(response: dict[str, Any]) -> str:
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        raise DerouterChatError("Derouter response missing choices")
    first = choices[0]
    if not isinstance(first, dict):
        raise DerouterChatError("Derouter choices[0] is not an object")
    message = first.get("message")
    if not isinstance(message, dict):
        raise DerouterChatError("Derouter choices[0].message missing")
    content = message.get("content")
    if not isinstance(content, str) or not content.strip():
        raise DerouterChatError("Derouter returned empty assistant content")
    return content


def call_derouter_chat(
    *,
    system_prompt: str,
    user_prompt: str,
    model: str,
    timeout: int,
    max_retries: int,
) -> tuple[str, dict[str, Any], str]:
    api_key = os.environ.get(DEFAULT_API_KEY_ENV, "").strip()
    if not api_key:
        raise DerouterChatError(f"{DEFAULT_API_KEY_ENV} missing")

    payload: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    endpoints = [PRIMARY_ENDPOINT, FALLBACK_ENDPOINT]
    last_error: Exception | None = None

    for endpoint in endpoints:
        attempts = max_retries + 1
        for attempt in range(attempts):
            try:
                response = http_chat_post(endpoint, api_key, payload, timeout=timeout)
                text = extract_assistant_text(response)
                return text, response, endpoint
            except DerouterChatRetryable as exc:
                last_error = exc
                if attempt < attempts - 1:
                    time.sleep(DEFAULT_RETRY_WAIT_SECONDS)
                    continue
                break
            except DerouterChatError as exc:
                last_error = exc
                break

    raise DerouterChatError(
        f"Derouter chat API unavailable after retry; last error: {last_error}"
    )


def call_derouter_with_aliases(
    *,
    system_prompt: str,
    user_prompt: str,
    tier: str,
    model: str,
    timeout: int,
    max_retries: int,
    exact_model_only: bool = False,
) -> tuple[str, dict[str, Any], str, str]:
    # one-shot override: только указанный id, без тихого отката на Opus/Terra
    aliases = [model] if exact_model_only else model_aliases_for_tier(tier, model)
    last_error: Exception | None = None
    for candidate in aliases:
        try:
            text, response, endpoint = call_derouter_chat(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                model=candidate,
                timeout=timeout,
                max_retries=max_retries,
            )
            if candidate != model:
                print(f"NOTE model alias accepted: {candidate} (configured {model})")
            return text, response, endpoint, candidate
        except DerouterChatError as exc:
            last_error = exc
            if is_model_not_found_error(exc):
                print(f"WARN model {candidate!r} not accepted: {exc}", file=sys.stderr)
                continue
            raise
    raise DerouterChatError(
        f"No working model id for tier {tier}; tried {aliases}; last error: {last_error}"
    )


def role_blocker_label(role: str) -> str:
    mapping = {
        "scout": "SCOUT",
        "research": "RESEARCH",
        "title": "TITLE",
        "writer": "WRITER",
        "sol": "SOL",
        "description": "DESCRIPTION",
        "cover-text": "COVER-TEXT",
        "schema": "SCHEMA",
        "cover-scene": "COVER-SCENE",
        "smoke": "SMOKE",
    }
    return mapping.get(role, role.upper())


def print_blocker(role: str, reason: str) -> None:
    label = role_blocker_label(role)
    print(f"DEROUTER {label} BLOCKER", file=sys.stderr)
    print(f"reason: {reason}", file=sys.stderr)


def write_stamp(
    *,
    stamp_path: Path,
    role: str,
    tier: str,
    model: str,
    endpoint: str,
    response: dict[str, Any],
    user_prompt_preview: str,
    one_shot_override: bool = False,
) -> None:
    usage = response.get("usage") if isinstance(response.get("usage"), dict) else {}
    stamp: dict[str, Any] = {
        "script": "scripts/excalibur_blog_derouter_opus_chat.py",
        "role": role,
        "tier": tier,
        "model": model,
        "endpoint": endpoint,
        "request_id": response.get("id"),
        "usage": usage,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "provider": "derouter-rest",
        "user_prompt_chars": len(user_prompt_preview),
        "contract": "shared/derouter-opus-brain-contract.md",
    }
    if one_shot_override:
        stamp["model_override"] = "one_shot_owner_override"
        stamp["tier_default_model_unchanged"] = True
    stamp_path.parent.mkdir(parents=True, exist_ok=True)
    stamp_path.write_text(json.dumps(stamp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_stamp_path(*, article_dir: str | None, role: str, root: Path) -> Path:
    if article_dir:
        ad = resolve_article_dir(article_dir, root)
        return ad / f"derouter-opus-stamp-{role}.json"
    if role == "smoke":
        return root / "memory/setup/derouter-smoke-terra-stamp.json"
    return root / "memory/setup/derouter-opus-stamp.json"


def resolve_derouter_output_path(
    output: str,
    *,
    article_dir: str | None,
    root: Path,
) -> Path:
    """Resolve ``--output`` under ``--article-dir`` for bare filenames (INC-20260828-1246)."""
    out = Path(output)
    if article_dir:
        ad = resolve_article_dir(article_dir, root)
        return resolve_article_output(out, article_dir=ad, root=root, default_name=out.name)
    if out.is_absolute():
        return out
    return root / out


def run_smoke_ping(
    *,
    root: Path,
    timeout: int,
    stamp_suffix: str,
    role_for_tier: str,
    system_prompt: str,
    user_prompt: str,
    pass_check: Callable[[str], bool],
) -> tuple[bool, str | None]:
    model, tier = resolve_model(role_for_tier, None, root)
    try:
        text, response, endpoint, resolved_model = call_derouter_with_aliases(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            tier=tier,
            model=model,
            timeout=timeout,
            max_retries=DEFAULT_MAX_RETRIES,
        )
    except DerouterChatError as exc:
        print_blocker("smoke", str(exc))
        return False, None

    stamp_path = root / f"memory/setup/derouter-smoke-{stamp_suffix}-stamp.json"
    write_stamp(
        stamp_path=stamp_path,
        role="smoke",
        tier=tier,
        model=resolved_model,
        endpoint=endpoint,
        response=response,
        user_prompt_preview=user_prompt,
    )
    rel = stamp_path.relative_to(root) if stamp_path.is_relative_to(root) else stamp_path
    print(f"STAMP {rel}")
    ok = pass_check(text)
    print(f"SMOKE {stamp_suffix} {'PASS' if ok else 'FAIL'}: {text.strip()[:80]}")
    return ok, resolved_model


def maybe_lock_model_in_tenant(root: Path, tier: str, resolved_model: str) -> None:
    tenant_path = root / "shared/tenant-config.json"
    if not tenant_path.is_file() or not resolved_model:
        return
    try:
        tenant = json.loads(tenant_path.read_text(encoding="utf-8"))
        writing = tenant.get("writing_model")
        if not isinstance(writing, dict):
            return
        tier_block = writing.get(tier)
        if not isinstance(tier_block, dict):
            return
        current = str(tier_block.get("model") or "").strip()
        if current == resolved_model:
            return
        tier_block["model"] = resolved_model
        writing[tier] = tier_block
        tenant["writing_model"] = writing
        tenant_path.write_text(json.dumps(tenant, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"LOCK tenant-config writing_model.{tier}.model → {resolved_model}")
    except (json.JSONDecodeError, OSError) as exc:
        print(f"WARN could not lock model in tenant-config: {exc}", file=sys.stderr)


def run_chat(args: argparse.Namespace) -> int:
    role = args.role.strip().lower()
    if role not in VALID_ROLES:
        raise DerouterChatError(f"Invalid role {role!r}; expected one of {sorted(VALID_ROLES)}")

    root = project_root()
    timeout = max(MIN_TIMEOUT_SECONDS, int(args.timeout))
    validate_writing_model_opus_writer_only(load_writing_model_config(root))

    if role == "smoke" or args.smoke:
        terra_ok, terra_model = run_smoke_ping(
            root=root,
            timeout=timeout,
            stamp_suffix="terra",
            role_for_tier="research",
            system_prompt="You are a connectivity test. Reply with exactly: pong",
            user_prompt="ping",
            pass_check=lambda text: "pong" in text.lower(),
        )
        opus_ok, opus_model = run_smoke_ping(
            root=root,
            timeout=timeout,
            stamp_suffix="opus",
            role_for_tier="writer",
            system_prompt="You are a connectivity test for Writer tier. Reply with exactly one Russian word: готово",
            user_prompt="smoke writer",
            pass_check=lambda text: "готово" in text.lower(),
        )
        if terra_model:
            maybe_lock_model_in_tenant(root, "utility", terra_model)
        if opus_model:
            maybe_lock_model_in_tenant(root, "powerful", opus_model)
        if terra_ok and opus_ok:
            print("SMOKE ALL PASS (terra + opus)")
            return 0
        if terra_ok:
            print("SMOKE PARTIAL: terra PASS, opus FAIL or skipped")
            return 1
        print("SMOKE FAIL")
        return 1

    one_shot_model = (getattr(args, "one_shot_model", None) or "").strip()
    if one_shot_model and args.model:
        raise DerouterChatError("use either --model or --one-shot-model, not both")
    model, tier = resolve_model(
        role,
        one_shot_model or args.model,
        root,
        one_shot=bool(one_shot_model),
    )
    if one_shot_model:
        print(f"NOTE one-shot owner override: role={role} model={model} (tier {tier} default untouched)")

    system_prompt = load_text_arg(
        inline=args.system_prompt, path=args.system_file, label="system-prompt"
    )
    user_prompt = load_text_arg(
        inline=args.user_prompt, path=args.user_file, label="user-prompt"
    )

    try:
        text, response, endpoint, resolved_model = call_derouter_with_aliases(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            tier=tier,
            model=model,
            timeout=timeout,
            max_retries=DEFAULT_MAX_RETRIES,
            exact_model_only=bool(one_shot_model),
        )
    except DerouterChatError as exc:
        print_blocker(role, str(exc))
        return 2

    if args.output:
        out = resolve_derouter_output_path(args.output, article_dir=args.article_dir, root=root)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        print(f"WROTE {out.relative_to(root) if out.is_relative_to(root) else out}")

    stamp_path = resolve_stamp_path(article_dir=args.article_dir, role=role, root=root)
    if args.stamp_path:
        stamp_path = Path(args.stamp_path)
        if not stamp_path.is_absolute():
            stamp_path = root / stamp_path
    write_stamp(
        stamp_path=stamp_path,
        role=role,
        tier=tier,
        model=resolved_model,
        endpoint=endpoint,
        response=response,
        user_prompt_preview=user_prompt[:200],
        one_shot_override=bool(one_shot_model),
    )
    print(f"STAMP {stamp_path.relative_to(root) if stamp_path.is_relative_to(root) else stamp_path}")

    preview = text.strip().replace("\n", " ")[:120]
    print(f"OK role={role} tier={tier} model={resolved_model} chars={len(text)} preview={preview!r}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Derouter chat — двухуровневый мозг Excalibur BLOG (Opus powerful / Terra utility)"
    )
    parser.add_argument(
        "--role",
        required=True,
        choices=sorted(VALID_ROLES),
        help="Pipeline role (scout, writer, sol, …) or smoke",
    )
    parser.add_argument("--system-prompt", help="System prompt inline")
    parser.add_argument("--system-file", help="System prompt file (skill/agent md)")
    parser.add_argument("--user-prompt", help="User prompt inline")
    parser.add_argument("--user-file", help="User prompt file (assembled inputs)")
    parser.add_argument("--output", "-o", help="Write assistant text to this path")
    parser.add_argument(
        "--article-dir",
        help="Article dir for stamp: <dir>/derouter-opus-stamp-<role>.json",
    )
    parser.add_argument("--stamp-path", help="Override stamp JSON path")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Alias: --role smoke (terra ping + opus writer one-liner)",
    )
    parser.add_argument(
        "--model",
        help="Override model id (must match role tier from tenant-config)",
    )
    parser.add_argument(
        "--one-shot-model",
        help=(
            "Разовый override владельца для одной статьи: точный id из каталога Derouter "
            "без проверки семейства tier и без alias-fallback; дефолты tenant-config не меняются"
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.smoke:
        args.role = "smoke"
    try:
        return run_chat(args)
    except DerouterChatError as exc:
        role = getattr(args, "role", "unknown")
        print_blocker(role, str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

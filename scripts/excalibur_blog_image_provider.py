#!/usr/bin/env python3
"""Резолв image provider из tenant-config + IMAGE_PROVIDER env."""

from __future__ import annotations

import json
import os
from pathlib import Path

TENANT_CONFIG_REL = Path("shared/tenant-config.json")

DEROUTER_FLOW = {
    "provider": "derouter-rest",
    "script": "scripts/excalibur_blog_derouter_gpt_image2_api.py",
    "probe_script": "scripts/excalibur_blog_derouter_image_base_probe.py",
    "contract": "shared/derouter-gpt-image-api-contract.md",
    "note": (
        "PRIMARY: Derouter REST image API (api-direct, 2K 16:9). "
        "Fallback: excalibur_blog_kie_gpt_image2_api.py when DEROUTER auth/5xx. "
        "FORBIDDEN: flux2-pro-*, Seedream, nano_banana*, z-image, mcp-derouter/start-mcp.sh."
    ),
}

GRSAI_FLOW = {
    "provider": "grsai",
    "script": "scripts/excalibur_blog_grsai_gpt_image2_api.py",
    "probe_script": "scripts/excalibur_blog_grsai_base_probe.py",
    "contract": "shared/grsai-gpt-image-api-contract.md",
    "note": (
        "PRIMARY: Grsai draw API (non-vip primary tier + resolution=2K first; "
        "one vip retry/sheet only when primary cannot deliver long_side>=2048 or hard API fail). "
        "Fallback: excalibur_blog_kie_gpt_image2_api.py when Grsai fail. "
        "FORBIDDEN: flux2-pro-*, Seedream, nano_banana*, z-image, mcp-derouter/start-mcp.sh."
    ),
}


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_tenant_config(root: Path | None = None) -> dict:
    root = root or project_root()
    path = root / TENANT_CONFIG_REL
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_image_provider(root: Path | None = None) -> str:
    """Вернуть provider id: grsai | derouter-rest."""
    env_override = os.environ.get("IMAGE_PROVIDER", "").strip().casefold()
    if env_override in {"grsai", "grsai-api", "grsai-rest"}:
        return "grsai"
    if env_override in {"derouter", "derouter-rest", "derouter-api"}:
        return "derouter-rest"

    tenant = load_tenant_config(root)
    tenant_provider = str(tenant.get("IMAGE_PROVIDER") or "").strip().casefold()
    if tenant_provider in {"grsai", "grsai-api", "grsai-rest"}:
        return "grsai"
    if tenant_provider in {"derouter", "derouter-rest", "derouter-api"}:
        return "derouter-rest"

    for key in ("image_api", "image_generation"):
        section = tenant.get(key) or {}
        provider = str(section.get("provider") or "").strip().casefold()
        if provider in {"grsai", "grsai-api", "grsai-rest"}:
            return "grsai"
        if provider in {"derouter", "derouter-rest", "derouter-api"}:
            return "derouter-rest"
    return "derouter-rest"


def resolve_image_flow(root: Path | None = None) -> dict[str, str]:
    provider = resolve_image_provider(root)
    if provider == "grsai":
        return dict(GRSAI_FLOW)
    return dict(DEROUTER_FLOW)


def resolve_image_script(root: Path | None = None) -> str:
    return resolve_image_flow(root)["script"]

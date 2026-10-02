"""Owner-scoped, repeatable setup using authenticated Fulcra operations."""

import json
from uuid import UUID, NAMESPACE_URL, uuid5

from fastmcp.exceptions import ToolError

PROFILE_PATH = "/aicq/profile.json"
SETTINGS_PATH = "/aicq/settings.json"
DEFAULT_SETTINGS = {"schema_version": 1, "background_responses": False}


def binding(fulcra):
    info = fulcra.get_user_info()
    try:
        userid = str(UUID(info["userid"]))
    except (KeyError, ValueError, TypeError):
        raise ToolError("Fulcra did not return a valid account identity.") from None
    owner = str(uuid5(NAMESPACE_URL, "urn:aicq:owner:" + userid))
    return {
        "schema_version": 1,
        "fulcra_userid": userid,
        "owner_id": owner,
        "agent_id": str(uuid5(UUID(owner), "default-agent")),
    }


def read_json(fulcra, path):
    # Querying returns an empty list for absence, while real API errors propagate.
    parent, name = path.rsplit("/", 1)
    payload = json.loads(
        fulcra.fulcra_api(
            "/input/v1/file_upload",
            query={"path": parent, "name": name, "state": "uploaded"},
        )
    )
    files = payload["files"]
    if not files:
        return None
    if len(files) != 1:
        raise ToolError(
            "AICQ found ambiguous current resource versions; setup needs repair."
        )
    data = fulcra.download_file(files[0]["id"]).read(16385)
    if len(data) > 16384:
        raise ToolError("AICQ resource exceeds the supported size.")
    value = json.loads(data)
    if not isinstance(value, dict):
        raise ToolError("AICQ resource must be a JSON object.")
    return value


def validate_profile(profile, expected):
    if any(profile.get(key) != value for key, value in expected.items()):
        raise ToolError(
            "Existing AICQ profile conflicts with the verified account binding; preserve it and repair setup."
        )


def validate_settings(settings):
    if settings.get("schema_version") != 1 or not isinstance(
        settings.get("background_responses"), bool
    ):
        raise ToolError(
            "Existing settings have an unsupported schema; preserve them for repair."
        )


def identity(fulcra):
    expected = binding(fulcra)
    profile = read_json(fulcra, PROFILE_PATH)
    if profile is not None:
        validate_profile(profile, expected)
    settings = read_json(fulcra, SETTINGS_PATH)
    if settings is not None:
        validate_settings(settings)
    return {
        **expected,
        "setup_complete": profile is not None and settings is not None,
        "profile_path": PROFILE_PATH,
        "settings_path": SETTINGS_PATH,
    }


def ensure_resource(fulcra, path, expected):
    existing = read_json(fulcra, path)
    if existing is not None:
        if path == PROFILE_PATH:
            validate_profile(existing, expected)
        else:
            validate_settings(existing)
        return "reused"
    data = json.dumps(expected, sort_keys=True).encode()
    fulcra.upload_file(data, "application/json", len(data), path)
    # An upload receipt alone is insufficient. Retry setup after uncertain ingestion.
    actual = read_json(fulcra, path)
    if actual != expected:
        raise ToolError(
            "Setup write is not yet confirmed. Retry setup to inspect and reuse persisted resources."
        )
    return "created"


def setup(fulcra):
    expected = binding(fulcra)
    profile = ensure_resource(fulcra, PROFILE_PATH, expected)
    settings = ensure_resource(fulcra, SETTINGS_PATH, DEFAULT_SETTINGS)
    return {
        **identity(fulcra),
        "resources": {"profile": profile, "settings": settings},
        "contact_setup": "pending M3",
        "messaging": "pending M4",
    }

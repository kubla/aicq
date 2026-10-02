import io
import json
from unittest.mock import Mock

import pytest
from fastmcp.exceptions import ToolError
from aicq_mcp.workspace import PROFILE_PATH, SETTINGS_PATH, binding, identity, setup


class Account:
    def __init__(self, userid="22222222-2222-4222-8222-222222222222"):
        self.userid, self.files, self.writes = userid, {}, []
        self.fail_settings_once = False

    def get_user_info(self):
        return {"userid": self.userid, "intercom_token": "do-not-return"}

    def fulcra_api(self, endpoint, query):
        path = query["path"] + "/" + query["name"]
        return json.dumps({"files": [{"id": path}] if path in self.files else []})

    def download_file(self, fileid):
        return io.BytesIO(json.dumps(self.files[fileid]).encode())

    def upload_file(self, data, content_type, size, path):
        if path == SETTINGS_PATH and self.fail_settings_once:
            self.fail_settings_once = False
            raise TimeoutError("uncertain upload")
        self.files[path] = json.loads(data)
        self.writes.append(path)
        return {"file": {"id": path}}


def test_fresh_setup_reuses_identity_on_repeated_setup_and_reconnect():
    first = Account()
    before = identity(first)
    assert not before["setup_complete"] and not first.writes
    result = setup(first)
    assert result["setup_complete"] and len(first.writes) == 2
    assert result["agent_id"] == before["agent_id"]
    repeated = setup(first)
    assert repeated["resources"] == {"profile": "reused", "settings": "reused"}
    second = Account(first.userid)
    second.files = first.files
    assert identity(second)["owner_id"] == result["owner_id"]
    assert identity(second)["agent_id"] == result["agent_id"]
    assert "intercom_token" not in json.dumps(result)


def test_interrupted_setup_preserves_profile_and_recovers_missing_settings():
    account = Account()
    account.fail_settings_once = True
    with pytest.raises(TimeoutError):
        setup(account)
    existing = dict(account.files[PROFILE_PATH])
    assert not identity(account)["setup_complete"]
    result = setup(account)
    assert result["resources"] == {"profile": "reused", "settings": "created"}
    assert account.files[PROFILE_PATH] == existing
    assert account.writes.count(PROFILE_PATH) == 1


def test_owner_conflict_and_upstream_failure_never_overwrite():
    account = Account()
    account.files[PROFILE_PATH] = binding(
        Account("33333333-3333-4333-8333-333333333333")
    )
    with pytest.raises(ToolError, match="conflicts"):
        setup(account)
    assert not account.writes
    account.fulcra_api = Mock(side_effect=TimeoutError("Fulcra unavailable"))
    with pytest.raises(TimeoutError):
        setup(account)
    assert not account.writes


def test_uncertain_persistence_requires_retry_and_invalid_identity_is_rejected():
    account = Account()
    account.upload_file = Mock(return_value={"file": {"id": "receipt-only"}})
    with pytest.raises(ToolError, match="not yet confirmed"):
        setup(account)
    with pytest.raises(ToolError, match="valid account identity"):
        binding(Account("not-a-user-id"))

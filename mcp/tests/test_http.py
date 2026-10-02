import time
from contextlib import asynccontextmanager

import httpx
import pytest
from mcp.server.auth.provider import AccessToken
from aicq_mcp.server import app, provider, RESOURCE_URL, UI_URI

HEADERS = {
    "Accept": "application/json, text/event-stream",
    "Content-Type": "application/json",
}


@asynccontextmanager
async def client(tmp_path, monkeypatch):
    from fulcra_mcp.settings import settings

    monkeypatch.setattr(settings, "state_path", tmp_path)
    provider.tokens["mcp_test_aicq"] = AccessToken(
        token="mcp_test_aicq",
        client_id="c",
        scopes=["openid"],
        resource=RESOURCE_URL,
        expires_at=int(time.time()) + 3600,
    )
    provider.tokens["mcp_test_other"] = AccessToken(
        token="mcp_test_other",
        client_id="c",
        scopes=["openid"],
        resource="https://other.example/mcp",
        expires_at=int(time.time()) + 3600,
    )
    try:
        async with (
            app.router.lifespan_context(app),
            httpx.AsyncClient(
                transport=httpx.ASGITransport(app=app),
                base_url="http://test",
                headers=HEADERS,
            ) as http,
        ):
            yield http
    finally:
        provider.tokens.pop("mcp_test_aicq", None)
        provider.tokens.pop("mcp_test_other", None)


async def test_http_discovery_entrypoints_and_audience_denial(tmp_path, monkeypatch):
    async with client(tmp_path, monkeypatch) as http:
        payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}
        for token in [None, "unissued", "mcp_test_other"]:
            headers = {"Authorization": "Bearer " + token} if token else {}
            response = await http.post("/mcp", json=payload, headers=headers)
            assert response.status_code == 401
        response = await http.post(
            "/mcp", json=payload, headers={"Authorization": "Bearer mcp_test_aicq"}
        )
        assert response.status_code == 200
        tools = response.json()["result"]["tools"]
        for name, entry in [("aicq_open", "global"), ("aicq_thread", "thread")]:
            tool = next(t for t in tools if t["name"] == name)
            assert tool["inputSchema"]["properties"] == {}
            assert not tool["inputSchema"].get("required")
            assert tool["_meta"]["openai/ui"]["entrypoints"] == [{"type": entry}]
            assert tool["_meta"]["ui"]["resourceUri"] == UI_URI
        resource = await http.get("/.well-known/oauth-protected-resource/mcp")
        assert (
            resource.status_code == 200 and resource.json()["resource"] == RESOURCE_URL
        )
        resource_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "resources/read",
            "params": {"uri": UI_URI},
        }
        html = await http.post(
            "/mcp",
            json=resource_request,
            headers={"Authorization": "Bearer mcp_test_aicq"},
        )
        assert html.status_code == 200
        content = html.json()["result"]["contents"][0]
        assert content["mimeType"] == "text/html;profile=mcp-app"
        assert "<script" in content["text"] and "Your agent address" in content["text"]
        assert 'src="/main.ts"' not in content["text"]


async def test_accidental_http_launch_cannot_use_stdio_owner_credentials(
    tmp_path, monkeypatch
):
    from fulcra_mcp.settings import settings
    from aicq_mcp.server import credentials

    async with client(tmp_path, monkeypatch) as http:
        monkeypatch.setattr(settings, "fulcra_environment", "stdio")

        def must_not_load_owner():
            raise AssertionError("HTTP request accessed stdio owner's credentials")

        monkeypatch.setattr(credentials, "get_fulcra_object", must_not_load_owner)
        response = await http.post(
            "/mcp",
            headers={"Authorization": "Bearer mcp_test_aicq"},
            json={
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {"name": "aicq_identity", "arguments": {}},
            },
        )
        assert response.status_code == 200
        result = response.json()["result"]
        assert result["isError"]
        assert "FULCRA_ENVIRONMENT=http" in result["content"][0]["text"]

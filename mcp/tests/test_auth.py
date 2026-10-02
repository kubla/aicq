import time
from unittest.mock import Mock

import pytest
from mcp.server.auth.provider import (
    AccessToken,
    AuthorizationParams,
    AuthorizeError,
    TokenError,
)
from mcp.server.auth.settings import ClientRegistrationOptions
from mcp.shared.auth import OAuthClientInformationFull
from pydantic import AnyHttpUrl
from aicq_mcp.auth import AICQOAuthProvider
from fulcra_mcp.settings import settings
from fulcra_mcp.provider import OIDC_SCOPES

RESOURCE = "http://127.0.0.1:4499/mcp"


def gateway(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "state_path", tmp_path)
    return AICQOAuthProvider(
        issuer_url="http://127.0.0.1:4499",
        resource_url=RESOURCE,
        client_registration_options=ClientRegistrationOptions(
            enabled=True, valid_scopes=OIDC_SCOPES
        ),
        required_scopes=["openid"],
    )


async def test_wrong_audience_rejected_before_authorization(tmp_path, monkeypatch):
    provider = gateway(tmp_path, monkeypatch)
    client = OAuthClientInformationFull(
        client_id="client", redirect_uris=[AnyHttpUrl("http://127.0.0.1:9999/callback")]
    )
    params = AuthorizationParams(
        state="client-state",
        resource="https://other.example/mcp",
        scopes=["openid"],
        code_challenge="pkce",
        redirect_uri=client.redirect_uris[0],
        redirect_uri_provided_explicitly=True,
    )
    with pytest.raises(AuthorizeError):
        await provider.authorize(client, params)
    assert not provider.state_mapping


async def test_resource_binding_survives_restart_and_refresh(tmp_path, monkeypatch):
    provider = gateway(tmp_path, monkeypatch)
    token = provider._bind_tokens(
        provider._issue_tokens("client", ["openid"], None), RESOURCE
    )
    restored = gateway(tmp_path, monkeypatch)
    assert (await restored.load_access_token(token.access_token)).resource == RESOURCE
    client = OAuthClientInformationFull(
        client_id="client", redirect_uris=[AnyHttpUrl("http://127.0.0.1:9999/callback")]
    )
    refresh = await restored.load_refresh_token(client, token.refresh_token)
    rotated = await restored.exchange_refresh_token(client, refresh, ["openid"])
    assert (await restored.load_access_token(rotated.access_token)).resource == RESOURCE
    assert await restored.load_refresh_token(client, token.refresh_token) is None
    stranger = OAuthClientInformationFull(
        client_id="stranger", redirect_uris=client.redirect_uris
    )
    assert await restored.load_refresh_token(stranger, rotated.refresh_token) is None
    wrong = provider._bind_tokens(
        provider._issue_tokens("client", ["openid"], None), "https://other.example/mcp"
    )
    assert await restored.load_access_token(wrong.access_token) is None
    assert await restored.load_access_token("not-an-issued-token") is None


async def test_overlapping_logins_bind_each_code_to_its_own_upstream_account(
    tmp_path, monkeypatch
):
    from datetime import datetime, timedelta
    from urllib.parse import parse_qs, urlparse, urlencode
    from fulcra_api.credentials import FulcraCredentials
    import fulcra_mcp.provider as foundation

    class LoginAPI:
        def __init__(self, **kwargs):
            pass

        def get_authorization_code_url(self, redirect_uri, state):
            return "https://login.example/authorize?" + urlencode({"state": state})

        def authorize_with_authorization_code(self, code, redirect_uri):
            self.fulcra_credentials = FulcraCredentials(
                access_token="fixture-" + code,
                access_token_expiration=datetime.now() + timedelta(hours=1),
            )

    monkeypatch.setattr(foundation, "FulcraAPI", LoginAPI)
    provider = gateway(tmp_path, monkeypatch)
    client = OAuthClientInformationFull(
        client_id="same-client",
        redirect_uris=[AnyHttpUrl("http://127.0.0.1:9999/callback")],
    )
    params = AuthorizationParams(
        state="same-downstream-state",
        resource=RESOURCE,
        scopes=["openid"],
        code_challenge="pkce",
        redirect_uri=client.redirect_uris[0],
        redirect_uri_provided_explicitly=True,
    )
    states = []
    for _ in range(2):
        url = await provider.authorize(client, params)
        states.append(parse_qs(urlparse(url).query)["state"][0])
    assert states[0] != states[1] and states[0] != params.state
    codes = []
    for index, state in enumerate(states):
        redirect = await provider.handle_callback(str(index), state)
        query = parse_qs(urlparse(redirect).query)
        assert query["state"] == [params.state]
        codes.append(query["code"][0])
    # Exchange in reverse callback order: the earlier code retains its account.
    for index in [1, 0]:
        token = await provider.exchange_authorization_code(
            client, provider.auth_codes[codes[index]]
        )
        assert provider.credentials_for_token(token.access_token)[
            1
        ].access_token == "fixture-" + str(index)
        refresh = await provider.load_refresh_token(client, token.refresh_token)
        await provider.exchange_refresh_token(client, refresh, ["openid"])
        with pytest.raises(TokenError):
            await provider.exchange_refresh_token(client, refresh, ["openid"])
    with pytest.raises(TokenError):
        await provider.handle_callback("fixture-replay", states[0])

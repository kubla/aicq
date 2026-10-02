"""Resource binding added to the existing Fulcra persisted OAuth gateway."""

import secrets
import time
from urllib.parse import parse_qs, urlparse
from mcp.server.auth.provider import TokenError, construct_redirect_uri
from fulcra_mcp.provider import FulcraOAuthProvider


class AICQOAuthProvider(FulcraOAuthProvider):
    def __init__(self, *args, resource_url, **kwargs):
        super().__init__(*args, **kwargs)
        self.resource_url = resource_url
        self.authorization_resources = {}
        self.code_credentials = {}

    async def authorize(self, client, params):
        if params.resource != self.resource_url:
            raise TokenError("invalid_target", "Use the advertised AICQ resource URL.")
        now = time.time()
        for state, pending in list(self.authorization_resources.items()):
            if pending["expires_at"] < now:
                self.authorization_resources.pop(state, None)
                self.state_mapping.pop(state, None)
        for code, pending in list(self.auth_codes.items()):
            if pending.expires_at < now:
                self.auth_codes.pop(code, None)
                self.code_credentials.pop(code, None)
        if len(self.authorization_resources) + len(self.auth_codes) >= 1000:
            raise TokenError(
                "temporarily_unavailable", "Too many pending sign-ins; retry later."
            )
        state = secrets.token_urlsafe(32)
        url = await super().authorize(
            client, params.model_copy(update={"state": state})
        )
        self.authorization_resources[state] = {
            "resource": params.resource,
            "client_state": params.state,
            "expires_at": now + 600,
        }
        return url

    async def handle_callback(self, code, state):
        pending = self.authorization_resources.pop(state, None)
        if (
            not pending
            or pending["resource"] != self.resource_url
            or pending["expires_at"] < time.time()
        ):
            raise TokenError(
                "invalid_grant", "AICQ authorization state is missing; reconnect."
            )
        redirect = await super().handle_callback(code, state)
        new_code = parse_qs(urlparse(redirect).query)["code"][0]
        auth_code = self.auth_codes[new_code]
        auth_code.resource = pending["resource"]
        self.code_credentials[new_code] = self.client_credentials.pop(
            auth_code.client_id
        )
        return construct_redirect_uri(
            str(auth_code.redirect_uri), code=new_code, state=pending["client_state"]
        )

    def _bind_tokens(self, result, resource):
        access = self.tokens[result.access_token]
        refresh = self.refresh_tokens[result.refresh_token]
        access.resource = resource
        refresh.resource = resource
        self._save_token_record(
            "access_tokens",
            result.access_token,
            access,
            self.token_grant.get(result.access_token),
        )
        self._save_token_record(
            "refresh_tokens",
            result.refresh_token,
            refresh,
            self.refresh_grant.get(result.refresh_token),
        )
        return result

    async def exchange_authorization_code(self, client, code):
        if (
            code.resource != self.resource_url
            or code.client_id != client.client_id
            or code.expires_at < time.time()
            or self.auth_codes.get(code.code) != code
        ):
            raise TokenError(
                "invalid_grant",
                "Authorization code is not for this AICQ client/resource.",
            )
        creds = self.code_credentials.pop(code.code, None)
        if creds is None:
            raise TokenError("invalid_grant", "AICQ sign-in state was lost; reconnect.")
        self.client_credentials[client.client_id] = creds
        return self._bind_tokens(
            await super().exchange_authorization_code(client, code), code.resource
        )

    async def load_access_token(self, token):
        access = await super().load_access_token(token)
        return access if access and access.resource == self.resource_url else None

    async def load_refresh_token(self, client, token):
        refresh = await super().load_refresh_token(client, token)
        return refresh if refresh and refresh.resource == self.resource_url else None

    async def exchange_refresh_token(self, client, refresh, scopes):
        if (
            refresh.resource != self.resource_url
            or refresh.client_id != client.client_id
            or self.refresh_tokens.get(refresh.token) != refresh
        ):
            raise TokenError(
                "invalid_grant", "Refresh token is not for this AICQ client/resource."
            )
        return self._bind_tokens(
            await super().exchange_refresh_token(client, refresh, scopes),
            refresh.resource,
        )

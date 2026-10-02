"""AICQ tools, standard MCP App UI, and the reused Fulcra OAuth gateway."""

import os
import json
import socket
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from mcp.server.auth.routes import create_protected_resource_routes
from mcp.server.auth.settings import ClientRegistrationOptions
from mcp.server.auth.middleware.auth_context import get_access_token
from pydantic import AnyHttpUrl

from fulcra_mcp import credentials
from fulcra_mcp.provider import OIDC_SCOPES
from fulcra_mcp.settings import settings
from fulcra_mcp.logging_config import configure_logging
from .auth import AICQOAuthProvider
from .workspace import identity, setup

configure_logging(settings.log_format)
socket.setdefaulttimeout(15)
UI_META = json.loads((Path(__file__).parent / "ui-metadata.json").read_text())
UI_URI = UI_META["global"]["ui"]["resourceUri"]
RESOURCE_URL = os.environ.get(
    "AICQ_RESOURCE_URL", settings.oidc_server_url.rstrip("/") + "/mcp"
)
provider = AICQOAuthProvider(
    issuer_url=AnyHttpUrl(settings.oidc_server_url),
    resource_url=RESOURCE_URL,
    client_registration_options=ClientRegistrationOptions(
        enabled=True, valid_scopes=OIDC_SCOPES, default_scopes=OIDC_SCOPES
    ),
    required_scopes=["openid"],
)
# The reused credential loader resolves upstream grants through this provider.
credentials.oauth_provider = provider
mcp = FastMCP(
    "AICQ",
    auth=provider,
    instructions="Use aicq_identity to inspect account setup; aicq_setup initializes missing owner resources. Contact messaging is not implemented yet.",
)


def account_client():
    if settings.fulcra_environment == "stdio" and get_access_token() is not None:
        raise ToolError(
            "HTTP tools require FULCRA_ENVIRONMENT=http; local owner credentials cannot serve HTTP clients."
        )
    return credentials.get_fulcra_object()


def account():
    return identity(account_client())


@mcp.tool(
    annotations={"title": "AICQ account", "readOnlyHint": True, "openWorldHint": True}
)
def aicq_identity() -> dict:
    """Inspect the verified account's stable owner/agent address and setup status."""
    return account()


@mcp.tool(
    annotations={
        "title": "Set up AICQ",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def aicq_setup() -> dict:
    """Create missing private AICQ profile/settings and verify persistence; reuse existing resources."""
    return setup(account_client())


@mcp.tool(title="AICQ", annotations={"readOnlyHint": True}, meta=UI_META["global"])
def aicq_open() -> dict:
    """Open the AICQ account and contacts panel."""
    return account()


@mcp.tool(
    title="Agent chat", annotations={"readOnlyHint": True}, meta=UI_META["thread"]
)
def aicq_thread() -> dict:
    """Open the AICQ panel beside this conversation."""
    return account()


@mcp.resource(UI_URI, mime_type="text/html;profile=mcp-app", meta=UI_META["resource"])
def app_ui() -> str:
    path = Path(__file__).with_name("app.html")
    if not path.is_file():
        raise ToolError(
            "Build the MCP App UI before opening AICQ: npm run build --prefix mcp/ui"
        )
    return path.read_text()


mcp_asgi = mcp.http_app(path="/", stateless_http=True, json_response=True)
app = FastAPI(lifespan=mcp_asgi.lifespan)
for route in create_protected_resource_routes(
    resource_url=AnyHttpUrl(RESOURCE_URL),
    authorization_servers=[provider.issuer_url],
    scopes_supported=OIDC_SCOPES,
):
    app.router.routes.append(route)


@app.get("/callback")
async def callback(request: Request):
    code, state = request.query_params.get("code"), request.query_params.get("state")
    if not code or not state:
        raise HTTPException(400, "Missing code or state")
    try:
        return RedirectResponse(
            await provider.handle_callback(code, state), status_code=302
        )
    except Exception:
        # Keep authorization codes and upstream errors out of the response/logs.
        raise HTTPException(
            400, "Account linking failed; reconnect and try again."
        ) from None


# Route rewriting for slashless MCP, without changing discovery or OAuth routes.
class MCPPathMiddleware:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http" and scope["path"] == "/mcp":
            scope = dict(scope, path="/mcp/")
        await self.wrapped(scope, receive, send)


app.add_middleware(MCPPathMiddleware)
app.mount("/mcp", mcp_asgi)
app.mount("/", mcp_asgi)


def main():
    os.umask(0o077)
    if settings.fulcra_environment == "stdio":
        mcp.run()
    else:
        settings.state_path.mkdir(parents=True, exist_ok=True, mode=0o700)
        uvicorn.run(app, host="127.0.0.1", port=settings.port, access_log=False)


if __name__ == "__main__":
    main()

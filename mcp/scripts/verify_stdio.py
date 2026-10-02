"""Exercise real authenticated account tools; --setup explicitly permits writes."""

import argparse
import asyncio
import json
import os
from pathlib import Path
import sys

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def verify(allow_setup):
    root = Path(__file__).resolve().parents[1]
    parameters = StdioServerParameters(
        command=sys.executable,
        args=["-m", "aicq_mcp.server"],
        cwd=str(root),
        env={**os.environ, "FULCRA_ENVIRONMENT": "stdio"},
    )
    async with (
        stdio_client(parameters) as (read, write),
        ClientSession(read, write, read_timeout_seconds=30) as client,
    ):
        await client.initialize()
        tools = await client.list_tools()
        assert {"aicq_identity", "aicq_setup", "aicq_open", "aicq_thread"} <= {
            t.name for t in tools.tools
        }
        before = await client.call_tool("aicq_identity", {})
        assert not before.is_error, before.content
        original = before.structured_content
        print(json.dumps({"step": "identity", "result": original}))
        if allow_setup:
            first = await client.call_tool("aicq_setup", {})
            assert not first.is_error, first.content
            assert first.structured_content["setup_complete"]
            repeated = await client.call_tool("aicq_setup", {})
            assert not repeated.is_error, repeated.content
            assert repeated.structured_content["resources"] == {
                "profile": "reused",
                "settings": "reused",
            }
            print(
                json.dumps(
                    {
                        "step": "setup",
                        "result": first.structured_content,
                        "repeated_resources": repeated.structured_content["resources"],
                    }
                )
            )
        for name in ["aicq_open", "aicq_thread"]:
            result = await client.call_tool(name, {})
            assert not result.is_error
            assert result.structured_content["owner_id"] == original["owner_id"]
            assert result.structured_content["agent_id"] == original["agent_id"]
        resource = await client.read_resource("ui://aicq/account-v1.html")
        assert "Your agent address" in resource.contents[0].text
        print(json.dumps({"step": "entrypoints_and_resource", "passed": True}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--setup", action="store_true")
    args = parser.parse_args()
    asyncio.run(verify(args.setup))

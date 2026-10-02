#!/usr/bin/env python3
"""Create a portable development bundle after building the MCP App UI."""

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
required = [
    "plugin.json",
    "mcp.json",
    "mcp/pyproject.toml",
    "mcp/uv.lock",
    "mcp/aicq_mcp/app.html",
]
for name in required:
    if not (root / name).is_file():
        raise SystemExit(f"Missing {name}; build the UI before packaging")
files = [root / name for name in required]
files += sorted((root / "skills").rglob("*.md"))
files += sorted((root / "mcp/aicq_mcp").glob("*.py"))
files += sorted((root / "mcp/aicq_mcp").glob("*.json"))
files += [root / "docs/mcp-development.md", root / "mcp/scripts/verify_stdio.py"]
output = root / ".local/aicq-development-plugin.zip"
output.parent.mkdir(exist_ok=True)
with ZipFile(output, "w", ZIP_DEFLATED) as bundle:
    for path in files:
        bundle.write(path, path.relative_to(root))
print(
    f"{output}: {len(files)} files; no local credentials, state, dependencies, or workspace history"
)

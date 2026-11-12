#!/usr/bin/env python3
"""Write the portable Agent Plugins 1.0 files next to each Codex plugin.

    python3 scripts/emit_portable.py          # write codex/<plugin>/plugin.json and mcp.json
    python3 scripts/emit_portable.py --check  # fail if they are out of date

Codex reads .codex-plugin/plugin.json and .mcp.json. Other apps that support the open
Agent Plugins standard (Cursor, GitHub Copilot, VS Code, Kiro and more) read a root
plugin.json and mcp.json that declare the 1.0.0 schemas. Both are derived from the Codex
files, so the Codex files stay the single source.
"""
import json, pathlib, sys

BASE = "https://agent-plugins.org/schemas/1.0.0/"
NEUTRAL = {"with ChatGPT": "with your AI assistant", "Let ChatGPT": "Let your AI assistant"}
root = pathlib.Path(__file__).resolve().parent.parent
check = "--check" in sys.argv
stale = []

def emit(path, data):
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if check:
        if not path.exists() or path.read_text() != text:
            stale.append(str(path.relative_to(root)))
    else:
        path.write_text(text)

for plugin in sorted(p.parent.parent for p in (root / "codex").glob("*/.codex-plugin/plugin.json")):
    codex = json.loads((plugin / ".codex-plugin" / "plugin.json").read_text())
    desc = codex["description"]
    for old, new in NEUTRAL.items():
        desc = desc.replace(old, new)
    if "chatgpt" in desc.lower() or "claude" in desc.lower():
        sys.exit(f"{plugin.name}: portable description still names an app: {desc}")
    emit(plugin / "plugin.json", {
        "$schema": BASE + "plugin.schema.json",
        "name": codex["name"],
        "version": codex["version"],
        "description": desc,
        "author": codex["author"],
        "homepage": codex["homepage"],
        "repository": codex["repository"],
        "license": codex["license"],
        "keywords": codex["keywords"],
    })
    servers = json.loads((plugin / ".mcp.json").read_text())["mcpServers"]
    emit(plugin / "mcp.json", {
        "$schema": BASE + "mcp.schema.json",
        "mcpServers": {
            name: {"type": s.get("transport", "stdio"), "command": s["command"],
                   **({"args": s["args"]} if "args" in s else {}),
                   **({"env": s["env"]} if s.get("env") else {})}
            for name, s in servers.items()
        },
    })

if stale:
    sys.exit("Out of date, run scripts/emit_portable.py: " + ", ".join(stale))
print("checked" if check else "written")

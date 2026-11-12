#!/usr/bin/env python3
"""Build dist/<plugin>-chatgpt-plugin.zip: a marketplace folder holding one Codex plugin.

    python3 scripts/build_chatgpt_zip.py <plugin> "<Display Name>"

ChatGPT and Codex install only from a marketplace, never from an uploaded file. So the
ChatGPT download of a plugin is a folder with .agents/plugins/marketplace.json beside the
plugin. Each zip names its own marketplace (ae5vg-<plugin>), so a user can add both.
"""
import json, pathlib, shutil, sys, zipfile

plugin, display = sys.argv[1], sys.argv[2]
root = pathlib.Path(__file__).resolve().parent.parent
top = f"{plugin}-chatgpt-plugin"
stage = root / "stage" / top
if stage.exists():
    shutil.rmtree(stage)
shutil.copytree(root / "codex" / plugin, stage / plugin)
(stage / ".agents" / "plugins").mkdir(parents=True)
(stage / ".agents" / "plugins" / "marketplace.json").write_text(json.dumps({
    "name": f"ae5vg-{plugin}",
    "interface": {"displayName": f"AE5VG {display}"},
    "plugins": [{
        "name": plugin,
        "source": {"source": "local", "path": f"./{plugin}"},
        "policy": {"installation": "AVAILABLE"},
        "category": "Productivity",
    }],
}, indent=2) + "\n")
(stage / "README.txt").write_text(
    f"{display} plugin for ChatGPT, Codex and others, by Stefan Brunner (AE5VG).\n\n"
    f"1. Move this folder somewhere permanent, for example your home folder.\n"
    f"2. In a terminal: codex plugin marketplace add ~/{top}\n"
    f"3. In the ChatGPT desktop app, open Plugins and install {display}.\n\n"
    f"Other apps that support the open Agent Plugins standard, such as Cursor,\n"
    f"GitHub Copilot and VS Code, install the {plugin} folder inside this one.\n\n"
    f"Needs uv (https://docs.astral.sh/uv/). More: https://ae5vg.com\n")
dist = root / "dist"
dist.mkdir(exist_ok=True)
out = dist / f"{top}.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(stage.rglob("*")):
        if f.is_file() and f.name != ".DS_Store":
            z.write(f, f.relative_to(stage.parent))
print(out.name, out.stat().st_size)

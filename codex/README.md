# Codex versions of the plugins

These folders hold the ChatGPT and Codex versions of the two plugins. Each folder also carries a portable `plugin.json` and `mcp.json` in the open Agent Plugins 1.0 format, so other apps that support it can install the same folder. `scripts/emit_portable.py` writes them from the Codex files. They use the same skills and the same servers, pinned to the same release commits, as the Claude versions in `plugins/`.

Add the marketplace and install from the Plugins Directory in the ChatGPT desktop app:

```
codex plugin marketplace add sbrunner-atx/ae5vg-plugins
```

Without GitHub: download `amateur-radio-chatgpt-plugin.zip` or `serial-console-chatgpt-plugin.zip` from the latest release or from https://ae5vg.com/downloads.html#plugins, unzip it into your home folder, and add the folder:

```
codex plugin marketplace add ~/amateur-radio-chatgpt-plugin
```

In Codex the servers start with their default settings: fldigi, WSJT-X and N3FJP on 127.0.0.1 at their standard ports. No callsign is set, so the radio servers stay receive-only.

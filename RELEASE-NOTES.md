Each plugin comes in two versions: one for Claude, and one for ChatGPT, Codex and others. Install a plugin to install the associated skills automatically. The server downloads include their skill files, but you have to add those yourself.

## Install in Claude

**Claude Code**

```
/plugin marketplace add sbrunner-atx/ae5vg-plugins
/plugin install amateur-radio@ae5vg
/plugin install serial-console-mcp@ae5vg
```

**Claude and Cowork:** go to Customize, Plugins, Add, Add marketplace, and enter `sbrunner-atx/ae5vg-plugins`. Or download a Claude zip below and choose Upload plugin.

## Install in ChatGPT, Codex and others

ChatGPT and Codex install plugins only from a marketplace. From GitHub:

```
codex plugin marketplace add sbrunner-atx/ae5vg-plugins
```

From a download:

- Download the ChatGPT zip and unzip it.
- Move the folder to your home folder.
- Add it, for example: `codex plugin marketplace add ~/amateur-radio-chatgpt-plugin`
- In the ChatGPT desktop app, open Plugins and install the plugin.

The ChatGPT version follows the open Agent Plugins standard, so it also installs in many other AI apps, such as Cursor, GitHub Copilot, VS Code, Kiro and Google Antigravity. In those apps, install the plugin folder inside the download, for example `amateur-radio-chatgpt-plugin/amateur-radio`.

## Requirements

- [uv](https://docs.astral.sh/uv/) on your computer.
- The servers run on your own computer: in Claude Code, Cowork, the ChatGPT desktop app and the other desktop apps. In web chat only the skills load.
- Amateur Radio stays receive-only until a callsign is set. Claude Code asks for it when you turn the plugin on. In Cowork, ChatGPT and the other apps it stays receive-only for now.

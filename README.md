# AE5VG plugins for Claude

**By Stefan Brunner, AE5VG** · [ae5vg.com](https://ae5vg.com)

> **Not working right now (13 November 2026).** In the Claude desktop app (chat and Cowork), the servers in these plugins do not start. The app skips a plugin server that asks for settings, such as the callsign, and reports `user_config_unsupported`; the plugin's connector pages have no place to enter settings. Both plugins ask for settings, so only their skills load. This is a gap in the Claude app, reported in [anthropics/claude-code](https://github.com/anthropics/claude-code/issues?q=userConfig+desktop) more than once.
>
> Until it is fixed, install the desktop extensions and the skill files from **[ae5vg.com/downloads.html](https://ae5vg.com/downloads.html)** instead. Claude Code in a terminal and the Codex versions were not tested with a radio.

Two Claude plugins:

- [**Amateur Radio**](plugins/amateur-radio): operate a station with fldigi, WSJT-X and N3FJP
- [**Serial Console**](plugins/serial-console-mcp): work any device through its serial console, from Juniper and Cisco gear to IoT gateways, instruments and radios

To add them in Claude Code:

```
/plugin marketplace add sbrunner-atx/ae5vg-plugins
/plugin install amateur-radio@ae5vg
/plugin install serial-console-mcp@ae5vg
```

In claude.ai or Cowork, go to Customize, Plugins, Add, Add marketplace, and enter `sbrunner-atx/ae5vg-plugins`. Or download a plugin zip from the [latest release](https://github.com/sbrunner-atx/ae5vg-plugins/releases/latest) and choose Upload plugin.

In Codex:

```
codex plugin marketplace add sbrunner-atx/ae5vg-plugins
```

Then install from the Plugins Directory in the ChatGPT desktop app. Without GitHub, download `amateur-radio-chatgpt-plugin.zip` or `serial-console-chatgpt-plugin.zip` from the latest release, unzip it into your home folder and add that folder, for example `codex plugin marketplace add ~/amateur-radio-chatgpt-plugin`. The Codex versions live in `codex/`; see [codex/README.md](codex/README.md).

The skills are copied from the server repositories. `sync-skills.sh` copies them again after a change there.

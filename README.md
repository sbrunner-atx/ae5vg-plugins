# AE5VG plugins for Claude

**By Stefan Brunner, AE5VG** · [ae5vg.com](https://ae5vg.com)

Two Claude plugins:

- [**Amateur Radio**](plugins/amateur-radio): operate a station with fldigi, WSJT-X and N3FJP
- [**Serial Console**](plugins/serial-console-mcp): work any serial console, from Juniper and Cisco gear to CAT radios and rotators

To add them in Claude Code:

```
/plugin marketplace add sbrunner-atx/ae5vg-plugins
/plugin install amateur-radio@ae5vg
/plugin install serial-console-mcp@ae5vg
```

In claude.ai or Cowork, go to Customize, Plugins, Add, Add marketplace, and enter `sbrunner-atx/ae5vg-plugins`.

The skills are copied from the server repositories. `sync-skills.sh` copies them again after a change there.

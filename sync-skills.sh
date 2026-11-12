#!/bin/sh
# Copy the skills from the server repositories into the plugins.
# Run from this folder; the server repositories sit beside it.
set -e
cp -R ../fldigi-mcp/skills/fldigi-operating ../fldigi-mcp/skills/signal-hunting plugins/amateur-radio/skills/
cp -R ../n3fjp-mcp/skills/contest-operating plugins/amateur-radio/skills/
cp -R ../serial-console-mcp/skills/serial-console ../serial-console-mcp/skills/junos-operating ../serial-console-mcp/skills/ios-operating plugins/serial-console-mcp/skills/
sed -i "s|see docs/N3FJP-API.md gotchas|see the gotchas in https://github.com/sbrunner-atx/n3fjp-mcp/blob/main/docs/N3FJP-API.md|" plugins/amateur-radio/skills/contest-operating/SKILL.md
cp -R plugins/amateur-radio/skills/. codex/amateur-radio/skills/
cp -R plugins/serial-console-mcp/skills/. codex/serial-console/skills/
echo "Skills copied. Check the diff, raise the plugin version, and commit."
# The ChatGPT copies must not name Claude.
sed -i.bak "s/Claude Desktop shows each call for/The app shows each call for/" codex/serial-console/skills/serial-console/SKILL.md && rm -f codex/serial-console/skills/serial-console/SKILL.md.bak
if grep -rIl -i claude codex/amateur-radio codex/serial-console; then echo "Claude is named in the ChatGPT plugins above: fix before release."; exit 1; fi

# Amateur Radio

**By Stefan Brunner, AE5VG** · [ae5vg.com](https://ae5vg.com)

Operate an amateur radio station with Claude. This plugin connects Claude to the station software you already run:

- **fldigi**, for PSK31, RTTY, Olivia and the other digital modes ([fldigi-mcp](https://ae5vg.com/products/fldigi-mcp.html))
- **WSJT-X**, for FT8, FT4 and the other weak-signal modes ([wsjtx-mcp](https://ae5vg.com/products/wsjtx-mcp.html))
- **N3FJP**, for logging contacts in Amateur Contact Log and the N3FJP contest loggers, Field Day included ([n3fjp-mcp](https://ae5vg.com/products/n3fjp-mcp.html))

It also brings three skills that teach Claude how to operate: keying the transmitter and returning to receive after every over, finding a station worth working on the waterfall, and running a contest from CQ through the exchange to the log.

## Use it

Install the plugin, then set your callsign in its settings. Ask Claude what is on the band, to answer a CQ, or to call CQ for Field Day and log each contact.

The station stays **receive-only until you set your callsign**. The callsign is the only transmit gate, and Claude still asks before each transmission. The N3FJP server refuses any command that could wipe your whole log unless you turn that protection off yourself.

You need [uv](https://docs.astral.sh/uv/) installed, and fldigi, WSJT-X or N3FJP running with its remote control interface turned on. Each one is optional: use the servers for the programs you have. If a program runs on another computer, [mcp-host-bridge](https://ae5vg.com/products/mcp-host-bridge.html) relays it to this one.

Works in Claude Code and in Cowork on your own computer. In plain chat the skills load, but the servers do not run.

## What it runs and what it sends

The plugin starts three local MCP servers with `uvx`, which downloads the pinned packages `fldigi-mcp`, `wsjtx-mcp` and `n3fjp-mcp` from PyPI. The servers talk only to fldigi (XML-RPC, port 7362), WSJT-X (UDP, port 2237) and N3FJP (TCP, port 1100) at the addresses in the settings, 127.0.0.1 by default. They send nothing anywhere else and collect no data.

## Support

Questions and bug reports: [GitHub issues](https://github.com/sbrunner-atx/ae5vg-plugins/issues). Documentation: [ae5vg.com](https://ae5vg.com).

N3FJP is used by name with permission. This project is not affiliated with, endorsed by or supported by N3FJP Software (Affirmatech), and support goes to this project, not to N3FJP.

## License

MIT. The servers have their own licenses: fldigi-mcp is GPL-3.0-or-later, wsjtx-mcp and n3fjp-mcp are MIT.

# Serial Console

**By Stefan Brunner** · [Project page](https://ae5vg.com/products/serial-console-mcp.html)

Let Claude work any device through the serial console it already has:

- Juniper (Junos) and Cisco (IOS, IOS-XE and similar) routers and switches
- IoT gateways, alarm and control panels, lab instruments, microcontrollers and embedded boards
- Radios with a serial control port: Icom CI-V, and Kenwood, Yaesu and Elecraft CAT
- GS-232 antenna rotators
- Anything else that speaks over RS-232, a USB serial adapter or a UART, in raw, ANSI or VT100 mode

The plugin includes skills for working a Junos console, an IOS console and serial devices in general: reading the mode from the prompt, moving between modes, and leaving the device as it was found.

## Use it

Plug in your USB-to-serial adapter, install the plugin, and ask Claude to list the serial ports and connect to the device. Turn on **Read-only mode** in the settings to allow only show, display and read commands.

You need [uv](https://docs.astral.sh/uv/) installed. Works in Claude Code and in Cowork on your own computer. In plain chat the skills load, but the server does not run.

## What it runs and what it sends

The plugin starts one local MCP server with uv: `serial-console-mcp` comes from its GitHub repository at a fixed release commit, its dependencies from PyPI, and a lock file in the plugin fixes every file installed. The server talks only to the serial ports on your computer that you ask it to open. It sends nothing over the network and collects no data.

## Support

Questions and bug reports: [GitHub issues](https://github.com/sbrunner-atx/serial-console-mcp/issues). Field Guide and documentation: [ae5vg.com](https://ae5vg.com/products/serial-console-mcp.html).

## License

MIT.

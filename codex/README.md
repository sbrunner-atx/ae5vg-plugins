# Codex versions of the plugins

These folders hold the Codex (OpenAI) versions of the two plugins. They use the same skills and the same servers, pinned to the same release commits, as the Claude versions in `plugins/`.

Add the marketplace and install from the Plugins Directory in the ChatGPT desktop app:

```
codex plugin marketplace add sbrunner-atx/ae5vg-plugins
```

Without GitHub: download `ae5vg-marketplace.zip` from the latest release or from https://ae5vg.com/downloads.html#plugins, unzip it, and add the folder:

```
codex plugin marketplace add ~/Downloads/ae5vg-marketplace
```

In Codex the servers start with their default settings: fldigi, WSJT-X and N3FJP on 127.0.0.1 at their standard ports. No callsign is set, so the radio servers stay receive-only.

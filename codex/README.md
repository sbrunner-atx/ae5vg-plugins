# Codex versions of the plugins

These folders hold the Codex (OpenAI) versions of the two plugins. They use the same skills and the same servers, pinned to the same release commits, as the Claude versions in `plugins/`.

Add the marketplace and install from the Plugins Directory in the ChatGPT desktop app:

```
codex plugin marketplace add sbrunner-atx/ae5vg-plugins
```

In Codex the servers start with their default settings: fldigi, WSJT-X and N3FJP on 127.0.0.1 at their standard ports. No callsign is set, so the radio servers stay receive-only.

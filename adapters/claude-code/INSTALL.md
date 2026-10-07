# SpineMe for claude-code

## Skill adapter (no plugin manager required)

1. Extract `spineme-claude-code-adapter.zip` into a temporary folder. Enable hidden-file
   display if your file browser hides dot-prefixed folders.
2. Copy its `.claude/skills/spineme` folder into `.claude/skills/spineme` in the project
   you want to audit. Create the parent folders if necessary. Compare existing
   SpineMe files before replacing them; preserve unrelated files and settings.
3. Start a fresh host session in that project and confirm SpineMe is discovered.
4. Invoke `/spineme` and request a full audit with compact output.

The archive's `INSTALL.md` is for you; it does not need to go into the project.
The source adapter recipe builds the correct folder layout; no installer runs
and no app settings change automatically.

[Host documentation](https://code.claude.com/docs/en/skills). Paths are project-relative. Personal/global and
remote/cloud installations may differ. Documentation checked 2026-10-08.

## Plugin option

Extract `spineme-claude-code-plugin.zip`. From your target project's terminal, start:

```bash
claude --plugin-dir /absolute/path/to/extracted/spineme
```

Replace the example path. Select the plugin's skill in the slash menu (normally
`/spineme:spineme`) and request a compact audit. This session-local development
load does not require a marketplace. For ongoing distribution follow
[Claude's plugin guide](https://code.claude.com/docs/en/plugins).
Use either the plugin or the direct skill adapter, not both.

## Model choices and verification

The host's selected model runs the audit. The core's Economy/Balanced/Advanced
profiles remain vendor-neutral; provide your own available-model mapping if desired.
This adapter sets no model and cannot switch one.

Check discovery, read-only behavior, scope limits, evidence accuracy, and verification
against a small disposable project before relying on it. Packaging has been checked
locally; this host's runtime loading and audit behavior have not been tested here.

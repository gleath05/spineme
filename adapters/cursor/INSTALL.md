# SpineMe for cursor

## Skill adapter (no plugin manager required)

1. Extract `spineme-cursor-adapter.zip` into a temporary folder. Enable hidden-file
   display if your file browser hides dot-prefixed folders.
2. Copy its `.cursor/skills/spineme` folder into `.cursor/skills/spineme` in the project
   you want to audit. Create the parent folders if necessary. Compare existing
   SpineMe files before replacing them; preserve unrelated files and settings.
3. Start a fresh host session in that project and confirm SpineMe is discovered.
4. Invoke `Use SpineMe. Audit this project with compact output.` and request a full audit with compact output.

The archive's `INSTALL.md` is for you; it does not need to go into the project.
The source adapter recipe builds the correct folder layout; no installer runs
and no app settings change automatically.

[Host documentation](https://cursor.com/docs/skills). Paths are project-relative. Personal/global and
remote/cloud installations may differ. Documentation checked 2026-10-08.

## Plugin option

Extract `spineme-cursor-plugin.zip`, then copy its `spineme` folder to
`~/.cursor/plugins/local/spineme`. Compare with any existing folder before copying.
Restart Cursor or run Developer: Reload Window, then confirm SpineMe appears in
Customize → Skills. This is a local development install, not marketplace publication.
Use a real copied folder; Cursor restricts symlink targets for local plugins.
See [Cursor plugins](https://cursor.com/docs/plugins). Use the plugin or adapter,
not both.

## Model choices and verification

The host's selected model runs the audit. The core's Economy/Balanced/Advanced
profiles remain vendor-neutral; provide your own available-model mapping if desired.
This adapter sets no model and cannot switch one.

Check discovery, read-only behavior, scope limits, evidence accuracy, and verification
against a small disposable project before relying on it. Packaging has been checked
locally; this host's runtime loading and audit behavior have not been tested here.

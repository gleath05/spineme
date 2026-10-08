#!/usr/bin/env python3
"""Build self-contained SpineMe ZIPs from one canonical skill; Python stdlib only."""
import hashlib
import json
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'

def archive(name, files):
    license_bytes = (ROOT / 'LICENSE').read_bytes()
    for path in list(files):
        if path.endswith('/SKILL.md'):
            files[str(PurePosixPath(path).parent / 'LICENSE')] = license_bytes
    files['spineme/LICENSE' if any(p.startswith('spineme/') for p in files) else 'LICENSE'] = license_bytes
    target = DIST / (name + '.zip')
    with ZipFile(target, 'w') as z:
        for path, data in sorted(files.items()):
            info = ZipInfo(path, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    with ZipFile(target) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(set(z.namelist()))
        for path in z.namelist():
            assert not PurePosixPath(path).is_absolute() and '..' not in PurePosixPath(path).parts
            assert z.read(path) == files[path], path
    return target

def build():
    DIST.mkdir(exist_ok=True)
    core = (ROOT / 'skills/spineme/SKILL.md').read_bytes()
    metadata = (ROOT / 'adapters/codex/openai.yaml').read_bytes()
    manifests = {}
    for name, file in [('portable', 'plugin.json'), ('claude', '.claude-plugin/plugin.json')]:
        data = (ROOT / file).read_bytes()
        obj = json.loads(data)
        assert obj['name'] == 'spineme' and obj['version'] == '0.1.2'
        manifests[name] = data
    written = []
    for config in sorted((ROOT / 'adapters').glob('*/adapter.json')):
        cfg = json.loads(config.read_text())
        host = config.parent.name
        rel = PurePosixPath(cfg['project_directory']) / 'spineme'
        assert not rel.is_absolute() and '..' not in rel.parts
        files = {str(rel / 'SKILL.md'): core,
                 'INSTALL.md': (config.parent / 'INSTALL.md').read_bytes()}
        if host == 'codex':
            files[str(rel / 'agents/openai.yaml')] = metadata
            files[str(rel / 'assets/spineme-icon.svg')] = (ROOT / 'assets/spineme-icon.svg').read_bytes()
        written.append(archive('spineme-' + host + '-adapter', files))
    for host in ('codex', 'cursor', 'claude-code'):
        files = {'spineme/skills/spineme/SKILL.md': core,
                 'spineme/INSTALL.md': (ROOT / 'adapters' / host / 'INSTALL.md').read_bytes()}
        if host == 'claude-code':
            files['spineme/.claude-plugin/plugin.json'] = manifests['claude']
        else:
            files['spineme/plugin.json'] = manifests['portable']
        if host in ('codex', 'cursor'):
            files['spineme/.codex-plugin/plugin.json'] = (ROOT / '.codex-plugin/plugin.json').read_bytes()
            files['spineme/assets/spineme-icon.svg'] = (ROOT / 'assets/spineme-icon.svg').read_bytes()
        if host == 'codex':
            files['spineme/skills/spineme/agents/openai.yaml'] = metadata
            files['spineme/skills/spineme/assets/spineme-icon.svg'] = (ROOT / 'assets/spineme-icon.svg').read_bytes()
        written.append(archive('spineme-' + host + '-plugin', files))
    written.append(archive('spineme-chat', {
        'spineme/SKILL.md': core,
        'spineme/START-HERE.md': (ROOT / 'adapters/chat/INSTALL.md').read_bytes()}))
    # Check every archive carries the exact canonical audit, independent of wrapper.
    for path in written:
        with ZipFile(path) as z:
            skills = [n for n in z.namelist() if n.endswith('/SKILL.md')]
            assert len(skills) == 1 and z.read(skills[0]) == core
    checksums = ''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n'
                        for p in sorted(written))
    (DIST / 'SHA256SUMS.txt').write_text(checksums)
    print(f'Built and checked {len(written)} archives from one canonical skill.')

if __name__ == '__main__':
    build()

#!/usr/bin/env python3
"""Offline package checks; does not test agent behavior or install plugins."""
import hashlib
import json
import re
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile
from build import ROOT, DIST, build

def hashes():
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in DIST.glob('*.zip')}

def main():
    build()
    first = hashes()
    build()
    assert hashes() == first, 'Build is not reproducible'
    core = (ROOT / 'skills/spineme/SKILL.md').read_bytes()
    assert core.startswith(b'---\nname: spineme\n')
    assert b'description:' in core.split(b'---', 2)[1]
    with tempfile.TemporaryDirectory() as tmp:
        for archive in DIST.glob('*.zip'):
            with ZipFile(archive) as z:
                assert z.testzip() is None
                z.extractall(Path(tmp) / archive.stem)
        extracted = list(Path(tmp).rglob('SKILL.md'))
        assert len(extracted) == 10
        assert all(p.read_bytes() == core for p in extracted)
    for p in ROOT.rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts:
            continue
        if p.suffix == '.json':
            json.loads(p.read_text())
        if p.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
                if '://' not in target and not target.startswith('#'):
                    assert (p.parent / target.split('#')[0]).exists(), (p, target)
    marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    assert marketplace['plugins'][0]['source'] == './'
    assert (ROOT / '.claude-plugin/plugin.json').is_file()
    template = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    assert template['plugins'][0]['source']['source'] == 'url'
    ET.parse(ROOT / 'assets/spineme-banner.svg')
    ET.parse(ROOT / 'assets/spineme-icon.svg')
    manifest = json.loads((ROOT / 'plugin.json').read_text())
    interface = manifest['extensions']['com.openai']['interface']
    assert interface['displayName'] == 'SpineMe'
    assert len(interface['defaultPrompt']) == 3
    for key in ('logo', 'composerIcon'):
        assert (ROOT / interface[key]).is_file()
    for archive in DIST.glob('*.zip'):
        with ZipFile(archive) as z:
            assert any(n.endswith('LICENSE') for n in z.namelist())
            for name in z.namelist():
                if name == 'spineme/plugin.json':
                    config = json.loads(z.read(name))
                    for key in ('logo', 'composerIcon'):
                        asset = config['extensions']['com.openai']['interface'][key]
                        assert 'spineme/' + (asset[2:] if asset.startswith('./') else asset) in z.namelist()

    print('PASS: archive extraction, canonical skill parity, reproducibility, JSON, local links, SVG.')
    print('Not tested: host plugin discovery, audit behavior, marketplace installation, hosted CI.')

if __name__ == '__main__':
    main()

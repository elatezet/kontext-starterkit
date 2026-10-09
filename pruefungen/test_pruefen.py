"""Regressionstests mit echten Dateien in einem temporären Ordner."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from pruefen import check

HEADER = '---\nstatus: entwurf\ngeprueft_am: offen\n---\n'


class CheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        return path

    def test_missing_frontmatter(self):
        self.write('ohne.md', '# Ohne Metadaten\n')
        found, _ = check(self.root)
        self.assertEqual(len(found), 1)
        self.assertIn('ohne.md:1: Frontmatter fehlt', found[0])

    def test_missing_required_fields(self):
        self.write('leer.md', '---\ntitel: Leer\n---\n')
        found, _ = check(self.root)
        self.assertEqual(len(found), 2)
        self.assertIn('leer.md:3: Pflichtfeld fehlt: status', found)
        self.assertIn('leer.md:3: Pflichtfeld fehlt: geprueft_am', found)

    def test_broken_link_line(self):
        self.write('projekt.md', HEADER + '\n[Fehlt](fehlt.md)\n')
        found, _ = check(self.root)
        self.assertEqual(found, ['projekt.md:6: Markdown-Ziel fehlt: fehlt.md'])

    def test_valid_relative_links_and_open(self):
        self.write('kontext/basis.md', HEADER)
        self.write('projekt.md', HEADER + '[Basis](kontext/basis.md#abschnitt)\n[Andere](https://example.invalid/extern.md)\n')
        self.assertEqual(check(self.root), ([], 2))

    def test_valid_date_and_reference_links(self):
        self.write('ziel.md', HEADER.replace('geprueft_am: offen', 'geprueft_am: "2024-02-29"'))
        self.write('a.md', HEADER + '[Ziel][basis]\n[basis]: ziel.md\n')
        self.assertEqual(check(self.root), ([], 2))

    def test_invalid_status_date_and_duplicate(self):
        self.write('a.md', '---\nstatus: fertig\ngeprueft_am: 2025-02-29\nstatus: aktiv\n---\n')
        found, _ = check(self.root)
        self.assertEqual(len(found), 3)
        self.assertTrue(any('a.md:2: Ungültiger status' in f for f in found))
        self.assertTrue(any('a.md:3: geprueft_am erwartet' in f for f in found))
        self.assertTrue(any('a.md:4: Doppelter Schlüssel' in f for f in found))

    def test_code_examples_ignored(self):
        self.write('a.md', HEADER + '```md\n[Falsch](fehlt.md)\n```\n`[Falsch](fehlt.md)`\n~~~md\n[Falsch](fehlt.md)\n~~~\n')
        self.assertEqual(check(self.root), ([], 1))

    def test_encoded_path_and_broken_reference(self):
        self.write('ziel name.md', HEADER)
        self.write('a.md', HEADER + '[Ziel](ziel%20name.md)\n[Fehlt][x]\n[x]: weg.md\n[Undefiniert][y]\n')
        found, _ = check(self.root)
        self.assertEqual(found, ['a.md:7: Markdown-Ziel fehlt: weg.md', 'a.md:8: Linkreferenz nicht definiert: y'])

    def test_escape_and_absolute_path(self):
        self.write('a.md', HEADER + '[Raus](../weg.md)\n[Absolut](/tmp/weg.md)\n')
        found, _ = check(self.root)
        self.assertEqual(len(found), 2)
        self.assertIn('a.md:5: Markdown-Link verlässt', found[0])
        self.assertIn('a.md:6: Markdown-Link muss relativ', found[1])

    def test_empty_and_unclosed(self):
        self.assertEqual(len(check(self.root)[0]), 1)
        self.write('a.md', '---\nstatus: entwurf\n')
        self.assertIn('a.md:1: Frontmatter nicht geschlossen', check(self.root)[0])

    def test_cli_exit_codes(self):
        script = Path(__file__).with_name('pruefen.py')
        path = self.write('a.md', HEADER)
        result = subprocess.run([sys.executable, str(script), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        path.write_text(HEADER + '[Fehlt](weg.md)\n', encoding='utf-8')
        result = subprocess.run([sys.executable, str(script), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('a.md:5: Markdown-Ziel fehlt: weg.md', result.stdout)


if __name__ == '__main__':
    unittest.main()

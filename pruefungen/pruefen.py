"""Prüft das dokumentierte Markdown-Teilformat, ausschließlich mit der Standardbibliothek."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

STATUSES = {'offen', 'entwurf', 'aktiv', 'erledigt', 'archiviert'}
FIELD = re.compile(r'^([a-z][a-z0-9_]*):\s*(.*?)\s*$')
INLINE = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s()]+)(?:\s+[\"\'][^\n]*?[\"\'])?\s*\)')
REFERENCE = re.compile(r'^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)')
REF_USE = re.compile(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]')


def visible_lines(lines: list[str]):
    """Behält Zeilennummern bei; überspringt Codezäune und maskiert Inline-Code."""
    fence = None
    for number, line in enumerate(lines, 1):
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if fence:
            if re.match(r'^\s{0,3}' + re.escape(fence[0]) + '{' + str(fence[1]) + r',}\s*$', line):
                fence = None
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]))
            continue
        # Gleiche Backtick-Länge öffnet und schließt einen Inline-Codeabschnitt.
        line = re.sub(r'(`+)(?!`)(.*?)(?<!`)\1(?!`)', lambda m: ' ' * len(m[0]), line)
        yield number, line


def check(root: Path) -> tuple[list[str], int]:
    root = root.resolve()
    findings: list[str] = []
    if not root.is_dir():
        return [f'{root}:1: Prüfpfad ist kein Ordner'], 0
    paths = sorted(p for p in root.rglob('*.md') if not any(part.startswith('.') for part in p.relative_to(root).parts))
    if not paths:
        return [f'{root}:1: Keine Markdown-Dateien gefunden'], 0
    for path in paths:
        label = path.relative_to(root).as_posix()

        def report(line: int, message: str):
            findings.append(f'{label}:{line}: {message}')

        if not path.resolve().is_relative_to(root):
            report(1, 'Dateiverweis verlässt den Prüfbestand')
            continue
        try:
            lines = path.read_text(encoding='utf-8').splitlines()
        except (OSError, UnicodeError) as error:
            report(1, f'Datei nicht als UTF-8 lesbar: {error}')
            continue
        fields: dict[str, tuple[str, int]] = {}
        end = 0
        if not lines or lines[0] != '---':
            report(1, 'Frontmatter fehlt (erste Zeile muss --- sein)')
        else:
            end = next((i for i in range(1, len(lines)) if lines[i] == '---'), 0)
            if not end:
                report(1, 'Frontmatter nicht geschlossen')
            else:
                for i in range(1, end):
                    if not lines[i].strip() or lines[i].lstrip().startswith('#'):
                        continue
                    match = FIELD.fullmatch(lines[i])
                    if not match:
                        report(i + 1, 'Nur flache Schlüssel mit einfachen Textwerten erlaubt')
                        continue
                    key, value = match.groups()
                    if len(value) >= 2 and value[0] == value[-1] and value[0] in '\"\'':
                        value = value[1:-1]
                    if key in fields:
                        report(i + 1, f'Doppelter Schlüssel: {key}')
                    else:
                        fields[key] = (value, i + 1)
                for key in ('status', 'geprueft_am'):
                    if key not in fields:
                        report(end + 1, f'Pflichtfeld fehlt: {key}')
                if 'status' in fields:
                    value, number = fields['status']
                    if value not in STATUSES:
                        report(number, f'Ungültiger status: {value!r}')
                if 'geprueft_am' in fields:
                    value, number = fields['geprueft_am']
                    if value != 'offen':
                        try:
                            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                                raise ValueError
                            date.fromisoformat(value)
                        except ValueError:
                            report(number, 'geprueft_am erwartet offen oder ein gültiges Datum JJJJ-MM-TT')
        body = [(n, line) for n, line in visible_lines(lines) if n > end + 1 or end == 0]
        definitions: dict[str, str] = {}

        def check_target(target: str, number: int):
            target = target.removeprefix('<').removesuffix('>')
            try:
                url = urlsplit(target)
            except ValueError:
                report(number, f'Ungültiges Linkziel: {target}')
                return
            if url.scheme or url.netloc or not url.path:
                return
            decoded = unquote(url.path)
            if not decoded.lower().endswith('.md'):
                return
            if decoded.startswith('/'):
                report(number, f'Markdown-Link muss relativ sein: {target}')
                return
            dest = (path.parent / decoded).resolve()
            if not dest.is_relative_to(root):
                report(number, f'Markdown-Link verlässt den Prüfbestand: {target}')
            elif not dest.is_file():
                report(number, f'Markdown-Ziel fehlt: {target}')

        for number, line in body:
            definition = REFERENCE.match(line)
            if definition:
                key = ' '.join(definition[1].lower().split())
                definitions[key] = definition[2]
                check_target(definition[2], number)
                continue
            for match in INLINE.finditer(line):
                check_target(match[1], number)
        for number, line in body:
            if REFERENCE.match(line):
                continue
            for match in REF_USE.finditer(line):
                key = ' '.join((match[2] or match[1]).lower().split())
                if key not in definitions:
                    report(number, f'Linkreferenz nicht definiert: {key}')
    return findings, len(paths)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ordner', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    findings, count = check(args.ordner)
    for finding in findings:
        print(finding)
    if findings:
        print(f'{len(findings)} Fundstellen in {count} Markdown-Dateien.')
        return 1
    print(f'OK: {count} Markdown-Dateien geprüft; keine Strukturfehler gefunden.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

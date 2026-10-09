---
status: entwurf
geprueft_am: offen
---

# Strukturprüfung

Öffnet ein Terminal im Kit-Ordner. Python 3.10 oder neuer genügt; der Prüfer nutzt ausschließlich die Standardbibliothek.

```sh
python3 pruefungen/pruefen.py .
python3 -B -m unittest discover -s pruefungen -p 'test_*.py' -v
```

`pruefen.py` liest alle `.md`-Dateien unterhalb des Prüfpfads, einschließlich der Vorlagen und Beispiele. Versteckte Ordner und Dateien sind ausgenommen. Ohne Pfadargument prüft es den Kit-Ordner, in dem das Skript liegt. Es schreibt keine Dateien. Ein leerer oder ungültiger Prüfpfad gilt als Fehler.

## Metadaten

Jede Datei braucht Frontmatter in der ersten Zeile. Der Prüfer verlangt `status` und `geprueft_am`, meldet doppelte Schlüssel und kontrolliert die erlaubten Statuswerte. Das Prüfdatum muss `offen` oder ein gültiges Kalenderdatum im Format `JJJJ-MM-TT` sein. Fehlende Felder meldet er an der schließenden Frontmatter-Zeile. Falsche Werte meldet er an ihrer eigenen Zeile.

Das Kit verwendet einen flachen Ausschnitt aus YAML: ein einfacher Textwert pro Schlüssel. Verschachtelte Daten, mehrzeilige Werte und Kommentare hinter Werten gehören nicht zu diesem Format. Das Skript ist kein allgemeiner YAML-Parser. Es prüft bei zusätzlichen Schlüsseln lediglich die Zeilenform.

## Links und Fundstellen

Der Prüfer kontrolliert relative `.md`-Ziele in Inline-Links und Linkreferenz-Definitionen. Er meldet undefinierte explizite Linkreferenzen. Er berücksichtigt URL-kodierte Pfade sowie Dateilinks mit Fragmenten oder Titel. Markdown-Ziele müssen vorhandene Dateien innerhalb des Prüfbestands sein. Ein absoluter lokaler Markdown-Link gilt als Fehler. Codezäune und Inline-Code sind ausgenommen.

Jeder Fund erscheint als `datei.md:zeile: meldung`. Die Zeile stammt aus der tatsächlichen Datei. Bei mindestens einem Fund endet der Prüfer mit Exitcode 1, sonst mit Exitcode 0. Korrigiert den Fund im Editor und startet denselben Befehl erneut. Die abschließende OK-Meldung gilt nur für den gerade gelesenen Stand.

Die Tests erzeugen ihre gültigen und fehlerhaften Dokumente mit `tempfile` außerhalb des Kits und entfernen sie anschließend. Sie prüfen unter anderem Pflichtfelder, Kalenderdaten, relative Links und beide Exitcodes. Ihre absichtlichen Fehler sind keine Befunde im Kit. Für eine Aufnahme des tatsächlichen Bestands verwendet ihr den ersten Befehl; inszeniert keine Testfälle als reale Funde.

## Grenzen

Der Prüfer prüft die Struktur. Ob Aussagen wahr sind, müsst ihr inhaltlich prüfen. Er prüft weder Fakten noch Rechte, Inhalt, Vollständigkeit oder Modellantworten. Er bestätigt kein Datum einer menschlichen Prüfung. Auch Links auf falsche, aber vorhandene Dateien können bestehen.

Externe URLs werden nicht abgerufen. Überschriftenanker, Bilder und andere Dateitypen werden nicht auf Existenz geprüft. Obsidian-Wikilinks, HTML-Links, verkürzte Referenzen und Markdown-Sonderfälle wie verschachtelte Linkbeschriftungen werden nicht ausgewertet. Verwendet deshalb die einfachen relativen Markdown-Links aus den Vorlagen. Obsidian kann mehr Syntax darstellen, als dieser kleine Prüfer versteht.

Die Interviews müssen im gewählten Werkzeug gesondert erprobt werden. Die Tests ersetzen weder einen solchen Lauf noch eine Nutzerprüfung. Eine Vorschau oder spätere Veröffentlichung gehört ebenfalls nicht zum Prüfumfang.

---
status: entwurf
geprueft_am: offen
---

# Kontext-Starterkit

Mit diesem Starterkit baut ihr einen eigenen Kontextbestand auf. Ihr beginnt mit einem Projekt oder eurem Fachwissen. Ein Interview fragt einzeln nach und erzeugt daraus zusammenhängende Markdown-Dateien. Das Kit ist ein redaktioneller Vorschlag; Veröffentlichung und Lizenzfreigabe stehen aus.

## Ordner öffnen

Kopiert den gesamten Ordner `starterkit` an euren Arbeitsort. Öffnet ihn in Obsidian über „Ordner als Vault öffnen“. Alle Verweise verwenden relative Markdown-Links. Ihr braucht keine Plugins. Alternativ öffnet ihr die Dateien in einem Texteditor und speichert sie als UTF-8 mit der Endung `.md`.

Die [Regeln mit Landkarte](regeln.md) erklären den Aufbau. Ebene 1 enthält eure Grundlagen und Methoden in `kontext/`. Ebene 2 beschreibt ein Vorhaben und seine Entscheidungen in `projekte/`. Ebene 3 hält den konkreten Auftrag in `aufgaben/` fest. Die Dateien mit `vorlage-` sind leer; das vollständig fiktive Designverzeichnis liegt getrennt in [beispiel/](beispiel/README.md).

## Wählt euren Einstieg

Für ein konkretes Vorhaben öffnet ihr das [Projektinterview](prompts/einstieg-projekt.md). Für eine wiederverwendbare Methode öffnet ihr das [Fachwissensinterview](prompts/einstieg-fachwissen.md). Beide Wege erzeugen Grundlagen, einen Projektstand, eine Entscheidungsdatei und eine Aufgabe. Beim Fachwissen kommt eine Methodendatei hinzu. Die Projektdatei hält dann knapp den ersten Anwendungskontext fest. Ist kein Beschluss nötig, steht das ausdrücklich in der Entscheidungsdatei. Unbekanntes darf ausdrücklich offen bleiben.

### Mit Dateizugriff

Öffnet eure Kopie des Kit-Ordners als Arbeitsordner im gewählten Agentenwerkzeug. Begrenzt den Dateizugriff auf diesen Ordner. Fügt den Prompt aus dem gewählten Interview ein und setzt `MODUS: DATEIEN`. Der Prompt nennt alle zu lesenden Dateien. Ein neutrales `regeln.md` wird nicht von jedem Werkzeug automatisch geladen; deshalb fordert der Prompt das Lesen ausdrücklich an.

Beantwortet jeweils die eine gestellte Frage. Sechs Kernfragen geben die Richtung vor; sobald eine erste Aufgabe bearbeitbar ist, bietet das Interview den Abschluss an. Weitere Fragen folgen nur bei entscheidenden Lücken. Bestehende Dokumente könnt ihr als freigegebene Auszüge bereitstellen. Nennt dabei die Herkunft und trennt belegte Angaben von Annahmen. Das Interview zeigt zum Schluss eine Zusammenfassung zur Bestätigung. Danach schreibt der Agent neue Dateien; vorhandene Fassungen darf er nur nach eurem ausdrücklichen Auftrag ersetzen. Kontrolliert die gespeicherten Inhalte im Editor.

### Mit Kopieren im Chat

Öffnet einen neuen Chat. Fügt zuerst den Prompt aus dem gewählten Interview ein und setzt `MODUS: CHAT`. Fügt in derselben Nachricht den vollständigen Inhalt von `regeln.md` und allen im Interview genannten Vorlagen ein. Schreibt vor jeden Dateiinhalt `DATEI: relativer/pfad.md` und danach `ENDE DATEI`. Ein Pfad allein übermittelt keinen Inhalt. Bei zu langen Nachrichten sendet ihr nummerierte Teile und schließt mit `MATERIAL VOLLSTÄNDIG` ab. Der Prompt wartet darauf, bevor er das Interview beginnt.

Nach eurer Bestätigung liefert der Chat je Datei den relativen Zielpfad und einen vollständigen Markdown-Codeblock. Legt diese Dateien im Kit-Ordner mit dem Texteditor an. Kopiert den Inhalt ohne die äußeren Codezäune, einschließlich des Dateikopfs zwischen `---`. Kontrolliert Dateiendung und Zielordner. Öffnet die gespeicherten Dateien erneut und folgt den Links. Der Chat hat eure lokalen Dateien nicht selbst gespeichert.

## Erste Aufgabe bearbeiten

Öffnet [Aufgabe bearbeiten](prompts/aufgabe-bearbeiten.md). Mit Dateizugriff nennt ihr den Pfad eurer erzeugten Aufgabe. Im Chat fügt ihr den vollständigen Inhalt der Regeln, der Aufgabe und ihrer verlinkten Grundlagen, Methode, Projektdatei und Entscheidung ein. Der Prompt nennt zuerst die verwendeten Quellen und bearbeitet dann den Auftrag. Ein offener Punkt bleibt offen, bis ihr ihn klärt.

Vergleicht das Ergebnis mit den Abnahmekriterien der Aufgabe. Prüft Aussagen und Quellen selbst. Lasst bei einem Fehler die betroffene Stelle mit Begründung überarbeiten. Wenn entscheidende Angaben fehlen, stoppt ihr und ergänzt den Kontext. Übernehmt nur von euch bestätigte Änderungen. Dokumentiert eine neue Entscheidung in der Entscheidungsdatei und aktualisiert den Projektstand samt nächstem Schritt. Setzt `geprueft_am` erst nach eurer inhaltlichen Prüfung auf deren tatsächliches Datum. Beginnt den nächsten Durchlauf mit den erneut eingelesenen Dateien.

## Bestand prüfen

Für die Strukturprüfung braucht ihr Python 3.10 oder neuer, ohne Zusatzpakete. Öffnet ein Terminal im Kit-Ordner und führt aus:

```sh
python3 pruefungen/pruefen.py .
python3 -B -m unittest discover -s pruefungen -p 'test_*.py' -v
```

Der erste Befehl prüft euren tatsächlichen Markdown-Bestand. Funde nennen Datei und Zeile; bei einem Fund endet er mit Exitcode 1. Der zweite Befehl testet den Prüfer an temporären Dateien. Diese Testfälle sind keine Funde in eurem Bestand. Die [Prüfanleitung](pruefungen/README.md) erklärt Umfang und Grenzen. Der Prüfer prüft die Struktur. Ob Aussagen wahr sind, müsst ihr inhaltlich prüfen. Ohne Python könnt ihr Dateiköpfe und Links manuell prüfen; das ist kein ausgeführter Skriptlauf.

## Pflege und optionales Git

Prüft den betroffenen Kontext vor jeder neuen Aufgabe und nach einer Entscheidung. Entfernt überholte Vorgaben oder kennzeichnet sie eindeutig. Im Team vereinbart ihr, wer welche Datei pflegt. Vermeidet gleichzeitiges Überschreiben derselben Datei. Legt vor größeren Änderungen eine Sicherung außerhalb des Kit-Ordners an.

Git ist optional. Es protokolliert gespeicherte Fassungen und macht Änderungen vergleichbar. Wenn ihr Git bereits nutzt, nehmt das Kit in ein passendes Repository auf, prüft die Unterschiede und commitet nur die ausgewählten Dateien. Achtet darauf, wo ein späterer Push die Inhalte veröffentlicht. Der Einstieg funktioniert auch mit lokalen Sicherungskopien.

Gebt nur Inhalte an ein Modell weiter, die ihr im gewählten Dienst verwenden dürft. Zugangsdaten gehören nicht in den Bestand. Klärt die Freigabe für vertrauliche oder personenbezogene Inhalte vor dem Einfügen.

## Quellen zum Artikel

Die im Artikel genannten Quellen, geprüft am 06.10.2026:

- Anthropic: [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 29.09.2025.
- Mitchell Hashimoto: [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey), 05.02.2026, Abschnitt „Engineer the Harness“.
- Addy Osmani: [Loop Engineering](https://addyosmani.com/blog/loop-engineering/), 07.06.2026.
- Teresa Torres im Podcast „Behind the Craft“ von Peter Yang: [Full Tutorial: Build Your Personal OS with Claude Code in 50 Min](https://creatoreconomy.so/p/automate-your-life-with-claude-code-teresa-torres), Dezember 2025, mit ihrem dreistufigen Kontextsystem.
- Teresa Torres auf Product Talk: [Conversations with Claude: Can You Conduct a Content Audit?](https://www.producttalk.org/conversations-with-claude-content-audit/), 11.03.2026.

## Lizenzvorschlag und Prüfgrenze

Für die eigens erstellten Textvorlagen wird weiterhin CC BY 4.0 vorgeschlagen. Dieser Vorschlag ist keine Lizenzfreigabe. Vor Veröffentlichung sind Rechte und endgültiger Lizenzhinweis einschließlich des Prüfskripts zu klären. Das Kit behauptet keine Freigabe durch t3n.

Die Interviews sind Arbeitsanweisungen, deren Befolgung vom verwendeten Modell abhängt. Automatische Strukturtests belegen weder fachliche Richtigkeit noch Verständlichkeit oder Modellverhalten. Das Beispiel zeigt einen erfundenen Zusammenhang; es belegt keine Nutzerwirkung.

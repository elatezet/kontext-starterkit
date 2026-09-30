# Erste Schicht

Mit diesem Starterkit haltet ihr den Kontext für eine Aufgabe in einer lesbaren Datei fest. Ihr gebt die Datei zusammen mit einem Arbeitsauftrag in einen Chat. Nachdem ihr das Ergebnis geprüft habt, speichert ihr bestätigte Änderungen zurück. Beim nächsten Gespräch beginnt ihr mit dieser aktuellen Fassung.

Ihr braucht einen Texteditor, einen Ordner für eure Dateien und ein Chatwerkzeug, in das ihr Text einfügen könnt. Markdown ist einfacher Text mit Zeichen für Überschriften und Listen. Die Dateien mit der Endung `.md` könnt ihr auch ohne besondere Markdown-App bearbeiten. Obsidian, Git und ein Terminal sind für den Einstieg nicht nötig.

## Wählt euer Anliegen

Wenn ihr die nächste Entscheidung in einem konkreten Vorhaben vorbereiten wollt, beginnt mit der [Projektvorlage](vorlagen/projekt.md). Das [fiktive Workshop-Beispiel](beispiele/projekt-workshop.md) zeigt eine ausgefüllte Fassung.

Wenn ihr eine eigene Arbeitsmethode wiederholt anwenden wollt, beginnt mit der [Fachwissensvorlage](vorlagen/fachwissen.md). Im [fiktiven Beispiel für Formulartexte](beispiele/fachwissen-formulartexte.md) stehen Maßstäbe und ein kommentierter Anwendungsfall.

Für den ersten Einsatz genügt eine dieser Vorlagen. Die Beispiele sind vollständig erfunden. Auch die dort als festgelegt bezeichneten Angaben gelten ausschließlich innerhalb der Übung.

## Von der Datei in den Chat und zurück

### 1. Legt eure Arbeitsdatei an

Kopiert die passende Vorlage im Dateimanager in euren Arbeitsordner. Nennt die Kopie etwa `mein-projekt.md` oder `mein-fachwissen.md`. Öffnet sie im Texteditor und ersetzt die Hinweise in eckigen Klammern durch eure Angaben. Speichert als einfachen Text mit der Endung `.md`. Wenn euer Editor formatierte Dokumente erstellt, wechselt zuerst in seinen Modus für reinen Text.

Schreibt bei fehlenden Angaben ausdrücklich „Offen“ oder „Ungeprüfte Annahme“. Bei Fakten nennt ihr die Herkunft, etwa eine eigene Notiz oder eine vereinbarte Vorgabe. Prüft vor dem Einfügen in einen Chat, welche Inhalte ihr mit dem gewählten Dienst teilen dürft. Für die Übung könnt ihr direkt eine Kopie eines fiktiven Beispiels verwenden.

Ihr seid für den nächsten Schritt bereit, wenn die nächste Entscheidung oder der zu prüfende Text feststeht und die offenen Angaben erkennbar sind.

### 2. Gebt Datei und Arbeitsauftrag gemeinsam weiter

Öffnet [startprompt.md](startprompt.md) und kopiert ausschließlich den Prompt für euren gewählten Einstieg. Öffnet einen neuen Chat und fügt den Prompt in das Eingabefeld ein. Ersetzt darin den Platzhalter zwischen `BEGINN KONTEXTDATEI` und `ENDE KONTEXTDATEI` durch den vollständigen Inhalt eurer Arbeitsdatei. Sendet beides als eine Nachricht.

Der Dateiname oder ein lokaler Dateipfad allein übermittelt den Inhalt nicht. Ihr müsst weder einen Ordner verbinden noch eine App einrichten. Falls euer Chatwerkzeug den Text wegen seiner Länge nicht annimmt, kürzt eure Arbeitsdatei auf die nötigen Angaben. Sendet sie dann erneut vollständig.

### 3. Prüft den Vorschlag an eurer Datei

Beim Projekt prüft ihr, ob die vorgeschlagene Handlung dem Ziel und euren Prüfmaßstäben entspricht. Jede Begründung muss zu einer konkreten Angabe passen. Bleibt eine Annahme ungeprüft, muss die Antwort diese Unsicherheit erhalten. Ein Vorschlag für ein Format ist noch keine Entscheidung von euch.

Beim Fachwissen prüft ihr jede vorgeschlagene Änderung am zugehörigen Maßstab. Vergleicht Ausgangstext und Vorschlag. Neue Aussagen über Abläufe oder Funktionen brauchen eine Quelle. Ein sprachlich passender Satz kann sachlich falsch sein. Vorschläge außerhalb eurer Methode müssen als solche erkennbar bleiben.

Wenn die Antwort etwas hinzuerfindet, verwirft ihr die betreffende Aussage. Gebt im Chat die Korrektur an und lasst nur den betroffenen Vorschlag neu formulieren. Fehlt eine entscheidende Information, klärt ihr diese zuerst. Ein Modell kann auch bei sorgfältigem Kontext Fehler machen.

### 4. Speichert nur geprüfte Änderungen zurück

Lasst euch für eine Änderung den Abschnittsnamen sowie die alte und die vorgeschlagene neue Fassung zeigen. Der Startprompt fordert das bereits an. Vergleicht den Vorschlag mit eurer lokalen Datei. Entscheidet selbst, was ihr übernehmt, und bearbeitet nur diese Stelle im Texteditor. Wenn ihr nichts bestätigen könnt, bleibt die Datei unverändert.

Speichert vor einer größeren Änderung eine Kopie, etwa `mein-projekt-vorher.md`. Haltet in der Arbeitsdatei unter „Geprüfte Änderungen“ fest, was ihr übernommen habt und warum. Eine Empfehlung des Modells wird erst durch eure Entscheidung zur Vorgabe. Eine Annahme wird erst mit einem passenden Beleg zum bestätigten Stand.

Speichert die Datei und öffnet sie erneut. Kontrolliert, ob die Änderung vorhanden ist und offene Punkte noch als offen markiert sind. Der Chat aktualisiert eure lokale Datei nicht automatisch.

### 5. Beginnt erneut mit dem aktuellen Stand

Ändert für einen zweiten Durchlauf eine relevante Vorgabe. Ihr könnt dafür die Übungsänderung am Ende des gewählten Beispiels nutzen. Speichert die Änderung und fügt die ganze aktualisierte Datei mit demselben Prompt in einen neuen Chat ein. Damit prüft ihr den aktuellen Stand ohne die alte Unterhaltung als zusätzliche Quelle.

Kontrolliert, ob die Antwort die neue Vorgabe berücksichtigt. Wenn sie noch vom alten Stand ausgeht, prüft zuerst den eingefügten Inhalt. Speichert auch nach diesem Durchlauf ausschließlich Änderungen, die ihr selbst geprüft habt.

Der erste Einsatz ist abgeschlossen, wenn ihr eine nachvollziehbare nächste Handlung oder eine begründete Textänderung beurteilen könnt. Eure Arbeitsdatei enthält danach genau den Stand, den ihr bestätigt habt. Ein ungeklärter Punkt darf offen bleiben.

## Was später hinzukommen kann

Wenn ihr mehrere Fassungen vergleichen wollt, könnt ihr später Git zur Versionsverwaltung ergänzen. Ein Agent mit Dateizugriff kann das Einlesen und das Vorschlagen von Änderungen verbinden. Dann braucht ihr einen klar begrenzten Arbeitsordner und prüft die Änderungen vor der Übernahme. Für den hier beschriebenen Ablauf genügt das Kopieren von Text.

## Grenzen des Kits

Das Paket ordnet eure Angaben und Prüfmaßstäbe. Es prüft keine externen Fakten und garantiert keine korrekten Modellantworten. Die Methode im Formularbeispiel ist für die Übung erfunden. Sie ist kein anerkannter Fachstandard. Eine Prüfung von Recht, Barrierefreiheit oder technischer Funktion ersetzt sie nicht.

Die beiden Abläufe wurden redaktionell simuliert. Ein tatsächlicher LLM-Test oder eine Nutzerstudie fand dafür nicht statt. Verständlichkeit für unerfahrene Leser, Verhalten einzelner Chatwerkzeuge und benötigte Zeit sind nicht gemessen. Der [redaktionelle Prüfbericht](redaktion/walkthrough.md) beschreibt die Prüfung und ihre Grenzen.

## Vorschlag zur Lizenz

Für die eigens erstellten Textvorlagen wird CC BY 4.0 vorgeschlagen. Die Herausgabe muss diesen Vorschlag vor Veröffentlichung bestätigen und den endgültigen Lizenzhinweis mit Urheberangabe und Lizenzverweis ergänzen. Hiermit wird noch keine Lizenzfreigabe erklärt. Fremde Texte, Bilder oder Fonts sind nicht Bestandteil des Pakets.

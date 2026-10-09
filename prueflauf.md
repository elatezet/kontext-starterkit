---
status: entwurf
geprueft_am: offen
---

# Prüflauf des Starterkits

Echte Skriptausgabe aus einer Übungskopie. Für diese Demonstration wurden das Prüfdatum entfernt und ein Dateiverweis verändert. Der Downloadbestand bleibt unverändert.

## Fehler finden

```text
beispiel/projekt.md:3: Pflichtfeld fehlt: geprueft_am
beispiel/projekt.md:27: Markdown-Ziel fehlt: entscheidung-fehlt.md
2 Fundstellen in 17 Markdown-Dateien.
```

## Angaben korrigieren und erneut prüfen

Prüfdatum und Verweis wurden in der Übungskopie auf ihren ursprünglichen Stand zurückgesetzt. Derselbe Prüfer läuft erneut:

```text
OK: 17 Markdown-Dateien geprüft; keine Strukturfehler gefunden.
```

Der Lauf prüft Metadaten und Dateiverweise. Er bestätigt weder die sachliche Richtigkeit noch eine menschliche Abnahme.

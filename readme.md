# Tankvorgänge-Verwaltungsanwendung

Die Tankvorgänge-Verwaltungsanwendung ist eine Python-Anwendung, die es Benutzern ermöglicht, Tankvorgänge für ihre Fahrzeuge zu verwalten. Die Anwendung ermöglicht das Hinzufügen neuer Fahrzeuge, das Speichern von Tankvorgängen mit Datum, Litermenge, Preis und gefahrenen Kilometern sowie das Anzeigen von Statistiken über den durchschnittlichen Verbrauch und den durchschnittlichen Kraftstoffpreis.

## Funktionalitäten

- Hinzufügen neuer Fahrzeuge mit Marke, Modell, Baujahr und Kilometerstand.
- Speichern von Tankvorgängen mit Datum, Litermenge, Preis und gefahrenen Kilometern.
- Anzeigen von Statistiken über durchschnittlichen Verbrauch und durchschnittlichen Kraftstoffpreis.
- Verwendung von SQLite-Datenbank zur Datenspeicherung.
- Benutzeroberfläche mit Hilfe von Tkinter.

## Paketstruktur

- **Model**: Enthält die Datenmodelle für die Tankvorgänge und die Datenbankzugriffsfunktionen.
- **View**: Enthält die Benutzeroberflächenklassen für die Anzeige von Tankvorgängen und das Hinzufügen neuer Fahrzeuge.
- **Controller**: Enthält die Controller-Klassen für die Logik der Anwendungssteuerung.
- **Main**: Enthält die Hauptdatei zum Starten der Anwendung.
- **App**: Enthält die App-Klasse zum Initialisieren und Starten der Anwendung.
- **Datenbank**: Enthält eine einfach SQLite3 Datenbank

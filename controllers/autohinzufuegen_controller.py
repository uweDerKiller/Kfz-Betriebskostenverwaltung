# autohinzufuegen_controller.py

from datetime import datetime
from tkinter import messagebox
import sqlite3
from models.auto import Kennzeichen


class AutoHinzufuegenController:
    def __init__(self, view):
        self.view = view

    def speichern(self, marke, modell, baujahr, kennzeichen):
        try:
            datetime.strptime(baujahr, "%Y")  # Prüfe das Datumsformat
        except ValueError:
            messagebox.showerror("Fehler", "Ungültiges Datumsformat")
            return
        kennzeichen_obj = Kennzeichen(kennzeichen)
        if not kennzeichen_obj.is_valid():
            messagebox.showerror("Fehler", "Ungültiges Kennzeichen")
            return
        # Hier könntest du weitere Validierungen für die anderen Felder durchführen

        # Hier könnten die Daten gespeichert werden (z. B. in einer Datenbank)
        # Füge deine Speicherlogik hier ein

        # Verbindung zur SQLite-Datenbank herstellen (falls die Datei nicht existiert, wird sie erstellt)
        conn = sqlite3.connect("meine_datenbank.db")

        # Erstellen eines Cursor-Objekts, um SQL-Statements auszuführen
        c = conn.cursor()

        # Erstellen einer Tabelle (wenn sie noch nicht existiert)
        c.execute(
            """CREATE TABLE IF NOT EXISTS autos
                (marke TEXT, modell TEXT, baujahr INTEGER, kennzeichen TEXT)"""
        )

        # Daten einfügen
        c.execute(
            "INSERT INTO autos (marke, modell, baujahr, kennzeichen) VALUES (?, ?, ?, ?)",
            (marke, modell, baujahr, str(kennzeichen_obj)),
        )

        # Änderungen bestätigen und die Verbindung schließen
        conn.commit()
        conn.close()

        messagebox.showinfo("Gespeichert", "Auto gespeichert")
